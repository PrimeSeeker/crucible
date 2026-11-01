# Umbrellas

## Decision

**One document per effort.** An effort too large for one feature is held
by an umbrella: `umbrella.md` in a feature folder of its own, a spec of
its own kind written under the spec contract's sections, whose
Acceptance is the ordered list of its children, each entry saying what
that child delivers, what it waits on, and whether it has landed. A
child that splits becomes an umbrella itself, at any depth; every
child's folder is born at the root like any feature's, and the list is
the index. Like a spec, it quotes no message from the operator: the
effort's request lives in the umbrella's workspace and goes with it at
the landing, and a child's request holds only the messages of its own
brainstorm, so a child's seats check its Intent against that request,
the umbrella's Intent and its own entry (`docs/decisions/the-spec.md`).

**Reviewed by what it carries, on no route.** An umbrella takes none of
the three presets (`docs/decisions/routes.md`). One that carries
decisions, constraints or interfaces gets a spec campaign; one that only
orders its children and states their obligations is approved by the
operator as a lane note is. Brainstorming proposes which and the
operator rules. No umbrella has a plan or execution of its own: its
children carry both (`skills/brainstorming/references/umbrellas.md`
§ Review).

**Binding through one line.** A child names its umbrella in a line of
its preamble, and through that line its own entry and the umbrella's
binding content, its Constraints & invariants and the decisions it
records as the operator's firm preference, bind it, up the chain of
umbrellas, each read where it lives
(`skills/brainstorming/references/umbrellas.md` § Children).
Every statement of what binds, in the skills and the seat templates,
names the umbrella; that clause is the one rule of the umbrella that
crucible's text states at each of its sites rather than once. The rule
for the umbrella's Intent is the exception that joins none of those
statements: the Intent is protected as the child's own is, a seat
raising a premise finding against what it asks, and a change on a
child's branch to what it asks is a finding; both are stated once, in
the shared reference beside the premise line, which § Children points
to (`skills/subagent-driven-development/references/premise-and-questions.md`
§ Premise findings).

**Edited by weight until it closes.** Lightly held edits travel on a
child's branch, a correction to the umbrella's Intent among them only
where it leaves what the Intent asks for unchanged. A binding change, a
change to a firm decision or to what the Intent asks for included,
never does: it goes to the operator, lands on a branch of its own, and
each child in flight takes it in from the base
(`skills/brainstorming/references/umbrellas.md` § Edits;
`skills/redteaming/references/flip-paths.md` § Under an umbrella:
binding changes and late splits). A child's controller never confirms a
change to umbrella content itself, however contained the change looks
(`skills/redteaming/references/flip-paths.md` § The containment test).

**Marks, not derived state.** Each entry carries its own mark, `landed`,
`umbrella` or `dropped`, and a child writes its own `landed` in the
commit that lands it (`skills/brainstorming/references/umbrellas.md`
§ Marks; `crucible:subagent-driven-development § Finish`). An umbrella
has closed when its marks say so, read down the chain; from then it is
frozen (`skills/brainstorming/references/umbrellas.md` § Closing).

**One closing review, a step and not a gate.** Once an umbrella is
complete by its marks, one review reads its children's landings, from
the umbrella's own to the one that completed it, unrelated landings on
a shared base aside, against the umbrella: its Intent, its entries,
its Constraints & invariants and its decisions. The controller whose
landing completes it, a landed drop included, announces it and runs it
right after; its width is that controller's call, the review itself is
not optional; where a child's landing completes it, that child's close
readout names it as the step after the landing. Where the completing
landing may happen outside a session, the close readout of each child
whose landing could complete the umbrella says the review is due once
they have all landed, and the operator starts it by asking. A nested
umbrella's review runs at its own completion and, where that completes
its parent, before the parent's, whose range covers it again. It takes two or three seats the
controller composes on the default role, read-only, each with a lens
that reads across children (fidelity to the umbrella's Intent, the seams between
children, a walkthrough of the workflows the effort changed), with no
instrument or template of its own. Its readout proposes keeping or
dropping each finding, a premise finding being a decision ask there,
and, where the project's instructions name no home for open items,
asks where the findings kept go; after the answer, the findings kept
and each premise finding with its ruling go to the project's home or
the one the answer named, an in-repository one's committed on a branch
of its own landed on the operator's go-ahead; where nothing is kept and
no premise finding was raised, nothing is written and the readout names
each finding dropped. Closing is still read from the
marks, nothing waits on the review, and it writes nothing into
`umbrella.md`; a feature that fixes its findings is a feature of its
own. An umbrella approved without a campaign takes it too
(`skills/brainstorming/references/umbrellas.md` § Closing review).

**An open premise ask at the landing.** A premise finding still open
when an umbrella lands goes to the operator with the landing ask, and
the landing never waits on it. With no ledger to hold it, it is noted
in the first entry with no mark in the umbrella's Children list, as
`open premise ask: <the ask>`; that child's brainstorm takes it into its
decision record, with the operator's ruling where one has come since or
else as open for its dialogue, and the child removes the note as a
clarification its spec states (`skills/brainstorming/references/umbrellas.md`
§ Landing, § Children; `skills/redteaming/references/flip-paths.md`
§ Premise findings).

**Work left open at the landing.** An umbrella has no ledger, so what
its brainstorm and campaign left open goes at its landing, each item
with its source, to the home the project's instructions name for open
items, an in-repository one's committed on its branch; where they name
none, the landing ask asks where the items go or whether to drop them,
with the offer to record the answer, and the workspace is not deleted
before it. Where nothing was left open, nothing is asked or written
(`skills/brainstorming/references/umbrellas.md` § Landing;
`docs/decisions/records-and-workspace.md`).

**Kept in the merged tree.** An umbrella's own pull request never
offers `umbrella.md` for removal; the trade-off is in
`docs/decisions/records-and-workspace.md`.

## Why

### One file, read in its current state

Before umbrellas, efforts that needed one improvised it, in three
shapes. A parent spec went through its own campaign, and each child spec
then carried a section of amendments to it; the parent's current state
was the original plus every child's amendments, read together. A parent
of about 24,600 words gained one appended addendum per child, seven in
all, and its levels ran four deep, the middle two with no document of
their own: a backlog item and a decision record stood in for them.
Crucible's own publication was planned in a backlog item of about 5,200
words that grew into a progress log, with the rest in agent memory,
which no seat is directed to and which cannot be committed under
`AGENTS.md`'s no-local-context rule. In each, the reader rebuilt the
current state by merging texts. (Basis: measured, by reading the
documents of crucible's own runs and of one other project crucible ran
on.)

The maintainer asked for umbrellas, having seen two of these patterns
in their own efforts: a parent spec with child specs under it, and
phases whose later requirements were held by earlier specs together
with agent memory. (Basis: the maintainer's preference.)

An umbrella edited in place holds the effort's current state in one
file, the same choice the decision records made against an append-only
log (`docs/decisions/decision-records.md`). The maintainer chose it
from three options an agent proposed, the other two being a frozen
parent amended from its children and a frozen parent plus an amendment
log. It closes and freezes like a shipped spec once nothing under it is
open. (Basis: judgment, accepted by the maintainer, 2026-10-27.)

### Recursion and flat folders

Recursion is the maintainer's: their efforts "tend to have
subphases-of-subphases", and they asked for it ("Yes, recursive,
please"). (Basis: the maintainer's preference, 2026-10-27.) One flat
umbrella holding a whole tree would also grow toward the append-only
parent's size, and any depth cap would have broken on the four-level
case: the reasons the umbrella-specs spec gave for rejecting both,
which the maintainer accepted with it. (Basis: judgment, accepted by
the maintainer, 2026-10-27.)

Folders stay flat because children born inside their umbrella's folder
would rewrite the birth and resolve steps every route uses, and a child
that existed before its umbrella could never sit there. The maintainer
had first proposed nesting the folders too; the spec's campaign
reversed that for these reasons, and the maintainer accepted the
reversal. (Basis: judgment, accepted by the maintainer, reversing the
maintainer's own earlier proposal, 2026-10-27.)

### Review by content

An umbrella's decisions, constraints and interfaces bind every child
under it, so one that carries them gets a campaign; an umbrella without
them holds an order and its children's obligations, whose checks each
child's own Acceptance carries, and is approved as a lane note is. The
ruling is made at the umbrella's birth, and a later binding change is
ruled on by itself. The maintainer chose this from an agent's options,
the others being a campaign for every umbrella and a campaign for none.
(Basis: judgment, accepted by the maintainer, 2026-10-27.)

The split first followed the line the routes then drew, by whether a
design decision deserved review before code. When the overturn question
replaced that line for features (`docs/decisions/routes.md`), it did not
take over here: it asks whether overturning a major mechanism after code
is reasonably expected, and an umbrella has no code of its own, so its
review stays chosen by its content. Once an umbrella's campaign runs,
the question stops it as any campaign's, read against its children's
code
(`skills/subagent-driven-development/references/premise-and-questions.md`
§ The arrangement questions). (Basis: judgment, accepted by the
maintainer, 2026-10-29.)

### The line, and what binds

A child is bound only through its line, read by each seat in its own
worktree, never through content restated in the child. Asked during the
spec's campaign, the maintainer ruled for the line: "restatement is a
drift invitation", the same reason requirements travel by pointer
(`docs/decisions/the-spec.md`); and checking a child's compliance with
its umbrella is "probably valuable". (Basis: the maintainer's
preference, 2026-10-27.)

The line names a path and no revision, so the plan header keeps its
single pin: the plan pins the spec, and the spec's preamble carries the
line. A seat treats as binding only what the statement it was handed
names, so a statement that left the umbrella out would leave that seat
reviewing without it; hence the clause at every statement. Within a
reviewed range, the child's own mark, a clarification its spec states
that changes nothing another entry waits on, and a binding change taken
in from the base are not findings: the mark and such a clarification
are the edits to its entry a child is meant to make, and the binding
change reached the base on the operator's ruling. (Basis: judgment,
accepted by the maintainer; the last point on 2026-10-28.)

An umbrella records the operator's firm preferences as a spec does
(`docs/decisions/the-spec.md`), so its firm decisions bind its children
too, and changing one is a binding change: as a lightly held edit it
could otherwise travel on one child's branch. Umbrella content stays
outside what a child's controller may confirm as a contained amendment,
keeping the decision ask it had. (Basis: judgment, accepted by the
maintainer, 2026-10-28.)

Until 2026-10-30 a child could edit the umbrella's Intent on its own
branch as a lightly held edit. Since then a premise finding protects
what a seat can read for itself, the request, what the Intent asks for
and firm decisions (`docs/decisions/evidence-and-findings.md`). For a
child, the umbrella's Intent counts as its own, so no child's branch
changes what the effort asks for without the operator. A
correction that leaves what the Intent asks unchanged stays a lightly
held edit; a change to what it asks is a binding change. (Basis: judgment, accepted by the maintainer.)

As the spec campaign first wrote that rule, it joined the binding
clause at each of the clause's sites. The plan phase counted thirteen
skill sites, several in no task's file list, and its controller
confirmed a contained amendment giving the rule one home, in the shared
reference beside the premise line, which § Children points to; the
restated clause itself is the skill-text rewrite's to collapse
(`docs/backlog/skill-text-rewrite.md`). (Basis: judgment, an agent's
call the maintainer has not ruled on: a contained amendment the agent
confirmed.)

### Binding changes off the child's branch

A binding change made on one child's branch would reach the base, and
that child's siblings, only when that child lands. Landed at once on its
own branch, with the operator approving its diff, it is on the base each
child in flight takes in at its next task or round boundary, before that
boundary's base revision is recorded, so it falls outside the range the
child's next review reads. Children take it in by a merge, since a
rebase would rewrite revisions their records name. (Basis: judgment,
accepted by the maintainer, 2026-10-27.)
A child in its branch review has no task or round left, so the same
check runs before each full-scope pass and fix wave, and the branch
review's range is then measured from the recomputed merge base. (Basis:
judgment, accepted by the maintainer, 2026-10-28.)

### Marks

State derived from which folders and branches exist misreads three
cases: a nested umbrella's landing, an unrelated feature taking a
child's slug, and a drop riding a branch that never lands. A mark
written by the child itself lands with the child, touches only its own
entry, and the blank line between entries keeps siblings' marks from
conflicting in git. Closing is read from the marks, recursively, so it
takes no write of its own up the chain. A child
already in flight when its umbrella is written carries no line, so its
finish finds its entry by its slug instead (2026-10-28). (Basis:
judgment, accepted by the maintainer.) A slug alone could match an
unrelated feature born after the umbrella, so the finish marks only
where the feature's folder was born on a tree without the umbrella.
(Basis: judgment, accepted by the maintainer, 2026-10-28.)

### An open premise ask at the landing

A premise finding holds no gate (`docs/decisions/evidence-and-findings.md`),
so an umbrella's landing, which every child waits on, never waits for
one. An umbrella has no ledger, its workspace is deleted at the landing,
and a release usually separates the landing from the first child's
session, so the ask is kept in that child's entry, in the merged tree
its brainstorm reads as the incoming document. A first form gave the
entry a carrier of its own, which a task review found conflicting with
the marks, the resume step and the edit rules, and leaving the ask no
exit; as a note the child removes by the clarification it may already
make, it adds no kind of edit. A ruling the operator gives between the
landing and that brainstorm is written nowhere until the child's
decision record takes it in. (Basis: judgment, accepted by the
maintainer, 2026-10-29.)

### Work left open at the landing

An umbrella has no ledger, and its workspace is deleted at its landing,
so what its brainstorm and campaign left open would otherwise have no
durable home, and no deferral counts as done until it has one
(`docs/decisions/records-and-workspace.md`). It goes where a
feature's goes, and so do the closing review's findings kept. (Basis:
judgment, accepted by the maintainer.) Until 2026-11-01 that was an
`open-items.md` in the umbrella's folder, the one file a closed
umbrella's folder gained; the maintainer judged that a feature's open
items stored in such a file "are definitely going to be lost"
(2026-10-30), and the maintainer's brainstorm of 2026-11-01 replaced
the file with the project's own home or, where none is named, the
operator's answer (`docs/decisions/records-and-workspace.md` § Work
left open). A closed umbrella's folder now gains nothing. (Basis: the
maintainer's preference.)

### The closing review

Each child's branch review grades that child against its own plan, and
the audit found that nothing read across the children, in 5 of its 10
clusters of lost or unseen findings
(`docs/decisions/evidence-and-findings.md` § The audit of the
hypothesis-specs umbrella). The controller first proposed widening the
last child's branch review; the maintainer asked instead, "Might be
worth a separate wider review?", and accepted the form the controller
then detailed. A widened child review would also have mixed its
siblings' defects into its own wave cap. (Basis: measured, for the
audit; the maintainer's preference, for a separate review; judgment,
accepted by the maintainer, for its form.)

At the spec campaign's first round the maintainer accepted making the
review a step after the last landing rather than a gate before the
umbrella is marked closed. That ask overstated a gate's cost: the step
has since gained the recursive completion rule and the written-down
findings, so a gate would add only a landing ask where the review
finds nothing and a check on resume, against a step that can be
skipped where a landing happens outside a session and nobody acts on
the readout. Put back on that trade-off after the campaign, the
maintainer left the choice to the controller, which kept the step; a
session resuming the effort is pointed to the review. (Basis:
judgment, accepted by the maintainer, for the step; the final choice a
call the maintainer left to the agent.)

The form the maintainer accepted at the brainstorm had one seat on the
other host. The spec campaign's round 0 found that no skill composes
such a seat, and its fix dropped the seat from the shipped default,
naming the drop in that round's readout: a seat on the other host is
the operator's own instruction where it applies, and the skills compose
none (`docs/backlog/second-runtime-seat.md`). (Basis: judgment, an
agent's call the maintainer has not ruled on: a fix in the spec
campaign's round 0, named in that round's readout and departing from a
detail of the form the maintainer accepted.)

## Rejected

- **A frozen parent amended from its children**, and **a frozen parent
  plus an amendment log**: both leave the reader merging texts (§ Why).
- **One flat umbrella for the whole tree**, and **a depth cap** (§ Why).
- **Children's folders inside their umbrella's** (§ Why).
- **State derived from folders and branches** (§ Why).
- **A changelog in the umbrella**: git history and the children's specs
  record what changed.
- **An effort's plan held in a backlog item or in agent memory**: the
  improvised form this record replaces (§ Why).
- **Widening the last child's branch review** to read the whole effort:
  it grades against that child's plan and would spend that child's wave
  cap on its siblings' defects (§ Why).
- **The closing review as a gate** before the umbrella is marked
  closed: it would add a landing ask where the review finds nothing and
  a check on resume (§ Why).

## Changes

- 2026-11-02: the umbrella's binding content no longer includes
  `[LOAD-BEARING]` marks, which are retired: what binds a child is its
  entry and the umbrella's Constraints & invariants and firm decisions;
  the entry marks (`landed`, `umbrella`, `dropped`) stay.
- 2026-11-01: the umbrella quotes no request; the effort's request
  lives in the umbrella's workspace and is deleted at its landing, a
  child's request holds only its own brainstorm's messages, and the
  closing review reads fidelity to the umbrella's Intent; because the
  quoted request in committed feature folders published the operator's
  messages (`docs/decisions/the-spec.md`).
- 2026-11-01: an umbrella's landing and its closing review send their
  open items to the project's home for them or, with none named, where
  the operator's answer sends them, the workspace kept until it comes;
  the closing review no longer writes the findings dropped; a closed
  umbrella's folder gains nothing. The maintainer's brainstorm retired
  the default `open-items.md`
  (`docs/decisions/records-and-workspace.md`).
- 2026-11-01: § Work left open at the landing names the maintainer's
  2026-10-30 view that a feature's open items kept in its folder's file
  will be lost, a default this file follows, and points to the backlog
  item that held the question; the record had given the default as
  accepted without the maintainer's later doubt.
- 2026-10-30: an umbrella gets one closing review across its children's
  landings, a step after the landing that completes it and not a gate,
  its findings kept or dropped at its readout and written to the
  umbrella folder's `open-items.md`, the one file a closed umbrella's
  folder gains; the umbrella's landing writes what its brainstorm and
  campaign left open to that file; the umbrella's Intent is protected
  as a child's own, a correction to it travelling as a lightly held edit
  only where it leaves what the Intent asks unchanged, and that rule is
  stated once, the exception to the binding clause stated at each site;
  the overturn question reads "reasonably expected". The audit of the
  hypothesis-specs umbrella found nothing reading across children, and
  the maintainer asked for a separate wider review. The one home's and
  the dropped other-host seat's bases are labelled agents' calls the
  maintainer has not ruled on.
- 2026-10-29: review by content no longer rests on the routes' retired
  "worth reviewing" line: the overturn question selects a feature's
  review, and an umbrella, with no code of its own, keeps review by
  content, its campaign stopped by the question read against its
  children's code.
- 2026-10-29: the basis of the open premise ask's note at the landing
  reads judgment, accepted by the maintainer, no longer an agent's
  call: the maintainer accepted the call.
- 2026-10-29: the umbrella's Request, which a child's points to, so a
  child's seats check its Intent against the effort's request; a
  premise finding open at the landing goes to the operator with the
  landing ask and is noted in the first unmarked entry until that child
  takes it up, since an umbrella has no ledger to carry it.
- 2026-10-29: a clarification its spec states is named beside the mark
  as an edit a child makes to its entry, and the recursion paragraph's
  basis is split between the maintainer's preference and the spec's
  reasoning; a probe found both misstated.
- 2026-10-28: an umbrella's firm decisions bind its children and
  changing one is a binding change; a child's controller never confirms
  a change to umbrella content as a contained amendment.
- 2026-10-28: umbrellas: one committed document per effort of several
  features, reviewed by what it carries, binding its children through a
  preamble line named at every statement of what binds, edited by
  weight, marked per entry and closed by its marks; it replaces
  improvised forms that left the reader merging texts.
- 2026-10-28: a child in branch review takes in a binding change before
  each pass and wave, and the slug match is limited to features born on
  a tree without the umbrella; the branch review found both gaps.
- 2026-10-28: the maintainer accepted the branch-review intake and the
  slug-match limit; their bases now say so.
