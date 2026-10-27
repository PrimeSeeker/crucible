# Umbrella specs — plan

Spec: `docs/crucible/2026-10-27-umbrella-specs/design.md` @ `fdffad2` — binding: its Constraints & invariants (1–4) and its [LOAD-BEARING] mark (D4).

## Goal

Crucible's skill text carries the umbrella: a new brainstorming reference
owning its shape and rules, a stub reaching it, the umbrella line read as
binding at every statement of what binds, the child-controller and
landing sites the spec assigns, and the documentation and decision
records describing it. `agents/` matches its templates, the prose budgets
match the skill directories, and the suite passes.

## Task dependency order

T1 → T2 → T3 → T4 → T5, run in that order. T2–T4 point at T1's
reference; T5 describes and cites what T1–T4 state. Each runs after its
predecessor completes, since several share `tests/prose-budget.txt` and
`skills/subagent-driven-development/SKILL.md` (census below).

## File ownership + overlap census

| File | Owner |
|---|---|
| `skills/brainstorming/references/umbrellas.md` (new) | T1 |
| `skills/brainstorming/SKILL.md` | T1 |
| `skills/brainstorming/references/lane-note.md` | T1 |
| `tests/test_skill_references.py` | T1 |
| `skills/redteaming/references/formats.md` | T2 |
| `skills/redteaming/SKILL.md` | T2 |
| `skills/redteaming/references/flip-paths.md` | T2 |
| `skills/redteaming/seat-prompt.md` | T3 |
| `skills/redteaming/terminal-pass-prompt.md` | T3 |
| `skills/requesting-code-review/code-reviewer.md` | T3 |
| `skills/requesting-code-review/SKILL.md` | T3 |
| `skills/subagent-driven-development/task-reviewer-prompt.md` | T3 |
| `skills/subagent-driven-development/re-review-prompt.md` | T3 |
| `skills/subagent-driven-development/implementer-prompt.md` | T3 |
| `skills/subagent-driven-development/references/very-small-lane.md` | T3 |
| `skills/subagent-driven-development/references/dispatch-composition.md` | T3 |
| `skills/writing-plans/SKILL.md` | T3 |
| the slot cards beside T3's templates, where one changes | T3 |
| `agents/*.md` (generated) | T3 |
| `skills/subagent-driven-development/SKILL.md` | T3 (pre-flight scan, Deviations, adjudicator inputs), T4 (§ Finish) |
| `skills/finishing-a-development-branch/SKILL.md` | T4 |
| `AGENTS.md` | T5 |
| `README.md` | T5 |
| `docs/decisions/records-and-workspace.md` | T5 |
| `docs/decisions/routes.md` | T5 |
| the umbrella decision record (`docs/decisions/the-spec.md` or a new record) | T5 |
| `tests/prose-budget.txt` | T1 (brainstorming), T2 (redteaming), T3 (redteaming, requesting-code-review, subagent-driven-development, writing-plans), T4 (subagent-driven-development, finishing-a-development-branch) |

Overlaps: `skills/subagent-driven-development/SKILL.md` (T3, then T4: disjoint sections) and `tests/prose-budget.txt` (T1–T4, each changing only the lines of the directories it edits; the redteaming and subagent-driven-development lines change twice, in task order). The sequential order resolves both.

## Inter-task contracts

- **The reference and its stub heading.** T1 produces `skills/brainstorming/references/umbrellas.md`, opening with the heading of its stub in `skills/brainstorming/SKILL.md`; T2 (flip-paths, redteaming § Exit), T4 (SDD § Finish, finishing) and T5 (records) point to it by that path and heading, never by the stub's "read … in full" wording, which the suite allows once per reference.
- **The umbrella line.** T1's reference states its form, ``Umbrella: `<path>` `` in an artifact's preamble (spec D7). T3's clause triggers on it ("where its preamble names an umbrella"); T4's § Finish rule keys on it or on a Children list naming the child's slug.
- **Marks and entries.** T1's reference states the mark vocabulary `landed`, `umbrella`, `dropped` and the entry form, entries separated by blank lines (spec D1, D9). T4's § Finish rule writes `landed` in that form.
- **The what-binds clause.** T3 produces one wording, carried at every statement of what binds (spec Constraint 2's exception); T5's records describe it without restating it.
- **Ownership lines.** T2's flip-paths states the child controller's side of D6 and D8; T1's reference states the rest of D6–D8 and points there for a child controller's actions.

## Acceptance mapping

| Spec criterion | Task | Check |
|---|---|---|
| 1. Each rule once in skill text | T5 | one-time: the key-term searches over `skills/` and their output, after T1–T4 |
| 2. Every statement of what binds names the umbrella | T3 | one-time: the eleven statements quoted after the change (pre-change search finds none); standing: `python tools/instrument_agents.py check` in the suite |
| 3. The reference is reachable | T1 | standing: `tests/test_skill_references.py` with the `EXPECTED` pair |
| 4. Records carry Changes lines | T5 | standing: `tests/test_decision_records.py` for sections; the branch reviewer for the lines (why-not for a test: the repo's rule allows no text assertion here) |
| 5. Budgets and suite | T1–T5 | standing: `tests/test_prose_budget.py` and the full suite, run by each task on its head |
| 6. No local context | T1–T5 | why-not: a judgment of committed prose, the branch reviewer's per `AGENTS.md` |

## Deferred-items routing table

| id | source (spec or plan site) | one-line intent | owning task |
|---|---|---|---|
| DI-1 | spec § Interfaces & boundaries, first marker | whether the umbrella decision lives in `docs/decisions/the-spec.md` or a new record | T5 |
| DI-2 | spec § Interfaces & boundaries, second marker | wording and placement of each site's sentence, within Constraint 2 | T1 |
| DI-3 | spec § Interfaces & boundaries, second marker | wording and placement of each site's sentence, within Constraint 2 | T2 |
| DI-4 | spec § Interfaces & boundaries, second marker | wording and placement of each site's sentence, and whether any slot card needs a new value | T3 |
| DI-5 | spec § Interfaces & boundaries, second marker | wording and placement of each site's sentence, within Constraint 2 | T4 |

## T1 — The reference and brainstorming's entry

**Why.** Everything a writer or reader of an umbrella needs lives in one reference loaded on demand, so the always-read brainstorming text grows only by a stub and pointers (spec D1–D11 ownership; Constraint 2). It is the producer every later task points at.

**Files.**
- `skills/brainstorming/references/umbrellas.md` (new): owns D1–D11 as the spec's Interfaces assigns, D5's workspace end aside (that is T2's formats site).
- `skills/brainstorming/SKILL.md`:
  - the stub section;
  - pointers from the scope-decomposition check (§ The dialogue), self-review check 3, step 4's proposals, and the incoming-document paragraph (§ Context gathering);
  - the Flow list's steps 5, 9 and 10, the opening's terminal-state sentence and § Handoff;
  - the spec contract's persistence paragraph (the umbrella line);
  - § Workspace provisioning's lifetime clause, pointing to `formats.md`'s Lifecycle.
- `skills/brainstorming/references/lane-note.md`: the umbrella line in a lane note's preamble.
- `tests/test_skill_references.py`: the `EXPECTED` pair.
- `tests/prose-budget.txt`: the brainstorming line.

Consumers by search: the stub regex in `tests/skill_corpus.py` (read, unchanged); `tests/test_structure.py`'s cited-file and orphan checks (the reference is cited by the stub).

**Contract.**
- Enacts D1–D4 and D6–D11, and D5's landing steps (before the first child, the campaign-record check, the parent mark).
- Produces the reference path and stub heading, the umbrella line's form, and the mark vocabulary and entry form (§ Inter-task contracts).
- Deferred to implementation: DI-2.

**Acceptance.**
- Happy: a session that reaches the scope-decomposition check, check 3 or step 4 with an effort spanning several sub-features is pointed to the reference. The reference states the umbrella's sections, the review choice, the landing steps, the line, the edits, the marks, closing and resuming.
- Edge:
  - an umbrella with only Intent, Acceptance and Mechanism sketches is approval-only;
  - a child in flight when its umbrella is written is entered unmarked;
  - a nested umbrella's entry is marked `umbrella`;
  - a split found mid-campaign replaces the spec.
- Error: a late split is an operator decision ask, never a supersede; a binding change is never edited on a child's branch.
- Integration: the suite passes, including `test_skill_references` with the new pair and `test_structure`'s cited-file and orphan checks, and `test_prose_budget` with the raised brainstorming line.

## T2 — Redteaming's sites: formats, Exit, flip-paths

**Why.** The landing's workspace end, the umbrella campaign's handoff and a child controller's actions on binding changes and late splits are read by controllers that never load brainstorming's reference, so they sit where those controllers act (spec Interfaces; terminal-pass-3 and s9-5 as merged).

**Files.**
- `skills/redteaming/references/formats.md`: § Feature folder's role name `umbrella.md`; § Feature workspace root and layout, Lifecycle, the umbrella's landing as a third end.
- `skills/redteaming/SKILL.md`: § Dispatch composition's seat input list admits the umbrellas; § Exit gains the umbrella campaign's handoff, pointing to the reference for the landing steps.
- `skills/redteaming/references/flip-paths.md`: a child controller's side of D6 and D8, and the supersede and unfold successor's umbrella line.
- `tests/prose-budget.txt`: the redteaming line.

Consumers by search of "lives until SDD Finish or feature abandonment" and "Feature folder": `skills/brainstorming/SKILL.md:108` (T1 points it here); README's workspace sentence (T5; "deleted when the feature finishes" stays true).

**Contract.**
- Enacts D5's workspace end, D6's late split and D8 from a child controller's side, and D7's successor line for a supersede or an unfold.
- Consumes T1's reference path and heading.
- Deferred to implementation: DI-3.

**Acceptance.**
- Happy: Lifecycle names three ends, and § Exit names the umbrella campaign's handoff.
- Edge: flip-paths covers a binding change arriving mid-flight (merge in the base at a boundary, before the base revision is recorded; amend where contradicted) and a successor carrying its predecessor's line.
- Error: a late split or a binding change found by a child's seat goes to the operator as a decision ask, never as an umbrella edit on the child's branch.
- Integration: the suite passes, and `test_prose_budget` passes with the redteaming line.

## T3 — What binds, at every statement of it

**Why.** A child's reviewers read its entry and its umbrella's binding content as binding only where the statement they work from says so, and they may open the umbrella only where their read scope admits it (spec D7; operator ruling A1, the pointer with template edits; Constraint 2's one exception).

**Files.**
- Each of the following gains the clause, and where it has one, its read scope and very-small-lane passage:
  - `skills/redteaming/seat-prompt.md`;
  - `skills/redteaming/terminal-pass-prompt.md`;
  - `skills/requesting-code-review/code-reviewer.md`;
  - `skills/subagent-driven-development/task-reviewer-prompt.md`;
  - `skills/subagent-driven-development/re-review-prompt.md`;
  - `skills/subagent-driven-development/implementer-prompt.md`.
- `skills/subagent-driven-development/SKILL.md`: the pre-flight plan-conflict scan, the Deviations paragraph and the adjudicator dispatch's inputs.
- `skills/requesting-code-review/SKILL.md`: the branch reviewer's inputs.
- `skills/subagent-driven-development/references/very-small-lane.md`: step 3's requirements input, and the upgrade hatch's successor line.
- `skills/subagent-driven-development/references/dispatch-composition.md`: item 2 (input paths up the chain) and item 4 (what the pointer makes binding).
- `skills/writing-plans/SKILL.md`: the spec pointer's "what the pin makes binding".
- The slot cards beside the six templates, only where one must carry an umbrella path.
- `agents/*.md`, regenerated with `python tools/instrument_agents.py write`.
- `tests/prose-budget.txt`: the redteaming, requesting-code-review, subagent-driven-development and writing-plans lines.

Consumers by search: a whitespace-tolerant scan of `skills/` for "preamble convention" found nine hits; the spec lists those plus statements without the phrase. The blind verifier receives no binding content and is untouched.

**Contract.**
- Enacts D7: what binds, the in-range finding rule with its exemptions, and the upgrade-hatch successor line.
- Consumes the umbrella line's form from T1.
- Produces the clause wording.
- Deferred to implementation: DI-4.

**Acceptance.**
- Happy: each of the eleven statements, quoted after the change, carries the clause. A seat's read scope admits the umbrellas, and the controller's input paths include them.
- Edge:
  - a lane-note child's reviewers bind the note's parts plus the entry and umbrella content;
  - a child with no umbrella line binds nothing new;
  - a chain of two umbrellas binds both.
- Error:
  - a change within the reviewed range to the umbrella's Constraints or marks is a finding;
  - so is a change to the child's entry that its spec does not state;
  - the child's own mark is not a finding, and neither is a binding change taken in from the base.
- Integration: `python tools/instrument_agents.py check` passes. The suite passes, including the prose budgets and the claude-ism scanner over the edited templates.

One-time check, recorded: a search of the eleven files for "umbrella", run before the change (no hits) and after (a hit in each statement named).

## T4 — Marks at a child's finish, and the merged-tree exception

**Why.** A child's `landed` mark is written by its own controller at the step every route reaches, and an umbrella's own pull request keeps `umbrella.md` in the merged tree (spec D9, D12).

**Files.**
- `skills/subagent-driven-development/SKILL.md` § Finish: the `landed` mark's timing, including the child in flight when its umbrella was written.
- `skills/finishing-a-development-branch/SKILL.md`, its pull-request records ask: `umbrella.md` is not offered for removal on an umbrella's own pull request.
- `tests/prose-budget.txt`: the subagent-driven-development and finishing-a-development-branch lines.

**Contract.**
- Enacts D9's timing and D12.
- Consumes the mark vocabulary, the entry form and the umbrella line from T1.
- Deferred to implementation: DI-5.

**Acceptance.**
- Happy: a child whose artifact carries an umbrella line marks its entry `landed` before the suite runs. An umbrella's own pull request does not offer `umbrella.md` for removal.
- Edge:
  - a child named by an open umbrella's Children list but carrying no line merges in the base when its tree lacks the umbrella, then marks its entry;
  - a child whose folder is offered for removal is offered as any feature's is.
- Error: a child named by no umbrella writes no mark.
- Integration: the suite passes, and `test_prose_budget` passes with both lines.

## T5 — Documentation, decision records, and the once-only sweep

**Why.** The repository's own documents describe and cite what T1–T4 state, and the decision records keep the reasoning and rejected options, each edit with its Changes line (spec Interfaces; Constraint 2; AGENTS.md).

**Files.**
- `AGENTS.md`: the `docs/crucible/` line, covering the umbrella's role file and that an umbrella stays open until it closes.
- `README.md`: § What it writes into your repository (`umbrella.md`), and a glossary entry if the existing glossary needs one.
- `docs/decisions/records-and-workspace.md`: the third workspace end, the living-specs Rejected bullet scoped to after shipping, and D12 with its trade-off.
- `docs/decisions/routes.md`: an umbrella takes none of the three routes.
- The umbrella decision record: D1–D4, D7–D10 and D12 with their reasons and rejected options. Each Why carries its basis, and the record cites `skills/brainstorming/references/umbrellas.md`.

**Contract.**
- Describes and cites; it states no rule a skill site owns.
- Deferred to implementation: DI-1.

**Acceptance.**
- Happy: each edited record carries a dated Changes line, and `test_decision_records` passes.
- Edge: no committed text names another project or a private setup (Constraint 4).
- Error: a record that restates a skill rule word for word instead of citing it is a defect.
- Integration: the full suite passes on the branch head.

One-time check, recorded: for each rule in the spec's Interfaces, a key-term search over `skills/` finds it stated at its owning site and pointed to elsewhere. The what-binds clause is the exception, stated at all eleven sites.
