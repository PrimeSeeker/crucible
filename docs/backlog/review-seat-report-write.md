# Review seats return reports as text: check the fix took

## Observation

- In one subagent-driven run of fifteen tasks on Claude Code, six of the
  seven scoped re-review dispatches returned their report as their final
  message and wrote no report file. The reasons they gave varied: that no
  write tool was offered, that the write step was skipped, and that
  writing conflicted with a rule against report files. The blind
  verifier of the same run's first spec round did the same once. The
  pattern matches the host's prose advice that subagents return findings
  as text, which `skills/using-crucible/references/claude-code-dispatch.md`
  records.
- In the same run one re-reviewer wrote its scratch diff into a
  `scratch/` directory at the reviewed worktree's root, since the
  templates then gave the scratch location only relative to the feature
  workspace.
- The re-review and verifier templates now say the report file is
  required even where the host advises returning text, and every review
  and seat template gives the scratch path from the checkout's root
  (`.crucible/<feature-slug>/scratch/…`). Whether that changes what seats
  do is unmeasured.

## Follow-up

On the first subagent-driven runs after the release that carries the
change, count the re-review and verifier dispatches that wrote no report
file or wrote scratch files outside the workspace. If the misses persist,
consider carrying the scratch directory as an absolute path in the slot
cards.
