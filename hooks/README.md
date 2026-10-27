# Crucible hooks

Crucible registers one hook, on Claude Code: the SessionStart router
injection. On Codex it registers none. A Codex session reaches the router
through skill discovery and the router's read-from-path fallback (see "Hook
registration per runtime" for why). This file documents the one hook: its
registration, what the hook script emits, how a failure surfaces, and how to
port it to another host.

**Anchor stability:** the `##` headings here are cited from other files as
interfaces (see `docs/authoring.md` § Anchor stability). Renaming one is a cross-file interface change; adding a new
section is not.

## Hook registration per runtime

One registration, one hook script, one runtime:

| | Claude Code | Codex |
|---|---|---|
| registration | `hooks/hooks.json` | none: `.codex-plugin/plugin.json` declares `"hooks": {}` |
| plugin-root placeholder | `${CLAUDE_PLUGIN_ROOT}` | — |
| SessionStart matcher | `startup\|clear\|compact` | — |

The Claude Code registration registers exactly one event, SessionStart, and
one shell-form command:

```
bash "${CLAUDE_PLUGIN_ROOT}/hooks/session-start" claude-code
```

The argument names the host. The script never infers it from the
environment: Codex sets `CLAUDE_PLUGIN_ROOT` in a hook's environment too
(measured on codex-cli 0.160.0), so no variable tells the hosts apart. The
script needs bash 3.2 or newer (macOS's `/bin/bash` is 3.2; on Windows, Git
Bash). It is measured on Git Bash 5.3 (Windows 11) and, on Debian 13.5
without Python, on bash 5.2.37 and on GNU bash 3.2.57 built from source.
Apple's `/bin/bash` has not run it. Where Windows has no Git Bash, see
"Porting to another host".

**Why Codex registers none.**
- Codex already routes without it, through skill discovery and the router's
  read-from-path fallback. A Codex session that never reads the router runs
  without crucible.
- superpowers dropped its own Codex SessionStart hook for UX reasons.

The manifest's `hooks` value is exactly `{}`, never an omitted field. The
registration is a single command string, one Codex could run: without the
field, Codex auto-discovers `hooks/hooks.json` and runs it (measured on
codex-cli 0.160.0, Windows 11).

**The matcher omits `resume`.** Whether a resumed Claude session is re-injected, and
whether the host reuses its `session_id` across a resume, is **not settled
by anything measured here**. Nothing depends on it, and no claim is made
either way.

**The envelope budget.** The rendered envelope is held under 10,000
characters, and the automated suite asserts it. That is Claude Code's
threshold for a hook's `additionalContext`, read in the 2.1.292 binary:
longer text is written to disk and the session gets a stand-in, or, where the
write fails, the text is cut at 10,000. Re-measure it on a host upgrade; the
test's docstring names the strings that locate it.

The registration carries no project's policy.

## SessionStart injection

`hooks/session-start`, given `claude-code`, reads the router,
`skills/using-crucible/SKILL.md`, and the Claude Code host map,
`skills/using-crucible/references/claude-code.md`, both resolved from the
script's own location. It prints one document:
`{"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": …}}`,
whose context is a lead line, the router, a `---` separator and the host
map, inlined in full. Each CRLF and lone CR in the files becomes LF; the
text is then escaped for backslash, double quote, newline, carriage return
and tab, and non-ASCII passes through as UTF-8. The script reads no stdin
and reads or writes no session state.

**A failure is visible and never breaks the session.** Any problem — a
missing or unreadable router or host-map file, a missing or unknown host
argument, a write that fails — means one `crucible: router not loaded:
<reason>` line on stderr, no other, and exit 1. Every failure found before
the document is written leaves stdout empty; that is required, not tidy,
because the host reads schema-valid JSON on stdout as success whatever the
exit code. (A write that fails part-way may leave part of the document on
stdout, and still exits 1.) The host shows a nonzero SessionStart exit as a
non-blocking hook-error notice carrying that line, and the session continues
without the router. A zero exit would hide the line: the host sends a
zero-exit hook's stderr to its debug log only (measured on Claude Code
2.1.292, Windows 11).

## Porting to another host

A new host is one registration file naming it plus one `case` arm in
`hooks/session-start` that prints that host's document. The host is named by
the registration's argument, never read from the environment. For other
hosts' document shapes, superpowers 6.4.1's `hooks/session-start` (which
covers Cursor and Copilot CLI) is the reference; they are not copied here.
A host that runs hooks under `cmd.exe` needs a wrapper, and that wrapper
must fail visibly where no bash is found: upstream's exits 0 there.

**Claude Code on Windows without Git Bash** (unmeasured end to end). The
registration sets no `"shell"` field, so the host runs the command under
bash where Git Bash is installed and under PowerShell where it is not; the
Hooks reference does not say what `"bash"` would do there. Under PowerShell,
`bash` may resolve to WSL's launcher, `C:\Windows\System32\bash.exe`.
Started from Python on Windows 11 (2026-10-11), that launcher exited 1, wrote its own message to
stdout as UTF-16LE and left stderr empty. Where `bash` resolves to nothing,
PowerShell reports the command as not found. Either way the hook exits
nonzero and the host shows its notice, but the notice may carry no message,
and whether the host adds that stray stdout to the context after a nonzero
exit is not documented. The script never runs, so its failure contract does
not reach this case.
