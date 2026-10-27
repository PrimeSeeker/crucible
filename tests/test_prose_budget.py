"""Shipped skill prose: the word-count ratchet.

``tests/prose-budget.txt`` holds one word count per skill directory
(whitespace-separated tokens in its ``*.md`` files). A count above its
number fails, so growth is a recorded raise in the commit that grows the
skill; a count more than ``SLACK`` words below fails too, so a cut lowers
the number and cannot be regrown silently (``AGENTS.md``, the prose
budget).
"""

from __future__ import annotations

from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
BUDGET_FILE = REPO / "tests" / "prose-budget.txt"
SLACK = 50


def read_budget() -> dict[str, int]:
    budget: dict[str, int] = {}
    for line in BUDGET_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        name, words = line.split()
        budget[name] = int(words)
    return budget


def count_words(skill_dir: Path) -> int:
    return sum(
        len(path.read_text(encoding="utf-8").split())
        for path in sorted(skill_dir.rglob("*.md"))
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
