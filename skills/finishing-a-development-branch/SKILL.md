---
name: finishing-a-development-branch
description: Use when implementation is complete, all tests pass, and you need to decide how to integrate the work
---

# Finishing a Development Branch

## Overview

After the close readout (`crucible:subagent-driven-development` § Finish), carry out the option the operator's answer chose without presenting the options again, and ask only what it left open: an unconfirmed base branch (Step 3), and the records question (Option 2) where the readout did not ask it.

With no close readout (an umbrella's landing, after a standalone review), or where the answer chose no option, Step 4 presents the options.

A discard the operator confirmed at SDD's Finish, before it deleted the feature workspace, runs Step 2 and then the discard path from after its confirmation, without confirming again; Steps 1, 3 and 4 do not run.

Run every command, tests and forge tooling included, as a single invocation: no shell program, no command substitution, no captured variables. Keep each output yourself and substitute it into the next command, so the flow runs the same with or without a POSIX shell.

## Step 1: Verify Tests

Run the project's merge gate: its own where it names one (a specific suite, type checks, lint), else its full test suite.

A full gate or suite run on exactly the HEAD being integrated, whose command and output you can still show, counts, and its result stands: green or red, it is not re-run for a different one. A run on any other tree, or one you can no longer show (after compaction, say), is re-run.

If tests fail, report `Tests failing (<N> failures). Must fix before completing:` with the failures, and stop: integration needs a green suite. The one exception: a red run ruled not the branch's, shown to the operator with its ruling and accepted (SDD's Finish), continues to Step 2.

## Step 2: Detect Environment

Run these now, inside the worktree, since Step 6 needs the third value after you leave it:

```
git rev-parse --absolute-git-dir
git rev-parse --path-format=absolute --git-common-dir
git rev-parse --show-toplevel
```

The first two print absolute paths: compare them yourself. The third is the worktree root: record it as `<worktree-path>`.

| git dir vs common dir | Step 4 menu | Step 6 cleanup |
|---|---|---|
| equal (normal repo) | 3 options | none: no worktree |
| differ, named branch | 3 options | by provenance |
| differ, detached HEAD (`git branch --show-current` prints nothing) | 2 options, no merge | none: externally managed, left in place |

## Step 3: Determine Base Branch

The base branch is what this work forked from, usually named in the plan, the conversation or the branch's upstream. If it is not already known, ask "This branch split from <best guess> - is that correct?" and confirm it before merging.

## Step 4: Present Options

Offer only these options, concisely, with your recommendation and its reason ("I recommend <option>: <reason>. Which option?"):

1. Merge back to <base-branch> locally
2. Push and create a Pull Request
3. Keep as-is (I'll handle it later)

On a detached HEAD, say it is an externally managed worktree, with no option 1, and that option 2 pushes it as a new branch.

Discard is never offered: it happens only when your human partner explicitly asks to throw the work away. Wait for the answer; the integration decision is theirs.

## Step 5: Execute Choice

### Option 1: Merge Locally

Find the main checkout first, since worktree removal must run from outside the worktree: the first `worktree <path>` line of `git worktree list --porcelain` is its root. Change your working directory there with your own tools, then run `git checkout <base-branch>`, `git pull`, `git merge <feature-branch>`.

Run Step 1's tests on the merged result. On a merge conflict or a red merged result, stop, leave the worktree and branch in place, and investigate: nothing is pushed, so the merge stays local and recoverable. Undo a merge stopped on a conflict with `git merge --abort`.

Once the merged result is green, remove the worktree (Step 6), then run `git branch -d <feature-branch>`. If `-d` refuses, the commits never reached the base and the merge did not take: investigate, and never use `-D` to make it go away.

Where the close readout named an umbrella's closing review as the step after this landing, run it next (`skills/brainstorming/references/umbrellas.md` § Closing review).

### Option 2: Push and Create PR

The repo's conventions (PR template, contribution guide, commit-message rules, sign-off or DCO, hooks) come first and override crucible's defaults. Meeting one by changing commits already made, such as adding sign-offs, is a history rewrite: ask the operator first.

**The records question.** Where the branch has a feature folder (found by the resolve step of `skills/redteaming/references/formats.md` § Feature folder), list the files the branch adds there with `git diff --name-only --diff-filter=A <base-branch>...HEAD -- <feature-folder>`. On an umbrella's own branch, drop `<feature-folder>/umbrella.md` from the list: it stays in the merged tree, where the umbrella's children read it. An empty list leaves nothing to ask. Otherwise, unless the close readout asked this and the answer settled it, tell the operator that the branch's commits carry these files, so the PR shows them under any merge strategy and removing them now only keeps them out of the merged tree, and ask whether they go into the PR. If not, remove exactly the listed files in a final commit (`git rm`, then commit) and re-run Step 1's suite on the new HEAD.

Then push with `git push -u origin <feature-branch>`, or from a detached HEAD `git push origin HEAD:refs/heads/<new-branch>`. A rejected push means the remote moved: investigate, and force-push only on your human partner's explicit request.

Open the pull/merge request against <base-branch> with the forge's tooling and report its URL.

Keep the worktree: PR feedback is handled there under `crucible:receiving-review`. Run Step 1's suite before pushing PR fixes; after substantial fixes, get a fresh review from the PR's reviewers or `crucible:requesting-code-review` § Standalone mode. New scope is a new feature: `crucible:brainstorming`.

### Option 3: Keep As-Is

Report "Keeping branch <name>. Worktree preserved at <path>."

### If your human partner asks to discard the work

Confirm first: "This will permanently delete: branch <name>; all commits: <commit-list>; worktree at <path>. Type 'discard' to confirm." Wait for that exact confirmation.

Then change directory to the main checkout's root (found as in Option 1), remove the worktree (Step 6), and force-delete the branch with `git branch -D <feature-branch>`.

## Step 6: Remove the Worktree

Runs for Option 1 and confirmed discards only; Options 2 and 3 keep the worktree. Both callers have already moved to the main checkout's root: use the values you recorded in Step 2, not values re-read there.

- git dir equals common dir: a normal repo with no worktree to clean up; done.
- `<worktree-path>` under `.worktrees/` or `worktrees/`: this workflow created it and owns its cleanup. Run `git worktree remove <worktree-path>`, then `git worktree prune`, which clears any stale registration. A removal refused for modified or untracked files is the guard working and deletes nothing: report what is uncommitted and ask the operator; never pass `--force` on your own.
- Otherwise the host environment owns the worktree: leave it in place; if the platform has a tool for leaving a worktree, use it.

## Common Rationalizations

| Excuse | Reality |
|---|---|
| "'Yeah, get rid of it' counts as confirmation" | Only the typed word `discard` authorizes deletion. |
| "`worktree remove` refused — I'll add --force" | It holds uncommitted work, and forcing destroys it silently. |
| "`branch -d` refused — I'll use -D" | The merge did not take; `-D` throws the commits away. |
| "The push was rejected — force-push will fix it" | The remote moved; force-push only on explicit request. |
| "This other worktree looks stale — I'll clean it too" | Step 6 removes only `<worktree-path>`, and only under `.worktrees/` or `worktrees/`. |
