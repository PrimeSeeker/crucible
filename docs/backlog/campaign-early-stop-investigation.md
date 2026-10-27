# Investigate stopping redteam campaigns earlier (fix-wave drift)

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
- A recount of past campaign records supports neither raising nor
  lowering the cap of four rounds, nor tightening or loosening the stop
  trigger: no fresh-panel round past a valid stop trigger is on record, so
  stopping later is as untested as stopping earlier. At least 7 of 75 stop
  calls were overturned, reopened or flagged `CONCLUSION-CHANGING`. The cap
  and the trigger stay, and a numbered spec-campaign round with no BLOCKER
  states in its readout whether it drove structural change and on what
  basis.

## Follow-up

Research questions:

- Is a multi-round spec campaign net-positive against one round plus
  execution-time review? Compare the two on session transcripts already
  on disk.
- Stop when the share of a round's findings introduced by the previous
  fix waves passes a threshold?
- Fix altitude and deferral as drift reducers.
- What would settle the cap and the trigger: one extra fresh-panel round
  past a valid stop trigger on a sample of campaigns, and a definition of
  "routine" at-cap escalation before escalations are counted again.
