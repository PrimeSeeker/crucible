"""The generated instrument agents, their generator, and the grammar both
read.

The ``agents/<name>.md`` files are generated from the templates by
``tools/instrument_agents.py`` and committed; its check mode is what makes
drift a failing test. This module covers:

- the check and write modes, driven through the real script: clean on the
  tree, failing on a seeded template edit;
- the render itself, re-derived here: each agent is its template's body
  with the runtime slot filled, nothing left unfilled and nothing added;
- the frontmatter, parsed the strict way the host's loader needs it;
- the one structure test over every instrument: each slot card and
  template conforms to the card and passage grammars (sections, slot
  lines, keyed passages, runtime slots only in the template body).

The instrument list and the runtime slots come from the generator; no
template wording is pinned. Nothing here launches a model or the host CLI.
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from instrument_corpus import (
    CARD_BUDGET,
    CARD_SECTIONS,
    CARD_SLOT_RE,
    MARKER_END,
    MARKER_OPEN_RE,
    REPO_ROOT,
    SLOT_TOKEN,
    card_path,
    card_sections,
    card_selectors,
    family,
    instruments,
    load_generator,
    runtime_slots,
    selector_values,
)

GENERATOR = REPO_ROOT / "tools" / "instrument_agents.py"
INSTRUMENTS = instruments()
TEMPLATES = sorted(INSTRUMENTS.values())
SEAT = INSTRUMENTS["redteam-seat"]


def agent_file(name: str) -> str:
    return load_generator().agent_path(name)


def run_generator(*args: str) -> subprocess.CompletedProcess[str]:
    """The generator as an author or CI runs it: a separate process."""
    return subprocess.run(
        [sys.executable, str(GENERATOR), *args],
        stdin=subprocess.DEVNULL,  # an inherited stdin can be an invalid handle
        capture_output=True,
        text=True,
        encoding="utf-8",
        cwd=REPO_ROOT,
        check=False,
    )


def copy_generator_inputs(dest: Path) -> None:
    """The files the generator reads and writes, copied under *dest* at
    their repo-relative paths: the templates and the agents, nothing else --
    so a clean check on the copy shows the generator reads no other file."""
    for rel in [*TEMPLATES, *map(agent_file, INSTRUMENTS)]:
        target = dest / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(REPO_ROOT / rel, target)


def _raw(rel: str) -> str:
    return (REPO_ROOT / rel).read_text("utf-8").replace("\r\n", "\n")


# --- the generator's check and write modes --------------------------------


def test_instrument_agent_check_is_clean_on_the_tree() -> None:
    """Break: a committed agent that differs from what the generator
    writes -- hand-edited, or left stale by a template edit -- or an
    agents directory holding other than the generated set."""
    result = run_generator("check")
    assert (result.returncode, result.stdout, result.stderr) == (0, "", "")
    present = {p.name for p in (REPO_ROOT / "agents").iterdir()}
    assert present == {Path(agent_file(name)).name for name in INSTRUMENTS}


@pytest.mark.parametrize(
    "edited, stale",
    [
        # One template edited, in each family: exactly its agent goes stale.
        (INSTRUMENTS["blind-verifier"], {"blind-verifier"}),
        (INSTRUMENTS["branch-reviewer"], {"branch-reviewer"}),
    ],
    ids=["redteaming-template", "sdd-template"],
)
def test_instrument_agent_seeded_edit_fails_the_check(
    tmp_path: Path, edited: str, stale: set[str]
) -> None:
    """Break: a template edit that the check does not see, or a check that
    fails without naming what is stale."""
    copy_generator_inputs(tmp_path)
    assert run_generator("check", "--root", str(tmp_path)).returncode == 0

    path = tmp_path / edited
    path.write_bytes(path.read_bytes() + b"\nOne more line.\n")
    result = run_generator("check", "--root", str(tmp_path))

    assert result.returncode == 1
    named = set(re.findall(r"agents/[a-z-]+\.md", result.stdout))
    assert named == {agent_file(name) for name in stale}


def test_instrument_agent_seeded_missing_agent_fails_the_check(
    tmp_path: Path,
) -> None:
    """Break: a deleted agent passing the check (nothing to compare against)."""
    copy_generator_inputs(tmp_path)
    (tmp_path / agent_file("re-reviewer")).unlink()
    result = run_generator("check", "--root", str(tmp_path))
    assert result.returncode == 1
    assert set(re.findall(r"agents/[a-z-]+\.md", result.stdout)) == {
        agent_file("re-reviewer")
    }


def test_instrument_agent_write_mode_regenerates_to_a_clean_check(
    tmp_path: Path,
) -> None:
    """Break: write mode leaving a stale, missing or CRLF agent behind --
    the author's one step after a template edit."""
    copy_generator_inputs(tmp_path)
    shutil.rmtree(tmp_path / "agents")
    seat = tmp_path / SEAT
    seat.write_bytes(seat.read_bytes() + b"\nOne more line.\n")

    assert run_generator("write", "--root", str(tmp_path)).returncode == 0
    assert run_generator("check", "--root", str(tmp_path)).returncode == 0
    for name in INSTRUMENTS:
        assert b"\r" not in (tmp_path / agent_file(name)).read_bytes(), name
    assert "One more line." in (tmp_path / agent_file("redteam-seat")).read_text(
        "utf-8"
    )


# --- the render, re-derived ------------------------------------------------


@pytest.mark.parametrize("name", sorted(INSTRUMENTS))
def test_instrument_agent_carries_its_template_body_with_runtime_filled(
    name: str,
) -> None:
    """Break: an agent whose body is not its template's fixed body -- the
    H1 title kept, a selector-keyed passage dropped or its marker stripped,
    a runtime slot filled with anything but the runtime name, or any text
    (an adapter reference, say) added between the notice and the body.

    The expected body is built here by plain string replacement on the
    template's lines after its title -- never by calling the generator's
    render.
    """
    gen = load_generator()
    title, body = _raw(INSTRUMENTS[name]).split("\n", 1)
    for slot in gen.RUNTIME_SLOTS[family(INSTRUMENTS[name])]:
        body = body.replace(slot, gen.RUNTIME)

    agent = _raw(agent_file(name))
    # Frontmatter, one notice line, then the body and nothing else.
    head, closing, after = agent.partition("\n---\n\n")
    assert head.startswith("---\n") and closing
    notice, gap, rest = after.partition("\n\n")
    assert gap and notice.startswith("<!--") and notice.endswith("-->")
    assert "\n" not in notice
    assert rest == body.strip("\n") + "\n"
    assert title not in agent  # controller-facing name, not instrument text
    markers = re.findall(r"^\[\[when [a-z0-9-]+ = [a-z0-9-]+\]\]$", body, re.M)
    assert re.findall(r"^\[\[when [a-z0-9-]+ = [a-z0-9-]+\]\]$", agent, re.M) == (
        markers
    )


@pytest.mark.parametrize("name", sorted(INSTRUMENTS))
def test_instrument_agent_leaves_no_runtime_slot_unfilled(name: str) -> None:
    """Break: the generator leaving a runtime slot token (a literal
    ``{runtime}`` or ``[RUNTIME]``) in the agent."""
    agent = _raw(agent_file(name))
    for slots in load_generator().RUNTIME_SLOTS.values():
        for slot in slots:
            assert slot not in agent, slot


# --- frontmatter -----------------------------------------------------------

#: A frontmatter line: ``key: value``, one space after the colon.
_FM_LINE = re.compile(r"^([A-Za-z][A-Za-z0-9_-]*): (\S.*)$")
#: Characters that may not open a YAML plain scalar (block context).
_YAML_INDICATORS = set("-?:,[]{}#&*!|>'\"%@`")


def parse_frontmatter(text: str) -> dict[str, str]:
    """The ``---``-fenced frontmatter of *text* as ``{key: value}``.

    A strict subset of YAML: one ``key: plain-scalar`` per line, no
    repeats, no flow collections, quotes, comments or block scalars, and
    no ``": "`` or ``" #"`` inside a value -- everything a loader could
    read two ways is refused rather than guessed at. Raises ``ValueError``
    on anything outside it. Stdlib only: the host CLI passed malformed
    frontmatter, so the suite parses it itself.
    """
    lines = text.split("\n")
    if lines[0] != "---":
        raise ValueError("no opening --- delimiter on line 1")
    try:
        end = lines.index("---", 1)
    except ValueError:
        raise ValueError("no closing --- delimiter") from None
    fields: dict[str, str] = {}
    for line in lines[1:end]:
        m = _FM_LINE.match(line)
        if not m:
            raise ValueError(f"not a key: value line: {line!r}")
        key, value = m.groups()
        if key in fields:
            raise ValueError(f"repeated key {key!r}")
        if value[0] in _YAML_INDICATORS:
            raise ValueError(f"{key}: value opens with an indicator: {value!r}")
        if ": " in value or " #" in value or value.endswith((":", " ")):
            raise ValueError(f"{key}: value is not a plain scalar: {value!r}")
        fields[key] = value
    return fields


@pytest.mark.parametrize("name", sorted(INSTRUMENTS))
def test_instrument_agent_frontmatter_parses_with_its_fields(name: str) -> None:
    """Break: frontmatter the loader could misread, a ``name`` the loader
    would expose as another instrument, a model other than the generator's
    policy default, or a restricting key (tools, disallowedTools,
    omitClaudeMd, skills), which no generated agent carries."""
    # Consumer: the host's plugin agent loader reads this frontmatter; it
    # exposes the agent as `crucible:<name>` and runs it on `model`.
    fields = parse_frontmatter(_raw(agent_file(name)))
    assert set(fields) == {"name", "description", "model"}
    assert fields["name"] == name
    assert fields["model"] == load_generator().MODELS[name]


@pytest.mark.parametrize(
    "text",
    [
        "name: x\n---\n",  # no opening delimiter
        "---\nname: x\nmodel: opus\n",  # no closing delimiter
        "---\nname: x\ntools: [Read\n---\n",  # unclosed flow sequence
        "---\nname: x\nname: y\n---\n",  # repeated key
        "---\ndescription: dispatch: only\n---\n",  # a second mapping colon
        "---\ndescription: 'quoted\n---\n",  # an unclosed quote
        "---\n  name: x\n---\n",  # indented, so not a top-level key
    ],
)
def test_instrument_agent_seeded_bad_frontmatter_is_refused(text: str) -> None:
    """The parse check demonstrably fires on the shapes the host CLI was
    measured to pass or only warn on."""
    with pytest.raises(ValueError):
        parse_frontmatter(text)


# --- the one structure test over every instrument -------------------------

#: Conditional prose not keyed by a passage marker: the pre-split inline
#: forms (``{only for right-sizing seats:}``, ``[if ... ]``, ``{when ...}``).
_UNKEYED_CONDITIONAL = re.compile(
    r"[\[{]\s*(?:only|when|if|unless|omit)\b[^\]}\n]*[\]}]", re.I
)
_CODE_SPAN = re.compile(r"`[^`\n]*`")
#: A dispatch-time slot token as the SDD family spells one in a prompt,
#: bare (``[REPORT_FILE]``) or carrying an inline fill rule
#: (``[SPEC_POINTER — ...]``). ``[LOAD-BEARING]`` is prose; its hyphen
#: keeps it out.
_SDD_BODY_SLOT_RE = re.compile(r"\[[A-Z][A-Z0-9_]*(?=\]| —)")


def body_slot_tokens(body: str, fam: str) -> set[str]:
    """Slot tokens *body* holds, spelled as family *fam* spells them."""
    if fam == "redteaming":
        return set(re.findall(r"\{[^{}\n]+\}", body))
    return {token + "]" for token in _SDD_BODY_SLOT_RE.findall(body)}


def card_slot_tokens(card: str) -> list[str]:
    """The slot tokens *card* declares under ``## Slots``."""
    return [
        m.group(1)
        for line in card_sections(card).get("## Slots", [])
        if (m := CARD_SLOT_RE.match(line))
    ]


def structure_violations(template: str, card: str, fam: str) -> list[str]:
    """Every way *template* (raw) and its slot *card* (raw) break the card
    grammar, the passage grammar, or the runtime-slot rule, as messages;
    empty when they conform.

    Structure only: the headings, line shapes and markers checked here are
    the grammar the generator and the passage resolution read, never a
    sentence of either file.
    """
    out: list[str] = []
    runtime = frozenset(load_generator().RUNTIME_SLOTS[fam])

    # The card: within budget, its three sections in order, each slot line
    # in the family's spelling, each selector with one sub-bullet per value.
    if len(card) > CARD_BUDGET:
        out.append(f"card is {len(card)} chars, over {CARD_BUDGET}")
    headings = tuple(line for line in card.split("\n") if line.startswith("## "))
    if headings != CARD_SECTIONS:
        out.append(f"card sections {headings}")
    sections = card_sections(card)
    own = re.compile(rf"^- {SLOT_TOKEN[fam]}: ")
    for line in sections.get("## Slots", []):
        if not (CARD_SLOT_RE.match(line) and own.match(line)):
            out.append(f"card slot line {line!r}")
    try:
        selectors = card_selectors(card)
    except AssertionError as exc:
        out.append(f"card selector grammar: {exc}")
        selectors = {}
    declared = selector_values(card)
    for name, values in declared.items():
        if tuple(selectors.get(name, {})) != values:
            out.append(f"selector {name}: one sub-bullet per value, in order")
    if not declared and sections.get("## Selectors") != ["none"]:
        out.append("selectors: neither declared nor none")
    if not sections.get("## Dispatch"):
        out.append("dispatch: section empty")

    # The template: an H1 title, then a body holding its family's
    # runtime slots and no dispatch-time slot (those live on the card).
    title, _, body = template.partition("\n")
    if not (title.startswith("# ") and not title.startswith("## ")):
        out.append(f"line 1 is not an H1 title: {title!r}")
    tokens = body_slot_tokens(body, fam)
    for token in sorted(tokens - runtime):
        out.append(f"dispatch-time slot in template: {token}")
    for token in sorted(runtime - tokens):
        out.append(f"runtime slot missing from template: {token}")
    for token in card_slot_tokens(card):
        if token in body:
            out.append(f"card slot in template: {token}")

    # The passages: every conditional keyed by a declared selector value
    # other than `off`, closed, never nested; every other value keys one.
    picked: set[tuple[str, str]] = set()
    open_: tuple[str, str] | None = None
    for line in body.split("\n"):
        m = MARKER_OPEN_RE.match(line)
        if m:
            if open_ is not None:
                out.append(f"nested passage at {line!r}")
            open_ = (m.group(1), m.group(2))
            if open_[1] == "off" or open_[1] not in declared.get(open_[0], ()):
                out.append(f"unkeyed conditional: {line!r} names no declared value")
            picked.add(open_)
            continue
        if line == MARKER_END:
            if open_ is None:
                out.append("[[end]] with no open passage")
            open_ = None
            continue
        prose = _CODE_SPAN.sub("", line)
        if "[[" in prose or "]]" in prose:
            out.append(f"malformed passage marker: {line!r}")
        for hit in _UNKEYED_CONDITIONAL.findall(prose):
            out.append(f"unkeyed conditional: {hit!r}")
    if open_ is not None:
        out.append(f"unclosed passage {open_}")
    for name, values in declared.items():
        for value in values:
            if value != "off" and (name, value) not in picked:
                out.append(f"selector {name} = {value} picks no passage")
    return out


@pytest.mark.parametrize("template", TEMPLATES)
def test_instrument_agent_structure_holds_for_every_instrument(template: str) -> None:
    """Break: over every instrument -- a card over budget or out of its
    grammar; a template keeping a dispatch-time slot, a card slot, or a
    conditional passage no declared selector value keys."""
    assert (
        structure_violations(_raw(template), _raw(card_path(template)), family(template))
        == []
    )


def _seed(template: str, *, body: str = "", card: tuple[str, str] | None = None):
    """*template* and its card, with *body* appended to the template and,
    for *card* = ``(pattern, new)``, the card's first match of *pattern*
    (multiline) replaced by *new*. Seeds are structural: nothing here
    depends on a sentence of the shipped files."""
    text = _raw(template) + body
    card_text = _raw(card_path(template))
    if card is not None:
        pattern, new = card
        seeded = re.sub(pattern, new, card_text, count=1, flags=re.M)
        assert seeded != card_text, pattern
        card_text = seeded
    return text, card_text, family(template)


def _a_card_slot(template: str) -> str:
    return card_slot_tokens(_raw(card_path(template)))[0]


_WITH_SELECTORS = [t for t in TEMPLATES if selector_values(_raw(card_path(t)))]


@pytest.mark.parametrize(
    "seed, expected",
    [
        # A dispatch-time slot back in a template, each family.
        (lambda: _seed(SEAT, body=f"\n{_a_card_slot(SEAT)}\n"),
         "dispatch-time slot in template"),
        (lambda: _seed(INSTRUMENTS["implementer"],
                       body=f"\n{_a_card_slot(INSTRUMENTS['implementer'])}\n"),
         "dispatch-time slot in template"),
        # An unkeyed conditional: the pre-split inline forms, and a marker
        # keyed by a value the card never declares.
        (lambda: _seed(INSTRUMENTS["blind-verifier"], body="\n{only with input 3:}\n"),
         "unkeyed conditional: '{only with input 3:}'"),
        (lambda: _seed(INSTRUMENTS["task-reviewer"],
                       body="\n[if the lane is very small: skip this]\n"),
         "unkeyed conditional: '[if the lane is very small: skip this]'"),
        (lambda: _seed(
            _WITH_SELECTORS[0],
            body="\n[[when "
            + next(iter(selector_values(_raw(card_path(_WITH_SELECTORS[0])))))
            + " = undeclared]]\nx\n[[end]]\n",
        ), "names no declared value"),
        # A runtime slot dropped from a template.
        (lambda: (
            _raw(SEAT).replace(sorted(runtime_slots(SEAT))[0], "x"),
            _raw(card_path(SEAT)),
            family(SEAT),
        ), "runtime slot missing from template"),
        # A card over its budget, or out of its grammar.
        (lambda: _seed(INSTRUMENTS["terminal-pass"],
                       card=(r"^## Dispatch$", "## Dispatch\n\n" + "x" * CARD_BUDGET)),
         f"over {CARD_BUDGET}"),
        (lambda: _seed(INSTRUMENTS["branch-reviewer"], card=(r"^  - off: .*\n", "")),
         "one sub-bullet per value, in order"),
        (lambda: _seed(SEAT, card=(r"^## Selectors$", "## Dispatch parameters")),
         "card sections"),
    ],
    ids=["rt-slot", "sdd-slot", "inline-brace", "inline-bracket", "undeclared-value",
         "runtime-slot-missing", "card-budget", "sub-bullet", "card-sections"],
)
def test_instrument_agent_seeded_structure_violation_is_caught(
    seed, expected: str
) -> None:
    """The structure test demonstrably fires on each break it names."""
    violations = structure_violations(*seed())
    assert any(expected in v for v in violations), violations
