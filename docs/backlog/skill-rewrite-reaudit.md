# Re-audit the mechanisms after the retirement children, and recalibrate

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
- The recorded runs cannot check either yet. Since 0.13.0 (2026-11-02)
  about 20 features have run, all on crucible's own repository in one
  session. Only `placement` and `compaction-fit` used a campaign or the
  task loop, where most retired mechanisms lived, and no other project has
  run a feature on those versions. On the controller's proposal, the
  maintainer held the audit until a few features on real code have run
  (2026-11-05).
- What those runs could show is recorded: the token figures and the first
  count of compaction re-reads in `docs/decisions/authoring-crucible.md`,
  and the verifier's eight runs in
  `docs/decisions/fix-verification-and-merge.md`.

- Crucible's calibrations (four or five seats in a large new spec's first
  round, the cap of four rounds, plan sizes) come from one project, and
  were meant to be re-derived before reuse elsewhere; the README says where
  they come from. The maintainer's estimate is that redteaming works, while
  the specific parameters are unclear. A/B runs on properly large tasks are
  too expensive: one run can burn about 5% of a weekly usage limit. The
  outcome review found no detectable difference
  (`docs/decisions/publication.md`), and a recount of campaign records left
  the cap unchanged (`campaign-early-stop-investigation.md`).

## Follow-up

Once a few features on real code have run on 0.13.0 or later, repeat the
audit on those runs with `audit-brief.md`, against `inventory.md` (both
beside the umbrella): did a retired mechanism's failure reach a later stage
or the operator, and does the verifier earn its keep. Report aggregate
figures only for any other project. Judge a session by its events'
timestamps: a file's date can be recent on an old run.

In the same transcripts, look for controllers re-reading a moved step's
reference after compaction before acting on that step.

In the same runs, count findings that fail their re-review on successive waves. A stuck trigger was declined on evidence with little real code under the current rules (`docs/decisions/model-roles-and-effort.md` § Why), and repeats there reopen it.

From the same runs, read seat counts, rounds and plan sizes against the
calibrations and re-derive what they support, labelling results from one
project as one project's. A second project is better evidence, not a
condition.
