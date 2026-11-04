# Backlog batch 1

Lane: very-small (operator-confirmed 2026-11-04)

## Intent

Close five small backlog items: a contradiction over what binds, text every redteam seat reads and never uses, a missing pointer in inline mode, the two seats that keep skipping their report file, and two loose ends of the unattended-session note.

## Change list

1. **What binds.** `crucible:writing-plans` § Binding vs advisory says that in the plan, each task's Contract and Acceptance and the header's inter-task contracts bind, and in the spec, what the spec pointer names. The implementer template's Binding line adds the task's Contract and Acceptance, and `docs/decisions/task-loop.md` follows, with a Changes line.
2. **The mark's criterion.** The redteam seat stops taking it, since no seat grades marks. `docs/decisions/instruments.md` is corrected, and `skills/subagent-driven-development/references/review-terms.md` keeps the section for plan authors.
3. **Inline mode.** Its task report is pointed at the duty to justify each test deleted or loosened.
4. **Report files.** The verifier's and re-reviewer's cards tell the controller to name the host's file-writing tool, taken from the host map's **Edit** entry, in the report slot. `docs/backlog/review-seat-report-write.md` stays open to count misses, with the model-role observation added as unverified.
5. **Unattended note.** The `hooks/README.md` failure sentence is limited to sessions that load the router, and the reason on the `hooks/session-start` line of `tests/claudeism-allowlist.txt` also covers `claude -p`. The hook does not change.
6. **Backlog and budget.** Delete `what-binds-disagreement.md`, `redteam-seat-marks-criterion.md` and `inline-mode-test-justification.md`, trim `unattended-session-followups.md` to its third bullet, and update `tests/prose-budget.txt`.

## Acceptance

1. "The mark's criterion" is gone from `skills/redteaming/seat-prompt.md`, its source and `agents/redteam-seat.md`, and stays in `review-terms.md`.
2. `skills/subagent-driven-development/references/inline-mode.md` names the deleted-or-loosened duty.
3. "requirements, interfaces, non-goals" is gone from `skills/writing-plans/SKILL.md` and `docs/decisions/task-loop.md`.
4. The Binding line of `skills/subagent-driven-development/implementer-prompt.md` names the task's Contract and Acceptance.
5. `skills/redteaming/verifier-prompt.slots.md` and `skills/subagent-driven-development/re-review-prompt.slots.md` name the host map's **Edit**.
6. The allowlist reason names `claude -p`, and the `hooks/README.md` sentence is limited as above.
7. `python tools/instrument_agents.py check` and `python -m pytest tests/` pass.

## Out of scope

Other backlog items; `record-wording-slips.md`, which waits for those records' next edit; raising these seats' model role; any change to what binds in a spec.
