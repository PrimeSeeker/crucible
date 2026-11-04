# Backlog batch 2: nine steps with no stated next action

Lane: very-small (operator-confirmed 2026-11-04)

## Intent

Give a controller a stated next step in nine places where crucible's text leaves it none, so a run neither stalls nor improvises there.

## Change list

1. **Repair re-check.** Where the wave's verifier gave the failing verdict, the re-check is a fresh blind verifier, given only the repaired items and their diff. It writes `verifier-recheck.md` beside `verifier.md`, and the round layout lists that file.
2. **Untraced hunk.** A hunk the verifier traces to no fix item is reverted as a scoped repair; where an item needs it, it is named under that item in the verifier block with the reason instead. `verified` waits until each is resolved.
3. **The spec terminal pass's follow-up wave.** Its record carries a verifier block and its report is `terminal-pass/verifier.md`. `verified` there also requires that block where the wave ran.
4. **A round 1 recorded degraded.** Where no returned seat ran the goal check, the outside-the-frame lens or the alternate-role swap, the next round runs it as round 1 would.
5. **A task waiting on the operator after BLOCKED.** It gets a `Task <N>: BLOCKED — <what it waits on>` ledger line, so a resume after compaction does not re-dispatch it. The re-dispatch after the answer adds the next line, which ends the wait.
6. **The lane's implementer reporting NEEDS_CONTEXT or BLOCKED.** Missing context: provide it and re-dispatch. A reasoning problem: bump the tier, the operator deciding at the default role. A change too big for one implementer: a decision ask, staying on the lane or moving to the standard route.
7. **An umbrella's closing-review seats.** Their dispatch window takes the status check.
8. **A plan change after three fix waves.** A `Task <N>: plan changed — <the ruling>` line; the task re-runs from step 1 on the changed plan, its BASE kept and the open findings passed as context, so its review re-grades them. Report paths count this line as they count a revert.
9. **A review missing a verdict.** Resume the seat for it; where the host cannot resume or the verdict is still missing, start a replacement seat. The controller never rules on it itself. This goes in the rules every route shares, since the lane does not load the task loop's text.

Also: `## Changes` lines in the decision records whose decisions change, the prose budget, and the backlog (`docs/backlog/verifier-repair-gaps.md` deleted, these items removed from `docs/backlog/skill-text-rewrite.md`).

## Acceptance

- Each of these text checks finds its text (all fail on the pre-change tree, 7b8e314):
  - `verifier-recheck.md` in `skills/redteaming/references/round-record.md`, `skills/redteaming/references/fix-application.md` and `skills/redteaming/verifier-prompt.slots.md`;
  - `untraced hunk` in `fix-application.md` and `round-record.md`;
  - `terminal-pass/verifier.md` in `verifier-prompt.slots.md`, and `fields 1, 2, 6, 7 and 8` in `round-record.md`;
  - `A round 1 recorded degraded` in `skills/redteaming/references/panels.md`, and `degraded` in `skills/redteaming/seat-prompt.slots.md`;
  - `BLOCKED — <what it waits on>` in `skills/subagent-driven-development/references/task-loop.md`;
  - `NEEDS_CONTEXT` in `skills/subagent-driven-development/references/very-small-lane.md`;
  - `status check` in `skills/brainstorming/references/umbrellas.md`;
  - `plan changed` in `skills/subagent-driven-development/SKILL.md` and `skills/subagent-driven-development/references/drift.md`;
  - `A review missing a verdict` in `skills/subagent-driven-development/SKILL.md`.
- `python -m pytest tests/` passes, its generated-files check included.
- Each decision this lane changes has a line in its record's `## Changes`.

## Out of scope

- The rest of `docs/backlog/skill-text-rewrite.md`, the closing seats' report form included.
- `docs/backlog/small-wave-full-pass.md` and the other backlog items.
- Any new test: agents read these rules, not code.
