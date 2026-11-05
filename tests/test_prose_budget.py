"""Shipped skill prose: the word-count ratchet.

``tests/prose-budget.txt`` holds one word count per skill directory
(whitespace-separated tokens in its hand-edited ``*.md`` files: every one
but a template the generator renders from its source, whose words the
source already counts). A count above its
number fails, so growth is a recorded raise in the commit that grows the
skill; a count more than ``SLACK`` words below fails too, so a cut lowers
the number and cannot be regrown silently (``AGENTS.md``, the prose
budget). ``TOTAL_CAP`` limits the sum, and no commit raises it on its own
authority (same section).
"""

from __future__ import annotations

from pathlib import Path

import pytest

from instrument_corpus import load_generator, source_path

REPO = Path(__file__).resolve().parent.parent
BUDGET_FILE = REPO / "tests" / "prose-budget.txt"
SLACK = 50
# 10% over the 43,079 words the 2026-11-03 compaction left. Only the operator
# moves it (AGENTS.md, the prose budget).
TOTAL_CAP = 47387


def read_budget() -> dict[str, int]:
    budget: dict[str, int] = {}
    for line in BUDGET_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        name, words = line.split()
        budget[name] = int(words)
    return budget


def rendered_templates() -> set[str]:
    """The templates the generator renders from their sources: generated
    text, so no budget counts it."""
    return set(load_generator().INSTRUMENTS.values())


def count_words(skill_dir: Path) -> int:
    """Words in *skill_dir*'s hand-edited ``*.md`` files: every one but a
    rendered template. *skill_dir* is ``<root>/skills/<name>``."""
    root = skill_dir.parent.parent
    rendered = rendered_templates()
    return sum(
        len(path.read_text(encoding="utf-8").split())
        for path in sorted(skill_dir.rglob("*.md"))
        if path.relative_to(root).as_posix() not in rendered
    )


def skill_dirs() -> list[str]:
    return sorted(p.name for p in (REPO / "skills").iterdir() if p.is_dir())


def test_every_skill_directory_has_a_budget() -> None:
    assert sorted(read_budget()) == skill_dirs()


@pytest.mark.parametrize("name", skill_dirs())
def test_skill_prose_matches_its_budget(name: str) -> None:
    budget = read_budget()[name]
    words = count_words(REPO / "skills" / name)
    assert words <= budget, (
        f"skills/{name} has {words} words, budget {budget}: raise its line in "
        f"tests/prose-budget.txt to {words} and say in the commit body what "
        f"the words buy or what went in exchange, or cut"
    )
    assert words >= budget - SLACK, (
        f"skills/{name} has {words} words, budget {budget}: lower its line in "
        f"tests/prose-budget.txt to {words}"
    )


def test_total_prose_stays_under_the_cap() -> None:
    total = sum(count_words(REPO / "skills" / name) for name in skill_dirs())
    assert total <= TOTAL_CAP, (
        f"skills/ holds {total} words, cap {TOTAL_CAP}: do not raise the cap. "
        f"Stop and ask the operator whether to compact or to raise it "
        f"(AGENTS.md, the prose budget)"
    )


def test_rendered_templates_are_not_counted(tmp_path: Path) -> None:
    """Break: the count taking a rendered template beside its source, so
    spliced text counts twice and a regenerated template moves a budget."""
    template = sorted(rendered_templates())[0]
    skill_dir = tmp_path / Path(template).parent
    skill_dir.mkdir(parents=True)
    (skill_dir / "SKILL.md").write_bytes(b"one two\n")
    (tmp_path / source_path(template)).write_bytes(b"three four five\n")
    assert count_words(skill_dir) == 5
    (tmp_path / template).write_bytes(b"three four five six seven\n")
    assert count_words(skill_dir) == 5
