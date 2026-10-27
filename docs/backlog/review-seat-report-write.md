# Review seats return reports as text, and resolve the scratch path against the wrong root

## Observation

- In one subagent-driven run of fifteen tasks on Claude Code, six of the
  seven scoped re-review dispatches returned their report as their final
  message and wrote no report file. The reasons they gave varied: that no
  write tool was offered, that the write step was skipped, and that
  writing conflicted with a rule against report files. The instrument's
  definition (`agents/re-reviewer.md`) restricts no tools, and the report
  paths did not match the host's report-name filter. The pattern matches
  the host's prose advice that subagents return findings as text, which
  `skills/using-crucible/references/claude-code-dispatch.md` already
  records.
- The blind verifier of the same run's first spec round did the same
  once. Task reviewers, the branch reviewer, redteam seats and the
  terminal pass wrote their files.
- Each miss cost the controller a resume, or a save of the returned text
  with the controller's mark (`skills/redteaming/references/formats.md`
  § Feature workspace root and layout). Saved text is the seat's words,
  but the record no longer shows that the seat wrote it.
- One re-reviewer wrote its scratch diff into the reviewed checkout's
  tracked tree, a `scratch/` directory at the worktree root, instead of
  under the feature workspace. The review templates give the scratch
  location only relatively ("under `scratch/`",
  `skills/subagent-driven-development/re-review-prompt.md` and
  `task-reviewer-prompt.md`), and a seat working from the worktree root
  resolves it there. The tree check voided the review, and it was
  re-dispatched.

## Follow-up

- Make the report file unmistakably the deliverable for the instruments
  that missed it: say near the report section that the file is required
  even where the host advises returning text, and that the reply carries
  only the verdict and the path. Then check whether the re-reviewer's
  miss rate falls.
- Have the slot cards carry the scratch directory as an absolute path,
  or have the templates anchor it to the feature workspace explicitly,
  so no seat resolves it against the checkout it reviews.
