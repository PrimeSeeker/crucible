---
name: using-git-worktrees
description: Use when starting feature work that needs isolation from current workspace or before executing implementation plans
---

# Using Git Worktrees

## Overview

Ensure work happens in an isolated workspace. Prefer your platform's native worktree tools. Fall back to manual git worktrees only when no native tool is available, when brainstorming starts a feature inside another feature's worktree, or when your instructions declare a worktree directory.

**Core principle:** Detect existing isolation first. Then use native tools. Then fall back to git. Never fight the harness.

**Announce at start:** "I'm using the using-git-worktrees skill to set up an isolated workspace."

**Every command below is a single Git invocation** — no shell program, no
command substitution, no pipes. Run each one, read its output or exit
code, and do the comparing and branching yourself. That keeps this flow
identical on Windows, macOS and Linux, with or without a POSIX shell.

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
are — treat it as a normal repo checkout, not a worktree. (The absolute
path forms above already report a submodule's git dir and common dir as
the *same* path, so the worktree predicate does not misfire there; this
probe is what confirms it.)

**If the two paths differ (and you are not in a submodule):** You are already in a linked worktree. Skip to Step 2 (Project Setup). Do NOT create another worktree.

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

**Only use this if Step 1a does not apply** — you have no native worktree tool available, brainstorming starts a feature inside another feature's worktree, or your instructions declare a worktree directory. Create a worktree manually using git.

#### Directory Selection

**`<project-root>`** is the checkout you are in — from another feature's linked worktree, the main checkout: the parent of the common dir Step 0 printed.

Follow this priority order. Explicit user preference always beats observed filesystem state.

1. **Check your instructions for a declared worktree directory preference.** If the user has already specified one, use it without asking.

2. **Look for an existing project-local worktree directory** at `<project-root>` — `.worktrees/` (preferred, hidden) or `worktrees/`. Use whichever exists; if both do, `.worktrees/` wins. List the directory with your own file-listing tool; this needs no shell.

3. **If there is no other guidance available**, default to `.worktrees/` at `<project-root>`.

**Whatever you selected is `<worktree-dir>` from here on** — the steps below
verify and create against *that* directory, never against a remembered
default. Substituting the wrong one is the whole bug this step prevents.

#### Safety Verification (project-local directories only)

**MUST verify the selected directory is ignored before creating the worktree:**

```
git -C <project-root> check-ignore -q <worktree-dir>/
```

Read the exit code: **0** means ignored — proceed. **1** means not ignored — add that directory to `.gitignore`, commit the change, then re-run the check against the same directory. From another feature's worktree, commit nothing: report the result to the operator and wait for their answer.

**Substitute your selection, and keep the trailing slash.** Two things go
wrong here:

- **Checking the wrong directory.** `worktrees/` and `.worktrees/` are
  separate paths with separate `.gitignore` entries; a project commonly
  ignores one and not the other. Verifying `.worktrees/` and then creating
  the worktree in `worktrees/` passes the check and commits the whole
  worktree anyway.
- **Dropping the slash.** A `.gitignore` entry written the usual way
  (`worktrees/`, `.worktrees/`) matches directories only, and for a path
  that does not exist yet Git learns "this is a directory" solely from the
  trailing slash on the query. Without it the check reports "not ignored"
  for a directory that already is, and you commit a redundant entry.

**Why critical:** Prevents accidentally committing worktree contents to repository.

#### Create the Worktree

Use the same `<worktree-dir>` you just verified, the branch name for the directory, and `<base>` as the start point: the repo's base branch or one the operator named when brainstorming's call or a declared directory brought you here, otherwise `HEAD`:

```
git -C <project-root> worktree add <worktree-dir>/<branch-name> -b <branch-name> <base>
```

Then work from that directory — set it as your working directory with
your own tools; nothing here needs a shell.

**Branch safety:** `git worktree add -b` refuses when the branch name already exists, and creates nothing. That is the intended answer — pick a fresh name or check out the existing branch deliberately; never force past it.

**Sandbox fallback:** If `git worktree add` fails with a permission error (sandbox denial), tell the user the sandbox blocked worktree creation and you're working in the current directory instead. Then run setup and baseline tests in place.

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

## Quick Reference

| Situation | Action |
|-----------|--------|
| Already in linked worktree | Skip creation (Step 0) |
| In a submodule | Treat as normal repo (Step 0 guard) |
| Native worktree tool available | Use it (Step 1a), unless Step 1a's last line sends you to Step 1b |
| No native tool | Git worktree fallback (Step 1b) |
| `.worktrees/` exists | Use it (verify ignored) |
| `worktrees/` exists | Use it (verify ignored) |
| Both exist | Use `.worktrees/` |
| Neither exists | Check instruction file, then default `.worktrees/` |
| Running the safety check | Check the directory you selected, with its trailing slash — never a remembered default |
| `git check-ignore` exits 1 | That directory is not ignored: add it to .gitignore + commit, re-check |
| Branch name already taken | `worktree add -b` refuses; pick a fresh name |
| Permission error on create | Sandbox fallback, work in place |
| Tests fail during baseline | Report failures + ask |
| No package.json/Cargo.toml | Skip dependency install |

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
