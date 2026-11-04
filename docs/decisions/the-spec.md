# The spec

## Decision

**The spec is a hypothesis.** A spec is read as probably subtly wrong and certainly locally imperfect. What binds in it, from its campaign's close, is its Constraints & invariants, the decisions it records as the operator's firm preference, the preamble conventions it declares binding and the umbrella content its umbrella line brings in; binding means never changed silently, and binding text is read for its intent. Everything else is lightly held, whoever proposed it, and downstream work may flip it with a logged rationale (`skills/subagent-driven-development/references/review-terms.md` § What binds in a spec; `crucible:brainstorming § Spec contract`).

**The request.** No spec, folded document, lane note or umbrella quotes a message from the operator: the Intent states the goal in its own words, and the messages that asked, verbatim, go to the feature workspace's `request.md`, deleted with it (`crucible:brainstorming § Workspace provisioning`; `skills/redteaming/references/formats.md` § Feature workspace root and layout). It is evidence of what was asked, not the standard, and a seat may find the request itself wrong. An umbrella's request goes with its workspace at the landing, and a child's holds only the messages of its own brainstorm and after. Seats that run the goal check receive the file by path and check the Intent against it (`docs/decisions/evidence-and-findings.md`, the goal check).

**Decision weights.** Constraints & invariants binds by construction and holds invariants every task must keep, not a requirement one site meets (`crucible:brainstorming § Spec contract`). A decision binds only where it is the operator's firm preference; no mark makes a decision binding, and what builds on an item is judged where a change to it is weighed (§ Flip paths).

**Approval strength.** The brainstorm decision record records each decision `open`, `accepted` or `firm`, each entry naming its proposer for attribution only: decision records attribute each position's basis from it (`docs/decisions/decision-records.md`), and no rule routes on it. `accepted` is the default for any approval, meaning "this until new evidence arrives"; `firm` is recorded only on the operator's explicit word; an answer that leaves the call to the controller is recorded `accepted — delegated to the controller`, never as the operator's ruling or choice (`crucible:brainstorming § Workspace provisioning`; for a route entry, `crucible:brainstorming § Proposing the arrangement`; for later rulings, `skills/redteaming/references/formats.md` § Feature workspace root and layout).

**Flip paths.** From the spec campaign's close on, binding content found wrong changes only through a scoped amendment or a supersede, and every such change is either contained, which the controller confirms and records as its own ruling, or put to the operator as a decision ask. The procedure, the test and its exclusions are stated once, in `skills/redteaming/references/flip-paths.md` (§ The containment test). A premise finding goes to the operator as a decision ask at any phase, never confirmed as contained (`skills/redteaming/references/premise-asks.md` § Premise findings; `docs/decisions/evidence-and-findings.md`).

**Requirements by pointer.** The converged spec is a shared input every downstream agent reads for itself; isolation covers the campaign's exhaust, never the spec. Nothing is copied into plans or briefs, and the plan header's spec pointer is the only pin (`crucible:writing-plans § Plan header`; `skills/subagent-driven-development/implementer-prompt.md` § Requirements; `skills/subagent-driven-development/references/inline-mode.md`; `skills/requesting-code-review/code-reviewer.md` § Binding Content). A task-loop review names the amendment and ruling commits in its range, and any other change there to the plan, a folded document or the spec is a scope finding (`skills/subagent-driven-development/task-reviewer-prompt.md` § Verdict 2: Scope).

**Intent-weighted content.** Mechanism sketches are advisory. A spec pins what binds or crosses tasks and defers local mechanism to the implementer at any severity; non-local mechanism, binding and cross-task content are never deferred (`crucible:writing-plans § Deferring detail`). Fixes land at the altitude of the text around them, and the spec states the current design only (`crucible:redteaming § Fix application and blind verification`). Seats grade sketches only for contradiction with binding content or infeasibility, and raise missing detail only when it is non-local (`skills/subagent-driven-development/references/review-terms.md` § Finding scope; `crucible:redteaming § Merge and finding hygiene`).

**Restated rules are interfaces.** A rule stated in several places has every stating site as a consumer: brainstorming's consumer sweep and a plan task's Files field enumerate them, and a fix report names the sibling instances of its defect (`crucible:brainstorming § Spec self-review`, check 5).

**Rules tied to a trigger are traced.** The same check traces each rule a design ties to a trigger through every route and phase that must reach it; where the trigger occurs and nothing reaches the rule, the design has a gap. The branch reviewer asks the same of the shipped text (`docs/decisions/branch-review.md`).

**A break is stated.** A landing that leaves the base unable to do what it did, or a path someone can reach failing, says so in its Intent; the operator sees it at the design presentation and again before the landing, and the branch reviewer labels an unstated one that follows from what the branch sets out to do, for the operator to repair or accept by a ruling (`crucible:brainstorming § Spec contract`; `skills/subagent-driven-development/references/finish.md`; `skills/requesting-code-review/code-reviewer.md` § What to Check; `crucible:requesting-code-review § The branch-review loop`). A permanent removal counts, stated as permanent. Work nobody can reach yet is not a break.

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
ask, and the maintainer agreed. A mark then named what
built on it, which the test read off it; the operator's preference was
recorded as a status, `firm`, not a mark: a mark recorded what built on
a decision, `firm` the operator's preference. The two
marks the skills had placed on
their own text, on the redteaming reporting stance and the branch
review's wave cap, went with their wording kept. Approvals default to
`accepted` because most mean "this until new evidence arrives", and the
maintainer left the statuses to the agent ("your call"). (Basis: the
maintainer's preference, for the aim; judgment, accepted by the
maintainer, for the test, the mark's form and the statuses, 2026-10-28;
measured, for the two exclusions' cases; judgment, a branch review's
proposal accepted by the maintainer, for testing a literal-reading ruling.)

On 2026-11-02 the marks were retired, among the campaign mechanisms the
skill text rewrite retired. What binds is the Constraints & invariants,
the preamble conventions a spec declares binding and the firm decisions,
and for a child of an umbrella also its entry and the umbrella's
Constraints and firm decisions; the containment test judges what builds
on any item, with no mark to read it from. The sample above had found 3
of 29 marks with any binding event after their campaign closed, and the
maintainer had judged them used too liberally. Every statement of what
binds dropped its marks and kept the rest. (Basis: judgment, an agent's
proposal accepted by the maintainer, for the retirement; the
maintainer's preference, for marks being used too liberally; measured,
for the sample.)

This record once restated the test's exclusions, and when the test
gained one, marking `Review: branch only` a task that has not run once
the plan's review has closed, the restatement missed it (the audit,
`docs/decisions/evidence-and-findings.md`). Since 2026-10-30 the record
points to the test's one home instead. The proposer each entry names,
as the binding-and-marks review had already ruled, is the brainstorm
decision record's, kept for attribution, and the premise line that
routed on it went on 2026-10-30 (`docs/decisions/evidence-and-findings.md`).
An answer leaving the call to the controller is recorded as delegated,
never as the operator's ruling or choice, so that the record keeps
apart the calls the maintainer made and those the maintainer left to
the agent. Each an agent's proposal, which the maintainer accepted at
the brainstorm. (Basis: measured, for the missed exclusion; judgment,
accepted by the maintainer, 2026-10-29.)

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

On 2026-11-01 the request moved out of the committed documents into
the feature workspace. Feature folders are committed and often pushed,
so a quoted request published the operator's private messages in every
project running crucible. The workspace is already uncommitted,
reaches every seat by an absolute path, and lives past the branch
review, the last seat that runs the goal check. Pointing seats at the
host's session transcripts instead was rejected: their formats are
host-specific, a feature can span several sessions, they cost a seat
time and noise to read, and they expose the seat to the controller's
framing of the work. A request store of its own that outlives the
workspace was rejected by the maintainer as a hack. For an umbrella
the request goes with its workspace at the landing, so a child checks
its Intent against its own brainstorm's request, the umbrella's Intent
and its own entry, and the closing review reads fidelity to the
umbrella's Intent. The accepted cost: no child's seats can catch an
umbrella Intent that misread the effort's request; that check is left
to the umbrella's own review, its campaign or the operator's approval.
(Basis: the maintainer's preference, for the rejected store; judgment,
accepted by the maintainer, for the rest.)

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
classes it measured (`docs/decisions/evidence-and-findings.md`, Evidence
on the author's side). Treating every
restating site as a consumer puts those siblings in the sweep. (Basis:
measured.)

### Breaks

Nothing stated what a landing leaves the base able to do. Asked whether an
incomplete umbrella's children should land on the base at all, the
maintainer reported no practical trouble, since they arrange a run around
partial work when they plan one, but "it requires being aware of the
issue", and by default the process could break the base without anyone
saying so. (Basis: the maintainer's preference, 2026-11-04.)

So the gap sits at every landing, a feature with no umbrella included. The
Intent states a break because the reviewer's goal check reads the Intent
and the design presentation shows it to the operator; the reviewer checks
because an author omits the break they did not think of; the close readout
repeats it because that is when a run or a release can still be timed around
it. A break the reviewer finds goes to the operator, since a fix wave can
only repair or dispute it, and only later work may be able to remove it; a
defect a fix can repair stays an ordinary finding, or every regression
would become an operator ask. Accepting one is a ruling, not an edit to
the spec, which would need a new pin the plan cannot take outside a flip
path. A permanent removal counts because a run can need timing around that
too. A standalone branch has no Intent or close readout, so the reviewer's
finding is all that reaches its operator.
Unreachable work stays out of the rule, so most landings owe nothing. The
rule's word is "break" because "containment" already names the
containment test for amendments. A reviewer reading a diff, with no run of
the product, can miss a break: an accepted residual. No agent was run on
the wording, the maintainer's account standing as the baseline. (Basis:
judgment, accepted by the maintainer, 2026-11-04; for the route of a break
the reviewer finds and for counting a permanent removal, judgment, accepted
by the maintainer, who left the call to the agent.)

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
- **`[LOAD-BEARING]` marks**, binding the sentence they annotated, the
  rule until 2026-11-02, and **a mark for the operator's preference**,
  which is recorded `firm` (§ Why).
- **The request quoted in committed documents**, redacted where a
  project's rules keep a part out, the form of 2026-10-29: it published
  the operator's messages (§ Why).
- **Seats reading the session transcripts for the request**, and **a
  request store that outlives the workspace** (§ Why).
- **The question at an umbrella's proposal alone:** a feature with no
  umbrella can break the base too (§ Why, Breaks).
- **A required no-break line in every close readout:** it would add text to
  every landing, and the reviewer's check already covers a silent one
  (§ Why, Breaks).

## Changes

- 2026-11-04: a landing that breaks the base, permanently or not, states it in its Intent, the operator sees it at the design presentation and before the landing, and the branch reviewer labels an unstated one that follows from what the branch sets out to do, for the operator to repair or accept by a ruling; because by default a landing could break the base with nobody saying so.
- 2026-11-03: the citations of brainstorming's workspace provisioning use its shortened heading.
- 2026-11-03: the premise-finding route is cited at `skills/redteaming/references/premise-asks.md`, where flip-paths' § Premise findings moved, so a controller handling a premise finding no longer loads the flip paths (`docs/decisions/authoring-crucible.md`).
- 2026-11-03: what binds is cited at its one controller statement, `skills/subagent-driven-development/references/review-terms.md` § What binds in a spec, moved there from flip-paths' opening so every route's controller reads it from brainstorm on (`docs/decisions/instruments.md`).
- 2026-11-03: citations follow the rules to their owners: what binds to
  flip-paths' opening, the measured finding classes to the evidence
  record, where brainstorming no longer states them.
- 2026-11-02: approval strength is recorded in the brainstorm decision
  record alone, the design digest being retired
  (`docs/decisions/operator-steering.md`).
- 2026-11-02: `[LOAD-BEARING]` marks retired: what binds is the
  Constraints & invariants, declared preamble conventions and firm
  decisions, and for a child its entry and the umbrella's Constraints
  and firm decisions; the containment test judges what builds on any
  item; because the marks were used too liberally and rarely fired.
- 2026-11-01: the request moves from a section of every committed
  document to the feature workspace's `request.md`, with no redaction;
  an umbrella's request goes with its workspace at the landing and a
  child's holds only its own brainstorm's messages; because quoting it
  in committed, often pushed feature folders published the operator's
  private messages.
- 2026-10-30: the containment test's exclusions are no longer restated
  here, the record pointing to the test's one home, after an audit found
  the restatement missing the newest; the proposer an entry names is the
  brainstorm decision record's, for attribution only, no rule routing
  on it; a call left to the controller is recorded
  `accepted — delegated to the controller`; a premise finding is a claim
  that the request, the Intent or a firm decision is wrong.
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
