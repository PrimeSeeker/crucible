# Plan: binding and marks

Spec: `docs/crucible/2026-10-28-binding-and-marks/design.md` @ `2985be2` — binding: its Constraints & invariants (C1–C3), its [LOAD-BEARING] marks (none), and, through its `Umbrella:` line, this feature's own entry in `docs/crucible/2026-10-28-hypothesis-specs/umbrella.md` and that umbrella's Constraints & invariants (C1) and [LOAD-BEARING] marks (none). A task calling for a change to those, or to the entry beyond its own mark, is a plan defect.

## Goal

The skills state D1's binding set, its intent reading and its stance wherever they state what binds; the scoped amendment is confirmed by the controller where contained, by the test stated once in `flip-paths.md`; marks take D3's form and the skills place none on their own text; the brainstorm record and the digest use `open` / `accepted` / `firm` with a proposer, and every later operator ruling enters the record; decision-record tasks read that record; the decision records and backlog state the new positions.

## Task dependency order

T1 → T2 → T3 → T4 → T5, strictly sequential: every task edits shared prose that later tasks point at, and all of T1–T4 touch `tests/prose-budget.txt`.

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
| `docs/decisions/the-spec.md`, `decision-records.md`, `adjudication.md`, `task-loop.md`, `branch-review.md`, `spec-campaign.md`, `umbrellas.md` | T5 |
| `docs/backlog/load-bearing-marks-audit.md` (deleted), `review-catch-and-implementers.md`, `nested-orchestration.md` | T5 |
| `tests/prose-budget.txt` | T1, T2, T3, T4 — **overlap**, each task changing only the lines of the skill directories it edited, in task order |

One overlap only (`tests/prose-budget.txt`), ordered by the strict sequence. The redteaming, subagent-driven-development and requesting-code-review directories are each edited by two tasks (T1/T3, T2/T3, T2/T3), on different files; their budget lines are updated by each in turn.

## Inter-task contracts

- **The containment test's home** — produced by T1 in `skills/redteaming/references/flip-paths.md`, under a heading T1 chooses and reports; consumed by T2 (SDD's routing of rulings and the Deviations paragraph point to it), T3 (the templates' and dispatch-composition's statements of what a binding finding leads to, where they say so) and T4 (the spec contract, where it says how binding content changes). Consumers point to it by file and heading; none restates its conditions (C3).
- **The later-rulings rule's home** — produced by T1 in `skills/redteaming/references/formats.md` § Feature workspace root and layout, beside the decision record's entry; consumed as pointers by T1 itself (redteaming § Round readout, `flip-paths.md`'s asks), T2 (SDD § Disputes and adjudication, where an operator's answer is recorded) and T4 (brainstorming § Workspace provisioning).
- **The status vocabulary** — `open`, `accepted`, `firm`, and an entry's proposer (the operator or the controller): T1 states the statuses in the digest format; T4 states them, the proposer and the route-entry rule in the decision record's definition. Both take the words from the spec's D4; the terms are exactly these three.
- **The firm class's wording** — every statement of what binds names it as decisions the spec (or an umbrella) records as the operator's firm preference. T2, T3 and T4 use that phrase or a plain shortening of it; T4's spec contract defines how a spec records one.
- **The plan-phase amendment's ledger seeding** — T1's `plan-phase.md` close seeds plan-phase contained amendments into the ledger; T2's SDD § Setup self-seed covers any the plan record names that the ledger lacks.

## Acceptance mapping

| Spec criterion | Task | Check |
|---|---|---|
| A1 — containment test stated once | T1 (its failing pre-change run), T4 (final run over `skills/`) | one-time check |
| A2 — no `settled` status; three statuses | T4 (final run over `skills/`; T1's digest statuses included) | one-time check |
| A3 — templates, BLOCKED with a proposed correction, spec contract, routing and visibility | T1, T2, T3, T4, each for its sites | why-not: prose fidelity, review-judged at each task and at the branch review |
| A4 — decision-record task input; proposer | T3 (writing-plans), T4 (record entries) | why-not: review-judged |
| A5 — backlog item gone and trimmed | T5 | one-time check |
| A6 — decision records and backlog state the new positions | T5 | why-not: review-judged |
| A7 — no mark on the skills' own text | T1 (its failing pre-change run), T2 (final run) | one-time check |
| A8 — suite green, prose budget, generated agents | every task | standing |
| A9 — net word change at landing | none: the controller, in the landing readout | why-not: a landing statement, not a task output |
| D4's later-rulings rule and route-entry confirmation (no A-line; the campaign's open MINOR) | T1 (the rule), T2 and T4 (pointers, route entries) | why-not: review-judged at those tasks and the branch review |

## Deferred-items routing table

| id | source (spec or plan site) | one-line intent | owning task |
|---|---|---|---|
| DI-1 | spec, Interfaces & boundaries (marker after Sites) | each template's wording of D1, at the altitude of its existing binding paragraph | T3 |

## Tasks

### T1 — The containment test and the redteaming controller

**Why.** The contained scoped amendment is the feature's one mechanism (D2), and C3 puts its test in one place, `flip-paths.md`, which both controllers read before any flip. This task writes it there, makes redteaming route through it, drops redteaming's own mark (D3), handles plan-phase amendments, and gives the later-rulings rule (D4) its home in `formats.md`, which both controllers read.

**Files.** `skills/redteaming/references/flip-paths.md`, `skills/redteaming/SKILL.md` (§ Flip paths, § Round readout, the reporting-stance mark), `skills/redteaming/references/plan-phase.md` (the plan-phase amendment; the conflicting sense of "structural"), `skills/redteaming/references/formats.md` (§ Design digest format's statuses; the later-rulings rule beside the decision record's entry in § Feature workspace root and layout), `tests/prose-budget.txt` (redteaming). Consumers of the changed rules: found by searching `skills/` and `docs/` for `scoped amendment`, `flip-paths`, `LOAD-BEARING`, `settled` and `structural`; sites outside this task's files are owned by T2–T5 per the census.

**Contract.** Enacts D2 (the test, plan-patching rulings under it, reversal, plan-phase handling, readouts not the digest), D3 (the redteaming mark), D4 (digest statuses; the later-rulings rule and the pointers from `flip-paths.md` and § Round readout), C1, C2, C3. Produces the test's home and the later-rulings rule's home (Inter-task contracts).

**Acceptance.**
- Happy: `flip-paths.md` states the containment test with every exclusion C1 names, and the scoped amendment's two confirmers; its steps are unchanged.
- Edge: a mark that names nothing, and a plan-patching ruling, are both covered by the test's text; the plan phase lands a contained amendment in its fix list and names it in its readout.
- Error: no site in this task's files restates the test's conditions; § Fix application's acceptance-item sentence is unchanged.
- One-time: A1's and A7's searches run before the change (both must fail: no test in `flip-paths.md`; the redteaming mark present), output quoted.
- Standing: the suite passes with the redteaming budget line updated.

### T2 — Execution routing: SDD, the lane, the branch review

**Why.** Execution is where most corrections arise. SDD's Deviations paragraph and its dispute rules today send every mark-touching ruling to the operator; under D2 every ruling touching binding content goes through T1's test, contained ones becoming the controller's rulings that reach the branch review and the close readout (C2). The lane reference and the branch review's dispatch state what an umbrella binds and gain the firm class; the branch review's wave cap loses its mark (D3).

**Files.** `skills/subagent-driven-development/SKILL.md` (§ Setup's self-seed, the Deviations paragraph, § Disputes and adjudication including the adjudicator's marking criterion and where an operator's answer is recorded, § Plan changes mid-execution, § Finish's close readout if its existing ruling line does not already carry contained amendments), `skills/subagent-driven-development/references/very-small-lane.md` (the branch-review item's umbrella clause only), `skills/requesting-code-review/SKILL.md` (the wave-cap mark; the dispatch paragraph's umbrella clause), `tests/prose-budget.txt` (subagent-driven-development, requesting-code-review). Consumers: by searching for `LOAD-BEARING`, `touches a`, `plan conflict`, `pending operator` and `Umbrella:` in `skills/subagent-driven-development/` and `skills/requesting-code-review/`.

**Contract.** Consumes T1's test (pointer) and the later-rulings rule (pointer). Enacts D1 (Deviations), D2 (producers, routing, ledger ruling, setup seed), D3 (wave-cap mark), D4 (pointer), C1, C2, C3.

**Acceptance.**
- Happy: a ruling touching any binding content (a Constraint, a mark, a firm decision) passes the test; a contained one is recorded as the controller's ruling with its reason and reaches the branch review and the close readout.
- Edge: a plan conflict that is a design judgment still goes to the operator; § Setup seeds plan-phase amendments the plan record names that the ledger lacks; the lane note's own binding parts are untouched.
- Error: no site restates the test's conditions; the very-small-lane change is confined to the umbrella clause.
- One-time: A7's search after this task, output quoted, every hit naming the mark rather than placing one.
- Standing: the suite passes with both budget lines updated.

### T3 — What binds, in every seat's own words

**Why.** Seats read their templates, not the controller's references: six templates each state what binds (r0-2). Each states D1's set (the firm class included, in the umbrella clause too), its intent reading and its stance; the reviewer templates send the literal-reading case to the controller (D2); the implementer reports BLOCKED with evidence and a proposed correction; the implementer and the task reviewer of a decision-record task read the decision record their plan task names (D5). `dispatch-composition.md` item 4 and `writing-plans` carry the controller-facing statement of the same, and `writing-plans` adds D5 and the firm class to § Binding vs advisory.

**Files.** `skills/redteaming/seat-prompt.md`, `skills/redteaming/terminal-pass-prompt.md`, `skills/requesting-code-review/code-reviewer.md`, `skills/subagent-driven-development/task-reviewer-prompt.md`, `skills/subagent-driven-development/re-review-prompt.md`, `skills/subagent-driven-development/implementer-prompt.md`, their `.slots.md` cards where a template change needs a slot change, `skills/subagent-driven-development/references/dispatch-composition.md` (item 4), `skills/writing-plans/SKILL.md` (§ Plan header's spec pointer, § Binding vs advisory, D5 where a task's inputs are described), `agents/*.md` (regenerated by `tools/instrument_agents.py write`), `tests/prose-budget.txt` (redteaming, requesting-code-review, subagent-driven-development, writing-plans). Consumers: every statement of what binds, found by searching for `what the pin`, `Constraints & invariants`, `LOAD-BEARING` and `Umbrella:` across `skills/`; those outside these files are T2's and T4's.

**Contract.** Consumes T1's test (pointer, where a template says what a binding finding leads to). Enacts D1, D2 (reviewers' literal-reading route; BLOCKED with a proposed correction), D5. Owns DI-1.

**Acceptance.**
- Happy: each of the six templates states the binding set with the firm class, the intent reading and the stance, at its existing paragraph's altitude; the implementer's BLOCKED carries evidence and a proposed correction.
- Edge: the umbrella clause in every template names firm decisions; a reviewer meeting a literal reading that reaches an unconsidered case sends it to the controller, not as a finding that binding content is wrong; a decision-record task's inputs reach both its implementer and its reviewer.
- Error: `agents/` matches the templates (`tools/instrument_agents.py check`); no template restates the containment test.
- Standing: the suite passes, generated-agents check and budget lines included.

### T4 — The spec contract, the decision record, umbrellas

**Why.** Brainstorming is where specs and decision records are written: the spec contract's decision-weight convention takes D1's reading, D3's mark form and guidance, and D4's `firm`; the decision record takes the three statuses, a proposer, the route-entry rule and a pointer to the later-rulings rule, replacing `settled` at the fold and lane entries too. `umbrellas.md` gives an umbrella's firm decisions binding force over its children and makes changing one a binding change (D1, D4).

**Files.** `skills/brainstorming/SKILL.md` (§ Spec contract, § Workspace provisioning (brainstorm exit), the fold's and the lane's entry paragraphs), `skills/brainstorming/references/umbrellas.md` (§ Children's binding sentence, § Edits' unmarked Decisions), `tests/prose-budget.txt` (brainstorming). Consumers: by searching `skills/` for `settled`, `lightly`, `LOAD-BEARING` and `unmarked`; the incoming-document sense of `settled` stays.

**Contract.** Consumes T1's test and the later-rulings rule (pointers) and the status vocabulary. Enacts D1, D3, D4, C3.

**Acceptance.**
- Happy: the spec contract states the mark form and what earns one, the narrowed Constraints guidance and how a spec records a firm decision; the record's entries carry status and proposer.
- Edge: an `open` route entry confirms nothing; an umbrella's firm decision binds its children and changing one is a binding change, not a lightly held edit.
- Error: the incoming-document `settled` hits stay; nothing here restates the containment test.
- One-time: A1's and A2's searches over `skills/` after this task, output quoted and every hit classed as the spec's criteria say.
- Standing: the suite passes with the brainstorming budget line updated.

### T5 — Decision records and the backlog

**Why.** A change that makes a record untrue edits it in the same change (`docs/decisions/decision-records.md`). Seven records state positions this feature changes; three backlog items close or go stale (D6). This task applies D5 to itself: it attributes each position from this feature's brainstorm decision record.

**Files.** `docs/decisions/the-spec.md` (weights and flip paths, the sample's aggregate figures as measured, the contained amendment), `docs/decisions/decision-records.md` (the firm-position sentence), `docs/decisions/adjudication.md` (routing of rulings that touch binding content), `docs/decisions/task-loop.md` (the implementer contract), `docs/decisions/branch-review.md` and `docs/decisions/spec-campaign.md` (their citations of the dropped marks), `docs/decisions/umbrellas.md` (what binds a child), each with a Changes line dated 2026-10-28; `docs/backlog/load-bearing-marks-audit.md` (deleted), `docs/backlog/review-catch-and-implementers.md` (the decision-record follow-up and the observation supporting only it removed), `docs/backlog/nested-orchestration.md` (its list of mid-run asks). Input, read-only: the brainstorm decision record at `.crucible/binding-and-marks/brainstorm-decisions.md` in this worktree. Consumers: by searching `docs/` for `LOAD-BEARING`, `lightly`, `touching a` and `scoped amendment`.

**Contract.** Consumes T1–T4's landed text: each record describes the skills as they now read. Enacts D4 (the decision-records sentence), D5 (attribution from the record's proposer and status), D6.

**Acceptance.**
- Happy: each listed record states the current position with its Basis attributed from the brainstorm record (the maintainer's preference only where the record says the operator proposed it; judgment, accepted by the maintainer, where the controller did), and a Changes line.
- Edge: the sample's figures appear only as aggregates, with no other project named (the no-local-context rule); a record that cited a dropped mark still reads true.
- Error: nothing under `docs/crucible/` is edited (shipped specs are frozen; the umbrella's entry mark is SDD Finish's).
- One-time: A5's checks, output quoted, run before the change (both must find their targets) and after.
- Standing: the suite passes.
