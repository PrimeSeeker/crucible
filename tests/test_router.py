"""Tests for the SessionStart router's content.

Covers, over the envelope the hook script emits for this tree (its
registration, document shape, escaping and failures are
``tests/test_hook_script.py``'s):

- the envelope carries the ``using-crucible`` skill content;
- it inlines exactly one host map, the Claude Code one, and no
  dispatch reference, and names every shipped skill exactly once (invocation form
  ``crucible:<name>`` per ``docs/authoring.md`` section "Reference
  convention");
- SUBAGENT-STOP is the first operative block after frontmatter, and in
  the emitted content it closes before any heading;
- no ``superpowers`` string and no dropped-skill name in the emitted
  content;
- the two router files hold no control character the hook's JSON
  escaping does not handle.
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
TESTS_DIR = REPO_ROOT / "tests"
SKILL_FILE = REPO_ROOT / "skills" / "using-crucible" / "SKILL.md"
REFERENCES_DIR = REPO_ROOT / "skills" / "using-crucible" / "references"
# Every shipped host map. Only the Claude one is injected; Codex sessions
# read theirs from disk, so no envelope may carry it.
ADAPTER_FILES = {
    "claude": REFERENCES_DIR / "claude-code.md",
    "codex": REFERENCES_DIR / "codex.md",
}
# The dispatch references: controller skills read them from disk, and no
# envelope inlines one.
DISPATCH_FILES = (
    REFERENCES_DIR / "claude-code-dispatch.md",
    REFERENCES_DIR / "codex-dispatch.md",
)

sys.path.insert(0, str(TESTS_DIR))

import hook_runner as hr  # noqa: E402  (path inserted above; not a package)

# The shipped-skill roster: every skills/ directory carrying a SKILL.md, the
# set tests/test_structure.py holds the router index to. The envelope must
# name each exactly once.
ROSTER = sorted(
    d.name for d in (REPO_ROOT / "skills").iterdir() if (d / "SKILL.md").is_file()
)

# Dropped upstream skill names -- banned everywhere in crucible prose
# (tests/test_references.py enforces it repo-wide; this file enforces it for
# the router's emitted content specifically, lead line included).
from test_references import DROPPED_SKILLS as DROPPED_NAMES  # noqa: E402


@pytest.fixture(scope="module")
def emitted_context() -> str:
    """The additionalContext string from one real hook run."""
    if hr.find_bash() is None:
        pytest.skip(hr.no_bash_reason())
    return hr.envelope()


# --- happy path: emission ------------------------------------------------


def test_hook_emits_skill_content(emitted_context: str) -> None:
    """The emitted context carries the full SKILL.md content."""
    skill_text = SKILL_FILE.read_text(encoding="utf-8")
    assert skill_text.strip() in emitted_context


# --- one host map per rendered envelope, no dispatch reference ----------


def test_envelope_inlines_exactly_one_host_map(emitted_context: str) -> None:
    """The rendered envelope carries the Claude Code host map in full and
    no other shipped host map at all.

    The break: rendering a pointer instead of the text (a fresh session
    would never read it), inlining the wrong runtime's reference, or
    inlining both.
    """
    mine = ADAPTER_FILES["claude"].read_text(encoding="utf-8").strip()
    assert mine in emitted_context, "claude host map is not inlined"
    theirs = ADAPTER_FILES["codex"].read_text(encoding="utf-8").strip()
    assert theirs not in emitted_context, "the envelope carries codex.md"


def test_envelope_inlines_no_dispatch_reference(emitted_context: str) -> None:
    """The dispatch references stay out of every envelope: the hook
    re-injects the host map alone, and a controller reads its dispatch
    reference from disk.

    The break: inlining a dispatch reference beside the host map, which
    spends the envelope budget on procedure only controllers use.
    """
    for path in DISPATCH_FILES:
        text = path.read_text(encoding="utf-8").strip()
        assert text not in emitted_context, f"the envelope carries {path.name}"


# --- router index vs the shipped-skill roster ----------------------------


def test_index_matches_roster_exactly_once_each(emitted_context: str) -> None:
    """Every roster name appears as a `crucible:<name>` invocation exactly
    once in the emitted content -- no missing, no duplicated, no extra
    skills invoked. Counted over the WHOLE envelope: a host map that named
    a roster skill would double its count and break the router's
    exactly-once index contract."""
    found = Counter(re.findall(r"crucible:([a-z][a-z-]*)", emitted_context))
    assert found == Counter(ROSTER)


def test_index_entries_carry_when_it_applies(emitted_context: str) -> None:
    """Each roster name has an index entry with non-empty when-it-applies
    text after the name."""
    for name in ROSTER:
        # Consumer: the host's skill loader resolves `crucible:<name>`, the
        # plugin-namespaced skill name an index entry opens with.
        m = re.search(
            rf"^- `crucible:{re.escape(name)}`(.+)$",
            emitted_context,
            re.MULTILINE,
        )
        assert m, f"no index line for crucible:{name}"
        assert len(m.group(1).strip(" —-:")) >= 10, f"empty when-it-applies: {name}"


# --- SUBAGENT-STOP placement ---------------------------------------------
#
# The guard is located by its tag and its position checked; its wording is
# not pinned. The tag is a structural delimiter: a dispatched subagent
# reading top-down meets the guard before any section of the router.

_GUARD_OPEN, _GUARD_CLOSE = "<SUBAGENT-STOP>", "</SUBAGENT-STOP>"
_HEADING = re.compile(r"^#{1,6} ", re.M)


def test_subagent_stop_is_first_operative_block_in_file() -> None:
    """In SKILL.md, the first content after the frontmatter fence is the
    SUBAGENT-STOP guard, closed -- a dispatched subagent reading top-down
    disengages before reading anything else."""
    text = SKILL_FILE.read_text(encoding="utf-8")
    m = re.match(r"^---\r?\n.*?\r?\n---\s*\r?\n", text, re.DOTALL)
    assert m, "SKILL.md must start with a frontmatter block"
    body = text[m.end() :].lstrip()
    assert body.startswith(_GUARD_OPEN), (
        "first operative block must be the SUBAGENT-STOP guard, found: "
        + body[:80]
    )
    assert body[len(_GUARD_OPEN) : body.index(_GUARD_CLOSE)].strip()


def test_subagent_stop_precedes_any_heading_in_emitted(
    emitted_context: str,
) -> None:
    """In the emitted envelope, the guard closes before the first heading
    of any level -- before any section of the router or the host map."""
    first_heading = _HEADING.search(emitted_context)
    assert first_heading is not None
    assert emitted_context.index(_GUARD_CLOSE) < first_heading.start()


# --- banned strings ------------------------------------------------------


def test_no_superpowers_string_emitted(emitted_context: str) -> None:
    assert "superpowers" not in emitted_context.lower()


def test_no_dropped_skill_names_emitted(emitted_context: str) -> None:
    lowered = emitted_context.lower()
    for name in DROPPED_NAMES:
        assert name not in lowered, f"dropped skill name emitted: {name}"


def test_skill_file_itself_is_clean() -> None:
    """The same bans hold for the file on disk (belt to the emission's
    braces -- the file is what the reference scanner and future edits
    see)."""
    lowered = SKILL_FILE.read_text(encoding="utf-8").lower()
    assert "superpowers" not in lowered
    for name in DROPPED_NAMES:
        assert name not in lowered


# --- characters the hook's escaping handles ------------------------------


@pytest.mark.parametrize(
    "path", [SKILL_FILE, ADAPTER_FILES["claude"]], ids=["router", "host-map"]
)
def test_router_files_hold_no_control_character_the_hook_cannot_escape(
    path: Path,
) -> None:
    """The hook escapes backslash, double quote, newline, carriage return
    and tab, and nothing else: any other control character in these files
    would reach its JSON string raw and make the document invalid, so the
    router would not load."""
    text = path.read_bytes().decode("utf-8")
    allowed = {"\n", "\r", "\t"}
    bad = sorted({f"U+{ord(c):04X}" for c in text if ord(c) < 0x20 and c not in allowed})
    assert bad == [], f"{path.name} carries {bad}"
