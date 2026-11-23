# Terminal pass

## Decision

Every spec campaign closes with the terminal pass, one fresh seat outside
the cap; the plan phase closes with its own after its fix wave. It has
two mandates, in this order: a re-read of the artifact, recorded before
it opens any record, then decision-ask fidelity, checking each ask
against the findings behind it and, in a spec campaign, the stop: the
stated basis against every forecast line in the numbered rounds' seat
verdicts, each forecast overturn answered by the mechanism it names,
and the stop round's fix list and any rulings list against the rule that a round whose wave
re-shapes a major mechanism is no stop round
(`docs/decisions/spec-campaign.md`). For that check its inputs gain
every numbered round's seat reports, their verdict sections only.
Decision-ask fidelity also checks, in both phases, that each question a
round record carries to readout is quoted verbatim in that readout,
reading it in its seat report's `Questions`, after a plain statement
that keeps its meaning, and that a call the
operator left to the controller is entered as delegated, never as the
operator's ruling or choice; and, in a spec campaign, each `accepted`
or `firm` entry of the brainstorm decision record whose decision the
artifact states, process entries such as the route and the campaign
shape aside: the decision still holds in the artifact, or a later entry
or a round readout naming the change and what it withdraws records its
change, an approval withdrawn with no such record being flagged
`CONCLUSION-CHANGING`. The record reaches it through its card's
`{decision-record-path}` slot, the spec phase's brainstorm decision
record and `none` in the plan phase. Its template takes by splice the
overturn question, from
`skills/subagent-driven-development/references/review-terms.md`, and
§ Premise findings, § Binding items and unrecorded choices and
§ Location, from the shared seat reference, so its findings
carry a location as every finding does
(`docs/decisions/instruments.md`;
`docs/decisions/evidence-and-findings.md`). It reports counted record
corrections of three kinds only (§ What the pass reports), expecting
the records to lean toward the controller's own recommendation. A
correction, or a mismatch in its Notes, flagged `CONCLUSION-CHANGING`
reaches the operator as a decision ask, and so does its one line on a
record it finds materially misleading as a whole, which sits outside the
count. Its tail is bounded: in the spec campaign one further fix wave,
taking what any fix list takes (`docs/decisions/fix-verification-and-merge.md`), in
the plan phase one scoped repair, and one second read. The second read
follows that wave or repair, its dispatch saying whether a re-read is
due (the card's `{re-read}` slot), and runs record-only after a pass whose
report carries a record correction or its line on a misleading record,
or on which the controller puts a decision ask again: it reads the close
the controller recorded after the pass against the pass's report and the seat findings behind each ask,
and the controller delivers that close after it, its corrections recorded first.
One read covers both cases. Of what it leaves open, a MINOR not against
binding text takes `deferred-minor`, which the spec terminal-pass record
and the plan record's `## Terminal pass` list; the rest goes to the
operator. The mandates, inputs and flag test are stated in full only in
`skills/redteaming/terminal-pass-prompt.md`
(`crucible:redteaming § Stop rule and terminal pass`).

## Why

### Why a pass at all

A campaign that stopped on a fix wave would otherwise converge on edits
no seat had read: the pass is the review of the last wave (crucible's
first design, 2026-08-06; judgment, accepted by the maintainer). It
earns its place: in a recount of the campaign records (2026-10-12), the
pass's first read found a BLOCKER or MAJOR after the stop call in 27 of
74 campaigns. (Basis: measured.) In the re-audit of 2026-11-23 (its scope
and limits in `docs/decisions/fix-verification-and-merge.md` § Blind
verification), the first read found something in the artifact in 13 of 22
spec first passes, one MAJOR and 23 MINORs, and one MAJOR in 7 plan
passes. (Basis: measured.)

### Fidelity of the asks

The operator steers through decision asks without reading the artifact
(`docs/decisions/operator-steering.md`), and the controller writes every
ask, so without a check it alone decides what the operator learns. On
2026-08-07 that check went into the terminal pass, at no added seat,
rather than into a fidelity seat each round, on cost. (Basis: judgment,
accepted by the maintainer.)

On 2026-10-07 the mandate narrowed to the asks: its other checks were
mechanical or low in yield, sampled fidelity catches being mostly
defects the re-read had found, a stop-rule call whose only effect was
another round, or ask wording with the recommendation unchanged, and
keeping the independent check where the operator decides was the
maintainer's choice. With one check
left, escalating every correction would have made each wording fix an
ask, so only `CONCLUSION-CHANGING` corrections escalate. (Basis:
measured, for the samples; the maintainer's preference, for where the
check sits; judgment, accepted by the maintainer, for the escalation.)

The stop came back into the mandate on 2026-10-29, as part of
decision-ask fidelity, when the stop trigger became the overturn
question. A stop-rule call then mattered little, since a wrong one only
cost another round; under the new trigger a stop is what ends review
before code, and a probe of the campaigns that stopped by the question
found the controller making each call and writing the readout that
justified it, one stop basis overstated. The seats' forecast lines give
the check a record the controller did not write. It reads only their
verdict sections, so whole seat reports stay outside its inputs.
(Basis: measured, for the probe; judgment, accepted by the maintainer,
for the check.)

The audit of the hypothesis-specs umbrella
(`docs/decisions/evidence-and-findings.md`) found the maintainer's
approvals in no reviewer's inputs, in 4 of its 10 clusters of missed
findings. Two approvals had been withdrawn without the change reaching
the maintainer: the very-small lane's inline test
(`docs/decisions/task-loop.md`) and the campaign stop's form
(`docs/decisions/spec-campaign.md`). From 2026-10-30 the spec
campaign's pass reads the brainstorm decision record and checks each
approval the artifact states against the artifact and the records of
its change. It would have caught the first, and the second as far as
the records go: a change recorded in a readout passes whether or not
that readout reached the maintainer, and nothing checks delivery
(`docs/decisions/operator-steering.md`). The same audit found doubts
stopping at the controller, so the pass also checks that each carried
question reaches the readout in its seat's words, reading those
questions alone of the seat reports, and that a call left to the
controller is not recorded as the maintainer's ruling. A stop called
while a premise ask holding it was pending entered the stop check with
that hold, and left it when the hold was retired on 2026-11-02
(`docs/decisions/spec-campaign.md`). Each check adds a little work to
every feature's terminal pass, which word counts do not show. Agents'
proposals, which the maintainer accepted. (Basis: measured, for the
audit's findings; judgment, accepted by the maintainer, for the
checks.)

From 2026-11-20 a readout states each carried question in plain words
before quoting it (`docs/decisions/evidence-and-findings.md`), and the
pass reads that statement against the quote: one that softens or
otherwise changes the question is a question changed in meaning, so the
controller's account does not stand in for the seat's words beside it.
The check reaches what the quote check reaches, the numbered rounds'
questions and not round 0's. (Basis: judgment, the controller's calls in
the spec campaign: the check, with the mark's withdrawal, on an ask the
maintainer left to it; its reach, the controller's own.)

The re-read comes first because reading the records' account of the
artifact before the artifact turns a confirming read into a re-derivation
of someone else's conclusion (2026-08-16). Counted corrections replaced
a pass or fail verdict on the record the same day, a binary verdict
inviting rumination over the record's author rather than a correction of
the record. (Basis: judgment, accepted by the maintainer.)

### What the pass reports

Each fidelity check and the materiality flag judge one item at a time:
a set of individually immaterial corrections all leaning one way passes
every one of them. The operating stance makes errors cheap to disclose
and names shading a record as the one reportable failure of the
reporting duty (`docs/decisions/spec-campaign.md`). A directional-bias
statement over the pass's corrections came to report it, after one pass
reading its corrections together had observed that both
"point the same direction: toward the self-correction narrative"
(2026-08-15). Its escalation got a threshold on 2026-08-21, because the
ask below it had fired in nearly every campaign and never changed
anything; a standing-stance line written into the closing record below
the threshold went on 2026-10-13, its reader the committed record trail
crucible no longer keeps; and on 2026-11-02 the statement folded to one
bias line, a decision ask
only on a materially misleading record, since nothing else escalates
that and its failure would be silent. (Basis: judgment, accepted by the
maintainer; a single incident, for the observation; the controller's,
on a call the maintainer delegated, for the kept trigger.)

A read of sixteen sessions of one code project on crucible 0.33.x,
twelve days of work, found the pass's record corrections recurring in
nearly every campaign, leaning toward the controller's own
recommendation and not becoming rarer over the twelve days. Its script
counted from a seat index holding 640 of the window's 880 seats, so its
counts of dispatches and of corrections that changed anything give way
to the re-audit's (§ Why a pass at all), which counted every seat. There
20 of 22 spec first passes reported a record correction, 63 in all, and
15 of the 20 said their corrections leaned toward the controller's
recommendation, toward settled or done, or toward the operator's
endorsement. Spec first passes and second reads flagged 25 corrections
`CONCLUSION-CHANGING`, a plan first pass at least one more, and in 5
of the 21 campaigns corrections visibly changed what happened next, by
an ask put again, a further round or the operator choosing an option the
controller had not recommended, each of the five carrying a flagged
one. Reporting every mismatch, and a line naming their shared direction,
had not reduced the lean. So from 2026-11-19 the pass expects the lean and
reports three kinds only. A `CONCLUSION-CHANGING` mismatch is kept, the
withdrawn approval among them. A decision whose record misstates who
made it or how firmly the operator holds it is kept, in either
direction, because a decision recorded as firm is shielded from
ordinary findings and one recorded as less is not. A question carried
to readout that is missing there or changed in meaning is kept, because
nothing else carries a seat's doubt past the controller. The same
filter covers the pass's Notes. The bias line gives way to one line
closing the corrections only where the pass finds the record materially
misleading as a whole, saying in what way and naming its entries: a
decision ask, as the bias line's statement of it was, for the reason
that trigger was kept. The controller's duty not to shade a record
stays; the pass reports a breach of it through those kinds and that
line, no longer as a pattern. The figures are approximate and cannot be
reproduced from this repository. (Basis: measured, for the figures; the
maintainer's proposal, for reporting only what would change a
conclusion and expecting the lean; the controller's, accepted by the
maintainer, for keeping the misattributed decision; the controller's
calls in the spec campaign, told to the maintainer in its round
readouts, for the third kind, the closing line and the either-direction
reading; the controller's calls in the spec campaign, for the filter
over Notes and the withdrawn approval's kept flag.)

### The tail

One campaign ran a re-pass and then appended six re-checks after it, so
the tail was bounded on 2026-09-27 to one fix wave and one second read
whose report is the last. A second read writes a new file rather than
appending, so the first report stays as written (2026-10-07). In the
plan phase the repaired text is itself unreviewed, which is why the
second read covers the whole repaired region, never the flagged item
alone. (Basis: a single incident, for the bound; judgment, accepted by
the maintainer, for the rest.)

The record-only run came with the skill text rewrite (2026-11-02). Its
audit found the second read catching new defects in most of the runs
read, among them MAJORs a repair had introduced and records leaning
toward the controller; run only after a wave, it never read the records
of a pass that corrected them without one. The follow-up wave narrowed
with every fix list (`docs/decisions/fix-verification-and-merge.md`).
(Basis: measured, for the catches; the controller's proposal, accepted
by the maintainer, for the record-only run.)

In the re-audit's runs (§ Why a pass at all), 26 second reads ran, 20 of
them spec second reads in seats of their own and 6 resuming a plan pass,
and none found a BLOCKER or MAJOR in its artifact; of the 25
`CONCLUSION-CHANGING` corrections counted above, 14 came from spec first
passes and 11 from second reads. The read of 2026-11-19, on its partial index, had found
the flagged ones coming from second reads of a close that put an ask
again. A narrowing of the record-only
run to an ask put again was approved with the design on 2026-11-19 and
withdrawn in its spec campaign: a correction the pass still reports is
one whose delivery matters, and nothing but the record-only read checks
that the close carries it. The triggers stay, the line on a misleading
record triggering the record-only run as a correction does, and fewer
second reads run because fewer corrections are reported. (Basis:
measured, for the figures; the controller's call in the spec campaign, withdrawing what the maintainer's approval of the
design carried, told to the maintainer in a round readout, for keeping
the triggers.) From 2026-11-20 the controller records the second read's
corrections in the close before delivering it, so the record the pass
checks is the close the operator received
(`docs/decisions/fix-verification-and-merge.md`).

## Rejected

- **A fidelity seat every round**: the same check at higher cost
  (§ Why).
- **Ruling-consistency, conservation-walk and whole-seat-report
  mandates for the pass**, removed on 2026-10-07 (§ Why); of the seat
  reports, the stop check reads the verdict sections and the fidelity
  check the questions carried to readout, and no more.
- **Escalating every correction**, or every directional-bias statement,
  to the operator (§ Why).
- **Reporting every mismatch**, and a line naming the direction the
  corrections share, removed on 2026-11-19 (§ Why).
- **Running the record-only second read only where an ask is put
  again**, approved with the design and withdrawn on 2026-11-19
  (§ Why).
- **A standing-stance line below the threshold** (§ Why).
- **A pass or fail verdict on the record** (§ Why).

## Changes

- 2026-11-23: the counts behind reporting three kinds only are the re-audit's, the read of 2026-11-19 having counted on a partial seat index: 20 of 22 spec first passes reported corrections, 15 of those leaning toward the controller, and corrections visibly changed what happened next in 5 of 21 campaigns, each carrying a flagged one; and the earlier statement that the flagged corrections came from second reads is corrected, 14 of the 25 counted having come from spec first passes. What the pass's first read found in those runs is recorded. No position changes.
- 2026-11-20: decision-ask fidelity also reads the plain statement a readout gives before each carried question's quote against the quote, one changing its meaning being a correction of the third kind, and the controller records the second read's corrections in the close before delivering it; because a readout now states carried questions in plain words beside the seat's own, and two controllers delivered readouts their records did not hold.
- 2026-11-20: the stop check reads the stop round's rulings list as it reads its fix list, since a ruling after the last numbered round now rides one as that round's own fix wave (`docs/decisions/fix-verification-and-merge.md`).
- 2026-11-19: the pass reports only corrections of three kinds, a `CONCLUSION-CHANGING` mismatch (a withdrawn approval among them), a decision whose record misstates who made it or how firmly the operator holds it, and a carried question missing from its readout or changed in meaning, its Notes filtered the same way, and its template tells it the lean toward the controller's recommendation is expected; the bias line gives way to one closing line, a decision ask outside the count, only where the record is materially misleading as a whole; the second read keeps its triggers, that line among them; because in a read of sixteen sessions of one code project the corrections recurred in nearly every campaign, leaned the same way and did not become rarer, and of about 24 readouts reporting them two visibly changed what happened next, and the flagged corrections it found came from second reads of a close that put an ask again; and nothing but the record-only read checks that the close carries a correction the pass still reports.
- 2026-11-05: the pass's read scoping admits the files a claim in the artifact cites, seat reports staying out, since its instruction to run a check needs them and two passes had read them anyway.
- 2026-11-03: the pass takes the overturn question from `skills/subagent-driven-development/references/review-terms.md`, where the arrangement questions moved from the shared seat reference so a controller that applies them no longer loads the seat rules; its template's text is unchanged.
- 2026-11-02: the pass's shared sections arrive spliced into its
  template, its card losing the plugin root, and it takes § Location;
  because no seat reads the shared reference at startup any more, and
  its template had left out the location every finding carries.
- 2026-11-02: the directional-bias statement becomes the report's bias
  line, a decision ask only where the pass states the record is
  materially misleading; its trigger on a `CONCLUSION-CHANGING`
  correction sharing the direction, its unconditional guard and the note
  on drift auditing removed. The second read gains its record-only run
  after a pass whose report carries a record correction or after which
  an ask is put again, checking the close the controller records before
  it and delivers after it; at most one per pass; its leftover MINORs
  not against binding text take `deferred-minor`, listed in the spec
  terminal-pass record's new `## Deferred minors` and the plan record's
  `## Terminal pass`; the spec terminal-pass record's states gain
  `dispatched → returned → verified → readout`; the card gains a
  `{re-read}` slot saying whether a re-read is due. The follow-up wave
  takes what any fix list takes. From the skill text rewrite.
- 2026-11-02: the stop check no longer counts a stop called while a
  premise ask was pending as a mismatch, the hold on the stop being
  retired (`docs/decisions/spec-campaign.md`).
- 2026-10-30: decision-ask fidelity also checks that each question
  carried to readout is quoted verbatim, reading it in its seat report,
  and that a call left to the controller is recorded as delegated; in a
  spec campaign, each accepted or firm approval the artifact states
  against the artifact and the records of its change, through a new
  `{decision-record-path}` slot on its card, and a stop called while a
  premise ask holding it was pending; the pass reads the shared
  reference's § Premise findings and § Binding items and unrecorded
  choices; after an audit found approvals in no reviewer's inputs.
- 2026-10-29: in a spec campaign, decision-ask fidelity also checks the
  stop's basis against every numbered round's forecast lines and the
  stop round's fix list against the re-shape rule, a mismatch that would
  have changed the stop flagged `CONCLUSION-CHANGING`; its inputs gain
  the seats' verdict sections and its card the plugin root; after the
  stop trigger became the overturn question.
- 2026-10-13: the terminal pass: an artifact re-read and decision-ask
  fidelity, stated in full only in its template, and a mandatory
  directional-bias statement that escalates only above its threshold.
