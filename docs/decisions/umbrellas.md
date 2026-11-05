# Umbrellas

## Decision

**One document per effort.** An effort too large for one feature is held by an umbrella: `umbrella.md` in a feature folder of its own, a spec of its own kind whose Acceptance is the ordered list of its children. A child that splits becomes an umbrella itself, at any depth, and every child's folder is born at the root (`skills/brainstorming/references/umbrellas.md` § Shape). Like a spec, it quotes no message from the operator: the effort's request goes with the umbrella's workspace at the landing, and a child's seats check its Intent against its own request, the umbrella's Intent and its own entry (`docs/decisions/the-spec.md`; `skills/subagent-driven-development/references/seat-rules.md` § The goal check).

**Reviewed by what it carries, on no route.** An umbrella takes none of the three presets (`docs/decisions/routes.md`). One that carries decisions, constraints or interfaces gets a spec campaign, one that only orders its children and states their obligations is approved by the operator as a lane note is, and no umbrella has a plan or execution of its own (`skills/brainstorming/references/umbrellas.md` § Review).

**Binding through one line.** A child names its umbrella in a line of its preamble, and through that line its own entry and the umbrella's Constraints & invariants and firm decisions bind it, up the chain of umbrellas, each read where it lives (`skills/brainstorming/references/umbrella-children.md` § Children). What binds, the umbrella included, is stated once for controllers (`skills/subagent-driven-development/references/review-terms.md` § What binds in a spec) and once for seats, by splice (`skills/subagent-driven-development/references/seat-rules.md` § What binds). The umbrella's Intent is protected as the child's own is (`skills/subagent-driven-development/references/seat-rules.md` § Premise findings, § Binding changes).

**Edited by weight until it closes.** Lightly held edits ride a child's branch; a binding change, to a firm decision or to what the Intent asks for included, goes to the operator and lands on a branch of its own, and a child's controller never confirms a change to umbrella content itself, however contained it looks (`skills/brainstorming/references/umbrella-children.md` § Edits and § Under an umbrella; `skills/redteaming/references/flip-paths.md` § The containment test).

**Marks, not derived state.** Each entry carries its own mark, a child writing its own `landed` in the commit that lands it, and an umbrella has closed when its marks say so, read down the chain; from then it is frozen (`skills/brainstorming/references/umbrella-children.md` § Marks; `skills/brainstorming/references/umbrellas.md` § Closing).

**One closing review, a step and not a gate.** Once an umbrella is complete by its marks, one review reads its children's landings against the umbrella, its seats composed by the controller with no instrument or template of their own. It is a step after the last landing: closing is still read from the marks, nothing waits on it, it writes nothing into `umbrella.md`, and a feature that fixes its findings is a feature of its own (`skills/brainstorming/references/umbrellas.md` § Closing review).

**An open premise ask at the landing.** A premise finding still open when an umbrella lands goes to the operator with the landing ask, and the landing never waits on it. With no ledger to hold it, it is noted in the first entry with no mark in the umbrella's Children list, for that child's brainstorm to take into its decision record (`skills/brainstorming/references/umbrellas.md` § Landing; `skills/brainstorming/references/umbrella-children.md` § Children; `skills/redteaming/references/premise-asks.md` § Premise findings).

**Work left open at the landing.** An umbrella has no ledger, so what its brainstorm and campaign left open goes at its landing to the home the project's instructions name for open items, or where the landing ask's answer sends it, and a decision ask unruled there, a premise ask aside, goes with those items (`skills/brainstorming/references/umbrellas.md` § Landing; `docs/decisions/records-and-workspace.md`). The premise note is the only note a landing writes into a Children entry.

**Children land on the base.** An umbrella's children land on the base as each finishes, so the base can hold part of an effort; what a landing breaks is stated as any feature's is (`docs/decisions/the-spec.md`), and an umbrella's proposal says whether its children can land without one (`skills/brainstorming/references/umbrellas.md` § Shape).

**Kept in the merged tree.** An umbrella's own pull request never offers `umbrella.md` for removal; the trade-off is in `docs/decisions/records-and-workspace.md`.

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
(`skills/subagent-driven-development/references/review-terms.md`
§ An umbrella's overturn question). (Basis: judgment, accepted by the
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
reviewing without it; hence, until 2026-11-02, the clause at every
statement. Within a
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
reference beside the premise line, which § Children points to. (Basis:
judgment, an agent's call the maintainer has not ruled on: a contained
amendment the agent confirmed.)

The restated clause itself was collapsed on 2026-11-02: what a child's
seat flags under its umbrella is the whole set § Edits names a binding
change, a change to another started child's entry included, stated for
controllers in § Children and § Edits and for seats once in the shared
seat reference's two statements of what binds, which each template
takes by splice; the controller-side statement of what binds in a spec
is the opening of `skills/redteaming/references/flip-paths.md`, and
other skill sites point to these. The copies had drifted: § Children
had left out another child's entry. (Basis: for the full set, the
controller's proposal, accepted by the maintainer; for the owners, the
controller's design, accepted by the maintainer.)

On 2026-11-03 the controller-side statement moved to `skills/subagent-driven-development/references/review-terms.md` § What binds in a spec, which every route's controller reads from brainstorm on, and the sites that restated what binds, § Children among them, became pointers to it. The seat side became one core, the shared seat reference's § What binds, taken by every seat that reads binding content, beside § Binding changes, which holds what a review seat flags and which the implementer does not take. An agent's proposal, on which the maintainer left the call to the agent. (Basis: judgment, accepted by the maintainer.)

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
conflicting in git, as a line after the list keeps a last entry's mark
from conflicting with an appended child (reproduced in a throwaway
repository, 2026-11-04). Closing is read from the marks, recursively, so it
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

The first design of the skill-text rewrite's `review-retirements`
generalized the premise note to every decision ask open at the landing.
Its campaign narrowed that: an
ask other than a premise one goes to the operator with the landing ask
and, unruled, to the open-items home by the step that already sends
work left open there, where the next child's brainstorm finds it by
reading the home without being bound to take it up; a premise ask,
which questions what the effort asks for, keeps the note its next
child's brainstorm takes up. (Basis: judgment, accepted by the
maintainer, who left both calls to the agent, 2026-11-01.)

### Children land on the base

The maintainer asked whether an incomplete umbrella's children should land
on the base by default at all. This repository's two umbrellas required
each child installed before the next one's brainstorm, which took seven
releases. One effort on another project, before umbrellas, landed about a
dozen features on its base over about two and a half months, with a break
on its base until a late one. A keyword search of its records, not a
full read, found no case of partial work reaching a real run, and the
maintainer reported no practical trouble. So the default stays, and what
changed is that a break gets stated. (Basis: measured, for the counts and
the search; judgment, accepted by the maintainer, 2026-11-04, for keeping
the default.)

An operator who wants an effort off the base can already name another base
(`docs/decisions/worktrees.md`), and picks the means once a break is
stated, so nothing says which. That path has not been run. (Basis:
judgment, accepted by the maintainer, 2026-11-04.)

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
other host. The spec campaign's round 0 found that no skill composed
such a seat, and its fix dropped the seat from the shipped default,
naming the drop in that round's readout: a seat on the other host is
the operator's own instruction where it applies, and this review
composes none. (Basis: judgment, an agent's fix in the spec campaign's
round 0, departing from a detail of the form the maintainer accepted,
and accepted by the maintainer on 2026-11-04.)

The seats' report names open with a fixed `closing-`, so no lens the
controller names can make a basename a host's report-name rules refuse
(`docs/decisions/instruments.md`;
`skills/using-crucible/references/<runtime>-dispatch.md`). (Basis:
judgment, an agent's call the maintainer has not ruled on.)

### Residuals accepted

The branch that added umbrellas left three points open, accepted on
2026-11-05 as they are. A child's `landed` mark is committed at SDD
Finish, after the branch review: a one-word edit, and a review reopened
after Finish reads it. An umbrella approved without a campaign still gets
a workspace and a decision record, which its landing deletes: a small
cost, and they hold the operator's rulings until then. With no home named
for open items, a session ending before the operator says where an
umbrella's items go leaves nothing telling the next session the ask is
pending: the workspace stays, so nothing is lost, and it takes a project
with no home and a session ending at that ask. An agent's proposal, which
the maintainer accepted. (Basis: judgment, accepted by the maintainer.)

Beside the mark, a feature with no umbrella line that marks an entry may
merge the base branch in at Finish, also after the branch review, and the
suite then runs on the merged tree. That stays as it is too. An agent's
proposal, which the maintainer accepted. (Basis: judgment, accepted by the
maintainer.)

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
- **Holding an incomplete umbrella's children off the base by default:**
  no harm is on record, both of this repository's umbrellas needed each
  child landed and installed before the next, and it would cost drift, one
  very large final diff and children other sessions cannot see (§ Why).
- **A dedicated effort-branch path:** a named base already allows it, and
  the operator picks the means once a break is stated (§ Why).

## Changes

- 2026-11-05: three residuals are accepted as they are, an unreviewed `landed` mark, an approval-only umbrella's workspace and a pending open-items ask with no carrier, since each costs little and a fix would add text for a rare case; a late-marking feature's base merge after the branch review stays too.
- 2026-11-05: a closing-review seat's prompt carries its report form, since the sections copied into it send a seat to a report format nothing gave.
- 2026-11-04: the Children list ends on a line of text, because a last entry's mark conflicts in git with an appended child; a seat finds a feature's own entry by its feature folder's slug, which nothing stated.
- 2026-11-04: an umbrella's children keep landing on the base, now weighed against holding them off it; its proposal says whether they can land without a break, and the entry of the child that owes the rest says what it owes. The maintainer asked, and a break is now stated (`docs/decisions/the-spec.md`).
- 2026-11-04: the closing review's dropped seat on the other host is ruled on: the maintainer kept it dropped, leaving it to the operator's own instruction.
- 2026-11-03: the premise-finding route is cited at `skills/redteaming/references/premise-asks.md`, where flip-paths' § Premise findings moved, so a controller handling a premise finding no longer loads the flip paths (`docs/decisions/authoring-crucible.md`).
- 2026-11-03: a feature with no umbrella line keeps at its finish only a trigger, the `git grep` for its slug, and the check that it was in flight when the umbrella was written moves to `skills/brainstorming/references/umbrella-children.md` § Marks; because every route's finish read a procedure that only a child already in flight when its umbrella was written uses.
- 2026-11-03: the umbrellas reference splits by reader: `skills/brainstorming/references/umbrella-children.md` holds § Children, § Edits, § Marks and § Resuming, with flip-paths' § Under an umbrella (raising a late split or a binding change, and taking one in at each boundary), and `skills/brainstorming/references/umbrellas.md` keeps the shape, review, landing, closing and closing review; because a child's controller loaded the whole reference, and flip-paths for one section, to act on the children's side alone (`docs/decisions/authoring-crucible.md`).
- 2026-11-03: what binds is stated once for controllers, in `skills/subagent-driven-development/references/review-terms.md` § What binds in a spec, and once for seats, in the shared seat reference's § What binds, with § Binding changes for what a review seat flags; § Children points to the controller statement; so that the sites restating it share one statement every controller already reads.
- 2026-11-03: a change on a child's branch to what the umbrella's Intent asks is stated for seats in the shared seat reference's § Binding changes, no longer also beside the premise line, and the reading of the overturn question for an umbrella's campaign is cited at its own section; because both sections narrowed to the seats that apply them (`docs/decisions/instruments.md`).
- 2026-11-03: the arrangement questions' citation follows their move from the shared seat reference to `skills/subagent-driven-development/references/review-terms.md`, a reference of their own, so a controller that applies them no longer loads the seat rules.
- 2026-11-02: the clause binding a child through its umbrella line is
  stated once per reader (the umbrellas reference's Children and Edits,
  flip-paths' opening, the shared seat reference), and § Children's
  finding rule names the whole binding-change set, another started
  child's entry included, where its copy had drifted; the closing
  review's report-name prefix keeps its reason here.
- 2026-11-02: the shared seat reference's citations follow its rename
  to `seat-rules.md`.
- 2026-11-02: a decision ask other than a premise ask still open at an
  umbrella's landing goes to the operator with the landing ask and,
  unruled, with the work left open to the open-items home, a ruled one
  leaving those items; the premise note stays the only note in a
  Children entry. The first design's note for every open ask was
  narrowed in its campaign, the maintainer leaving the call to the
  agent.
- 2026-11-02: an umbrella's campaign sends its `deferred-minor`
  entries, the MINORs its fix lists no longer take, with what it left
  open to the landing's open-items step, having no ledger or branch
  review to take them (`docs/decisions/fix-verification-and-merge.md`).
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
