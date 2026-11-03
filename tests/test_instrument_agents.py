"""The generated templates and instrument agents, their generator, and the
grammar both read.

The seven templates are rendered from their sources and the shared
references, and the ``agents/<name>.md`` files from the templates, by
``tools/instrument_agents.py``; both are committed, and its check mode is
what makes drift a failing test. This module covers:

- the check and write modes, driven through the real script: clean on the
  tree, failing on a seeded source edit or a hand edit to a generated file;
- the splice, on fixture references: each include replaced by its
  section, from either shared reference, an unresolvable include refused
  (a heading held in both among them), an include inside a selector
  passage read only under its value;
- citations of shared sections: a rendered template cites, with a bare
  ``§``, only shared sections its source takes;
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
from collections import Counter
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
    passages,
    resolve,
    runtime_slots,
    selector_values,
    shared_references,
    source_path,
)

GENERATOR = REPO_ROOT / "tools" / "instrument_agents.py"
INSTRUMENTS = instruments()
TEMPLATES = sorted(INSTRUMENTS.values())
SEAT = INSTRUMENTS["redteam-seat"]
SHARED = shared_references()


def agent_file(name: str) -> str:
    return load_generator().agent_path(name)


def stale_paths(stdout: str) -> set[str]:
    """The paths a check run names as stale, one ``stale: <path>`` line each."""
    return set(re.findall(r"^stale: (\S+)", stdout, re.M))


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
    their repo-relative paths: the template sources, the shared
    references, the rendered templates and the agents, nothing else -- so a
    clean check on the copy shows the generator reads no other file."""
    sources = [source_path(t) for t in TEMPLATES]
    for rel in [*sources, *SHARED, *TEMPLATES, *map(agent_file, INSTRUMENTS)]:
        target = dest / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(REPO_ROOT / rel, target)


def _raw(rel: str) -> str:
    return (REPO_ROOT / rel).read_text("utf-8").replace("\r\n", "\n")


# --- the generator's check and write modes --------------------------------


def test_instrument_agent_check_is_clean_on_the_tree() -> None:
    """Break: a committed rendered template or agent that differs from
    what the generator writes -- hand-edited, or left stale by an edit to a
    source or a shared reference -- or an agents directory holding
    other than the generated set."""
    result = run_generator("check")
    assert (result.returncode, result.stdout, result.stderr) == (0, "", "")
    present = {p.name for p in (REPO_ROOT / "agents").iterdir()}
    assert present == {Path(agent_file(name)).name for name in INSTRUMENTS}


@pytest.mark.parametrize(
    "edited, stale",
    [
        # A source edited, in each family: its template and agent go stale.
        (
            source_path(INSTRUMENTS["blind-verifier"]),
            {INSTRUMENTS["blind-verifier"], agent_file("blind-verifier")},
        ),
        (
            source_path(INSTRUMENTS["branch-reviewer"]),
            {INSTRUMENTS["branch-reviewer"], agent_file("branch-reviewer")},
        ),
        # A hand edit to a generated file: exactly that file goes stale.
        (INSTRUMENTS["task-reviewer"], {INSTRUMENTS["task-reviewer"]}),
        (agent_file("terminal-pass"), {agent_file("terminal-pass")}),
    ],
    ids=["redteaming-source", "sdd-source", "template-hand-edit", "agent-hand-edit"],
)
def test_instrument_agent_seeded_edit_fails_the_check(
    tmp_path: Path, edited: str, stale: set[str]
) -> None:
    """Break: a source edit that the check does not see, a hand edit to a
    rendered template or an agent passing it, or a check that fails without
    naming exactly what is stale."""
    copy_generator_inputs(tmp_path)
    assert run_generator("check", "--root", str(tmp_path)).returncode == 0

    path = tmp_path / edited
    path.write_bytes(path.read_bytes() + b"\nOne more line.\n")
    result = run_generator("check", "--root", str(tmp_path))

    assert result.returncode == 1
    assert stale_paths(result.stdout) == stale


def test_instrument_agent_seeded_missing_agent_fails_the_check(
    tmp_path: Path,
) -> None:
    """Break: a deleted agent or rendered template passing the check
    (nothing to compare against)."""
    copy_generator_inputs(tmp_path)
    (tmp_path / agent_file("re-reviewer")).unlink()
    (tmp_path / INSTRUMENTS["implementer"]).unlink()
    result = run_generator("check", "--root", str(tmp_path))
    assert result.returncode == 1
    assert stale_paths(result.stdout) == {
        agent_file("re-reviewer"),
        INSTRUMENTS["implementer"],
    }


def test_instrument_agent_write_mode_regenerates_to_a_clean_check(
    tmp_path: Path,
) -> None:
    """Break: write mode leaving a stale, missing or CRLF template or agent
    behind -- the author's one step after a source edit -- or a second
    write changing anything."""
    copy_generator_inputs(tmp_path)
    shutil.rmtree(tmp_path / "agents")
    for template in TEMPLATES:
        (tmp_path / template).unlink()
    seat = tmp_path / source_path(SEAT)
    seat.write_bytes(seat.read_bytes() + b"\nOne more line.\n")

    assert run_generator("write", "--root", str(tmp_path)).returncode == 0
    assert run_generator("check", "--root", str(tmp_path)).returncode == 0
    generated = [*TEMPLATES, *map(agent_file, INSTRUMENTS)]
    for rel in generated:
        assert b"\r" not in (tmp_path / rel).read_bytes(), rel
    for rel in (SEAT, agent_file("redteam-seat")):
        assert "One more line." in (tmp_path / rel).read_text("utf-8"), rel

    before = {rel: (tmp_path / rel).read_bytes() for rel in generated}
    again = run_generator("write", "--root", str(tmp_path))
    assert (again.returncode, again.stdout) == (0, "")
    assert {rel: (tmp_path / rel).read_bytes() for rel in generated} == before


# --- the splice ------------------------------------------------------------

#: Sections appended to copies of the shipped shared references, under
#: headings no real section uses, so each expected rendering is a literal
#: and the real sources' own includes keep resolving beside them. Alpha and
#: beta go to the first reference, delta to the second. The H1 between
#: alpha and beta checks that a ``#`` heading ends a section.
_FIXTURE_SECTIONS = (
    "\n"
    "## Splice fixture alpha\n"
    "\n"
    "Alpha line one.\n"
    "\n"
    "```\n"
    "## Inside a fence, not a heading\n"
    "```\n"
    "\n"
    "### Splice fixture alpha detail\n"
    "\n"
    "Alpha detail line.\n"
    "\n"
    "\n"
    "# Splice fixture part\n"
    "\n"
    "Text under an H1, in no section.\n"
    "\n"
    "## Splice fixture beta\n"
    "\n"
    "Beta line.\n"
)
_ALPHA = (
    "## Splice fixture alpha\n"
    "\n"
    "Alpha line one.\n"
    "\n"
    "```\n"
    "## Inside a fence, not a heading\n"
    "```\n"
    "\n"
    "### Splice fixture alpha detail\n"
    "\n"
    "Alpha detail line."
)
_BETA = "## Splice fixture beta\n\nBeta line."
_SECOND_FIXTURE_SECTIONS = "\n## Splice fixture delta\n\nDelta line.\n"
_DELTA = "## Splice fixture delta\n\nDelta line."


def _seed_splice_tree(tmp_path: Path, extra: str = "", second: str = "") -> None:
    """The generator inputs under *tmp_path*, each shared reference keeping
    every real section: the first gains the alpha and beta fixtures, then
    *extra*; the second gains the delta fixture, then *second*."""
    copy_generator_inputs(tmp_path)
    first_ref, second_ref = SHARED
    appended = {
        first_ref: _FIXTURE_SECTIONS + extra,
        second_ref: _SECOND_FIXTURE_SECTIONS + second,
    }
    for rel, fixture in appended.items():
        reference = tmp_path / rel
        real = reference.read_bytes().decode("utf-8")
        assert "Splice fixture" not in real, "a real section shadows the fixture"
        reference.write_bytes((real.rstrip("\n") + "\n" + fixture).encode("utf-8"))


def _insert_after(rel: str, root: Path, anchor_line: str, new: str) -> None:
    """Insert *new* after the first line equal to *anchor_line* in *rel*
    under *root*."""
    path = root / rel
    lines = path.read_bytes().decode("utf-8").split("\n")
    at = lines.index(anchor_line) + 1
    path.write_bytes("\n".join([*lines[:at], new, *lines[at:]]).encode("utf-8"))


def test_splice_replaces_each_include_with_its_section(tmp_path: Path) -> None:
    """Break: an include left as a marker, a section cut short at its
    ``###`` subsection or at a ``##`` line inside a code fence, or run on
    into the next ``#`` or ``##`` heading, its heading dropped, a section of
    the second shared reference not spliced, or the agent rendered from
    anything but the spliced template.

    The expected text is the source's own render, whatever includes it
    already holds, with the fixture sections where the new includes sit."""
    _seed_splice_tree(tmp_path)
    assert run_generator("write", "--root", str(tmp_path)).returncode == 0
    baseline = (tmp_path / SEAT).read_text("utf-8").split("\n")
    source = source_path(SEAT)
    _insert_after(
        source,
        tmp_path,
        _raw(source).split("\n", 1)[0],
        "\n[[include Splice fixture alpha]]\n\n[[include Splice fixture beta]]"
        "\n\n[[include Splice fixture delta]]",
    )

    assert run_generator("write", "--root", str(tmp_path)).returncode == 0
    rendered = (tmp_path / SEAT).read_text("utf-8")
    expected = "\n".join(
        [baseline[0], "", _ALPHA, "", _BETA, "", _DELTA, *baseline[1:]]
    )
    assert rendered == expected
    assert _BETA in (tmp_path / agent_file("redteam-seat")).read_text("utf-8")
    assert run_generator("check", "--root", str(tmp_path)).returncode == 0


@pytest.mark.parametrize(
    "include, extra, second, named",
    [
        ("[[include Splice fixture gamma]]", "", "", "Splice fixture gamma"),
        (
            "[[include Splice fixture alpha detail]]",
            "",
            "",
            "Splice fixture alpha detail",
        ),
        ("[[include]]", "", "", "[[include]]"),
        (
            "[[include: Splice fixture alpha]]",
            "",
            "",
            "[[include: Splice fixture alpha]]",
        ),
        (
            "[[include Splice fixture beta]]",
            "\n## Splice fixture beta\n\nA second beta.\n",
            "",
            "Splice fixture beta",
        ),
        (
            "[[include Splice fixture beta]]",
            "",
            "\n## Splice fixture beta\n\nA beta in the second reference.\n",
            "Splice fixture beta",
        ),
        (
            "[[include Splice fixture beta]]",
            "[[when lane = very-small]]\n",
            "",
            "Splice fixture beta",
        ),
        (
            "[[include Splice fixture delta]]",
            "",
            "[[when lane = very-small]]\n",
            "Splice fixture delta",
        ),
    ],
    ids=["missing-heading", "subsection-heading", "no-heading", "malformed",
         "duplicate-heading", "heading-in-both-references", "marker-in-section",
         "marker-in-second-reference"],
)
def test_splice_refuses_an_include_it_cannot_resolve(
    tmp_path: Path, include: str, extra: str, second: str, named: str
) -> None:
    """Break: a source naming a heading no shared reference holds (or a
    ``###`` one, or one held twice, in one reference or across both), a
    malformed include, or a section holding a marker line rendering anyway
    -- or a failed render writing a partial tree. Both modes stop with exit
    2 and name the include."""
    _seed_splice_tree(tmp_path, extra, second)
    assert run_generator("check", "--root", str(tmp_path)).returncode == 0
    source = source_path(INSTRUMENTS["implementer"])
    _insert_after(source, tmp_path, _raw(source).split("\n", 1)[0], include)
    before = (tmp_path / INSTRUMENTS["implementer"]).read_bytes()

    for mode in ("check", "write"):
        result = run_generator(mode, "--root", str(tmp_path))
        assert result.returncode == 2, (mode, result.stdout, result.stderr)
        assert named in result.stderr and source in result.stderr, result.stderr
    assert (tmp_path / INSTRUMENTS["implementer"]).read_bytes() == before


@pytest.mark.parametrize("reference", SHARED)
def test_splice_refuses_a_missing_shared_reference(
    tmp_path: Path, reference: str
) -> None:
    """Break: a source taking a section while a shared reference is
    missing ending in a traceback, or in check mode's exit 1, which means
    "stale" -- or a failed render writing a partial tree. Both modes stop
    with exit 2 and name the reference."""
    copy_generator_inputs(tmp_path)
    (tmp_path / reference).unlink()
    outputs = [*TEMPLATES, *map(agent_file, INSTRUMENTS)]
    before = {rel: (tmp_path / rel).read_bytes() for rel in outputs}

    for mode in ("check", "write"):
        result = run_generator(mode, "--root", str(tmp_path))
        assert result.returncode == 2, (mode, result.stdout, result.stderr)
        assert reference in result.stderr, result.stderr
    assert {rel: (tmp_path / rel).read_bytes() for rel in outputs} == before


def test_splice_inside_a_selector_passage_follows_the_selector(
    tmp_path: Path,
) -> None:
    """Break: a section included inside a selector-keyed passage reaching
    the instrument under another value, or breaking the passage grammar the
    selector tests read."""
    from test_dispatch_contracts_templates import selection_leaks

    template = next(t for t in TEMPLATES if passages(_raw(t)))
    card = _raw(card_path(template))
    selector, value, _ = passages(_raw(template))[0]
    marker = f"[[when {selector} = {value}]]"
    _seed_splice_tree(tmp_path)
    _insert_after(
        source_path(template), tmp_path, marker, "[[include Splice fixture beta]]"
    )

    assert run_generator("write", "--root", str(tmp_path)).returncode == 0
    rendered = (tmp_path / template).read_text("utf-8")
    assert structure_violations(rendered, card, family(template)) == []
    assert selection_leaks(rendered, card) == []
    for candidate in selector_values(card)[selector]:
        shown = _BETA in resolve(rendered, {selector: candidate})
        assert shown == (candidate == value), candidate


# --- citations of shared sections ------------------------------------------


def taken_sections(source_text: str) -> set[str]:
    """The shared headings *source_text*, a template source, includes."""
    include = load_generator().INCLUDE_RE
    return {m.group(1) for line in source_text.split("\n") if (m := include.match(line))}


def shared_headings() -> list[tuple[str, str]]:
    """``(heading, reference)`` for each ``##`` section of every shared
    reference, in order."""
    gen = load_generator()
    return [(h, ref) for ref in SHARED for h, _ in gen.sections(_raw(ref))]


def test_shared_headings_are_unique_across_the_references() -> None:
    """Break: a ``##`` heading held twice, in one shared reference or
    across them, so an include of it fails to render and a bare ``§``
    citation of it names two sections."""
    # Consumer: the generator, which resolves an include by heading across
    # every shared reference.
    held = Counter(h for h, _ in shared_headings())
    assert [h for h, n in held.items() if n > 1] == []


def untaken_shared_citations(template_text: str, source_text: str) -> list[str]:
    """The shared references' headings that *template_text* (a rendered
    template) cites with a bare ``§`` and that its source, *source_text*,
    takes no include of.

    A bare citation names no file: a ``§`` after a ``.md`` path or a
    ``crucible:<skill>`` token cites that file, not a section of this
    template. A cited shared heading is the longest one the citation's
    text starts with, ending at a word boundary."""
    headings = sorted((h for h, _ in shared_headings()), key=len, reverse=True)
    taken = taken_sections(source_text)
    norm = re.sub(r"\s+", " ", template_text)
    out: list[str] = []
    for m in re.finditer("§", norm):
        before = norm[: m.start()].rstrip().rstrip("`")
        if before.endswith(".md") or re.search(r"crucible:[a-z0-9-]+$", before):
            continue
        tail = norm[m.end():].lstrip()
        cited = next(
            (
                h
                for h in headings
                if tail.startswith(h) and not tail[len(h) : len(h) + 1].isalnum()
            ),
            None,
        )
        if cited is not None and cited not in taken:
            out.append(cited)
    return out


@pytest.mark.parametrize("template", TEMPLATES)
def test_shared_citations_name_sections_the_template_takes(template: str) -> None:
    """Break: a rendered template citing a shared section its seat never
    receives -- the section left out of its source, or a spliced section
    pointing at a sibling the seat does not take -- so the citation names
    text the seat cannot read."""
    # Consumer: the seat, which reads a bare `§` citation as a section of
    # its own text, since its shared sections arrive spliced in.
    assert untaken_shared_citations(_raw(template), _raw(source_path(template))) == []


@pytest.mark.parametrize("reference", SHARED)
def test_shared_citation_check_fires_on_an_untaken_section(reference: str) -> None:
    """The check demonstrably fires on a bare citation of a section of
    each shared reference that the source does not take, and passes over
    one that names its file."""
    template = INSTRUMENTS["implementer"]
    source = _raw(source_path(template))
    taken = taken_sections(source)
    untaken = next(
        h for h, ref in shared_headings() if ref == reference and h not in taken
    )
    text = _raw(template)
    assert untaken_shared_citations(f"{text}\nSee § {untaken}.\n", source) == [untaken]
    cited_file = f"{text}\nSee `{reference}` § {untaken}.\n"
    assert untaken_shared_citations(cited_file, source) == []


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
#: (``[SPEC_POINTER — ...]``). A hyphenated bracketed word, such as
#: ``[NOT-A-SLOT]``, is prose; its hyphen keeps it out.
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
