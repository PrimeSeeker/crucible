# Slot card — task-reviewer

## Slots

- [WORKTREE_PATH]: the absolute path to the worktree holding the reviewed branch.
- [PLUGIN_ROOT]: the absolute path of crucible's plugin root, the one you read this card from.
- [MANDATE_REMINDER]: one line restating this review's binding output: all four verdicts, staked severities with evidence, written to this review's report file, and a reply of the task verdict and that file's path.
- [REQUIREMENTS]: the plan's path and the task's number, as the implementer's card named them; then each commit in BASE..HEAD that landed a scoped amendment or a plan-patching ruling, by hash, or "no amendment commits".
- [IMPLEMENTER_REPORT]: the implementer's report file, as its card named it; its Decision Log is the deviation audit's input.
- [REPORT_FILE]: this review's output, in the feature workspace: `sdd/reports/task-<N>-review.md`; `sdd/reports/task-<N>-x<X>-review.md` for re-run <X> after revert-and-replan. A replacement seat adds `-r<R>` before `.md`, as in `sdd/reports/task-<N>-review-r<R>.md`.
- [BASE_SHA]: the commit before this task.
- [HEAD_SHA]: the current commit.

## Selectors

none

## Dispatch

- Operation: a fresh-seat dispatch of instrument `task-reviewer` with this card filled — each slot's rule replaced by its value — through your adapter's instrument-dispatch operation.
- Description: `Review Task <N> (intent + scope + deviations + quality)`.
- Model: REQUIRED: per SDD SKILL.md Models — reviewers run on the bounded role or better, always.
- Effort: per `skills/subagent-driven-development/references/dispatch-composition.md` § Models and effort.
