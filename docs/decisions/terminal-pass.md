# Terminal pass

## Decision

Every spec campaign closes with the terminal pass, one fresh seat outside
the cap; the plan phase closes with its own after its fix wave. It has
two mandates, in this order: a re-read of the artifact, recorded before
it opens any record, then decision-ask fidelity, checking each ask
against the findings behind it. It reports counted record corrections,
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
  mandates for the pass**, removed on 2026-10-07 (§ Why).
- **Escalating every correction**, or every directional-bias statement,
  to the operator (§ Why).
- **A standing-stance line below the threshold** (§ Why).
- **A pass or fail verdict on the record** (§ Why).

## Changes

- 2026-10-13: the terminal pass: an artifact re-read and decision-ask
  fidelity, stated in full only in its template, and a mandatory
  directional-bias statement that escalates only above its threshold.
