# The SessionStart hook and the router

## Decision

**One hook, on Claude Code.** Crucible's only hook is the SessionStart
router injection on Claude Code, registered in `hooks/hooks.json` for
`startup|clear|compact` as
`bash "${CLAUDE_PLUGIN_ROOT}/hooks/session-start" claude-code`. The
script is bash, extensionless and pinned to LF (`.gitattributes`),
written for bash 3.2 and newer. It resolves the plugin root from its own
location and picks its host by the argument alone, never from the
environment; `claude-code` is its one arm. It prints one
`hookSpecificOutput` document whose context is a lead line, the router,
a separator and the Claude Code host map, with each CRLF and lone CR
turned into LF. A session the host marks unattended, its hook's
environment holding `CLAUDE_CODE_SESSION_ATTENDED=0`, gets a short note
in that context's place: it loads no crucible skill the prompt does not
name, and one the prompt names first reads the host map at the path the
note gives; any other value, or none, gets the router. It runs no external command, so the `PATH` it starts
with cannot break it or make it run a file from the working directory;
the registration's own `bash` is still found on `PATH`
(`hooks/README.md` § Hook registration per runtime). Every failure prints one `crucible: router not loaded:
<reason>` line on stderr and exits 1, and a failure found before the
write leaves stdout empty (`hooks/README.md` § SessionStart injection).
It is measured on Git Bash 5.3 (Windows 11) and, on Debian 13.5, on bash
5.2.37 and on GNU bash 3.2.57 built from source; Apple's `/bin/bash` has
not run it, and Windows without Git Bash is not served
(`hooks/README.md` § Hook registration per runtime, § Porting to another
host). Codex registers no hook (`docs/decisions/runtime-adapters.md`).

**No guards.** Crucible ships no PreToolUse hook, no branch protection
and no checkout rule, and names no replacement. Worktree and edit
discipline is prose in the skills; a project's own hooks stay with the
project, and judgment rules stay prose.

**The router** (`skills/using-crucible/SKILL.md`). A plain Rule: before
acting, clarifying questions and exploration included, check the Skill
Index and invoke every skill whose trigger matches and any the operator
names; a loaded skill whose trigger turns out not to match is set aside,
saying so, and one that applies is skipped only on the operator's
explicit word. Upstream's twelve red-flag thoughts, each answered with a
check. The planning trigger is entering the host's planning mode.
"Operator" is defined once, as the person inherited text calls "your
human partner". The precedence line ranks the instruction files,
user-level, project and any other the host loads, and the operator's
direct requests above the skills (`docs/decisions/operator-steering.md`).
The router also carries the trivial-edit waiver
(`docs/decisions/routes.md`), the evidence-before-claims line
(`docs/decisions/evidence-and-findings.md`) and the line stopping a
session another router also reached (`docs/decisions/fork-and-own.md`),
names the runtime adapter by
its path from the plugin root, and tells a dispatched seat to ignore it.
The rendered envelope, router plus host map, stays under 10,000
characters, which `tests/test_session_start.py` asserts; an overrun is
trimmed in the prose, never met by raising the bound.

**Interpreters.** A hook's script is bash; a script a workflow step runs
may be stdlib Python (`AGENTS.md`, Interpreters). No workflow step runs
Python now, so a user's host needs none; the suite needs Python 3.10 or
newer. writing-skills keeps the
general rule in one line: forward slashes, and an interpreter the users'
hosts have, named in the invocation.

**No runtime port.** No JavaScript core, Claude Code mod, CLI or mod
probe; the mod path waits in `docs/backlog/claude-code-mod.md`.

## Why

### One bash hook, every failure visible

A hook runs with no agent around it to recover from a missing
interpreter, while an agent that meets a missing `python3` tries
`python`. Until 2026-10-11 the hook was a POSIX `sh` launcher probing for
a Python 3.10 or newer to run a 108-line handler that concatenated two
markdown files; it became one bash script, at macOS's bash 3.2 as the
floor. Upstream's hook is bash too, behind a Windows wrapper
(`superpowers/hooks/session-start`, `superpowers/hooks/run-hook.cmd` at
v6.2.0). (Basis: judgment, accepted by the maintainer.)

The host comes from the argument because Codex sets `CLAUDE_PLUGIN_ROOT`
in a hook's environment too (measured on codex-cli 0.160.0), so no
variable tells the hosts apart; upstream's hook picks among three
document shapes by three environment variables. A one-value argument had
been removed on 2026-10-07 as a leftover; it came back on 2026-10-11 for
this reason. The JSON document kept Claude Code's input unchanged when
the hook moved to bash, and leaves a host that reads only JSON one arm
away. (Basis: measured; external, for upstream; judgment, accepted by the
maintainer.)

Failures are loud because a quiet one went unseen. On Claude Code 2.1.292
(Windows 11, 2026-10-07) a SessionStart hook exiting nonzero showed a
non-blocking notice carrying its first stderr line and the session went
on, while a zero exit's stderr reached only the debug log; the handler's
fail-open exit 0 had hidden every failure. Stdout stays empty before the
write because the host takes schema-valid JSON on stdout as success
whatever the exit code, except 2 (the Claude Code hooks reference,
https://code.claude.com/docs/en/hooks, read 2026-10-20), so a document
printed before a failure would load the router and show no notice.
Upstream's wrapper exits 0 where it finds no bash, and its hook puts a
file-read error into the context. (Basis: measured; external.)

Without the line-ending step, a CRLF checkout put 110 carriage returns
into the context (2026-10-11). On 2026-10-14 the script ran fourteen
cases under each of bash 5.2.37 and GNU bash 3.2.57, on Debian 13.5 under
WSL 2 with no Python installed: every success exited 0 with JSON
byte-identical to Git Bash 5.3's output on the same tree, and every
failure exited 1 with empty stdout and the one line. Apple's `/bin/bash`
stays, in the maintainer's words, "plausibly working, but untested".
(Basis: measured; the maintainer's preference, for leaving it there.)

The script read its files with `cat` until 2026-10-27. Upstream had a
field report of a hook spawned with an empty `PATH` (`cat: command not
found`, superpowers issue #2310), and with `PATH` empty bash searches the
working directory: a `cat` planted there ran at session start (Git Bash
5.3, 2026-10-27). The read is now bash's own. Under bash 5.2.37 and GNU
bash 3.2.57 (Debian 13.5, WSL 2) and Git Bash 5.3, the new script's
output is byte-identical across the three, and with `PATH` empty and a
planted `cat` the envelope is complete and the planted file does not
run. (Basis: measured; external.)

### Unattended sessions

A headless session gets the router's workflows with nobody to answer
them: on 2026-11-04 a `claude -p` run on crucible 0.19.0, asked to add a
feature, loaded brainstorming "as your setup requires for feature work"
and ended on a question to the user. The same day (Claude Code 2.1.317,
Windows 11) a probe hook in a `claude -p` session saw
`CLAUDE_CODE_SESSION_ATTENDED=0` and `CLAUDE_CODE_ENTRYPOINT=sdk-cli` in
its environment, against 1 and `cli` in an interactive CLI session's
hook, at startup and at compaction, while its input (session, transcript
path, working directory, event and source) carried no field saying which;
other front-ends were not measured. The host's environment-variable page,
read that day, lists neither variable, so the hook keys on the value 0
alone: a host that drops or renames the variable gets the router back,
today's behavior. With the note in place, the same request loaded no
crucible skill and went to the task (one run, the same day). The note
names the host map's path because a skill the prompt names, run without
the router, would otherwise find no host mechanics. The maintainer had
expected headless sessions to be beyond reach; the probe moved the
ruling to the hook. (Basis: measured;
judgment, an agent's proposal accepted by the maintainer.)

### No guards

Crucible's first design (2026-08-06) moved mechanically checkable rules
into hooks: guards in the plugin for worktree-only edits and protected
branches, project-specific hooks left with the project, judgment rules
left as prose. The guards retired on 2026-10-04. The checkout guard had
denied nothing in real use: its log, read that day, held denies only from
the install probes of 2026-08-07. On Codex no guard had ever run, since
the Codex hook never started its handler. git itself refuses to check out
a branch another worktree has checked out (re-checked on git 2.56.0,
2026-10-20). Branch protection, the maintainer ruled, was never
crucible's job: it belongs outside crucible, with the projects that want
it, and crucible names no replacement. (Basis: measured; the maintainer's
preference.)

### The router

The router was rewritten on 2026-10-07. It had kept upstream's all-caps
block, which contradicted its own permission to set a non-matching skill
aside; its red-flag table had been cut from twelve rows to four with no
recorded criterion; its precedence line had lost user-level instruction
files; its planning trigger had widened to any proposed plan. The rewrite
restored all twelve thoughts verbatim with the replies as checks
(`superpowers/skills/using-superpowers/SKILL.md` at v6.2.0 has the
twelve), the plan-mode trigger and user-level files, and dropped the
block and the hook's matching wrapper. It is unmeasured and reversible.
(Basis: judgment, accepted by the maintainer.)

The budget is Claude Code's own threshold, read in the 2.1.292 binary on
2026-10-07: a command hook's `additionalContext` longer than 10,000
characters is written to disk with a stand-in left in the session, or
cut at 10,000 where the write fails. The earlier 8,750-character budget,
and a headroom floor under it, had no measured basis on the host it
still governed. The test names its basis, to be re-measured on a host
upgrade. (Basis: measured.)

The router names the adapter from the plugin root since 2026-10-01: on
2026-08-23 a Codex session joined a short adapter path to the shared
`skills/` root and read the wrong file first. The miss reproduced in none
of six baseline runs, and a re-run after the change showed no
regression. (Basis: a single incident; measured, for the runs.)

### Interpreters

The plugin's Python floor fell from 3.10 to 3.8 on 2026-10-11, when the
hook stopped needing Python: 3.10 had come from a helper script that has
since gone, and 3.8 was the floor `conserve.py`'s own code stated. The
trade was accepted: a host with bash but no usable Python loaded the
router and learned of the missing interpreter only at the first
`conserve.py` run, where the controller stopped. On 2026-10-12 the
interpreter rules moved from writing-skills into `AGENTS.md`, as rules
for crucible's contributors, and writing-skills kept one neutral line.
(Basis: judgment, accepted by the maintainer.)

On 2026-11-02 the skill text rewrite retired merge conservation and
`conserve.py`, the one workflow script, and with it the plugin's Python
requirement for users (`docs/decisions/fix-verification-and-merge.md`).
(Basis: judgment, an agent's proposal accepted by the maintainer.)

### No runtime port

A port was planned to replace the remaining scripts: a JavaScript core, a
Claude Code mod adapter, a CLI and an `sh` fallback. On 2026-10-11 it
came to three delivery paths for one check and a concatenation, and the
bash hook and `conserve.py` took its place. The mod path, with its
reasons and the triggers that would reopen it, is in the backlog item.
(Basis: judgment, accepted by the maintainer.)

## Rejected

- **Checking the host map in the unattended note's branch:** with the
  variable at 0 a broken install exits 0 with a note naming a missing
  file, and a skill the prompt names then fails on that read, where the
  agent sees it. A check would add a failure path for a session that
  otherwise never reads the file, so the failure sentence covers sessions
  that load it.
- **PreToolUse guards and a checkout rule**: they denied nothing in real
  use, never ran on Codex, and git already refuses the one checkout that
  matters (§ Why).
- **A hook that infers its host from the environment**: one host sets
  another's variables.
- **A Python hook behind a probing launcher**: an interpreter dependency
  where no agent can recover.
- **A hook that fails open**, exiting 0: it hides every failure.
- **Only a README line for headless runs**, telling users to turn
  crucible off: the host already marks the sessions the hook can serve.
- **Upstream's all-caps block and wrapper**: they contradicted the
  router's permission to set a non-matching skill aside.
- **An 8,750-character envelope budget**: no measured basis; 10,000 is the
  host's threshold.
- **A JavaScript core, Claude Code mod or CLI**: three delivery paths for
  one check and a concatenation.

## Changes

- 2026-11-04: a failure covers a missing router or host map only in a session that loads them; because the unattended note's branch reads neither, and checking the host map there was rejected.
- 2026-11-04: a session the host marks unattended gets a note in place
  of the router, since nobody there can answer the router's workflows;
  the router stops a session another router also reached.
- 2026-11-02: interpreters: no workflow step runs Python, `conserve.py`
  and the Python 3.8 floor for users retired with merge conservation,
  which the skill text rewrite retired.
- 2026-10-27: writing-skills' rule now names the interpreter in the
  invocation, since packagers can strip executable bits (upstream,
  v7.0.1 review).
- 2026-10-27: the script reads with a builtin, not `cat`, and runs no
  external command: under an empty `PATH`, bash ran a `cat` planted in
  the working directory. The registration keeps `bash` from `PATH`.
- 2026-10-14: one SessionStart hook, on Claude Code: a bash script at a
  3.2 floor, told its host by argument, every failure visible; measured on
  Git Bash 5.3, bash 5.2.37 and GNU bash 3.2.57, Apple's bash untested.
- 2026-10-12: interpreters: a hook's script bash, a workflow step's
  script stdlib Python, `conserve.py` the one, at Python 3.8.
- 2026-10-11: no runtime port: no JavaScript core, Claude Code mod or
  CLI; the mod path in the backlog.
- 2026-10-07: the router: a plain Rule, upstream's twelve red-flag
  thoughts as checks, the planning-mode trigger, "operator" defined once,
  the precedence line, the adapter named from the plugin root, and an
  envelope under 10,000 characters.
- 2026-10-04: no PreToolUse guards, no branch protection and no checkout
  rule.
