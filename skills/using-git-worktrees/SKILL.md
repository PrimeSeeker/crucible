---
name: using-git-worktrees
description: Use when starting feature work that needs isolation from current workspace or before executing implementation plans
---

# Using Git Worktrees

## Overview

Ensure work happens in an isolated workspace: detect existing isolation first, then use native tools, then fall back to git. Never fight the harness.

Every command in Steps 0–1 and 1b's reference is a single Git invocation: no shell program, no command substitution, no pipes. Run each, read its output or exit code, and do the comparing and branching yourself, so the flow runs the same with or without a POSIX shell.

**Stubs.** A reference a section names to read in full binds as if written here. Read it when its step comes, unless read since your last compaction; after compaction, re-read the step in progress's reference first.

## Step 0: Detect Existing Isolation

Before creating anything, run these four and keep the results:

```
git rev-parse --absolute-git-dir
git rev-parse --path-format=absolute --git-common-dir
git branch --show-current
git rev-parse --show-superproject-working-tree
```

Compare the first two (both absolute) yourself. The fourth prints nothing outside a submodule; a printed path means a submodule, which counts as a normal checkout.

**Paths differ, no submodule:** you are in a linked worktree. If it is another feature's and you are starting a new one, create this feature's own with Step 1b, on the request below. Otherwise skip to Step 2, create no other worktree, and report:
- on a branch: "Already in isolated workspace at `<path>` on branch `<name>`."
- detached HEAD (`git branch --show-current` printed nothing): "Already in isolated workspace at `<path>` (detached HEAD, externally managed). Branch creation needed at finish time."

**Paths equal, or a submodule:** you are in a normal checkout.

Create a worktree only on the operator's explicit request. Their approval of a message naming the worktree, or a worktree preference declared in your instructions, is that request: do not ask again. Where neither exists, name the worktree, and its base where Step 1b sets it, in one line and ask. Work in place only where your instructions or the operator say so, and then skip to Step 2.

## Step 1: Create Isolated Workspace

### 1a. Native Worktree Tools (preferred)

The user has asked for an isolated workspace (Step 0 consent). If you have a native way to create a worktree (a tool named like `EnterWorktree` or `WorktreeCreate`, a `/worktree` command, a `--worktree` flag), use it and skip to Step 2.

Go to Step 1b only if you have no native worktree tool, if brainstorming starts a feature inside another feature's worktree, or if your instructions declare a worktree directory.

### 1b. Git Worktree Fallback

Only where Step 0 or Step 1a's last line sends you here, **read `skills/using-git-worktrees/references/git-fallback.md` in full**.

## Step 2: Project Setup

Run the project's dependency setup, where it has one.

## Step 3: Verify Clean Baseline

Run the project's own test command (`npm test`, `cargo test`, `pytest`, `go test ./...`). If tests fail, report the failures and ask whether to proceed or investigate; if they pass, report ready.

## Common Rationalizations

| Excuse | Reality |
|---|---|
| "`git worktree add` is quicker than hunting for a native tool" | Bypassing a native tool (e.g. `EnterWorktree`) outside Step 1a's last-line cases is the #1 mistake: it creates phantom state the harness can't see or manage. |
| "The worktree directory is surely ignored" | Run `git check-ignore`: an unignored worktree directory gets committed into the repo. |
| "I checked `.worktrees/` — close enough" | Check the directory you selected: `worktrees/` and `.worktrees/` have different `.gitignore` entries. |
| "The trailing slash is cosmetic" | Without it, Git reports an ignored directory that does not exist yet as not ignored. |
