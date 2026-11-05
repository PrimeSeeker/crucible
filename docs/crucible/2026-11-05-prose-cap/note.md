Lane: very-small (operator-confirmed 2026-11-05)

## Intent

Skill text regrows after every rewrite, and nothing refuses it, because a commit raises its own per-skill budget. Add one limit the author can't raise: a total word cap, set 10% over the compaction baseline. Reaching it puts the choice to the operator: compact or raise. Also make excess text a review finding on this repository, since that rule now reaches only readers of `writing-skills`. No break.

## Change list

- `tests/test_prose_budget.py`: add the cap of 47,387 and a test that the skills' total stays at or under it, its failure message telling the agent not to raise the number and to stop and ask the operator whether to compact or raise it.
- `AGENTS.md`, the prose budget entry: the cap moves only on the operator's ruling, quoted in the commit body, and the branch reviewer checks this; a compaction's landing asks for the new number. Add one sentence: a review of text agents read counts excess as a finding (`crucible:writing-skills § Reader cost`).
- `docs/decisions/authoring-crucible.md`: record the cap and why (total words tracked the route load, +5.3% against +4.6-5.0%, with no route list to keep current); replace "no replacement" in the retired trigger's passage; fix both pointers to the backlog item; add a Changes line.
- Delete `docs/backlog/prose-creep-containment.md`, now resolved.

## Acceptance

- The full suite passes, and the new test passes at 45,382 words.
- With the cap temporarily set to 45,381, that test fails and its message names both choices; restoring the cap passes.
- The backlog item is gone and no decision record points to it.
- `AGENTS.md` names the cap and the excess rule.

## Out of scope

Per-route counts, per-spec allowances, periodic re-derivation, any shipped skill text, and lowering the text now.
