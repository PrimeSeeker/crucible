"""Render the seat templates from their sources, and the Claude Code
instrument agents from the templates.

Each templated instrument's fixed text has one hand-edited source,
``<template stem>.source.md`` beside the template it renders
(``implementer-prompt.md`` from ``implementer-prompt.source.md``), and may
take sections of the shared seat reference,
``skills/subagent-driven-development/references/seat-rules.md``. This
script splices the sections each source names into it and writes the
result as the template, at the path every host's dispatch reads; from each
template it renders the Claude Code agent, ``agents/<name>.md`` at the
plugin root. Templates and agents are committed, because the hosts load
them from the tree, and neither is ever edited by hand: edit the source or
the shared seat reference, then run write mode. Check mode fails on any
template or agent that write mode would change.

The splice:

- an include is a source line reading exactly ``[[include <heading>]]``,
  naming a ``##`` heading of the shared seat reference by its exact text;
- the line is replaced by that section as it stands: its heading line and
  everything up to the next ``#`` or ``##`` heading outside a code fence
  (``###`` subsections included), trailing blank lines dropped, so the
  section keeps its heading in the template;
- a heading the reference lacks or holds twice fails rendering, and so
  does any other source line opening ``[[include``;
- a spliced section is plain text: a line in it opening ``[[`` fails
  rendering, so includes never nest and a section never opens or closes a
  selector passage;
- an include inside a selector passage puts the section inside that
  passage, so the instrument reads it only where its card selects it;
- the splice copies text and fills nothing: the runtime slot is filled
  afterwards, in the agent only, and dispatch-time slots live on the card,
  so a section carries no slot token (the structure tests fail a template
  or agent holding one out of place). A value that differs by seat, such
  as a scratch path, stays in the template's own text beside the include,
  or the section splits.

Rendering an agent:

- the body is the template's fixed body -- everything after its line-1 H1
  title -- with every selector-keyed passage kept, marker lines included;
- its runtime slot is filled with the runtime name, Claude Code, and
  nothing else is added: a seat takes its tools from the host;
- the frontmatter carries ``name``, ``description`` and ``model`` only.

Usage, from the plugin root::

    python tools/instrument_agents.py write   # regenerate templates and agents/
    python tools/instrument_agents.py check   # exit 1 naming each stale file

Either mode exits 2, writing nothing, when a source cannot be rendered.
Stdlib only.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

#: Instrument agent name -> its template. The one list of the
#: seven; the tests import it.
INSTRUMENTS: dict[str, str] = {
    "redteam-seat": "skills/redteaming/seat-prompt.md",
    "blind-verifier": "skills/redteaming/verifier-prompt.md",
    "terminal-pass": "skills/redteaming/terminal-pass-prompt.md",
    "implementer": "skills/subagent-driven-development/implementer-prompt.md",
    "task-reviewer": "skills/subagent-driven-development/task-reviewer-prompt.md",
    "re-reviewer": "skills/subagent-driven-development/re-review-prompt.md",
    "branch-reviewer": "skills/requesting-code-review/code-reviewer.md",
}

#: The shared seat reference, whose ``##`` sections a source may take.
SHARED_REFERENCE = "skills/subagent-driven-development/references/seat-rules.md"

#: A template's source is its path with this suffix for ``.md``.
SOURCE_SUFFIX = ".source.md"

#: An include line, holding the heading it names.
INCLUDE_RE = re.compile(r"^\[\[include (\S(?:.*\S)?)\]\]$")


def source_path(template: str) -> str:
    """The hand-edited source *template* is rendered from, beside it."""
    return template[: -len(".md")] + SOURCE_SUFFIX


#: Each instrument's model role as a Claude Code alias: the bounded role
#: for the blind verifier, the default role for the rest. Beside the host
#: map's Model roles entry, this is the one shipped site naming this host's
#: models; an alias tracks its model line, so it changes only when a role
#: moves to a new line. A dispatch still names its model every time and
#: wins; this only catches a forgotten one.
MODELS: dict[str, str] = {name: "opus" for name in INSTRUMENTS}
MODELS["blind-verifier"] = "sonnet"

#: A few words on what each instrument is, for the host's agent listing.
ROLES: dict[str, str] = {
    "redteam-seat": "a redteam panel seat",
    "blind-verifier": "the blind verifier of a redteam fix wave",
    "terminal-pass": "the terminal pass that closes a redteam phase",
    "implementer": "the implementer of a planned task or a fix wave",
    "task-reviewer": "the reviewer of one implemented task",
    "re-reviewer": "the scoped re-reviewer of a fix wave",
    "branch-reviewer": "the whole-branch reviewer before merge",
}

#: Dispatch-only, and discouraging the host from choosing the
#: agent for general work. Kept a YAML plain scalar: no ": " and no " #".
DESCRIPTION = (
    "Crucible instrument ({role}), dispatched only by a crucible controller "
    "with a filled slot card. Never select it for general work."
)

#: The runtime the agents are generated for.
RUNTIME = "Claude Code"

#: Each family's runtime slot, as its templates spell it: the runtime
#: name. Every other token is a dispatch-time slot, which lives on the card.
RUNTIME_SLOTS: dict[str, tuple[str, ...]] = {
    "redteaming": ("{runtime}",),
    "sdd": ("[RUNTIME]",),
}


class TemplateError(ValueError):
    """A source or template the generator cannot render faithfully."""


def _lf(data: bytes) -> str:
    return data.decode("utf-8").replace("\r\n", "\n")


def sections(reference: str) -> list[tuple[str, list[str]]]:
    """``(heading, lines)`` for each ``##`` section of *reference*, in
    order: the heading line through the line before the next ``#`` or
    ``##`` heading outside a code fence, trailing blank lines dropped."""
    found: list[tuple[str, list[str]]] = []
    current: list[str] | None = None
    fenced = False
    for line in reference.split("\n"):
        if line.startswith("```"):
            fenced = not fenced
        if not fenced and line.startswith(("# ", "## ")):
            current = None
            if line.startswith("## "):
                current = []
                found.append((line[3:].strip(), current))
        if current is not None:
            current.append(line)
    for _, lines in found:
        while lines and not lines[-1].strip():
            lines.pop()
    return found


def render_template(template: str, root: Path) -> str:
    """The full text of *template* for the tree at *root*: its source with
    every include replaced by the section it names."""
    source = source_path(template)
    path = root / source
    if not path.is_file():
        raise TemplateError(f"{template}: no source {source}")
    found: list[tuple[str, list[str]]] | None = None
    out: list[str] = []
    for line in _lf(path.read_bytes()).split("\n"):
        if not line.startswith("[[include"):
            out.append(line)
            continue
        m = INCLUDE_RE.match(line)
        if not m:
            raise TemplateError(f"{source}: malformed include line {line!r}")
        if found is None:
            found = sections(_lf((root / SHARED_REFERENCE).read_bytes()))
        held = [lines for heading, lines in found if heading == m.group(1)]
        if len(held) != 1:
            why = "no such '## ' heading" if not held else "a heading held twice"
            raise TemplateError(f"{source}: {line!r}: {why} in {SHARED_REFERENCE}")
        for spliced in held[0]:
            if spliced.startswith("[["):
                raise TemplateError(
                    f"{source}: {line!r}: the section holds a marker line "
                    f"{spliced!r} in {SHARED_REFERENCE}"
                )
        out.extend(held[0])
    return "\n".join(out)


def render(name: str, root: Path, template_text: str | None = None) -> str:
    """The full text of ``agents/<name>.md`` for the tree at *root*,
    rendered from *template_text*, or from the rendered template."""
    template_path = INSTRUMENTS[name]
    if template_text is None:
        template_text = render_template(template_path, root)
    title, _, body = template_text.partition("\n")
    if not title.startswith("# "):
        raise TemplateError(f"{template_path}: line 1 is not an H1 title")

    families = [
        slots for slots in RUNTIME_SLOTS.values() if all(s in body for s in slots)
    ]
    if len(families) != 1:
        raise TemplateError(
            f"{template_path}: does not hold exactly one family's runtime slots"
        )
    for slot in families[0]:
        body = body.replace(slot, RUNTIME)

    frontmatter = "\n".join(
        [
            "---",
            f"name: {name}",
            f"description: {DESCRIPTION.format(role=ROLES[name])}",
            f"model: {MODELS[name]}",
            "---",
        ]
    )
    notice = (
        f"<!-- Generated from {template_path} by tools/instrument_agents.py; "
        "do not edit by hand. -->"
    )
    return f"{frontmatter}\n\n{notice}\n\n{body.strip(chr(10))}\n"


def agent_path(name: str) -> str:
    """Where *name*'s agent lives, relative to the plugin root."""
    return f"agents/{name}.md"


def expected(root: Path) -> dict[str, bytes]:
    """Every generated file under *root*, template then agent per
    instrument, as write mode would produce it."""
    out: dict[str, bytes] = {}
    for name, template in INSTRUMENTS.items():
        text = render_template(template, root)
        out[template] = text.encode("utf-8")
        out[agent_path(name)] = render(name, root, text).encode("utf-8")
    return out


def stale(root: Path) -> list[str]:
    """Generated paths under *root* that are missing or differ, byte for
    byte, from what write mode would produce."""
    return [
        rel
        for rel, data in expected(root).items()
        if not (root / rel).is_file() or (root / rel).read_bytes() != data
    ]


def write(root: Path) -> list[str]:
    """Regenerate every stale file under *root*; return the paths written.
    Renders everything before writing anything."""
    files = expected(root)
    written = [
        rel
        for rel, data in files.items()
        if not (root / rel).is_file() or (root / rel).read_bytes() != data
    ]
    for rel in written:
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(files[rel])
    return written


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("mode", choices=("write", "check"))
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="plugin root (default: this checkout)",
    )
    args = parser.parse_args(argv)
    try:
        if args.mode == "write":
            for rel in write(args.root):
                print(f"wrote {rel}")
            return 0
        found = stale(args.root)
    except TemplateError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    run = "python tools/instrument_agents.py write"
    for rel in found:
        if rel.startswith("agents/"):
            print(f"stale: {rel} (run: {run})")
        else:
            print(
                f"stale: {rel} (rendered from {source_path(rel)}: edit the "
                f"source, not the template, then run: {run})"
            )
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main())
