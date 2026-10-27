"""Structural check on the decision records in ``docs/decisions/``.

Every record carries the three sections a record cannot omit:
``## Decision``, ``## Why`` and ``## Changes``. The check is structural
(headings exist), not a check of their content; that a later edit added
its Changes line is the branch reviewer's check, not this file's.

The helper takes an explicit root so a seeded tree under tmp_path shows
the check failing.
"""

from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

REQUIRED_SECTIONS = ("Decision", "Why", "Changes")


def record_paths(root: Path) -> list[Path]:
    return sorted((root / "docs" / "decisions").glob("*.md"))


def missing_sections(root: Path) -> list[str]:
    violations = []
    for path in record_paths(root):
        text = path.read_bytes().decode("utf-8").replace("\r\n", "\n")
        headings = set(re.findall(r"^## +(.+?)\s*$", text, re.MULTILINE))
        for section in REQUIRED_SECTIONS:
            if section not in headings:
                violations.append(
                    f"{path.relative_to(root).as_posix()}: "
                    f"no '## {section}' section"
                )
    return violations


def test_decision_records_exist() -> None:
    # Guards the check below against passing over an empty directory.
    assert record_paths(REPO_ROOT)


def test_every_record_has_its_required_sections() -> None:
    assert not missing_sections(REPO_ROOT), "\n".join(
        missing_sections(REPO_ROOT)
    )


def _seed_record(tmp_path: Path, text: str) -> Path:
    root = tmp_path / "repo"
    decisions = root / "docs" / "decisions"
    decisions.mkdir(parents=True)
    (decisions / "demo-record.md").write_text(text, encoding="utf-8")
    return root


_COMPLETE = (
    "# Demo\n\n## Decision\n\nA position.\n\n## Why\n\nA reason.\n\n"
    "## Changes\n\n- 2026-01-01: adopted.\n"
)


def test_seeded_complete_record_passes(tmp_path: Path) -> None:
    assert missing_sections(_seed_record(tmp_path, _COMPLETE)) == []


def test_seeded_record_missing_changes_is_caught(tmp_path: Path) -> None:
    text = _COMPLETE.split("## Changes")[0]
    hits = missing_sections(_seed_record(tmp_path, text))
    assert len(hits) == 1 and "## Changes" in hits[0]


def test_seeded_record_with_changes_only_as_subheading_is_caught(
    tmp_path: Path,
) -> None:
    text = _COMPLETE.replace("## Changes", "### Changes")
    hits = missing_sections(_seed_record(tmp_path, text))
    assert len(hits) == 1 and "## Changes" in hits[0]
