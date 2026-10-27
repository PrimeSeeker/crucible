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
  what its parts share, what each part delivers, and in what order;
  readable in its current state from one file.
- Umbrellas nest: a part that itself splits becomes an umbrella.
- Every seat of a child that receives binding content reads the
  umbrella's binding content as binding, so a child is reviewed for
  compliance with its umbrella.
- What a later part must deliver lives in the umbrella, never only in
  memory or chat.

**Non-goals.**

- Moving existing feature folders, nesting folders, or retrofitting an
  umbrella onto past work. An umbrella for work already in progress is
  the first use of this feature, not part of it.
- Tracking state in the umbrella (a status field per child), or any
  tool that computes it.
- A changelog in the umbrella: git history and the children's specs
  record what changed.
- Changing what the three routes do, the spec contract's sections, the
  campaign, the plan phase or SDD beyond the sites named in § Interfaces
  & boundaries.

## Decisions

- **D1 — The umbrella is a spec of its own kind.** It has a slug, a
  branch, a workspace and a feature folder like a feature, and takes none
  of the three routes: its review is D4's. Its folder holds
  `umbrella.md`, born by the existing birth step, written under the spec
  contract's sections with these contents: Intent (the effort's goal and
  non-goals); optionally Decisions, Constraints & invariants, and
  Interfaces & boundaries (what children provide each other), under the
  spec contract's weights; and Acceptance, which is the Children list —
  ordered entries, each naming the child's slug, what it must deliver
  and what it waits on — with the checks left to each child's own
  Acceptance. An umbrella carries no `Deferred to implementation:`
  marker: detail it leaves open goes to the entry of the child that
  owns it. A nested umbrella's preamble carries the pin to its parent
  (D7). Rationale: the spec contract's shape lets the campaign, its
  seats and its terminal pass review an umbrella as they review a spec.
  Rejected: a frozen parent amended from its children, and a frozen
  parent plus an amendment log (both leave the reader merging texts, the
  cost the improvised forms paid).
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
  the operator, as a lane note is: drafted and shown with the proposal at
  step 4, written as approved. Brainstorming proposes which at step 4,
  the operator rules, and the ruling is an entry in the brainstorm
  decision record. Neither takes a plan phase or SDD: children write the
  plans. Binding content a child later adds to an umbrella is reviewed by
  that child's review (D8).
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
  route is proposed as for any feature. A feature whose brainstorm finds
  it must split before its spec campaign replaces its unreviewed spec
  with `umbrella.md` (back to step 4); after the campaign, the split is a
  supersede whose successor is `umbrella.md`.
- **D7 — The pin.** A child's spec, folded document, lane note or
  umbrella carries in its preamble a line
  ``Umbrella: `<path>` @ `<rev>` ``. What binds the child then includes
  the umbrella's Constraints & invariants and [LOAD-BEARING] marks at
  that revision, and, through the umbrella's own pin, its parent's, up
  the chain. Every seat that receives binding content reads them there
  as binding, and grades the child's compliance with them. A child that
  edits its umbrella (D8) pins the commit carrying the edit; once the
  child's own campaign has closed, a re-pin is part of a scoped amendment
  of the child's spec, as a plan header's spec pointer is re-stamped. A
  supersede's or unfold's successor carries its predecessor's pin and
  may re-pin, being reviewed afresh.
- **D8 — Edits ride a child.** A child that changes its umbrella edits it
  on the child's own branch; the edit lands with the child, under the
  child's review, which is the only check on it. Adding a child or
  rewording a not-yet-started child's entry is lightly held; a started
  child's entry is edited only by that child. A change to the umbrella's
  binding content is a decision ask to the operator before the edit, as
  a scoped amendment is; the ask names every child in flight, and each
  takes a scoped amendment of its own spec that re-pins to the change or
  records why it is unaffected. An edit no child causes (dropping a child
  on the operator's word) rides the next child's branch; where no child
  follows, it takes a branch of its own, the operator approves its diff,
  and it lands through `crucible:finishing-a-development-branch`.
- **D9 — State is derived.** A child is landed when its folder is on the
  branch children land on — a child that is itself an umbrella, when it
  has also closed (D10); in flight when it has a branch; otherwise not
  started. Only a dropped child is marked in its entry, with its reason.
  A slug named in an entry that another feature has taken meanwhile is
  refused at the child's birth, as any taken slug is; the child takes a
  new slug and edits its entry. Rationale: no status edits, and none of
  the sibling conflicts they would cause. Rejected: a status field per
  child.
- **D10 — Closing.** An umbrella closes when every child has landed or
  been dropped. The child whose landing completes that says in its close
  readout that the umbrella closes when it lands, with the dropped
  children and their reasons; where that closes the umbrella's own
  parent too, it says so for each level (where a branch of its own
  closes it, D8, the controller tells the operator the same). Whether any
  dropped child becomes a backlog item is the operator's call, as for any
  close readout's leftovers. From the close on, the umbrella is frozen.
- **D11 — Resuming an effort.** A session continuing an effort reads the
  umbrella and derives the next child from what has landed. Agent memory
  holds at most a pointer to the umbrella.
- **D12 — The records stay in the merged tree.** Before a pull request,
  finishing does not offer to remove the files of an umbrella's folder or
  of a child's: D5 and D9 read them on the branch children land on.

## Constraints & invariants

1. An umbrella binds a child only through the pin in the child's
   preamble (D7), read by each seat at the pinned revision; never through
   a copied block.
2. Each rule this feature adds is stated once, at the site its reader
   acts from; every other site points there.
3. A shipped spec is never silently edited, as before. An umbrella is
   edited in place until it closes, by its own campaign's fixes before it
   lands and by children's edits after (D8), and is frozen from its
   close.
4. No committed text this feature writes names a project other than
   crucible or describes a private setup (`AGENTS.md`).

## Interfaces & boundaries

The sites the change touches, found by search.

- **`skills/brainstorming/SKILL.md`.** One stub section, naming the new
  reference `skills/brainstorming/references/umbrellas.md` to read in
  full, reached from the scope-decomposition check (§ The dialogue) and
  self-review check 3; step 4 proposes the umbrella and its review (D4),
  and the Flow list's steps 5, 9 and 10 cover it; the opening's
  terminal-state sentence and
  § Handoff gain the umbrella's terminal state (campaign, or approval,
  then landing); the spec contract gains the pin (D7). The reference
  holds the umbrella's shape and rules (D1, D2, D4–D12) and opens with
  the stub's heading; other sites point to it without the stub's
  wording, since the suite allows one stub per reference.
- **`tests/test_skill_references.py`**, its `EXPECTED` set: the new stub
  and reference pair, since the test asserts the set of stubs exactly.
- **`skills/brainstorming/references/lane-note.md`.** A lane note under
  an umbrella carries the pin in its preamble, and its Intent states any
  change the lane makes to its umbrella.
- **`skills/redteaming/references/formats.md`** § Feature folder: the
  role name `umbrella.md` beside `design.md`, `folded.md` and `note.md`;
  § Feature workspace root and layout, Lifecycle: the umbrella's landing
  as a third end (D5); brainstorming's provisioning clause points there.
- **The seats' binding content and read scope.** Every template whose
  binding-content statement names a spec's preamble conventions — the
  redteam seat (`skills/redteaming/seat-prompt.md`), the terminal pass
  (`terminal-pass-prompt.md`), the branch reviewer
  (`skills/requesting-code-review/code-reviewer.md`), the task reviewer,
  the re-reviewer and the implementer
  (`skills/subagent-driven-development/task-reviewer-prompt.md`,
  `re-review-prompt.md`, `implementer-prompt.md`), each with its
  very-small-lane passage where it has one — states that a pinned
  umbrella's binding content binds too, and its read scope admits the
  pinned umbrellas at their revisions. Their slot cards change only
  where a slot must carry an umbrella path. `agents/` is regenerated.
  The blind verifier, which receives no binding content, is unchanged.
- **The other statements of what binds** that name a spec's preamble
  conventions: `skills/subagent-driven-development/SKILL.md` § The Task
  Loop's Deviations paragraph and `skills/writing-plans/SKILL.md`'s spec
  pointer (what the pin makes binding) gain the same clause.
- **`skills/redteaming/SKILL.md`** § Dispatch composition: its seat
  input list admits the pinned umbrellas; § Exit gains the umbrella
  campaign's handoff (landing, then the first child's brainstorm).
- **`skills/subagent-driven-development/references/dispatch-composition.md`**
  items 2 and 4: the pinned umbrellas, up the chain, are among the input
  paths and the binding content of every seat that receives binding
  content.
- **`skills/redteaming/references/flip-paths.md`.** A finding that an
  umbrella's binding content is wrong is a decision ask as D8 states,
  pointing to the reference.
- **`skills/subagent-driven-development/SKILL.md` § Finish** step 3: the
  close readout of a child whose landing closes its umbrella says so
  (D10).
- **`skills/finishing-a-development-branch/SKILL.md`**, its pull-request
  records ask: not offered for an umbrella's folder or a child's (D12).
- **`AGENTS.md`**, the `docs/crucible/` line, and **`README.md`**
  § What it writes into your repository: the umbrella's role file, open
  until it closes.
- **Decision records.**
  - `docs/decisions/the-spec.md`: "the plan header's spec pointer is the
    only pin", in its Decision and its Rejected list, gains the umbrella
    pin.
  - `docs/decisions/records-and-workspace.md`: the workspace's third
    end; the Rejected bullet on living specs scoped to after shipping;
    the pull-request records ask's exception (D12).
  - `docs/decisions/routes.md`: an umbrella takes none of the three
    routes.
  - The umbrella decision itself (D1–D4, D7–D10, D12) in
    `docs/decisions/the-spec.md` or a new record, with the observation
    that crucible's reviewers' research reach should be examined
    separately (operator, 2026-10-27).
  - Each edit carries its Changes line.
- **Untouched:** the plan header's single pin (the umbrella's pin
  travels in the spec's own preamble); the blind verifier; what the
  routes do; birth and resolve; the other consumers of the feature
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
2. **Every statement of what binds names the pinned umbrella.** A search
   over `skills/` for the phrase "preamble convention" (whitespace
   between the words allowed) finds the umbrella clause within the same
   statement at every hit, and `python tools/instrument_agents.py check`
   passes. One-time check for the first, recorded with its output (on
   today's tree it finds nine hits, none with the clause); standing for
   the second, through the suite.
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
  the shape (D1); review (D4); landing (D5); children (D6, D7); edits
  (D8); state (D9); closing (D10); resuming (D11); records (D12).
- The pin line, in a child's preamble:
  ``Umbrella: `docs/crucible/<date>-<effort>/umbrella.md` @ `<rev>` ``.
- The templates' clause, beside "any preamble convention it declares
  binding": "and, where its preamble pins an umbrella, that umbrella's
  Constraints & invariants and [LOAD-BEARING] marks at the pinned
  revision, up the chain".
