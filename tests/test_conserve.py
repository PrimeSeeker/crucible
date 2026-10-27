"""The merge-conservation check (``skills/redteaming/scripts/conserve.py``).

Every id a seat report carries must occur in the round's record outside an
``unaccounted:`` verdict -- clean rounds silent, misses named on stdout,
exit 2 only for a usage error or a missing or unreadable input, never for
how a report is laid out. ``--help`` carries that contract.

The check runs from any cwd inside the target repo. Nothing here touches a
real checkout: every repo is a throwaway temp git repo under pytest's
tmp_path.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "skills" / "redteaming" / "scripts" / "conserve.py"
SCRIPTS_DIR = SCRIPT.parent

sys.path.insert(0, str(SCRIPTS_DIR))

import conserve  # noqa: E402  (helper scripts are not a package)

pytestmark = pytest.mark.skipif(
    shutil.which("git") is None,
    reason="conservation-check tests need real git repos (git not on PATH)",
)

SLUG = "demo-feature"


# --- helpers ------------------------------------------------------------


def _git(repo: Path, *args: str) -> str:
    proc = subprocess.run(
        [
            "git",
            "-C",
            str(repo),
            "-c",
            "user.email=t7@test.invalid",
            "-c",
            "user.name=t7",
            *args,
        ],
        capture_output=True,
        text=True,
        timeout=60,
        stdin=subprocess.DEVNULL,
    )
    assert proc.returncode == 0, f"git {args} failed: {proc.stderr}"
    return proc.stdout


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    """A real temp git repo with one commit (so git status/ls-files work)."""
    root = tmp_path / "target-repo"
    root.mkdir()
    _git(root, "init", "-b", "main")
    (root / "README.md").write_text("target repo\n", encoding="utf-8")
    (root / "src").mkdir()
    (root / "src" / "app.py").write_text("x = 1\n", encoding="utf-8")
    _git(root, "add", ".")
    _git(root, "commit", "-m", "initial")
    return root


def _run(repo: Path, *argv: str, monkeypatch: pytest.MonkeyPatch) -> int:
    """Drive the check in-process from the repo root's cwd."""
    monkeypatch.chdir(repo)
    return conserve.main(list(argv))


def _ws(repo: Path, slug: str = SLUG) -> Path:
    return repo / ".crucible" / slug


# A round the conservation check reads clean: s1-1 and s2-1 merged as one
# entry, s1-2 its own, s2's question answered.
RECORD = """# Round record — spec campaign, round 01

state: merge

## Merged finding list

- M1 [MAJOR] stale cache — origins: s1-1, s2-1 — disposition: applied
- M2 [MINOR] naming drift — origins: s1-2 — disposition: parked

## Question dispositions

- s2-q1 — answered: per round
"""

SEAT_S1 = """## Verdict

Two findings.

## Findings

FINDING s1-1 [MAJOR] stale cache

FINDING s1-2 [MINOR] naming drift

## Questions

none
"""

SEAT_S2 = """## Findings

FINDING s2-1 [MAJOR] the cache is stale

## Questions

QUESTION s2-q1

Is the cap per round?
"""


# --- conserve -----------------------------------------------------------


# RECORD with the s1-2 entry gone: s1-2 is then accounted nowhere.
RECORD_WITHOUT_S1_2 = RECORD.replace(
    "- M2 [MINOR] naming drift — origins: s1-2 — disposition: parked\n", ""
)


def _round(
    repo: Path,
    *,
    phase: str = "spec",
    number: int = 1,
    record: str | bytes | None = RECORD,
    seats: dict[str, str | bytes] | None = None,
) -> Path:
    """Write one round directory: its record (unless None) and its
    ``seat-<id>.md`` reports (text, or raw bytes)."""
    if seats is None:
        seats = {"s1": SEAT_S1, "s2": SEAT_S2}
    rd = _ws(repo) / "campaigns" / phase / f"round-{number:02d}"
    rd.mkdir(parents=True, exist_ok=True)
    files = dict(seats.items())
    if record is not None:
        files["record"] = record
    for name, body in files.items():
        path = rd / ("record.md" if name == "record" else f"seat-{name}.md")
        if isinstance(body, bytes):
            path.write_bytes(body)
        else:
            path.write_text(body, encoding="utf-8")
    return rd


def _conserve(
    repo: Path,
    *args: str,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture,
) -> tuple[int, str, str]:
    """``conserve <args>`` (default: the spec phase's round 01) -> (exit
    code, stdout, stderr), setup chatter drained so a clean round's silence
    is conserve's own."""
    capsys.readouterr()
    rc = _run(repo, *(args or (SLUG, "spec", "01")), monkeypatch=monkeypatch)
    captured = capsys.readouterr()
    return rc, captured.out, captured.err


def _provisioned(repo: Path) -> None:
    _ws(repo).mkdir(parents=True)


class TestConserve:
    """Break: a seat id the record never mentions passing as clean (the
    merging controller's silent drop), a mention not counting, an id
    counted from the wrong seat or from a recorded verdict, or a report's
    layout stopping the check."""

    # --- clean -----------------------------------------------------------

    @pytest.mark.parametrize("phase", ["spec", "plan"])
    @pytest.mark.parametrize("round_arg", ["01", "1", "round-01"])
    def test_clean_round_is_silent(
        self, repo: Path, monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture, phase: str, round_arg: str
    ) -> None:
        _provisioned(repo)
        _round(repo, phase=phase)
        assert _conserve(
            repo, SLUG, phase, round_arg, monkeypatch=monkeypatch, capsys=capsys
        ) == (0, "", "")

    # --- unaccounted ids --------------------------------------------------

    def test_unaccounted_finding_id_is_named(
        self, repo: Path, monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture
    ) -> None:
        _provisioned(repo)
        _round(repo, record=RECORD_WITHOUT_S1_2)
        assert _conserve(repo, monkeypatch=monkeypatch, capsys=capsys) == (
            1, "unaccounted: s1-2\n", ""
        )

    def test_unaccounted_question_id_is_named(
        self, repo: Path, monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture
    ) -> None:
        _provisioned(repo)
        _round(repo, record=RECORD.replace("- s2-q1 — answered: per round\n", ""))
        assert _conserve(repo, monkeypatch=monkeypatch, capsys=capsys) == (
            1, "unaccounted: s2-q1\n", ""
        )

    def test_every_unaccounted_id_shares_one_line_grouped_per_seat(
        self, repo: Path, monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture
    ) -> None:
        """Per seat, findings in numeric order (s1-2 before s1-10), then
        questions; ids as the report wrote them."""
        _provisioned(repo)
        _round(
            repo,
            record="origins: s1-1\n",
            seats={
                "s2": "FINDING s2-1 [MAJOR]\n",
                "s1": "s1-q1 s1-10 s1-1 S1-2 s1-q1\n",
            },
        )
        assert _conserve(repo, monkeypatch=monkeypatch, capsys=capsys) == (
            1, "unaccounted: S1-2, s1-10, s1-q1, s2-1\n", ""
        )

    def test_a_lost_seats_file_is_read(
        self, repo: Path, monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture
    ) -> None:
        """A seat lost mid-round leaves a partial report; its ids count."""
        _provisioned(repo)
        _round(
            repo,
            seats={"s1": SEAT_S1, "s2": SEAT_S2, "s3": "FINDING s3-1 [MAJ"},
        )
        assert _conserve(repo, monkeypatch=monkeypatch, capsys=capsys) == (
            1, "unaccounted: s3-1\n", ""
        )

    # --- matching ---------------------------------------------------------

    @pytest.mark.parametrize(
        ("seat", "report", "record"),
        [
            ("s1", "FINDING S1-1 [MAJOR]", "origins: s1-1"),
            ("s1", "FINDING s1-1 [MAJOR]", "origins: S1-1"),
            ("S1", "FINDING s1-1 [MAJOR]", "origins: s1-1"),
            ("s1", "QUESTION S1-Q1", "- s1-q1 — answered: yes"),
        ],
        ids=["report-upper", "record-upper", "filename-upper", "question-upper"],
    )
    def test_matching_is_case_insensitive_on_both_sides(
        self, repo: Path, monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture, seat: str, report: str, record: str
    ) -> None:
        _provisioned(repo)
        _round(repo, record=record + "\n", seats={seat: report + "\n"})
        # No stderr note: the report's id was collected, and accounted.
        assert _conserve(repo, monkeypatch=monkeypatch, capsys=capsys) == (0, "", "")

    @pytest.mark.parametrize(
        "token",
        ["xs1-2", "s1-2-3", "-s1-2", "s1-2x", "1s1-2", "s1-2Я", "Яs1-2", "s1-2é"],
    )
    def test_a_report_token_inside_a_longer_word_is_no_id(
        self, repo: Path, monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture, token: str
    ) -> None:
        _provisioned(repo)
        _round(
            repo,
            record="origins: s1-1\n",
            seats={"s1": f"FINDING s1-1 [MAJOR] see {token}\n"},
        )
        assert _conserve(repo, monkeypatch=monkeypatch, capsys=capsys) == (0, "", "")

    @pytest.mark.parametrize(
        ("token", "named"),
        [
            ("_s1-2_", "s1-2"),
            ("x_s1-2", "s1-2"),
            ("(s1-2)", "s1-2"),
            ("**s1-2**", "s1-2"),
            ("`s1-2`", "s1-2"),
            ("s1-2.", "s1-2"),
            ("s1-20", "s1-20"),
        ],
    )
    def test_a_report_token_between_boundaries_is_an_id(
        self, repo: Path, monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture, token: str, named: str
    ) -> None:
        _provisioned(repo)
        _round(
            repo,
            record="origins: s1-1\n",
            seats={"s1": f"FINDING s1-1 [MAJOR] see {token}\n"},
        )
        assert _conserve(repo, monkeypatch=monkeypatch, capsys=capsys) == (
            1, f"unaccounted: {named}\n", ""
        )

    @pytest.mark.parametrize(
        "mention",
        ["s1-20", "xs1-2", "s1-2-3", "-s1-2", "s1-2x", "1s1-2", "s1-2Я", "Яs1-2"],
    )
    def test_a_record_token_inside_a_longer_word_does_not_account(
        self, repo: Path, monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture, mention: str
    ) -> None:
        _provisioned(repo)
        _round(repo, record=RECORD_WITHOUT_S1_2 + f"\nsee {mention}\n")
        assert _conserve(repo, monkeypatch=monkeypatch, capsys=capsys) == (
            1, "unaccounted: s1-2\n", ""
        )

    @pytest.mark.parametrize(
        "mention", ["s1-2", "_s1-2_", "x_s1-2", "(s1-2)", "**s1-2**", "`s1-2`", "S1-2."]
    )
    def test_a_record_token_between_boundaries_accounts(
        self, repo: Path, monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture, mention: str
    ) -> None:
        _provisioned(repo)
        _round(repo, record=RECORD_WITHOUT_S1_2 + f"\nsee {mention}\n")
        assert _conserve(repo, monkeypatch=monkeypatch, capsys=capsys) == (0, "", "")

    def test_another_seats_prefix_in_a_report_is_not_collected(
        self, repo: Path, monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture
    ) -> None:
        _provisioned(repo)
        _round(
            repo,
            record="origins: s1-1, s2-1\n",
            seats={
                "s1": "FINDING s1-1 [MAJOR] duplicate of s2-5 and t9-q1\n",
                "s2": "FINDING s2-1 [MAJOR]\n",
            },
        )
        assert _conserve(repo, monkeypatch=monkeypatch, capsys=capsys) == (0, "", "")

    # --- the recorded verdict ---------------------------------------------

    @pytest.mark.parametrize(
        "verdict",
        [
            "unaccounted: s1-2",
            "- unaccounted: s1-2",
            "**unaccounted:** s1-2",
            "**unaccounted**: s1-2",
            "_unaccounted_: s1-2",
            "Unaccounted: s1-2",
            "UNACCOUNTED: s1-2",
            "`unaccounted`: s1-2",
            "unaccounted : s1-2",
            "    unaccounted: s1-2",
            "conservation: 3 raw → 2 merged; unaccounted: s1-2",
            "conservation: 3 raw seat findings → 2 merged\n  entries;\nunaccounted: s1-2",
        ],
        ids=[
            "bare", "bulleted", "bold-colon-inside", "bold-colon-outside",
            "underscore-emphasis", "capitalised", "upper", "code-spanned",
            "space-before-colon", "indented", "on-the-conservation-line",
            "own-line-after-wrapped-conservation-line",
        ],
    )
    def test_an_earlier_verdict_does_not_account_its_ids(
        self, repo: Path, monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture, verdict: str
    ) -> None:
        _provisioned(repo)
        _round(repo, record=RECORD_WITHOUT_S1_2 + f"\n## Quorum block\n\n{verdict}\n")
        assert _conserve(repo, monkeypatch=monkeypatch, capsys=capsys) == (
            1, "unaccounted: s1-2\n", ""
        )

    def test_an_id_in_the_conservation_arithmetic_is_accounted(
        self, repo: Path, monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture
    ) -> None:
        """Only the text after the label is excluded: s1-2, named before it,
        is accounted; s3-1, named after it, is not."""
        _provisioned(repo)
        _round(
            repo,
            record=RECORD_WITHOUT_S1_2
            + "\nconservation: 4 raw → 2 merged (s1-2 duplicate of s1-1); "
            "unaccounted: s3-1\n",
            seats={"s1": SEAT_S1, "s2": SEAT_S2, "s3": "FINDING s3-1 [MINOR]\n"},
        )
        assert _conserve(repo, monkeypatch=monkeypatch, capsys=capsys) == (
            1, "unaccounted: s3-1\n", ""
        )

    def test_the_exclusion_ends_at_the_end_of_its_line(
        self, repo: Path, monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture
    ) -> None:
        """Break: the exclusion running past its line, so an id merged on a
        later line after an earlier verdict reads as still unaccounted."""
        _provisioned(repo)
        _round(
            repo,
            record=RECORD_WITHOUT_S1_2
            + "\nunaccounted: s1-2\n- E9 MINOR — origins: s1-2 — merged late\n",
        )
        assert _conserve(repo, monkeypatch=monkeypatch, capsys=capsys) == (
            0, "", ""
        )

    def test_the_label_needs_its_colon(
        self, repo: Path, monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture
    ) -> None:
        """Break: a bare word 'unaccounted' cutting its line, so a sentence
        that merges the id is excluded and the id reads as dropped."""
        _provisioned(repo)
        _round(
            repo,
            record=RECORD_WITHOUT_S1_2
            + "\nThe once unaccounted s1-2 is merged into E9.\n",
        )
        assert _conserve(repo, monkeypatch=monkeypatch, capsys=capsys) == (
            0, "", ""
        )

    # --- notes and skips --------------------------------------------------

    def test_a_report_with_no_ids_is_noted_on_stderr(
        self, repo: Path, monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture
    ) -> None:
        _provisioned(repo)
        _round(
            repo,
            seats={
                "s1": SEAT_S1,
                "s2": "## Findings\n\nnone\n\n## Questions\n\nnone\n",
            },
        )
        rc, out, err = _conserve(repo, monkeypatch=monkeypatch, capsys=capsys)
        assert (rc, out) == (0, "")
        assert "seat-s2.md" in err
        assert "seat-s1.md" not in err

    @pytest.mark.parametrize("round_arg", ["00", "0", "round-00"])
    def test_round_00_is_skipped(
        self, repo: Path, monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture, round_arg: str
    ) -> None:
        _provisioned(repo)
        _round(repo, number=0, record="nothing merged\n")
        rc, out, err = _conserve(
            repo, SLUG, "spec", round_arg, monkeypatch=monkeypatch, capsys=capsys
        )
        assert (rc, out) == (0, "")
        assert "round-00" in err

    # --- exit 2: usage, missing or unreadable input ------------------------

    @pytest.mark.parametrize(
        "case",
        [
            "invalid-round",
            "no-workspace",
            "no-round-directory",
            "no-seat-reports",
            "no-record",
            "record-is-a-directory",
            "record-not-utf8",
            "seat-report-not-utf8",
        ],
    )
    def test_usage_error_or_missing_input_exits_2(
        self, repo: Path, monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture, case: str
    ) -> None:
        args = (SLUG, "spec", "01")
        if case == "invalid-round":
            args = (SLUG, "spec", "terminal-pass")
        if case != "no-workspace":
            _provisioned(repo)
        if case == "no-seat-reports":
            _round(repo, seats={})
        elif case == "no-record":
            _round(repo, record=None)
        elif case == "record-is-a-directory":
            (_round(repo, record=None) / "record.md").mkdir()
        elif case == "record-not-utf8":
            _round(repo, record=RECORD.encode("utf-8") + b"\xff\xfe s1-2\n")
        elif case == "seat-report-not-utf8":
            _round(repo, seats={"s1": SEAT_S1, "s2": b"FINDING s2-1 \xff\n"})
        rc, out, err = _conserve(repo, *args, monkeypatch=monkeypatch, capsys=capsys)
        assert (rc, out) == (2, "")
        assert err.strip() != ""

    @pytest.mark.parametrize(
        "bad_slug",
        ["Bad-Slug", "spaces here", "trailing-", "-leading", "a--b", "dots.in", "../up"],
    )
    def test_invalid_slug_exits_2(
        self, repo: Path, monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture, bad_slug: str
    ) -> None:
        # A slug beginning with '-' is refused by argparse itself
        # (SystemExit 2); the rest by the slug check, beside a valid round.
        _provisioned(repo)
        _round(repo)
        capsys.readouterr()
        try:
            rc = _run(repo, bad_slug, "spec", "01", monkeypatch=monkeypatch)
        except SystemExit as exc:
            rc = exc.code
        captured = capsys.readouterr()
        assert (rc, captured.out) == (2, "")
        if not bad_slug.startswith("-"):
            assert "invalid feature slug" in captured.err

    @pytest.mark.parametrize(
        "argv",
        [(SLUG, "terminal", "01"), (SLUG, "spec"), (SLUG,)],
        ids=["unknown-phase", "no-round", "no-phase"],
    )
    def test_malformed_command_line_exits_2(
        self, repo: Path, monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture, argv: tuple[str, ...]
    ) -> None:
        _provisioned(repo)
        _round(repo)
        capsys.readouterr()
        with pytest.raises(SystemExit) as exc:
            _run(repo, *argv, monkeypatch=monkeypatch)
        assert exc.value.code == 2
        assert capsys.readouterr().out == ""

    def test_outside_a_repository_exits_2(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture
    ) -> None:
        plain = tmp_path / "not-a-repo"
        rd = plain / ".crucible" / SLUG / "campaigns" / "spec" / "round-01"
        rd.mkdir(parents=True)
        (rd / "record.md").write_text(RECORD, encoding="utf-8")
        (rd / "seat-s1.md").write_text(SEAT_S1, encoding="utf-8")
        monkeypatch.chdir(plain)
        capsys.readouterr()
        assert conserve.main([SLUG, "spec", "01"]) == 2
        captured = capsys.readouterr()
        assert captured.out == ""
        assert "git" in captured.err.lower()

    def test_no_workspace_points_at_the_provisioning_step(
        self, repo: Path, monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture
    ) -> None:
        """Break: the no-workspace reason sending its reader to a step that
        does not exist -- a removed command, or a section the cited
        reference no longer has."""
        rc, out, err = _conserve(repo, monkeypatch=monkeypatch, capsys=capsys)
        assert (rc, out) == (2, "")
        cited = re.search(r"(skills/\S+\.md) § (.+?)\s*$", err)
        assert cited is not None, err
        path, heading = cited.groups()
        text = (REPO_ROOT / path).read_text(encoding="utf-8")
        assert re.search(rf"^## {re.escape(heading)}$", text, re.M), (path, heading)

    def test_help_is_the_contract_under_the_scripts_own_name(
        self, tmp_path: Path
    ) -> None:
        """Break: ``--help`` losing the contract text the prose sends its
        readers to, or naming a program other than the one the prose runs."""
        env = {k: v for k, v in os.environ.items() if k != "FORCE_COLOR"}
        env["PYTHON_COLORS"] = "0"
        proc = subprocess.run(
            [sys.executable, str(SCRIPT), "--help"],
            cwd=str(tmp_path),
            env=env,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=60,
            stdin=subprocess.DEVNULL,
        )
        assert (proc.returncode, proc.stderr) == (0, "")
        assert proc.stdout.startswith("usage: conserve.py "), proc.stdout
        assert conserve.CONSERVE_DESCRIPTION in proc.stdout

    # --- no layout of a readable report stops the check ---------------------

    @pytest.mark.parametrize(
        "report",
        [
            "The cache is stale (s1-1). Naming drifts (s1-2).\n",
            "Finding s1-1 [MAJOR] stale\nFINDING: s1-2 MINOR\n",
            "# Findings\n## 2. Findings\n### FINDING s1-1\n## Appendix\ns1-2\n",
            "## Index\n- s1-1 [BLOCKER]\n- s1-2 [MAJOR]\n## Findings\n"
            "FINDING s1-1 [MINOR]\n",
            "```\nFINDING s1-1 [MAJOR]\n```\n~~~\ns1-2\n~~~\n",
            "FINDING s1-1 [MAJOR]\r\n\r\nFINDING s1-2 [MINOR]\r\n",
            "﻿s1-1 s1-2\n",
            "```\ns1-1\x00s1-2",
            "FINDING s1-1[MAJOR\nQUESTION about s1-2: and this?\n",
        ],
        ids=[
            "prose-only", "keyword-headers", "stray-headings",
            "index-disagreeing", "fenced", "crlf", "byte-order-mark",
            "unterminated-fence-and-nul", "malformed-headers",
        ],
    )
    def test_any_readable_report_layout_is_checked(
        self, repo: Path, monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture, report: str
    ) -> None:
        _provisioned(repo)
        _round(repo, record=RECORD_WITHOUT_S1_2, seats={"s1": report})
        assert _conserve(repo, monkeypatch=monkeypatch, capsys=capsys) == (
            1, "unaccounted: s1-2\n", ""
        )

    def test_cli_form_from_subdir_reports_the_miss_on_stdout(
        self, repo: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        _provisioned(repo)
        _round(repo, record=RECORD_WITHOUT_S1_2)
        proc = subprocess.run(
            [sys.executable, str(SCRIPT), SLUG, "spec", "01"],
            cwd=str(repo / "src"),
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=60,
            stdin=subprocess.DEVNULL,
        )
        assert (proc.returncode, proc.stdout, proc.stderr) == (
            1, "unaccounted: s1-2\n", ""
        )
