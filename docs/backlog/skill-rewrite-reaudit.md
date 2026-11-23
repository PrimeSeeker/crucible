# Re-audit the changes since 0.33.1 on real code, and recalibrate

## Observation

- The re-audit the skill text rewrite owed ran on 2026-11-23, over 36
  features of one code project on crucible 0.33.1. Its results are in the
  records that hold each question, its scope and limits in
  `docs/decisions/fix-verification-and-merge.md` § Blind verification: the
  verifier stays, the stuck trigger is closed, a lane note with a plan met
  its reopening condition, and the figures of the read of 2026-11-19, whose
  script counted from a seat index holding 640 of 880 seats, are corrected
  where recounted.
- No run on 0.34 or later existed then, so nothing measured the changes
  made since. That project's first sessions on 0.38.0-rc.1 have begun.
- The read did not examine the waves' line counts the readout trace lost,
  the load-bearing marks, or the containment test's exclusions; snapshot
  blessing never fired.
- What the read saw and nobody has ruled on:
  - four of six fresh looks fired at a passage's third patch, where the
    router's sign is the second
    (`docs/decisions/model-roles-and-effort.md` § A fresh look);
  - three landings had no full-scope read after their last change, each on
    the operator's word or a call left to the controller, one of them
    landing six hand-merged rebase conflicts no reviewer read;
  - in one session whole features ran after a compaction with no skill
    invoked again, the controller twice announcing a skill without
    invoking it, working from the re-attached copies and the references it
    read;
  - one plan task, by its own Contract, ran as 22 seats the controller
    composed, outside the implementer and the task review.
- Crucible's calibrations (four or five seats in a large new spec's first
  round, the cap of four rounds, plan sizes) come from one project, and
  were meant to be re-derived before reuse elsewhere; the README says where
  they come from. The maintainer's estimate is that redteaming works, while
  the specific parameters are unclear. A/B runs on properly large tasks are
  too expensive: one run can burn about 5% of a weekly usage limit. The
  outcome review found no detectable difference
  (`docs/decisions/publication.md`), and a recount of campaign records left
  the cap unchanged (`campaign-early-stop-investigation.md`). The re-audit's
  campaigns, on the same project, seated two seats in round 1 in 10 of 23
  and four or five in 10, ran one to four rounds, one reaching the cap, and
  planned 3 to 14 tasks: what controllers chose, not what serves.

## Follow-up

Once a few features of real code have run on 0.38 or later, read their
transcripts for the threads below. Count seats from the transcripts
themselves: the index behind the read of 2026-11-19 took dispatches from an
event that repeats them without a timestamp and lost the originals. Report
aggregate figures only for any project, and judge a session by its events'
timestamps: a file's date can be recent on an old run.

Read what the lean-gates narrowing did
(`docs/decisions/operator-steering.md`, `docs/decisions/branch-review.md`,
`docs/decisions/adjudication.md`, `docs/decisions/terminal-pass.md`). Five
things, each against what the runs on 0.33.1 showed before it:

- the share of decisions put to the operator that are housekeeping: about
  30% by the reader seats of 2026-11-19, about half by the re-audit's hand
  check of 30 items, two classifications;
- later full-scope passes per first pass: 51 per 34, about 1.5;
- any BLOCKER or MAJOR a later pass raised, and whether the first pass
  missed it or a wave introduced it: 3 in 51 later passes, none introduced
  by a wave;
- any choice the operator said they should have been asked, which the test
  for a choice no skill puts to them withheld;
- any controller ruling on a literal-reading finding that a later pass or
  the operator reversed: no adjudicator's ruling of 24 was reversed.

On the terminal pass's record check, before lean-gates, 20 of 22 spec first
passes reported a record correction, 63 in all.

Such a read shows what the remaining passes caught and what the operator
objected to. It cannot show a defect that a pass not run would have caught,
what the narrowed steps cost, or what every pass missed: the earlier counts
have no ground truth behind them, and the figures are approximate.

Read what the path for a late ruling and the recorded readout did (the last
paragraph and the list of `skills/redteaming/references/round-readout.md`;
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

Read what process notes did (`docs/decisions/operator-steering.md`
§ Process notes): whether controllers made notes as the work went and
offered them in a line when it ended, whether that line named what deserved
attention and whether the operator agreed with the choice (since 2026-11-23
it no longer gives a count), whether expected but large costs came back
into the line as "material" (a branch reviewer asked; the maintainer reads
the word as beyond what the work was expected to cost, and left the
wording), what the notes held and which causes they named, whether a seat's
remark reached them as the seat wrote it, whether seats reported the host's
advice on report files as something off (two did on the build of process
notes; none of nine probe seats did, with or without the rule's reason; the
maintainer expects none to, now that the rule gives its reason), and
whether an operator took the offer. Before them, a keyword search of 18
sessions over two weeks found one operator request for a process report,
and nothing measured whether anything had been volunteered.

Read what the changes of 2026-11-23 did
(`docs/decisions/branch-review.md` § Record corrections;
`docs/decisions/routes.md` § The very-small lane): how many record
corrections controllers made after a review ended, and whether a later
read found one wrong or reaching a document that binds work; whether a lane
note written without being shown departed from the design the operator
approved, and whether a branch reviewer's goal check found it; whether a
reviewer who found a note excluding something asked for raised it as a
premise finding, which the lane passage's "mismatch" implies and the
definition in `skills/redteaming/references/premise-asks.md` does not name
(a branch reviewer asked; either route reaches the operator); and whether a
prose change on the lane landed with an outcome its Intent stated and its
text did not carry. Nothing was measured before them: they rest on a
controller's notes on three features.

Compare the routes on branches that are prose only. Two such features of
similar size were built back to back on crucible itself: the folded route
took 27 seat runs, the very-small lane 6, and none of the lane's three
full-scope reads raised a BLOCKER or MAJOR. One pair settles nothing, and
the folded feature changed review mechanics across routes while the lane's
replaced no mechanism. Read what the folded feature's spec campaign found
that a branch review would have missed, and whether the overturn question
(`skills/subagent-driven-development/references/review-terms.md` § The
arrangement questions), which asks how likely an overturn is, should also
weigh what one costs where the branch is text.

From the same runs, read seat counts, rounds and plan sizes against the
calibrations and re-derive what they support, labelling results from one
project as one project's. A second project is better evidence, not a
condition. Where the retirements the read did not examine come up, read
whether their failure reached a later stage or the operator.

For each settled change campaigned only to get tasks, read whether the
MAJORs its first round merged were of a kind the branch review catches.
That decides whether a lane note with a plan is built
(`docs/decisions/routes.md` § Separable choices): 5 of the 8 one-round
campaigns of the runs on 0.33.1 were such changes and still merged 2 to 4
MAJORs each.
