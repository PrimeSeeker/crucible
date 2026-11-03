### 1b. Git Worktree Fallback

Create a worktree manually using git.

#### Directory Selection

**`<project-root>`** is the checkout you are in — from another feature's linked worktree, the main checkout: the parent of the common dir Step 0 printed.

Follow this priority order. Explicit user preference always beats observed filesystem state.

1. **Check your instructions for a declared worktree directory preference.** If the user has already specified one, use it without asking.

2. **Look for an existing project-local worktree directory** at `<project-root>` — `.worktrees/` (preferred, hidden) or `worktrees/`. Use whichever exists; if both do, `.worktrees/` wins. List the directory with your own file-listing tool; this needs no shell.

3. **If there is no other guidance available**, default to `.worktrees/` at `<project-root>`.

**Whatever you selected is `<worktree-dir>` from here on** — the steps below
verify and create against *that* directory, never against a remembered
default.

#### Safety Verification (project-local directories only)

**MUST verify the selected directory is ignored before creating the worktree:**

```
git -C <project-root> check-ignore -q <worktree-dir>/
```

Read the exit code: **0** means ignored — proceed. **1** means not ignored — add that directory to `.gitignore`, commit the change, then re-run the check against the same directory. From another feature's worktree, commit nothing: report the result to the operator and wait for their answer.

**Substitute your selection, and keep the trailing slash:** without the
slash, Git reports an ignored directory that does not exist yet as not
ignored.

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
