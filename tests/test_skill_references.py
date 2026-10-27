"""On-demand skill references and their stubs (skill-prose extraction lane).

A route-conditional section moved out of a SKILL.md leaves its heading
behind with a stub naming the reference to read in full. These checks keep
each stub and its reference paired: the reference exists, opens with the
stub's own heading, and is named by exactly one stub. A shared reference is
the exception: named by a stub in each skill that shares it, it opens with
a heading of its own, none of its stubs' headings.
"""

from __future__ import annotations

import re
from collections import Counter

from skill_corpus import REPO_ROOT, skill_corpus, stub_references

SKILLS = sorted(
    p.relative_to(REPO_ROOT).as_posix()
    for p in (REPO_ROOT / "skills").glob("*/SKILL.md")
)

#: The extracted references, so a stub silently dropped (its section back
#: inline, or lost) fails here rather than going unnoticed.
EXPECTED = {
    ("skills/redteaming/SKILL.md", "skills/redteaming/references/plan-phase.md"),
    ("skills/redteaming/SKILL.md", "skills/redteaming/references/folded-lane.md"),
    (
        "skills/subagent-driven-development/SKILL.md",
        "skills/subagent-driven-development/references/very-small-lane.md",
    ),
    (
        "skills/brainstorming/SKILL.md",
        "skills/brainstorming/references/folded-lane-document.md",
    ),
    ("skills/brainstorming/SKILL.md", "skills/brainstorming/references/lane-note.md"),
    ("skills/redteaming/SKILL.md", "skills/redteaming/references/flip-paths.md"),
    (
        "skills/subagent-driven-development/SKILL.md",
        "skills/redteaming/references/flip-paths.md",
    ),
}

#: References more than one skill's stub names; each of their stubs is a
#: pair in EXPECTED.
SHARED = {"skills/redteaming/references/flip-paths.md"}


def _stubs() -> list[tuple[str, str, str]]:
    return [
        (skill, heading, ref)
        for skill in SKILLS
        for heading, ref in stub_references(skill)
    ]


def test_skill_references_stub_set_is_the_extraction() -> None:
    assert {(skill, ref) for skill, _, ref in _stubs()} == EXPECTED


def _first_line(ref: str) -> str:
    return (REPO_ROOT / ref).read_text("utf-8").replace("\r\n", "\n").split("\n", 1)[0]


def test_skill_references_each_reference_opens_with_its_stub_heading() -> None:
    """Break: a reference renamed or re-headed away from its stub, so the
    `§` citations that land on the stub no longer describe the file the
    controller is told to read."""
    for skill, heading, ref in _stubs():
        assert (REPO_ROOT / ref).is_file(), f"{skill}: stub names missing {ref}"
        if ref in SHARED:
            continue
        first = _first_line(ref)
        assert first == heading, f"{ref} opens with {first!r}, stub heading {heading!r}"


def test_skill_references_shared_reference_opens_with_its_own_heading() -> None:
    """Break: a shared reference opening with one stub's heading, so it
    reads as that skill's section and the other skill's citations of its
    own stub describe a different file."""
    for ref in SHARED:
        first = _first_line(ref)
        stub_headings = {heading for _, heading, r in _stubs() if r == ref}
        assert re.fullmatch(r"#{1,4} .+", first), f"{ref} opens with {first!r}"
        assert first not in stub_headings, f"{ref} opens with stub heading {first!r}"


def test_skill_references_each_reference_has_one_stub() -> None:
    """Break: a second stub naming a reference, or a shared reference's
    stub repeated within one skill, so a procedure gains an always-loaded
    entry point the expected pairs do not list."""
    counts = Counter(ref for _, _, ref in _stubs())
    expected = Counter(ref for _, ref in EXPECTED)
    assert {ref: n for ref, n in counts.items() if n != expected[ref]} == {}


def test_skill_references_stub_is_a_pointer_not_the_section() -> None:
    """Break: the section's body pasted back under its stub while the
    reference also stays, so the skill carries the text twice. A stub is
    the heading plus one short paragraph."""
    for skill, heading, ref in _stubs():
        text = (REPO_ROOT / skill).read_text("utf-8").replace("\r\n", "\n")
        start = text.index(f"\n{heading}\n") + len(heading) + 2
        nxt = re.search(r"^#{1,4} ", text[start:], re.MULTILINE)
        body = text[start : start + nxt.start()] if nxt else text[start:]
        assert len([p for p in body.split("\n\n") if p.strip()]) == 1, (skill, heading)


def test_skill_references_corpus_carries_the_reference_text() -> None:
    for skill, _, ref in _stubs():
        ref_text = (REPO_ROOT / ref).read_text("utf-8").replace("\r\n", "\n")
        assert ref_text.rstrip("\n") in skill_corpus(skill)
