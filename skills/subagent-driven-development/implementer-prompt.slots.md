# Slot card — implementer

## Slots

- [TASK]: `Task <N>: <task name>`, as the plan numbers and names it; on the very-small lane, the lane note's title; for a branch-review fix wave, `Branch wave <n> fixes`.
- [REQUIREMENTS]: for a task and its fresh fix-wave implementer, the plan's path and the task's number (`the plan at <path>, Task <N>`); on the very-small lane, the lane note's committed path at its pinned revision; for a branch-review fix wave, the spec at its pinned revision and the plan (one document where the plan is folded into the spec).
- [UMBRELLAS]: per the dispatch composition's item 2; else "none".
- [CONTEXT]: one line on where this work fits; interfaces and decisions from neighboring tasks the requirements cannot know; a pointer to any ledger entry parked in the area it touches. A fix-only dispatch (a fresh fix-wave implementer, a branch-review fix wave) adds the findings to answer, verbatim with their ids and the report files they come from; the fresh fix-wave implementer is also told a prior implementer worked the task and its report file holds what was tried.
- [PLAN_REMINDER]: one line: the binding acceptance criteria and the Decision Log obligation; on the very-small lane, the note's Acceptance checks; on a fix-only dispatch, that each finding is fixed or NOT CONFIRMED, each `Change (…)` applied or declined.
- [WORKTREE_PATH]: the absolute path to the assigned worktree.
- [PLUGIN_ROOT]: the absolute path of crucible's plugin root, the one you read this card from.
- [REPORT_FILE]: in the feature workspace, `sdd/reports/task-<N>-report.md`, which the fresh fix-wave implementer appends to; `sdd/reports/lane-report.md` on the very-small lane; `sdd/branch-review/wave-<n>-fix.md` for a branch-review fix wave.

## Selectors

- lane: very-small | off
  - very-small: the lane pointer line under Requirements; set on the very-small lane's optional implementer dispatch
  - off: none; every other dispatch

## Dispatch

- Description: `Implement Task <N>: <task name>`; for a branch-review fix wave, `Fix branch wave <n>`.
- Model: a clearly bounded task may drop to the bounded role.
