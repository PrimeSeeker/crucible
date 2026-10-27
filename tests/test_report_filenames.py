"""Instrument report filenames clear Claude Code's subagent report-name filter.

Claude Code's Write tool refuses a subagent's write when the target's
basename matches ``HOST_FILTER`` ("Subagents should return findings as
text, not write report files"), whatever the dispatch authorized — see
``skills/using-crucible/references/claude-code-dispatch.md``. An instrument whose
report path matches has its write refused on every dispatch, leaving the
controller to save the report, so no report filename crucible hands an
instrument may match it.
"""

from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILLS = REPO / "skills"
FORMATS = SKILLS / "redteaming" / "references" / "formats.md"

#: The host's pattern, as measured in Claude Code 2.1.289's Write tool.
HOST_FILTER = re.compile(r"^(REPORT|SUMMARY|FINDINGS|ANALYSIS).*\.md$", re.I)

REPORT_SLOT = re.compile(r"^- (\{report-path\}|\[REPORT_FILE\]):")
BACKTICKED_MD = re.compile(r"`([^`\s]+\.md)`")


def _slot_card_report_names() -> list[tuple[str, str]]:
    """(basename, source) for every .md a slot card's report slot names."""
    names: list[tuple[str, str]] = []
    for card in sorted(SKILLS.rglob("*.slots.md")):
        for line in card.read_text(encoding="utf-8").splitlines():
            if REPORT_SLOT.match(line):
                for path in BACKTICKED_MD.findall(line):
                    names.append((path.rsplit("/", 1)[-1], card.relative_to(REPO).as_posix()))
    return names


def _formats_round_layout_names() -> list[tuple[str, str]]:
    """(basename, source) for the files formats.md's per-round layout lists."""
    text = FORMATS.read_text(encoding="utf-8")
    block = text.split("Per-round directory contents:", 1)[1]
    block = block.split("```", 2)[1]
    names: list[tuple[str, str]] = []
    for line in block.splitlines():
        match = re.match(r"^\s*(\S+\.md)\s", line + " ")
        if match:
            names.append((match.group(1), "formats.md per-round layout"))
    return names


def _blocked(pairs: list[tuple[str, str]]) -> list[str]:
    """Each filter-matching basename with every source that names it."""
    sources: dict[str, list[str]] = {}
    for name, src in pairs:
        if HOST_FILTER.match(name) and src not in sources.setdefault(name, []):
            sources[name].append(src)
    return [f"{name} ({'; '.join(srcs)})" for name, srcs in sorted(sources.items())]


def test_collectors_see_the_known_report_names():
    """The collectors are not vacuous: they find report names on both
    surfaces. (``Per-round directory contents:`` is this module's anchor
    into formats.md, not a pinned sentence; reworded, the collector fails
    loudly here.)"""
    # Consumer: conserve.py reads seat reports by file name
    # (`seat-*.md`); `verifier.md`, `terminal-pass.md` and `second-read.md`
    # are instruments' write targets, which the host's Write tool admits or
    # refuses by name (the filter below).
    slot_names = {name for name, _ in _slot_card_report_names()}
    layout_names = {name for name, _ in _formats_round_layout_names()}
    assert {"verifier.md", "terminal-pass.md", "second-read.md"} <= slot_names
    assert {"seat-<id>.md", "verifier.md", "terminal-pass.md", "second-read.md"} <= layout_names


def test_every_report_slot_names_a_path_the_collector_sees():
    """Break: a card's report slot naming its output in a form the
    collector cannot read (no backticked ``.md`` path), so that seat's
    filename escapes the host-filter check below."""
    silent = []
    for card in sorted(SKILLS.rglob("*.slots.md")):
        for line in card.read_text(encoding="utf-8").splitlines():
            if REPORT_SLOT.match(line) and not BACKTICKED_MD.findall(line):
                silent.append(card.relative_to(REPO).as_posix())
    assert silent == [], f"report slots naming no backticked .md path: {silent}"


def test_no_instrument_report_name_matches_the_host_filter():
    # Consumer: Claude Code's Write tool, which refuses a subagent's write
    # to a basename HOST_FILTER matches.
    blocked = _blocked(_formats_round_layout_names() + _slot_card_report_names())
    assert blocked == [], f"report filenames Claude Code refuses to subagents: {blocked}"
