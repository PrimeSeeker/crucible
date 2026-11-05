# Redteam campaigns: what would settle the cap

## Observation

- A recount of past campaign records (2026-10-12) supported neither
  raising nor lowering the cap of four rounds: no fresh-panel round past a
  valid stop is on record, so stopping later is as untested as stopping
  earlier. At least 7 of 75 stop calls were overturned, reopened or
  flagged `CONCLUSION-CHANGING`.
- A read of the transcripts on disk (2026-11-06) did not show multi-round
  campaigns paying for themselves and could not settle the cap
  (`docs/decisions/spec-campaign.md` § Why). None of the feature work on
  real code it read ran under the overturn question.

## Follow-up

Once features on real code have run under the current stop rule, run one
extra fresh-panel round past a valid stop on a sample of campaigns, about
1.5 to 3 million input-equivalent tokens per campaign at recorded round
costs, and define "routine" at-cap escalation before escalations are
counted again.
