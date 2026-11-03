"""Skill size: every SKILL.md fits the host's cut after compaction.

After compaction Claude Code re-attaches each invoked skill cut at about
20,000 characters: a header line naming the skill's install path, the body
without its frontmatter, then a truncation notice. A controller working
from a cut copy loses every step past the cut. Each ``SKILL.md`` body is
held at or under ``LINE`` characters; the margin covers long install paths
and small edits. The measurement and the line's basis:
``docs/decisions/authoring-crucible.md``.

The body is the text after the frontmatter's closing ``---`` line, whose
newline belongs to the frontmatter; a file with no frontmatter is all
body. Its size is its length as a Python ``str``, in characters, not bytes.
"""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

#: The test line, in characters of body.
LINE = 18_000


def body(text: str) -> str:
    """*text* less its frontmatter block, the closing fence's line included."""
    lines = text.splitlines(keepends=True)
    if lines and lines[0].rstrip("\r\n") == "---":
        for i in range(1, len(lines)):
            if lines[i].rstrip("\r\n") == "---":
                return "".join(lines[i + 1 :])
    return text


def over_line(root: Path) -> list[tuple[str, int]]:
    """(path, body size) for each ``skills/*/SKILL.md`` under *root* whose
    body exceeds ``LINE``."""
    over = []
    for path in sorted((root / "skills").glob("*/SKILL.md")):
        size = len(body(path.read_text(encoding="utf-8")))
        if size > LINE:
            over.append((path.relative_to(root).as_posix(), size))
    return over


def test_every_skill_body_is_at_or_under_the_line() -> None:
    assert list((REPO_ROOT / "skills").glob("*/SKILL.md")), "no SKILL.md found"
    # Reader: the host's re-attachment of an invoked skill after compaction,
    # which keeps only the first ~20,000 characters of header and body.
    over = over_line(REPO_ROOT)
    assert not over, "SKILL.md bodies over the {:,}-character line: {}".format(
        LINE,
        "; ".join(f"{rel} has {size:,}" for rel, size in over)
        + ". Move a long step body into a reference read at its step, "
        "keeping the spine (docs/decisions/authoring-crucible.md)",
    )


def _skill(root: Path, name: str, text: str) -> None:
    path = root / "skills" / name / "SKILL.md"
    path.parent.mkdir(parents=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def test_body_drops_the_frontmatter_and_its_closing_fence() -> None:
    text = "---\nname: a\ndescription: d\n---\n# A\n\nStep one.\n"
    assert body(text) == "# A\n\nStep one.\n"


def test_a_file_without_frontmatter_is_all_body() -> None:
    assert body("# A\n---\nStep one.\n") == "# A\n---\nStep one.\n"


def test_the_line_admits_a_body_at_it_and_fails_one_past_it(tmp_path: Path) -> None:
    """Break: the frontmatter or its fence's newline counted, or ``<`` for
    ``<=``, so a body exactly at the line fails; or a body past it, with
    no frontmatter to strip, passing."""
    front = "---\nname: x\ndescription: d\n---\n"
    _skill(tmp_path, "at-line", front + "x" * 17_999 + "\n")
    _skill(tmp_path, "past-line", "x" * 18_000 + "\n")
    assert over_line(tmp_path) == [("skills/past-line/SKILL.md", 18_001)]
