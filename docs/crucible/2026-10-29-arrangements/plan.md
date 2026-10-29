# Arrangements — implementation plan

Spec: `docs/crucible/2026-10-29-arrangements/design.md` @ `65d4bfa` — binding: its Constraints & invariants (C1–C4), any preamble convention it declares binding, and the decisions it records as the operator's firm preference (none); through its `Umbrella:` line, this feature's own entry in `docs/crucible/2026-10-28-hypothesis-specs/umbrella.md` and that umbrella's Constraints & invariants, [LOAD-BEARING] marks and firm decisions. The spec carries no [LOAD-BEARING] marks. A task calling for a change to those, or to the entry other than D3's stated clarification and D8's Intent edit, is a plan defect.

## Goal

The installed skills carry the arrangement model: four choices with three presets proposed at step 4; the overturn question as the step-4 selector and the spec campaign's stop, with the seats' forecast line and the terminal pass's stop check; the plan's `Review: branch only` mark, run in execution and reviewed first by the branch reviewer; the inline criterion; the operator-confirmed downshift. The decision records, README, backlog and umbrella state the positions D15 and D8 name. The suite passes.

No task carries a `Review: branch only` mark: the install this plan runs under predates the mark.

## Task dependency order

T1 → T2 → T3 → T4 → T5 → T6 → T7, run in sequence. T1 produces the definitions every later task points to. T5 and T6 share the completion line, the slot and the per-task line (Inter-task contracts). T7 records what T1–T6 shipped and runs the repository-wide acceptance searches.

## File ownership + overlap census

| File | Owning task |
|---|---|
| `skills/subagent-driven-development/references/premise-and-questions.md` | T1 |
| `skills/redteaming/SKILL.md` | T2 |
| `skills/redteaming/references/formats.md` | T2 |
| `skills/redteaming/seat-prompt.md`, `agents/redteam-seat.md` | T2 |
| `skills/redteaming/terminal-pass-prompt.md`, `skills/redteaming/terminal-pass-prompt.slots.md`, `agents/terminal-pass.md` | T2 |
| `skills/brainstorming/SKILL.md` | T3 |
| `skills/redteaming/references/folded-lane.md` | T3 |
| `skills/subagent-driven-development/references/very-small-lane.md` | T3 |
| `skills/writing-plans/SKILL.md` | T4 |
| `skills/redteaming/references/plan-phase.md` | T4 |
| `skills/redteaming/references/flip-paths.md` | T4 |
| `skills/subagent-driven-development/SKILL.md` | T5 |
| `skills/subagent-driven-development/implementer-prompt.md`, `agents/implementer.md` | T5 |
| `skills/subagent-driven-development/task-reviewer-prompt.slots.md`, `agents/task-reviewer.md` | T5 |
| `skills/requesting-code-review/SKILL.md` | T6 |
| `skills/requesting-code-review/code-reviewer.md`, `skills/requesting-code-review/code-reviewer.slots.md`, `agents/branch-reviewer.md` | T6 |
| `tests/instrument_corpus.py` (only if T6 raises the card budget) | T6 |
| `README.md` | T7 |
| `docs/decisions/*.md` (each record that states what changed; D15 names `routes.md`, `spec-campaign.md`, `task-loop.md`, `branch-review.md`, `plans.md`, `umbrellas.md`) | T7 |
| `docs/backlog/review-catch-and-implementers.md` (deleted), `docs/backlog/lane-entry-and-downshift.md`, `docs/backlog/campaign-early-stop-investigation.md`, `docs/backlog/review-seat-report-write.md` | T7 |
| `docs/crucible/2026-10-28-hypothesis-specs/umbrella.md` (D8's Intent edit only) | T7 |
| `tests/prose-budget.txt` | shared, see below |

**Overlaps.** One: `tests/prose-budget.txt`. Each task that changes a skill directory's word count updates that directory's line in its own commit (AGENTS.md, the prose budget), so T1–T6 touch it in sequence, never concurrently; `subagent-driven-development` changes in T1, T3 and T5, `redteaming` in T2, T3 and T4. `agents/` files are generated (`python tools/instrument_agents.py write`), each from one template, so each is owned by its template's task. No other file has two owners.

## Inter-task contracts

- **The arrangement questions' home** — T1 produces a `##` section of `premise-and-questions.md` titled `The arrangement questions`, holding the overturn question (with its two "no" cases and its reading for an umbrella's campaign), "overdetermined", and the mark's criterion. Consumers point to it as `skills/subagent-driven-development/references/premise-and-questions.md` § The arrangement questions and never restate it (C1): T2 (stop rule, seat forecast line, terminal pass stop check, seat template's section list), T3 (step-4 subsection, the lane reference's inline test and Lane Fit hatch reading), T4 (writing-plans' mark, plan-phase seats grading marks), T5 (SDD § Inline mode), T6 (Lane Fit, branch reviewer's section list).
- **The step-4 subsection** — T3 produces the brainstorming subsection proposing the arrangement, which holds D1's table and unsupported list (C1). The two `### … — proposing the fold (step 4)` and `… — proposing the lane (step 4)` headings go; the step-5 headings (`… — the combined spec+plan document (step 5)`, `… — the lane note (step 5)`) stay, since `very-small-lane.md` cites the latter. Consumers that name the arrangement by its step-4 home point there.
- **The forecast line** — T2 produces it in the seat template (`spec` kind only), form as spec D7; T2's terminal pass reads it.
- **The mark** — T4 produces the plan line `Review: branch only — <reason>` (writing-plans); T5 reads it in the task loop; T6 reads which tasks carried it through the ledger's completion line.
- **The completion line** — T5 produces `Task <N>: complete (commits <base7>..<head7>, branch review only)` in SDD's ledger forms; T6 fills `[BRANCH_ONLY_TASKS]` from these lines and the plan.
- **Amendment commits for a marked task's range** — T4 changes flip-paths' step 3 to name them to the branch reviewer for a marked task's range; T6 carries them in `[BRANCH_ONLY_TASKS]`.
- **The per-task line** — T6 produces it in the branch reviewer's output format, in the first full-scope pass's report (`sdd/branch-review/pass-1.md`); T5's Finish per-task record check reads it in place of the review file for a branch-review-only task, and T6's requesting-code-review refuses a first pass missing one. T5 names it by this description before T6 defines its form.
- **Lane Fit's verdict words** — WITHIN SHAPE and EXCEEDS SHAPE keep their names and forms (C2): T6 re-defines what they judge (D4); T3's lane reference reads EXCEEDS SHAPE as opening the upgrade hatch.

## Acceptance mapping

| Criterion | Task | Check |
|---|---|---|
| A1 | T3 (skills/), T7 (all paths) | One-time. T3 runs the before search over all A1 paths and its after over `skills/`; T7 runs the after over every A1 path. |
| A2 | T7 | One-time, after T1–T6 have landed. |
| A3 | T2 (skills/), T7 (all paths) | One-time. T2 runs the before over all A3 paths and the after over `skills/`; T7 the after over every path. |
| A4 | T2 | Why neither: prose fidelity, judged by T2's review. |
| A5 | T6 | Standing: `python tools/instrument_agents.py check` in the suite; the rest by T6's review. |
| A6 | T6 | Why neither: a trace by review, task-review check by check, against T5's gates and T6's reviewer mandate. |
| A7 | T5 (SDD), T3 (lane), T7 (all paths) | One-time. T3 runs the before over all A7 paths; T3 and T5 the after over their files; T7 the after over every path. |
| A8 | T7 | One-time: the file list and a diff stat, quoted. |
| A9 | every task; T7 last | Standing: `python -m pytest tests/`, its summary line quoted. |
| A10 | T7 | Why neither: a report. T7 computes the net word change to `skills/` across the branch from `tests/prose-budget.txt` and states what was removed; the landing quotes it. |
| A11 | T7 | Why neither: prose, judged by T7's review. |

## Deferred-items routing table

| id | source (spec or plan site) | one-line intent | owning task |
|---|---|---|---|
| DI-1 | spec Interfaces, first marker | wording and placement of each pointer to the arrangement questions' home | T2 |
| DI-1 | spec Interfaces, first marker | wording and placement of each pointer to the arrangement questions' home | T3 |
| DI-1 | spec Interfaces, first marker | wording and placement of each pointer to the arrangement questions' home | T4 |
| DI-1 | spec Interfaces, first marker | wording and placement of each pointer to the arrangement questions' home | T5 |
| DI-1 | spec Interfaces, first marker | wording and placement of each pointer to the arrangement questions' home | T6 |
| DI-2 | spec Interfaces, second marker | where in the branch reviewer's template the text for branch-review-only tasks sits | T6 |
| DI-3 | spec Interfaces, third marker | how the new slot fits the card budget: a trim of card text or a raised budget with its reason | T6 |

## T1 — The arrangement questions' home

**Why.** C1 gives four definitions one home each; three of them, the overturn question, "overdetermined" and the mark's criterion, live in one new section of the shared reference every seat already reads (spec Interfaces, "The arrangement questions"), so every later task points instead of restating. The reference's opening scope sentence widens to the controllers that apply the section.

**Files.** `skills/subagent-driven-development/references/premise-and-questions.md`; `tests/prose-budget.txt` (its `subagent-driven-development` line). Consumers of the file: the templates and skills that point to it (`skills/brainstorming/SKILL.md`, `skills/redteaming/seat-prompt.md`, `skills/redteaming/SKILL.md`, `skills/requesting-code-review/code-reviewer.md`, `skills/subagent-driven-development/implementer-prompt.md`, `skills/subagent-driven-development/task-reviewer-prompt.md`, `skills/redteaming/references/flip-paths.md`; records `docs/decisions/evidence-and-findings.md`, `docs/decisions/instruments.md`): the existing sections keep their headings, so these stay valid; the new pointers are T2–T6's, the records T7's. The file's own "structural" use (its premise-finding paragraph) is D9's to judge: it refers to an ordinary finding, so it stays unless the new section makes it ambiguous.

**Contract.** Produces § The arrangement questions (Inter-task contracts). Enacts D2's definitions (the question, its two "no" cases), the umbrella-campaign reading (Interfaces), D14's "overdetermined", D10's mark criterion; C1.

**Acceptance.**
- Happy: the section exists under the pinned heading and states each of the four items once; the scope sentence names the controllers that apply it.
- Edge: an umbrella's campaign, whose "after code" is its children's code, has a stated reading; "overdetermined" reads the same for the step-4 selector and the inline criterion (one sense, spec D14).
- Error: no second statement of any of the four elsewhere in the file.
- Integration: the suite passes (A9), the prose-budget line raised with the reason in the commit body.

## T2 — The stop rule, the forecast line and the terminal pass's stop check

**Why.** D6–D9 move the spec campaign's stop from severity plus "structural" to the overturn question, have every spec-kind seat forecast it, and give the terminal pass a check of the stop basis against every numbered round's forecasts; the cap stays, with "the cap bounds rounds, not spend". The readout's structural item becomes the overturn item at both its sites.

**Files.** `skills/redteaming/SKILL.md` (§ Panels calibration, § Round readout's item, § Stop rule and terminal pass: trigger, open-findings wave, the re-shape rule, at least one panel round, the cap clause, the terminal pass's inputs; § Dispatch composition's shared-reference grant extended to instrument `terminal-pass`); `skills/redteaming/references/formats.md` (§ Round record format's readout item; a `##` heading is frozen, its body is not); `skills/redteaming/seat-prompt.md` (the forecast line in `## Verdict` for `spec` kind; the shared reference's section list gains § The arrangement questions); `skills/redteaming/terminal-pass-prompt.md` and `terminal-pass-prompt.slots.md` (the stop check; a plugin-root slot); `agents/redteam-seat.md`, `agents/terminal-pass.md` (regenerated); `tests/prose-budget.txt` (`redteaming`). Consumers to account for, by search for "structural", "zero BLOCKERs", "stop rule", "stop round" and "Verdict" over `skills/redteaming/`: the "structural" sites D9 keeps (flip-paths' supersede and containment, T4's file) and the ones it re-expresses here (§ Panels, the cap clause); flip-paths' premise-ruling site and folded-lane's unfolding site are T4's and T3's. `tests/test_instrument_agents.py` and `tests/instrument_corpus.py` read the slot cards; the terminal-pass card stays within its budget.

**Contract.** Consumes T1's home. Produces the forecast line and the stop check (Inter-task contracts). Enacts D6, D7, D8 (the redteaming half), D9 (§ Panels and cap-clause sites), the readout-item interface; DI-1.

**Acceptance.**
- Happy: the stop rule states the overturn trigger and the re-shape rule; a `spec`-kind seat's Verdict asks for the forecast line in D7's form; the terminal pass's inputs include every numbered round's seat reports' `## Verdict` sections and its stop check flags a mismatch CONCLUSION-CHANGING (A4).
- Edge: a `plan`-kind seat gets no forecast line; the plan phase's readout carries no overturn item (it carries no structural item today); a one-seat round and an umbrella campaign's seats (kind `spec`) are covered.
- Error: a stop round whose seats all forecast "not plausible" while an earlier round's plausible forecast stands unanswered is flagged (A4's reproducer).
- Integration: A3's before search (all its paths) and after search over `skills/`, quoted; the readout item reads the same in `SKILL.md` and `formats.md`; `python tools/instrument_agents.py check` passes; the suite passes.

## T3 — Step 4 proposes the arrangement

**Why.** D1–D3 replace the two route-entry subsections, the shape test and the "worth reviewing" split with one subsection proposing a preset by the overturn question, holding D1's table and unsupported list (C1), with a route entry for every preset. D4's hatch reading, D9's unfolding site, D10's folded-campaign grading and D14's lane half live in the two route references.

**Files.** `skills/brainstorming/SKILL.md` (the step-4 subsection replacing `### The folded lane — proposing the fold (step 4)` and `### The very-small lane — proposing the lane (step 4)`; the Flow's step 4; the overview's and the minor-design lines naming the shape test; the route entry written for every preset); `skills/redteaming/references/folded-lane.md` (its shape-test lines; the unfolding judged by whether the work needs a separate plan, D9; the folded campaign's seats grade marks and its close readout lists them, D10); `skills/subagent-driven-development/references/very-small-lane.md` (its qualifying-shape lines; the inline test, D14's lane half; the upgrade hatch reading EXCEEDS SHAPE as an overturn plausible after code, D4); `tests/prose-budget.txt` (`brainstorming`, `redteaming`, `subagent-driven-development`). Consumers, by search for "no new mechanism", "blast radius", "worth reviewing", "qualifying shape", "proposing the fold", "proposing the lane" and "wide enough to crowd" over `skills/`: the hits in `code-reviewer.md` are T6's, in `README.md` and `docs/decisions/` T7's; the step-5 heading `very-small-lane.md` cites stays (Inter-task contracts).

**Contract.** Consumes T1's home. Produces the step-4 subsection (Inter-task contracts). Enacts D1, D2, D3, D4 (the hatch reading), D9 (the unfolding site), D10 (the folded campaign's grading), D14 (the lane), C2; DI-1.

**Acceptance.**
- Happy: one step-4 subsection names a preset, the overturn answer with its reason and, for folded, the plan-size reason; D1's table and unsupported list appear there only; a standard-preset route entry is written like the other two.
- Edge: an umbrella's review stays chosen by content (D2); a folded feature stays a minor design with no digest; a settled change one implementer can carry goes to the very-small preset with a dispatched implementer, and a multi-task one to the standard preset (D2).
- Error: no surviving shape-test or "worth reviewing" statement in `skills/`; the lane's inline default and the hatch still work on the unchanged verdict words (C2).
- Integration: A1's before search over all its paths and after over `skills/`, quoted; A7's before over all its paths and after over `very-small-lane.md`, quoted; the suite passes.

## T4 — The mark at plan time, and the flip paths

**Why.** D10 lets a plan task carry `Review: branch only — <reason>` where it meets the criterion in T1's home; the plan phase's seats grade marks and its close readout lists them. D13 puts marking unrun tasks in the containment test's never-contained list. Flip-paths also holds D9's premise-ruling site and D11's amendment-commit rule (step 3 of a plan patch), which names the commits to the branch reviewer for a marked task's range.

**Files.** `skills/writing-plans/SKILL.md` (the mark, pointing to the criterion; § Task sizing's reviewer-gate rationale; § Per-task structure where it lists task fields); `skills/redteaming/references/plan-phase.md` (seats grade marks; the close readout lists marked tasks, as information); `skills/redteaming/references/flip-paths.md` (§ Premise findings' "makes its round structural", D9; step 3's amendment commits, D11; § The containment test's never-contained list, D13; the supersede and containment uses of "structural" stay); `tests/prose-budget.txt` (`writing-plans`, `redteaming`). Consumers, by search for "reviewer's gate", "Per-task structure", "never contained" and "amendment commit" over `skills/` and `docs/decisions/`: `docs/decisions/plans.md` (reviewer's gate) is T7's; the SDD task loop's reading of the mark is T5's; the slot carrying the commits is T6's.

**Contract.** Consumes T1's home. Produces the mark line and the amendment-commit naming (Inter-task contracts). Enacts D9 (premise site), D10, D11 (flip-paths' site), D13, C4; DI-1.

**Acceptance.**
- Happy: writing-plans states the mark line's form and points to the criterion; the plan phase's close readout lists marked tasks; marking an unrun task after the plan phase is never contained.
- Edge: a plan with no marked task changes nothing in the plan phase's readout; a folded document's marks are T3's site, not restated here.
- Error: a contained amendment that adds a mark is impossible by the never-contained list; a premise ruling that makes an overturn plausible again is stated without "structural".
- Integration: the suite passes.

## T5 — A marked task in execution, and the inline criterion

**Why.** D11 runs a marked, dispatched task with no task review and no fix loop: widened gates, leads for the branch reviewer, a failed gate or a concern touching a later task's ground sending it to step 3; the completion line records it; Finish's per-task record check reads the per-task line in place of the review file. D10 keeps the task review for an inline task whatever its mark. D14 replaces inline mode's "costs more than it protects" with the criterion in T1's home.

**Files.** `skills/subagent-driven-development/SKILL.md` (§ The Task Loop steps 2–4 and its "Never skip it"; the completion line among the ledger forms; § Finish's per-task record check; § Inline mode, D14 and D10's inline case); `skills/subagent-driven-development/implementer-prompt.md` (its routed-item paragraph, which ties routed items to the task review); `skills/subagent-driven-development/task-reviewer-prompt.slots.md` (D11 names the card: where it implies every task gets a review); `agents/implementer.md`, `agents/task-reviewer.md` (regenerated); `tests/prose-budget.txt` (`subagent-driven-development`). Consumers, by search for "Never skip it", "task-<N>-review", "Task <N>: complete", "routed item" and "costs more than it protects" over `skills/` and `docs/decisions/`: `requesting-code-review` and `code-reviewer.md` are T6's; `docs/decisions/task-loop.md` is T7's.

**Contract.** Consumes T1's home and T4's mark line. Produces the completion line; consumes the per-task line by description (Inter-task contracts). Enacts D10 (inline case), D11 (SDD, implementer template, task-reviewer card), D14 (inline mode), C3 (the controller's gate half); DI-1.

**Acceptance.**
- Happy: a marked dispatched task whose report passes the widened gates completes with the new completion line and its leads recorded; the resume rule treats that line as complete.
- Edge: a marked task worked inline keeps its task review; a marked task whose concern touches what a later task builds on runs from step 3; a revert-and-replan of a marked task keeps its `-x<X>` report naming.
- Error: a report with no RED output and no logged exception, or a routed item with no Decision Log entry, sends the task to step 3, not to a fix wave.
- Integration: A7's after search over `skills/subagent-driven-development/SKILL.md`, quoted; `python tools/instrument_agents.py check` passes; the suite passes.

## T6 — The branch reviewer as a marked task's first review

**Why.** D12 makes the branch reviewer the first review of each branch-review-only task through `[BRANCH_ONLY_TASKS]`, with the per-task line in its first full-scope pass and the task loop's wiring for failed judgments; D4 turns Lane Fit's "shape" into the overturn question asked after code; the reviewer's section list gains the arrangement questions.

**Files.** `skills/requesting-code-review/SKILL.md` (filling the slot from the ledger and the plan; refusing a first pass missing a task's line; a failed intent, scope or deviation-audit judgment on such a task opening a wave whatever its severity); `skills/requesting-code-review/code-reviewer.md` (the per-task judgments, the per-task line in the output format, Lane Fit per D4, the section list); `skills/requesting-code-review/code-reviewer.slots.md` (the slot); `agents/branch-reviewer.md` (regenerated); `tests/instrument_corpus.py` only where DI-3 is resolved by raising `CARD_BUDGET`, with its reason; `tests/prose-budget.txt` (`requesting-code-review`). Consumers, by search for "Lane Fit", "WITHIN SHAPE", "EXCEEDS SHAPE", "qualifying shape" and the slot names over `skills/` and `tests/`: the lane reference's hatch is T3's; `tests/test_instrument_agents.py` reads the card budget.

**Contract.** Consumes T1's home, T5's completion line, T4's amendment-commit naming. Produces `[BRANCH_ONLY_TASKS]` and the per-task line (Inter-task contracts). Enacts D4 (Lane Fit), D12, C2, C3 (the branch reviewer's half); DI-1, DI-2, DI-3.

**Acceptance.**
- Happy: with a ledger holding a branch-review-only completion line, the filled slot carries the task's range, its latest non-reverted report path, the decision record's path where its plan entry names it, and its range's amendment commits; the reviewer's first pass reports a per-task line for it.
- Edge: no such task gives "none"; a task reverted and redone points at its `-x<X>` report; later passes re-grade the whole branch without repeating the lines.
- Error: a MINOR-staked scope failure on such a task opens a wave; a first pass missing a task's line is refused.
- Integration: A5's standing check (`python tools/instrument_agents.py check`) and the card-budget test pass; A6's trace stated in the report, check by check, against T5's gates; the suite passes.

## T7 — Records, README, backlog and the umbrella

**Why.** D15 has the decision records take the positions with their bases and the backlog follow; D9 corrects README's paraphrase; D8 drops "caps as cost bounds" from the umbrella's Intent; D5 records the origin question's answer in `routes.md`. This task also runs the repository-wide acceptance searches and computes U5's figure.

**Files.** `README.md`; `docs/decisions/routes.md`, `spec-campaign.md`, `task-loop.md`, `branch-review.md`, `plans.md`, `umbrellas.md`, and any other record a search finds stating what changed (`crucible-suite.md` and `plans.md` use "structural"; `evidence-and-findings.md` and `instruments.md` describe the shared reference and its grants); `docs/backlog/review-catch-and-implementers.md` (deleted), `lane-entry-and-downshift.md`, `campaign-early-stop-investigation.md`; `docs/backlog/review-seat-report-write.md` (this effort's report-file counts, its own commit, decision record entry 11); `docs/crucible/2026-10-28-hypothesis-specs/umbrella.md` (D8's Intent edit only). Inputs: the brainstorm decision record `.crucible/arrangements/brainstorm-decisions.md`, from which each position's basis is attributed by its entry's proposer and status, and the campaign records under `.crucible/arrangements/campaigns/spec/` for the report-file counts. Every changed record gains a `## Changes` line.

**Contract.** Consumes what T1–T6 shipped. Enacts D5, D8 (the umbrella edit), D9 (README), D15; A1, A2, A3, A7 (all paths), A8, A10, A11.

**Acceptance.**
- Happy: each changed record states the new position with its basis and a Changes line (A8); `routes.md` states D5's answer with its evidence and limits (A11); the backlog matches D15.
- Edge: Changes sections quoting retired phrases are exempt from the searches (A1, A3, A7); the umbrella's edit touches its Intent's non-goals only, no constraint, mark, firm decision or entry.
- Error: no record attributes a controller proposal to the operator.
- Integration: the after searches for A1, A3 and A7 over every path, and A2's one-home search, quoted; A10's net word change to `skills/` across the branch with what was removed; the suite passes, its summary line quoted (A9).
