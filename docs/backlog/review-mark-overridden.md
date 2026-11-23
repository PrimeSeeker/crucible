# A task's `Review: branch only` mark rarely takes effect

## Observation

- A plan may mark a task `Review: branch only`; a report raising a concern
  sends the task to its task review anyway
  (`docs/decisions/task-loop.md` § Branch review only).
- In the re-audit of 2026-11-23, over 36 features of one code project on
  crucible 0.33.1, 17 tasks in 13 features carried the mark. 3 completed
  branch review only, and the branch review found nothing on them. 13 went
  to a task review because the implementer reported concerns, and one ran
  inline, which keeps its task review.
- Concerns are near-universal: 114 of 144 task implementers reported
  `DONE_WITH_CONCERNS`, so the mark's condition almost never holds.
- 4 of the 14 tasks reviewed despite the mark drew fixes, all prose
  defects, such as stale descriptions and a record contradicting the
  shipped prompts, which the branch review, reading the whole diff, would
  plausibly have caught: a reader's judgment.

## Follow-up

- Decide whether the mark is worth keeping while any concern overrides it,
  and what, if anything, should. No fix is designed here.
