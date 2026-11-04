Lane: very-small (operator-confirmed 2026-11-05)

# A full-scope pass after a wave that changes no rule

## Intent

A full-scope pass after every fix wave costs what the whole branch costs, even when the wave only rewords text that a clean pass has already read. Skip that pass when the wave took no blocker or major and changes no rule or behavior, as judged independently. A wave that adds or changes a rule keeps its pass, because a few-sentence wave of that kind produced a major its scoped re-review could not see. No break.

## Change list

- `skills/requesting-code-review/SKILL.md`, loop step 3: also skip the pass where the wave took no BLOCKER or MAJOR and its re-review's `Rule or behavior change` line reads none, and append `full pass skipped` to the wave's ledger line. The cleanup-wave paragraph defers to step 3.
- `skills/subagent-driven-development/re-review-prompt.source.md`, Verdict (then regenerate): in a branch-review wave, add `**Rule or behavior change:** [None | what the fix diff adds or changes]`. None means a reader or the code must do the same as before: wording, a citation, or a statement brought in line with a rule already in force.
- `skills/subagent-driven-development/references/finish.md`: the close readout names each skipped pass with the re-review's line.
- `docs/decisions/branch-review.md`: The loop in Decision, a Why section with the evidence and its limit, a Rejected entry for counting size, and a Changes line.
- Prose budget raised; `docs/backlog/small-wave-full-pass.md` deleted.

## Acceptance

- A throwaway check script confirms each change above is present and the backlog item is gone. It fails on the pre-change tree on every item (run once).
- `python tools/instrument_agents.py check` exits 0.
- `python -m pytest tests/` is green.

## Out of scope

Task-loop fix waves, redteam campaigns and their terminal pass, standalone mode, the first full-scope pass (every branch still gets one), the wave cap, and any test based on file, line or task counts.
