# Plan: binding and marks

Spec: `docs/crucible/2026-10-28-binding-and-marks/design.md` @ `2985be2` — binding: its Constraints & invariants (C1–C3), its [LOAD-BEARING] marks (none) and any preamble convention it declares binding (none); and, through its `Umbrella:` line, this feature's own entry in `docs/crucible/2026-10-28-hypothesis-specs/umbrella.md` and that umbrella's Constraints & invariants (C1) and [LOAD-BEARING] marks (none). A task calling for a change to those, or any change to the entry (its `landed` mark is SDD Finish's), is a plan defect.

## Goal

The skills state D1's binding set, its intent reading and its stance wherever they state what binds; the scoped amendment is confirmed by the controller where contained, by the test stated once in `flip-paths.md`, and SDD handles the reports that start one; marks take D3's form and the skills place none on their own text; the brainstorm record and the digest use `open` / `accepted` / `firm` with a proposer, and every later operator ruling enters the record; decision-record tasks read that record; the decision records and backlog state the new positions.

## Task dependency order

T1 → T2 → T3 → T4 → T5, strictly sequential: every task edits shared prose that later tasks point at, and T1–T4 all touch `tests/prose-budget.txt`.

## File ownership + overlap census

| File | Owner |
|---|---|
| `skills/redteaming/references/flip-paths.md` | T1 |
| `skills/redteaming/SKILL.md` | T1 |
| `skills/redteaming/references/plan-phase.md` | T1 |
| `skills/redteaming/references/formats.md` | T1 |
| `skills/subagent-driven-development/SKILL.md` | T2 |
| `skills/subagent-driven-development/references/very-small-lane.md` | T2 |
| `skills/requesting-code-review/SKILL.md` | T2 |
| `skills/redteaming/seat-prompt.md` | T3 |
| `skills/redteaming/terminal-pass-prompt.md` | T3 |
| `skills/requesting-code-review/code-reviewer.md` | T3 |
| `skills/subagent-driven-development/task-reviewer-prompt.md` | T3 |
| `skills/subagent-driven-development/re-review-prompt.md` | T3 |
| `skills/subagent-driven-development/implementer-prompt.md` | T3 |
| the six templates' `.slots.md` cards, where a template change needs one | T3 |
| `skills/subagent-driven-development/references/dispatch-composition.md` | T3 |
| `skills/writing-plans/SKILL.md` | T3 |
| `agents/*.md` (regenerated, never hand-edited) | T3 |
| `skills/brainstorming/SKILL.md` | T4 |
| `skills/brainstorming/references/umbrellas.md` | T4 |
| `docs/decisions/the-spec.md`, `decision-records.md`, `adjudication.md`, `task-loop.md`, `branch-review.md`, `spec-campaign.md`, `umbrellas.md`, `plans.md` | T5 |
| `docs/backlog/load-bearing-marks-audit.md` (deleted), `review-catch-and-implementers.md`, `nested-orchestration.md` | T5 |
| `tests/prose-budget.txt` | T1, T2, T3, T4 — **overlap**, each task changing only the lines of the skill directories it edited, in task order |

One overlap only (`tests/prose-budget.txt`), ordered by the strict sequence. The redteaming, subagent-driven-development and requesting-code-review directories are each edited by two tasks (T1/T3, T2/T3, T2/T3), on different files; their budget lines are updated by each in turn.

**Searched and left unchanged** (hits of the tasks' consumer searches — `scoped amendment`, `flip-paths`, `LOAD-BEARING`, `settled`, `structural`, `what the pin`, `Constraints & invariants`, `Umbrella:`, `lightly`, `touching a` — in no task's files): `docs/decisions/authoring-crucible.md` (names `flip-paths.md` as a shared reference), `docs/decisions/records-and-workspace.md`, `docs/decisions/rejected-machinery.md`, `docs/decisions/crucible-suite.md`, `docs/authoring.md`, `docs/backlog/skill-size-after-compaction.md`, `skills/systematic-debugging/defense-in-depth.md` (each another sense of the word); `docs/decisions/routes.md`, `skills/redteaming/references/folded-lane.md` (the small routes' qualifying shape and the stop rule's sense of structural: Non-goal sites); `skills/brainstorming/references/folded-lane-document.md` (names the Constraints section; states no binding set); `docs/backlog/skill-text-rewrite.md` (the mark's two senses in SDD, still true and that item's), `docs/backlog/campaign-early-stop-investigation.md` (the stop rule's sense of structural; `arrangements`' item); `docs/backlog/escalation-and-effort.md`, `docs/backlog/outcome-evidence.md`, `docs/decisions/model-roles-and-effort.md`, `docs/decisions/publication.md`, `AGENTS.md`, `README.md`, `hooks/README.md`, `tests/test_decision_records.py`, `tests/test_instrument_agents.py`, `tests/test_router.py` and `tests/claudeism_scanner_corpus/` (other senses, or a frozen corpus); `tests/test_skill_references.py`, which pins which `SKILL.md` files carry a stub to `flip-paths.md` (see the containment test's contract).

## Inter-task contracts

- **The containment test's home** — produced by T1 in `skills/redteaming/references/flip-paths.md`, under a heading T1 chooses and reports; consumed by T2 (SDD's routing and Deviations paragraph point to it), T3 (templates and dispatch-composition, where they say what a binding finding leads to) and T4 (the spec contract, where it says how binding content changes). Consumers point by file and heading; none restates its conditions (C3). A pointer never takes the stub shape `tests/test_skill_references.py` pins — a "read `<reference>` in full" sentence in a `SKILL.md`: SDD's existing stub to `flip-paths.md` stays its one, and brainstorming gets none.
- **The later-rulings rule's home** — produced by T1 in `skills/redteaming/references/formats.md` § Feature workspace root and layout, beside the decision record's entry; consumed as pointers by T1 itself (redteaming § Round readout, `flip-paths.md`'s asks), T2 (SDD § Disputes and adjudication, where an operator's answer is recorded; the lane reference's re-pin; the branch review's fourth-wave escalation) and T4 (brainstorming § Workspace provisioning).
- **The two correction reports** — produced by T3 in the templates, consumed by T2 in SDD (T2 runs first and writes its handling against this contract; T3 writes the templates to match):
  - the implementer's BLOCKED report on a binding item, naming the item, the evidence that shows it wrong, and a proposed correction — handled in SDD § The Task Loop step 2's BLOCKED triage by the containment test;
  - a reviewer's literal-reading finding, naming the binding item and the case its literal reading reaches that its author did not consider, and saying it is that case — ruled on by the controller (§ Disputes and adjudication, who rules) through the containment test, never sent to the adjudicator as an ordinary dispute.
- **The status vocabulary** — `open`, `accepted`, `firm`, and an entry's proposer (the operator or the controller): T1 states the statuses in the digest format; T4 states them, the proposer and the route-entry rule in the decision record's definition. Both take the words from the spec's D4; the terms are exactly these three.
- **The firm class's wording** — every statement of what binds names it as decisions the spec (or an umbrella) records as the operator's firm preference. T1, T2, T3 and T4 use that phrase or a plain shortening of it; T4's spec contract defines how a spec records one.
- **Plan-phase amendments into the ledger** — T1's `plan-phase.md` names a contained amendment in the plan record's `## Fix list` as an item opening `Contained amendment:` (the item, the change and its reason, the commit), names it in the phase's readout, and seeds it at close as a controller ruling under the ledger's `## Adjudication rulings`. T2's SDD § Setup self-seed copies any such fix-list item the ledger lacks, in the same form.

## Acceptance mapping

| Spec criterion | Task | Check |
|---|---|---|
| A1 — containment test stated once | T1 (failing pre-change run), T4 (final run over `skills/`) | one-time check |
| A2 — no `settled` status; three statuses | T1 (failing pre-change run), T4 (final run over `skills/`) | one-time check |
| A3 — templates, BLOCKED with a proposed correction, spec contract, routing and visibility | T1, T2, T3, T4, each for its sites | why-not: prose fidelity, review-judged at each task and at the branch review |
| A4 — decision-record task input; proposer | T3 (writing-plans), T4 (record entries) | why-not: review-judged |
| A5 — backlog item gone and trimmed | T5 | one-time check |
| A6 — decision records and backlog state the new positions | T5 | why-not: review-judged |
| A7 — no mark on the skills' own text | T1 (failing pre-change run), T4 (final run over `skills/`) | one-time check |
| A8 — suite green, prose budget, generated agents | every task | standing |
| A9 — net word change at landing | none: the controller, in the landing readout | why-not: a landing statement, not a task output |
| D4's later-rulings rule and the route-entry rule, which no A-line covers | T1 (the rule), T2 and T4 (pointers; route entries in T4) | why-not: review-judged at those tasks and the branch review |

## Deferred-items routing table

| id | source (spec or plan site) | one-line intent | owning task |
|---|---|---|---|
| DI-1 | spec, Interfaces & boundaries (marker after Sites) | each template's wording of D1, at the altitude of its existing binding paragraph | T3 |

## Tasks

### T1 — The containment test and the redteaming controller

**Why.** The contained scoped amendment is the feature's one mechanism (D2), and C3 puts its test in one place, `flip-paths.md`, which both controllers read before any flip. This task writes it there, makes redteaming route through it, states what binds where redteaming does (D1), drops redteaming's own mark (D3), handles plan-phase amendments, and gives the later-rulings rule (D4) its home in `formats.md`, which both controllers read.

**Files.** `skills/redteaming/references/flip-paths.md`, `skills/redteaming/SKILL.md` (§ Flip paths, § Round readout, the reporting-stance mark), `skills/redteaming/references/plan-phase.md` (the plan-phase amendment; the conflicting sense of "structural"), `skills/redteaming/references/formats.md` (§ Design digest format's statuses; the later-rulings rule beside the decision record's entry in § Feature workspace root and layout), `tests/prose-budget.txt` (redteaming). Consumer accounting for its searches (`scoped amendment`, `flip-paths`, `LOAD-BEARING`, `settled`, `structural`): hits in SDD's files are T2's, in the templates and `writing-plans` T3's, in brainstorming T4's, in the listed records and backlog items T5's; the rest are in the census's unchanged list.

**Contract.** Enacts D1 (where redteaming states what binds), D2 (the test, plan-patching rulings under it, reversal, plan-phase handling, readouts not the digest), D3 (the redteaming mark), D4 (digest statuses; the later-rulings rule and the pointers from `flip-paths.md` and § Round readout), C1, C2, C3. Produces the test's home, the later-rulings rule's home and the plan-phase fix-list form (Inter-task contracts).

**Acceptance.**
- Happy: `flip-paths.md` states the containment test with every exclusion C1 names, and the scoped amendment's two confirmers; its steps are unchanged.
- Edge: a mark that names nothing, and a plan-patching ruling, are both covered by the test's text; the plan phase lands a contained amendment as a `Contained amendment:` fix-list item, names it in its readout and seeds it at close.
- Error: no site in this task's files restates the test's conditions; § Fix application's acceptance-item sentence is unchanged; `folded-lane.md` is untouched.
- One-time: A1's, A2's and A7's searches run before the change, output quoted; each must fail (no test in `flip-paths.md`; `settled` statuses present; two placed marks present).
- Standing: the suite passes with the redteaming budget line updated.

### T2 — Execution routing: SDD, the lane, the branch review

**Why.** Execution is where most corrections arise. SDD sends every mark-touching ruling to the operator today; under D2 every ruling touching binding content goes through T1's test, contained ones becoming the controller's rulings that reach the branch review and the close readout (C2). SDD must also handle the two correction reports T3's templates will produce. The lane reference and the branch review's dispatch state what an umbrella binds and gain the firm class; the branch review's wave cap loses its mark (D3).

**Files.** `skills/subagent-driven-development/SKILL.md` — § Setup (the ledger's self-seed; the pre-flight plan-conflict scan's umbrella clause and its ruling), § The Task Loop step 2 (BLOCKED triage) and the Deviations paragraph, § Disputes and adjudication (who rules; the adjudicator's marking criterion; where an operator's answer is recorded), § Plan changes mid-execution, § Finish's close readout if its existing ruling line does not already carry contained amendments; `skills/subagent-driven-development/references/very-small-lane.md` (the branch-review item's umbrella clause; a pointer to the later-rulings rule where an operator-approved change re-pins the note); `skills/requesting-code-review/SKILL.md` (the wave-cap mark; the dispatch paragraph's umbrella clause; a pointer to the later-rulings rule where a fourth-wave escalation's answer is recorded); `tests/prose-budget.txt` (subagent-driven-development, requesting-code-review). Consumer accounting for its searches (`LOAD-BEARING`, `touches a`, `plan conflict`, `pending operator`, `Umbrella:` in these two skill directories): template hits are T3's; `references/dispatch-composition.md` is T3's; nothing else.

**Contract.** Consumes T1's test and the later-rulings rule (pointers), and the two correction reports (Inter-task contracts). Enacts D1 (Deviations; the pre-flight scan), D2 (producers, routing, ledger ruling, setup seed), D3 (wave-cap mark), D4 (pointers at its three ruling sites; the lane reference's pointer is D4's, beside its umbrella clause), C1, C2, C3.

**Acceptance.**
- Happy: a ruling touching any binding content (a Constraint, a mark, a firm decision) passes the test; a contained one is recorded as the controller's ruling with its reason and reaches the branch review and the close readout; a BLOCKED report with a proposed correction is triaged through the test.
- Edge: a reviewer's literal-reading finding is the controller's to rule on, not the adjudicator's; a plan conflict that is a design judgment still goes to the operator; § Setup seeds `Contained amendment:` items the plan record names that the ledger lacks; the lane note's own binding parts are untouched.
- Error: no site restates the test's conditions; the very-small-lane change is confined to the umbrella clause and the pointer.
- Standing: the suite passes with both budget lines updated.

### T3 — What binds, in every seat's own words

**Why.** Seats read their templates, not the controller's references: six templates each state what binds. Each states D1's set (the firm class included, in the umbrella clause too), its intent reading and its stance; the reviewer templates produce the literal-reading report and the implementer prompt the BLOCKED report with a proposed correction (D2), in the forms the inter-task contract states; the implementer and the task reviewer of a decision-record task read the decision record their plan task names (D5). `dispatch-composition.md` item 4 and `writing-plans` carry the controller-facing statement of the same, and `writing-plans` adds D5 and the firm class to § Binding vs advisory.

**Files.** `skills/redteaming/seat-prompt.md`, `skills/redteaming/terminal-pass-prompt.md`, `skills/requesting-code-review/code-reviewer.md`, `skills/subagent-driven-development/task-reviewer-prompt.md`, `skills/subagent-driven-development/re-review-prompt.md`, `skills/subagent-driven-development/implementer-prompt.md`, their `.slots.md` cards where a template change needs a slot change, `skills/subagent-driven-development/references/dispatch-composition.md` (item 4), `skills/writing-plans/SKILL.md` (§ Plan header's spec pointer, § Binding vs advisory, D5 where a task's inputs are described), `agents/*.md` (regenerated by `tools/instrument_agents.py write`), `tests/prose-budget.txt` (redteaming, requesting-code-review, subagent-driven-development, writing-plans). Consumer accounting for its searches (`what the pin`, `Constraints & invariants`, `LOAD-BEARING`, `Umbrella:` across `skills/`): hits in `redteaming/SKILL.md` and `flip-paths.md` are T1's, in SDD's `SKILL.md`, the lane reference and the branch review's `SKILL.md` T2's, in brainstorming T4's; `folded-lane.md` and `folded-lane-document.md` are in the census's unchanged list.

**Contract.** Consumes T1's test (pointer, where a template says what a binding finding leads to). Produces the two correction reports (Inter-task contracts). Enacts D1, D2 (the reports), D5. Owns DI-1.

**Acceptance.**
- Happy: each of the six templates states the binding set with the firm class, the intent reading and the stance, at its existing paragraph's altitude; the implementer's BLOCKED names the item, its evidence and a proposed correction.
- Edge: the umbrella clause in every template names firm decisions; a reviewer meeting a literal reading that reaches an unconsidered case reports it as that case, for the controller; a decision-record task's inputs reach both its implementer and its reviewer.
- Error: `agents/` matches the templates (`tools/instrument_agents.py check`); no template restates the containment test; the Lane Fit's qualifying-shape line in `code-reviewer.md` stays as worded.
- Standing: the suite passes, generated-agents check and budget lines included.

### T4 — The spec contract, the decision record, umbrellas

**Why.** Brainstorming is where specs and decision records are written: the spec contract's decision-weight convention takes D1's reading, D3's mark form and guidance, and D4's `firm`; the decision record takes the three statuses, a proposer, the route-entry rule and a pointer to the later-rulings rule, replacing `settled` at the fold and lane entries too. `umbrellas.md` gives an umbrella's firm decisions binding force over its children and makes changing one a binding change (D1, D4). As the last task to edit `skills/`, it runs the final A1, A2 and A7 checks.

**Files.** `skills/brainstorming/SKILL.md` (§ Spec contract, § Workspace provisioning (brainstorm exit), the fold's and the lane's entry paragraphs), `skills/brainstorming/references/umbrellas.md` (§ Children's binding sentence, § Edits' unmarked Decisions), `tests/prose-budget.txt` (brainstorming). Consumer accounting for its searches (`settled`, `lightly`, `LOAD-BEARING`, `unmarked` in `skills/`): the incoming-document `settled` hits stay; `folded-lane-document.md` is in the census's unchanged list; other hits are T1's, T2's or T3's files, already changed.

**Contract.** Consumes T1's test and the later-rulings rule (pointers) and the status vocabulary. Enacts D1, D3, D4, C3.

**Acceptance.**
- Happy: the spec contract states the mark form and what earns one, the narrowed Constraints guidance and how a spec records a firm decision; the record's entries carry status and proposer.
- Edge: an `open` route entry confirms nothing; an umbrella's firm decision binds its children and changing one is a binding change, not a lightly held edit.
- Error: the incoming-document `settled` hits stay; the qualifying-shape lines of the fold and the lane stay as worded; nothing here restates the containment test.
- One-time: A1's, A2's and A7's searches over `skills/` after this task, output quoted, every hit classed as the spec's criteria say.
- Standing: the suite passes with the brainstorming budget line updated.

### T5 — Decision records and the backlog

**Why.** A change that makes a record untrue edits it in the same change (`docs/decisions/decision-records.md`). Eight records state positions this feature changes; three backlog items close or go stale (D6). This task applies D5 to itself: it attributes each position from this feature's brainstorm decision record, whose path the controller names in both its implementer's and its task reviewer's dispatches.

**Files.** `docs/decisions/the-spec.md` (weights and flip paths, the sample's aggregate figures as measured, the contained amendment), `docs/decisions/decision-records.md` (the firm-position sentence), `docs/decisions/adjudication.md` (routing of rulings that touch binding content), `docs/decisions/task-loop.md` (the implementer contract), `docs/decisions/branch-review.md` and `docs/decisions/spec-campaign.md` (their citations of the dropped marks), `docs/decisions/umbrellas.md` (what binds a child), `docs/decisions/plans.md` (the plan phase's handling of a spec found wrong), each with a Changes line dated 2026-10-28; `docs/backlog/load-bearing-marks-audit.md` (deleted), `docs/backlog/review-catch-and-implementers.md` (the decision-record follow-up and the observation supporting only it removed), `docs/backlog/nested-orchestration.md` (its list of mid-run asks). Input, read-only: `.crucible/binding-and-marks/brainstorm-decisions.md` in this worktree. Consumer accounting for its searches (`LOAD-BEARING`, `lightly`, `touching a`, `scoped amendment` in `docs/`): the remaining hits are in the census's unchanged list or under `docs/crucible/`, which is frozen.

**Contract.** Consumes T1–T4's landed text: each record describes the skills as they now read. Enacts D4 (the decision-records sentence), D5 (attribution from the record's proposer and status), D6.

**Acceptance.**
- Happy: each listed record states the current position with its Basis attributed from the brainstorm record (the maintainer's preference only where the record says the operator proposed it; judgment, accepted by the maintainer, where the controller did), and a Changes line.
- Edge: the sample's figures appear only as aggregates, with no other project named (the no-local-context rule); a record that cited a dropped mark still reads true.
- Error: nothing under `docs/crucible/` is edited (shipped specs are frozen; the umbrella's entry mark is SDD Finish's).
- One-time: A5's checks, output quoted, run before the change (both must find their targets) and after.
- Standing: the suite passes.
