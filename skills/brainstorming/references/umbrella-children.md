### Umbrella children

This file holds an umbrella's children's side; what an umbrella is, and its review, landing and closing, are in `skills/brainstorming/references/umbrellas.md`.

#### Children

A child's brainstorm takes its entry as an incoming document (§ Context gathering): what the entry settles stays settled, and the dialogue asks only what it leaves open. An `open premise ask:` note in the entry (`skills/brainstorming/references/umbrellas.md` § Landing) enters the child's brainstorm decision record, with the operator's ruling where one has come since, or else as open, for the dialogue to take up; the child then removes the note, a clarification its spec states (§ Edits). The child's route is proposed as for any feature.

**The umbrella line.** A child's spec, folded document, lane note or umbrella carries in its preamble one line naming its umbrella's file:

    Umbrella: `docs/crucible/<date>-<effort>/umbrella.md`

What that line makes binding is as `skills/subagent-driven-development/references/review-terms.md` § What binds in a spec states; each seat reads it in its own worktree, never from a copied block. Within the range a seat reviews, a binding change as § Edits defines it is a finding, a change to another started child's entry included; the child's own mark and a clarification of its own entry that its spec states, changing nothing another entry waits on, are not, and neither is a binding change taken in from the base. The umbrella's Intent is protected as the child's own is: `skills/subagent-driven-development/references/seat-rules.md` § Premise findings states what a seat raises against it, and § Binding changes what a change to it on a child's branch is. A child that existed before its umbrella carries no line and is bound by nothing in it. A successor's line is set where the successor is written: `skills/redteaming/references/flip-paths.md` for a supersede or an unfold; after the very-small lane's upgrade hatch, the spec brainstorming writes carries the line the note's preamble carries.

**A split.** A feature found to need splitting before its spec campaign closes removes its spec and writes `umbrella.md` in its place: back to step 4, and a campaign in progress stops. Found later — after its campaign closes, or once its lane note is committed — the split is an operator decision ask, and so is a binding change a child finds its umbrella needs; a child's controller raises either by § Under an umbrella. On a late split, the feature is abandoned and a new umbrella with its own slug takes the work up, listing the abandoned feature by path. In the parent, the new umbrella is entered in the old entry's place, carrying its obligation, and carries the parent's umbrella line; entries that waited on the old one wait on it; the old entry stays, marked `dropped` and naming it. That change to the parent lands as a binding change does (§ Edits).

#### Edits

An umbrella is edited in place until it closes (`skills/brainstorming/references/umbrellas.md` § Closing): by its own campaign's fixes before it lands, and after that by the edits below and the marks of § Marks.

**Lightly held edits ride a child's branch and land with it:**

- adding a child;
- rewording an entry whose child has not started — a child has started once its feature folder is born;
- a child's clarification of its own entry, stated in its spec, that changes nothing another entry waits on;
- corrections to the umbrella's Intent that leave what it asks for unchanged, and edits to its Decisions not firm and its Interfaces & boundaries;
- the child's own mark.

**A binding change** — to the umbrella's Constraints & invariants or firm decisions, to what its Intent asks for, or any other change to a started child's entry — is never made on a child's branch. It is a decision ask to the operator, naming every open umbrella and every child in flight beneath it, at every depth. On the operator's ruling it lands at once on a branch of its own: the operator approves its diff, and it lands through `crucible:finishing-a-development-branch`. Each child in flight then takes it in, or the operator rules that child unaffected, as § Under an umbrella states. Dropping a child, on the operator's word, lands the same way.

#### Marks

Each entry ends with its mark, or with none:

- `landed` — the child marks its own entry on its own branch before its finish, so the mark lands with it; `crucible:subagent-driven-development` § Finish says when.
- `umbrella` — a nested umbrella's entry, marked in its landing (`skills/brainstorming/references/umbrellas.md` § Landing).
- `dropped` — a dropped child's entry, with its reason, or, after a late split, naming the umbrella that took the work up.

An entry with no mark has not landed. A mark touches only its own entry; the blank lines between entries keep siblings' marks from conflicting in git. A child that existed before its umbrella is entered with its mark when the umbrella is written; one still in flight then is entered unmarked and marks its entry at its own finish.

#### Resuming

A session continuing an effort reads its umbrella and takes the first entry with no mark whose dependencies have landed — marked `landed`, or `umbrella` and closed; a `dropped` dependency is the operator's call — descending into an entry marked `umbrella` that is not closed, once its own dependencies have landed, to take its next entry by the same rule. It confirms with the operator that the entry is not in flight elsewhere, then brainstorms it as § Children states. A complete umbrella (`skills/brainstorming/references/umbrellas.md` § Closing) has no entry left to take; what remains of its effort is its closing review (`skills/brainstorming/references/umbrellas.md` § Closing review). What a later part must deliver lives in the umbrella: agent memory holds at most a pointer to it.

#### Under an umbrella

Which of an umbrella's edits is a binding change, and what follows the operator's ruling, are in § Edits. Your side, as a feature's controller:

**Raising.** Two findings, yours or a seat's, go to the operator as a decision ask: that the feature needs splitting after its spec campaign closes or once its lane note is committed, and that its umbrella needs an edit § Edits classes as a binding change. Neither is a scoped amendment or a supersede, and **neither is made as an edit to an umbrella on the feature's branch**.

**Receiving.** For a feature whose preamble carries an umbrella line, at each task or round boundary and before each full-scope pass and fix wave of its branch review (`crucible:requesting-code-review`) — before you record the task's BASE, the revision the round reviews, the pass's range or the wave's FIX_BASE — check whether a binding change to an umbrella in its chain has landed on the base since the branch last took the base in (`git diff HEAD...<base> -- <umbrella paths>` shows what changed there). If one has, and the operator has not ruled the feature unaffected, merge the base into the feature's branch — never rebase it, which would rewrite the revisions your records name. Where the change contradicts the feature's spec, folded document or lane note, amend it: a spec or folded document by the scoped amendment `skills/redteaming/references/flip-paths.md` states; a lane note by an operator-approved change to its binding parts, re-pinned in the ledger as `skills/subagent-driven-development/references/very-small-lane.md` states, or by that lane's upgrade hatch.
