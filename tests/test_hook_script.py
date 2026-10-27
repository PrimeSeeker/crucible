"""The SessionStart registration and ``hooks/session-start``, the hook script.

Covers:

- the registration's shape: one shell-form command, ``bash`` running the
  script with its host named as the argument, the script anchored at the
  plugin root (the whole registration is pinned once, in
  ``tests/test_codex_manifests.py``); the script is LF-only and
  ``.gitattributes`` keeps it so on any checkout;
- the document: the ``claude-code`` arm prints one SessionStart document
  whose ``additionalContext`` is the lead line, the router, ``---`` and
  the host map, assembled here from the tree's files; on a relocated tree,
  router text carrying every character the escaping handles comes back
  exactly, with each CRLF and lone CR turned into LF;
- failure: a missing or unreadable router file, a missing host map, an
  unknown or missing host argument, and a closed stdout each exit 1 with
  one ``crucible: router not loaded:`` stderr line and nothing on stdout;
- end to end: the registered command, its placeholder substituted the way
  the host substitutes it, run through ``bash -c`` the way the host runs a
  shell-form hook, emits the envelope.

Every run needs a bash that runs a script file (``tests/hook_runner.py``
finds one); without one, the tests that run the hook skip.
"""

from __future__ import annotations

import json
import os
import shlex
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

TESTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(TESTS_DIR))

import hook_runner as hr  # noqa: E402  (path inserted above; not a package)

REPO_ROOT = TESTS_DIR.parent
HOOKS_JSON = REPO_ROOT / "hooks" / "hooks.json"
SCRIPT = REPO_ROOT / "hooks" / "session-start"
ROUTER_REL = Path("skills") / "using-crucible" / "SKILL.md"
HOST_MAP_REL = Path("skills") / "using-crucible" / "references" / "claude-code.md"
PLACEHOLDER = "${CLAUDE_PLUGIN_ROOT}"

LEAD = (
    "You have crucible. Below: the using-crucible skill, then this host's "
    "runtime reference. Read both before acting."
)

needs_bash = pytest.mark.skipif(hr.find_bash() is None, reason=hr.no_bash_reason())


def _registered_command() -> str:
    data = json.loads(HOOKS_JSON.read_text(encoding="utf-8"))
    (group,) = data["hooks"]["SessionStart"]
    (hook,) = group["hooks"]
    assert "args" not in hook, "the registration is shell form: no args"
    return hook["command"]


# --- the registration and the script file -------------------------------


def test_registration_runs_the_script_under_bash_naming_its_host() -> None:
    """``bash <script> claude-code``: the script anchored at the plugin root
    and present on disk, and the host named by the registration."""
    # Consumer: the host's plugin hook loader reads hooks/hooks.json.
    argv = shlex.split(_registered_command())
    assert argv[0] == "bash"
    assert argv[2:] == ["claude-code"]
    word = argv[1]
    assert word.startswith(PLACEHOLDER + "/"), word
    assert REPO_ROOT / word[len(PLACEHOLDER) + 1 :] == SCRIPT
    assert SCRIPT.is_file(), f"registered script missing: {word}"


def test_hook_script_is_lf_only() -> None:
    """A CR in a bash script breaks it."""
    assert b"\r" not in SCRIPT.read_bytes()


@pytest.mark.skipif(shutil.which("git") is None, reason="git not on PATH")
def test_hook_script_is_pinned_lf_in_gitattributes() -> None:
    """A CRLF checkout (``core.autocrlf=true``) would put a CR on every
    line of the script unless ``.gitattributes`` pins it to LF."""
    proc = subprocess.run(
        ["git", "check-attr", "eol", "--", "hooks/session-start"],
        cwd=REPO_ROOT,
        stdin=subprocess.DEVNULL,  # the inherited stdin can be an invalid handle
        capture_output=True,
        text=True,
        timeout=60,
    )
    assert proc.returncode == 0, proc.stderr
    assert proc.stdout.strip() == "hooks/session-start: eol: lf"


# --- the document ---------------------------------------------------------


@needs_bash
def test_envelope_is_the_lead_line_router_and_host_map() -> None:
    """The ``claude-code`` arm's context is assembled from the tree's two
    files exactly: lead line, blank line, router, ``---``, blank line, host
    map. Non-ASCII (the router's em dashes) arrives intact through the
    UTF-8 decode of stdout."""
    router = (REPO_ROOT / ROUTER_REL).read_text(encoding="utf-8")
    host_map = (REPO_ROOT / HOST_MAP_REL).read_text(encoding="utf-8")
    want = f"{LEAD}\n\n{router}\n---\n\n{host_map}"
    assert hr.additional_context(hr.run_hook(SCRIPT, "claude-code")) == want


@needs_bash
def test_hook_ignores_stdin() -> None:
    """The host writes a JSON payload on stdin; the script reads none of
    it, so garbage there changes nothing."""
    proc = hr.run_hook(SCRIPT, "claude-code", stdin="not json {{{")
    assert hr.additional_context(proc) == hr.envelope()


def _relocate(tmp_path: Path, *, router: bytes | None, host_map: bytes | None) -> Path:
    """Copy the script into an isolated plugin-shaped tree holding the given
    router and host-map bytes (``None``: the file is absent).

    Resolution must be relative to the script's own location: were the
    script reading the real repository instead, the content and failure
    cases below would come out wrong.
    """
    dest = tmp_path / "hooks" / "session-start"
    dest.parent.mkdir(parents=True)
    shutil.copyfile(SCRIPT, dest)
    for rel, data in ((ROUTER_REL, router), (HOST_MAP_REL, host_map)):
        if data is not None:
            path = tmp_path / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
    return dest


@needs_bash
def test_relocated_router_text_is_carried_exactly(tmp_path: Path) -> None:
    """Every character the escaping handles comes back as written.

    The real router files exercise only quote and newline escaping, so this
    is the case that shows the order is right: a backslash escaped after
    the quote would double the quote's own backslash. CRLF and a lone CR
    become LF, as text-mode reading does; trailing newlines survive;
    ``&`` stays literal (bash 5.2's ``patsub_replacement`` gives it a
    meaning in a substitution's replacement); the em dash passes through.
    """
    router = (
        b'path C:\\dir\\file and a "quoted" word\r\n'
        b"tab\there & there\r\n"
        b"lone\rcarriage \xe2\x80\x94 dash\r\n"
        b"\r\n"
    )
    host_map = b"# map\n\nback\\slash \\n literal\n\n"
    dest = _relocate(tmp_path, router=router, host_map=host_map)

    context = hr.additional_context(hr.run_hook(dest, "claude-code"))

    want_router = (
        'path C:\\dir\\file and a "quoted" word\n'
        "tab\there & there\n"
        "lone\ncarriage \u2014 dash\n"
        "\n"
    )
    want_map = "# map\n\nback\\slash \\n literal\n\n"
    assert context == f"{LEAD}\n\n{want_router}\n---\n\n{want_map}"
    # The repository's own router was not read.
    assert "SUBAGENT-STOP" not in context


# --- failure ----------------------------------------------------------------


def _assert_failed_visibly(proc: subprocess.CompletedProcess[str]) -> None:
    """Exit 1 (the host's non-blocking hook-error notice), EMPTY stdout
    (schema-valid JSON on stdout would be read as success whatever the
    exit code), and one stderr line naming the failure."""
    assert proc.returncode == 1, (proc.returncode, proc.stdout, proc.stderr)
    assert proc.stdout == "", "a failed run must emit EMPTY stdout"
    lines = proc.stderr.splitlines()
    assert len(lines) == 1, proc.stderr
    assert lines[0].startswith("crucible: router not loaded: "), lines[0]


_ROUTER = b"---\nname: using-crucible\ndescription: tmp\n---\n\nrouter\n"
_HOST_MAP = b"# tmp host map\n"


@needs_bash
def test_failure_missing_router_file(tmp_path: Path) -> None:
    dest = _relocate(tmp_path, router=None, host_map=_HOST_MAP)
    _assert_failed_visibly(hr.run_hook(dest, "claude-code"))


@needs_bash
def test_failure_missing_host_map(tmp_path: Path) -> None:
    """The router present, the host map absent: the envelope would be
    incomplete, so the hook fails rather than emitting a router with no
    runtime mechanics attached."""
    dest = _relocate(tmp_path, router=_ROUTER, host_map=None)
    _assert_failed_visibly(hr.run_hook(dest, "claude-code"))


@needs_bash
def test_failure_unreadable_router_file(tmp_path: Path) -> None:
    """A directory where the router file should be: present, unreadable."""
    dest = _relocate(tmp_path, router=None, host_map=_HOST_MAP)
    (tmp_path / ROUTER_REL).mkdir(parents=True)
    _assert_failed_visibly(hr.run_hook(dest, "claude-code"))


@needs_bash
@pytest.mark.parametrize(
    "args",
    [(), ("",), ("codex",), ("Claude-Code",)],
    ids=["no-argument", "empty-argument", "unknown-host", "wrong-case"],
)
def test_failure_host_argument_names_no_arm(tmp_path: Path, args: tuple[str, ...]) -> None:
    """The host is named by the registration alone: with no host, or one
    the script has no arm for, it prints no document at all -- not a
    default host's -- even with both router files readable."""
    dest = _relocate(tmp_path, router=_ROUTER, host_map=_HOST_MAP)
    _assert_failed_visibly(hr.run_hook(dest, *args))


@needs_bash
def test_empty_path_runs_no_command_from_the_working_directory(tmp_path: Path) -> None:
    """A host can spawn the hook with an empty PATH, under which bash looks
    names up in the working directory (upstream field report: `cat: command
    not found` at session start). The script runs no external command: with
    PATH empty and a planted ``cat`` in the working directory, the envelope
    is complete and the planted file never runs."""
    bash = hr.find_bash()
    assert bash is not None
    marker = tmp_path / "ran"
    planted = tmp_path / "cat"
    planted.write_bytes(f"#!/bin/sh\n: > '{marker.as_posix()}'\n".encode())
    planted.chmod(0o755)
    # PATH is emptied inside bash: Git for Windows' bash.exe launcher builds
    # a PATH of its own, so an empty one passed from here never arrives.
    proc = subprocess.run(
        [bash, "-c", 'PATH= "$BASH" "$0" claude-code', SCRIPT.as_posix()],
        cwd=tmp_path,
        stdin=subprocess.DEVNULL,
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=60,
    )
    assert hr.additional_context(proc) == hr.envelope()
    assert not marker.exists()


@needs_bash
def test_failure_closed_stdout() -> None:
    """A write that fails is a failure too: with stdout closed, exit 1 and
    the one stderr line, never a silent exit 0."""
    bash = hr.find_bash()
    assert bash is not None
    proc = subprocess.run(
        [bash, "-c", '"$BASH" "$0" claude-code >&-', SCRIPT.as_posix()],
        stdin=subprocess.DEVNULL,  # the inherited stdin can be an invalid handle
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=60,
    )
    _assert_failed_visibly(proc)


# --- end to end -------------------------------------------------------------


@needs_bash
def test_registered_command_emits_the_envelope() -> None:
    """The registered command, run as the host runs a shell-form hook: under
    ``bash -c``, with the bash it names resolving to the one running it."""
    bash = hr.find_bash()
    assert bash is not None
    command = _registered_command().replace(PLACEHOLDER, REPO_ROOT.as_posix())
    path = f"{Path(bash).parent}{os.pathsep}{os.environ.get('PATH', '')}"
    proc = subprocess.run(
        [bash, "-c", command],
        env={**os.environ, "PATH": path},
        input="not json {{{",
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=60,
    )
    assert hr.additional_context(proc) == hr.envelope()
