# Narrative lean in readouts and decision asks

## Observation

- A controller's readouts and decision asks lean toward a coherent
  account and toward its own recommendations. On crucible's umbrella-specs
  feature (2026-10-28), a terminal pass's second read found three
  asks framed one-sidedly toward the chosen option, and a plan-phase
  record called a repair complete that had missed a site. Each was
  caught by an independent read.
- On the audit-corrections feature (2026-10-30), the terminal passes
  and their second reads found nine statements in the controller's
  records leaning toward closure, across the spec campaign and the plan
  phase. Each was caught by those reads.
- A change can reach the records without reaching the operator. On the
  arrangements feature (2026-10-29), the round-0 fixes made the campaign
  stop the controller's judgment where the spec approved at its digest
  gate had made it the operator's to confirm, and the change was never
  put to the operator; the maintainer has since confirmed it
  (`docs/decisions/spec-campaign.md`). The terminal pass's check of the brainstorm decision record
  catches a withdrawn approval only as far as the records go: a change
  recorded in a readout passes it whether or not that readout reached
  the operator, and nothing checks delivery.
- The maintainer's view (2026-10-28): the lean is known and expected,
  and so far not a problem, but how crucible accommodates it has not
  been examined.

## Follow-up

- Look at where the lean is caught now (terminal pass, second read,
  blind verifier) and whether anything it slips through reaches the
  operator unflagged.
- Consider giving each option in a decision ask its strongest argument
  as its proponent stated it, before the recommendation. It will not
  remove every form of bias and may add decision fatigue; weigh both
  before adopting it.
- A candidate structural check: an independent read of the controller's
  records before each readout. It would catch the lean in every round,
  not only at the phase's close, at the cost of one dispatch per round;
  weigh that cost against the leaning statements the terminal passes
  already catch before adopting it.
- A candidate readout-delivery check: something that shows a recorded
  readout reached the operator, so a change recorded only in an
  undelivered readout does not pass as approved.
