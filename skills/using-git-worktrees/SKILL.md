---
name: using-git-worktrees
description: Use when starting feature work that needs isolation from current workspace or before executing implementation plans
---

# Using Git Worktrees

## Overview

Ensure work happens in an isolated workspace.

**Core principle:** Detect existing isolation first. Then use native tools. Then fall back to git. Never fight the harness.

**Every command below is a single Git invocation** — no shell program, no
command substitution, no pipes. Run each one, read its output or exit
code, and do the comparing and branching yourself. That keeps this flow
identical on Windows, macOS and Linux, with or without a POSIX shell.

**Stubs.** A reference a section names to read in full binds as if written here. Read it when its step comes, unless read since your last compaction; after compaction, re-read the step in progress's reference first.

## Step 0: Detect Existing Isolation

**Before creating anything, check if you are already in an isolated workspace.**

Run these three and keep the results:

```
git rev-parse --absolute-git-dir
git rev-parse --path-format=absolute --git-common-dir
git branch --show-current
```

Both `rev-parse` forms print an absolute path. Compare the first two
yourself — the comparison is the point of running them.

**Submodule guard:** confirm you are not inside a submodule before
concluding anything:

```
git rev-parse --show-superproject-working-tree
```

Empty output means you are not in a submodule. A printed path means you
are — treat it as a normal repo checkout, not a worktree.

**If the two paths differ (and you are not in a submodule):** You are already in a linked worktree. If it is another feature's and you are starting a new one, create this feature's own with Step 1b, on the request below. Otherwise skip to Step 2 (Project Setup) and do NOT create another worktree.

Report with branch state:
- On a branch: "Already in isolated workspace at `<path>` on branch `<name>`."
- Detached HEAD (`git branch --show-current` printed nothing): "Already in isolated workspace at `<path>` (detached HEAD, externally managed). Branch creation needed at finish time."

**If the two paths are equal (or you are in a submodule):** You are in a normal repo checkout.

Create a worktree on the operator's explicit request. Their approval of a message that names the worktree (brainstorming closes its design presentation with one), or a worktree preference declared in your instructions, is that request: do not ask again. Where neither exists, name the worktree, and its base where Step 1b sets it, in one line and ask. Work in place only where your instructions or the operator say so, and then skip to Step 2.

## Step 1: Create Isolated Workspace

**You have two mechanisms. Try them in this order.**

### 1a. Native Worktree Tools (preferred)

The user has asked for an isolated workspace (Step 0 consent). Do you already have a way to create a worktree? It might be a tool with a name like `EnterWorktree`, `WorktreeCreate`, a `/worktree` command, or a `--worktree` flag. If you do, use it and skip to Step 2.

Native tools handle directory placement, branch creation, and cleanup automatically. Using `git worktree add` when you have a native tool creates phantom state your harness can't see or manage.

Only proceed to Step 1b if you have no native worktree tool available, if brainstorming starts a feature inside another feature's worktree, or if your instructions declare a worktree directory — the native tools known to this skill cannot be given a base or a directory.

### 1b. Git Worktree Fallback

**Only use this where Step 0 or Step 1a's last line sends you here:** read `skills/using-git-worktrees/references/git-fallback.md` in full.

## Step 2: Project Setup

Detect the project type from the files at its root and run the matching setup command:

| Marker file | Setup command |
|-------------|---------------|
| package.json | `npm install` |
| Cargo.toml | `cargo build` |
| requirements.txt | `pip install -r requirements.txt` |
| pyproject.toml | `poetry install` |
| go.mod | `go mod download` |

Several may apply; run each match. None matching means no dependency install is needed.

## Step 3: Verify Clean Baseline

Run the project's own test command (`npm test`, `cargo test`, `pytest`, `go test ./...`) to ensure the workspace starts clean.

**If tests fail:** Report failures, ask whether to proceed or investigate.

**If tests pass:** Report ready.

### Report

```
Worktree ready at <full-path>
Tests passing (<N> tests, 0 failures)
Ready to implement <feature-name>
```

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "I'm obviously not in a worktree — no need to check" | Run Step 0. Harness-created isolation and submodules both fool eyeballing; the detection commands settle it. |
| "`git worktree add` is quicker than hunting for a native tool" | A native tool (e.g. `EnterWorktree`) owns placement, branching, and cleanup. Bypassing it outside the cases Step 1a's last line names is the #1 mistake — it creates phantom state your harness can't see or manage. |
| "The worktree directory is surely ignored already" | Run `git check-ignore`. An unignored worktree directory commits the whole tree into the repo. |
| "I checked `.worktrees/` — close enough" | `worktrees/` and `.worktrees/` are different paths with different `.gitignore` entries. Check the one you selected, or the check certifies a directory you are not using. |
| "The trailing slash is cosmetic" | It is the only thing telling Git the queried path is a directory. Drop it and the check misreports an ignored directory as unignored. |
| "Any directory name works" | Explicit instructions beat an existing project-local directory, which beats the `.worktrees/` default. |
| "I'll wrap these commands in a shell one-liner" | Each step is one Git invocation on purpose: the flow has to run where no POSIX shell exists. Do the comparing and branching yourself. |
| "The workspace is fresh — baseline tests can wait" | A dirty baseline makes every later failure ambiguous. Run the tests now; proceeding past failures is your human partner's call. |
