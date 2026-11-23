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
- Features on real code have since run under it: the re-audit of
  2026-11-23 read 23 campaigns of one code project on crucible 0.33.1. One
  reached the cap, after its terminal pass flagged the stop basis and the
  operator ran a fourth round, which found 1 MAJOR and 4 MINORs. The pass
  flagged 4 of the 21 stop bases it read. No round ran past a valid stop,
  by inference: each round after the first followed a wave that changed a
  mechanism, a flagged stop or the operator's word.
  Whether any stop was overturned after code was not determined: the
  post-close amendments in 13 of those features' ledgers were not
  classified.

## Follow-up

On a sample of coming campaigns on real code, run one extra fresh-panel
round past a valid stop, about 1.5 to 3 million input-equivalent tokens per
campaign at recorded round costs, and define "routine" at-cap escalation
before escalations are counted again. Classifying post-close amendments
would show stops overturned after code where they were written back.
