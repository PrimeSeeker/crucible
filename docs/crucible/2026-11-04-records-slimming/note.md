Lane: very-small (operator-confirmed 2026-11-04)

# Slim the decision records, and settle when an edit needs a Changes line

## Intent

Stop the decision records restating skill procedure, so a skill edit stops leaving a record untrue with no test failing and stops forcing a repeat edit. A record's Decision states positions and points at the skill heading holding the procedure. Settle when a record edit needs a Changes line, and fix the slips listed in `docs/backlog/decision-records-upkeep.md`.

## Change list

- `AGENTS.md`, `docs/decisions/decision-records.md`: a Changes line goes with an edit that changes a decision or its reasoning; an edit that changes neither, such as a citation, wording or a cut of restated text, adds none, and its commit says what it did. A Decision points at procedure rather than restating it, and other records follow when next edited. `decision-records.md` takes its Why, a Rejected entry for removing Changes sections, and a Changes line. `tests/test_decision_records.py`'s docstring follows.
- Decision sections of `branch-review`, `evidence-and-findings`, `task-loop`, `records-and-workspace`, `spec-campaign`, `umbrellas`, `plans`, `the-spec`: each position in a sentence or two with a pointer.
- The backlog item's slips, at their sites. Its two `routes.md` bases get checked against whatever decision record survives, and what can't be checked is reported.
- `docs/backlog/decision-records-upkeep.md` deleted once nothing in it stays open.

## Acceptance

1. `python -m pytest tests/` passes, its reference scanner resolving every new pointer.
2. `git diff --name-only <base>...HEAD -- skills agents hooks tools` prints nothing.
3. The new Changes rule is in both files, and the old "every edit" wording is in neither.
4. Each slip's check passes: `the-spec.md` names binding content; the anchor limit is stated in `authoring-crucible.md` and the scanner's docstring; `dual-runtime.md`'s "rules above" pointer is gone; the user-level home is in the `records-and-workspace.md` Decision; `shared-tree`, `git-steps` and `evidence-and-findings` point at `rejected-machinery.md`; no bare "(§ Why)" Rejected entry remains in the five named records; the backlog item is gone.
5. Each of the eight records' Decision word counts falls, with no target.
6. Judged by the branch reviewer: each removed sentence's content is at the heading its pointer names, or still in the record; a record citing one of the eight for a statement still finds it there or one pointer on; each Rejected entry in the five records says why not.

## Out of scope

- Any skill, agent, hook or tool change. A disagreement between a record and a skill is reported, not resolved here.
- Why, Rejected and existing Changes lines, apart from the slips above and `decision-records.md`'s own additions.
- Decision sections of the other 22 records, apart from the slips.
