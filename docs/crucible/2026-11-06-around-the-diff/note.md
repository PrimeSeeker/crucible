Lane: very-small (operator-confirmed 2026-11-06)

# Around the diff

## Intent

Implementers and controllers read "no unrelated refactoring" and the scope gate
conservatively, so safe improvements beside a change get skipped or left as
proposals nobody can judge, a separate proposal depending on someone able to
weigh it, which a non-developer may not be. Make these improvements part of the
work at the design and code stages, and keep larger ones as proposals. No break.

## Change list

- Test first, as below; where today's text does not show the failure, return to
  the operator before writing anything.
- `skills/subagent-driven-development/references/review-terms.md` gains a section
  spliced into the implementer, task-reviewer and branch-reviewer templates:
  "**Around the diff.** An improvement or bug fix you come across in the files
  the task changes, or in what the changed code directly calls or is called by,
  is part of the task: make it where the tests cover it and nothing outside the
  task relies on what it changes, and log it in one line in the Decision Log.
  Propose instead of making one that needs another task's file, binding content,
  a new capability or a restructure. A fix wave makes only what its findings
  need. A logged one inside this boundary is not extra and passes scope, and is
  judged on quality; one beyond it fails scope."
- Implementer template: the "improve code you touch" clause gives way to the
  section; the self-review line is aligned.
- Task reviewer: the scope verdict is aligned. Branch reviewer: takes the section.
- `skills/brainstorming/SKILL.md`: the design-stage sentence becomes "include
  improvements and bug fixes in or beside what the work changes where they are
  reasonably safe; propose what significantly exceeds that."
- `skills/subagent-driven-development/references/very-small-lane.md` step 2 and
  `inline-mode.md`: the same section binds the controller; on the lane the log
  line is the existing `Departure:` line.
- `docs/decisions/task-loop.md`: the position, the test's figures and limits, a
  Changes line. `tests/prose-budget.txt` raised. Templates regenerated.

## Acceptance

- A search finds `## Around the diff` once in `review-terms.md` and once each in
  the rendered `implementer-prompt.md`, `task-reviewer-prompt.md` and
  `code-reviewer.md`.
- A search finds no `no unrelated refactoring` in `skills/brainstorming/SKILL.md`.
- `docs/crucible/2026-11-06-around-the-diff/microtest/README.md` exists, with
  each arm's reading.
- `python -m pytest tests/` passes.

## Out of scope

- Redteam seats' handling of improvements.
- The cleanup wave, the wave cap and the re-reviewer.
- `crucible:systematic-debugging`'s rule against bundling changes with a fix under
  diagnosis.
- A per-feature cleanup allowance.
- Measuring real features.
