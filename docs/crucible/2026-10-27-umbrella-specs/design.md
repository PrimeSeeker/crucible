# Umbrella specs: efforts that take several features

## Intent

**Problem.** Some work is too large for one spec and is split into
several features that share decisions, an order, or both. Crucible has no
document for the whole. Brainstorming's scope-decomposition check
(`skills/brainstorming/SKILL.md` § The dialogue) splits a request into
sub-features, each with "its own spec → campaign → plan cycle", and
stops there: nothing holds what the sub-features share, what each still
owes, or the order. The scoped amendment and the supersede
(`skills/redteaming/references/flip-paths.md`) work inside one feature
only.

Where an effort needed one anyway, it was improvised, in three shapes
seen on crucible itself and on one other project crucible ran on:

- **A frozen parent amended from its children.** A parent spec went
  through its own campaign; each child spec then carried a section of
  amendments to the parent rather than edit it. The parent's current
  state is the original plus every child's amendments, read together.
- **An append-only parent.** A parent of about 24,600 words gained one
  addendum per child, appended in place; its current state is its body
  merged in the reader's head with seven addenda. Its levels ran four deep
  (parent, subprojects, waves, sub-waves), and the middle levels had no
  document of their own: one was held by a backlog item serving as an
  index of obligations stated across many records and items, another by
  a decision record holding the rules every sub-wave follows.
- **A phase plan in the backlog and in memory.** Crucible's own
  publication was planned in a backlog item of about 5,200 words that
  grew into a progress log, with the rest in agent memory local to one
  machine; later phases' requirements sat partly in earlier specs'
  out-of-scope lists. Memory is local to one machine and host, no seat is
  directed to it, and its content cannot be committed under `AGENTS.md`'s
  no-local-context rule.

**Goals.**

- One committed document kind, the **umbrella**, that holds an effort:
  what its parts share, what each part delivers, in what order, and which
  parts have landed; readable in its current state from one file.
- Umbrellas nest: a part that itself splits becomes an umbrella.
- Every seat of a child that receives binding content reads the
  umbrella's binding content as binding, so a child is reviewed for
  compliance with its umbrella and for delivering its entry.
- What a later part must deliver lives in the umbrella, never only in
  memory or chat.

**Non-goals.**

- Moving existing feature folders, nesting folders, or retrofitting an
  umbrella onto past work. An umbrella for work already in progress is
  the first use of this feature, not part of it.
- A changelog in the umbrella: git history and the children's specs
  record what changed.
- Changing what the three routes do, the spec contract's sections, the
  campaign, the plan phase or SDD beyond the sites named in § Interfaces
  & boundaries.

## Decisions

- **D1 — The umbrella is a spec of its own kind.** It has a slug, a
  branch, a workspace and a feature folder like a feature, and takes none
  of the three routes: its review is D4's. Its folder holds
  `umbrella.md`, born by the existing birth step and written under the
  spec contract's sections: Intent (the effort's goal and non-goals);
  Decisions, Constraints & invariants, Interfaces & boundaries (what
  children provide each other) and Mechanism sketches where it has them;
  and Acceptance, which is the Children list — ordered entries, each
  naming the child's slug, what it must deliver, what it waits on, and
  its mark (D9) — stating that each child's own Acceptance carries the
  checks. A campaigned umbrella carries every section, so its seats grade
  it as the spec it is. An umbrella carries no `Deferred to
  implementation:` marker: detail it leaves open goes to the entry of
  the child that owns it. A nested umbrella's preamble carries the pin to
  its parent (D7). Rejected: a frozen parent amended from its children,
  and a frozen parent plus an amendment log (both leave the reader
  merging texts, the cost the improvised forms paid).
- **D2 — Recursive.** A child that splits becomes an umbrella and the
  parent of its own children; its entry in its parent says so. Each
  umbrella holds only what its children share; what one child alone needs
  moves down to that child. Rejected: one flat umbrella holding the whole
  tree (it grows toward the append-only parent's size), and a depth cap
  (arbitrary; the four-level case would have broken it).
- **D3 — Folders stay flat.** A child's feature folder is born at the
  root like any other; the umbrella's Children list is the index of its
  children, and a child's pin names its parent. Birth and resolve are
  unchanged. Rejected: children born inside their umbrella's folder (it
  rewrites the birth and resolve rules every route uses, and a child that
  existed before its umbrella could never sit there).
- **D4 — Review scaled to content** [LOAD-BEARING]. An umbrella carrying
  Decisions, Constraints & invariants or Interfaces & boundaries takes a
  spec campaign; one holding only Intent and Acceptance is approved by
  the operator, as a lane note is: drafted, self-reviewed and shown with
  the proposal at step 4, and written as approved. Brainstorming proposes
  which at step 4, the operator rules, and the ruling is an entry in the
  brainstorm decision record. Neither takes a plan phase or SDD: children
  write the plans.
- **D5 — The umbrella lands before its first child,** through
  `crucible:finishing-a-development-branch`, so children branch from a
  base that holds it and other sessions can read it. Before it lands,
  the controller checks the campaign records, where a campaign ran
  (round records, readouts, the digest), names any gap in the campaign's
  close readout, and deletes the umbrella's workspace: the umbrella's
  landing is a third end of a workspace's life, beside SDD Finish and
  abandonment, since the umbrella never reaches SDD.
- **D6 — A child's brainstorm takes its entry as input.** The entry is
  an incoming document in brainstorming's sense: what it settles stays
  settled, and the dialogue asks only what it leaves open. The child's
  route is proposed as for any feature; a child that changes its
  umbrella's binding content does not take the very-small lane. A
  feature whose brainstorm finds it must split before its spec is
  reviewed replaces that spec with `umbrella.md` (back to step 4). One
  found to need splitting later — after its campaign, or once its lane
  note is committed — is an operator decision ask: the feature is
  abandoned and a new umbrella, with its own slug, takes the work up and
  lists the abandoned feature by path.
- **D7 — The pin.** A child's spec, folded document, lane note or
  umbrella carries in its preamble a line
  ``Umbrella: `<path>` @ `<rev>` ``, the revision being a commit on the
  branch children land on. What binds the child then includes its own
  entry, and the umbrella's Constraints & invariants and [LOAD-BEARING]
  marks at that revision, and, through the umbrella's own pin, its
  parent's, up the chain. Every seat that receives binding content reads
  them there as binding. A change the child makes to its umbrella (D8) is
  stated in the child's own spec, where its review reads it, and binds the
  child over the pinned text. A child that existed before its umbrella
  carries no pin and is bound by nothing in it.
- **D8 — Edits ride a child.** A child that changes its umbrella edits it
  on its own branch, stating the change in its spec; the edit lands with
  the child, and the branch review checks the edit against the statement.
  Adding a child or rewording a not-yet-started child's entry is lightly
  held. A change to the umbrella's binding content — its Constraints &
  invariants, its [LOAD-BEARING] marks, or a started child's entry — is a
  decision ask to the operator before the edit, as a scoped amendment is;
  the ask names every open umbrella and every child in flight beneath it,
  at every depth. Once the change has landed, each of them re-pins to it
  or records why it is unaffected: a child in flight by a scoped
  amendment of its own spec (on the very-small lane, by the lane's own
  decision ask for its note), an open nested umbrella by an edit riding
  its next child's branch. Dropping a child, on the operator's word,
  lands at once on a branch of its own: the operator approves its diff,
  and it lands through `crucible:finishing-a-development-branch`.
- **D9 — Each entry carries a mark.** A child marks its own entry
  `landed` in the commit that lands it, written on its own branch before
  its finish; a child that is itself an umbrella marks its entry `open`
  when it lands and `closed` when it closes (D10). A dropped child's
  entry is marked `dropped`, with its reason. An entry with no mark has
  not landed; whether it is in flight shows from a branch named by its
  slug. Each child edits only its own entry, so siblings' marks do not
  conflict. Rejected: state derived from which folders and branches
  exist (a nested umbrella's landing, an unrelated feature taking a
  child's slug, and drops riding unlanded branches all misread it).
- **D10 — Closing.** An umbrella is closed when every entry is marked
  `landed`, `closed` or `dropped`; anyone reading it sees that. The child
  whose landing closes a nested umbrella also marks that umbrella's
  entry in its parent `closed`, on the same branch. Whether a dropped
  child becomes a backlog item is the operator's call. From the close on,
  the umbrella is frozen.
- **D11 — Resuming an effort.** A session continuing an effort reads the
  umbrella and takes the first entry with no mark whose dependencies
  have landed, after checking that no branch named by its slug exists.
  Agent memory holds at most a pointer to the umbrella.
- **D12 — `umbrella.md` stays in the merged tree.** Before an umbrella's
  own pull request, finishing does not offer to remove `umbrella.md`:
  the children read it, marks included, on the branch they land on. A
  child's folder is offered like any feature's.

## Constraints & invariants

1. An umbrella binds a child only through the pin in the child's
   preamble (D7), read by each seat at the pinned revision; never through
   a copied block.
2. Each rule this feature adds is stated once, at the site its reader
   acts from (§ Interfaces & boundaries assigns each); every other site
   points there.
3. A shipped spec is never silently edited, as before. An umbrella is
   edited in place until it closes, by its own campaign's fixes before it
   lands and by children's edits and marks after, and is frozen from its
   close.
4. No committed text this feature writes names a project other than
   crucible or describes a private setup (`AGENTS.md`).

## Interfaces & boundaries

The sites the change touches, found by search, each with the rule it
owns.

- **`skills/brainstorming/references/umbrellas.md`** (new) owns D1–D4 and
  D6–D11: the shape, recursion, flat folders, review, children, the pin
  as its writers set it, edits, marks, closing and resuming. It opens with
  the heading of its stub.
- **`skills/brainstorming/SKILL.md`.** One stub section naming the
  reference to read in full, reached from the scope-decomposition check
  (§ The dialogue), self-review check 3 and step 4 (proposing the
  umbrella and its review); the Flow list's steps 5, 9 and 10, the
  opening's terminal-state sentence and § Handoff gain the umbrella's
  terminal state (campaign, or approval, then landing); the spec
  contract's persistence paragraph points to the reference for the pin.
  Other sites point to the reference without the stub's wording, since
  the suite allows one stub per reference.
- **`tests/test_skill_references.py`**, its `EXPECTED` set: the new stub
  and reference pair.
- **`skills/brainstorming/references/lane-note.md`.** A lane note under an
  umbrella carries the pin in its preamble.
- **`skills/redteaming/references/formats.md`** § Feature folder: the
  role name `umbrella.md`. § Feature workspace root and layout,
  Lifecycle, owns D5's third end; brainstorming's provisioning clause
  points there.
- **What binds, at every statement of it.** Each site below gains the
  clause that a pinned umbrella's binding content, and the child's own
  entry, bind too, read at the pinned revisions up the chain:
  - the templates' binding-content statements and read scopes:
    `skills/redteaming/seat-prompt.md`, `terminal-pass-prompt.md`,
    `skills/requesting-code-review/code-reviewer.md`,
    `skills/subagent-driven-development/task-reviewer-prompt.md`,
    `re-review-prompt.md`, `implementer-prompt.md`, each with its
    very-small-lane passage where it has one;
  - `skills/subagent-driven-development/SKILL.md`: the pre-flight
    plan-conflict scan, the Deviations paragraph and the adjudicator
    dispatch's inputs;
  - `skills/requesting-code-review/SKILL.md`: the branch reviewer's
    inputs;
  - `skills/subagent-driven-development/references/very-small-lane.md`:
    step 3's requirements input;
  - `skills/writing-plans/SKILL.md`: the spec pointer's "what the pin
    makes binding".

  Slot cards change only where a slot must carry an umbrella path, and
  `agents/` is regenerated. The blind verifier, which receives no
  binding content, is unchanged.
- **`skills/subagent-driven-development/references/dispatch-composition.md`**
  items 2 and 4 own the controller's side: the pinned umbrellas' paths,
  up the chain, are among a binding-receiving seat's input paths; the
  revisions come from the pins.
- **`skills/redteaming/SKILL.md`** § Dispatch composition: its seat
  input list admits the pinned umbrellas; § Exit gains the umbrella
  campaign's handoff (landing, then the first child's brainstorm).
- **`skills/redteaming/references/flip-paths.md`.** A finding that an
  umbrella's binding content is wrong points to the reference (D8).
- **`skills/subagent-driven-development/SKILL.md` § Finish** owns the
  mark's timing: a child whose spec pins an umbrella marks its entry, and
  where its landing closes a nested umbrella that umbrella's entry in its
  parent, before the suite runs (D9, D10).
- **`skills/finishing-a-development-branch/SKILL.md`**, its pull-request
  records ask, owns D12.
- **`AGENTS.md`**, the `docs/crucible/` line, and **`README.md`**
  § What it writes into your repository: the umbrella's role file, open
  until it closes.
- **Decision records.**
  - `docs/decisions/the-spec.md`: "the plan header's spec pointer is the
    only pin", in its Decision and its Rejected list, gains the umbrella
    pin.
  - `docs/decisions/records-and-workspace.md`: the workspace's third
    end; the Rejected bullet on living specs scoped to after shipping;
    D12, with its trade-off: a project that keeps feature folders out of
    its merged tree still keeps `umbrella.md`.
  - `docs/decisions/routes.md`: an umbrella takes none of the three
    routes.
  - The umbrella decision itself (D1–D4, D7–D10, D12) in
    `docs/decisions/the-spec.md` or a new record.
  - Each edit carries its Changes line.
- **`docs/backlog/`**: a new item, the reviewers' research reach — the
  operator's observation (2026-10-27) that review seats research more
  freely than their read scopes suggest, to be examined separately.
- **Untouched:** the plan header's single pin (the umbrella's pin travels
  in the spec's own preamble); the blind verifier; what the routes do;
  birth and resolve; the supersede; the other consumers of the feature
  folder.

Deferred to implementation: whether the umbrella decision lives in
`docs/decisions/the-spec.md` or a new record.

Deferred to implementation: the exact wording and placement of each
site's sentence, within Constraint 2, and whether any slot card needs a
new value.

## Acceptance

1. **Each rule once.** For each rule in § Interfaces & boundaries, a
   search by its key terms over `skills/`, `AGENTS.md`, `README.md`,
   `docs/*.md` and `docs/decisions/` finds it stated at its owning site
   and pointed to elsewhere. One-time check, recorded as the searches and
   their output; the branch reviewer checks it too.
2. **Every statement of what binds names the pinned umbrella.** Each
   file listed under "What binds, at every statement of it" contains the
   word "umbrella" in that statement. One-time check, recorded as a
   search of those ten files for "umbrella" with its output; on today's
   tree it finds none. `python tools/instrument_agents.py check`
   passes (standing, through the suite).
3. **The reference is reachable.** `skills/brainstorming/references/umbrellas.md`
   exists and one stub in `skills/brainstorming/SKILL.md` names it.
   Standing: `tests/test_skill_references.py`, its `EXPECTED` set gaining
   the pair.
4. **Records.** Each edited decision record carries a Changes line dated
   with its commit. Standing: `tests/test_decision_records.py` for the
   record's required sections; the branch reviewer for the Changes line.
5. **Budgets and suite.** `tests/prose-budget.txt` is updated for each
   skill directory the change grows or shrinks, and the full suite
   (`python -m pytest tests/`) passes on the branch's head. Example paths
   in shipped text use placeholders, which the suite's dangling-path
   check skips.
6. **No local context.** Constraint 4; checked by the branch reviewer,
   as `AGENTS.md` assigns.

Why no further standing test: no code or host reads a feature folder or
an umbrella — `grep -rln "docs/crucible\|feature folder\|feature_folder"
tools tests hooks` found one hit, a frozen scanner-corpus file
(2026-10-27) — and the repository's test rule allows a text assertion
only where one does. Whether the design works is shown by the first
umbrella run on it.

## Mechanism sketches (advisory)

- The reference's outline: when to propose (the decomposition check
  found several sub-features that share decisions, an order, or both);
  the shape (D1); review (D4); landing (D5, pointing to formats);
  children (D6, D7); edits (D8); marks (D9); closing (D10); resuming
  (D11).
- The pin line, in a child's preamble:
  ``Umbrella: `docs/crucible/<date>-<effort>/umbrella.md` @ `<rev>` ``.
- A Children entry:
  ``- `<slug>` — <what it delivers>; waits on `<slug>` — landed``.
- The templates' clause, beside "any preamble convention it declares
  binding": "and, where its preamble pins an umbrella, the child's own
  entry and that umbrella's Constraints & invariants and [LOAD-BEARING]
  marks at the pinned revision, up the chain".
