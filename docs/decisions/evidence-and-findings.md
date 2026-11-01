# Evidence and findings

## Decision

**Finding hygiene.** Panel seats, the terminal pass and the execution
reviewers stake a severity on each finding, BLOCKER, MAJOR or MINOR. In
the spec campaign and the plan phase, a BLOCKER without a reproduction
or evidence is a question, a code-shaped claim in a finding (what a
regex, a command or the code does) carries a run transcript or the tag
`UNVERIFIED`, and an `UNVERIFIED` finding never enters a fix list as it
stands: the controller verifies or discards it
(`skills/redteaming/seat-prompt.md`; `crucible:redteaming § Merge and
finding hygiene`). Every finding carries its evidence and a location:
file:line, or, for a premise finding, the passage of the spec, plan or
request it contradicts
(`skills/subagent-driven-development/references/premise-and-questions.md`
§ Location). The task reviewer and the branch reviewer treat a BLOCKER
without evidence as a question; the re-reviewer cites file:line for its
verdicts and any new breakage; none of the three uses the `UNVERIFIED`
tag. Improvements and style are not findings: an improvement goes in a
seat's `Questions` (below). The execution reviewers raise no formatting
that no repo tool enforces: where a tool enforces it, the tool's failure
is the finding
(`skills/subagent-driven-development/task-reviewer-prompt.md` § Finding
Hygiene and Severity; `skills/requesting-code-review/code-reviewer.md` §
Calibration).

**Premise findings.** A redteam seat, the terminal pass, the branch
reviewer, an umbrella's closing-review seat or an implementer may claim,
with evidence, that one of three things is wrong:
the request, what the Intent asks for, or a firm decision. The request
is the feature workspace's `request.md`, which the seats running the
goal check receive by path (`docs/decisions/the-spec.md`); the Intent is
a section of the document, and a firm decision says so in its
rationale. On the very-small lane the lane note's Intent stands for the
spec's; for an umbrella's child the umbrella's Intent is protected as
the child's own is, and a change on the child's branch to what that
Intent asks is a finding. The finding
carries the label `premise` after its staked severity. Every other
decision, whoever proposed it, is lightly held: a finding against it is
an ordinary one, and so is a correction of an Intent's wording or facts
that leaves what it asks for unchanged. Any other binding item shown
wrong, such as a Constraint, keeps its own route, and a
`literal-reading` finding keeps its own label, since it questions an
application, not the premise. No rule routes on who proposed a
decision. A task reviewer raises none: its doubt about a premise is a question
(`skills/subagent-driven-development/references/premise-and-questions.md`
§ Premise findings). The controller corrects a label in either
direction, its reason recorded with it. Every premise finding goes to
the operator as a decision ask with a recommendation. It is an open
decision ask, not an open BLOCKER or MAJOR: it holds open no gate keyed
on one, opens no fix wave and consumes no cap, the readouts carry it
until it is ruled, and work goes on except what builds on the
challenged premise. In a spec campaign, one whose upholding would
re-shape a major mechanism holds the stop until it is ruled
(`docs/decisions/spec-campaign.md`). An open one is carried across each
phase's close until ruled
(`skills/redteaming/references/flip-paths.md` § Premise findings).

**The goal check.** Before reading the Intent, a redteam seat and the
branch reviewer restate in one sentence the goal that the request file
their dispatch names asks for (`docs/decisions/the-spec.md`), then
compare it with the Intent: a mismatch the seat can stand behind is a
premise finding, a vaguer one a question. A plan-phase seat compares it
with the Intent of the spec the plan's header names and the plan's
Goal; an umbrella child's seat with the child's Intent, the umbrella's
Intent and the child's entry. With no request file, the seat restates
the goal from the Intent and says the request was unavailable.
On the very-small lane the check is part of the branch reviewer's Lane
Fit (`docs/decisions/routes.md`;
`skills/subagent-driven-development/references/premise-and-questions.md`
§ The goal check).

**Questions.** Redteam seats, the task reviewer, the branch reviewer and
the implementer each have a `Questions` section for anything material
they could not stake as a finding: a question, a doubt, a misgiving with
nothing specific to point to, or a suggested improvement. It holds a few
items at most, none being the normal case for doubts and misgivings, and
an item carries no severity
(`skills/subagent-driven-development/references/premise-and-questions.md`
§ Questions). Nothing in it is dropped unrecorded: a redteam seat's item
gets a disposition in the round record, answered, carried to the
readout, rejected with a ruling or adopted; a task reviewer's or an
implementer's becomes a lead the branch reviewer rules on
(`docs/decisions/branch-review.md`); the branch reviewer's own go under
the ledger's `## Questions` with the controller's disposition, for the
close readout; a standalone branch review's report is their record. A
redteam seat's question that doubts the request, what the Intent asks
for or a firm decision is always carried to the readout, round 0's
included, since the operator settles such a doubt and the controller is
the Intent's author; the readout quotes each carried question verbatim.
An improvement the controller adopts is a lightly held change it names
in the readout, and rides the next fix wave: in a campaign as a
fix-list item naming the question id; at the branch review as a
labelled change, `Change (improvement)`, which the fixer applies or
declines with a reason, with no defect to confirm and nothing for the
adjudicator, an operator's ruling and work the operator asked for
riding a wave the same way. It never opens a wave by itself, the branch
review's one cleanup wave aside (`docs/decisions/branch-review.md`); the
controller never applies one itself outside the very-small lane; one
with no wave to ride goes to the operator in the readout, and one a
fixer declines is work left open (`crucible:redteaming § Merge and
finding hygiene`; `crucible:requesting-code-review § The branch-review
loop`; `crucible:subagent-driven-development § What a report voices`).

**Evidence on the author's side.** Whoever writes the text under review
carries the seats' rule. A spec's author checks each claim about
existing code, files or tool behaviour as it is written, reading the
file or running the command, or writes it with `UNVERIFIED`, and treats
an unverified draft claim as wrong until checked; the self-review's
evidence check resolves the tags or leaves them as declared input for
the campaign (`crucible:brainstorming § Spec contract`;
`crucible:brainstorming § Spec self-review`). A plan's author reads
every signature, format and pin from the code, never from memory
(`crucible:writing-plans § Self-review`). The controller's fix lists,
merged entries, rulings, verification outcomes, readouts and decision
asks show the evidence for each code-shaped claim or carry `UNVERIFIED`,
and a decision ask resting on an untagged, unverified mechanical fact is
a defect in the ask. The implementer's report gives each code-shaped
claim its command and output, or `UNVERIFIED`
(`skills/subagent-driven-development/implementer-prompt.md` § Report
Format). Before a fix list freezes, each item names every artifact site
restating the content it changes, and an item that adds or changes a
rule, a seat's suggested wording included, also names each site that
brainstorming's consumer sweep and trace find for it: who produces the
rule's input, who reads its output, and which routes and phases reach
it. Every spec-campaign and plan-phase fix list takes the trace, round
0's, a terminal pass's follow-up wave's and a plan-phase repair's
included; execution's waves do not. A fix landing at fewer sites than
its item names has not landed (`crucible:redteaming § Fix application
and blind verification`). `UNVERIFIED` is the one marker; it tags a
claim and never admits a finding to a fix list.

**Evidence before claims.** Before saying work is complete, fixed or
passing, an agent runs the check that shows it and reports what its
output said (`crucible:using-crucible § The Rule`). Where a fix item's
substance is a predicate (an acceptance check, a gate, a grep), the
controller runs it at the tree state it will run against before
recording the item applied, with the command and output under the item;
a check of a state not yet reached must fail on today's tree, and a
check taken from a seat's remedy is run the same way. The implementer
quotes each test result from the run's own output, the tool result or a
background run's output file, and until that output is read the outcome
is unknown, whatever a notification promised
(`skills/subagent-driven-development/implementer-prompt.md` § Tests:
Test-First, Evidence Before Done). The task reviewer takes that reported
output as given; which seats run the full suite is stated in
`docs/decisions/spec-campaign.md`.

**What the requirements leave unsaid.** The execution reviewers read
the requirements' silence as no permission: a failure on an input they
imply but never name is a defect, graded by its effect on a reasonable
person using the software (`skills/requesting-code-review/code-reviewer.md`
§ What to Check; `skills/subagent-driven-development/task-reviewer-prompt.md`
§ Verdict 4: Quality). A redteam seat, the terminal pass and the branch
reviewer report a consequential choice the artifact takes for granted
with no decision recording it, for the branch reviewer one the code
makes, and a binding item that is itself wrong; both clauses have one
home, the shared reference's § Binding items and unrecorded choices
(`skills/subagent-driven-development/references/premise-and-questions.md`),
which the task reviewer and the implementer do not read. The
implementer's test evidence
names every failing test, whether its change caused it or not
(`skills/subagent-driven-development/implementer-prompt.md` § Report
Format), and the task reviewer and the re-reviewer re-read evidence that
looks truncated at its stated path before reporting it missing
(`skills/subagent-driven-development/task-reviewer-prompt.md` § The
Implementer's Report; `skills/subagent-driven-development/re-review-prompt.md`
§ Tests).

## Why

### Review that holds without a human reader

No step requires the operator to read code or a diff
(`docs/decisions/operator-steering.md`), so human review is not the
backstop and crucible's review has to hold on its own: claims are run,
not read, fixes are verified blind, and severities are staked
(2026-08-06). In "FactReview: Evidence-Grounded Peer Review with
Execution-Based Claim Verification", removing execution evidence changed
17.0% of claim statuses, more than removing any other single evidence
source (https://arxiv.org/abs/2604.04074). (Basis: judgment, accepted by
the maintainer; external.)

Improvements and style were ruled out of findings on 2026-08-06, with
the adversarial reviewer stance: the hunt is bounded by finding
hygiene, not by softening. Upstream's reviewer filed code style and
optimization under Minor and asked for strengths and recommendations
(`superpowers/skills/requesting-code-review/code-reviewer.md`). The
maintainer called the rule probably suboptimal (2026-10-20), and asked
for "more proactivity throughout the process? I believe we disallowed
improvement suggestions" (2026-10-28). Improvements stayed out of
findings, which cost a fix wave, and share the `Questions` section with
doubts, an adopted one riding a wave that something else opened: an
agent's proposal, which the maintainer accepted. (Basis: judgment,
accepted by the maintainer, for the 2026-08-06 rule and the shared
section; external, for upstream; the maintainer's preference, for
reopening it.)

An adopted improvement then rode a branch-review fix wave "as one of its
findings", while the fixer's contract is to confirm a defect before
editing and answer each finding fixed or NOT CONFIRMED: an improvement
has no defect, so a fixer that declined it could only dispute it to the
adjudicator (the audit below, at MINOR). Since 2026-10-30 an
improvement, an operator's ruling and requested work ride a wave
labelled as changes, applied or declined with a reason, and an applied
one reaches the re-review, which checks it landed and broke nothing. The
implementer's and re-reviewer's cards name the label, overriding their
templates' two-answer rule for labelled items, so neither template grew.
An agent's proposal, which the maintainer accepted. (Basis: measured,
for the finding; judgment, accepted by the maintainer, for the form.)

### Premise findings, the goal check and questions

The maintainer judged the execution reviewers' mandate narrower than
the redteam seats' and asked for it to be extended "to parity", and
asked whether the process could "detect that things aren't right when
there is no specific issue to point to": "your intents don't mean what
you seem to think they do" is "not a finding in a normal sense, but
potentially useful" (2026-10-28). Until then a seat could find a binding
item wrong, but a doubt about the premise behind it had no form: the
branch reviewer cited file:line for every finding and had no section for
questions, and no seat saw the request. (Basis: the maintainer's
preference, for the aim.)

An escape analysis (2026-10-28) over git history and the first
full-scope branch review of 109 features, on crucible and one other
project, attributed later fixes by blame to the task ranges whose
reviews had approved them. Task reviews let through 12 real defects: 10
minor wording, consistency or comment slips, and 2 MAJORs, both
premise-level, both needing other tasks' knowledge and both caught by
the branch review. Of 11 branch-review BLOCKERs or MAJORs on planned
routes, 6 were premise-level or plan-coverage gaps. (Basis: measured.)
A differential probe of the same day re-read 10 past task reviews that
had approved; on records and design prose its seat raised what the
rubric neither asks for nor forbids, an unruled decision recorded as
settled and controller proposals listed as operator rulings among them
(`docs/decisions/model-roles-and-effort.md`). (Basis: measured, on 10
samples.)

The `premise` label, its route to the operator as a decision ask that
holds no gate, a location that may be a passage, the goal check against
a quoted request, and one `Questions` section for questions, doubts and
improvements across seats are an agent's proposals, which the maintainer
accepted. (Basis: judgment, accepted by the maintainer.) Since
2026-11-01 the quoted request is the feature workspace's `request.md`,
not a section of the committed document, which published the operator's
messages (`docs/decisions/the-spec.md`).

As first written, the line between a premise finding and an ordinary one
followed who stood behind the decision challenged: a finding against a
decision the operator made was a premise finding, against one the
operator only accepted from the controller's proposal an ordinary one.
The audit below found that line unworkable: the spec contract made every
decision neither firm nor marked lightly held, while the shared
reference made a finding against "a decision the operator made" an
operator ask; seats never see a decision's proposer; the mislabel rule
corrected one direction only; and routing on the proposer reversed in
effect the declined mark of who decided (§ What the requirements leave
unsaid). Since 2026-10-30 a premise finding protects what a seat can
read for itself, the request, what the Intent asks for and firm decisions,
and every other decision is lightly held whoever proposed it, which
matches the maintainer's reading of an approval as "this until new
evidence arrives" (`docs/decisions/the-spec.md`). The proposer stays in
the brainstorm decision record, for attribution only, and the controller
corrects a mislabel in either direction. An agent's proposal, which the
maintainer accepted. That a change on a child's branch to what its
umbrella's Intent asks is a finding is stated once, in the shared
reference beside the premise line, rather than at each site restating
the umbrella's binding clause: an agent's call, confirmed as a contained
amendment at the plan phase and reported in its readout. (Basis:
measured, for the audit's findings; judgment, accepted by the
maintainer, for the line; judgment, an agent's call the maintainer has
not ruled on, for the one home: a contained amendment the agent
confirmed.)

Doubts stopped at the controller. A seat question could be carried to
the readout, but the readout's list had no item for it, and a doubt
about the Intent could be answered or rejected by the Intent's own
author: across the three features the audit read, seat questions were
answered 47 times, adopted 12, rejected once and carried never. Such a
doubt is now always carried, and the readout quotes each carried
question verbatim, so the operator reads the seat's words rather than
the controller's account of them; every other question keeps its four
dispositions. An agent's proposal, which the maintainer accepted.
(Basis: measured; judgment, accepted by the maintainer.)

A branch's prose review once ran two waves of line-wrap fixes, each
seeding the next; with formatting no tool enforces out of scope, ragged
lines cost nothing (2026-10-07). (Basis: a single incident.)

### Evidence on the author's side

A classification on 2026-08-27 of about 1,620 findings from the 24
feature records then committed, 6 in crucible and 18 in one other
project, found where review effort went: about 40% of findings corrected
a false, mechanically checkable claim about code, files or tools that
the author could have checked when writing; about 29% surfaced consumers
or producers the author never enumerated; about 19%, and 60 to 90% of
findings from round 2 on in the three campaigns instrumented for it,
were introduced by fix waves, mostly a fix landing at one site while a
sibling statement stood. Only 14% were the design judgments a panel
exists for. Seats were held to evidence; the authors and fixers writing
what they review were not. Of 16 findings that overturned or attacked a
ratified decision or a recorded ruling, 15 overturned either a decision
ratified on a factual premise its author supplied and got wrong, or an
adjudication ruling: an unverified fact in a decision ask is how false
premises reach the operator's rulings. (Basis: measured.) The consumer
sweep that answers the second class is part of the spec contract
(`docs/decisions/the-spec.md`).

The rules shipped as prose, with `UNVERIFIED` the only marker and no
tiers of verified, inferred or guessed. A lint for untagged code-shaped
claims waits until the prose rules are seen eroding
(`docs/backlog/claims-lint-untagged-code-claims.md`), a deferral the
maintainer ratified on 2026-08-27. (Basis: judgment, accepted by the
maintainer.)

The propagation sweep finds the sites that restate what a fix changes;
it does not follow the change to what consumes it. In the audit below,
6 of the 10 clusters of lost or unseen findings began with a fix wave
that created the defect while nothing traced its consequences. From
2026-10-30 each fix item that adds or changes a rule takes
brainstorming's consumer sweep and trace before the list freezes, a
seat's suggested wording being a proposal traced like the controller's
own, and what the trace finds lands as restating sites, which the blind
verifier already checks, with no new record field. Execution's waves
are left out by choice: each is followed by a scoped re-review and, at
the branch review, a full-scope pass, while a campaign's last wave is
read only by the verifier and the terminal pass. The trace adds a little
work to every fix list of every feature, which word counts do not show.
An agent's proposal, which the maintainer accepted. (Basis: measured,
for the clusters; judgment, accepted by the maintainer, for the rule.)

### Evidence before claims

Upstream's verification-before-completion skill requires fresh
verification evidence before any claim of success or completion, and
before a commit or the next task: "Evidence before claims, always"
(`superpowers/skills/verification-before-completion/SKILL.md`).
Crucible keeps that as one always-loaded line in the router, added on
2026-10-07, instead of a skill that has to trigger, and each seat states
its own checks; SDD's Finish runs the full suite or the project's
declared merge gate on HEAD (`crucible:subagent-driven-development
§ Finish`). The maintainer confirmed that reason on 2026-10-20; whether
crucible's checks cover upstream's table of common failures is still to
be compared (`docs/upstream.md`). (Basis: external, for upstream;
judgment, accepted by the maintainer.)

Fix items whose substance was a check were twice recorded applied with
nobody having run them (2026-08-21 and 2026-09-24), and a check that
cannot fail on today's tree shows nothing about whether it can fire.
On 2026-10-05 the maintainer ruled that only the part of that item its
evidence supported should land. (Basis: measured; the maintainer's
preference, for the scope.)

Twice an implementer acted on a suite outcome no tool had shown it while
the output file it watched was still empty, which is why a result now
comes from the run's own output (2026-10-14). The rule binds the
implementer alone, the seat the focused-check rule leaves to the full
suite (`docs/decisions/spec-campaign.md`); controllers have the router's
line. (Basis: measured; judgment, accepted by the maintainer,
for the scope.)

### What the requirements leave unsaid

The four rules came from superpowers releases v6.4.1 to v7.0.1, adopted
at the review of that range
(`docs/crucible/2026-10-27-upstream-review/dispositions.md`). Upstream
also had brainstorming record which choices the person made and which
the agent made; the maintainer declined it, since a mark saying the
operator decided invites deference to the choice, and took the seats'
clause in its place, which asks for the missing decision instead.
(Basis: external; judgment, accepted by the maintainer.) The premise
line of 2026-10-29, keyed on who proposed a decision, undid that decline
in effect, and since 2026-10-30 no rule routes on the proposer
(§ Premise findings, the goal check and questions).

The clause asking for a missing decision, and the one that a binding
item is itself wrong, sat in the redteam seat's template alone, so the
branch reviewer had neither (the audit below). On 2026-10-30 both moved
to a section of the shared reference that the redteam seat, the
terminal pass and the branch reviewer read; for the branch reviewer the
missing decision is one the code makes. The task reviewer's and the
implementer's templates do not name the section, so the rejection of a
premise-finding mandate for task reviewers stands (§ Rejected). An
agent's proposal, which the maintainer accepted. (Basis: measured, for
the gap; judgment, accepted by the maintainer, for the move.)

### The audit of the hypothesis-specs umbrella

The umbrella shipped three features through the full process. At the
maintainer's request (2026-10-29), five fresh auditors read the shipped
tree blind to the review records, and two more traced each finding back
through the records. Of 23 distinct correctness findings, 11 had been
raised during development and lost (6 dropped, 3 dismissed, 2 "fixed"
into the defect) and 12 were never seen. Grouped into 10 clusters, the
misses had five patterns: a fix wave created the defect and nothing
traced its consequences (6 of 10); findings arrived after a batched
landing approval, were handed over only in chat and were lost when
Finish deleted the ledger (4); reviewers read the diff, not the
unchanged text it contradicts (5); nothing read across the children
(5); and the operator's approvals were in no reviewer's inputs (4). The
records that cite "the audit" draw on these figures. (Basis: measured.)

## Rejected

- **Tiers of certainty** beside `UNVERIFIED` (§ Why).
- **A lint for untagged code-shaped claims**, until the prose rules are
  seen eroding (§ Why).
- **Recording a predicate's result both before and after the change**,
  with a written argument that it is not vacuous: the rule that it must
  fail first carries both (2026-10-05).
- **A premise-finding mandate for task reviewers**: on code the
  differential probe found the task review's rubric hiding nothing, and
  on prose the catches it missed were things the rubric neither asks for
  nor forbids, which `Questions`, the default role and the decision-record
  basis check cover (§ Why).
- **Improvements as findings**: a finding can open a fix wave, and an
  improvement never does by itself (§ Why).
- **A premise line keyed on a decision's proposer**, the form of
  2026-10-29: seats cannot see the proposer, and it undid the declined
  mark of who decided (§ Why).

## Changes

- 2026-11-02: a mark no longer appears among the binding items shown
  wrong that keep their own route: `[LOAD-BEARING]` marks are retired
  (`docs/decisions/the-spec.md`).
- 2026-11-01: the goal check reads the request from the feature
  workspace's `request.md`, named in the seat's dispatch, no longer from
  a section of the document; an umbrella child's seats compare the goal
  its own request asks for with its Intent, the umbrella's Intent and
  its entry; because the
  quoted request in committed feature folders published the operator's
  messages.
- 2026-10-30: a premise finding protects the request, what the Intent
  asks for and firm decisions, readable from the document, every other
  decision being lightly held whoever proposed it, and the controller
  corrects a mislabel in either direction; this reverses the 2026-10-29
  line by who stands behind a decision, which had undone the declined
  attribution mark, and that decline holds again; a doubt about the
  request, the Intent or a firm decision is always carried to the
  readout, quoted verbatim; adopted improvements, rulings and requested
  work ride a branch-review wave as labelled changes, applied or
  declined, an improvement opening none but the cleanup wave; each fix
  item that adds or changes a rule is traced before its list freezes;
  the binding-item and unrecorded-choice clauses moved to the shared
  reference, reaching the branch reviewer and the terminal pass; after
  an audit of the hypothesis-specs umbrella. The one home's basis is
  labelled an agent's call the maintainer has not ruled on. The
  terminal pass and an umbrella's closing-review seats are named among
  the seats that raise premise findings, as the shared reference names
  them.
- 2026-10-29: premise findings, the goal check and a widened `Questions`
  section: a seat may claim that the operator's premise is wrong, as a
  decision ask that holds no gate; a premise finding's location is the
  passage it contradicts; improvements stay out of findings and go in
  `Questions`, an adopted one riding the next fix wave; after the
  maintainer's request and two probes.
- 2026-10-27: what the requirements leave unsaid: the execution
  reviewers grade a failure on an implied input by its effect on a
  reasonable person, seats report an unrecorded consequential choice,
  the implementer names every failing test, and the task reviewer and
  re-reviewer re-read evidence that looks truncated; adopted from
  upstream at the v7.0.1 review.
- 2026-10-14: evidence before claims: a completion claim rests on a check
  run, a predicate fix is run and must fail before its change, and a test
  result comes from the run's own output, unknown until read.
- 2026-10-07: finding hygiene: staked severity, a BLOCKER without
  evidence is a question, campaign seats' code claims run or tagged
  `UNVERIFIED` and kept out of fix lists, and improvements, style and
  unenforced formatting not findings.
- 2026-08-27: evidence on the author's side: claims checked when written,
  record hygiene for the controller and the implementer, and the
  propagation sweep before a fix list freezes.
