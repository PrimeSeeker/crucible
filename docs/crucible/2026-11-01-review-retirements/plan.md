# Plan: review retirements

Spec: `docs/crucible/2026-11-01-review-retirements/design.md` @ `18d5bd6` — binding: its Constraints & invariants (I1–I3); it declares no binding preamble convention and records no firm decision. Through its umbrella line, `docs/crucible/2026-11-01-skill-text-rewrite/umbrella.md`: this feature's own entry (`review-retirements`) and the umbrella's Constraints & invariants (C1–C4); the umbrella records no firm decision. A task calling for a change to those, or to the entry other than a clarification the spec states that changes nothing another entry waits on, is a plan defect. (The spec still names the `[LOAD-BEARING]` marks it retires; neither it nor the umbrella carries one.)

## Goal

The skill text, its templates, generated agents, tests, decision records and the backlog items the umbrella's entry names all state the campaign side of the umbrella as the spec's Decisions R1–R15 give it, with nothing stating a retired mechanism as current (I3), the prose budget's sum at or below 65,978 words, and the three `SKILL.md` files over the compaction line no larger than at `8c14505` (X8).

## Task dependency order

T1 → T2 → T3 → T4 → T5 → T6 → T7 → T8 → T9 → T10, strictly in sequence: most tasks edit the same few files (census below), and each runs from the tree its predecessor left.

## File ownership + overlap census

Each file against the tasks that edit it, in run order; a file edited by several tasks is edited by each in turn, the later task working on the earlier one's result and touching only its own mechanism's words. `agents/*` are regenerated, never hand-edited, by every task that edits their template (`python tools/instrument_agents.py write`). `tests/prose-budget.txt` is edited by every task that changes a skill's word count (Inter-task contracts, X5).

| File | Tasks |
|---|---|
| `skills/redteaming/SKILL.md` | T2, T3, T4, T5, T6, T7, T8, T9 |
| `skills/redteaming/references/formats.md` | T3, T4, T5, T6, T7, T8 |
| `skills/redteaming/references/flip-paths.md` | T1, T2, T6, T8 |
| `skills/redteaming/references/plan-phase.md` | T3, T4, T5, T6 |
| `skills/redteaming/references/folded-lane.md` | T2, T4, T6, T7 |
| `skills/redteaming/seat-prompt.md` | T1, T2, T7 |
| `skills/redteaming/seat-prompt.slots.md` | T2, T7 |
| `skills/redteaming/terminal-pass-prompt.md` | T1, T2, T5 |
| `skills/redteaming/terminal-pass-prompt.slots.md` | T5 |
| `skills/redteaming/scripts/conserve.py` (deleted) | T3 |
| `skills/brainstorming/SKILL.md` | T1, T6 |
| `skills/brainstorming/references/umbrellas.md` | T1, T6, T9 |
| `skills/subagent-driven-development/SKILL.md` | T1, T2, T4, T6 |
| `skills/subagent-driven-development/references/premise-and-questions.md` | T1, T2 |
| `skills/subagent-driven-development/references/dispatch-composition.md` | T1 |
| `skills/subagent-driven-development/references/very-small-lane.md` | T1, T6 |
| `skills/subagent-driven-development/implementer-prompt.md` | T1 |
| `skills/subagent-driven-development/task-reviewer-prompt.md` | T1 |
| `skills/subagent-driven-development/re-review-prompt.md` | T1 |
| `skills/requesting-code-review/SKILL.md` | T1, T4 |
| `skills/requesting-code-review/code-reviewer.md` | T1, T4 |
| `skills/requesting-code-review/code-reviewer.slots.md` | T4 |
| `skills/writing-plans/SKILL.md` | T1, T8 |
| `agents/redteam-seat.md` (generated) | T1, T2, T7 |
| `agents/terminal-pass.md` (generated) | T1, T2, T5 |
| `agents/branch-reviewer.md` (generated) | T1, T4 |
| `agents/implementer.md`, `agents/task-reviewer.md`, `agents/re-reviewer.md` (generated) | T1 |
| `tests/prose-budget.txt` | T1–T9 |
| `tests/test_instrument_agents.py` | T1 |
| `tests/test_conserve.py` (deleted), `tests/instrument_corpus.py`, `tests/test_dispatch_contracts_templates.py`, `tests/test_report_filenames.py` | T3 |
| `tests/test_structure.py` | T6 |
| `README.md`, `docs/authoring.md` | T3 |
| `docs/decisions/the-spec.md` | T1, T6 |
| `docs/decisions/evidence-and-findings.md` | T1, T2 |
| `docs/decisions/umbrellas.md` | T1, T4, T9 |
| `docs/decisions/routes.md` | T1, T6, T8 |
| `docs/decisions/spec-campaign.md` | T2, T3, T4, T5, T6, T7, T8 |
| `docs/decisions/terminal-pass.md` | T2, T5 |
| `docs/decisions/instruments.md` | T2 |
| `docs/decisions/fix-verification-and-merge.md` | T3, T4, T8 |
| `docs/decisions/session-start-hook.md` | T3 |
| `docs/decisions/plans.md` | T3, T4, T8 |
| `docs/decisions/branch-review.md`, `docs/decisions/records-and-workspace.md` | T4 (records-and-workspace also T9) |
| `docs/decisions/operator-steering.md`, `docs/decisions/model-roles-and-effort.md`, `docs/decisions/publication.md` | T6 |
| `docs/crucible/2026-11-01-skill-text-rewrite/umbrella.md` | T9 |
| `docs/backlog/skill-text-rewrite.md`, `lane-entry-and-downshift.md`, `decision-ask-framing.md`, `claude-code-mod.md`, `second-runtime-seat.md`, `umbrella-followups.md` | T10 |

## Inter-task contracts

- **X1. The `deferred-minor` disposition.** Produced by T4: the name `deferred-minor`, its place in the merged list's disposition vocabulary (`formats.md` field 5), and its seeding under the ledger's `## Deferred minors` with source `Spec` or `Plan` (spec R2, Interfaces "Ledger lines"). Consumed by T5 (a second read's leftover MINOR takes it; the spec terminal-pass record and the plan record's `## Terminal pass` list it) and T9 (an umbrella's landing sends its entries to the open-items step).
- **X2. What earlier phases left open, minus `deferred-minor`.** T4 makes `plan-phase.md`'s list exclude `deferred-minor` entries, which go to `## Deferred minors`; T9 names them separately in the umbrella landing's open-items step, which reuses that list.
- **X3. The asks-apart rule's owner.** T6 states it once in `crucible:redteaming` § Round readout; the other readouts point to it, SDD's close readout carrying its own sentence (spec R11). No later task restates it.
- **X4. What binds.** T1 leaves every statement of what binds without marks (R8); T4's definition of "a MINOR against binding text" (R2) refers to that content, not to marks.
- **X5. Prose budget and generated agents.** Each task that changes a skill directory's word count sets that line of `tests/prose-budget.txt` to the new count, and each task that edits a template regenerates `agents/`; the suite (`tests/test_prose_budget.py`, `tests/test_instrument_agents.py`) passes on every task's tree.
- **X6. Decision records and the vocabulary list.** Each task that changes a decision updates its record in place with a dated `## Changes` line (`AGENTS.md`), which names the labels, record lines or statuses the task removes or adds (spec R15); T10 collects them for the landing message.
- **X7. Removed anchors.** T6 removes `formats.md` § Design digest format and renames `crucible:brainstorming` § Digest gate; every citation of either is updated in the same task, and `tests/test_references.py` passes. T3's deletion of `conserve.py` leaves no plugin-root path to it in scanned text (skills, hooks, `docs/decisions/`, `docs/upstream.md`); a record keeping it as history names it bare.
- **X8. Oversized `SKILL.md` files do not grow** (the umbrella's C2, spec A3). Every task that edits `skills/subagent-driven-development/SKILL.md`, `skills/redteaming/SKILL.md` or `skills/brainstorming/SKILL.md` leaves it no larger in bytes than at `8c14505` (46,565, 40,662 and 24,257), measured on its own tree; where its own additions would grow one, it offsets them within its own mechanism's text in that file, and where it cannot, it stops and reports BLOCKED with the figures. Its report records the three sizes.

## Acceptance mapping

- **A1** (no retired mechanism stated) → one-time check, T10, run after T1–T9 on the final tree; each of T1–T9 also runs its own terms' search over its sites (their Acceptance).
- **A2** (the suite passes) → one-time check at Finish by the controller (SDD § Finish); every task also runs the full suite on its own tree (X5).
- **A3** (the sizes) → one-time check at Finish by the controller; X5 keeps the budget's numbers current and X8 the three `SKILL.md` byte sizes within their limits, task by task.
- **A4** (the paths walked) → one-time check by the controller, recorded in the branch review's records (the spec assigns it there); no task discharges it.
- **A5** (the backlog) → one-time check, T10.

## Deferred-items routing table

| id | source (spec or plan site) | one-line intent | owning task |
|---|---|---|---|
| D1 | plan T2, Contract | how the seat template limits the goal check to a spec campaign's round 1 (a selector value or wording) | T2 |
| D2 | plan T2, Contract | where in execution the "tell the operator when a premise finding is raised" rule lives | T2 |
| D3 | plan T5, Contract | how the terminal-pass card selects the record-only second read (a selector value or wording covering both runs) | T5 |
| D4 | plan T6, Contract | the short gate's heading and wording in brainstorming | T6 |

## Tasks

### T1. Retire `[LOAD-BEARING]` marks

**Why.** Marks are the first retirement because statements of what binds appear in nearly every template and many skills; later tasks edit those same files and should find the marks gone. The spec retires marks and keeps the rest of what binds, the umbrella entry marks (`landed`, `umbrella`, `dropped`) untouched.

**Files.** Statements of what binds and the mark's definition: `skills/brainstorming/SKILL.md` (Spec contract Decisions bullet, Constraints bullet, What binds); `skills/redteaming/references/flip-paths.md` (opening paragraph; the containment test's "a mark names what builds on it" clause); `skills/brainstorming/references/umbrellas.md` (§ Children's umbrella line paragraph, § Edits' lightly held and binding-change bullets); `skills/redteaming/seat-prompt.md`, `terminal-pass-prompt.md`; `skills/requesting-code-review/code-reviewer.md`, `SKILL.md` (inputs paragraph); `skills/subagent-driven-development/SKILL.md` (pre-flight scan's statement only, Deviations, adjudicator inputs), `implementer-prompt.md`, `task-reviewer-prompt.md`, `re-review-prompt.md`, `references/dispatch-composition.md` (item 4), `references/very-small-lane.md`, `references/premise-and-questions.md` ("or a mark"); `skills/writing-plans/SKILL.md` (Spec pointer); the regenerated agents of the six templates; `tests/test_instrument_agents.py` (the comment using `[LOAD-BEARING]` as its example); `tests/prose-budget.txt`; decision records `the-spec.md`, `umbrellas.md`, `evidence-and-findings.md`, `routes.md` where they state marks as current. Inputs: the brainstorm decision record (`.crucible/review-retirements/brainstorm-decisions.md`) for each changed record's basis.

**Contract.** Enacts R8. Produces X4. "load-bearing" in other senses (the flip-paths heading, the lens "for whatever this artifact makes load-bearing", the breaker's "real and load-bearing") is not the mark and stays.

**Acceptance.**
- Happy: every statement of what binds names Constraints & invariants, binding preamble conventions and firm decisions, and, for a child, its entry and the umbrella's Constraints and firm decisions with the entry clause's qualifiers (spec R8); none names marks.
- Edge: "the feature's own mark" (the `landed` mark) survives at every site that has it; `Review: branch only` marks untouched.
- Error: a one-time search for `LOAD-BEARING` (case-insensitive) over `skills/`, `agents/`, `tests/` (corpus excluded) and `docs/decisions/`, run before the change (hits) and after (only other senses and history), recorded in the report.
- Integration: the full suite passes; agents regenerated; budget lines current.

### T2. Premise holds, the round-1 lens, the goal check

**Why.** Premise findings stay with their label and routes; only the holds go, and in execution the operator hears of a premise finding when it is raised (R5). The round-1 lens is added (R6), and the goal check narrows to round 1 and the branch review (R7).

**Files.** `skills/redteaming/SKILL.md` (stop rule's hold; mandate 2's "and the hold above"; lens roster; the one-seat round 1); `skills/redteaming/references/flip-paths.md` (§ Premise findings: the stop hold, the execution hold; the execution carrying bullet as the likely home of the tell-the-operator rule); `skills/redteaming/terminal-pass-prompt.md` (stop check's pending-ask mismatch); `skills/redteaming/seat-prompt.md`, `seat-prompt.slots.md` (goal check passages and read scoping); `skills/redteaming/references/folded-lane.md` (round-1 seat's lenses); `skills/subagent-driven-development/references/premise-and-questions.md` (the plan sentence of § The goal check); `skills/subagent-driven-development/SKILL.md` where the execution rule lands, if there; regenerated agents; `tests/prose-budget.txt`; decision records `spec-campaign.md`, `terminal-pass.md`, `evidence-and-findings.md`, `instruments.md`. Inputs: the brainstorm decision record (entries 14, 15).

**Contract.** Enacts R5, R6, R7. Plan-phase and later-round seats keep the request file among their inputs, as grounds for a premise finding; only the goal check's step leaves them.

Deferred to implementation: how the seat template limits the goal check to a spec campaign's round 1 (D1).

Deferred to implementation: where the execution rule lives (D2).

An implementer's own BLOCKED on a premise it cannot go on without (SDD's task loop, the implementer template) is not the retired hold and stays.

**Acceptance.**
- Happy: the stop rule, mandate 2 and the terminal pass's stop check name no premise hold; § Premise findings keeps the label, routes, carrying and the umbrella note; the execution rule says the controller tells the operator when a premise finding is raised; the roster carries the outside-the-frame lens, round 1 only.
- Edge: a one-seat round 1 carries the lens beside general (R6); the folded lane's round-1 seat names it.
- Error: a plan-phase seat dispatched from the card runs no goal check; a later-round spec seat runs none; a round-1 seat and the branch reviewer still do. One-time search for `Reviewing a plan, compare` before (one hit, `premise-and-questions.md`) and after (none).
- Error: one-time search, case-insensitive, for the holds' wording (`holds the stop`, `pending premise ask`, `premise ask was pending`, `waits for the ruling`, `does not stop while`) over `skills/`, `agents/` and `docs/decisions/`, run before (hits, among them `flip-paths.md` § Premise findings, the terminal-pass template's stop check and its agent, `evidence-and-findings.md`, `spec-campaign.md`) and after (history only); these terms join A1's search in T10.
- Integration: the full suite passes; agents regenerated; budget lines current.

### T3. Retire merge conservation

**Why.** The script and its rule caught almost nothing (umbrella Intent); retiring it removes crucible's only workflow Python (R1).

**Files.** Delete `skills/redteaming/scripts/conserve.py` and `tests/test_conserve.py`; `tests/instrument_corpus.py` (`load_conserve`, the docstring), `tests/test_dispatch_contracts_templates.py` (the conserve-based tests and helpers only they use), `tests/test_report_filenames.py` (the conserve reader comment and what it asserts); `skills/redteaming/SKILL.md` (the plan phase's reuse line; seat-id reason; the deferral's conservation clause; Merge conservation, Check it and degraded-verdict paragraphs; the stance's "conservation check"); `skills/redteaming/references/formats.md` (intro, bookkeeping list, field 3's conservation line); `skills/redteaming/references/plan-phase.md` ("merge-conservation rules"); `README.md` (Python requirement); `docs/authoring.md` (the script-invocation example; "cited by other skills and scripts" where no script cites the headings any more); `tests/prose-budget.txt`; decision records `fix-verification-and-merge.md`, `session-start-hook.md`, `plans.md`, `spec-campaign.md`. Inputs: the brainstorm decision record.

**Contract.** Enacts R1. Keeps the `origins:` element, question dispositions, the always-carried rule and Adopted. Seat ids stay unique within a feature, `p0` aside, with the stop check as the reason. Honors X7 for the deleted path. `AGENTS.md`'s Interpreters bullet is a general rule and stays.

**Acceptance.**
- Happy: no skill, record or doc runs or names the script as current; the README lists no Python requirement for users; the suite no longer imports `conserve`.
- Edge: `tests/test_report_filenames.py` asserts nothing whose only named reader was the script (AGENTS.md's test rule); a record keeping the script as history names it bare.
- Error: one-time search for `conserve` and `conservation` (case-insensitive) before (hits) and after (history and the unrelated git-status sense only).
- Integration: the full suite passes, the anchor and path checks included; budget line current.

### T4. Small fix lists and `deferred-minor`

**Why.** Fix waves introduce defects (umbrella Intent); fix lists shrink to BLOCKER, MAJOR and binding-text MINORs, and the other MINORs travel to the branch review's triage (R2).

**Files.** `skills/redteaming/SKILL.md` (disposition list; Deferral precedence; fix list definition and the list of fix lists; the stop round's wave; round 0's fixes; folded and umbrella Exit bullets); `skills/redteaming/references/formats.md` (field 5 vocabulary; field 6); `skills/redteaming/references/plan-phase.md` (one merged wave; repair; Close seeding; What earlier phases left open); `skills/redteaming/references/folded-lane.md` (exit seeding); `skills/subagent-driven-development/SKILL.md` (ledger sources; Setup seeding; branch review handoff); `skills/requesting-code-review/SKILL.md` (the deferred minors' kinds), `code-reviewer.md` (Execution Trail, triage, Ledger Triage), `code-reviewer.slots.md` (`[LEDGER_MINORS]`); `agents/branch-reviewer.md`; `tests/prose-budget.txt`; decision records `fix-verification-and-merge.md`, `spec-campaign.md`, `branch-review.md`, `records-and-workspace.md`, `plans.md`, `umbrellas.md`. Inputs: the brainstorm decision record (entries 3, 6).

**Contract.** Enacts R2. Produces X1 and X2; consumes X4. The terminal pass's wave and second read are T5's; the umbrella landing's step text is T9's.

**Acceptance.**
- Happy: a fix list takes BLOCKER, MAJOR and binding-text MINOR findings, round 0's included; an accepted other MINOR follows the precedence (Interfaces for missing non-local mechanism, `deferred-to-implementation`, `parked`, then `deferred-minor`); the plan phase's and folded closes seed `deferred-minor` entries under `## Deferred minors` with source `Spec` or `Plan`; Setup seeds any missing; the branch reviewer triages them for their effect on the code alone, never editing spec or plan text.
- Edge: a repeated `deferred-minor` is closed as its duplicate and seeded once; a wrong or out-of-scope MINOR stays `rejected`; deferral markers, adopted improvements, rulings and contained amendments still ride fix lists.
- Error: a `deferred-minor` the reviewer leaves parked reaches the close readout with the keep-or-drop proposal (I1).
- Integration: the full suite passes; agent regenerated; budget lines current.

### T5. The terminal pass's wave, the second read, the bias line

**Why.** The terminal pass's follow-up wave takes T4's rule; the second read gains its record-only run, which caught records leaning toward the controller; the bias statement folds to one line keeping its "materially misleading" trigger (R3, R4).

**Files.** `skills/redteaming/SKILL.md` (Mechanics of the terminal pass; the directional-bias sentences; § Operating stance body, heading kept); `skills/redteaming/terminal-pass-prompt.md` (second-read passage; bias paragraph and report line), `terminal-pass-prompt.slots.md` (`follow-up`, report path); `skills/redteaming/references/plan-phase.md` (repair, second read, record); `skills/redteaming/references/formats.md` (`second-read.md` rows; `confirmed`; the terminal-pass record's states and `deferred-minor` list; the plan record's `## Terminal pass`); `agents/terminal-pass.md`; `tests/prose-budget.txt`; decision records `terminal-pass.md`, `spec-campaign.md`. Inputs: the brainstorm decision record (entries 6, 12, 19).

**Contract.** Enacts R3, R4; consumes X1.

Deferred to implementation: how the card selects the record-only run (D3).

The spec's Interfaces "Terminal-pass records" fixes the file name and the states.

**Acceptance.**
- Happy: the record-only second read runs whenever the pass's report carries a record correction or an ask is put again, on the close recorded before it and delivered after it; one second read covers both runs; at most one per pass; its leftover non-binding MINORs take `deferred-minor`.
- Edge: in the plan phase the post-pass close is recorded under `## Terminal pass` and a repair lands before the second read; the spec terminal-pass record reaches `verified` for a record-only read.
- Error: the bias line escalates only where the pass states the record is materially misleading; one-time search for `sharing that direction` over `skills/`, `agents/` and `docs/decisions/` before (hits in the template, its agent and the redteaming skill) and after (history only).
- Integration: the full suite passes, the selector-resolution test included; agent regenerated; budget line current.

### T6. Retire the digest; the short gate; decision asks apart

**Why.** The digest goes and a short gate keeps the operator's stop before a campaign (R13); every readout's decision asks stand in a block after its body (R11).

**Files.** `skills/brainstorming/SKILL.md` (opening; Flow steps; the folded and very-small route lines; the gate; § Design digest; § Digest gate; the decision record's derivation sentence); `skills/redteaming/SKILL.md` (formats intro mention; the gate mentions; readout consumers; the digest readout item; § Round readout's asks rule; Exit's open-judgments clause); `skills/redteaming/references/formats.md` (intro; layout `digest.md`; field 8's digest note and asks block; § Design digest format); `skills/redteaming/references/flip-paths.md` (the digest clauses); `skills/redteaming/references/folded-lane.md`; `skills/redteaming/references/plan-phase.md` (readout pointers); `skills/brainstorming/references/umbrellas.md` (§ Review's digest clause and step numbers; § Landing step 1's digest; the landing ask and closing-review readout pointers); `skills/subagent-driven-development/SKILL.md` (Finish record checks; close readout's own asks sentence); `skills/subagent-driven-development/references/very-small-lane.md`; `tests/test_structure.py` (`digest.md` entry); `tests/prose-budget.txt`; decision records `operator-steering.md`, `the-spec.md`, `spec-campaign.md`, `routes.md`, `model-roles-and-effort.md`, `publication.md`. Inputs: the brainstorm decision record (entries 2, 6).

**Contract.** Enacts R11, R13. Produces X3; honors X7. The gate's heading drops the word "digest", and every citation of `crucible:brainstorming` § Digest gate is updated with it (X7).

Deferred to implementation: the short gate's heading and wording (D4).

A renumbered Flow updates every step citation.

**Acceptance.**
- Happy: brainstorming writes no digest; its gate shows the decision record's decisions and open asks inline and the campaign shape; § Round readout states the asks-apart rule once, the other readouts point to it, SDD's close readout states it in a sentence of its own.
- Edge: a folded or very-small route, an umbrella approved without a campaign: no text still says "no digest" where nothing remains to contrast; Flow step citations resolve.
- Error: a one-time search for `digest` (case-insensitive) before (hits) and after (unrelated senses and history only).
- Integration: the full suite passes, anchor citations included; budget lines current.

### T7. Round 0 on every spec campaign

**Why.** One rule for round 0, fixing the folded lane's wrong reason and retiring the greenfield seat variant (R12).

**Files.** `skills/redteaming/SKILL.md` (§ Round 0); `skills/redteaming/seat-prompt.md` (the `ordered-first` passages), `seat-prompt.slots.md` (the `worksheet` selector's `ordered-first` value); `skills/redteaming/references/folded-lane.md` (round 0's reason); `skills/redteaming/references/formats.md` (round-00 record, wording for no baseline if needed); `agents/redteam-seat.md`; `tests/prose-budget.txt`; `docs/decisions/spec-campaign.md`. Inputs: the brainstorm decision record (entry 4).

**Contract.** Enacts R12. The `worksheet` selector keeps its `pre-pass` value.

**Acceptance.**
- Happy: round 0 runs on every spec campaign; with no code baseline it checks claims against the inputs and liveness.
- Edge: the plan phase's pre-pass, which uses `worksheet: pre-pass`, is unchanged.
- Error: one-time search for `ordered-first` and `greenfield` before (hits) and after (none outside history).
- Integration: the full suite passes, the selector test included; agent regenerated; budget line current.

### T8. The containment exclusion and the re-seat

**Why.** The containment test drops its late-downshift exclusion and keeps the check-passing one (R9); the right-sizing re-seat stops reading line counts (R10).

**Files.** `skills/redteaming/references/flip-paths.md` (the exclusion bullet); `skills/writing-plans/SKILL.md` (the review mark's restatement of that exclusion, its words only); `skills/redteaming/SKILL.md` (right-sizing lens; the trace's line counts); `skills/redteaming/references/formats.md` (field 8's line counts and the trace bullet); `tests/prose-budget.txt`; decision records `plans.md` and `routes.md` (the exclusion's restatements, words only), `spec-campaign.md`, `fix-verification-and-merge.md`. Inputs: the brainstorm decision record (entry 7).

**Contract.** Enacts R9, R10. Leaves `Review: branch only` otherwise to `execution-retirements` (spec Interfaces).

**Acceptance.**
- Happy: the containment test lists four exclusions, the check-passing one included; the re-seat is the controller's judgment on growth.
- Edge: the mark's other text in writing-plans and the records is unchanged but for the exclusion's words.
- Error: one-time search for `numstat` and `line counts` before (hits) and after (the preset-test sense and history only), and for `a task that has not run` before (hits in `flip-paths.md` and a history line of `the-spec.md`) and after (history only).
- Integration: the full suite passes; budget lines current.

### T9. Umbrellas and the umbrella's edits

**Why.** The umbrella landing carries open asks by its two carriers, and the umbrella's own D4 and Interfaces record this child's refinements (R14; spec Interfaces "The umbrella on this branch").

**Files.** `skills/brainstorming/references/umbrellas.md` (§ Landing step 3: other open asks to the operator with the landing ask, unruled ones and `deferred-minor` entries to the open-items home, a ruled one leaving step 3's items); `skills/redteaming/SKILL.md` (Exit's umbrella bullet); `tests/prose-budget.txt`; decision records `umbrellas.md`, `records-and-workspace.md`; `docs/crucible/2026-11-01-skill-text-rewrite/umbrella.md` (D4's digest bullet: the shape stays at the gate; D4's containment bullet: the check-passing exclusion kept; Interfaces' deferred campaign MINORs bullet). Inputs: the brainstorm decision record (entries 2, 3, 7, 13, 17).

**Contract.** Enacts R14; consumes X1, X2. The premise note (step 2) and flip-paths' umbrella carrying bullet stay. The umbrella edits are the lightly held ones the spec lists; the entry's `landed` mark is Finish's.

**Acceptance.**
- Happy: an open premise ask at landing keeps the note; any other open ask goes to the operator and, unruled, to the open-items home with the `deferred-minor` entries.
- Edge: an ask ruled before the landing leaves step 3's committed items.
- Error: the umbrella's Constraints & invariants, its Children entries and its other Decisions are unchanged: a diff of `umbrella.md` from the tree T9 starts on shows only D4's two bullets and the Interfaces bullet. The spec's clarification of this child's entry is stated in the spec, not written into the entry; the entry's `landed` mark is Finish's.
- Integration: the full suite passes; budget line current.

### T10. The backlog and the final search

Review: branch only — it edits backlog items and runs a read-only search, builds no mechanism, and nothing later builds on how it words them.

**Why.** The umbrella's entry names the backlog items this child resolves or trims (A5), and A1's search runs on the final tree.

**Files.** `docs/backlog/skill-text-rewrite.md` (vocabulary point trimmed to what stays; containment-test point; the round-0 half of the predating findings; the mark's half of "load-bearing"), `lane-entry-and-downshift.md` (digest follow-up), `decision-ask-framing.md` (what R3 and R11 answer), `claude-code-mod.md` (the `conserve` half and its re-open trigger), `second-runtime-seat.md` (the `conserve` mention), `umbrella-followups.md` (the size sentence). Inputs: the decision records' Changes lines from T1–T9 (X6).

**Contract.** Discharges A5 and A1. Keeps the no-local-context rule (`AGENTS.md`). An item fully resolved is deleted; a partly resolved one keeps only what stays open.

**Acceptance.**
- Happy: each named item resolved or trimmed, the report saying which; the vocabulary list (X6) assembled for the landing message.
- Edge: a bullet the umbrella leaves to `execution-retirements` (the hatch, the breaker's word, the statements-of-what-binds bullet) stays.
- Error: a hit A1's search finds outside history and unrelated senses is not fixed in T10: it goes in the report as a concern naming the site and the mechanism, and the controller routes it as a plan change, a fix task before the branch review.
- Error: A1's search, case-insensitive, over `skills/`, `agents/`, `tests/` (corpus excluded), `docs/decisions/`, `docs/authoring.md`, `README.md`, `AGENTS.md`, for the spec's terms and the terms T1–T9 named, finds only history and unrelated senses; command and output recorded.
- Integration: the full suite passes.
