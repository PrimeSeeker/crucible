# The spec

## Decision

**The spec is a hypothesis.** A spec is read as probably subtly wrong
and certainly locally imperfect. What binds in it, from its campaign's
close, is its Constraints & invariants, its marks, the decisions it
records as the operator's firm preference, the preamble conventions it
declares binding, and the umbrella content its umbrella line brings in.
Binding means never changed silently, not never changed without the
operator, and binding text is read for its intent: a case its literal
reading reaches that its author plainly did not consider is raised for a
ruling, never applied literally. Everything else is lightly held, and
downstream work may flip it with a logged rationale
(`crucible:brainstorming § Spec contract`).

**The request.** A `## Request` section precedes the Intent of every
spec, folded document, lane note and umbrella: the message that asked
for the work and each later message that changed what was asked,
verbatim, a message the controller is unsure about included. It stands
outside the parts any route makes binding: it is evidence of what was
asked, not the standard, and a seat may find the request itself wrong.
A part the project's rules for committed text keep out is replaced by
`[redacted: <kind>]`, and where no rule settles a part, the controller
asks the operator once, as it writes the section. A child's Request
points to its umbrella's and quotes only what was asked of the child, or
the effort's whole request where its umbrella has none. Seats check the
Intent against it (`docs/decisions/evidence-and-findings.md`, the goal
check).

**Decision weights.** A mark, `[LOAD-BEARING: <what builds on it>]`,
binds exactly the sentence or bullet it annotates, and is earned only
where something beyond that sentence builds on the decision: other
tasks, other features or children, an outside commitment. A wording, a
threshold only the feature uses and the operator's preference earn none.
Constraints & invariants binds by construction and holds invariants
every task must keep, not a requirement one site meets. Marks are a spec
convention: the skills place none on their own text.

**Approval strength.** The brainstorm decision record and the design
digest record each decision `open`, `accepted` or `firm`, and each
record entry names its proposer, the operator or the controller.
`accepted`, the default for any approval, a "+", an "OK" or a "your
call" included, means "this until new evidence arrives"; `firm` is
recorded only on the operator's explicit word, never inferred from an
approval. A firm decision that reaches a spec or an umbrella is stated
there as the operator's firm preference and binds without a mark. A
route entry confirms its route only when `accepted` or `firm`. Every
operator ruling on a decision ask after the brainstorm enters the
brainstorm decision record too (`crucible:brainstorming § Workspace
provisioning (brainstorm exit)`;
`skills/redteaming/references/formats.md` § Feature workspace root and
layout).

**Flip paths.** From the spec campaign's close on, binding content found
wrong changes only through a scoped amendment (a correction inside a
mechanism that stands; no new campaign or plan phase) or a supersede (a
successor with its own review). Every change to binding content, a
ruling that patches the plan included, is either contained or put to
the operator as a decision ask. It is contained when everything that
builds on or consumes the changed item lies inside the feature, and it
changes no umbrella content and no firm decision, makes no failing
check pass on the same work, and redefines no mechanism, which takes a
supersede. The controller confirms a contained scoped amendment itself
and records it as its own ruling, which reaches the branch review and
the close readout; reversing one is a scoped amendment the operator
confirms. The procedure and the test are stated once, in
`skills/redteaming/references/flip-paths.md` (§ The containment test).
A premise finding, a claim that something the operator asked for or
decided is wrong, goes to the operator as a decision ask at any phase,
the spec campaign included, never confirmed as contained; where it is
also a binding item found wrong, a firm decision or a lane note's
Intent, its route governs (`skills/redteaming/references/flip-paths.md`
§ Premise findings).

**Requirements by pointer.** The converged spec is a shared input every
downstream agent reads for itself; isolation covers the campaign's
exhaust, never the spec. Nothing is copied into plans or briefs: a
task-loop seat is given the plan's path and its task number
(`crucible:subagent-driven-development § The Task Loop`), a task the
controller implements inline is reviewed with the same pointer, and the
plan header's spec pointer is the only pin. A task-loop review names the
amendment and ruling commits in its range, and any other change there to
the plan, a folded document or the spec is a scope finding. The branch
review reads the spec at its pinned revision and the plan.

**Intent-weighted content.** Mechanism sketches are advisory. A spec
pins what binds or crosses tasks and defers local mechanism to the
implementer at any severity; non-local mechanism, binding and cross-task
content are never deferred. Fixes land at the altitude of the text around
them, and the spec states the current design only. Seats grade sketches
only for contradiction or infeasibility, and raise missing detail only
when it is non-local (`crucible:redteaming § Merge and finding hygiene`;
`crucible:redteaming § Fix application and blind verification`).

**Restated rules are interfaces.** A rule stated in several places has
every stating site as a consumer: brainstorming's consumer sweep and a
plan task's Files field enumerate them, and a fix report names the
sibling instances of its defect (`crucible:brainstorming § Spec
self-review`, check 5).

**Rules tied to a trigger are traced.** For a rule a design ties to a
trigger ("at each X, do Y"), the same check names every route and phase
that must reach the rule and the moment X occurs in each; where X occurs
and nothing reaches the rule, the design has a gap. The branch reviewer
asks the same of the shipped text (`docs/decisions/branch-review.md`).

## Why

### Weights and flip paths

The maintainer's amendment to the design philosophy of 2026-08-06: a
design does not freeze at plan acceptance. A spec carries many lightly held
positions that downstream work is expected to flip, while a load-bearing
decision either holds or goes through an explicit event, "never a quiet
in-flight rewrite". The scoped amendment, for a contained flip with no
new campaign, was adopted on 2026-08-07, and on 2026-08-22 the maintainer
ruled that the bar binds only from the campaign's close: during its own
campaign the spec is the artifact under review. The procedure moved to
one shared reference on 2026-10-13, after its two copies in redteaming
and SDD had drifted apart; the maintainer chose that option. (Basis: the
maintainer's preference.)

Downstream, an implementer may depart from what is lightly held, logging
each departure, but one who finds binding content wrong reports BLOCKED
and never improvises around it
(`skills/subagent-driven-development/implementer-prompt.md` § Binding vs
Advisory: the Deviation License). (Basis: judgment, accepted by the
maintainer, 2026-08-05.) Since 2026-10-28 the report names the item, the
evidence that shows it wrong and a proposed correction
(`docs/decisions/task-loop.md`).

### The spec as a hypothesis

The maintainer asked that the process state throughout that a spec is
"likely subtly flawed (and almost certainly has some local errors as
well, given that we're trying to stop redteaming early)", and observed
that most of their approvals are shaped like "no strong preference,
let's go with this until new evidence arrives", while "load-bearing
marks are used too liberally and result in bureaucracy" (2026-10-28).
An earlier count found 27 and 15 marks in the specs of crucible's first
two features (August 2026), and 0 to 7, most 2 or 3, in those since
October; the maintainer, on 2026-10-27: "we're probably marking too
many points as load-bearing". (Basis: the maintainer's preference, for
the aim; measured, for the count.)

Until 2026-10-28 every correction to a spec's binding content, however
contained, cost an operator ask. A sample took the place of a full count, which
workspaces deleted at finish would have made a transcript dig, and in
which a mark that never fired cannot be told from one that deterred a
drift: four features with marks that went through implementation, on
crucible and one other project, their session transcripts searched by
keyword, so the figures are order-of-magnitude only and the sample's
report is not committed. 3 of 29 marks and 9 of 36 Constraints items had
any binding event after their campaign closed, most of them a review
finding that cited the item and rejected a real drift, at the cost of at
most a fix round. The costly cases took three shapes: ceremony, a mark
on a command's wording forcing a scoped amendment and a re-pin of the
plan; literalism, a controller applying a Constraint literally to an
edge case its author plausibly never considered and removing existing
behaviour, with no ask; and a probably blocked improvement, a Constraint
reverting an implementer's improvement. The one chain of a stop and two
asks began at an Acceptance threshold and ended in a Constraint change
the maintainer accepted with "OK, I guess", after the host's permission
classifier had refused the spec edit as "rewriting a binding acceptance
threshold so a failing gate would pass". Unmarked operator rulings
flipped downstream went fine, under the logged-rationale rule. An agent
offered dropping the count or sampling, recommending the first, and the
maintainer chose the sample. (Basis: measured, for the sample; the
maintainer's preference, for sampling in place of a count, 2026-10-28.)

Under the containment test, a correction whose consumers all lie inside
the feature is the controller's to confirm, and is made visible rather
than asked: its marker, its named commit, a ruling in the ledger that the branch review
receives, and a line in the close readout. Umbrella content and firm
decisions keep the operator's ask they had; the failing-check exclusion
answers the acceptance-threshold case, and the intent reading the
literalism case, with a ruling on a literal-reading case passing the
test whichever way it goes, since the controller that rules on it is
the role that applied the text literally in the sample. An agent
proposed the controller as confirmer, one of three options with a
fresh adjudicator per correction and a batched, non-blocking operator
ask, and the maintainer agreed. A mark names what
builds on it, which is what the test reads off it; the operator's
preference is recorded as a status, `firm`, not a mark: a mark records
what builds on a decision, `firm` the operator's preference. The two
marks the skills had placed on
their own text, on the redteaming reporting stance and the branch
review's wave cap, went with their wording kept. Approvals default to
`accepted` because most mean "this until new evidence arrives", and the
maintainer left the statuses to the agent ("your call"). (Basis: the
maintainer's preference, for the aim; judgment, accepted by the
maintainer, for the test, the mark's form and the statuses, 2026-10-28;
measured, for the two exclusions' cases; judgment, a branch review's
proposal accepted by the maintainer, for testing a literal-reading ruling.)

### The request

Until 2026-10-29 no step recorded the operator's request and no seat saw
it, so none could check a spec's Intent against what was asked. The
hypothesis-specs umbrella asked for the request quoted verbatim in the
spec or lane note itself, where every seat already reads it, redacted
where `AGENTS.md`'s no-local-context rule would keep a part out, as
evidence and not the standard. Its placement before the Intent, outside
every binding part, and its form are an agent's proposal, which the
maintainer accepted; the placement moved there from the opening of the
Intent during the spec's campaign, since a lane note's Intent binds and the
request must not. (Basis: judgment, accepted by the maintainer.)

### The trace

On crucible's umbrella-specs feature (2026-10-28), the spec campaign and
the plan phase missed a rule triggered "at each task or round boundary"
in two phases that have none, the very-small lane and every branch
review; an implementer and the branch review found it. The consumer
sweep finds the sites that state a rule; it does not ask whether every
flow reaches the rule's trigger. The trace sits in the author's
self-review and the branch review, and gives no campaign seat a duty: an
agent's proposal, which the maintainer accepted. (Basis: a single
incident; judgment, accepted by the maintainer.)

### Pointers, not copies

Copying spec content into the plan and then into every task brief made
the copy the reviewed object. Measured on crucible's own dual-runtime
spec and plan campaigns (2026-08): the share of findings caused by
earlier rounds' own edits rose rather than fell (plan campaign, by round:
17, 53, 80, 87 and 83%), a recurring finding was "X is uncarried, inline
it", and 35 test functions over 1,147 lines existed only to check the
copying. Isolation was the reason for copying, yet all four recorded
cases of a seat seeing what it should not were campaign exhaust, none the
spec; the blind fix verifier stays the one seat kept from the spec.
Carriage retired on 2026-08-17. On 2026-10-11 the brief extractor
went too: a 649-line script that parsed agent-written plan markdown and
grew its rules one misread input shape at a time, for a seat that can
read one section of a plan itself. (Basis: measured.)

### Intent at the spec's altitude

Agents read literally, so what binds must be explicit and everything
else visibly advisory (the design philosophy of 2026-08-06; judgment,
accepted by the maintainer). Measured over four large spec campaigns crucible
ran on one project (2026-09-27): Decisions sections grew 2.8 to 5.4 times
across a campaign and bare numbers about 3.5 to 4.2 times, rounds 4 and 5
still produced blockers, and in the three campaigns instrumented for it,
60 to 90% of the findings from round 2 on were introduced by earlier fix
waves. That fits fixes landing below the altitude of the text around
them and carrying their mechanism in, which the rule then in force made
necessary by forbidding the deferral of any blocker or major finding.
(Basis: measured.)

### Restated rules

In a 2026-08-27 classification of about 1,620 findings from 24 campaign
records, fix waves that failed to land were dominated by a correct fix
applied at one site while sibling statements of the same content stood
unedited; an unenumerated consumer is one of the two largest finding
classes `crucible:brainstorming § Spec self-review` names. Treating every
restating site as a consumer puts those siblings in the sweep. (Basis:
measured.)

## Rejected

- **Carriage**: copying the spec's [LOAD-BEARING] decisions into a plan's
  global constraints and per-task constraints fields, and extracting a
  brief per task (§ Why).
- **Plan revisions stamped into dispatches**: the plan header's spec
  pointer is the only pin; seats read the live plan, and the commits that
  patched it are named instead.
- **Deferral bounded to minor findings**: it forced blockers and majors
  to land their mechanism in the spec (§ Why).
- **Annotating a fix in the spec** with finding citations or changelog
  prose: what changed and why lives in the round records.
- **An operator ask for every correction to binding content**, the rule
  until 2026-10-28, and **a fresh adjudicator per correction or a
  batched, non-blocking operator ask** as the confirmer of a contained
  one (§ Why).
- **A mark for the operator's preference**: it is recorded `firm`
  (§ Why).

## Changes

- 2026-10-29: a `## Request` section, outside the binding parts, before
  every spec's, folded document's, lane note's and umbrella's Intent; a
  premise finding goes to the operator at any phase; check 5 traces each
  rule tied to a trigger through every route and phase; after the
  umbrella-specs run and the hypothesis-specs umbrella's entry.
- 2026-10-28: testing a literal-reading ruling, accepted by the
  maintainer at the landing.
- 2026-10-28: sampling in place of a count attributed to the
  maintainer's preference, as the brainstorm record has it.
- 2026-10-28: a ruling on a literal-reading case passes the containment
  test whichever way it goes, after a branch review found the
  controller's own literal application unguarded.
- 2026-10-28: the spec as a hypothesis: firm decisions bind, binding
  text is read for its intent, the controller confirms a scoped
  amendment the containment test finds contained and records it as its
  ruling, a mark names what builds on it and the skills carry none, and
  approvals are recorded `open`, `accepted` or `firm` with a proposer;
  after the maintainer's request and a sample of marks and Constraints
  items after their campaign's close.
- 2026-10-13: flip paths: the scoped amendment and the supersede, stated
  once in a shared reference.
- 2026-10-11: requirements by pointer: the plan's path and task number,
  with no brief extracted.
- 2026-10-01: a rule restated in several places is an interface whose
  consumers are its restating sites.
- 2026-09-27: intent-weighted content: local mechanism deferred at any
  severity, fixes at the text's own altitude.
- 2026-08-06: decision weights: [LOAD-BEARING] marks bind, everything
  else is lightly held.
