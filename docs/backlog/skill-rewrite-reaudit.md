# Re-audit the mechanisms after the retirement children

## Observation

- The skill text rewrite (`docs/crucible/2026-11-01-skill-text-rewrite/umbrella.md`)
  retires and simplifies mechanisms on an audit of recorded runs whose
  limits it states: counts are lower bounds, whether a later stage
  would have caught a finding is the readers' judgment, and the newest
  mechanisms ran only on crucible's own text.
- Its D2 retires a mechanism outright only where the failure it targets
  would be loud, so a regression should show; nothing yet checks that
  it did.
- The blind verifier was kept for now on uncertain evidence (D5).
- Resident tokens per route were counted at the rewrite's start, before
  `compaction-fit` and after it, as a baseline
  (`docs/decisions/authoring-crucible.md` § Why, Resident tokens per
  route; manifests and script in
  `docs/crucible/2026-11-03-compaction-fit/`).
- `compaction-fit` moved long step bodies of three skills into
  references read at their step. After compaction the host re-attaches
  the skill, not those references: a controller reaches a moved step's
  text only by re-reading its reference, as each skill's statement of
  what a stub means tells it to, and whether controllers do is
  unmeasured.

## Follow-up

After `review-retirements` and `execution-retirements` have run on a
few features, repeat the audit on the new runs with
`audit-brief.md`, against `inventory.md` (both beside the umbrella):
did a retired mechanism's failure reach a later stage or the operator,
and does the verifier earn its keep. Report aggregate figures only for
any other project.

With it:

- re-count the resident-token manifests
  (`docs/crucible/2026-11-03-compaction-fit/resident-tokens.json`, with
  `resident_tokens.py` beside it) at the head of the day, against the
  baseline in the decision record;
- in the new runs' transcripts, look for controllers re-reading a moved
  step's reference after compaction before acting on that step.
