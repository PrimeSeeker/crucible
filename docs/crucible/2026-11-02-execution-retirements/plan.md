# Plan: execution retirements

Spec: `docs/crucible/2026-11-02-execution-retirements/design.md` @ `5e123b2` — binding: its Constraints & invariants (I1–I4); it declares no binding preamble convention and records no firm decision. Through its umbrella line, `docs/crucible/2026-11-01-skill-text-rewrite/umbrella.md`: this feature's own entry (`execution-retirements`) and the umbrella's Constraints & invariants (C1–C4); the umbrella records no firm decision. A task calling for a change to those, or to the entry other than a clarification the spec states that changes nothing another entry waits on, is a plan defect; the spec's lightly held D4 edit (Interfaces, "The umbrella on this branch") is T8's.

## Goal

The skill text, its templates and cards, generated agents, tests, decision records and the backlog items the spec names state the execution side of the umbrella as the spec's Decisions E1–E11 give it, with nothing stating a retired mechanism as current (I4); the prose budget's sum at or below 65,246 words; the subagent-driven-development, redteaming and brainstorming `SKILL.md` files no larger than at `10cd3f5`, and no other `SKILL.md` over 20,000 bytes (A3).

## Task dependency order

T1 → T2 → T3 → T4 → T5 → T6 → T7 → T8, strictly in sequence: most tasks edit the same few files (census below), and each runs from the tree its predecessor left.

## File ownership + overlap census

Each file against the tasks that edit it, in run order; a file edited by several tasks is edited by each in turn, the later task working on the earlier one's result and touching only its own mechanism's words. `agents/*` are regenerated, never hand-edited, by every task that edits their template (`python tools/instrument_agents.py write`). `tests/prose-budget.txt` is edited by every task that changes a skill's word count (X4). Abbreviations: SDD = `skills/subagent-driven-development/`, RCR = `skills/requesting-code-review/`, RT = `skills/redteaming/`.

| File | Tasks |
|---|---|
| `SDD/SKILL.md` | T1, T2, T3, T4, T5, T6, T7 |
| `SDD/implementer-prompt.md` | T1, T5 |
| `SDD/implementer-prompt.slots.md` | T1, T4, T5 |
| `SDD/task-reviewer-prompt.md` | T3, T5 |
| `SDD/task-reviewer-prompt.slots.md`, `SDD/re-review-prompt.slots.md` | T4 |
| `SDD/references/dispatch-composition.md` | T1 |
| `SDD/references/very-small-lane.md` | T2, T5, T7 |
| `SDD/references/premise-and-questions.md` | T7 |
| `RCR/SKILL.md` | T1, T2, T4, T5, T6, T7 |
| `RCR/code-reviewer.md` | T5, T6, T7 |
| `RCR/code-reviewer.slots.md` | T4, T5, T6, T7 |
| `skills/finishing-a-development-branch/SKILL.md` | T2 |
| `skills/writing-plans/SKILL.md` | T5, T6 |
| `RT/SKILL.md` | T4, T5, T6 |
| `RT/references/formats.md` | T4, T5, T6, T7 |
| `RT/references/plan-phase.md` | T4, T5, T6, T7 |
| `RT/references/folded-lane.md` | T4, T5, T6 |
| `RT/references/flip-paths.md` | T2, T5, T7 |
| `RT/seat-prompt.md`, `RT/seat-prompt.slots.md` | T4, T5, T6 |
| `skills/brainstorming/SKILL.md` | T5, T7 |
| `skills/brainstorming/references/folded-lane-document.md` | T5 |
| `skills/brainstorming/references/umbrellas.md` | T5, T7 |
| `agents/implementer.md` (generated) | T1, T5 |
| `agents/task-reviewer.md` (generated) | T3, T5 |
| `agents/branch-reviewer.md` (generated) | T5, T6, T7 |
| `agents/redteam-seat.md` (generated) | T4, T5, T6 |
| `tests/prose-budget.txt` | T1–T7 |
| `README.md` | T2 |
| `docs/upstream.md` | T3 |
| `docs/decisions/task-loop.md` | T1, T2, T3, T5, T6 |
| `docs/decisions/adjudication.md` | T1, T2, T3 |
| `docs/decisions/branch-review.md` | T1, T2, T5, T6, T7 |
| `docs/decisions/model-roles-and-effort.md` | T1, T3 |
| `docs/decisions/shared-tree.md` | T4 |
| `docs/decisions/spec-campaign.md` | T4, T6 |
| `docs/decisions/plans.md` | T5, T6 |
| `docs/decisions/routes.md` | T5, T6, T7 |
| `docs/decisions/evidence-and-findings.md`, `docs/decisions/the-spec.md`, `docs/decisions/records-and-workspace.md`, `docs/decisions/instruments.md`, `docs/decisions/test-rules.md`, `docs/decisions/umbrellas.md` | each by the tasks whose mechanism it states as current, found by that task's own term search; the task's report names which |
| `docs/crucible/2026-11-01-skill-text-rewrite/umbrella.md` | T8 |
| `docs/backlog/implementer-dispute-channel.md`, `skill-text-rewrite.md`, `umbrella-followups.md`, `escalation-and-effort.md`, `nested-orchestration.md`, `skill-size-after-compaction.md` | T8 |

The census lists the sites the spec's Mechanism sketches name and the planning search found (A1's terms plus each mechanism's own); a site a task's own search finds beyond it joins that task's Files in its report, and a decision record any task changes takes its dated `## Changes` line in that task (X6).

## Inter-task contracts

- **X1. Ledger lines.** The forms the spec's Interfaces ("The ledger", "The answers after the third wave", "The hatch's move") fix, each produced in `SDD/SKILL.md` by one task and read by SDD's resume rule, Finish's record check and `RCR/SKILL.md`: T1 the `<W>/3` fix-wave line, the `Task <N>: reverted — <the ruling>` line with no attempt number, the repair recorded under `## Adjudication rulings`, the park and block lines and the post-`3/3` resume; T2 the `Task <N>: inline` line; T4 removes the ambiguous-liveness BLOCKED line; T5 removes the deferred list; T7 removes the `Hatch:` line and states the move aside to `sdd-lane/`. A later task never restates an earlier one's form.
- **X2. Removed headings and citations.** T1 removes SDD § Revert-and-replan; T6 removes RCR § Tasks completed branch review only and the branch-reviewer template's § Tasks With No Task Review and § Task Lines; T7 removes the template's Lane Fit section. Each updates every citation of what it removes in the same task (spec, Interfaces "Removed headings"), and `tests/test_references.py` passes on its tree.
- **X3. The branch-reviewer card.** T4 the replacement wording its slots carry, if any; T5 the `[LEDGER_MINORS]` clause on routed deferred items; T6 the slot for tasks completed branch review only (renamed, D2) and `[MANDATE_REMINDER]`; T7 the `lane` selector's text. Each edits the card and `RCR/code-reviewer.md` together and regenerates `agents/branch-reviewer.md`; the card stays within the card budget the suite checks.
- **X4. Prose budget and generated agents.** Each task that changes a skill directory's word count sets that line of `tests/prose-budget.txt` to the new count, and each that edits a template regenerates `agents/`; the full suite passes on every task's tree.
- **X5. Oversized `SKILL.md` files do not grow** (the umbrella's C2, spec A3). Every task that edits `SDD/SKILL.md`, `RT/SKILL.md` or `skills/brainstorming/SKILL.md` leaves it no larger in bytes than at `10cd3f5` (46,563, 39,855 and 22,725), and every other `SKILL.md` it edits at or below 20,000 bytes, measured on its own tree by `git cat-file -s` or the file size; where its own additions would exceed a limit, it offsets them within its own mechanism's text in that file, and where it cannot, it stops and reports BLOCKED with the figures. Its report records the sizes of each `SKILL.md` it edited.
- **X6. Decision records and the vocabulary list.** Each task that changes a decision updates its record in place with a dated `## Changes` line (`AGENTS.md`), which names the labels, ledger lines and slots the task removes (spec E11); a record may keep a retired mechanism as history (I4). T8 collects the lines into the vocabulary list for the landing.
- **X7. What binds, by pointer.** T2 makes the adjudicator's inputs point to SDD § The Task Loop's Deviations paragraph (E2); T3's removal of the pre-flight scan removes the other partial statement. No later task adds a restatement of what binds.

## Acceptance mapping

- **A1** (no retired mechanism stated) → one-time check, T8, run after T1–T7 on the final tree; each of T1–T7 also runs its own terms' search over its sites before and after (their Acceptance), and adds any further terms it judges its mechanism needs to T8's list in its report.
- **A2** (the suite passes) → one-time check at Finish by the controller (SDD § Finish); every task also runs the full suite on its own tree (X4).
- **A3** (the sizes) → one-time check at Finish by the controller; X4 keeps the budget's numbers current and X5 the `SKILL.md` byte sizes within their limits, task by task.
- **A4** (the paths walked) → one-time check by the controller, recorded in the branch review's records (the spec assigns it there); no task discharges it.
- **A5** (the landing check) → one-time check by the controller, before T8 is dispatched, its result recorded under the ledger's `## Progress`; a gap it finds is added to T8 by a plan change (SDD § Plan changes mid-execution).
- **A6** (the backlog) → one-time check, T8.

## Deferred-items routing table

| id | source (spec or plan site) | one-line intent | owning task |
|---|---|---|---|
| D1 | plan T2, Contract | where the `Task <N>: inline` line and the own-diff trigger are stated in SDD (inline mode, the ledger bullet, or § Disputes and adjudication) | T2 |
| D2 | plan T6, Contract | the new name of the branch-reviewer card's slot for tasks completed branch review only, free of A1's terms | T6 |
| D3 | plan T4, Contract | where `tree-check.txt` is named in the workspace layout and how the one shared-tree rule states it for both skills | T4 |

## Tasks

### T1. The fix loop and drift

**Why.** The fix loop's fresh implementer at waves 4–5, its tier escalation and the breaker go: three resumed waves, then the operator (E1). Drift found after the fact becomes an operator ask, revert or repair, and revert-and-replan's section, attempt numbers and the wave a DRIFT pass consumed go (E3). Both change the ledger forms later tasks read (X1), so they run first.

**Files.** `SDD/SKILL.md` (§ The Task Loop's fix-loop step and its Models row "Escalation, fix waves 4–5"; the ledger bullets and the resume rule; § Revert-and-replan, removed; the Deviations paragraph's last sentence; the rationalization table's drift row; Finish's record check where it reads the `-x<X>` names); `SDD/implementer-prompt.md` and `.slots.md` (the wave-4–5 rules; the fresh fix-only form is kept for the no-resume fallback, an inline task converted to dispatch and the branch review's fix wave); `SDD/references/dispatch-composition.md` (the escalation line); `RCR/SKILL.md` (§ The branch-review loop's Drift paragraph; the cap's escalation where it names the breaker); `agents/implementer.md`; `tests/prose-budget.txt`; decision records `task-loop.md`, `adjudication.md` (the breaker), `branch-review.md` (a DRIFT pass spends a wave), `model-roles-and-effort.md` (waves 4–5, escalation), and any other its search finds. Inputs: the brainstorm decision record (`.crucible/execution-retirements/brainstorm-decisions.md`, entries 0, 5) for each changed record's basis. Search terms: `wave 4`, `waves 4`, `wave-4`, `4–5`, `five waves`, `wave 5`, `breaker`, `<W>/5`, `tier bump`, `revert-and-replan`, `replan`, `attempt <X>`, `patch forward`, `patched forward`.

**Contract.** Enacts E1 and E3 and the spec's Interfaces "The ledger" (its T1 forms, X1) and "The answers after the third wave". Produces X1's T1 forms and removes SDD § Revert-and-replan (X2). The DRIFT flag stays as the trigger; on the very-small lane drift from the note stays a wave finding. The branch review's own three-wave cap is unchanged. "Load-bearing" in senses other than the breaker's stays.

**Acceptance.**
- Happy: a task's fix waves resume its recorded implementer, at most three, with the ledger reading `<W>/3`; after the third the controller puts the open findings to the operator with park / block / another approach and records ask and answer under `## Adjudication rulings`; drift within the materiality bound is an operator ask, revert or repair, the controller recommending one.
- Edge: a resumed controller after a `3/3` line goes to the open ask, not a fourth wave; a revert ruled at the branch review returns to it after the re-run tasks complete and resumes with a full-scope pass; a repair for a completed task ruled before the branch review begins waits for its first fix wave (spec Interfaces "The ledger"); a host with no resume operation gets the fresh fix-only implementer each wave.
- Error: a one-time search for the task's terms (case-insensitive) over `skills/`, `agents/`, `tests/` (corpus excluded) and `docs/decisions/`, run before (hits) and after (history in records and unrelated senses only), recorded in the report.
- Integration: the full suite passes; agents regenerated; budget lines current; X5 sizes recorded.

### T2. Disputes

**Why.** The controller rules on disputes with its evidence; a fresh adjudicator rules only where a dispute touches binding text or the Intent, or concerns a diff the controller wrote (E2), and its inputs point to the one full statement of what binds (X7).

**Files.** `SDD/SKILL.md` (§ Disputes and adjudication; inline mode; the ledger bullets for `Task <N>: inline`; the adjudicator's report paths, kept; Finish's red-suite handling); `SDD/references/very-small-lane.md` (disputes on the lane, whose diffs the controller writes); `RCR/SKILL.md` (§ The branch-review loop's Disputes and Finish's red suite paragraphs); `skills/finishing-a-development-branch/SKILL.md` (Step 1's exception names the ruling, not the adjudicator); `RT/references/flip-paths.md` (where it names the adjudicator's rulings); `README.md` (its line on adjudication); `tests/prose-budget.txt`; decision records `adjudication.md`, `task-loop.md`, `branch-review.md`, and any other its search finds (`evidence-and-findings.md`, `records-and-workspace.md`, `instruments.md`, `the-spec.md` carry hits). Inputs: the brainstorm decision record (entries 1, 5). Search terms: `adjudicat`, `adjudicator dismissed`, `NOT CONFIRMED`.

**Contract.** Enacts E2. Produces X1's `Task <N>: inline` line and X7. The rule holds in the task loop, the branch review and on the lane; a plan conflict that is a design judgment still goes to the operator; a ruling touching binding text passes `RT/references/flip-paths.md` § The containment test; every controller ruling and every dismissed BLOCKER or MAJOR reaches the close readout (I1).

Deferred to implementation: where the `Task <N>: inline` line and the own-diff trigger are stated in SDD (D1).

**Acceptance.**
- Happy: an implementer's NOT CONFIRMED on a dispatched task's diff, touching neither binding text nor the Intent, is ruled by the controller with its evidence, recorded under `## Adjudication rulings`; one touching binding text goes to the adjudicator.
- Edge: a dispute on an inline task's diff or any lane diff goes to the adjudicator, and after a compaction the controller still finds the task was inline from its ledger line; a red suite at Finish the controller judges not the branch's goes to the operator with its ruling, whoever made it.
- Error: the task's term search, before and after, recorded; no site states that every dispute goes to a fresh seat, or that the adjudicator's dismissal alone lets finishing proceed.
- Integration: the full suite passes; budget lines current; X5 sizes recorded.

### T3. Small retirements

**Why.** The pre-flight plan-conflict scan and the task review's cannot-verify items go, and snapshot blessing becomes one line (E4).

**Files.** `SDD/SKILL.md` (Setup's pre-flight scan; step 3's cannot-verify paragraph and the loop trigger it fed; step 4's snapshot procedure and the Models row for the snapshot seat, its report path kept); `SDD/task-reviewer-prompt.md` (the cannot-verify instruction and report line); `agents/task-reviewer.md`; `docs/upstream.md` (its row naming the cannot-verify and pre-flight references as carried into SDD); `tests/prose-budget.txt`; decision records `task-loop.md`, `adjudication.md` (the pre-flight scan's batch), `model-roles-and-effort.md` (the snapshot row), and any other its search finds (`test-rules.md`, `instruments.md` carry hits). Inputs: the brainstorm decision record (entries 0, 5). Search terms: `pre-flight`, `preflight`, `cannot-verify`, `cannot verify`, `snapshot`.

**Contract.** Enacts E4. The reviewer checks a requirement outside the diff in the code it needs, its verdicts carrying the result. The snapshot seat keeps its role (bounded or better) and report path `task-<N>-snapshot-<k>.md`, which Finish's record check reads. `skills/receiving-review/SKILL.md`'s "say when you cannot verify an item" is another sense and stays.

**Acceptance.**
- Happy: SDD Setup has no plan-conflict scan; the task-reviewer template asks for no cannot-verify items; the snapshot rule is one line naming the blind seat, its inputs, and the operator ask for a visible change.
- Edge: a requirement living outside the diff is still graded in the intent verdict; Finish's record check still finds the snapshot report.
- Error: the task's term search, before and after, recorded.
- Integration: the full suite passes; agent regenerated; budget lines current; X5 sizes recorded.

### T4. The shared tree: the status check and seat replacement

**Why.** The tree check becomes one status check after each review seat against the dispatch-time HEAD and untracked list kept in `<workspace>/tree-check.txt` (E5); seat replacement becomes one line (E6). Both rules are stated in SDD and redteaming and restated in cards and records.

**Files.** `SDD/SKILL.md` (§ Shared-tree rules: the tree check and the replacement gate; the ledger's ambiguous-liveness BLOCKED line); `RT/SKILL.md` (Inputs and state's Shared tree paragraph; § Panels' topping-up paragraph); `RT/references/formats.md` (the round record's tree-check readings and fields, removed; the workspace layout gains `tree-check.txt`); `RT/references/plan-phase.md` and `RT/references/folded-lane.md` where they state the readings or the gate; `RCR/SKILL.md` (its pointer to the shared-tree rules); the slot cards that state the replacement or fresh-path rule (`SDD/task-reviewer-prompt.slots.md`, `SDD/re-review-prompt.slots.md`, `SDD/implementer-prompt.slots.md`, `RCR/code-reviewer.slots.md`, `RT/seat-prompt.slots.md`) where their wording states the retired procedure; `RT/seat-prompt.md` if it does; generated agents of any template changed; `tests/prose-budget.txt`; decision records `shared-tree.md`, `spec-campaign.md` (ambiguous liveness), and any other its search finds. Inputs: the brainstorm decision record (entries 0, 5). Search terms: `tree check`, `tree-check`, `readings`, `status --porcelain`, `ambiguous liveness`, `ambiguous seat liveness`, `liveness is ambiguous`.

**Contract.** Enacts E5 and E6. The no-commit rule while a seat works is unchanged; a campaign's quorum and degraded-round rules are unchanged; the round-0 and plan-phase pre-passes' "liveness" (producer and consumer of a mechanism) is another sense and stays.

Deferred to implementation: where `tree-check.txt` is named in the workspace layout and how the shared-tree rule states it in both skills (D3).

**Acceptance.**
- Happy: after each review seat the controller runs one status check, comparing HEAD and the untracked paths with `tree-check.txt` written at dispatch; seats dispatched together are one window.
- Edge: an implementer's untracked test leftovers present at dispatch do not void a review; an untracked file deleted during the window does; a resumed controller finds the dispatch-time state in the file; a seat whose state the host cannot confirm is a stop-and-ask.
- Error: the task's term search, before and after, recorded; no round-record format field names tree-check readings.
- Integration: the full suite passes; agents regenerated where templates changed; budget lines current; X5 sizes recorded.

### T5. The deferral chain

**Why.** The routing table and the chain behind it go: a marker sits in its owning task, a spec marker is named in the Contract of each owning task, and the plan phase's pre-pass checks owners (E7). The deferral rules span writing-plans, brainstorming, the plan phase, the folded lane, three templates and the branch review.

**Files.** `skills/writing-plans/SKILL.md` (the header's routing-table section; § Deferring detail; § Binding vs advisory's "routing table's rows"); `skills/brainstorming/SKILL.md` (the deferral device) and `references/folded-lane-document.md`; `RT/SKILL.md` (§ Merge and finding hygiene's deferral paragraph, the misplaced-deferral definition; § Exit's folded close seeding); `RT/references/plan-phase.md` (the pre-pass's ownership closure, its owner check; the close's seeding of the deferred list); `RT/references/folded-lane.md` (per-round appending; the close check); `RT/references/formats.md` where it names the table or its rows; `RT/seat-prompt.md` (the pre-pass passage) and `.slots.md` if its wording does; `SDD/SKILL.md` (the ledger's deferred list; the implementer dispatch's routed-item reminder; the task review's per-row check; step 4's routed-item gate for a marked task); `SDD/implementer-prompt.md` and `.slots.md` (the "Deferred to you" section and the header's routing-table mention); `SDD/task-reviewer-prompt.md` (the per-row check and its report line); `RCR/SKILL.md` (the inputs' routed items and the sweep); `RCR/code-reviewer.md` and `code-reviewer.slots.md` (`[LEDGER_MINORS]`'s routed-item clause); `SDD/references/very-small-lane.md`, `RT/references/flip-paths.md`, `skills/brainstorming/references/umbrellas.md` where they state the table; generated agents `implementer`, `task-reviewer`, `branch-reviewer`, `redteam-seat` as their templates change; `tests/prose-budget.txt`; decision records `plans.md`, `task-loop.md`, `branch-review.md`, and any other its search finds (`the-spec.md`, `routes.md`, `evidence-and-findings.md`, `records-and-workspace.md`, `crucible-suite.md` carry hits). Inputs: the brainstorm decision record (entries 2, 6). Search terms: `routing table`, `routing-table`, `routed item`, `routed deferred`, `deferred list`, `T<N>`, `one row per owning task`.

**Contract.** Enacts E7 and the spec's Interfaces "Deferral ownership" (the ownership closure, misplaced deferral, the folded lane's round-0 pre-pass and re-run, no deferred list seeded at the folded close). Removes X1's deferred list; produces X3's `[LEDGER_MINORS]` change. The carriage of `deferred-minor` entries into `## Deferred minors` is unchanged (I2). A deferred call stays the implementer's, logged where it departs from advisory content.

**Acceptance.**
- Happy: writing-plans asks for no routing table; a plan's marker sits in its task and a spec marker is named by site in each owning task's Contract; the plan phase's pre-pass reports a spec marker no task names as an ownership-closure finding.
- Edge: a spec marker spanning several tasks is named in each; on the folded lane a fix item landing a marker names its owning tasks' Contracts and round 0's pre-pass and its re-run check owners; a `deferred-minor` entry still reaches the branch review's triage.
- Error: the task's term search, before and after, recorded; no template asks a seat for a per-row check or report line.
- Integration: the full suite passes; agents regenerated; budget lines current; X5 sizes recorded.

### T6. The `Review: branch only` mark

**Why.** The mark becomes one field and its reason: no seat grades marks, no rule limits which wave adds one before the plan's review closes, none is added after, and at the branch review a marked task's report is an input like the others, with no owed line (E8).

**Files.** `skills/writing-plans/SKILL.md` (§ Per-task structure's review-mark paragraph); `RT/SKILL.md` (the question-adoption rule on marks; the readout's marked-task item, kept for the plan phase and folded close); `RT/references/plan-phase.md` and `folded-lane.md` (the grading mandates); `RT/references/formats.md` where it records mark grading; `RT/seat-prompt.md` and `.slots.md` (the mark-grading clause); `SDD/SKILL.md` (step 2's marked task and the inline case; step 4's "widened as that step states"; Finish's record check of the owed line; the resume rule's "branch review only" completion line, kept); `RCR/SKILL.md` (§ Tasks completed branch review only, removed; the inputs paragraph; the loop-wiring clause counting failed judgments as BLOCKER or MAJOR; step 1's missing-line rule); `RCR/code-reviewer.md` (§ Tasks With No Task Review and § Task Lines, removed) and `code-reviewer.slots.md` (`[BRANCH_ONLY_TASKS]` reshaped and renamed, `[MANDATE_REMINDER]`); generated agents `branch-reviewer` and `redteam-seat` as their templates change; `tests/prose-budget.txt`; decision records `plans.md`, `branch-review.md`, `task-loop.md`, `spec-campaign.md`, and any other its search finds (`evidence-and-findings.md`, `test-rules.md`, `routes.md`, `umbrellas.md`, `the-spec.md`, `model-roles-and-effort.md` carry hits). Inputs: the brainstorm decision record (entries 3, 6). Search terms: `BRANCH_ONLY`, `Task Lines`, `branch-review-only list`, `Tasks With No Task Review`, `grade each mark`, `grading marks`, `adds grading`, `widened as that step states`, `audit of a task completed branch review only`, `and for a task completed branch review only`, `owes a line`.

**Contract.** Enacts E8 and the spec's Interfaces "The marked task at the branch review". Removes the headings X2 assigns it; produces X3's slot and `[MANDATE_REMINDER]` change. A marked task dispatched whose report is DONE and passes the step-4 gates (RED before GREEN, or the logged exception) completes branch review only; any concern or failed gate sends it to task review; a marked inline task keeps its task review. The mark's criterion is unchanged.

Deferred to implementation: the slot's new name (D2).

**Acceptance.**
- Happy: no seat card or template grades marks; the branch reviewer's card carries one slot listing each task completed branch review only with its range, report path, decision-record path where named and amendment commits, and its full-scope pass reads each report's Decision Log against the diff, its findings opening waves by staked severity.
- Edge: a mark is refused once the plan's review has closed (the task keeps its review); the plan phase's close readout still lists marked tasks; a marked task redone after a revert is read by the next full-scope pass with no owed line.
- Error: the task's term search, before and after, recorded; `tests/test_references.py` passes with the removed headings' citations updated (X2).
- Integration: the full suite passes; agents regenerated; budget lines current; card budget held; X5 sizes recorded.

### T7. The very-small lane

**Why.** Lane Fit's shape verdict goes, its goal half being the branch review's goal check; the upgrade hatch becomes one stop-and-ask line, the move's records handled as the spec's Interfaces state (E9; brainstorm entries 8 and 11).

**Files.** `SDD/references/very-small-lane.md` (the `Hatch:` ledger line; § The upgrade hatch; the branch review's lane inputs, the lane-fit statement); `SDD/SKILL.md` (§ Setup's predecessor-links bullet, which gains the hatch's use beside a supersede); `SDD/references/premise-and-questions.md` where it names Lane Fit; `RCR/SKILL.md` (the lane's inputs and lane-fit statement); `RCR/code-reviewer.md` (the Lane Fit section, removed) and `code-reviewer.slots.md` (the `lane` selector's text); `skills/brainstorming/SKILL.md` (the hatch's route entry; the hatch's spec written by the resolve step) and `references/umbrellas.md` (the hatch's duty to carry the `Umbrella:` line); `RT/references/plan-phase.md` (its **Close**: after a hatch, writing the ledger's line 2 and seeding the lane's open findings and unruled leads, which the controller running the plan phase reads there); `RT/references/flip-paths.md` and `RT/references/formats.md` where they state the hatch (formats' note beside the hatch's spec); `agents/branch-reviewer.md`; `tests/prose-budget.txt`; decision records `routes.md`, `branch-review.md`, and any other its search finds (`operator-steering.md`, `evidence-and-findings.md`, `terminal-pass.md`, `the-spec.md` carry hits). Inputs: the brainstorm decision record (entries 6, 8, 11). Search terms: `Lane Fit`, `lane-fit`, `EXCEEDS SHAPE`, `WITHIN SHAPE`, `Hatch:`, `hatch`.

**Contract.** Enacts E9 and the spec's Interfaces "The hatch's move" (the move aside as `sdd-lane/`, line 2 linking `sdd-lane/ledger.md`, the carried findings and leads with their staked severity, brainstorming's input, no preset proposed). Removes X1's `Hatch:` line and the Lane Fit section (X2); produces X3's `lane` change. The folded lane stays no hatch target; the lane's goal check runs with the note's Intent.

**Acceptance.**
- Happy: where overturning a major mechanism of the change is reasonably expected once coded, the controller puts stay-or-move to the operator; on the move the lane's `sdd/` is moved aside whole and the standard route's ledger links it; the branch reviewer on the lane runs the goal check and no shape verdict.
- Edge: a hatch from a child of an umbrella carries the `Umbrella:` line into the spec; a carried BLOCKER or MAJOR the standard route's reviewer dismisses reaches the close readout.
- Error: the task's term search, before and after, recorded; `tests/test_references.py` passes (X2).
- Integration: the full suite passes; agent regenerated; budget lines current; card budget held; X5 sizes recorded.

### T8. The umbrella edit, the backlog, the vocabulary and the final search

**Why.** The spec's lightly held edit to the umbrella's D4 lands on this branch; the backlog items the umbrella names for this child are resolved, trimmed or reworded (A6); the vocabulary list is collected (E11, X6); and the final search shows nothing states a retired mechanism as current (A1).

**Files.** `docs/crucible/2026-11-01-skill-text-rewrite/umbrella.md` (D4: the own-diff read and the status check's comparison with the dispatch-time list kept in the workspace, by `skills/brainstorming/references/umbrellas.md` § Edits; not the entry's `landed` mark, which comes at Finish); `docs/backlog/implementer-dispute-channel.md`, `skill-text-rewrite.md` (the late mark, the breaker's sense of "load-bearing", the hatch naming no skill, the vocabulary point), `umbrella-followups.md` (the bullet on statements of what binds), `escalation-and-effort.md`, `nested-orchestration.md`, `skill-size-after-compaction.md`, and any other backlog item the final search finds stating a retired mechanism as current; any site the final search finds that T1–T7 left (named in its report, with the task whose mechanism it is). Inputs: the brainstorm decision record (entries 1, 5, 6) for the umbrella edit's basis; T1–T7's reports for their further terms and `## Changes` lines; the controller's A5 record in the ledger. Search terms: A1's list, plus the further terms T1–T7's reports name.

**Contract.** Enacts E11, A1 and A6, and the spec's Interfaces "The umbrella on this branch". Consumes X6. A backlog item resolved is deleted; one partly resolved keeps only what stays open; open items are checked against the no-local-context rule (`AGENTS.md`).

**Acceptance.**
- Happy: A1's search over its scope, its command and output recorded, finds only history in decision records, the kept one-line forms and unrelated senses; each A6 item is deleted or trimmed, the report saying which; the vocabulary list collected from X6's lines is in the report for the landing.
- Edge: a hit T1–T7 left is fixed here and named with its owning mechanism; an A5 gap added to this task by a plan change is fixed.
- Error: the search run before this task's own edits shows the backlog hits it removes.
- Integration: the full suite passes.
