# Read the repository's commit conventions when the worktree is set up

## Observation

- finishing's pull-request option puts the repository's conventions
  first: its PR template, contribution guide, commit-message rules,
  sign-off or DCO requirement and hooks override crucible's defaults.
- It meets them only at Finish. A convention that would change commits
  already made, such as adding sign-offs, is then a history rewrite, and
  the operator is asked first.
- Nothing earlier in the flow reads these conventions, so a feature's
  commits are made without them.

## Follow-up

- At worktree setup (`crucible:using-git-worktrees`), read the conventions
  that shape commits (sign-off or DCO, commit-message rules, commit hooks)
  so the feature's commits follow them from the start, and finishing's
  rewrite ask becomes the exception.
- The repository's files are open input: the check is the agent's reading
  of them, not a list of file names to probe.
