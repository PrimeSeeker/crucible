# Umbrella specs — plan

Spec: `docs/crucible/2026-10-27-umbrella-specs/design.md` @ `fdffad2` — binding: its Constraints & invariants (1–4) and its [LOAD-BEARING] mark (D4).

## Goal

Crucible's skill text carries the umbrella:
- a new brainstorming reference owning its shape and rules, with a stub reaching it;
- the umbrella line read as binding at every statement of what binds;
- the child-controller and landing sites the spec assigns, with pointers routing controllers to them;
- the documentation and decision records describing it.

`agents/` matches its templates, the prose budgets match the skill directories, and the suite passes.

## Task dependency order

T1 → T2 → T3 → T4 → T5, run in that order. T2–T4 point at T1's reference, and T5 describes and cites what T1–T4 state. Each runs after its predecessor completes, since several share files (census below).

## File ownership + overlap census

| File | Owner |
|---|---|
| `skills/brainstorming/references/umbrellas.md` (new) | T1 |
| `skills/brainstorming/SKILL.md` | T1 |
| `skills/brainstorming/references/lane-note.md` | T1 |
| `tests/test_skill_references.py` | T1 |
| `skills/redteaming/references/formats.md` | T2 |
| `skills/redteaming/references/flip-paths.md` | T2 |
| `skills/redteaming/SKILL.md` | T2 (§ Exit; the § Flip paths stub's triggers), T3 (§ Dispatch composition) |
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
| `skills/subagent-driven-development/SKILL.md` | T3 (pre-flight scan, Deviations, adjudicator inputs), T4 (§ The Task Loop step 1, § Plan changes mid-execution, § Finish) |
| `skills/finishing-a-development-branch/SKILL.md` | T4 |
| `AGENTS.md` | T5 |
| `README.md` | T5 |
| `docs/decisions/records-and-workspace.md` | T5 |
| `docs/decisions/routes.md` | T5 |
| the umbrella decision record (`docs/decisions/the-spec.md` or a new record) | T5 |
| `tests/prose-budget.txt` | T1 (brainstorming), T2 (redteaming), T3 (redteaming, requesting-code-review, subagent-driven-development, writing-plans), T4 (subagent-driven-development, finishing-a-development-branch) |

There are three overlaps, each between disjoint sections and resolved by the sequential order:
- **`skills/redteaming/SKILL.md`:** T2, then T3.
- **`skills/subagent-driven-development/SKILL.md`:** T3, then T4.
- **`tests/prose-budget.txt`:** T1–T4, each changing only the lines of the directories it edits. The redteaming and subagent-driven-development lines change twice, in task order.

## Inter-task contracts

- **The reference.** T1 produces `skills/brainstorming/references/umbrellas.md`, opening with the heading of its stub in `skills/brainstorming/SKILL.md`. T2 (flip-paths, redteaming § Exit), T4 (SDD, finishing) and T5 (records) point to it by its full path. They never use the stub's "read … in full" wording, which the suite allows once per reference.
- **Child-controller rules.** T2 writes them into `skills/redteaming/references/flip-paths.md`:
  - raising a binding change or a late split as a decision ask;
  - receiving a binding change;
  - a successor's umbrella line on a supersede or unfold.

  T1's reference points there by path, with no section citation, since T1 runs first. T2 adds the triggers to redteaming's § Flip paths stub, and T4 adds them to SDD's § Plan changes mid-execution stub.
- **The umbrella line.** T1's reference states its form, ``Umbrella: `<path>` `` in an artifact's preamble (spec D7). Its consumers:
  - T2: the successor carries it;
  - T3: the clause triggers on it;
  - T4: § Finish keys on it, or on a Children list naming the child's slug.
- **Marks and entries.** T1's reference states the mark vocabulary (`landed`, `umbrella`, `dropped`) and the entry form, with entries separated by blank lines (spec D1, D9). T4's § Finish writes `landed` in that form.
- **How umbrella paths reach a seat, and what binds.** T3 owns the whole rule:
  - dispatch-composition items 2 and 4;
  - redteaming § Dispatch composition's seat input list;
  - each template's read scope and binding statement;
  - any slot card value.

  It is one clause, its grammar fitted to each site (spec Constraint 2's exception). T5's records describe the clause without restating it.
- **Taking in the base.** T2's flip-paths states the receiving side of D8. T4's pointer at SDD § The Task Loop step 1 sends a controller there before it records BASE whenever a binding change is pending.
- **Role-file mentions.** Wherever a SKILL.md names the role file, it uses a placeholder path, for example `<feature-folder>/umbrella.md`. It names the reference by its full path. A bare backticked basename fails `tests/test_structure.py`'s cited-file check.

## Departure from the spec's site list

The spec's § Interfaces & boundaries names `skills/redteaming/references/flip-paths.md` as the owner of a child controller's side of D6 and D8. It does not name the sites that route a controller there. This plan adds three such pointers:
- redteaming's § Flip paths stub triggers (T2);
- SDD's § Plan changes mid-execution stub triggers (T4);
- SDD's § The Task Loop step 1 (T4).

The spec's third non-goal excludes changes to the campaign or SDD beyond the sites it names, and it is lightly held. These three pointers depart from it because Constraint 2 requires each rule to be reachable from the site its reader acts from. They state no rule. A redteaming controller reaches the receiving rule through its stub trigger before a round's dispatch, where it records the round's base revision.

## Acceptance mapping

| Spec criterion | Task | Check |
|---|---|---|
| 1. Each rule once in skill text | T1–T4 for the rules each owns; T5 whole-tree | one-time: key-term searches over `skills/`, run before the change (none found) and after, in each owning task's report; T5 repeats them over the finished tree |
| 2. Every statement of what binds names the umbrella | T3 | one-time: each statement named under What binds, in eleven files, quoted after the change; a search of those files for "umbrella" before the change finds none. Standing: `python tools/instrument_agents.py check` in the suite |
| 3. The reference is reachable | T1 | standing: `tests/test_skill_references.py` with the `EXPECTED` pair |
| 4. Records carry Changes lines | T5 | standing: `tests/test_decision_records.py` for sections. Why-not for the lines themselves: the repo's rule allows no text assertion there, so the branch reviewer checks them |
| 5. Budgets and suite | T1–T5 | standing: `tests/test_prose_budget.py` and the full suite, run by each task on its head |
| 6. No local context | T1–T5 | why-not: a judgment of committed prose, which is the branch reviewer's per `AGENTS.md` |

## Deferred-items routing table

| id | source (spec or plan site) | one-line intent | owning task |
|---|---|---|---|
| DI-1 | spec § Interfaces & boundaries, first marker | whether the umbrella decision lives in `docs/decisions/the-spec.md` or a new record | T5 |
| DI-2 | spec § Interfaces & boundaries, second marker | wording and placement of each site's sentence, within Constraint 2 | T1 |
| DI-3 | spec § Interfaces & boundaries, second marker | wording and placement of each site's sentence, within Constraint 2 | T2 |
| DI-4 | spec § Interfaces & boundaries, second marker | wording and placement of each site's sentence, and whether any slot card needs a new value | T3 |
| DI-5 | spec § Interfaces & boundaries, second marker | wording and placement of each site's sentence, within Constraint 2 | T4 |
| DI-6 | spec § Interfaces & boundaries, second marker | wording and placement of each documentation and record sentence | T5 |

## T1 — The reference and brainstorming's entry

**Why.** Everything a writer or reader of an umbrella needs lives in one reference loaded on demand, so the always-read brainstorming text grows only by a stub and pointers (spec D1–D11; Constraint 2; Interfaces, the reference and brainstorming bullets). Every later task points at it.

**Files.**
- `skills/brainstorming/references/umbrellas.md` (new). It owns D1–D11 as the spec's Interfaces assigns, with two exceptions. D5's workspace end is T2's formats site. A child controller's actions under D6 and D8 are T2's flip-paths, which the reference points to by path.
- `skills/brainstorming/SKILL.md`:
  - the stub section;
  - pointers from the scope-decomposition check (§ The dialogue), self-review check 3, step 4's proposals, and the incoming-document paragraph (§ Context gathering);
  - the Flow list's steps 5, 6, 9 and 10, the opening's terminal-state sentence and § Handoff. Step 6 is the approval-only umbrella's self-review on the draft.
  - the spec contract's persistence paragraph, for the umbrella line;
  - § Workspace provisioning's lifetime clause, pointing to `formats.md`'s Lifecycle.
- `skills/brainstorming/references/lane-note.md`: the umbrella line in a lane note's preamble.
- `tests/test_skill_references.py`: the `EXPECTED` pair.
- `tests/prose-budget.txt`: the brainstorming line.

Consumers found by search, all read and left unchanged:
- the stub regex in `tests/skill_corpus.py`;
- `tests/test_structure.py`'s cited-file and orphan checks: the reference is cited by the stub, and role-file mentions use a placeholder path.

**Contract.**
- Enacts D1–D4 and D6–D11, and D5's landing steps: landing before the first child, the campaign-record check, and the parent mark.
- Produces the reference path and stub heading, the umbrella line's form, and the mark vocabulary and entry form (§ Inter-task contracts).
- Routed item: DI-2.

**Acceptance.**
- Happy:
  - A session reaching the scope-decomposition check, check 3 or step 4 with an effort spanning several sub-features is pointed to the reference.
  - The incoming-document paragraph points a child's brainstorm, and a session resuming an effort, to it.
  - The reference states the umbrella's sections, the review choice, the landing steps, the line, the edits, the marks, closing and resuming.
- Edge:
  - An umbrella with only Intent, Acceptance and Mechanism sketches is approval-only, and its self-review runs on the draft.
  - A child in flight when its umbrella is written is entered unmarked.
  - A nested umbrella's entry is marked `umbrella`.
  - A split found mid-campaign replaces the spec.
- Error: for a late split or a binding change found by a child, the reference sends the reader to `skills/redteaming/references/flip-paths.md` and states neither as a supersede nor as an umbrella edit on the child's branch.
- Integration: the suite passes, including `test_skill_references` with the new pair, `test_structure`'s cited-file and orphan checks, and `test_prose_budget` with the raised brainstorming line.

One-time check for criterion 1, recorded: key-term searches over `skills/` for T1's rules, run before (the rules absent from their owning sites; earlier tasks' pointers may already match) and after.

## T2 — Redteaming's sites: formats, Exit, flip-paths and its stub

**Why.** Some text is read by controllers that never load brainstorming's reference:
- the landing's workspace end;
- the umbrella campaign's handoff;
- a child controller's actions on binding changes, late splits and successors.

So it sits where those controllers act, with the § Flip paths stub routing them there (spec D5–D8; Interfaces, the formats, redteaming and flip-paths bullets).

**Files.**
- `skills/redteaming/references/formats.md`: § Feature folder's role name `umbrella.md`; § Feature workspace root and layout, Lifecycle, the umbrella's landing as a third end.
- `skills/redteaming/SKILL.md`: § Exit gains the umbrella campaign's handoff, pointing to the reference for the landing steps. The § Flip paths stub's triggers gain a binding change to the child's umbrella and a late split.
- `skills/redteaming/references/flip-paths.md`:
  - a child controller's side of D6 and D8: raising a binding change or a late split as a decision ask, never an umbrella edit on the child's branch, and receiving a binding change, as D8 states;
  - the supersede or unfold successor's umbrella line.
- `tests/prose-budget.txt`: the redteaming line.

Consumers found by searching "lives until SDD Finish or feature abandonment", "Feature folder" and the flip-paths triggers: 13 sites in 12 files. The ones this change concerns:
- `skills/brainstorming/SKILL.md`'s provisioning clause (T1 points it here);
- README's workspace sentence: "deleted when the feature finishes" stays true;
- SDD's § Plan changes mid-execution stub (T4).

None of the others needs a change.

**Contract.**
- Enacts D5's workspace end; D6's late split and D8, from a child controller's side; and D7's successor line for a supersede or an unfold.
- Consumes T1's reference path and the umbrella line's form.
- Routed item: DI-3.

**Acceptance.**
- Happy: Lifecycle names three ends, and § Exit names the umbrella campaign's handoff.
- Edge: flip-paths covers a binding change arriving mid-flight, by merging in the base at a boundary before the base revision is recorded and amending where contradicted. It also covers a successor carrying its predecessor's line.
- Error: a late split, or a binding change found by a child's seat, goes to the operator as a decision ask, never as an umbrella edit on the child's branch. The § Flip paths stub's trigger list covers both.
- Integration: the suite passes, and `test_prose_budget` passes with the redteaming line.

One-time check for criterion 1, recorded: key-term searches over `skills/` for T2's rules, run before (the rules absent from their owning sites; earlier tasks' pointers may already match) and after.

## T3 — What binds, at every statement of it

**Why.** A child's reviewers read its entry and its umbrella's binding content as binding only where the statement they work from says so. They may open the umbrella only where their read scope and the controller's input list admit it (spec D7; Constraint 1; Constraint 2's one exception; Interfaces, the What-binds, dispatch-composition and redteaming bullets).

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
- `skills/redteaming/SKILL.md` § Dispatch composition: its seat input list admits the umbrellas.
- `skills/writing-plans/SKILL.md`: the spec pointer's "what the pin makes binding".
- The slot cards beside the six templates, only where one must carry an umbrella path.
- `agents/*.md`, regenerated with `python tools/instrument_agents.py write`.
- `tests/prose-budget.txt`: the redteaming, requesting-code-review, subagent-driven-development and writing-plans lines.

Consumers found by search: a whitespace-tolerant scan of `skills/` for "preamble convention" found nine hits. The spec lists those plus the statements without the phrase: thirteen statements in eleven files. The blind verifier receives no binding content and is untouched.

**Contract.**
- Enacts D7: what binds, the in-range finding rule and its exemptions, and the upgrade-hatch successor line.
- Owns how umbrella paths reach a seat.
- Consumes the umbrella line's form from T1.
- Produces the clause, its grammar fitted to each site.
- Routed item: DI-4.

**Acceptance.**
- Happy:
  - Each statement named under What binds, in eleven files, quoted after the change, carries the clause.
  - Each seat's read scope admits the umbrellas.
  - The controller's input paths, in dispatch-composition and redteaming § Dispatch composition, include them.
- Edge:
  - A lane-note child's reviewers bind the note's parts plus the entry and umbrella content.
  - A child with no umbrella line binds nothing new.
  - A chain of two umbrellas binds both.
- Error:
  - A change within the reviewed range to the umbrella's Constraints & invariants or [LOAD-BEARING] marks is a finding. So is a change to the child's entry, unless it is a clarification the child's spec states that changes nothing another entry waits on (D8).
  - The child's own mark is not a finding, and neither is a binding change taken in from the base.
- Integration: `python tools/instrument_agents.py check` passes. The suite passes, including the prose budgets and the claude-ism scanner over the edited templates.

One-time checks, recorded:
- a search of the eleven files for "umbrella", run before the change (no hits) and after (a hit in each statement named);
- key-term searches over `skills/` for T3's rules, run before and after.

## T4 — Marks, the base merge's entry point, and the merged-tree exception

**Why.** A child's `landed` mark is written by its own controller at the step every route reaches. An SDD controller reaches flip-paths' receiving rules before it records a task's base. An umbrella's own pull request keeps `umbrella.md` in the merged tree. (Spec D8, D9, D12; Interfaces, the SDD § Finish and finishing bullets.)

**Files.**
- `skills/subagent-driven-development/SKILL.md`:
  - § Finish: the `landed` mark's timing, including the child in flight when its umbrella was written;
  - § The Task Loop step 1: a pointer to flip-paths when a binding change to the child's umbrella is pending, before BASE is recorded;
  - § Plan changes mid-execution: its flip-paths stub's triggers gain a binding change and a late split.
- `skills/finishing-a-development-branch/SKILL.md`, its pull-request records ask: `umbrella.md` is not offered for removal on an umbrella's own pull request.
- `tests/prose-budget.txt`: the subagent-driven-development and finishing-a-development-branch lines.

**Contract.**
- Enacts D9's timing and D12, and D8's entry point on the SDD side.
- Consumes the mark vocabulary, the entry form and the umbrella line from T1, and flip-paths' rules from T2.
- Routed item: DI-5.

**Acceptance.**
- Happy:
  - A child whose artifact carries an umbrella line marks its entry `landed` before the suite runs.
  - An umbrella's own pull request does not offer `umbrella.md` for removal.
  - A pending binding change sends the controller to flip-paths before BASE is recorded.
- Edge:
  - A child named by an open umbrella's Children list but carrying no line merges in the base when its tree lacks the umbrella, then marks its entry.
  - A child's own folder is offered for removal as any feature's is.
- Error:
  - A child named by no umbrella writes no mark.
  - A SKILL.md mention of the role file uses a placeholder path, so `test_structure` passes.
- Integration: the suite passes, and `test_prose_budget` passes with both lines.

One-time check for criterion 1, recorded: key-term searches over `skills/` for T4's rules, run before (the rules absent from their owning sites; earlier tasks' pointers may already match) and after.

## T5 — Documentation, decision records, and the whole-tree sweep

**Why.** The repository's own documents describe and cite what T1–T4 state, and the decision records keep the reasoning and rejected options, each edit with its Changes line (spec Constraint 2; Interfaces, the AGENTS, README and decision-records bullets; `AGENTS.md`).

**Files.**
- `AGENTS.md`: the `docs/crucible/` line, covering the umbrella's role file and that an umbrella stays open until it closes.
- `README.md`: § What it writes into your repository (the umbrella's role file), and a glossary entry if the existing glossary needs one.
- `docs/decisions/records-and-workspace.md`: the third workspace end, the living-specs Rejected bullet scoped to after shipping, and D12 with its trade-off.
- `docs/decisions/routes.md`: an umbrella takes none of the three routes.
- The umbrella decision record: D1–D4, D7–D10 and D12 with their reasons and rejected options. Each Why carries its basis, and the record cites `skills/brainstorming/references/umbrellas.md`.

**Contract.**
- Describes and cites; it states no rule a skill site owns.
- Routed items: DI-1, DI-6.

**Acceptance.**
- Happy: each edited record carries a dated Changes line, and `test_decision_records` passes.
- Edge: no committed text names another project or a private setup (Constraint 4).
- Error: a record that restates a skill rule word for word instead of citing it is a defect.
- Integration: the full suite passes on the branch head.

One-time check, recorded: criterion 1's key-term searches over the finished `skills/` tree. Every rule is stated at its owning site and pointed to elsewhere, and the what-binds clause is stated in all eleven files. The same searches over `AGENTS.md`, `README.md`, `docs/*.md` and `docs/decisions/` show those files describing and citing each rule rather than restating it. A miss is reported to the controller as a cannot-verify item naming the owning task.
