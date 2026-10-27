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
  and Acceptance, which is the Children list — ordered entries separated
  by blank lines, each naming the child's slug, what it must deliver,
  what it waits on, and its mark (D9) — stating that each child's own
  Acceptance carries the checks. A campaigned umbrella carries every
  section, so its seats grade it as the spec it is. An umbrella carries
  no `Deferred to implementation:` marker: detail it leaves open goes to
  the entry of the child that owns it. A nested umbrella's preamble names
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
  children, and a child's preamble names its parent. Birth and resolve
  are unchanged. Rejected: children born inside their umbrella's folder
  (it rewrites the birth and resolve rules every route uses, and a child
  that existed before its umbrella could never sit there).
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
  abandonment, since the umbrella never reaches SDD. A nested umbrella
  marks its entry in its parent `umbrella` in the same landing.
- **D6 — A child's brainstorm takes its entry as input.** The entry is
  an incoming document in brainstorming's sense: what it settles stays
  settled, and the dialogue asks only what it leaves open. The child's
  route is proposed as for any feature. A feature whose brainstorm finds
  it must split before its spec is reviewed removes that spec and writes
  `umbrella.md` in its place (back to step 4). One found to need
  splitting later — after its campaign, or once its lane note is
  committed — is an operator decision ask: the feature is abandoned, its
  entry is marked `dropped` naming the new umbrella, and a new umbrella
  with its own slug takes the work up, listing the abandoned feature by
  path.
- **D7 — The umbrella line.** A child's spec, folded document, lane note
  or umbrella carries in its preamble a line ``Umbrella: `<path>` ``.
  What binds the child then includes its own entry, and the umbrella's
  Constraints & invariants and [LOAD-BEARING] marks, and, through the
  umbrella's own line, its parent's, up the chain. Every seat that
  receives binding content reads them there as binding, in the worktree
  it works in, at the commit its review reads. A successor — by
  supersede, unfold or the very-small lane's upgrade hatch — carries its
  predecessor's line. A child that existed before its umbrella carries no
  line and is bound by nothing in it.
- **D8 — Edits.** Lightly held edits ride a child's branch and land with
  it: adding a child, rewording a not-yet-started child's entry, and the
  child's own mark (D9). A change to the umbrella's binding content — its
  Constraints & invariants, its [LOAD-BEARING] marks, or a started
  child's entry — is a decision ask to the operator, naming every open
  umbrella and every child in flight beneath it, at every depth. On the
  operator's ruling it lands at once on a branch of its own: the operator
  approves its diff, and it lands through
  `crucible:finishing-a-development-branch`. Each child in flight then
  takes in the base before its next dispatch, or the operator rules it
  unaffected; a child whose spec the change contradicts takes a scoped
  amendment. Dropping a child, on the operator's word, lands the same
  way.
- **D9 — Each entry carries a mark.** A child marks its own entry
  `landed` in the commit that lands it, written on its own branch before
  its finish; a nested umbrella's entry is marked `umbrella` when it
  lands (D5); a dropped child's entry `dropped`, with its reason. A child
  that existed before its umbrella is entered with its mark when the
  umbrella is written, or once it has landed if it is still in flight
  then. An entry with no mark has not landed. A mark touches only its own
  entry, and blank lines between entries keep siblings' marks from
  conflicting in git. Rejected: state derived from which folders and
  branches exist (a nested umbrella's landing, an unrelated feature
  taking a child's slug, and drops riding unlanded branches all misread
  it).
- **D10 — Closing.** An umbrella is closed when every entry is marked
  `landed` or `dropped`, or `umbrella` with that umbrella itself closed;
  anyone reading it sees that, recursively, and nothing is written
  upward. Whether a dropped child becomes a backlog item is the
  operator's call. From the close on, the umbrella is frozen.
- **D11 — Resuming an effort.** A session continuing an effort reads the
  umbrella and takes the first entry with no mark whose dependencies have
  landed — marked `landed`, or `umbrella` and closed; a `dropped`
  dependency is the operator's call — and confirms with the operator that
  it is not in flight elsewhere. Agent memory holds at most a pointer to
  the umbrella.
- **D12 — `umbrella.md` stays in the merged tree.** Before an umbrella's
  own pull request, finishing does not offer to remove `umbrella.md`:
  the children read it, marks included, on the branch they land on. A
  child's folder is offered like any feature's.

## Constraints & invariants

1. An umbrella binds a child only through the umbrella line in the
   child's preamble (D7), read by each seat in its own worktree; never
   through a copied block.
2. Each rule this feature adds to skill text is stated once, at the site
   its reader acts from (§ Interfaces & boundaries assigns each); other
   skill text points there. Documentation and decision records describe
   and cite it.
3. A shipped spec is never silently edited, as before. An umbrella is
   edited in place until it closes, by its own campaign's fixes before it
   lands and by the edits and marks of D8 and D9 after, and is frozen
   from its close.
4. No committed text this feature writes names a project other than
   crucible or describes a private setup (`AGENTS.md`).

## Interfaces & boundaries

The sites the change touches, found by search, each with the rule it
owns.

- **`skills/brainstorming/references/umbrellas.md`** (new) owns D1–D4 and
  D6–D11, and D5's mark: the shape, recursion, flat folders, review,
  children, the umbrella line as its writers set it, edits, marks,
  closing and resuming. It opens with the heading of its stub.
- **`skills/brainstorming/SKILL.md`.** One stub section naming the
  reference to read in full, reached from the scope-decomposition check
  (§ The dialogue), self-review check 3 and step 4 (proposing the
  umbrella and its review); the incoming-document paragraph points a
  child's brainstorm, and a session resuming an effort, to the
  reference; the Flow list's steps 5, 9 and 10, the opening's
  terminal-state sentence and § Handoff gain the umbrella's terminal
  state (campaign, or approval, then landing); the spec contract's
  persistence paragraph points to the reference for the umbrella line.
  Other sites point to the reference without the stub's wording, since
  the suite allows one stub per reference.
- **`tests/test_skill_references.py`**, its `EXPECTED` set: the new stub
  and reference pair.
- **`skills/brainstorming/references/lane-note.md`.** A lane note under an
  umbrella carries the umbrella line in its preamble.
- **`skills/redteaming/references/formats.md`** § Feature folder: the
  role name `umbrella.md`. § Feature workspace root and layout,
  Lifecycle, owns D5's third end; brainstorming's provisioning clause
  points there.
- **What binds, at every statement of it.** Each site below gains the
  clause that the child's own entry and its umbrella's binding content
  bind too, up the chain, read in the seat's worktree:
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
    makes binding";
  - `skills/subagent-driven-development/references/dispatch-composition.md`:
    item 4's statement of what the pointer makes binding.

  Slot cards change only where a slot must carry an umbrella path, and
  `agents/` is regenerated. The blind verifier, which receives no
  binding content, is unchanged.
- **`skills/subagent-driven-development/references/dispatch-composition.md`**
  item 2 owns the controller's side: the umbrellas' paths, up the chain,
  are among a binding-receiving seat's input paths.
- **`skills/redteaming/SKILL.md`** § Dispatch composition: its seat
  input list admits the umbrellas; § Exit gains the umbrella campaign's
  handoff (landing, then the first child's brainstorm).
- **`skills/redteaming/references/flip-paths.md`** owns the in-flight
  child's side of D8 — a binding change to its umbrella: take in the
  base before the next dispatch, and a scoped amendment where the
  child's spec contradicts it — and the successor's umbrella line for a
  supersede or an unfold (D7).
- **`skills/subagent-driven-development/references/very-small-lane.md`**,
  its upgrade hatch: the successor carries the note's umbrella line (D7).
- **`skills/subagent-driven-development/SKILL.md` § Finish** owns the
  `landed` mark's timing: a child whose spec carries an umbrella line
  marks its entry before the suite runs (D9).
- **`skills/finishing-a-development-branch/SKILL.md`**, its pull-request
  records ask, owns D12.
- **`AGENTS.md`**, the `docs/crucible/` line, and **`README.md`**
  § What it writes into your repository: the umbrella's role file, open
  until it closes.
- **Decision records.**
  - `docs/decisions/records-and-workspace.md`: the workspace's third
    end; the Rejected bullet on living specs scoped to after shipping;
    D12, with its trade-off: a project that keeps feature folders out of
    its merged tree still keeps `umbrella.md`.
  - `docs/decisions/routes.md`: an umbrella takes none of the three
    routes.
  - The umbrella decision itself (D1–D4, D7–D10, D12) in
    `docs/decisions/the-spec.md` or a new record.
  - Each edit carries its Changes line.
- **Untouched:** the plan header's single pin (the umbrella line carries
  no revision; the plan pins the spec, whose preamble carries the line);
  the blind verifier; what the routes do; birth and resolve; the other
  consumers of the feature folder.

Deferred to implementation: whether the umbrella decision lives in
`docs/decisions/the-spec.md` or a new record.

Deferred to implementation: the exact wording and placement of each
site's sentence, within Constraint 2, and whether any slot card needs a
new value.

## Acceptance

1. **Each rule once in skill text.** For each rule in § Interfaces &
   boundaries, a search by its key terms over `skills/` finds it stated
   at its owning site and pointed to elsewhere; `AGENTS.md`, `README.md`,
   `docs/*.md` and `docs/decisions/` describe and cite it. One-time
   check, recorded as the searches and their output; the branch reviewer
   checks it too.
2. **Every statement of what binds names the umbrella.** For each of the
   eleven files listed under "What binds, at every statement of it", the
   statement named there, quoted after the change, carries the clause.
   One-time check, recorded as the quotes; before the change, a search
   of those files for "umbrella" finds none.
   `python tools/instrument_agents.py check` passes (standing, through
   the suite).
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
- The umbrella line, in a child's preamble:
  ``Umbrella: `docs/crucible/<date>-<effort>/umbrella.md` ``.
- A Children entry, a blank line before the next:
  ``- `<slug>` — <what it delivers>; waits on `<slug>` — landed``.
- The templates' clause, beside "any preamble convention it declares
  binding": "and, where its preamble names an umbrella, the child's own
  entry and that umbrella's Constraints & invariants and [LOAD-BEARING]
  marks, up the chain".
