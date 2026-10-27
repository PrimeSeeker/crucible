#!/usr/bin/env python3
"""The merge-conservation check of one numbered redteam panel round.

    python <plugin-root>/skills/redteaming/scripts/conserve.py <feature-slug> <phase> <round>

``<phase>`` is ``spec`` (the spec campaign) or ``plan`` (the plan phase),
the name of its directory under ``campaigns/`` in the feature workspace
``<repo>/.crucible/<feature-slug>/``. The check asks, by token presence,
whether every finding and question id the round's ``seat-<id>.md`` reports
carry occurs in its ``record.md`` outside a recorded ``unaccounted:``
verdict. It reads no markdown structure, and no content shape stops it.
``CONSERVE_DESCRIPTION`` below, its ``--help``, is the full contract; the
workspace and the round record are defined in
``skills/redteaming/references/formats.md``.

Stdlib only, and Python 3.8 or newer: the README states that floor, so
syntax or library calls from a newer Python raise it. Runs from any cwd
inside the target repo (root resolved via ``git rev-parse --show-toplevel``).
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
CAMPAIGNS = ("spec", "plan")
ROUND_ARG_RE = re.compile(r"^(?:round-)?(\d{1,3})$")


def _err(msg: str, code: int = 1) -> int:
    print(f"conserve: {msg}", file=sys.stderr)
    return code


def _repo_root() -> Path | None:
    """Resolve the enclosing checkout's root from the current cwd."""
    try:
        proc = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            timeout=30,
            stdin=subprocess.DEVNULL,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if proc.returncode != 0:
        return None
    top = proc.stdout.strip()
    return Path(top) if top else None


def _workspace_dir(root: Path, slug: str) -> Path:
    return root / ".crucible" / slug


# --- the check ----------------------------------------------------------

SEAT_REPORT_NAME_RE = re.compile(r"^seat-(?P<seat>.+)\.md$")
# A recorded verdict's label: the word, then its colon, with any whitespace,
# emphasis or code-span markers between them. The text after it on its line
# never accounts for an id.
VERDICT_LABEL_RE = re.compile(r"unaccounted[\s*_`]*:", re.I)


class _ConserveError(Exception):
    """An input the check needs cannot be read; never a clean round."""


def _round_number(arg: str) -> int | None:
    m = ROUND_ARG_RE.match(arg.strip())
    return int(m.group(1)) if m else None


def _id_re(seat: str) -> re.Pattern[str]:
    """``seat``'s finding and question ids as whole tokens: neither preceded
    nor followed by a letter of any script, a digit or a hyphen (``[^\\W_]``
    is a letter or digit, so an underscore is a boundary)."""
    return re.compile(
        rf"(?<![^\W_])(?<!-){re.escape(seat)}-q?\d+(?![^\W_])(?!-)", re.I
    )


def _report_ids(text: str, seat: str) -> dict[str, str]:
    """The ids of ``seat`` that ``text`` carries: case-folded id -> its
    first spelling in ``text``."""
    ids: dict[str, str] = {}
    for m in _id_re(seat).finditer(text):
        ids.setdefault(m.group().casefold(), m.group())
    return ids


def _id_sort_key(key: str) -> tuple[str, int, int]:
    """Grouped per seat: a seat's findings in numeric order, then its
    questions."""
    stem, _, index = key.rpartition("-")
    if index.startswith("q"):
        return (stem, 1, int(index[1:]))
    return (stem, 0, int(index))


def _without_verdicts(record: str) -> str:
    """``record`` with each line cut at its verdict label, if it has one."""
    lines: list[str] = []
    for line in record.split("\n"):
        m = VERDICT_LABEL_RE.search(line)
        lines.append(line[: m.start()] if m else line)
    return "\n".join(lines)


def _read(path: Path, what: str) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise _ConserveError(
            f"{what} {path} cannot be read as UTF-8 (byte {exc.start})"
        ) from exc
    except OSError as exc:
        raise _ConserveError(f"{what} {path} cannot be read ({exc})") from exc


def cmd_conserve(root: Path, slug: str, campaign: str, round_arg: str) -> int:
    number = _round_number(round_arg)
    if number is None:
        return _err(
            f"invalid round {round_arg!r} — expected a numbered panel round "
            "(01, 1, or round-01). The check's scope is numbered panel "
            "rounds of either phase; the terminal pass is not one",
            2,
        )
    label = f"round-{number:02d}"
    ws = _workspace_dir(root, slug)
    if not ws.is_dir():
        return _err(
            f"no workspace at {ws} — create it by the provisioning step in "
            "skills/redteaming/references/formats.md § Feature workspace root "
            "and layout",
            2,
        )
    if number == 0:
        # Stdout stays the verdict channel; the note keeps a skip from
        # reading as a clean round.
        return _err(
            f"campaigns/{campaign}/{label} merges no seat reports — "
            "conservation check skipped (no verdict to record)",
            0,
        )
    round_dir = ws / "campaigns" / campaign / label
    if not round_dir.is_dir():
        return _err(
            f"no round directory at {round_dir} — check the phase and round "
            "arguments",
            2,
        )
    seats = [
        (m.group("seat"), path)
        for path in sorted(round_dir.iterdir())
        if (m := SEAT_REPORT_NAME_RE.match(path.name)) and path.is_file()
    ]
    if not seats:
        return _err(f"no seat reports (seat-<id>.md) in {round_dir}", 2)
    record_path = round_dir / "record.md"
    if not record_path.exists():
        return _err(f"no record.md in {round_dir}", 2)
    try:
        record = _without_verdicts(_read(record_path, "record"))
        reports = [(seat, path, _read(path, "seat report")) for seat, path in seats]
    except _ConserveError as exc:
        return _err(str(exc), 2)

    missing: dict[str, str] = {}
    for seat, path, text in reports:
        ids = _report_ids(text, seat)
        if not ids:
            _err(f"note: {path.name} carries no {seat}-<n> or {seat}-q<n> id", 0)
            continue
        accounted = _report_ids(record, seat)
        for key, spelled in ids.items():
            if key not in accounted:
                missing.setdefault(key, spelled)
    if missing:
        print("unaccounted: " + ", ".join(
            missing[key] for key in sorted(missing, key=_id_sort_key)
        ))
        return 1
    return 0


# --- CLI ----------------------------------------------------------------

# Prose elsewhere points at this text rather than restating the rules.
CONSERVE_DESCRIPTION = """\
Check one numbered panel round's merge by token presence: every finding and
question id the round's seat reports carry must occur in the round's
record.md. No markdown structure is read, and no layout of a readable
report stops the check.

Seat ids: one per seat-<id>.md file in the round directory, every such file
read, a lost or replaced seat's included (the plan phase's seat-p0.md is
one). Seat ids are never reused within a feature, the plan phase's p0
excepted, so a mention of one round's id never accounts for another
round's finding.
Ids collected per report: the whole tokens <id>-<n> and <id>-q<n> for that
report's own seat id, anywhere in the file; ids of other seats it mentions
are not collected from it.
Whole token, on both sides: not preceded or followed by a letter of any
script, a digit or a hyphen, so s1-2 matches none of s1-20, xs1-2 or
s1-2-3; an underscore is a boundary (_s1-2_ carries s1-2).
Accounted: the id occurs as a whole token in record.md, except in the text
after an 'unaccounted' label on the same line, wherever that line sits, so
a recorded verdict never accounts for the ids it names. The label is the
word unaccounted followed by its colon, with any whitespace, emphasis or
code-span markers between them (unaccounted:, Unaccounted:,
**unaccounted**:, `unaccounted`:, unaccounted :). Nothing else in the
record is excluded.
Matching is case-insensitive on both sides.

The phase is spec or plan; the round 01, 1 or round-01. Round 00 is
skipped: exit 0, a note on stderr, no verdict to record. A seat report
yielding no ids gets one note on stderr naming it; the exit code is
unaffected.

Exit codes:
  0  clean; nothing on stdout.
  1  unaccounted ids, and nothing else: one line on stdout,
     'unaccounted: <id>, ...', each id as its report wrote it, grouped per
     seat, findings before questions.
  2  the check cannot run, the reason on stderr: a usage error (an invalid
     slug, phase or round), no repository, no workspace, no round
     directory, no seat reports, no record.md, or an input that cannot be
     read, or read as UTF-8. Never because of what a seat report or the record says
     or how it is laid out.
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="conserve.py",
        description=CONSERVE_DESCRIPTION,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "feature_slug", help="lowercase hyphen-separated feature slug"
    )
    parser.add_argument(
        "campaign", choices=CAMPAIGNS, metavar="phase",
        help="the phase whose round to check: spec (the spec campaign) or "
        "plan (the plan phase)",
    )
    parser.add_argument(
        "round", help="numbered panel round: 01, 1, or round-01"
    )
    args = parser.parse_args(argv)

    slug: str = args.feature_slug
    if not SLUG_RE.match(slug):
        print(
            f"conserve: invalid feature slug {slug!r} — must match "
            "[a-z0-9]+(-[a-z0-9]+)* (lowercase, hyphen-separated)",
            file=sys.stderr,
        )
        return 2

    root = _repo_root()
    if root is None:
        return _err(
            "could not resolve the repo root (not inside a git checkout, or "
            "git is unavailable) — the workspace lives at "
            "<repo>/.crucible/<feature-slug>/, so run this from inside the "
            "target repo",
            2,
        )

    return cmd_conserve(root, slug, args.campaign, args.round)


if __name__ == "__main__":
    sys.exit(main())
