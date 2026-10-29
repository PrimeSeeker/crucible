# Redteam campaigns: the worth of later rounds, drift, and the cap

## Observation

- Drift looks like a general problem of working with agents. On one
  project, 60–90% of the findings in campaign rounds 2 and later were
  introduced by the previous round's fix waves.
- Large specs there still drew BLOCKERs and double-digit MAJOR counts at
  rounds 4–5, and the Decisions sections of four large specs grew 2.8–4.7×
  over their campaigns.
- On the same project a small change run through the full process (spec,
  campaign, per-task review, branch review) cost about 36M
  input-equivalent tokens, 23% of it implementation. A direct-fix session
  with no spec and an iterated branch review landed five fixes for about
  10.6M, and its scoped re-review caught a MAJOR the first fix had left
  open. That shows the branch-review loop catching a real defect on a
  small change; it says nothing about what a spec round would have caught.
- A recount of past campaign records (2026-10-12) supported neither
  raising nor lowering the cap of four rounds: no fresh-panel round past a
  valid stop is on record, so stopping later is as untested as stopping
  earlier. At least 7 of 75 stop calls were overturned, reopened or
  flagged `CONCLUSION-CHANGING`.
- On crucible's own umbrella-specs feature (2026-10-28), four spec
  rounds, a terminal pass and its second read mostly fixed wording,
  much of it drift from earlier rounds' fixes, and missed the one
  structural gap (a rule triggered at task or round boundaries that two
  phases never reach). An implementer and the branch review found it,
  and one fix wave closed it.
- Since 2026-10-29 a spec campaign stops once overturning a major
  mechanism after code is no longer plausible, each seat forecasting the
  answer and the terminal pass checking the stop against the forecasts
  (`docs/decisions/spec-campaign.md`). The trigger is a hypothesis with
  no demonstrated accuracy: three stops under it, all on prose changes to
  crucible's skills, with no counterfactual. The cap of four stays.

## Follow-up

Research questions:

- Is a multi-round spec campaign net-positive against one round plus
  execution-time review? Compare the two on session transcripts already
  on disk, the campaigns stopped by the overturn question included.
- Fix altitude and deferral as drift reducers.
- What would settle the cap: one extra fresh-panel round past a valid
  stop on a sample of campaigns, and a definition of "routine" at-cap
  escalation before escalations are counted again.
