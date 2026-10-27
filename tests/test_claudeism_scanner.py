"""Claude-ism scanner corpus suite.

The scanner under test is ``tests/claudeism_scanner.py``; its shipped
allowlist is ``tests/claudeism-allowlist.txt``. Everything here is
corpus-driven: each case names the break it catches.

Scan corpus (enforced by ``collect_sources``): every ``.md`` under
``skills/`` and ``hooks/``, plus the repository ``README.md``, plus the
SessionStart hook script ``hooks/session-start``, read as a source file.
``docs/`` is excluded -- specs and plans quote Claude-isms deliberately.

The live-tree gate (zero unallowlisted matches over the finished tree) is
``tests/test_acceptance_gate.py``'s, not this file's. What this file gates
is the instrument -- detection, the allowlist grammar, and the scan
corpus.
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
TESTS_DIR = Path(__file__).resolve().parent
CORPUS = TESTS_DIR / "claudeism_scanner_corpus"
PRE_ADAPTATION = CORPUS / "pre-adaptation-bf4b26c"

sys.path.insert(0, str(TESTS_DIR))

import claudeism_scanner as cs  # noqa: E402  (path inserted above; not a package)

# --- corpus helpers ------------------------------------------------------

# The pre-adaptation copies stand for their pre-adaptation repository
# paths, so their original line numbers (35, 66, 103, 12) are assertable.
REVIEW_SKILL = "skills/requesting-code-review/SKILL.md"
REVIEWER = "skills/requesting-code-review/code-reviewer.md"
SDD_SKILL = "skills/subagent-driven-development/SKILL.md"


def _pre_adaptation(location: str) -> str:
    return (PRE_ADAPTATION / location).read_text(encoding="utf-8")


def _scan_corpus_file(relpath: str, location: str | None = None) -> list[cs.Match]:
    text = (CORPUS / relpath).read_text(encoding="utf-8")
    return cs.find_matches(text, location or f"corpus/{relpath}")


def _terms(matches: list[cs.Match]) -> Counter:
    return Counter(m.term for m in matches)


# --- happy path: the four pre-adaptation positives -----------------------


@pytest.mark.parametrize(
    "location, line, script",
    [
        (REVIEW_SKILL, 35, "review-package"),
        (SDD_SKILL, 66, "task-brief"),
        (SDD_SKILL, 103, "review-package"),
    ],
)
def test_pre_adaptation_bash_entrypoint_positive(location, line, script):
    """Break: the shell-only entrypoint construction stops being a term.

    Each of these three lines is a ``bash <plugin-root>/.../scripts/<name>``
    core-coordination entrypoint as it stood before adaptation. A term list
    that no longer covers the construction lets it back into shared text.
    """
    matches = cs.find_matches(_pre_adaptation(location), location)
    hits = [
        m
        for m in matches
        if m.term == "bash-script-entrypoint" and m.line == line
    ]
    assert len(hits) == 1, f"expected one entrypoint hit at {location}:{line}"
    assert script in hits[0].text


def test_pre_adaptation_subagent_general_purpose_positive():
    """Break: ``Subagent (general-purpose)`` stops being a term.

    Shared text must not carry it; before adaptation it opened the branch
    reviewer's dispatch block on line 12.
    """
    matches = cs.find_matches(_pre_adaptation(REVIEWER), REVIEWER)
    hits = [m for m in matches if m.term == "subagent-general-purpose"]
    assert [m.line for m in hits] == [12]


def test_positives_survive_per_term_allowlisting_of_the_same_files():
    """Break: allowlisting is widened from per-term to whole-file.

    Every one of the three captured files also carries model-policy prose
    that names models. With every model term allowed at all
    three locations the four positives must still be reported -- a
    whole-file entry would swallow them, which is why the grammar forbids
    one.
    """
    rows = [
        f"2 | {term} | {location} | model-policy prose in this file"
        for location in (REVIEW_SKILL, REVIEWER, SDD_SKILL)
        for term in ("opus", "sonnet", "haiku", "fable")
    ]
    allowlist = cs.parse_allowlist("\n".join(rows))

    sources = {
        location: _pre_adaptation(location)
        for location in (REVIEW_SKILL, REVIEWER, SDD_SKILL)
    }
    reported = cs.unallowlisted(cs.scan_sources(sources), allowlist)

    positives = {
        (m.location, m.line)
        for m in reported
        if m.term in ("bash-script-entrypoint", "subagent-general-purpose")
    }
    assert positives == {
        (REVIEW_SKILL, 35),
        (SDD_SKILL, 66),
        (SDD_SKILL, 103),
        (REVIEWER, 12),
    }


# --- edge cases ----------------------------------------------------------


def test_one_response_parallelism_detected():
    """Break: the replaced parallelism claim is not a term.

    Both the pre-adaptation spelling and a reworded variant must match;
    the independence property that replaces it must not.
    """
    matches = _scan_corpus_file("edge/one-response-parallelism.md")
    hits = [m for m in matches if m.term == "one-response-parallelism"]
    assert [m.line for m in hits] == [3, 5]
    assert _terms(matches)["one-response-parallelism"] == 2
    assert len(matches) == 2, "the independence property must not match"


def test_bare_provider_nouns_detected():
    """Break: a bare provider noun stops being reportable on its own."""
    assert _terms(_scan_corpus_file("edge/bare-provider-nouns.md")) == Counter(
        {
            "claude-code": 1,
            "anthropic": 1,
            "claude-md": 1,
            "claude-home-path": 1,
            "claude-plugin-root": 1,
        }
    )


def test_sentence_initial_case_variants_detected():
    """Break: matching becomes case-sensitive.

    Each term appears twice -- once mid-sentence in its lowercase form and
    once capitalised at the start of a sentence.
    """
    assert _terms(_scan_corpus_file("edge/sentence-initial-case.md")) == Counter(
        {"claude-ai": 2, "anthropic": 2, "opus": 2}
    )


def test_codex_model_names_detected():
    """Break: a Codex model name stops being a term, or the generic slug
    pattern stops catching a Codex line no term names yet.

    A Codex slug is one hit, not a slug hit plus a bare-name hit inside it.
    """
    matches = _scan_corpus_file("edge/codex-model-names.md")
    assert [(m.term, m.line, m.text) for m in matches] == [
        ("codex-model-slug", 3, "gpt-6.1-sol"),
        ("codex-model-slug", 3, "GPT-6-Astra"),
        ("codex-model-slug", 4, "gpt-7-nova"),
        ("sol", 5, "Sol"),
        ("astra", 5, "Astra"),
        ("terra", 6, "Terra"),
        ("luna", 6, "Luna"),
    ]


def test_quoting_does_not_hide_the_invocation_verb():
    """Break: the verb is matched as the bare phrase ``Skill tool``.

    The vocabulary has to survive the quoting the emitted
    text actually uses -- ``Skill`` adjacent to ``tool`` across an
    intervening quote.
    """
    matches = _scan_corpus_file("edge/quoted-invocation-verb.md")
    assert [m.term for m in matches] == ["skill-tool"] * 3
    assert [m.line for m in matches] == [3, 4, 5]


def test_the_invocation_verb_is_caught_in_the_plural():
    """Break: ``tool\\b`` rejecting ``Skill tools``.

    "Load them with the Skill tools this host exposes" is the same section
    2.7 construction with a plural noun, and the pattern missed it -- a
    false NEGATIVE in a merge-gate instrument.
    """
    matches = _scan_corpus_file("edge/invocation-verb-plural.md")
    assert [(m.term, m.line) for m in matches] == [("skill-tool", 3), ("skill-tool", 4)]


def test_two_nouns_in_a_listing_are_not_the_invocation_verb():
    """Break: a separator class of ``\\W`` rather than of quoting.

    "A skill, tool, or command" is ordinary English listing two nouns, and
    ``skill\\W{0,4}tool`` reported it as the host's invocation verb -- a
    false POSITIVE, which in this instrument means an author is pushed to
    reword compliant prose, or to allowlist a hit that is not one.

    ``Skill tooling`` and ``skill toolkit`` are the other direction of the
    same class: different words, never the verb.
    """
    assert _scan_corpus_file("negative/adjacent-nouns-and-plurals.md") == []


def test_the_plan_mode_phrase_has_live_corpus_coverage():
    """Break: a regression in ``before-entering-plan-mode`` going unseen.

    The term had ZERO positives anywhere -- not in the corpus, not in the
    live tree -- so its pattern could break, or be deleted, with the whole
    suite staying green. Three spellings the shared text actually uses.
    """
    matches = _scan_corpus_file("edge/plan-mode-phrase.md")
    assert [(m.term, m.line) for m in matches] == [
        ("before-entering-plan-mode", 6),
        ("before-entering-plan-mode", 7),
        ("before-entering-plan-mode", 8),
    ]
    assert [m.text for m in matches] == [
        "before entering plan mode",
        "before-entering-plan-mode",
        "before** entering plan mode",
    ]


def test_shell_assignment_form_detected():
    """Break: the entrypoint pattern is anchored to the start of a line.

    The construction bound to a variable is reachable by none of the plain
    literal cases above.
    """
    matches = _scan_corpus_file("edge/shell-assignment-form.md")
    assert [(m.term, m.line) for m in matches] == [("bash-script-entrypoint", 7)]


def test_shell_command_substitution_form_detected():
    """Break: the entrypoint pattern requires the command to start a token.

    Inside ``$(...)`` and inside backticks the construction is preceded by
    a punctuation character, not by whitespace at line start.
    """
    matches = _scan_corpus_file("edge/shell-command-substitution-form.md")
    assert [(m.term, m.line) for m in matches] == [
        ("bash-script-entrypoint", 7),
        ("bash-script-entrypoint", 8),
    ]


def test_path_prefix_outside_the_basename_still_reported():
    """Break: the shipped-file mask widens from the basename to the path.

    The non-term is the *basename* that names a shipped file. A mask that
    blanks the leading directory segments as well swallows
    ``~/.claude/…`` -- the exact construction shared text must not
    carry -- whenever a hyphenated filename happens to follow it, and it
    swallows a bare ``claude/`` directory the same way. Both are false
    negatives in a merge-gate instrument.

    The fourth line is the control: no hyphen in the basename, so nothing
    is masked there under either reading, and it must keep reporting.
    """
    matches = _scan_corpus_file("edge/path-prefix-outside-the-basename.md")
    assert [(m.term, m.line, m.text) for m in matches] == [
        ("claude-home-path", 7, "~/.claude/skills/"),
        ("claude-home-path", 8, "~/.claude/agents/"),
        ("claude", 9, "claude"),
        ("claude-home-path", 10, "~/.claude/settings.json"),
    ]


# --- negatives -----------------------------------------------------------


def test_namespace_vocabulary_never_flagged():
    """Break: ``crucible:<skill-name>`` becomes a scanner target.

    The namespaced name is canonical on
    every runtime; only the invocation mechanism is adapter-mediated.
    """
    assert _scan_corpus_file("negative/namespace-vocabulary.md") == []


def test_adapter_basename_citation_never_flagged():
    """Break: a hyphenated basename naming a shipped file becomes a term.

    This is what makes the router's citation of both adapter references
    compliant rather than a term the allowlist would have to carry.
    """
    assert _scan_corpus_file("negative/adapter-basename-citation.md") == []


def test_words_near_a_codex_model_name_never_flagged():
    """Break: a Codex model term loses its word boundaries.

    "Solve", "terrain", "lunar" and "astral" begin with a model name, and
    "ChatGPT-style" ends in the slug's prefix; none of them names a model.
    """
    assert _scan_corpus_file("negative/codex-near-miss-words.md") == []


# --- allowlist grammar ---------------------------------------------------


@pytest.mark.parametrize(
    "row",
    [
        "2 | * | skills/using-crucible/references/claude-code.md | all of it",
        "2 |  | skills/using-crucible/references/claude-code.md | all of it",
        "2 | skills/using-crucible/references/claude-code.md | all of it",
    ],
    ids=["star-term", "empty-term", "term-omitted"],
)
def test_whole_file_entry_rejected(row):
    """Break: the loader accepts a whole-file allowlist entry.

    A whole-file entry would suppress the pre-adaptation positives that
    share a file with allowlisted model-policy prose.
    """
    with pytest.raises(cs.AllowlistError):
        cs.parse_allowlist(row)


def test_unknown_term_rejected():
    """Break: a typo'd or retired term id silently allows nothing."""
    with pytest.raises(cs.AllowlistError):
        cs.parse_allowlist("2 | opuss | skills/x/SKILL.md | typo")


def test_only_classes_two_and_three_in_four_fields_parse():
    """Break: a row outside classes 2 and 3, or a row with a fifth field,
    parses -- a verbatim-snippet column would freeze policy wording in the
    allowlist."""
    with pytest.raises(cs.AllowlistError):
        cs.parse_allowlist("1 | opus | skills/x/SKILL.md | floor")
    with pytest.raises(cs.AllowlistError):
        cs.parse_allowlist("2 | opus | skills/x/SKILL.md | Opus floor | floor")


def test_duplicate_entry_rejected():
    """Break: the same term/location pair is entered twice, hiding drift."""
    row = "2 | opus | skills/x/SKILL.md | reason"
    with pytest.raises(cs.AllowlistError):
        cs.parse_allowlist(row + "\n" + row)


# --- the hook script ------------------------------------------------------

CLAUDE_ADAPTER = "skills/using-crucible/references/claude-code.md"
CODEX_ADAPTER = "skills/using-crucible/references/codex.md"


def test_hook_script_is_scanned_as_a_source(tmp_path):
    """Break: the scan narrows back to ``.md`` files.

    The envelope's lead line lives in the hook script and in no ``.md``
    file, so a Claude-ism there is invisible to a scan of ``.md`` sources.
    The script is read, never run: the one here is not even valid bash.
    """
    files = {
        "skills/using-crucible/SKILL.md": "# Router\n\nNeutral text only.\n",
        "hooks/session-start": 'lead="Read both before acting on Claude Code." ((\n',
    }
    for relpath, text in files.items():
        path = tmp_path / relpath
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    sources = cs.collect_sources(tmp_path)
    matches = cs.scan_tree(tmp_path)

    assert cs.HOOK_SCRIPT in sources
    assert [(m.term, m.location, m.line) for m in matches] == [
        ("claude-code", "hooks/session-start", 1)
    ]


# --- the scan corpus itself ----------------------------------------------


def test_collect_sources_covers_the_declared_corpus_and_excludes_docs():
    """Break: the scanned surface silently narrows (or swallows docs/).

    ``docs/`` is excluded by design -- specs and plans quote Claude-isms
    deliberately, and scanning them would make every quotation a finding.
    """
    sources = cs.collect_sources(REPO_ROOT)

    assert "README.md" in sources
    assert "skills/using-crucible/SKILL.md" in sources
    assert CLAUDE_ADAPTER in sources
    assert "hooks/README.md" in sources
    assert "hooks/session-start" in sources
    assert not any(loc.startswith("docs/") for loc in sources)
    assert not any(loc.startswith("tests/") for loc in sources)

    expected = {
        p.relative_to(REPO_ROOT).as_posix()
        for p in list((REPO_ROOT / "skills").rglob("*.md"))
        + list((REPO_ROOT / "hooks").rglob("*.md"))
    } | {"README.md", "hooks/session-start"}
    assert set(sources) == expected


# --- the shipped allowlist -----------------------------------------------


@pytest.fixture(scope="module")
def shipped() -> cs.Allowlist:
    return cs.load_allowlist(cs.ALLOWLIST_PATH)


def test_shipped_allowlist_locations_exist(shipped):
    """Break: an entry outlives the file it was derived from."""
    missing = [e.location for e in shipped.entries if not (REPO_ROOT / e.location).is_file()]
    assert missing == []


#: The Codex model-line terms: the only terms the Codex host map may carry.
CODEX_MODEL_TERMS = frozenset({"codex-model-slug", "sol", "terra", "astra", "luna"})


def test_shipped_codex_adapter_reference_carries_only_its_model_names(shipped):
    """Break: a Claude-ism lands in the Codex adapter reference, or an
    allowlist row there licenses one.

    No hook injects it, so it is read from disk alone. Its Model roles
    entry names this host's models, so its allowlist rows may license Codex
    model-line terms and nothing else, and every term it carries must be
    one those rows license.
    """
    rows = {e.term for e in shipped.entries if e.location == CODEX_ADAPTER}
    assert rows <= CODEX_MODEL_TERMS
    codex_text = (REPO_ROOT / CODEX_ADAPTER).read_text(encoding="utf-8")
    stray = [m for m in cs.find_matches(codex_text, CODEX_ADAPTER) if m.term not in rows]
    assert stray == [], "\n".join(m.render() for m in stray)


#: How near a Codex personal-skill path must sit to each Claude one.
PAIR_DISTANCE_LINES = 6

#: The Codex host's personal skill directories: the one its documentation
#: names, and the CLI's own tree, in either spelling. The CLI's built-in
#: skills under `.system/` are not a personal skill directory.
_CODEX_SKILL_PATH = re.compile(
    r"(?:\$HOME/\.agents/skills|~/\.agents/skills"
    r"|\$CODEX_HOME/skills|~/\.codex/skills)(?!/\.system)"
)


def unpaired_claude_home_paths(text: str, location: str) -> list[int]:
    """Lines of *text* carrying a ``claude-home-path`` hit with no Codex
    personal-skill path within ``PAIR_DISTANCE_LINES`` lines of it."""
    lines = text.split("\n")
    codex = [n for n, line in enumerate(lines, start=1) if _CODEX_SKILL_PATH.search(line)]
    return [
        m.line
        for m in cs.find_matches(text, location)
        if m.term == "claude-home-path"
        and not any(abs(m.line - n) <= PAIR_DISTANCE_LINES for n in codex)
    ]


def test_the_claude_home_path_routing_entry_still_has_its_codex_sibling(shipped):
    """Break caught: deleting the Codex sibling that is the whole
    justification for the class-2 entry sitting over it.

    ``claude-home-path`` @ ``skills/writing-skills/SKILL.md`` is class 2, and
    class 2 is FILE-scoped by construction -- it cannot see which sentence
    carries the hit. Its recorded justification is that the file cites that
    host's personal skill path *as one host's, beside the Codex path*. Delete
    the Codex path and the same entry silently covers a bare
    only-personal-skill-location claim -- the construction the scanner
    exists to keep out.
    So every hit the entry covers must have a Codex path near it.
    """
    location = "skills/writing-skills/SKILL.md"
    assert any(
        e.location == location and e.term == "claude-home-path" for e in shipped.entries
    )
    text = (REPO_ROOT / location).read_text(encoding="utf-8")
    hits = [m for m in cs.find_matches(text, location) if m.term == "claude-home-path"]
    assert hits, "the entry no longer covers anything"
    # Consumer: the Codex host reads user skills from `$HOME/.agents/skills`
    # (its documentation) and keeps its own under `~/.codex/skills`; the
    # pair names one of them.
    assert unpaired_claude_home_paths(text, location) == []


def test_the_pairing_check_fires_on_a_lone_claude_home_path():
    """The proximity check demonstrably fires: a Claude path with no Codex
    path near it is reported, and one with a Codex path nearby is not."""
    lone = "Personal skills live in `~/.claude/skills/`.\n" + "filler\n" * 10
    assert unpaired_claude_home_paths(lone, "x.md") == [1]
    paired = "Claude: `~/.claude/skills/`.\nCodex: `$CODEX_HOME/skills`.\n"
    assert unpaired_claude_home_paths(paired, "x.md") == []
    documented = "Claude: `~/.claude/skills/`.\nCodex: `$HOME/.agents/skills`.\n"
    assert unpaired_claude_home_paths(documented, "x.md") == []
    # The host's built-in skills directory is not a personal-skill path.
    system_only = "Claude: `~/.claude/skills/`.\nBuilt in: `~/.codex/skills/.system/`.\n"
    assert unpaired_claude_home_paths(system_only, "x.md") == [1]


def test_router_contributes_no_allowlist_entry(shipped):
    """Break: a provider noun returns to shared router text.

    There is no router class: the router carries no provider noun, so a
    match there is a defect and never an allowlist candidate.
    """
    router = "skills/using-crucible/SKILL.md"
    assert [e for e in shipped.entries if e.location == router] == []
    text = (REPO_ROOT / router).read_text(encoding="utf-8")
    assert cs.find_matches(text, router) == []
