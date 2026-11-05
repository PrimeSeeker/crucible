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
- The re-review and verifier templates say the report file is required
  even where the host advises returning text, and every read-only seat's
  slot card carries its scratch directory as an absolute path.
- On the two runs after the report-file change, the misses persisted in the blind
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
  - In a third run (2026-11-03, six tasks with a spec campaign of two
    rounds and two terminal passes), four reports came back as text: the
    blind verifiers of the second spec round and of the plan phase, which
    said no write tool was available to them, and both branch-review
    re-reviewers, one citing no write tool and one its instructions
    barring report files. Each was saved by the controller under its
    mark; dispatches telling the seat to write with its Write tool "if
    you have it" did not change the outcome. Panel seats, pre-passes,
    terminal passes, implementers, task reviewers, a task re-reviewer and
    the branch-review passes wrote theirs.

- Since 2026-11-04 the verifier's and the re-reviewer's cards have the
  controller name the host's file-writing tool in the report slot,
  through the host map, with no "if you have it". The evidence is thin
  and mixed: one write under unhedged wording, four misses in the third
  run under the hedged one. That dropping the hedge helps is unverified,
  and naming a tool may not answer a seat that says its instructions bar
  report files. The first four uses, all branch-review re-reviewers on the bounded
  role, wrote on their first return; no verifier has run under it yet.
- These two are the only review seats whose cards name the bounded role;
  the other review seats run on the default role, and an implementer may
  drop to the bounded role on a clearly bounded task. Whether the role is
  the cause is UNVERIFIED: the dispatches' models are not in this item,
  and a task re-reviewer wrote its report in the third run.
- The check on an appended report asks that it hold the seat's section
  (`skills/subagent-driven-development/references/dispatch-composition.md`,
  item 5), and nothing marks whose section is whose. A seat re-dispatched
  to the same report whose own write failed passes on the earlier attempt's
  section. No run on record has hit it.

## Follow-up

- Count report-file misses, and scratch files written outside the
  workspace, on the runs after, recording each seat's model.
- If the misses persist, carry the report path too as an absolute path
  in the slot cards, as the scratch directory now is.
