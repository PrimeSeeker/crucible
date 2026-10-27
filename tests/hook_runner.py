"""Running the SessionStart hook script from tests.

The hook is a bash script, so every test that runs it needs a bash, and
the bash on PATH is not always one that can run it. On Windows the default
PATH puts WSL's launcher, ``System32\\bash.exe``, ahead of Git for Windows'
bash; WSL's bash cannot open a Windows path and exits 1. So no candidate
is trusted by name: each is made to run a probe script, and the first that
runs it is the bash these tests use. Git for Windows' bash is tried ahead
of PATH's on Windows, located from the running ``git``'s own install.

Every child these helpers start gets its own stdin. Under pytest's default
fd capture on Windows, the process's standard input handle can name a
closed handle, or a handle since reused for an unrelated file; a child
left to inherit it fails to start with WinError 6, or reads that file.

Without a usable bash, ``find_bash`` returns ``None`` and the hook-running
tests skip with ``no_bash_reason()``, which names each candidate tried and
what failed for it.
"""

from __future__ import annotations

import functools
import json
import os
import shutil
import subprocess
import sys
import tempfile
from collections.abc import Iterable
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
HOOK_SCRIPT = REPO_ROOT / "hooks" / "session-start"
HOST = "claude-code"

# The lead of every skip reason; ``no_bash_reason`` appends the failures.
NO_BASH_REASON = "no bash that runs a script file was found"

_PROBE_OUTPUT = "crucible-bash-probe"
_PROBE_TIMEOUT = 30


def _git_bash_candidates() -> list[Path]:
    """Git for Windows' bash, located from the install the running ``git``
    belongs to, then from the default install directories."""
    roots: list[Path] = []
    try:
        exec_path = subprocess.run(
            ["git", "--exec-path"],
            stdin=subprocess.DEVNULL,
            capture_output=True,
            text=True,
            timeout=30,
        ).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        exec_path = ""
    if exec_path:
        # <root>/<mingw64|ucrt64|...>/libexec/git-core: the install root is
        # an ancestor; walk up rather than assume the depth.
        roots.extend(Path(exec_path).parents)
    for variable in ("ProgramW6432", "ProgramFiles", "ProgramFiles(x86)"):
        base = os.environ.get(variable)
        if base:
            roots.append(Path(base) / "Git")
    local = os.environ.get("LOCALAPPDATA")
    if local:
        roots.append(Path(local) / "Programs" / "Git")
    candidates: list[Path] = []
    for root in roots:
        for rel in ("bin/bash.exe", "usr/bin/bash.exe"):
            candidate = root / rel
            if candidate not in candidates and candidate.is_file():
                candidates.append(candidate)
    return candidates


def _candidates() -> list[str]:
    found: list[str] = []
    if sys.platform == "win32":
        found.extend(str(p) for p in _git_bash_candidates())
    on_path = shutil.which("bash")
    if on_path:
        found.append(on_path)
    if sys.platform != "win32":
        found.append("/bin/bash")
    unique: list[str] = []
    seen: set[str] = set()
    for candidate in found:
        key = os.path.normcase(os.path.normpath(candidate))
        if key not in seen:
            seen.add(key)
            unique.append(candidate)
    return unique


def _probe_failure(bash: str, script: Path) -> str | None:
    """``None`` when ``bash`` runs the probe script; otherwise what failed."""
    try:
        proc = subprocess.run(
            [bash, str(script)],
            stdin=subprocess.DEVNULL,
            capture_output=True,
            timeout=_PROBE_TIMEOUT,
        )
    except subprocess.TimeoutExpired:
        return f"timed out after {_PROBE_TIMEOUT}s"
    except (OSError, subprocess.SubprocessError) as exc:
        return f"did not start: {exc!r}"
    if proc.returncode == 0 and proc.stdout == _PROBE_OUTPUT.encode():
        return None
    # WSL's launcher writes UTF-16LE; dropping the NULs keeps it readable.
    stdout = proc.stdout.replace(b"\x00", b"").decode("utf-8", "replace")
    failure = f"exit {proc.returncode}, stdout {stdout[:120]!r}"
    stderr = proc.stderr.replace(b"\x00", b"").decode("utf-8", "replace").strip().splitlines()
    if stderr:
        failure += f", stderr ending {stderr[-1][:200]!r}"
    return failure


def probe(candidates: Iterable[str]) -> tuple[str | None, str]:
    """The first of ``candidates`` that runs a probe script, and ``""``; or,
    when none does, ``None`` and the skip reason naming each candidate and
    what failed for it."""
    failures: list[str] = []
    with tempfile.TemporaryDirectory() as tmp:
        script = Path(tmp) / "probe"
        # Prints only under bash: BASH_VERSION is unset in any other shell.
        script.write_bytes(
            b'[ -n "$BASH_VERSION" ] && printf %s ' + _PROBE_OUTPUT.encode() + b"\n"
        )
        for candidate in candidates:
            failure = _probe_failure(candidate, script)
            if failure is None:
                return candidate, ""
            failures.append(f"{candidate}: {failure}")
    if not failures:
        return None, f"{NO_BASH_REASON}: no candidate bash to try"
    return None, f"{NO_BASH_REASON}: " + "; ".join(failures)


@functools.cache
def _found() -> tuple[str | None, str]:
    return probe(_candidates())


def find_bash() -> str | None:
    """The first candidate bash that runs a probe script, or ``None``."""
    return _found()[0]


def no_bash_reason() -> str:
    """Why ``find_bash`` found none: each candidate and what failed for it."""
    return _found()[1]


def run_hook(
    script: Path = HOOK_SCRIPT,
    *args: str,
    stdin: str = "",
) -> subprocess.CompletedProcess[str]:
    """Run ``script`` under the found bash with ``args``, as the host does:
    stdout and stderr captured, decoded as UTF-8."""
    bash = find_bash()
    assert bash is not None, no_bash_reason()
    return subprocess.run(
        [bash, script.as_posix(), *args],
        input=stdin,
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=60,
    )


def additional_context(proc: subprocess.CompletedProcess[str]) -> str:
    """The ``additionalContext`` of a successful run's SessionStart
    document, after checking the document's shape."""
    assert proc.returncode == 0, proc.stderr
    assert proc.stderr == "", f"unexpected stderr: {proc.stderr!r}"
    document = json.loads(proc.stdout)
    assert set(document) == {"hookSpecificOutput"}, document.keys()
    out = document["hookSpecificOutput"]
    assert set(out) == {"hookEventName", "additionalContext"}, out.keys()
    assert out["hookEventName"] == "SessionStart"
    context = out["additionalContext"]
    assert isinstance(context, str)
    return context


@functools.cache
def envelope() -> str:
    """The envelope the repository's own hook emits for this tree."""
    return additional_context(run_hook(HOOK_SCRIPT, HOST))
