# Git steps

## Decision

**Single invocations.** `crucible:using-git-worktrees` and
`crucible:finishing-a-development-branch` run every command as a single
invocation: no shell program, no command substitution, no captured
variable, and in the worktree skill, where every command is a Git one, no
pipe. The agent keeps each output itself, compares the absolute paths
`git rev-parse` prints, and substitutes values into the next command;
finishing finds the main checkout from `git worktree list --porcelain`.

**Seats' git conduct.** An implementer stages changed paths by name,
never runs `git add -A`, `git add .` or a bare `git stash`, commits only
to its worktree's branch, and commits with the identity git already has,
setting none and reporting BLOCKED where none is configured
(`skills/subagent-driven-development/implementer-prompt.md` § Where You
Work). The controller commits nothing in a worktree while a dispatched
agent works there (`docs/decisions/shared-tree.md`).

**Finishing's guards.** A `git branch -d` that refuses after a local
merge means the merge did not take: the agent investigates and never
reaches for `-D`. A `git worktree remove` that refuses because the
worktree holds modified or untracked files is reported to the operator,
never forced past with `--force`. A merge that stopped on a conflict is
undone with `git merge --abort`; one that completed and fails its tests
stays local and recoverable while the agent investigates. Force-deleting
a branch belongs to an explicitly requested, typed-out discard
(`crucible:finishing-a-development-branch § Step 5: Execute Choice`,
§ Step 6: Cleanup Workspace), and a force-push to the operator's
explicit request (`crucible:finishing-a-development-branch § Common
Rationalizations`).

**Crucible's own repository.** Contributors work on a feature branch in
a worktree under `.worktrees/`, never commit on `master` directly, and
land on `master` by merging, each landing on the maintainer's go-ahead
(the Git section of `AGENTS.md`). Line endings are LF
(`docs/decisions/authoring-crucible.md`).

## Why

### Single invocations

Upstream's two skills computed their values in POSIX shell, for instance
`GIT_DIR=$(cd "$(git rev-parse --git-dir)" 2>/dev/null && pwd -P)`
(`superpowers/skills/finishing-a-development-branch/SKILL.md`,
`superpowers/skills/using-git-worktrees/SKILL.md`), which does not run
where the agent's shell is PowerShell or no POSIX shell exists. The
design for crucible's Codex support (2026-08-09) required core
coordination to run without bash on Windows, and its worktree and
finishing skills to express individual Git operations; the rewrite landed
on 2026-08-15. On 2026-10-08 finishing's rule widened from a single Git
invocation to a single invocation, because one of its steps then ran a
Python script; that script is gone, and the steps still run the
project's test command and the forge's tooling. (Basis: external, for
upstream; judgment, accepted by the maintainer.)

### Seats' git conduct

The index is shared inside a worktree, so `git add -A`, `git add .` or a
bare `git stash` takes another party's work along with it; the staging
rule followed three such incidents in crucible's runs, recorded on
2026-10-04, and landed on 2026-10-05 trimmed to what they support. On
2026-08-23 an implementer committed under an identity taken from its
session context in place of the configured one; the rule against setting
one followed on 2026-10-07.
(Basis: measured, from three incidents; a single incident, for the
identity.)

### Finishing's guards

Git's own refusals name the flag that overrides them: checked on
2026-10-20 with git 2.56.0, a refused `git branch -d` hints
`git branch -D`, and a refused `git worktree remove` says to "use
--force to delete it". An agent that follows the hint throws away the
commits or the files the refusal protected. Upstream's flow ran both
commands with nothing said about a refusal; crucible's guards arrived
with the single-invocation rewrite on 2026-08-15. On 2026-10-15
`git merge --abort` was narrowed to a conflicted merge: after a merge
that completed, git refuses it ("There is no merge to abort"), and a
completed merge that fails its tests is, as upstream says, local and
recoverable. (Basis: measured, for git's behaviour; judgment, accepted
by the maintainer.)

### Crucible's own repository

Landing on `master` only on the maintainer's go-ahead for that landing
is the maintainer's own rule. `master` is where releases are cut: a
release lands on it, is tagged and then promoted to `stable`
(`docs/decisions/releases.md`). (Basis: the maintainer's preference.)

## Rejected

- **Shell one-liners or POSIX scripts for the Git flow**: the flow has to
  run where no POSIX shell exists (§ Why).
- **Forcing past a Git refusal** (`-D`, `--force`, a force-push) on the
  agent's own initiative: the refusal is protecting work (§ Why).
- **A staging rule for two sessions sharing one branch**: it came from
  one accidental split, and was declined on 2026-10-05 with the trim.

## Changes

- 2026-10-27: the identity incident no longer says whose address the
  seat used, which is private context.
- 2026-10-15: finishing's guards: no `-D` past a `branch -d` refusal, no
  `--force` past a `worktree remove` refusal, and `git merge --abort`
  for a merge stopped on a conflict only.
- 2026-10-11: git conduct: implementers stage by name with no
  `git add -A`, `git add .` or bare `git stash`, set no identity and
  report BLOCKED without one; no controller commit while a seat works;
  crucible's own repository on feature branches in `.worktrees/`,
  landing on `master` by merge on the maintainer's go-ahead.
- 2026-10-08: worktree and finishing steps as single invocations, with no
  shell program, command substitution or captured variable.
