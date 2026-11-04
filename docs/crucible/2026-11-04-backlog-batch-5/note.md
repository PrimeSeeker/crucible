# Backlog batch 5: five small text fixes

Lane: very-small (operator-confirmed 2026-11-04)

## Intent

Close five backlog items whose fix is already stated: two sites misstating what binds in a plan; the unstated-break route's two gaps; four slips in the decision records; the first three umbrella follow-ups; and the save path that can overwrite an appended report. No break.

## Change list

1. `references/review-terms.md` § Finding scope: "content a format requires", not "makes binding". `code-reviewer.source.md`: the drift rule names the binding plan items.
2. `requesting-code-review/SKILL.md`: an `unstated break` is written open under `## Adjudication rulings`. `references/finish.md`: the readout's break line includes one still open. `code-reviewer.source.md`: the label sentence and the verdict line name it beside `premise`.
3. `references/umbrellas.md` § Shape: a line of text after the Children list's last entry. `references/seat-rules.md` § Binding changes: a feature's own entry is the one naming its feature folder's slug. `brainstorming/SKILL.md`: Flow step 4 points to the arrangement and umbrella sections; the scope check says what it asks of an umbrella's own draft.
4. `redteaming/references/formats.md`: a report saved to an appended report is appended, the mark opening its section.
5. Records: `evidence-and-findings.md` names the closing-review seats; `umbrellas.md` dates the clause; `routes.md` and `task-loop.md` say which calls were left to the agent; `instruments.md`'s Changes line stops reading as an event. Positions and Changes lines for items 2 to 4.
6. Regenerate the templates. `tests/prose-budget.txt`: raise the numbers.
7. `docs/backlog/`: delete `plan-binding-reach.md`, `unstated-break-route.md`, `record-wording-slips.md`; remove the three points from `umbrella-followups.md` and the save path from `lane-split-seams.md`.

## Acceptance

1. A text check for each clause and removal, failing before the change and passing after.
2. The instrument check exits 0.
3. The full suite passes.

## Out of scope

- The other points in `umbrella-followups.md` and `lane-split-seams.md`.
- Any new test beyond the budget numbers.
- Minors that could not lose a record and sit on a path no run has reached: filed, not fixed.
