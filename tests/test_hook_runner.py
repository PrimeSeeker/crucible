"""``tests/hook_runner.py``'s bash probe, which decides whether the hook
tests run or skip.

Covers:

- an inherited standard input that is no usable handle does not stop the
  probe finding the bash: pytest's default fd capture leaves the process's
  Win32 standard input handle naming a closed handle, and a child started
  without its own stdin inherits it;
- a candidate that cannot run the probe script is passed over for one that
  can;
- with no candidate that runs the probe script, the skip reason names each
  candidate and what failed for it.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

TESTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(TESTS_DIR))

import hook_runner as hr  # noqa: E402  (path inserted above; not a package)

# Leaves the process with no usable standard input, then prints what
# find_bash finds. On Windows the Win32 standard input handle is set to
# INVALID_HANDLE_VALUE, the state a closed inherited stdin gives (a child
# started without its own stdin then fails to start with WinError 6); off
# Windows fd 0 is closed.
_INVALID_STDIN_CHILD = r"""
import os
import sys

sys.path.insert(0, sys.argv[1])
if sys.platform == "win32":
    import ctypes

    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    kernel32.SetStdHandle.argtypes = [ctypes.c_uint32, ctypes.c_void_p]
    kernel32.SetStdHandle.restype = ctypes.c_int
    STD_INPUT_HANDLE = 0xFFFFFFF6  # (DWORD)-10
    INVALID_HANDLE_VALUE = ctypes.c_void_p(-1).value
    if not kernel32.SetStdHandle(STD_INPUT_HANDLE, INVALID_HANDLE_VALUE):
        raise ctypes.WinError(ctypes.get_last_error())
else:
    os.close(0)
import hook_runner

print(hook_runner.find_bash())
"""


def test_probe_finds_bash_with_no_usable_stdin() -> None:
    """The break: a probe that lets its child inherit standard input, so an
    invalid inherited handle reads as "no bash" and every hook test skips."""
    bash = hr.find_bash()
    if bash is None:
        pytest.skip(hr.no_bash_reason())
    proc = subprocess.run(
        [sys.executable, "-c", _INVALID_STDIN_CHILD, str(TESTS_DIR)],
        stdin=subprocess.DEVNULL,
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert proc.returncode == 0, proc.stderr
    assert proc.stdout.strip() == bash


def test_probe_passes_over_a_candidate_that_cannot_run_the_script(tmp_path: Path) -> None:
    """A missing executable ahead of a working bash: the working one wins."""
    bash = hr.find_bash()
    if bash is None:
        pytest.skip(hr.no_bash_reason())
    missing = str(tmp_path / "no-such-bash.exe")
    assert hr.probe([missing, bash]) == (bash, "")


def test_skip_reason_names_each_candidate_and_what_failed(tmp_path: Path) -> None:
    """The break: a skip reason that says only "no bash", hiding the cause.

    Two candidates fail in different ways: one does not exist, so it never
    starts; the other is Python, which starts, cannot parse the bash probe
    script and exits 1 with a SyntaxError on stderr.
    """
    missing = str(tmp_path / "no-such-bash.exe")
    not_bash = sys.executable

    bash, reason = hr.probe([missing, not_bash])

    assert bash is None
    # Reader: pytest prints this reason in the -rs skip summary that
    # pytest.ini turns on; it must say what failed, per candidate.
    assert reason.startswith(hr.NO_BASH_REASON), reason
    missing_part, not_bash_part = reason[len(hr.NO_BASH_REASON) :].split("; ")
    assert missing in missing_part, reason
    assert "FileNotFoundError" in missing_part, reason
    assert not_bash in not_bash_part, reason
    assert "exit 1" in not_bash_part, reason
    assert "SyntaxError" in not_bash_part, reason


def test_skip_reason_with_no_candidate_says_none_was_found() -> None:
    bash, reason = hr.probe([])
    assert bash is None
    # Reader: pytest's -rs skip summary (pytest.ini).
    assert reason.startswith(hr.NO_BASH_REASON), reason
    assert "no candidate" in reason, reason
