"""The claudeism scanner over the finished tree, the hook script included.

The scanner CLI is run here as a real process over the real tree, so a
Claude-ism in shared text or in the text the hook emits without an
allowlist entry fails the ordinary suite. Nothing below launches a model, a
subagent or the hook.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
TESTS_DIR = Path(__file__).resolve().parent
SCANNER = TESTS_DIR / "claudeism_scanner.py"

sys.path.insert(0, str(TESTS_DIR))

import claudeism_scanner as cs  # noqa: E402  (path inserted above)


def test_scanner_cli_reports_no_unallowlisted_match_over_the_finished_tree(
    tmp_path: Path,
) -> None:
    """The scanner gate as an operator runs it: the real CLI, as its own
    process, over the finished tree -- shared workflow files AND the
    SessionStart hook script, where the envelope's lead line lives.

    The break: any Claude-ism surviving in shared text or in emitted hook
    output without a per-term-per-location allowlist entry justifying it.
    Run from a directory that is not the repo root, so a CLI that silently
    resolved its corpus from the working directory rather than from its
    own location would come back with an empty scan instead of a pass.
    """
    proc = subprocess.run(
        [sys.executable, str(SCANNER)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        cwd=str(tmp_path),
        stdin=subprocess.DEVNULL,
        timeout=300,
    )
    assert proc.returncode == 0, f"{proc.stdout}\n{proc.stderr}"

    # The same scan in process, so a failure names the offending matches
    # instead of only an exit code -- and so an empty corpus cannot pass.
    allowlist = cs.load_allowlist()
    matches = cs.scan_tree(REPO_ROOT)
    reported = cs.unallowlisted(matches, allowlist)
    assert reported == [], "\n".join(match.render() for match in reported)
    assert allowlist.entries, "an empty allowlist would allow nothing to be checked"
    assert matches, "an empty scan corpus would pass vacuously"

    # THE HOOK SCRIPT REALLY IS IN THE CORPUS. The envelope is the two
    # router files, scanned as .md sources, plus a lead line that lives only
    # in the hook script; the scanner reads the script rather than running
    # it. Seeded with a term in a copy of the tree, so the check has a way
    # to fail: a corpus assembled without the script reports nothing there.
    scanned = cs.collect_sources(REPO_ROOT)
    hook = REPO_ROOT / cs.HOOK_SCRIPT
    assert scanned.get(cs.HOOK_SCRIPT) == hook.read_text(encoding="utf-8"), (
        "the hook script was not scanned"
    )
    for name in ("skills", "hooks"):
        shutil.copytree(REPO_ROOT / name, tmp_path / "tree" / name)
    seeded_hook = tmp_path / "tree" / cs.HOOK_SCRIPT
    with seeded_hook.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write("# Dispatch on Opus.\n")
    seeded = cs.unallowlisted(cs.scan_tree(tmp_path / "tree"), allowlist)
    assert [(m.term, m.location) for m in seeded] == [("opus", cs.HOOK_SCRIPT)], (
        "a Claude-ism placed in the hook script was not reported, so the "
        "hook half of this gate proves nothing"
    )

    # A CODEX MODEL NAME IN A SKILL FAILS THE GATE TOO: skills name roles,
    # and only the adapter pair names models. Seeded in a skill outside the
    # adapters with a bare line name and a slug no term names, so neither
    # the line-name terms nor the generic slug pattern can be lost unseen.
    skill = "skills/subagent-driven-development/SKILL.md"
    with (tmp_path / "tree" / skill).open("a", encoding="utf-8", newline="\n") as handle:
        handle.write("Dispatch the reviewer on Astra, or on gpt-7-nova.\n")
    seeded = cs.unallowlisted(cs.scan_tree(tmp_path / "tree"), allowlist)
    assert [(m.term, m.location) for m in seeded] == [
        ("astra", skill),
        ("codex-model-slug", skill),
        ("opus", cs.HOOK_SCRIPT),
    ], "a Codex model name placed in a skill was not reported"
