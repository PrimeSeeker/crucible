# Recalibrate seat counts, the round cap and plan sizes

## Observation

- Crucible's calibrations (four or five seats in a large new spec's first
  round, the cap of four rounds, plan sizes) come from one project, and
  were meant to be re-derived before reuse elsewhere. The README says
  where they come from.
- The maintainer's estimate is that redteaming works, while the specific
  parameters are unclear. A/B runs on properly large tasks are too
  expensive: one run can burn about 5% of a weekly usage limit.
- A retrospective outcome review of that project's git history, its
  method fixed before the data was read, compared escaped defects
  (post-merge fixes and reverts touching a feature's files) before and
  after crucible: no detectable difference. The per-line ratio was 0.10
  at one setting of the method's parameter (G = 3) but unstable at
  another (G = 7); per commit, with uncertain items counted against
  crucible, it reversed (1.75); classifiers called about the same share
  of later edits repairs in both periods (29% and 31%). The README's comparisons stay
  labelled as impressions.
- A recount of campaign records left the cap and the stop trigger
  unchanged, the evidence inconclusive
  (`campaign-early-stop-investigation.md`).

## Follow-up

Decide how and when the seat counts, the cap and plan sizes are
recalibrated: a trigger, and the evidence it reads, preferably from more
than one project.
