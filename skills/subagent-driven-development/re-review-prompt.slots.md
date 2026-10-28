# Slot card — re-reviewer

## Slots

- [WORKTREE_PATH]: the absolute path to the worktree holding the fixed branch.
- [PLUGIN_ROOT]: the absolute path of crucible's plugin root, the one you read this card from.
- [MANDATE_REMINDER]: one line restating this re-review's binding output: a verdict on every listed finding, a ruling on each fix-report concern, new breakage in the fix diff only, and the wave verdict, written to this re-review's report file, and a reply of the wave verdict and that file's path.
- [REQUIREMENTS]: in a task's fix wave, the plan's path and the task's number, as the implementer's card named them, then each commit in FIX_BASE..HEAD that landed a scoped amendment or a plan-patching ruling, by hash, or "no amendment commits"; in a branch-review wave, the spec at its pinned revision and the plan (one document where the plan is folded into the spec); on the very-small lane, the lane note at its pinned revision.
- [UMBRELLAS]: where the spec's preamble carries an `Umbrella:` line (on the very-small lane, the note's), the umbrella it names and each one up the chain, by path; else "none".
- [FINDINGS]: the findings this wave's fix report answers fixed, copied verbatim from the review that raised them, one per bullet — never those it answers NOT CONFIRMED, which go to the adjudicator.
- [FIX_REPORT]: in a task's fix wave, the implementer's report file, this wave's fix report appended; in a branch-review wave, `sdd/branch-review/wave-<n>-fix.md` — on the very-small lane the controller's own, held to the same fix-report contract.
- [REPORT_FILE]: this re-review's output, in the feature workspace: `sdd/reports/task-<N>-re-review-w<W>.md` for task fix wave <W>, `sdd/reports/task-<N>-x<X>-re-review-w<W>.md` in re-run <X> after revert-and-replan; `sdd/branch-review/wave-<n>-re-review.md` for branch-review wave <n>. A replacement seat adds `-r<R>` before `.md`, as in `sdd/reports/task-<N>-re-review-w<W>-r<R>.md`.
- [FIX_BASE_SHA]: the head the previous review saw.
- [HEAD_SHA]: the current commit.

## Selectors

- lane: very-small | off
  - very-small: the lane passage under Requirements; set for each inline fix wave's re-review on the very-small lane
  - off: none; every other re-review

## Dispatch

- Operation: a fresh-seat dispatch of instrument `re-reviewer` with this card filled — each slot's rule replaced by its value, each selector line cut to its one value and its sub-bullets dropped — through your adapter's instrument-dispatch operation.
- Description: `Re-review Task <N> fix wave <W>`, or `Re-review branch wave <n>` for a branch-review wave.
- Model: REQUIRED: per SDD SKILL.md Models — the re-reviewer runs on the bounded role or better, always, scoped re-reviews of small fix diffs included.
- Effort: per `skills/subagent-driven-development/references/dispatch-composition.md` § Models and effort.
