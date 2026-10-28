### Umbrellas — an effort that takes several features

An **umbrella** holds an effort too large for one feature: what its parts share, what each part delivers, in what order, and which parts have landed, readable in its current state from one file. Propose one where the scope-decomposition check, self-review check 3 or the design at step 4 finds sub-features that share decisions, an order, or both; sub-features that share neither are separate features.

#### Shape

An umbrella is a spec of its own kind. It has a slug, a branch, a worktree, a workspace and a feature folder like a feature, and takes none of the three routes: its review is the one § Review states. Its file is `umbrella.md` in its feature folder, born by the birth step of `skills/redteaming/references/formats.md` § Feature folder and written under the spec contract's sections:

- **Request** — the effort's request, as the spec contract defines it. A child's Request points to this section and quotes only what was asked of that child: the passages of it that ask something of the child, and each later message that changed what was asked of it. Under an umbrella with no Request, a child quotes the effort's whole request.
- **Intent** — the effort's goal and non-goals.
- **Decisions**, **Constraints & invariants**, **Interfaces & boundaries** (what children provide each other) and **Mechanism sketches**, where it has them. Its Interfaces & boundaries describe; a contract between children that must bind is one of its Constraints & invariants.
- **Acceptance** — the Children list, stating that each child's own Acceptance carries the checks.

A campaigned umbrella carries every section, so its seats grade it as the spec it is. It carries no `Deferred to implementation:` marker: detail it leaves open goes into the entry of the child that owns it.

**The Children list** is ordered, one entry per child, with a blank line between entries. An entry names the child's slug, what it must deliver, what it waits on, and its mark (§ Marks):

    - `cache-layer` — a read-through cache behind the store interface; waits on nothing — landed

    - `cache-metrics` — hit-rate metrics for the cache layer; waits on `cache-layer`

**Recursion.** A child that splits becomes an umbrella and the parent of its own children; its entry in its parent says so. Each umbrella holds only what its children share: what one child alone needs moves down into that child's entry. There is no depth cap.

**Folders stay flat.** A child's feature folder is born at the root like any other; the Children list is the index of an umbrella's children, and a child's umbrella line names its parent. Birth and resolve are unchanged.

#### Review

An umbrella carrying Decisions, Constraints & invariants or Interfaces & boundaries takes a spec campaign; one without them (Mechanism sketches aside) is approved by the operator, as a lane note is: drafted, self-reviewed and shown with the proposal at step 4, and written as approved. Propose which at step 4; the operator rules, and the ruling is an entry in the brainstorm decision record. Neither takes a plan phase or SDD: its children write the plans. This classifies an umbrella at its birth; the operator's ruling on a later binding change (§ Edits) says whether that change takes a campaign.

A campaigned umbrella takes steps 5–10 as a spec does, and the campaign's close hands off to its landing. An approval-only umbrella is written at step 5 as approved and its workspace provisioned at step 7; it takes no digest and no digest gate, and its handoff is its landing.

#### Landing

An umbrella lands before its first child, through `crucible:finishing-a-development-branch`, so children branch from a base that holds it and other sessions can read it. Before it lands, its controller:

1. where a campaign ran, checks its records — round records, readouts, the digest — and names any gap in the campaign's close readout;
2. writes each premise finding still open into the entry of the child the effort resumes at (§ Resuming), marked as an open premise ask, so that child's brainstorm finds it, and puts it to the operator with the landing ask, as `skills/redteaming/references/flip-paths.md` § Premise findings states; the landing does not wait for the ruling;
3. deletes the umbrella's workspace, an end of a workspace's life that the Lifecycle of `skills/redteaming/references/formats.md` § Feature workspace root and layout names;
4. for a nested umbrella, marks its entry in its parent `umbrella`, in the same landing.

After the landing, the effort resumes at its first child (§ Resuming).

#### Children

A child's brainstorm takes its entry as an incoming document (§ Context gathering): what the entry settles stays settled, and the dialogue asks only what it leaves open. An open premise ask its umbrella's landing wrote into the entry (§ Landing) enters the child's brainstorm decision record, with the operator's ruling where one has come since, or else as open, for the dialogue to take up. The child's route is proposed as for any feature.

**The umbrella line.** A child's spec, folded document, lane note or umbrella carries in its preamble one line naming its umbrella's file:

    Umbrella: `docs/crucible/<date>-<effort>/umbrella.md`

Through that line the child is bound by its own entry and by the umbrella's Constraints & invariants, [LOAD-BEARING] marks and firm decisions (those it records as the operator's firm preference), and, through the umbrella's own line, by its parent's, up the chain. Each seat reads them in its own worktree, never from a copied block. Within the range a seat reviews, a change to the umbrella's Constraints & invariants, marks or firm decisions is a finding, and so is a change to the child's entry other than its own mark or a clarification its spec states (§ Edits); a binding change taken in from the base is not. A child that existed before its umbrella carries no line and is bound by nothing in it. A successor's line is set where the successor is written: `skills/redteaming/references/flip-paths.md` for a supersede or an unfold, `skills/subagent-driven-development/references/very-small-lane.md` for the lane's upgrade hatch.

**A split.** A feature found to need splitting before its spec campaign closes removes its spec and writes `umbrella.md` in its place: back to step 4, and a campaign in progress stops. Found later — after its campaign closes, or once its lane note is committed — the split is an operator decision ask, and so is a binding change a child finds its umbrella needs; a child's controller raises either by `skills/redteaming/references/flip-paths.md`. On a late split, the feature is abandoned and a new umbrella with its own slug takes the work up, listing the abandoned feature by path. In the parent, the new umbrella is entered in the old entry's place, carrying its obligation, and carries the parent's umbrella line; entries that waited on the old one wait on it; the old entry stays, marked `dropped` and naming it. That change to the parent lands as a binding change does (§ Edits).

#### Edits

An umbrella is edited in place until it closes (§ Closing): by its own campaign's fixes before it lands, and after that by the edits below and the marks of § Marks.

**Lightly held edits ride a child's branch and land with it:**

- adding a child;
- rewording an entry whose child has not started — a child has started once its feature folder is born;
- a child's clarification of its own entry, stated in its spec, that changes nothing another entry waits on;
- edits to the umbrella's Intent, its Decisions neither marked nor firm, and its Interfaces & boundaries;
- the child's own mark.

**A binding change** — to the umbrella's Constraints & invariants, [LOAD-BEARING] marks or firm decisions, or any other change to a started child's entry — is never made on a child's branch. It is a decision ask to the operator, naming every open umbrella and every child in flight beneath it, at every depth. On the operator's ruling it lands at once on a branch of its own: the operator approves its diff, and it lands through `crucible:finishing-a-development-branch`. Each child in flight then takes it in, or the operator rules that child unaffected, as `skills/redteaming/references/flip-paths.md` states. Dropping a child, on the operator's word, lands the same way.

#### Marks

Each entry ends with its mark, or with none:

- `landed` — the child marks its own entry on its own branch before its finish, so the mark lands with it; `crucible:subagent-driven-development` § Finish says when.
- `umbrella` — a nested umbrella's entry, marked in its landing (§ Landing).
- `dropped` — a dropped child's entry, with its reason, or, after a late split, naming the umbrella that took the work up.

An entry with no mark has not landed. A mark touches only its own entry; the blank lines between entries keep siblings' marks from conflicting in git. A child that existed before its umbrella is entered with its mark when the umbrella is written; one still in flight then is entered unmarked and marks its entry at its own finish.

#### Closing

An umbrella is closed when every entry is marked `landed` or `dropped`, or `umbrella` with that umbrella itself closed. Anyone reading it sees that, recursively; nothing is written upward. Whether a dropped child becomes a backlog item is the operator's call. From its close the umbrella is frozen.

#### Resuming

A session continuing an effort reads its umbrella and takes the first entry with no mark whose dependencies have landed — marked `landed`, or `umbrella` and closed; a `dropped` dependency is the operator's call — descending into an entry marked `umbrella` that is not closed, once its own dependencies have landed, to take its next entry by the same rule. It confirms with the operator that the entry is not in flight elsewhere, then brainstorms it as § Children states. What a later part must deliver lives in the umbrella: agent memory holds at most a pointer to it.
