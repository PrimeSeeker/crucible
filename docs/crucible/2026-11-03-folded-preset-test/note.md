Lane: very-small (operator-confirmed 2026-11-03)

# Folded preset: the test behind the task count

## Intent

At step 4, the choice between the folded and standard presets rests on what the task count stood for. The plan phase reviews a plan's decomposition: who owns which file, the order of the tasks, the seams between them and where acceptance lands. So folded fits where that decomposition needs no review of its own. Folding also costs reading. Every seat executing a folded plan reads the whole document. The plan half is also written before a campaign chosen because an overturn is expected. So folded needs task entries short enough for every seat to read them all. A controller's proposal justifies its choice by these conditions, never by a count of tasks.

## Change list

Advisory.

- `skills/brainstorming/references/proposing-the-arrangement.md`:
  - the overturn-expected bullet states the two conditions in place of "one or two tasks";
  - the counts bullet adds task counts;
  - the proposal's "plan-size reason" becomes the reason the fold fits.
- `docs/decisions/routes.md`:
  - the Decision states the same test and the proposal's reason;
  - a Why paragraph gives the count's origin, its lapsed digest leg, the maintainer's decomposition argument and the reading cost that remains, each with its basis;
  - the Rejected entry on counts covers task counts;
  - a Changes line.
- `README.md`: the folded preset's line drops "one or two tasks".
- `tests/prose-budget.txt`: brainstorming's line follows its count.

## Acceptance

1. `python -m pytest tests/` passes.
2. `grep -nE "two tasks|plan-size" skills/brainstorming/references/proposing-the-arrangement.md docs/decisions/routes.md README.md` prints nothing.
3. `grep -nE "^- 2026-11-03: .*folded" docs/decisions/routes.md` prints the new Changes line.

## Out of scope

Measuring folding's reading cost against a plan phase's; the unfold rule; the task-sizing calibration (`docs/backlog/outcome-evidence.md`); any other preset's test.
