# Per-task review as a plan choice

## Observation

- On crucible's own umbrella-specs feature (2026-10-28, five tasks, all
  prose), the issues that mattered surfaced in the implementers'
  `DONE_WITH_CONCERNS` reports: a duplicated rule, ceremony for an
  approval-only document, a rule two phases could never reach, and
  wrong Basis tags in a decision record. The five task reviewers
  approved every task and raised only minors; the branch review
  confirmed the unreachable rule as its one MAJOR.
- An escape analysis of 109 features' histories, on crucible and one
  other project (2026-10-28), found task reviews letting through 12
  real defects: 10 minor wording, consistency or comment slips, and 2
  premise-level MAJORs that needed other tasks' knowledge, both caught
  by the branch review.
- Since then the task reviewer runs on the default role, every task,
  and rules on every concern the implementer reports
  (`docs/decisions/task-loop.md`).

## Follow-up

**Per-task review as a plan choice** (maintainer agreed): for tasks
that are sequential on shared files and low in mechanism, such as
prose, the plan may route review to the branch review alone, keeping
the implementer's concerns as the per-task net. Who rules on those
concerns when no task review runs is part of the choice. Taken up by
the `arrangements` child of
`docs/crucible/2026-10-28-hypothesis-specs/umbrella.md`.
