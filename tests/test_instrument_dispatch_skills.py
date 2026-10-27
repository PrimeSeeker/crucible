"""Every skill that dispatches a templated instrument names it together with
its slot card.

An instrument is named in skill text by its bare agent name in backticks
(``implementer``), the name the host exposes the generated agent under; the
card is what the controller fills for that dispatch. A skill that names an
instrument without its card leaves the controller nothing to fill. The
instrument list and each template's path come from
``tools/instrument_agents.py``; no dispatch sentence is pinned.
"""

from __future__ import annotations

import re

import pytest

from instrument_corpus import REPO_ROOT, card_path, instruments, raw

SKILLS = sorted(
    p.relative_to(REPO_ROOT).as_posix() for p in (REPO_ROOT / "skills").glob("*/SKILL.md")
)


def owning_skill(template: str) -> str:
    """The skill whose directory holds *template*: the one that dispatches
    its instrument."""
    return "/".join(template.split("/")[:2]) + "/SKILL.md"


def named_instruments(text: str) -> set[str]:
    """The instruments *text* names, by their backticked bare name."""
    return {name for name in instruments() if f"`{name}`" in text}


@pytest.mark.parametrize("name", sorted(instruments()))
def test_skill_dispatch_owning_skill_names_the_instrument(name: str) -> None:
    """Break: the skill that owns an instrument's template no longer naming
    the instrument it dispatches."""
    # Consumer: the host's agent loader exposes each generated agent under
    # this name (agents/<name>.md frontmatter `name`, as `crucible:<name>`),
    # so the bare name is the dispatch target the controller passes on.
    assert name in named_instruments(raw(owning_skill(instruments()[name])))


@pytest.mark.parametrize("skill", SKILLS)
def test_skill_dispatch_names_each_instrument_with_its_card(skill: str) -> None:
    """Break: a skill naming an instrument without the card the controller
    fills for it."""
    text = raw(skill)
    for name in sorted(named_instruments(text)):
        card = card_path(instruments()[name])
        assert (REPO_ROOT / card).is_file(), card
        # Consumer: the controller opens the named card to fill it; the
        # basename is the path it resolves beside the template.
        basename = card.rsplit("/", 1)[1]
        assert re.search(rf"(?<![\w-]){re.escape(basename)}", text), (skill, name)
