# Umbrellas

## Decision

**One document per effort.** An effort too large for one feature is held
by an umbrella: `umbrella.md` in a feature folder of its own, a spec of
its own kind written under the spec contract's sections, whose
Acceptance is the ordered list of its children, each entry saying what
that child delivers, what it waits on, and whether it has landed. A
child that splits becomes an umbrella itself, at any depth; every
child's folder is born at the root like any feature's, and the list is
the index (`skills/brainstorming/references/umbrellas.md` § Shape).

**Reviewed by what it carries, on no route.** An umbrella takes none of
the three routes (`docs/decisions/routes.md`). One that carries
decisions, constraints or interfaces gets a spec campaign; one that only
orders its children and states their obligations is approved by the
operator as a lane note is. Brainstorming proposes which and the
operator rules. No umbrella has a plan or execution of its own: its
children carry both (`skills/brainstorming/references/umbrellas.md`
§ Review).

**Binding through one line.** A child names its umbrella in a line of
its preamble, and through that line its own entry and the umbrella's
binding content bind it, up the chain of umbrellas, each read where it
lives (`skills/brainstorming/references/umbrellas.md` § Children).
Every statement of what binds, in the skills and the seat templates,
names the umbrella; that clause is the one rule of the umbrella that
crucible's text states at each of its sites rather than once.

**Edited by weight until it closes.** Lightly held edits travel on a
child's branch. A binding change never does: it goes to the operator,
lands on a branch of its own, and each child in flight takes it in from
the base (`skills/brainstorming/references/umbrellas.md` § Edits;
`skills/redteaming/references/flip-paths.md` § Under an umbrella:
binding changes and late splits).

**Marks, not derived state.** Each entry carries its own mark, `landed`,
`umbrella` or `dropped`, and a child writes its own `landed` in the
commit that lands it (`skills/brainstorming/references/umbrellas.md`
§ Marks; `crucible:subagent-driven-development § Finish`). An umbrella
has closed when its marks say so, read down the chain; from then it is
frozen (`skills/brainstorming/references/umbrellas.md` § Closing).

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
please"). One flat umbrella holding a whole tree would also grow toward
the append-only parent's size, and any depth cap would have broken on
the four-level case. (Basis: the maintainer's preference, 2026-10-27.)

Folders stay flat because children born inside their umbrella's folder
would rewrite the birth and resolve steps every route uses, and a child
that existed before its umbrella could never sit there. The maintainer
had first proposed nesting the folders too; the spec's campaign
reversed that for these reasons, and the maintainer accepted the
reversal. (Basis: judgment, accepted by the maintainer, reversing the
maintainer's own earlier proposal, 2026-10-27.)

### Review by content

The split follows the line the routes draw: a design decision worth
reviewing gets a campaign, and a document without one is approved as a
lane note is (`docs/decisions/routes.md`). An umbrella's decisions,
constraints and interfaces bind every child under it; an umbrella
without them holds an order and its children's obligations, whose
checks each child's own Acceptance carries. The ruling is made at the
umbrella's birth, and a later binding change is ruled on by itself. The
maintainer chose this from an agent's options, the others being a
campaign for every umbrella and a campaign for none. (Basis: judgment,
accepted by the maintainer, 2026-10-27.)

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
reviewed range, the child's own mark and a binding change taken in from
the base are not findings: the mark is the one edit to its entry a child
is meant to make, and the binding change reached the base on the
operator's ruling. (Basis: judgment, accepted by the maintainer; the
last point on 2026-10-28.)

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
judgment, an agent's proposal not yet accepted by the maintainer.)

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
(Basis: judgment, an agent's proposal not yet accepted by the
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

## Changes

- 2026-10-28: umbrellas: one committed document per effort of several
  features, reviewed by what it carries, binding its children through a
  preamble line named at every statement of what binds, edited by
  weight, marked per entry and closed by its marks; it replaces
  improvised forms that left the reader merging texts.
- 2026-10-28: a child in branch review takes in a binding change before
  each pass and wave, and the slug match is limited to features born on
  a tree without the umbrella; the branch review found both gaps.
