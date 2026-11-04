# Backlog batch 3: a landing that voids a closing review, and how far a record cut reaches

Lane: very-small (operator-confirmed 2026-11-04)

## Intent

Settle whether another session's landing should void an umbrella's closing review whose range did not move: it keeps doing so, an accepted residual the record states, so the status check stays one rule. Stop a clause-sized edit to a decision record from requiring a cut of the whole record, while keeping the short shape as the goal.

## Change list

1. **The cut rule.** `docs/decisions/decision-records.md` and `AGENTS.md`: a position not yet cut takes the short shape when an edit rewrites it; a clause-sized edit leaves it, and the record's other positions stay as they are. The record's Why gives the reasoning, and its Changes takes a line.
2. **The closing review's window.** `docs/decisions/shared-tree.md`: Why states the residual and what was declined, Rejected names the exception, and Changes takes a line. No skill text changes.
3. **The backlog.**
   - `docs/backlog/skill-text-rewrite.md` loses the item this closes and its follow-up clause.
   - `docs/backlog/decision-record-cut-reach.md` gives way to `docs/backlog/decision-records-uncut.md`, holding what stays open: 22 records not yet cut, about 78 KB of Decision text, which the narrowed rule no longer brings to the short shape on any schedule.
   - `docs/backlog/umbrella-followups.md` gains the question whether children of an incomplete umbrella should land on the base by default: nothing requires a child to leave the base shippable as a product, no record weighs an umbrella branch, and the proposal is to ask at step 4 whether the base can ship with only some children landed, as a feature of its own with a spec campaign.

## Acceptance

1. Text checks, each failing on the pre-change tree unless marked:
   - `skills/` is unchanged from the base (holds on the pre-change tree too, and guards this lane's scope);
   - the `shared-tree.md` Why states the residual, its Rejected names the exception, and its Changes has a line for it;
   - the `decision-records.md` Decision states the rule by rewrite, "is next edited" is gone from that record and from `AGENTS.md`, `AGENTS.md` says "when an edit rewrites", and the record's Changes has a line for it;
   - `decision-record-cut-reach.md` is gone and `decision-records-uncut.md` exists;
   - `skill-text-rewrite.md` no longer holds the closed item or its follow-up clause;
   - `umbrella-followups.md` holds the new question.
2. `python -m pytest tests/` passes.
3. Judged by the branch reviewer: no other site states the old cut rule; the status check stays one rule, and the record's account of it matches the skill text; each basis line matches who proposed the position, from the brainstorm decision record.

## Out of scope

- Cutting any record.
- The other three items `backlog-batch-2` left in `skill-text-rewrite.md`.
- Any change to a status check.
- Designing or changing how an umbrella's children land.
