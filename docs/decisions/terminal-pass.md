# Terminal pass

## Decision

Every spec campaign closes with the terminal pass, one fresh seat outside
the cap; the plan phase closes with its own after its fix wave. It has
two mandates, in this order: a re-read of the artifact, recorded before
it opens any record, then decision-ask fidelity, checking each ask
against the findings behind it and, in a spec campaign, the stop: the
stated basis against every forecast line in the numbered rounds' seat
verdicts, each forecast overturn answered by the mechanism it names,
and the stop round's fix list against the rule that a round whose wave
re-shapes a major mechanism is no stop round
(`docs/decisions/spec-campaign.md`). For that check its inputs gain
every numbered round's seat reports, their verdict sections only.
Decision-ask fidelity also checks, in both phases, that each question a
round record carries to readout is quoted verbatim in that readout,
reading it in its seat report's `Questions`, and that a call the
operator left to the controller is entered as delegated, never as the
operator's ruling or choice; and, in a spec campaign, each `accepted`
or `firm` entry of the brainstorm decision record whose decision the
artifact states, process entries such as the route and the campaign
shape aside: the decision still holds in the artifact, or a later entry
or a round readout naming the change and what it withdraws records its
change, an approval withdrawn with no such record being flagged
`CONCLUSION-CHANGING`. The record reaches it through its card's
`{decision-record-path}` slot, the spec phase's brainstorm decision
record and `none` in the plan phase. Its card carries the plugin root,
through which it reads the shared reference's overturn question,
§ Premise findings and § Binding items and unrecorded choices
(`docs/decisions/instruments.md`). It reports counted record corrections,
and only a correction flagged `CONCLUSION-CHANGING` reaches the operator
as a decision ask. Its directional-bias statement is mandatory and
unconditional, and escalates only above its threshold. Its tail is
bounded: in the spec campaign one further fix wave and a second read, in
the plan phase one scoped repair and a resumed second read. The
mandates, inputs, flag test and threshold are stated in full only in
`skills/redteaming/terminal-pass-prompt.md`
(`crucible:redteaming § Stop rule and terminal pass`).

## Why

### Why a pass at all

A campaign that stopped on a fix wave would otherwise converge on edits
no seat had read: the pass is the review of the last wave (crucible's
first design, 2026-08-06; judgment, accepted by the maintainer). It
earns its place: in a recount of the campaign records (2026-10-12), the
pass's first read found a BLOCKER or MAJOR after the stop call in 27 of
74 campaigns. (Basis: measured.)

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
(`docs/backlog/decision-ask-framing.md`). The same audit found doubts
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

The re-read comes first because reading the records' account of the
artifact before the artifact turns a confirming read into a re-derivation
of someone else's conclusion (2026-08-16). Counted corrections replaced
a pass or fail verdict on the record the same day, a binary verdict
inviting rumination over the record's author rather than a correction of
the record. (Basis: judgment, accepted by the maintainer.)

### The bias statement

Each fidelity check and the materiality flag judge one item at a time:
a set of individually immaterial corrections all leaning one way passes
every one of them. The operating stance makes errors cheap to disclose
and names shading a record as the one reportable failure of the
reporting duty (`docs/decisions/spec-campaign.md`); the bias statement is
the instrument that reports it. Before it existed, one pass reading its
corrections together had already observed that both "point the same
direction: toward the self-correction narrative" (2026-08-15). (Basis:
judgment, accepted by the maintainer; a single incident, for the
observation.)

The escalation got its threshold on 2026-08-21, because the ask below it
had fired in nearly every campaign and never changed anything. A
standing-stance line, written into the closing record below the
threshold, went on 2026-10-13: its reader was the committed record
trail, which crucible no longer keeps. (Basis: judgment, accepted by the
maintainer.)

### The tail

One campaign ran a re-pass and then appended six re-checks after it, so
the tail was bounded on 2026-09-27 to one fix wave and one second read
whose report is the last. A second read writes a new file rather than
appending, so the first report stays as written (2026-10-07). In the
plan phase the repaired text is itself unreviewed, which is why the
second read covers the whole repaired region, never the flagged item
alone. (Basis: a single incident, for the bound; judgment, accepted by
the maintainer, for the rest.)

## Rejected

- **A fidelity seat every round**: the same check at higher cost
  (§ Why).
- **Ruling-consistency, conservation-walk and whole-seat-report
  mandates for the pass**, removed on 2026-10-07 (§ Why); of the seat
  reports, the stop check reads the verdict sections and the fidelity
  check the questions carried to readout, and no more.
- **Escalating every correction**, or every directional-bias statement,
  to the operator (§ Why).
- **A standing-stance line below the threshold** (§ Why).
- **A pass or fail verdict on the record** (§ Why).

## Changes

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
