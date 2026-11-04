# Slot card — task-reviewer

## Slots

- [WORKTREE_PATH]: the reviewed branch's worktree, absolute.
- [PLUGIN_ROOT]: the plugin root you read this card from, absolute.
- [MANDATE_REMINDER]: one line restating this review's binding output: in the report file, all four verdicts, a ruling on each concern the implementer reports, staked severities with evidence, and questions; a reply of the task verdict and that file's path.
- [REQUIREMENTS]: the plan's path and task number, as the implementer's card named them; then, by hash, each BASE..HEAD commit that landed a scoped amendment or a plan-patching ruling, or "no amendment commits"; for a `plan changed` line's re-run, also each merge its receiving step took, whose content is the base's, not the task's.
- [UMBRELLAS]: per the dispatch composition's item 2; else "none".
- [IMPLEMENTER_REPORT]: the implementer's report file, as its card named it; for a `plan changed` line's re-run, each earlier run's too.
- [REPORT_FILE]: in the feature workspace, `sdd/reports/task-<N>-review.md`.
- [SCRATCH_DIR]: the seat's scratch directory, absolute.
- [BASE_SHA]: the commit before this task, recorded at its implementer's dispatch; never `HEAD~1`.
- [HEAD_SHA]: the current commit.

## Selectors

none

## Dispatch

- Description: `Review Task <N> (intent + scope + deviations + quality)`.
