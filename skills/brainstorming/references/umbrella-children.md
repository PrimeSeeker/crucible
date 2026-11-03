### Umbrella children

What an umbrella is, and its review, landing and closing: `skills/brainstorming/references/umbrellas.md`.

#### Children

A child's brainstorm takes its entry as an incoming document (§ Context gathering). An `open premise ask:` note in the entry (umbrellas.md § Landing) enters the child's brainstorm decision record with the operator's ruling if one has come since, else as open for the dialogue; the child then removes the note, a clarification its spec states (§ Edits). The route is proposed as for any feature.

**The umbrella line.** A child's spec, folded document, lane note or umbrella carries in its preamble one line naming its umbrella's file:

    Umbrella: `docs/crucible/<date>-<effort>/umbrella.md`

What that line makes binding is as `skills/subagent-driven-development/references/review-terms.md` § What binds in a spec states; each seat reads it in its own worktree, never from a copied block. Within the range a seat reviews, a binding change as § Edits defines it is a finding, a change to another started child's entry included; the child's own mark and a clarification of its own entry that its spec states, changing nothing another entry waits on, are not, and neither is a binding change taken in from the base. The umbrella's Intent is protected as the child's own is: `skills/subagent-driven-development/references/seat-rules.md` § Premise findings states what a seat raises against it, and § Binding changes what a change to it on a child's branch is. A child that existed before its umbrella carries no line and is bound by nothing in it. A successor written by a supersede, an unfold or the very-small lane's upgrade hatch carries its predecessor's line.

**A split.** Found before the spec campaign closes: replace the spec with `umbrella.md` and return to step 4; a running campaign stops. Found later (after that close, or once the lane note is committed): a decision ask, raised by § Under an umbrella. On a late split the feature is abandoned; a new umbrella with its own slug takes the work up, lists the feature by path and carries the parent's umbrella line. In the parent it takes the old entry's place and obligation, and entries that waited on the old one wait on it; the old entry stays, marked `dropped` and naming it. That change lands as a binding change does (§ Edits).

#### Edits

An umbrella is edited in place until it closes (umbrellas.md § Closing): before it lands by its own campaign's fixes, after only by the edits below and the marks of § Marks.

**Lightly held** edits ride a child's branch and land with it:

- adding a child;
- rewording an entry whose child has not started — a child has started once its feature folder is born;
- a child's clarification of its own entry, stated in its spec, that changes nothing another entry waits on;
- corrections to the umbrella's Intent that leave what it asks for unchanged, and edits to its non-firm Decisions and its Interfaces & boundaries;
- the child's own mark.

**A binding change** — to the umbrella's Constraints & invariants or firm decisions, to what its Intent asks for, or any other change to a started child's entry — is never made on a child's branch. It is a decision ask naming every open umbrella and every child in flight beneath it, at every depth. On the ruling it lands at once on its own branch, its diff operator-approved, through `crucible:finishing-a-development-branch`. Each child in flight then takes it in, or the operator rules that child unaffected (§ Under an umbrella). Dropping a child, on the operator's word, lands the same way.

#### Marks

Each entry ends with its mark, or with none, meaning not landed:

- `landed`: set by the child on its own branch before its finish, so it lands with the child; `crucible:subagent-driven-development` § Finish says when.
- `umbrella`: a nested umbrella's entry, marked in its landing (umbrellas.md § Landing).
- `dropped`: with the reason, or, after a late split, naming the umbrella that took the work up.

A mark touches only its own entry. A child that existed before its umbrella is entered with its mark when the umbrella is written, or, if still in flight, unmarked, marking its entry at its own finish.

A feature with no umbrella line marks too where an umbrella on the base branch holds an unmarked entry opening with its slug (`git grep -n "<feature-slug>" <base-branch> -- "*/umbrella.md"`) and its feature folder was born on a tree without that umbrella: `git cat-file -e <commit>:<umbrella-path>` fails for the folder's first commit, the last line of `git log --diff-filter=A --format=%h -- <feature-folder>`. Where its tree lacks that umbrella, it merges the base branch in first, never rebasing. A feature born on a tree that held the umbrella is not that entry's child. A feature no umbrella names writes no mark; an entry already marked needs nothing.

#### Resuming

To continue an effort, take its umbrella's first unmarked entry whose dependencies have landed (marked `landed`, or `umbrella` and closed; a `dropped` one is the operator's call), descending by the same rule into an unclosed `umbrella` entry whose own dependencies have landed. Confirm with the operator that it is not in flight elsewhere, then brainstorm it (§ Children). A complete umbrella leaves only its closing review (umbrellas.md § Closing, § Closing review). Agent memory holds at most a pointer to the umbrella, which holds what later parts must deliver.

#### Under an umbrella

**Raising.** Two findings, yours or a seat's, are decision asks: that the feature needs splitting after its spec campaign closes or once its lane note is committed, and that its umbrella needs a binding change (§ Edits says what is one and what follows the ruling). Neither is a scoped amendment or a supersede, nor an edit to an umbrella on the feature's branch.

**Receiving.** For a feature whose preamble carries an umbrella line, at each task or round boundary and before each full-scope pass and fix wave of its branch review (`crucible:requesting-code-review`) — before you record the task's BASE, the revision the round reviews, the pass's range or the wave's FIX_BASE — check whether a binding change to an umbrella in its chain has landed on the base since the branch last took the base in (`git diff HEAD...<base> -- <umbrella paths>`). If one has and the operator has not ruled the feature unaffected, merge the base in, never rebasing: a rebase rewrites the revisions your records name. Where the change contradicts the feature's document, amend a spec or folded document by the scoped amendment of `skills/redteaming/references/flip-paths.md`, a lane note by an operator-approved change to its binding parts, re-pinned in the ledger as `skills/subagent-driven-development/references/very-small-lane.md` states, or by that lane's upgrade hatch.
