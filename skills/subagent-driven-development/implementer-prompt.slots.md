# Slot card — implementer

## Slots

- [TASK]: `Task <N>: <task name>` as in the plan; on the very-small lane, the lane note's title; for a branch-review fix wave, `Branch wave <n> fixes`.
- [REQUIREMENTS]: for a task and its fresh fix-wave implementer, `the plan at <path>, Task <N>`; on the very-small lane, the lane note's path at its pinned revision; for a branch-review fix wave, the spec at its pinned revision and the plan (one document where the plan is folded in).
- [UMBRELLAS]: per the dispatch composition's item 2; else "none".
- [CONTEXT]: one line on where the work fits; neighboring tasks' interfaces and decisions the requirements cannot know; a pointer to any ledger entry parked in its area; the repository's commit conventions (`crucible:using-git-worktrees`), where they go beyond its instruction files. A fix-only dispatch (a fresh fix-wave implementer, a branch-review fix wave) adds the findings to answer, verbatim, each with its id and source report file; a fresh fix-wave implementer is also told a prior implementer worked the task and its report file holds what was tried.
- [PLAN_REMINDER]: one line: the binding acceptance criteria and the Decision Log obligation; on the very-small lane, the note's Acceptance checks; on a fix-only dispatch, each finding fixed or NOT CONFIRMED, each `Change (…)` applied or declined.
- [WORKTREE_PATH]: the assigned worktree, absolute.
- [PLUGIN_ROOT]: the plugin root you read this card from, absolute.
- [REPORT_FILE]: in the feature workspace, `sdd/reports/task-<N>-report.md`, which a fresh fix-wave implementer appends to; on the very-small lane, `sdd/reports/lane-report.md`, which a later part's implementer appends to; for a branch-review fix wave, `sdd/branch-review/wave-<n>-fix.md`.

## Selectors

- lane: very-small | off
  - very-small: the lane pointer line under Requirements; set on the very-small lane
  - off: none; every other dispatch

## Dispatch

- Description: `Implement Task <N>: <task name>`; for a branch-review fix wave, `Fix branch wave <n>`.
- Model: a clearly bounded task may drop to the bounded role.
