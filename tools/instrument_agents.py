"""Generate the Claude Code instrument agents from their templates.

Each templated instrument's fixed text ships as a plugin agent,
``agents/<name>.md`` at the plugin root. The template is the one
hand-edited home of that text; this script renders each agent from
it and the files are committed, because the plugin loads them from the
tree. A generated agent is never edited by hand: edit the template, then
run write mode.

Rendering:

- the body is the template's fixed body -- everything after its line-1 H1
  title -- with every selector-keyed passage kept, marker lines included;
- its runtime slot is filled with the runtime name, Claude Code, and
  nothing else is added: a seat takes its tools from the host;
- the frontmatter carries ``name``, ``description`` and ``model`` only.

Usage, from the plugin root::

    python tools/instrument_agents.py write   # regenerate agents/
    python tools/instrument_agents.py check   # exit 1 naming each stale file

Stdlib only.
"""

from __future__ import annotations

import argparse
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
    """A template the generator cannot render faithfully."""


def _lf(data: bytes) -> str:
    return data.decode("utf-8").replace("\r\n", "\n")


def render(name: str, root: Path) -> str:
    """The full text of ``agents/<name>.md`` for the tree at *root*."""
    template_path = INSTRUMENTS[name]
    template = _lf((root / template_path).read_bytes())
    title, _, body = template.partition("\n")
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


def stale(root: Path) -> list[str]:
    """Agent paths under *root* that are missing or differ, byte for byte,
    from what write mode would produce."""
    out = []
    for name in INSTRUMENTS:
        path = root / agent_path(name)
        expected = render(name, root).encode("utf-8")
        if not path.is_file() or path.read_bytes() != expected:
            out.append(agent_path(name))
    return out


def write(root: Path) -> list[str]:
    """Regenerate every stale agent under *root*; return the paths written."""
    written = stale(root)
    for rel in written:
        name = Path(rel).stem
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(render(name, root).encode("utf-8"))
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
    for rel in found:
        print(f"stale: {rel} (run: python tools/instrument_agents.py write)")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main())
