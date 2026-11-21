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

In the same runs, count findings that fail their re-review on successive
waves, and decide whether a stuck trigger is wanted. The transcripts read
so far point both ways, with little real code under the current rules
(`docs/decisions/model-roles-and-effort.md` § Why).

In the same runs, read whether fresh looks fired where they should and whether
the ones adopted helped (`docs/decisions/model-roles-and-effort.md` § A fresh
look).

From the same runs, read seat counts, rounds and plan sizes against the
calibrations and re-derive what they support, labelling results from one
project as one project's. A second project is better evidence, not a
condition. Check too whether any one-round campaign was a settled change run
only to get a plan, the trigger that reopens a lane note with a plan
(`docs/decisions/routes.md` § Separable choices).

In the same runs, read how the around-the-diff rule did on real code
(`docs/decisions/task-loop.md` § Around the diff): were fold-ins worth having,
did one bring a defect, and what happened on the cases its wording test did
not reach: a callee with several callers, a fold-in larger than a loop merge,
the fix-wave sentence, prose and no-seam work, the design-stage sentence, the
inline paths, a reviewer on the shipped wording, and the bounded role.

In the same runs, read what the lean-gates narrowing did
(`docs/decisions/operator-steering.md`, `docs/decisions/branch-review.md`,
`docs/decisions/adjudication.md`, `docs/decisions/terminal-pass.md`). Five
things, each against what a read of sixteen sessions of one code project
found before it:

- the share of decisions put to the operator that are housekeeping, against
  about 30% in that read;
- later full-scope passes per first pass, against about 1.1 in that read;
- any BLOCKER or MAJOR a later pass raised, and whether the first pass
  missed it or a wave introduced it;
- any choice the operator said they should have been asked, which the test
  for a choice no skill puts to them withheld;
- any controller ruling on a literal-reading finding that a later pass or
  the operator reversed.

One figure on the terminal pass's record check comes from before lean-gates,
on one folded-lane feature of a code project: a terminal pass and its
second read reported seven record corrections and no artifact finding, two
default-role runs for a feature of about a hundred lines of code.

Such a read shows what the remaining passes caught and what the operator
objected to. It cannot show a defect that a pass not run would have caught,
what the narrowed steps cost, or what every pass missed: the earlier counts
have no ground truth behind them, and the figures are approximate. Report
aggregate figures only for any project, as above.

In the same runs, read what the path for a late ruling and the recorded
readout did (the last paragraph and the list of
`skills/redteaming/references/round-readout.md`;
`docs/decisions/fix-verification-and-merge.md`,
`docs/decisions/spec-campaign.md`, `docs/decisions/terminal-pass.md`). Four
things, each against what was observed before them:

- whether a ruling arriving after a spec campaign's last numbered round's
  fix list froze went by that path, what its rulings list's verifier found,
  and whether the list raised an ask of its own; before it, three campaigns
  met such a ruling and their controllers did three different things, and
  in about 20 campaigns of one code project at least 2 of 11 fix passes
  around the terminal pass carried a ruling, a lower bound;
- whether recorded readouts match the messages delivered; before it, in two
  runs the controller recorded a shortened readout and delivered a fuller
  one. Only a read of transcripts can show this: no seat reads the
  operator's messages;
- whether a plan phase met a ruling between its readout and its terminal
  pass, which has no stated path; none is known, the three known cases being
  spec campaigns;
- how often a ruling arrived after the terminal pass was dispatched, the case
  the rule sends to the campaign's close, and how long the terminal pass's
  wait for the operator's answers held, so the trade-off accepted over never
  waiting gets a figure; no figure exists from before, neither was observed.

In the same runs, read what process notes did
(`docs/decisions/operator-steering.md` § Process notes): whether controllers
made notes as the work went and offered them in a line when it ended, what
the notes held and which causes they named, whether a seat's remark reached
them as the seat wrote it, and whether an operator took the offer. Before
them, a keyword search of 18 sessions over two weeks found one operator
request for a process report, and nothing measured whether anything had been
volunteered.
