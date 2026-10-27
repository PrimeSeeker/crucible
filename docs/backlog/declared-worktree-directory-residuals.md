# Declared worktree directory: two residuals of upstream's git fallback

## Observation

Where a repository's instruction files declare a worktree directory, the
git fallback of `crucible:using-git-worktrees` creates the worktree there,
as upstream does. Two behaviours of that route stay as upstream wrote
them, accepted when the fallback was restored:

- From the main checkout, a declared directory that is not gitignored gets
  `.gitignore` fixed and committed on whichever branch the main checkout
  has checked out, which can be the base branch (`using-git-worktrees`
  Step 1b, § Safety Verification). From another feature's worktree the
  same check commits nothing and reports instead. Not reachable in
  crucible's own repository, whose `.worktrees/` is ignored.
- `crucible:finishing-a-development-branch` Step 6 removes only worktrees
  under `.worktrees/` or `worktrees/`. A worktree in any other declared
  directory is left in place; nothing is destroyed.

## Follow-up

- Whether the Safety Verification's commit should become a report, as it
  already is from another feature's worktree.
- Whether finishing's cleanup should match the directory Step 1b chose
  rather than the two default names.
