# Slot card — task-reviewer

## Slots

- [WORKTREE_PATH]: the absolute path to the worktree holding the reviewed branch.
- [PLUGIN_ROOT]: the absolute path of crucible's plugin root, the one you read this card from.
- [MANDATE_REMINDER]: one line restating this review's binding output: all four verdicts, a ruling on each concern the implementer reports, staked severities with evidence, questions, written to this review's report file, and a reply of the task verdict and that file's path.
- [REQUIREMENTS]: the plan's path and the task's number, as the implementer's card named them; then each commit in BASE..HEAD that landed a scoped amendment or a plan-patching ruling, by hash, or "no amendment commits".
- [UMBRELLAS]: per the dispatch composition's item 2; else "none".
- [IMPLEMENTER_REPORT]: the implementer's report file, as its card named it; its Decision Log is the deviation audit's input.
- [REPORT_FILE]: this review's output, in the feature workspace: `sdd/reports/task-<N>-review.md`.
- [SCRATCH_DIR]: the seat's scratch directory, absolute.
- [BASE_SHA]: the commit before this task, as recorded at its implementer's dispatch — never `HEAD~1`, which drops all but the last commit of a multi-commit task.
- [HEAD_SHA]: the current commit.

## Selectors

none

## Dispatch

- Description: `Review Task <N> (intent + scope + deviations + quality)`.
