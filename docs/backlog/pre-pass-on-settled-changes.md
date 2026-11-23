# The round-0 pre-pass on settled changes

## Observation

- Every spec campaign opens with a round-0 pre-pass: one agent checks the
  artifact's claims about code, the liveness of its mechanisms and its
  regex and CLI claims before any panel reads it
  (`crucible:redteaming § Round 0 — mechanical pre-pass`;
  `docs/decisions/spec-campaign.md`).
- A read of five campaigns on settled changes, all on the folded preset
  (one code project, crucible 0.33.1, 2026-11-23;
  `docs/decisions/routes.md` § Separable choices), judged who would have
  met each of the pre-pass's 17 BLOCKER or MAJOR findings without it. The
  implementer would have met 12, by a failing test, a type check or the
  file its task edits; the task reviewer 1; the branch reviewer,
  plausibly, 3; 1 was undetermined, and none would have been built in
  silently. 10 of the 17 were defects in the folded plan's tasks, mostly
  their reach: file lists, censuses, contract checks and overlaps.
- The five pre-passes took 373 thousand of those campaigns' 1.39 million
  seat output tokens. In three of the features implementers added files
  their task's census had missed, by themselves.
- What the pre-pass's corrections saved the panel that read the artifact
  next was not measured. In one campaign a pre-pass fix was itself wrong,
  and round 1 caught it.
- The five were selected because each stopped after one round, and every
  verdict is one reader's judgment of what did not happen.

## Follow-up

Ask the same of campaigns not selected this way, standard-route ones
included: who would have met each pre-pass finding without it, and whether
a panel spends less on an artifact the pre-pass has corrected. Until then
round 0 stays as it is: one read of five settled changes is no ground to
change a step every campaign runs.
