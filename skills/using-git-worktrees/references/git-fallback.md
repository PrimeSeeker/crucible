### 1b. Git Worktree Fallback

#### Directory Selection

**`<project-root>`** is the checkout you are in; from another feature's linked worktree, it is the main checkout, the parent of the common dir Step 0 printed.

Use the worktree directory your instructions declare, without asking; else an existing `.worktrees/` or `worktrees/` at `<project-root>` (list it with your own file-listing tool), `.worktrees/` winning if both exist; else `.worktrees/` there. The selection is `<worktree-dir>` from here on: the check and the create below run against it, never a remembered default.

#### Safety Verification (project-local directories only)

Before creating, run `git -C <project-root> check-ignore -q <worktree-dir>/`. Keep the trailing slash: without it, Git reports an ignored directory that does not exist yet as not ignored.

Exit 0 means ignored: proceed. Exit 1 means not ignored: commit nothing, put it to the operator as a decision ask, recommending the ignore entry and the branch it goes on, and re-run the check on the same directory once they settle it.

#### Create the Worktree

When brainstorming's call or a declared directory brought you here, `<base>` is the repo's base branch or one the operator named; otherwise `HEAD`. Create the worktree in the same `<worktree-dir>` with `git -C <project-root> worktree add <worktree-dir>/<branch-name> -b <branch-name> <base>`, then make the new worktree your working directory with your own tools.

If `-b` refuses because the branch name exists, nothing was created: pick a fresh name or check out the existing branch deliberately; never force past it.

If `git worktree add` fails with a permission error (sandbox denial), tell the user the sandbox blocked worktree creation and you're working in the current directory instead; then run setup and baseline tests in place.
