# Review seats return reports as text: the fix has not taken

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
- In a later run of five tasks, two of the five task reviewers wrote
  no file on their first return: one said its tools could not write the
  folder, the other skipped the write and wrote it when resumed.
- Since then the re-review and verifier templates say the report file is
  required even where the host advises returning text, and every review
  and seat template gives the scratch path from the checkout's root
  (`.crucible/<feature-slug>/scratch/…`).
- On the two runs after that change, the misses persisted in the blind
  verifier and the scoped re-reviewer, and in no other seat:
  - In the first, read from its session transcripts, both blind
    verifiers wrote no file on their first return and wrote it when
    resumed once. Two scoped re-reviewers, one in a task's fix wave and
    one in a branch-review fix wave, reported the write barred ("my
    instructions bar report files") and returned the report as text,
    which the controller saved under its mark. Panel seats, task
    reviewers, the branch-review passes and the terminal passes wrote
    theirs.
  - In the second, read from its workspace records, two of the three
    spec-campaign blind verifiers wrote no file on their first return and
    wrote it when resumed once. The plan phase's verifier, every panel
    seat and pre-pass, every terminal-pass read, seven implementers and
    seven task reviewers wrote theirs on the first return. The
    controller's dispatch constraints added "Write your report file
    before replying" from the second spec round, under which one verifier
    still missed, and "Use your Write tool to write…" from the plan
    phase, under which none did; that is one dispatch under the second
    wording, so it shows no effect yet.

## Follow-up

- Have the verifier's and the re-reviewer's cards name the host's
  file-write tool for the report, through the host map, since the one
  verifier dispatched under that wording wrote on its first return;
  count report-file misses, and scratch files written outside the
  workspace, again on the runs after.
- If the misses persist, carry the scratch directory, and with it the
  report path, as an absolute path in the slot cards.
