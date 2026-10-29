# Audit corrections — plan

Spec: `docs/crucible/2026-10-29-audit-corrections/design.md` @ `39cb385` — binding: its Constraints & invariants (C1–C8). It has no [LOAD-BEARING] marks, no preamble convention declared binding, no firm decisions and no `Umbrella:` line; its Decisions are lightly held.

## Goal

The skills, templates, slot cards, generated agents, decision records, `AGENTS.md`, `README.md`, `docs/dual-runtime.md` and backlog items carry the spec's decisions D1–D5 and D7–D27 (D6 was withdrawn), the suite passes, and the word delta against `dd6897d` is reported.

## Task dependency order

T1 → T2 → T3 → T4 → T5 → T6 → T7 → T8 → T9, one at a time. T2 comes before T4 and T6 because they point at the section T2 creates; T5 comes before T7, which points at the heading T5 creates; the records tasks (T8, T9) come after the skills they describe; T9 runs the closing checks.

## File ownership + overlap census

| File | Owner |
|---|---|
| `docs/backlog/skill-text-rewrite.md`, `campaign-early-stop-investigation.md`, `decision-ask-framing.md`, `reviewer-research-reach.md`, `records-retention-config.md` | T1 |
| `skills/subagent-driven-development/references/premise-and-questions.md` | T2 |
| `skills/redteaming/SKILL.md`, `skills/redteaming/references/formats.md`, `skills/redteaming/references/flip-paths.md` | T3 |
| `skills/redteaming/seat-prompt.md`, `seat-prompt.slots.md`, `terminal-pass-prompt.md`, `terminal-pass-prompt.slots.md`, `skills/redteaming/references/plan-phase.md`, `folded-lane.md`, `agents/redteam-seat.md`, `agents/terminal-pass.md` | T4 |
| `skills/brainstorming/SKILL.md`, `skills/brainstorming/references/umbrellas.md`, `skills/writing-plans/SKILL.md` | T5 |
| `skills/requesting-code-review/SKILL.md`, `code-reviewer.md`, `skills/subagent-driven-development/implementer-prompt.slots.md`, `re-review-prompt.slots.md`, `agents/branch-reviewer.md` | T6 |
| `skills/subagent-driven-development/SKILL.md`, `references/very-small-lane.md`, `skills/finishing-a-development-branch/SKILL.md`, `AGENTS.md`, `README.md`, `docs/dual-runtime.md` | T7 |
| `docs/decisions/evidence-and-findings.md`, `the-spec.md`, `routes.md`, `spec-campaign.md`, `task-loop.md`, `terminal-pass.md`, `plans.md`, `decision-records.md`, `instruments.md` | T8 |
| `docs/decisions/branch-review.md`, `records-and-workspace.md`, `umbrellas.md` | T9 |
| `tests/prose-budget.txt` | T2–T7, each its own skill directories' lines |

Overlap: `tests/prose-budget.txt` only, written by T2–T7 in task order, each task changing the lines of the skill directories it edits. No other file has two owners. The spec's D8 wording change is spread across T2–T9 by file ownership, held together by contract IC-2; T1's backlog edit avoids the threshold word (T1, Contract).

## Inter-task contracts

- **IC-1 — the parity section (D12) and the umbrella's Intent (D1).** Produced by T2: a section of `premise-and-questions.md` headed `## Binding items and unrecorded choices`, holding the two clauses moved out of `seat-prompt.md`; and, in § Premise findings, the one sentence that a child's branch changing what its umbrella's Intent asks is a finding (D1 as amended at `39cb385`). Consumed by T4 (`seat-prompt.md` and `terminal-pass-prompt.md` name the section and drop their own copies), T5 (`umbrellas.md` § Children states the Intent rule for the umbrella's reader) and T6 (`code-reviewer.md` names the section, adding the code-choice reading). T8's `evidence-and-findings.md` and `instruments.md` name the section as the clauses' home.
- **IC-2 — the overturn wording (D8).** The question reads "is overturning a major mechanism after code reasonably expected?"; the seat's forecast line takes the two forms `Overturn after code: reasonably expected — <which mechanism, why>` and `Overturn after code: not reasonably expected`. T2 states the question; T4 owns the forecast line and the terminal pass's check of it; T3 (`SKILL.md`, `formats.md`, `flip-paths.md`), T5, T6, T7, T8 and T9 use the same words at their sites.
- **IC-3 — labelled changes in a wave (D14).** An entry in a wave's findings list reads `Change (<kind>): <the change> — apply it, or decline it with a reason` with `<kind>` one of `improvement`, `ruling`, `requested`. T6 produces the label rule in `requesting-code-review/SKILL.md` and the two cards' wording; T7's `very-small-lane.md` inline fix report answers such an entry `applied` or `declined`.
- **IC-4 — open items (D20, D22, D23).** The file is `<feature-folder>/open-items.md`. T3 adds it to `formats.md` § Feature folder's files named by role and to § Lifecycle's account of deletion. The seeding of earlier phases' leftovers under the ledger's `## Questions` as `<phase>: <item> — carried` has one home, `plan-phase.md`'s close (T4), beside its existing seeding; `redteaming/SKILL.md` § Exit (T3, the folded close) and SDD § Setup (T7, the lane and the backstop) point to it. T7 writes the Finish order, the readout's keep-or-drop list and the file's commit; T5 writes the umbrella landing's file.
- **IC-5 — the cleanup wave's ledger mark (D19).** `Branch wave <n>/3 (cleanup, …)` off the lane, `Wave <n> (cleanup):` on it. T6 states the wave and the off-lane form; T7 the lane form.
- **IC-6 — the closing review's entry point (D24).** T5 writes `#### Closing review` in `umbrellas.md`, pointed to from § Resuming. T3's `formats.md` § Lifecycle names the closing review's workspace end by the file `skills/brainstorming/references/umbrellas.md`, not the heading, which does not exist when T3 runs; T7's SDD § Finish close readout and finishing's merge option point to the heading.
- **IC-7 — the delegated status (D18).** A decision record entry left to the controller reads `accepted — delegated to the controller`. Its home is brainstorming § Workspace provisioning (T5), where the statuses are defined; `formats.md`'s status account (T3) points to it; T8 checks `decision-records.md`'s basis form reads it.
- **IC-8 — the terminal pass's new input (D16).** The brainstorm decision record's path, passed through a slot T4 adds to `terminal-pass-prompt.slots.md`; T3's `SKILL.md` lists it among the pass's inputs.

## Acceptance mapping

| Spec criterion | Task | Kind |
|---|---|---|
| A1 suite passes | T9 (each task also runs it) | standing test |
| A2 proposer routing gone | T9 | one-time check, `git grep` at `dd6897d` (fires) and at HEAD (none) |
| A3 no project-specific home in skills | — | why-not: prose fidelity (C7), judged by the task reviews and the branch review; the search cannot fail today |
| A4 "plausible" no longer states the threshold | T9 | one-time check, `git grep -n -i plausib` over `skills/`, `docs/decisions/`, `docs/backlog/` at `dd6897d` and at HEAD; T9's report lists the `dd6897d` hits, classes each as overturn wording or unrelated, and shows no overturn-wording hit at HEAD |
| A5 word delta reported | T9 | one-time check, per-directory word counts at `dd6897d` against HEAD |
| A6 decisions land where Interfaces says | — | why-not: prose fidelity, judged by the task reviews and the branch review |

## Deferred-items routing table

| id | source (spec or plan site) | one-line intent | owning task |
|---|---|---|---|
| DI-1 | spec § Mechanism sketches (last line) | the closing review's report file names inside its workspace, clear of the host's report-name filter and of what `tests/test_report_filenames.py` checks | T5 |

## Tasks

### T1 — Backlog edits

**Why.** D27: the feature's non-goals are deferrals, and a deferral counts once it is recorded; the operator asked for these as backlog items ("backlog everything that doesn't fit"). They come first so no later task depends on an unrecorded deferral.

**Files.** The five backlog items in the census. Each edit states the current state (AGENTS.md: an item states the current state, not a progress log). Inputs: the spec's § Intent and § Non-goals, and `tests/prose-budget.txt` at `dd6897d` for figures.

**Contract.** Enacts D27. Edits:
- `skill-text-rewrite.md`: skill word totals as of `dd6897d`, so labelled; the design targets of § Non-goals' first bullet (growth, separability of review before code and plan form, signal and vocabulary sprawl, the forecast → readout → stop-check chain, the binding clause restated at many sites, the containment test's incident rules, request blocks copied into child specs); the two predating findings; moving right-sizing to the branch review; the tension-closed-by-adding restructure the operator deferred.
- `campaign-early-stop-investigation.md`: no after-code record of whether a stopped campaign's mechanism was overturned. Its existing sentence stating the stop trigger points to `docs/decisions/spec-campaign.md` instead of quoting the threshold word, so it reads true before and after T3.
- `decision-ask-framing.md`: the undelivered readout and the controller-lean evidence, with a readout-delivery check as a candidate.
- `reviewer-research-reach.md`: the review methods the effort's reviews never ran and the seat-by-model comparison (four other-host seats, all in first rounds, so stage and model are confounded).
- `records-retention-config.md`: its mode must say where open items go (D22); its observation that crucible commits no process records gains that this feature adds a committed open-items file.

**Acceptance.** Happy: each item holds its addition, no progress-log prose. Edge: an item whose existing text the addition contradicts is reconciled, not appended to. Error: no local context (AGENTS.md rule): no project names, paths or session details. Integration: the suite passes.

### T2 — The shared reference

**Why.** The shared reference is where every seat reads what it may raise. D1 narrows the premise line to what the document itself shows and gives the umbrella's Intent its one home; D12 moves the parity clauses here so the branch reviewer gains them by a pointer; D8 changes the overturn question it defines.

**Files.** `premise-and-questions.md`; `tests/prose-budget.txt` (SDD's line). Consumers of its sections, by `git grep premise-and-questions`: `seat-prompt.md`, `terminal-pass-prompt.md` (T4), `code-reviewer.md` (T6), `implementer-prompt.md`, `task-reviewer-prompt.md` (read only: they name § Premise findings, whose narrowing needs no change there), `brainstorming/SKILL.md`, `writing-plans/SKILL.md` (T5), SDD `SKILL.md`, `very-small-lane.md` (T7), `flip-paths.md`, `redteaming/SKILL.md` (T3).

**Contract.** Enacts D1 (three protected items, the lane's Intent, an umbrella child's request; everything else lightly held; "who stands behind" and "where the operator chose it" gone; the umbrella-Intent sentence of IC-1), D8 (IC-2; the two cases usual, not only; the umbrella reading's "could plausibly overturn"), D12 (produces IC-1's section).

**Acceptance.** Happy: a reader can classify a premise finding from the document alone. Edge: the umbrella reading of the overturn question uses IC-2's wording. Error: no proposer-based routing remains (A2's phrases absent from this file). Integration: the suite passes; the word delta is reported.

### T3 — Redteaming controller rules

**Why.** The controller's own rules: what the readout carries, when a campaign stops, how a fix list is traced, what the terminal pass reads, what the record formats hold, and how premise findings and rulings route.

**Files.** `skills/redteaming/SKILL.md`, `references/formats.md`, `references/flip-paths.md`; `tests/prose-budget.txt` (redteaming's line). Consumers: `terminal-pass-prompt.md` and its card (T4) read the readout list and the pass's inputs; `conserve.py` reads ids only (read only).

**Contract.** Enacts D2 (mislabel both ways, `flip-paths.md`), D4 (readout item, carried doubts, round 0 included), D5 (the pause, controller side), D8 (IC-2 at these sites), D10 (the adopted-question rule: no mark added where no mark-grading seat reads after), D15 (trace in the fix list, recorded in restating sites), D16 (lists IC-8's input), D18 (IC-7, pointing to its home), D21 (flip-paths' "in execution" ruling route: a branch-review wave at the readout, a plan change at the next task boundary), D22/D24 (IC-4's role and both Lifecycle ends, IC-6's workspace end named by file), D23 (§ Exit points to IC-4's seeding home).

**Acceptance.** Happy: the readout's closed list includes carried questions. Edge: a pending premise ask that would re-shape a mechanism pauses the campaign; at the cap it is put alone. Error: the blind verifier's inputs are unchanged (C6). Integration: `conserve.py`'s tests and the reference checks pass.

### T4 — Redteaming seats and plan phase

**Why.** The seat side of T3's rules: what a seat forecasts, what the terminal pass checks and reads, where the parity clauses now live, and the plan phase's new census, mark rule and seeding.

**Files.** `seat-prompt.md`, `seat-prompt.slots.md`, `terminal-pass-prompt.md`, `terminal-pass-prompt.slots.md`, `references/plan-phase.md`, `references/folded-lane.md`; `agents/redteam-seat.md` and `agents/terminal-pass.md`, regenerated by `python tools/instrument_agents.py write`; `tests/prose-budget.txt` (redteaming's line, after T3).

**Contract.** Consumes IC-1, IC-2, IC-8. Produces IC-4's seeding home. Enacts D4 and D18 where `terminal-pass-prompt.md` checks readouts (its fidelity check reads the carried-questions item and the delegated status), D5 (the stop check treats a stop while a holding ask was pending as a mismatch), D8 (the forecast line), D10 (marks in `plan-phase.md` and `folded-lane.md`), D12 (pointers to IC-1, the seat's copies removed), D16 (the decision-record check, its scope and its channel), D17 (the pre-pass set census and its widened supporting inputs), D23 (the plan phase's close seeding). Slot cards stay within the 3,000-character budget.

**Acceptance.** Happy: the generated agents match their templates (the suite's `check` mode). Edge: a card near its budget gets wording in the template, not the card. Error: no seat template keeps its own copy of IC-1's clauses. Integration: the suite passes.

### T5 — Brainstorming, umbrellas, writing-plans

**Why.** Where a feature's route and its decision record are chosen, and where an umbrella's lifecycle lives: the inline test's preset row, step 4's selector, the delegated status, the umbrella's Intent, its landing's open items and its closing review.

**Files.** `skills/brainstorming/SKILL.md`, `references/umbrellas.md`, `skills/writing-plans/SKILL.md`; `tests/prose-budget.txt` (brainstorming's and writing-plans' lines).

**Contract.** Consumes IC-1, IC-2, IC-4. Produces IC-6 and IC-7's home. Enacts D1 (§ Edits and § Children: the umbrella's Intent, as IC-1 states it), D7 (preset table, the lane's dispatch clause), D8/D9 (step 4 keyed on the answer; the unsupported reason), D10 (the mark sentence in writing-plans), D18 (IC-7 in § Workspace provisioning), D23 (the umbrella landing's `open-items.md`, its override, the later append), D24 (`#### Closing review`, § Resuming's pointer, when, seats on the default role, records, append rule, nested umbrellas, no gate). Owns DI-1.

**Acceptance.** Happy: an umbrella completed by a landed drop or a landing makes its closing review due. Edge: a nested umbrella's review runs at its own completion, then its parent's. Error: closing is still read from the marks; nothing gates on the review. Integration: the suite passes.

### T6 — The branch review

**Why.** The branch review's parity, its leads' guards, the labelled changes that ride a wave, the cleanup wave, the readout's waves and the open-items commit in a reopened pass.

**Files.** `skills/requesting-code-review/SKILL.md`, `code-reviewer.md`, `skills/subagent-driven-development/implementer-prompt.slots.md`, `re-review-prompt.slots.md`; `agents/branch-reviewer.md`, regenerated; `tests/prose-budget.txt` (requesting-code-review's and SDD's lines).

**Contract.** Consumes IC-1, IC-2. Produces IC-3 and IC-5's off-lane form. Enacts D12 (pointer and the code-choice reading), D13 (a confirmed intent or scope gap opens a wave; an unruled lead refuses the pass), D14 (labels; the cards override the templates' two-answer rule for labelled items; templates unchanged; the implementer card has 53 characters of room, so its wording leans on the label's own instruction, IC-3), D19 (cleanup wave), D21 (a readout ruling's or requested wave; a declined ruling back to the operator; past the cap on the operator's answer), D22 (the open-items commit in scope, beside the umbrella mark), D8 (IC-2 in `code-reviewer.md`).

**Acceptance.** Happy: a cleanup wave runs once, counted, with its re-review and full-scope pass. Edge: minors the cleanup raises open no wave; a MAJOR at the cap escalates. Error: an adopted improvement never reaches the adjudicator. Integration: the cards stay within budget (2,947 and 2,864 characters at `dd6897d`); the suite passes.

### T7 — Execution and finish

**Why.** The Finish order the operator asked to loosen, the hand-over of work left open, the lane's inline test, and the closing review's pointer from a landing.

**Files.** `skills/subagent-driven-development/SKILL.md`, `references/very-small-lane.md`, `skills/finishing-a-development-branch/SKILL.md`, `AGENTS.md`, `README.md`, `docs/dual-runtime.md`; `tests/prose-budget.txt` (SDD's and finishing's lines). Consumers: SDD § What a report voices ("none opens a fix wave", read against D13 and D19); `AGENTS.md`'s feature-folder entry ("Frozen once the feature ships"); `docs/dual-runtime.md`'s layout line for the feature folder; README § What it writes into your repository.

**Contract.** Consumes IC-3, IC-4, IC-5, IC-6. Enacts D7 (the lane's inline test), D8 (IC-2 in the lane), D13/D19 (SDD § What a report voices agrees: a lead opens no wave by itself, a confirmed intent or scope gap at the branch review does), D14 (the lane's inline fix report), D19 (IC-5's lane form), D20 (readout before the suite; the keep-or-drop list; recommendation by finishing's options; the order after an integration answer; more work reopening the loop first; discard; red and dismissed red runs; finishing asking only what is left open, the files question with its warning, removal after the suite as now; no "exactly as written"), D21 (SDD Setup seeds open premise asks and points to IC-4's seeding home; a task-loop ruling as a plan change at the next task boundary, SDD § Plan changes mid-execution), D22 (the file, its contents, its commit, the override; `AGENTS.md`'s line keeping the default, the controller's local-context check, and its feature-folder entry naming `open-items.md` and the closed umbrella folder's one added file; `docs/dual-runtime.md`'s layout line; README's account of what crucible writes), D24 (the close readout naming the closing review; finishing's merge option pointing to it).

**Acceptance.** Happy: a merge answer runs file, suite, deletion, finishing in that order. Edge: an answer asking for more work reopens the loop before any of them; a discard skips the file and the suite; a red suite reopens the loop and the earlier answer stands only where nothing new was left open. Error: no item is left only in the workspace (C3); nothing lands without the operator's answer (C1). Integration: the suite passes; the hook and envelope budget tests are unaffected.

### T8 — Decision records, part one

**Why.** The records state each position and how it was learned; the spec reverses or changes several. Each edit adds a `## Changes` line the branch reviewer checks.

**Files.** `docs/decisions/evidence-and-findings.md`, `the-spec.md`, `routes.md`, `spec-campaign.md`, `task-loop.md`, `terminal-pass.md`, `plans.md`, `decision-records.md` (read for IC-7; edited only where its basis form does not cover a delegated entry), `instruments.md` (what each seat reads of the shared reference, and the terminal pass's card slots). Inputs: the brainstorm decision record, `.crucible/audit-corrections/brainstorm-decisions.md`, for each position's proposer and status.

**Contract.** Enacts in the records D1–D3 (with the deference decline's Changes line), D4, D5, D7–D11, D12 (IC-1 as the clauses' home, in `evidence-and-findings.md` and `instruments.md`), D14 and D19 where `evidence-and-findings.md` restates how an adopted improvement rides a wave and that it never opens one, D15–D18, D16 in `instruments.md` (the card's new slot), D25 (the stop confirmed by the operator), D26 (the per-feature work stated). Uses IC-2's wording.

**Acceptance.** Happy: each changed position has a dated Changes line. Edge: a reversed position names what it reverses. Error: no basis attributed beyond its decision-record entry's status (delegated entries read as delegated). Integration: the suite passes (its record checks included).

### T9 — Decision records, part two, and the closing checks

**Why.** The finish and umbrella records, then the checks that span the branch.

**Files.** `docs/decisions/branch-review.md`, `records-and-workspace.md`, `umbrellas.md`. Inputs as T8.

**Contract.** Enacts in the records D1 (the umbrella's Intent, in `umbrellas.md`), D13, D14, D19 (the rejection of minors opening waves revised), D20–D23 (the two reversed positions: no committed summary, filing left to the operator), D24 (the closing review, a step), IC-2's wording in `umbrellas.md`. Runs A2, A4 and A5. An overturn-wording hit A4 still finds at HEAD, in a file T9 does not own, is reported as a finding for the branch review, never edited by T9.

**Acceptance.** Happy: A2, A4 and A5's commands and outputs in the report, each one-time check also run at `dd6897d`, where A2 and A4 must hit. Edge: an A4 hit on an unrelated "plausibly" is classed as such. Error: a remaining overturn-wording hit is reported, never silently left. Integration: the full suite's summary line quoted.
