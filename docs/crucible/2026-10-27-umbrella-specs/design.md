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
  amendments to the parent, because a shipped spec is never edited. The
  parent's current state is the original plus every child's amendments,
  read together.
- **An append-only parent.** A parent of about 24,600 words gained one
  addendum per child, appended in place; its current state is its body
  merged in the reader's head with seven addenda. Its levels ran four deep
  (parent, subprojects, waves, sub-waves), and the middle levels had no
  document of their own: one was held by a backlog item serving as an
  index of obligations stated across many records and items, another by
  a decision record holding the rules every sub-wave follows.
- **A phase plan in the backlog and in memory.** Crucible's own
  publication was planned in a backlog item of about 5,200 words that
  grew into a progress log, with the rest in the operator's machine-local
  agent memory; later phases' requirements sat partly in earlier specs'
  out-of-scope lists. Memory is invisible to every dispatched seat and
  cannot be committed under `AGENTS.md`'s no-local-context rule.

**Goals.**

- One committed document kind, the **umbrella**, that holds an effort:
  what its parts share, what each part delivers, and in what order;
  readable in its current state from one file.
- Umbrellas nest: a part that itself splits becomes an umbrella.
- An umbrella's binding content reaches every seat of every child
  through the pointer seats already receive.
- What a later part must deliver lives in the umbrella, never only in
  memory or chat.

**Non-goals.**

- Moving existing feature folders, or retrofitting an umbrella onto past
  work. An umbrella for work already in progress is the first use of
  this feature, not part of it.
- Tracking state in the umbrella (a status field per child), or any
  tool that computes it.
- Running children in parallel under any new coordination rule.
- Changing the three routes, the spec contract's sections, the campaign,
  the plan phase or SDD beyond the sites named in § Interfaces &
  boundaries.

## Decisions

- **D1 — The umbrella is a feature with a living document.** Its feature
  folder holds `umbrella.md`, born by the existing birth step. Contents,
  in order: Intent (goal and non-goals); optionally shared Decisions and
  Constraints & invariants, under the spec contract's weights; Children,
  an ordered list whose entries each name the child's slug, chosen up
  front, what it must deliver and what it waits on; and, once the
  umbrella has landed, a Changes section, one line per edit,
  `<YYYY-MM-DD>: <what changed> (<child slug>)`. Rationale: one file
  holds the current state; the Changes lines say which child changed
  what without a git query. Rejected: a frozen parent amended from its
  children, and a frozen parent plus an amendment log (both leave the
  reader merging texts, the cost the improvised forms paid).
- **D2 — Recursive.** A child that splits gets `umbrella.md` in its own
  feature folder and becomes the umbrella of its own children; its entry
  in its parent says so. Each umbrella holds only what its children
  share; what one child alone needs moves down to that child. Rejected:
  one flat umbrella holding the whole tree (it grows toward the
  append-only parent's size), and a depth cap (arbitrary; the four-level
  case would have broken it).
- **D3 — Children nest in their umbrella's folder.** A child born under
  an umbrella is born as `<umbrella-folder>/<YYYY-MM-DD>-<child-slug>/`.
  The branch and the workspace `.crucible/<slug>/` stay named by slug
  alone. A folder that already exists is never moved: an umbrella over
  work already started lists those children by their existing paths.
  Rationale: the tree is visible in the file system, and a child's parent
  is its location. Moving a folder would break every path citing it.
- **D4 — Review scaled to content** [LOAD-BEARING]. An umbrella carrying
  shared Decisions or Constraints & invariants takes a spec campaign; one
  holding only Intent and Children is approved by the operator, as a
  lane note is: drafted and shown with the proposal at step 4, written
  as approved. Brainstorming proposes which at step 4, the operator
  rules, and the ruling is an entry in the brainstorm decision record.
  Neither takes a plan phase or SDD: children write the plans.
- **D5 — The umbrella lands before its first child,** through
  `crucible:finishing-a-development-branch`, so children branch from a
  base that holds it and other sessions can read it. Before it lands,
  the controller runs the record check of SDD Finish step 1 over the
  campaign records, where a campaign ran, and deletes the umbrella's
  workspace: the umbrella never reaches SDD, whose Finish deletes every
  other feature's.
- **D6 — A child's brainstorm takes its entry as input.** The entry is
  an incoming document in brainstorming's sense: what it settles stays
  settled, and the dialogue asks only what it leaves open. The child's
  route is proposed as for any feature.
- **D7 — The pin.** A child's spec, folded document or lane note carries
  a header line ``Umbrella: `<path>` @ `<rev>` ``. The umbrella binds the
  child at that revision with the spec contract's weights: its
  Constraints & invariants and its [LOAD-BEARING] marks. A child that
  edits its umbrella pins the commit carrying that edit.
- **D8 — Edits ride a child.** A child that changes its umbrella edits it
  on the child's own branch, with its Changes line; the edit lands with
  the child, under the child's review. Adding a child or rewording a
  not-yet-started child's entry is lightly held. A change to the
  umbrella's binding content is a decision ask to the operator before
  the edit, as a scoped amendment is. An edit no child causes (dropping
  a child on the operator's word) rides the next child's branch, or a
  branch of its own where no child follows.
- **D9 — State is derived.** A child whose folder is on the base branch
  has landed; one with a branch is in flight; any other has not started.
  Only a dropped child is marked in its entry, with its reason.
  Rationale: no status edits, and none of the sibling conflicts they
  would cause. Rejected: a status field per child.
- **D10 — Closing.** The umbrella closes when every child has landed or
  been dropped; the child whose landing completes that names the closure
  in its close readout, with the dropped children and their reasons (where
  a branch of its own closes it, D8, the controller tells the operator
  the same).
  Whether any of them becomes a backlog item is the operator's call, as
  for any close readout's leftovers. From the close on, the umbrella is
  frozen like any shipped spec.
- **D11 — Resuming an effort.** A session continuing an effort reads the
  umbrella and derives the next child from what has landed. Agent memory
  holds at most a pointer to the umbrella.
- **D12 — No parallel-sibling rule.** The only edits that could
  invalidate a sibling in flight are changes to binding content, and
  those pass through the operator (D8).

## Constraints & invariants

1. An umbrella's binding content reaches a child's seats through the
   pointer every seat already carries (the dispatch composition's item
   4), never through a copied block or a new slot.
2. Each rule this feature adds is stated once, at the site its reader
   acts from; every other site points there.
3. Birth refuses a slug that any folder under the root carries, at any
   depth, and resolve finds a slug's folder at any depth. A slug names
   one feature across the whole tree.
4. A shipped spec is never edited, as before. An umbrella is a shipped
   spec from its close; before that, it changes only by edits carrying
   Changes lines (D8).
5. No committed text this feature writes names a project other than
   crucible or describes a private setup (`AGENTS.md`).

## Interfaces & boundaries

The sites the change touches; the consumer sweep below found them by
search.

- **`skills/brainstorming/SKILL.md`.** The scope-decomposition check
  proposes an umbrella; step 4 proposes the umbrella's review (D4); the
  spec contract gains the pin (D7); the handoff names the umbrella's
  terminal state (campaign, or approval then landing). The umbrella's
  shape and rules (D1, D2, D3's nesting, D5–D11) are in a new reference,
  `skills/brainstorming/references/umbrella.md`, read when an umbrella is
  proposed, written, edited or closed, as `lane-note.md` is read for the
  lane, and under the same stub convention: a heading left in the skill
  with a stub naming the reference, which opens with that heading.
- **`tests/test_skill_references.py`**, its `EXPECTED` set: the new stub
  and reference pair, since the test asserts the set of stubs exactly.
- **`skills/brainstorming/references/lane-note.md`.** A lane note may
  carry the pin.
- **`skills/redteaming/references/formats.md` § Feature folder.** Birth
  under an umbrella; birth and resolve match at any depth; the role name
  `umbrella.md`.
- **`skills/redteaming/SKILL.md`.** § Fix application and blind
  verification's "the artifact states the current design only" gains the
  umbrella's Changes section as its one exception besides the amendment
  marker; § Exit gains the umbrella campaign's handoff (landing, then the
  first child's brainstorm).
- **`skills/subagent-driven-development/references/dispatch-composition.md`**
  item 4: where the binding artifact's header pins an umbrella, the
  umbrella's binding content at that revision binds too, and the seat
  reads it there; recursively up the chain.
- **`skills/subagent-driven-development/SKILL.md` § Finish** step 3: the
  close readout of a child whose landing closes its umbrella names the
  closure (D10).
- **`AGENTS.md`**, the `docs/crucible/` line: children nest in their
  umbrella's folder; an umbrella stays open until it closes.
- **Decision records.** `docs/decisions/records-and-workspace.md`: nested
  folders, and the Rejected bullet on living specs scoped to after
  shipping. The umbrella decision (D1, D2, D4, D7–D10) goes in
  `docs/decisions/the-spec.md` or a new record, by the family it fits.
  Each edit carries its Changes line.
- **Untouched:** writing-plans' spec pointer (the pin travels in the
  spec's own header, which seats read through item 4); the seat templates
  and slot cards; the routes; `agents/` (no template changes); the other
  consumers of the resolve step, which find a nested folder unchanged
  once resolve matches at any depth: finishing's pull-request records
  ask, the supersede's successor placement (`flip-paths.md`), the
  folded lane's unfold and the very-small lane's upgrade hatch.

Deferred to implementation: whether the umbrella decision lives in
`docs/decisions/the-spec.md` or a new record.

Deferred to implementation: the exact wording and placement of each
site's sentence, within Constraint 2.

## Acceptance

1. **Nested folders.** `formats.md` § Feature folder states birth under
   an umbrella and any-depth matching. One-time check: a recursive
   listing of `docs/crucible/` shows each existing folder matched exactly
   once by its slug under the new rule (command and output recorded).
2. **Each rule once.** For each rule in § Interfaces & boundaries, a
   search by its key terms over `skills/`, `AGENTS.md` and
   `docs/decisions/` finds it stated at its owning site and pointed to
   elsewhere. One-time check, recorded as the searches and their output;
   the branch reviewer checks it too.
3. **The reference is reachable.** `skills/brainstorming/references/umbrella.md`
   exists and a stub in `skills/brainstorming/SKILL.md` names it.
   Standing: `tests/test_skill_references.py`, its `EXPECTED` set gaining
   the pair.
4. **Records.** Each edited decision record carries a Changes line dated
   with its commit. Standing: `tests/test_decision_records.py` for
   format; the branch reviewer for presence.
5. **Budgets and suite.** `tests/prose-budget.txt` is updated for each
   skill directory the change grows or shrinks, and the full suite
   (`python -m pytest tests/`) passes on the branch's head.
6. **No local context.** Constraint 5; checked by the branch reviewer,
   as `AGENTS.md` assigns.

Why no new standing test: no code or host reads a feature folder or an
umbrella (a search of `tools/`, `tests/` and `hooks/` found none), and
the repository's test rule allows a text assertion only where one does.
Whether the design works is shown by the first umbrella run on it.

## Mechanism sketches (advisory)

- The reference's outline: when to propose (the decomposition check
  found several sub-features that share decisions, an order, or both);
  the shape (D1); review (D4); landing (D5); children (D3, D6, D7);
  edits (D8); state (D9); closing (D10); resuming (D11).
- The pin line, beside a plan's header pin:
  ``Umbrella: `docs/crucible/2026-11-01-effort/umbrella.md` @ `a1b2c3d` ``.
- The any-depth match: list `<root>` recursively and keep directories
  whose own name is exactly `YYYY-MM-DD-<feature-slug>`; birth creates
  under the umbrella's folder when the feature has one, else under
  `<root>`.
