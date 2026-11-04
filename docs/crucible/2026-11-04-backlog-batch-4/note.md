# Backlog batch 4: three gaps in what the controller does next

Lane: very-small (operator-confirmed 2026-11-04)

## Intent

Close three gaps in what the controller does next: a `BLOCKED` raised during a fix wave loses its wave on resume; a `plan changed` re-run must name a merge to its reviewer, and the reviewer's card has no place for it; nothing says what follows the operator's "stay" for a change too big for one implementer. No break.

## Change list

1. `skills/subagent-driven-development/references/task-loop.md`, step 2's wait sentence: in a fix wave the line reads `Task <N>: BLOCKED — wave <W>: <what it waits on>`; after the answer that wave continues, and its `fix wave <W>/3` line ends the wait.
2. `skills/subagent-driven-development/SKILL.md`, resume rule: a task whose latest line is an answered `BLOCKED — wave <W>` resumes inside that wave, not at step 1 and not counting it again.
3. `skills/subagent-driven-development/task-reviewer-prompt.slots.md`, `[REQUIREMENTS]`: also each merge a `plan changed` re-run's receiving step took, whose content is the base's, not the task's.
4. `skills/subagent-driven-development/references/very-small-lane.md`, step 2: on staying, split the change, one fresh implementer per part, in order, each told what the earlier parts committed.
5. `skills/subagent-driven-development/implementer-prompt.slots.md`, `[REPORT_FILE]`: a later part's implementer appends to `lane-report.md`.
6. `docs/decisions/task-loop.md` and `docs/decisions/routes.md`: the positions and their `## Changes` lines.
7. `docs/backlog/skill-text-rewrite.md`: remove the three items. `tests/prose-budget.txt`: raise the number.

## Acceptance

1. A text check for each new clause, failing before the change and passing after.
2. The backlog file no longer lists the three.
3. The instrument check exits 0.
4. The full suite passes.

## Out of scope

- The other 11 points in `docs/backlog/skill-text-rewrite.md`.
- A `BLOCKED` in a branch-review wave (the pending-ask carrier is filed in `docs/backlog/unstated-break-route.md`).
- Any new test beyond the budget number.
