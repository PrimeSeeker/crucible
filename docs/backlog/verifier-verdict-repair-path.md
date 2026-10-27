# No repair path for a FALSE delta claim, or for a not-landed item in the spec campaign

## Observation

- After every spec-campaign fix wave the blind verifier reports a verdict
  per fix item (landed, not landed or partly landed) and per delta claim
  (TRUE or FALSE with evidence, or not checked with the reason;
  `skills/redteaming/verifier-prompt.md`). The controller checks each
  claim reported not checked itself and records the outcome in the round
  record's verifier block (`skills/redteaming/SKILL.md` § Fix application
  and blind verification).
- Neither the skill nor `skills/redteaming/references/formats.md` says
  what happens next to an item the verifier found not landed, or to a
  delta claim found FALSE, in the spec campaign. The plan phase has a
  sanctioned path for a not-landed item only: one scoped repair edit and
  a re-check of that item only (`skills/redteaming/references/plan-phase.md`,
  the two repair paths; the other is for terminal-pass findings). Neither
  phase has a path for a FALSE delta claim.
- A route for FALSE delta claims was once drafted in a spec campaign and
  reshaped over two rounds; the third round removed it, because it named a
  spec-campaign repair path that does not exist.
- A recount of past campaign records found 29 units with a defect the
  verifier flagged and the wave left in place; in at least 7 of them the
  process of the time handed the note to the terminal pass on purpose.
  Whether later verifiers' unchecked delta claims were then checked is not
  recorded.

## Follow-up

- Decide what happens to a not-landed item in the spec campaign and to a
  FALSE delta claim in either phase: a repair inside its wave (as the plan
  phase's scoped repair does for a not-landed item), the next round's fix
  list, or the next round's panel (the plan phase has no next round).
  State it once, in the skill.
- Record the repair's outcome in the verifier block, beside the
  controller's check of a claim not checked.
