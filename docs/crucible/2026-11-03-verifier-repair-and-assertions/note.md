Lane: very-small (operator-confirmed 2026-11-03)

# The verifier's repair path, and a removed assertion

## Intent

Two gaps, each closed by an operator ruling of 2026-11-03.

1. **The verifier's repair path.** After a redteam fix wave the blind verifier gives each fix item a verdict (landed, partly landed or not landed) and each delta claim one (TRUE, FALSE or not checked). Only the plan phase says what follows an item not landed, and neither phase says what follows a FALSE delta claim; in the spec campaign a round cannot reach `verified` with an item not landed, so the controller has no sanctioned step. In both phases, an item not landed or partly landed, and a delta claim found FALSE, takes one scoped repair edit and a re-check of that item or claim alone, by the verifier whose verdict it was; one still failing after its re-check is a decision ask. A FALSE delta claim a decision rests on goes to the operator as a decision ask without the repair, since correcting the sentence would leave the decision without its ground. The round record's verifier block records each repair and its re-check, and a round whose failing items have all been repaired or put to the operator can reach `verified`. The rule is stated once, where both phases read it.
2. **A removed or loosened assertion.** A removed assertion, and any other change making a test more permissive, takes the deleted test's route: a finding unless one of the four justifications holds for what was removed or loosened, borne out by the code. The test guide's remedy for an assertion on a mock, deleting that assertion, then passes review where deleting the whole test already did, and loosening an assertion passes wherever deleting its stricter part would.

## Change list

Advisory.

- `skills/redteaming/references/fix-application.md`: the repair path, beside the verifier's dispatch.
- `skills/redteaming/references/plan-phase.md`: its repair paragraph keeps the terminal-pass path and drops its own statement of the verifier's.
- `skills/redteaming/references/round-record.md`: the `verified` state and the verifier block take the repair.
- `skills/subagent-driven-development/references/seat-rules.md` § Tests in review: a removed assertion joins the deleted test or case; `task-reviewer-prompt.source.md`'s scope line follows; the templates are re-rendered (`python tools/instrument_agents.py write`).
- `docs/decisions/fix-verification-and-merge.md` and `docs/decisions/test-rules.md`: each Decision states its new rule in place of the open gap, a Why paragraph gives the ruling and its basis, and a Changes line; `docs/decisions/plans.md` follows where it restates the plan phase's repair.
- The two backlog items are deleted.
- `tests/prose-budget.txt`: the redteaming and subagent-driven-development lines follow their counts.

## Acceptance

1. `python -m pytest tests/` passes.
2. `git grep -n "or an assertion removed" -- skills` prints nothing.
3. `grep -c "FALSE" skills/redteaming/references/fix-application.md` prints a number above 0.
4. `git grep -n -e "verifier-verdict-repair-path" -e "weakened-test-justification" -- ':!docs/crucible'` prints nothing.
5. `grep -nE "^- 2026-11-0[34]: .*(FALSE|repair)" docs/decisions/fix-verification-and-merge.md` and `grep -nE "^- 2026-11-0[34]: .*assertion" docs/decisions/test-rules.md` each print the new Changes line.

## Out of scope

The terminal pass's repair path; the verifier's template and read scoping; the fix waves of the task loop and the branch review; the group's other rulings.
