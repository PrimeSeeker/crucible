---
name: finishing-a-development-branch
description: Use when implementation is complete, all tests pass, and you need to decide how to integrate the work
---

# Finishing a Development Branch

## Overview

**Core principle:** Verify tests → Detect environment → Present options → Execute choice → Clean up.

**Announce at start:** "I'm using the finishing-a-development-branch skill to complete this work."

**Every command below is a single invocation** — no shell program, no
command substitution, no captured variables. Run each one, keep its output
yourself, and substitute it into the next command. That keeps this flow
identical on Windows, macOS and Linux, with or without a POSIX shell.

## Step 1: Verify Tests

Run the project's full test suite (`npm test` / `cargo test` / `pytest` / `go test ./...`).

Merge-acceptance criteria are project-defined — if the project names its own gate (specific suite, type checks, lint), run that; the full test suite is only the default.

A full run on exactly the HEAD being integrated, whose command and output you can still show, counts, and its result stands — green or red, it is not re-run for a different one; any other tree, or a run you can no longer show (after compaction, say), is re-run.

**If tests fail**, report the failures and stop — the menu comes after a green suite:

```
Tests failing (<N> failures). Must fix before completing:

[Show failures]
```

**If tests pass:** continue to Step 2.

## Step 2: Detect Environment

Run these three now, while you are still inside the workspace — Step 6 needs the third value after you have moved out of it:

```
git rev-parse --absolute-git-dir
git rev-parse --path-format=absolute --git-common-dir
git rev-parse --show-toplevel
```

Both `rev-parse` path forms print an absolute path; compare the first two yourself. The third is the workspace root — write it down as `<worktree-path>`.

This determines which menu to show and how cleanup works:

| State | Menu | Cleanup |
|-------|------|---------|
| git dir == common dir (normal repo) | Standard 3 options | No worktree to clean up |
| git dir != common dir, named branch | Standard 3 options | Provenance-based (see Step 6) |
| git dir != common dir, detached HEAD | Reduced 2 options (no merge) | Externally managed — leave in place |

`git branch --show-current` prints nothing on a detached HEAD.

## Step 3: Determine Base Branch

The base branch is whatever this work forked from — usually named in the
plan, the conversation, or the branch's upstream. If it is not already
known, ask: "This branch split from <your best guess> - is that correct?"
Confirm before merging: merging into the wrong base is expensive to undo.

## Step 4: Present Options

**Normal repo and named-branch worktree — present exactly these 3 options:**

```
Implementation complete. What would you like to do?

1. Merge back to <base-branch> locally
2. Push and create a Pull Request
3. Keep the branch as-is (I'll handle it later)

Which option?
```

**Detached HEAD — present exactly these 2 options:**

```
Implementation complete. You're on a detached HEAD (externally managed workspace).

1. Push as new branch and create a Pull Request
2. Keep as-is (I'll handle it later)

Which option?
```

Present the menu exactly as written — concise, with every option coming
from the list above. Discarding the work happens only in response to your
human partner explicitly asking for it (see "If your human partner asks to
discard the work" below). Wait for their answer; the integration decision
is theirs.

## Step 5: Execute Choice

### Option 1: Merge Locally

First locate the main checkout — worktree removal later must run from outside the worktree:

```
git worktree list --porcelain
```

The first `worktree <path>` line is the main checkout's root. Change your working directory there with your own tools, then merge:

```
git checkout <base-branch>
git pull
git merge <feature-branch>
```

The merge fast-forwards when the base has not moved. Then verify tests on the merged result with the project's test command, as Step 1 says.

If the merge reports a conflict, or tests fail on the merged result: stop,
leave the worktree and branch in place, and investigate — nothing has been
pushed, so the merge is local and recoverable. A merge that stopped on a
conflict is undone with `git merge --abort`.

Once the merged result is green: clean up the worktree (Step 6), then
delete the branch:

```
git branch -d <feature-branch>
```

**Branch safety:** `-d` refuses to delete a branch whose commits have not
reached the base. That refusal is a signal, never an obstacle — the merge
did not take. Investigate; never reach for `-D` to make it go away.

### Option 2: Push and Create PR

**The repo's conventions come first:** its PR template, contribution
guide, commit-message rules, sign-off or DCO requirement and hooks
override crucible's defaults. One that would change commits already made,
such as adding sign-offs, is a history rewrite: ask the operator
first.

**Ask about the records.** Where the branch has a feature folder (the one
the resolve step of `skills/redteaming/references/formats.md`
§ Feature folder finds), list the files the branch adds there:

```
git diff --name-only --diff-filter=A <base-branch>...HEAD -- <feature-folder>
```

On an umbrella's own branch, where the list holds
`<feature-folder>/umbrella.md`, drop that file from the list: it stays
in the merged tree, since the umbrella's children read it, marks
included, on the branch they land on
(`skills/brainstorming/references/umbrellas.md`). An empty list leaves
nothing to ask.

Tell the operator that the branch's commits carry these files, so
the PR shows them under any merge strategy and removing them now keeps
them out of the merged tree only; then ask whether they go into the PR.
If not, remove exactly the listed files in a final commit (`git rm`, then
commit) and re-run Step 1's suite on the new HEAD.

Then push:

```
git push -u origin <feature-branch>
```

From a detached HEAD, name the new branch on the remote instead:

```
git push origin HEAD:refs/heads/<new-branch>
```

Open the pull/merge request against <base-branch> with the forge's tooling
and report its URL.

**Keep the worktree:** PR feedback is handled there under
`crucible:receiving-review`, with Step 1's suite run before fixes are
pushed and, after substantial fixes, a fresh review from the PR's
reviewers or `crucible:requesting-code-review`'s standalone mode. New
scope is a new feature: `crucible:brainstorming`.

### Option 3: Keep As-Is

Report: "Keeping branch <name>. Worktree preserved at <path>."

### If your human partner asks to discard the work

This path exists only as a response to an explicit request to throw the
work away. Confirm first:

```
This will permanently delete:
- Branch <name>
- All commits: <commit-list>
- Worktree at <path>

Type 'discard' to confirm.
```

Wait for that exact confirmation. When it arrives, change your working
directory to the main checkout root (Option 1 shows how to find it), clean
up the worktree (Step 6), and force-delete the branch:

```
git branch -D <feature-branch>
```

## Step 6: Cleanup Workspace

**Runs for Option 1 and confirmed discards.** Options 2 and 3 always
preserve the worktree. Both callers have already changed directory to the
main repo root — worktree removal must run from outside the worktree —
and use the values captured in Step 2, from before that directory change.

**If git dir == common dir:** Normal repo, no worktree to clean up. Done.

**If `<worktree-path>` is under `.worktrees/` or `worktrees/`:** This workflow
created the worktree — we own cleanup:

```
git worktree remove <worktree-path>
git worktree prune
```

`prune` is self-healing: it clears any stale registration left behind.

**If removal is refused** because the worktree holds modified or untracked
files: that is the guard working. Nothing is deleted. Report what is
uncommitted and ask the operator — never pass `--force` to get past
it on your own.

**Otherwise:** The host environment owns this workspace — leave it in
place. If your platform provides a workspace-exit tool, use it.

## Quick Reference

| Option | Merge | Push | Keep Worktree | Cleanup Branch |
|--------|-------|------|---------------|----------------|
| 1. Merge locally | yes | - | - | yes |
| 2. Create PR | - | yes | yes | - |
| 3. Keep as-is | - | - | yes | - |
| Discard (explicit request only) | - | - | - | yes (force) |

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Tests passed earlier this session" | Run the suite on the tree you are about to integrate. A green run only proves the tree it ran on. |
| "They obviously want it merged" | Integration is your human partner's decision. Present the menu and wait. |
| "They seem done with this feature — I'll offer to discard it" | The menu is complete as written. Discard happens only when your human partner asks for it in so many words. |
| "'Yeah, get rid of it' counts as confirmation" | Only the typed word `discard` authorizes deletion. |
| "The PR is up, so the worktree is clutter now" | PR feedback gets fixed in that worktree. It stays until the work lands. |
| "This other worktree looks stale — I'll clean it too" | Clean up only worktrees under `.worktrees/` or `worktrees/`. Everything else belongs to the host. |
| "`worktree remove` refused — I'll add --force" | The refusal means uncommitted work is in there. Show the operator what it is; forcing destroys it silently. |
| "`branch -d` refused — I'll use -D" | `-d` refuses because the commits never reached the base. `-D` throws them away. Find out why the merge did not take. |
| "The merged-result failure is probably flaky" | A failing merged result stops everything. Branch and worktree stay put while you investigate. |
| "The base branch is obviously main" | Confirm the fork point or ask. Merging into the wrong base is expensive to undo. |
| "I'll wrap these steps in a shell one-liner" | Each step is one invocation on purpose: the flow has to run where no POSIX shell exists. Carry the values between commands yourself. |
| "The push was rejected — force-push will fix it" | A rejected push means the remote moved. Investigate; force-push only on your human partner's explicit request. |
