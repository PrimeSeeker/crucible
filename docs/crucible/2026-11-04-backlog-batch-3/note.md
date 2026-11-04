# Backlog batch 3: a landing that voids a closing review, and how far a record cut reaches

Lane: very-small (operator-confirmed 2026-11-04)

## Intent

Stop another session's landing voiding an umbrella's closing review whose range did not move, while still catching a seat's own commit. Stop a clause-sized edit to a decision record from requiring a cut of the whole record, while keeping the short shape as the goal.

## Change list

1. **The cut rule.** `docs/decisions/decision-records.md` and `AGENTS.md`: a position not yet cut takes the short shape when an edit rewrites it; a clause-sized edit leaves it, and the record's other positions stay as they are. The record's Why gives the reasoning, and its Changes takes a line.
2. **The closing review's window.** `skills/brainstorming/references/umbrellas.md` § Closing review, Seats: the status check stands, except that a HEAD moved only by `merge` or `pull` entries in `git reflog` since dispatch voids nothing; any other entry, a seat's `commit` among them, still voids. The prose budget rises to match.
3. **Its record.** `docs/decisions/shared-tree.md`: the same exception in the Decision, its reasoning in Why, including the accepted gap that a seat opening a working file during a landing can see newer text, and a Changes line.
4. **The backlog.**
   - `docs/backlog/skill-text-rewrite.md` loses the item this closes and its follow-up clause.
   - `docs/backlog/decision-record-cut-reach.md` gives way to `docs/backlog/decision-records-uncut.md`, holding what stays open: 22 records not yet cut, about 78 KB of Decision text, which the narrowed rule no longer brings to the short shape on any schedule.
   - `docs/backlog/umbrella-followups.md` gains the question whether children of an incomplete umbrella should land on the base by default: nothing requires a child to leave the base shippable as a product, no record weighs an umbrella branch, and the proposal is to ask at step 4 whether the base can ship with only some children landed, as a feature of its own with a spec campaign.

## Acceptance

1. Text checks, each failing on the pre-change tree:
   - the closing seats' text names `git reflog`, `merge` and `pull` and says such a move voids nothing, and the old sentence is gone;
   - the `shared-tree.md` Decision carries the exception, and its Changes has a line for it;
   - the `decision-records.md` Decision states the rule by rewrite, "is next edited" is gone from that record and from `AGENTS.md`, `AGENTS.md` says "when an edit rewrites", and the record's Changes has a line for it;
   - `decision-record-cut-reach.md` is gone and `decision-records-uncut.md` exists;
   - `skill-text-rewrite.md` no longer holds the closed item or its follow-up clause;
   - `umbrella-followups.md` holds the new question.
2. `python -m pytest tests/` passes.
3. Judged by the branch reviewer: the exception still voids a window on a seat's commit; no other site states the old cut rule or an unexcepted closing-review check; each basis line matches who proposed the position, from the brainstorm decision record.

## Out of scope

- Cutting any record.
- The other three items `backlog-batch-2` left in `skill-text-rewrite.md`.
- The status check of any other window.
- Designing or changing how an umbrella's children land.
