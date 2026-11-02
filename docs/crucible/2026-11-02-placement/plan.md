# Placement — implementation plan

Spec: `docs/crucible/2026-11-02-placement/design.md` @ `18d24f0` — binding: its Constraints & invariants (P1–P6); it records no firm decision and declares no binding preamble convention; through its `Umbrella:` line, this feature's own entry (`placement`) in `docs/crucible/2026-11-01-skill-text-rewrite/umbrella.md` and that umbrella's Constraints & invariants (C1–C4), each seat reading them in its worktree. A task calling for a change to those Constraints, or to the entry other than its mark and the clarifications the spec states, is a plan defect.

## Goal

The skills state each rule once, at the site where its reader acts, by the spec's owner map; the seven seat templates take their shared clauses by build-time splice from one shared seat reference, `skills/subagent-driven-development/references/seat-rules.md`; host-neutral rules have left the adapters; the corrections list holds; the decision records, docs and backlog say what the tree now does; the prose budget counts hand-written text (D16) and is lowered to the new counts.

## Task dependency order

T1 → T2 → T3 → T4 → T5 → T6 → T7 → T8, one at a time. T1 builds the splice and renames the shared reference, which every later task cites; T2 fills the shared reference and rewires the templates; T3 moves the controller-shared rules into `dispatch-composition.md` and the router, which T4–T6 point to; T4–T6 work through the controller skills; T7 is independent of T2–T6 and runs after them only to keep one writer on the tree; T8 closes the docs and measures the result.

## File ownership + overlap census

Each file has one owning task (first column); a file another task also edits is listed under Overlaps with its order. "Rendered" files and `agents/` are generator output: a task that changes a source regenerates them, and the generator's check mode is their test.

| File | Owner | Also edited by |
|---|---|---|
| `tools/instrument_agents.py` | T1 | — |
| the seven template sources (new; naming deferred, T1) and the seven rendered templates (`skills/redteaming/seat-prompt.md`, `verifier-prompt.md`, `terminal-pass-prompt.md`; `skills/requesting-code-review/code-reviewer.md`; `skills/subagent-driven-development/implementer-prompt.md`, `task-reviewer-prompt.md`, `re-review-prompt.md`) | T1 (created, rendering today's text) | T2 (content) |
| `agents/*.md` (seven, generated) | T1 | T2 (regenerated) |
| `skills/subagent-driven-development/references/premise-and-questions.md` → `seat-rules.md` (rename) | T1 | T2 (content) |
| `tests/test_prose_budget.py`, `tests/prose-budget.txt` | T1 | every later task lowers its skills' lines in `prose-budget.txt` |
| `tests/test_instrument_agents.py`, `tests/instrument_corpus.py`, `tests/test_dispatch_contracts_templates.py`, `tests/test_structure.py`, `tests/test_codex_manifests.py` (docstring), and any other test the splice reaches | T1 | T2 (the citation-resolution test) |
| `AGENTS.md` | T1 (agents bullet; The prose budget) | T2 (Where text goes) |
| `docs/dual-runtime.md` | T1 | — |
| `docs/decisions/instruments.md` | T1 (the generator include) | T2 (plugin-root slot reason; report-write exception) |
| `docs/decisions/authoring-crucible.md` | T1 (The prose budget) | T8 (placement of seat rules) |
| `docs/decisions/runtime-adapters.md` | T1 (the one generated artifact) | T3 (the adapters' content) |
| the seven slot cards (`*.slots.md` beside each template) | T2 (plugin-root slots) | T3 (Operation, Model and Effort lines) |
| `skills/subagent-driven-development/writing-good-tests.md` | T2 | — |
| `skills/subagent-driven-development/references/dispatch-composition.md` | T3 | — |
| `skills/using-crucible/SKILL.md` and the four adapter files in `skills/using-crucible/references/` | T3 | — |
| `skills/dispatching-parallel-agents/SKILL.md` | T3 (step 3) | — |
| `docs/decisions/shared-tree.md`, `docs/decisions/rejected-machinery.md` | T3 | — |
| `skills/subagent-driven-development/SKILL.md` | T4 | T1 (rename citation), T3 (read line; § Shared-tree rules moved out) |
| `skills/subagent-driven-development/references/very-small-lane.md` | T4 | T1 (rename), T3 (shared-tree citation), T6 (route-entry pointer) |
| `skills/requesting-code-review/SKILL.md` | T4 | T3 (read line; shared-tree citation) |
| `skills/finishing-a-development-branch/SKILL.md`, `skills/receiving-review/SKILL.md` | T4 | — |
| `docs/decisions/git-steps.md` | T4 (the renamed Step 6) | — |
| `skills/redteaming/SKILL.md` | T5 | T1 (rename), T3 (read line; shared-tree citation) |
| `skills/redteaming/references/formats.md` | T5 | T3 (shared-tree citation) |
| `skills/redteaming/references/flip-paths.md` | T5 | T1 (rename) |
| `skills/redteaming/references/plan-phase.md`, `folded-lane.md` | T5 | — |
| `skills/brainstorming/SKILL.md`, `skills/brainstorming/references/umbrellas.md`, `lane-note.md`, `folded-lane-document.md` | T6 | T1 (rename, in the first two) |
| `skills/writing-plans/SKILL.md` | T6 | T1 (rename) |
| `skills/using-git-worktrees/SKILL.md`, `skills/systematic-debugging/` (its `.md` files) | T7 | — |
| `docs/authoring.md` | T8 | — |
| `docs/backlog/skill-text-rewrite.md` | T8 | T1 (rename), T3 (shared-tree citation) |
| `docs/backlog/cross-skill-anchor-citations.md` (deleted) | T8 | — |
| `docs/backlog/skill-size-after-compaction.md` | T3 (shared-tree citation) | — |
| `docs/crucible/2026-11-01-skill-text-rewrite/umbrella.md` | T8 (Interfaces line) | the entry's mark at Finish (SDD § Finish, not a task) |
| `docs/upstream.md`; `docs/decisions/evidence-and-findings.md`, `plans.md`, `routes.md`, `spec-campaign.md`, `task-loop.md`, `umbrellas.md` | T1 (rename citations) | any task that moves wrong-level text into one of them (D13), in that task's order |

Overlaps are all ordered by the dependency order above; no two tasks run at once.

## Inter-task contracts

- **The shared seat reference's path** (T1 → all): `skills/subagent-driven-development/references/seat-rules.md`. From T1 on, no tracked file names `premise-and-questions.md` outside `docs/crucible/` and `tests/claudeism_scanner_corpus/`.
- **The splice** (T1 → T2): a template source names a shared section by its exact `##` heading text in `seat-rules.md`; the generator writes each rendered template at its current path and each agent from it; `python tools/instrument_agents.py check` fails on any stale rendered template or agent; a named heading missing from `seat-rules.md` fails generation. T1 states the source naming and the include marker in the generator's docstring; T2 writes to that form.
- **The shared sections' headings** (T2 → T4, T5, T6): the spec's pinned list (Interfaces & boundaries, The shared seat reference's sections), each a `##` heading of `seat-rules.md`, with § Location kept. Composed-seat sites cite them as `` `skills/subagent-driven-development/references/seat-rules.md` § <heading> ``.
- **The moved shared-tree rules** (T3 → T4, T5): `dispatch-composition.md` gains `## Shared-tree rules` (the heading text unchanged from SDD's) holding the no-commit rule, the status check and the replacement line; SDD loses its section, and every citation of `crucible:subagent-driven-development § Shared-tree rules` becomes `` `skills/subagent-driven-development/references/dispatch-composition.md` § Shared-tree rules ``. T3 also adds `## Filling a card` there for the card rules.
- **The read line** (T3 → T4, T5): each of SDD, redteaming and requesting-code-review carries one line telling its controller to read `dispatch-composition.md` and its dispatch reference when the skill starts and after compaction (D7); T4 and T5 keep it as T3 leaves it.
- **The decision ask's form** (T3 → T4, T5, T6): the router gains a `## Decision asks` heading holding R1's definition in one sentence; other sites cite `crucible:using-crucible § Decision asks`.
- **Paired texts** (T2, T5, T6 → T8): the seat side in `seat-rules.md` (T2), the controller side in flip-paths' opening (T5), `umbrellas.md` § Edits (T6) and writing-plans § Deferring detail (T6); each task that edits one side checks the other side still agrees; T8 lists the pairs in `docs/authoring.md` and runs A3's agreement check.
- **The route entry** (T6 ← T4): T6 moves the upgrade hatch's route-entry text from `very-small-lane.md` into brainstorming § Proposing the arrangement (step 4) and leaves a pointer in `very-small-lane.md`; T4 does not touch that line.

## Acceptance mapping

- **A1 (removal lists)** — one-time, every task: its report lists each passage removed or moved beside the owner site that states its rule, and, for T2, each rule a rendered template gained, which must be a correction.
- **A2 (the splice)** — standing tests: rendered templates and agents match their sources, every named section exists, the budget counts by D16 (T1); every citation of a shared section in a rendered template names a section that template takes (T2).
- **A3 (the corrections)** — one-time, each item by its owning task (the task whose Contract names it), command and output in its report; the paired texts' agreement, T8.
- **A4 (the suite)** — standing: every task ends on a full green suite (`python -m pytest tests/`), quoted from the run.
- **A5 (sizes)** — one-time, T8: the net change on D16's count against `8332a00`, each rendered template's size, the `SKILL.md` sizes against 20,000 bytes, the envelope's size.
- **A6 (records and docs)** — one-time, by the task owning each text (census); citations of renamed files and headings resolving is standing (the reference scanner).
- **A7 (the backlog)** — one-time, T8.
- **A8 (the umbrella)** — the Interfaces line, one-time, T8; the entry's mark, at SDD § Finish (not a task: Finish marks the entry before the landing).

## Tasks

### T1 — The splice and the rename

**Why.** D5 and D16 need a generator that renders each seat template from a hand-edited source plus named shared sections, and a budget that counts what is hand-written; every later task cites the shared reference by its new name. T1 builds the mechanism with no change in what any seat reads: each source starts as today's template text, so the rendered templates and agents come out unchanged apart from the rename.

**Files.** `tools/instrument_agents.py`; seven new template sources; the seven rendered templates and `agents/*.md` (regenerated); the rename of `premise-and-questions.md` to `seat-rules.md` and every citer (found by `git grep premise-and-questions`: the skills, `agents/`, the decision records listed in the census, `docs/upstream.md`, `docs/backlog/skill-text-rewrite.md`); the tests in the census; `tests/prose-budget.txt`; the texts that call the template the hand-edited home or `agents/` the one generated artifact (`AGENTS.md`, `docs/dual-runtime.md`, the generator docstring, `docs/decisions/runtime-adapters.md`, `tests/test_codex_manifests.py`'s docstring); the texts stating the budget's basis (`tests/prose-budget.txt`'s header, `tests/test_prose_budget.py`'s docstring, `AGENTS.md` The prose budget, `docs/decisions/authoring-crucible.md` The prose budget); `docs/decisions/instruments.md` (drop the rejected generator include, record the splice; its Changes line). Inputs: `.crucible/placement/brainstorm-decisions.md` for the records' bases.

**Contract.** Enacts D5, D6, D16 and the rename (D4's first half); produces the splice and path contracts above. Owns the spec's deferral marker in Interfaces & boundaries, The splice (source naming, the include marker, includes inside selector passages and beside slot tokens, the orphan check reaching a source, tests reading template text); shares its per-seat-value item with T2.

**Acceptance.**
- Happy: `check` passes on the tree; rendered templates equal today's templates except the renamed path; agents regenerate to the same.
- Edge: a source naming a heading absent from `seat-rules.md` fails generation; a source whose include sits inside a selector passage renders under each selector value as the selector tests expect; a second `write` run changes nothing.
- Error: a hand edit to a rendered template or agent fails `check`; a source left uncited fails the orphan check, or the check is shown to reach it another way.
- Integration: the budget test counts sources and no rendered template (a one-time demonstration that adding a rendered copy of a source does not move the count); the suite is green.

### T2 — The shared seat reference and the seven templates

**Why.** G1 and G2 on the seat side: the clauses the templates copy move into `seat-rules.md` under the pinned sections and come back into each template by splice, P6 deciding which seat takes what, so no seat gains or loses a rule beyond the corrections. The verifier's text is trimmed; the re-reviewer takes the full comment rule.

**Files.** `seat-rules.md`; the seven template sources; the rendered templates and `agents/` (regenerated); `writing-good-tests.md` (its Quick Reference restatements, the justification list's departure); the seven cards' plugin-root slots where their only use was the shared reference; the citation-resolution test (A2); `docs/decisions/instruments.md` (the slot's reason; the verifier and re-reviewer exception to its rejected report-write wording); `AGENTS.md` Where text goes; `tests/prose-budget.txt`. Consumers to account for: every template site citing "the shared reference's § …" (found by search), `redteaming/SKILL.md` § Dispatch composition's listing of the reference among seat inputs (its fix rides T5, which owns that file; T2 reports it as handed over).

**Contract.** Enacts D4, P6, R2–R4 (seat side), and these corrections: the re-reviewer's comment rule, the suite bound's fuller form, the terminal pass's location, § Premise findings' pointer into § The goal check. Produces the section-headings contract. Shares the splice marker's per-seat-value and slot-token items with T1.

**Acceptance.**
- Happy: each pinned heading exists; each template source takes only sections P6 allows; the re-reviewer's rendered text holds the full comment rule.
- Edge: a section whose rule one taker lacks is split or kept in the templates that carry it (shown for the suite bound and the branch reviewer); a spliced section citing a section its seat does not take is split, not given to that seat (shown for the terminal pass and § Questions).
- Error: the citation-resolution test fails on a seeded citation to a section the template does not take.
- Integration: per template, the rules gained list (A1) holds only corrections; `check` and the suite are green.

### T3 — The controller-shared layer

**Why.** D7, D8 and D9: rules every dispatching controller shares go to `dispatch-composition.md`, which each dispatching skill reads at start and after compaction through one kept line; host-neutral rules leave the adapters; the decision ask gets one owner in the router.

**Files.** `dispatch-composition.md` (`## Shared-tree rules` moved in from SDD; `## Filling a card`; effort only on request; item 4's umbrella sentence out); the read line in SDD, redteaming and requesting-code-review, replacing their three paragraphs; SDD's § Shared-tree rules removed and every citer updated (found by `git grep "Shared-tree rules"`: redteaming, `formats.md`, requesting-code-review, `very-small-lane.md`, `docs/decisions/shared-tree.md`, `docs/decisions/rejected-machinery.md`, `docs/backlog/skill-size-after-compaction.md`, `docs/backlog/skill-text-rewrite.md`); the router (never predict, name the model, `## Decision asks`); the four adapter files; dispatching-parallel-agents step 3; the cards' Operation, Model and Effort lines; `docs/decisions/runtime-adapters.md` (the adapters' content); `tests/prose-budget.txt`.

**Contract.** Enacts D7, D8, D9 and R1's owner; the corrections: fan-out independence, requesting-code-review's controller reading `dispatch-composition.md`, the report-file check's scope; `ultra` to the Codex dispatch reference. Produces the shared-tree, read-line and decision-ask contracts. Keeps every C3 guard it moves (the status check, the replacement line) stated in full at its new home.

**Acceptance.**
- Happy: each moved rule is stated once at its owner; each dispatching skill's read line names both files.
- Edge: requesting-code-review keeps its standalone-mode `tree-check.txt` rule; each card keeps the role its seat runs on.
- Error: no citation of SDD's old § Shared-tree rules remains (the reference scanner); the envelope stays under 10,000 characters (`tests/test_session_start.py`), its size quoted.
- Integration: the claude-ism scanner passes (P4); the suite is green.

### T4 — The execution skills

**Why.** D7, D10, D11 and D15 in SDD, the very-small-lane reference, requesting-code-review, finishing and receiving-review: each keeps what its controller does, card inputs and seat rubrics go to their owners, and the execution-side corrections land.

**Files.** `skills/subagent-driven-development/SKILL.md`; `very-small-lane.md`; `skills/requesting-code-review/SKILL.md`; `skills/finishing-a-development-branch/SKILL.md`; `skills/receiving-review/SKILL.md`; `docs/decisions/git-steps.md` (the renamed Step 6's citation); any decision record receiving moved text (D13); `tests/prose-budget.txt`. Consumers: every citation of finishing's Step 6 and of SDD headings this task renames (by search).

**Contract.** Enacts D7, D10 (the adjudicator's composed sections, P6), D11, D15 and the owner map's execution rows; the corrections: lane drift, the amendment-commit slot, the red-suite persistence in the branch review. Consumes the shared-tree, read-line, decision-ask and section-headings contracts.

**Acceptance.**
- Happy: each owner-map row this task touches holds (owner states the rule; other sites point or say nothing).
- Edge: finishing's force-push rule is in its body before its table row goes; the adjudicator's dispatch names § Building the diff, § What binds in a range and its read-only limits, and nothing it does not follow today.
- Error: no dangling citation of a renamed heading (the reference scanner).
- Integration: the suite is green.

### T5 — The redteaming skill and its references

**Why.** The owner map and corrections in redteaming, `formats.md`, `flip-paths.md`, `plan-phase.md` and `folded-lane.md`: the controller keeps what it does, seat mandates live in templates, and the controller side of the paired texts lives in flip-paths' opening.

**Files.** `skills/redteaming/SKILL.md` (including § Dispatch composition's listing of the shared reference, handed over by T2, and § Round 0's composed sections); `skills/redteaming/references/formats.md`, `flip-paths.md`, `plan-phase.md`, `folded-lane.md`; any decision record receiving moved text (D13); `tests/prose-budget.txt`.

**Contract.** Enacts the owner map's redteaming rows and the corrections: the delegated answer's form in `formats.md`, the trace's scope, the folded lane's lens line, flip-paths step 3's "scope finding", the plan-phase second read's wording, the non-local-mechanism list's pointer (paired text, controller side in writing-plans by T6). Consumes the section-headings, shared-tree, read-line and decision-ask contracts.

**Acceptance.**
- Happy: each owner-map row this task touches holds; flip-paths' opening and the shared § What binds sections agree.
- Edge: the round-0 pre-pass names only sections it follows today (§ Suite bound and its scratch rule); the replacement line reaches redteaming's controller through its read line.
- Error: no dangling citation (the reference scanner).
- Integration: the suite is green.

### T6 — Brainstorming, its references and writing-plans

**Why.** The owner map and corrections on the brainstorming and planning side: writing-plans owns the deferral boundaries, the mark rule and the kinds of acceptance check; brainstorming owns the consumer sweep and every route entry, the hatch's included; `umbrellas.md` owns the umbrella finding rule's controller side and names the closing review's composed sections.

**Files.** `skills/brainstorming/SKILL.md`; `skills/brainstorming/references/umbrellas.md`, `lane-note.md`, `folded-lane-document.md`; `skills/writing-plans/SKILL.md`; `very-small-lane.md` (the route-entry pointer only); any decision record receiving moved text (D13); `tests/prose-budget.txt`.

**Contract.** Enacts the owner map's brainstorming and writing-plans rows, R2's controller side, and the corrections: brainstorming's open-items pointer to `formats.md` § Open items; the fuller non-local-mechanism list in writing-plans § Deferring detail. Produces the route-entry move. Consumes the section-headings and decision-ask contracts. `brainstorming/SKILL.md` stays below its size at `8332a00` (C2).

**Acceptance.**
- Happy: each owner-map row this task touches holds; the paired texts it owns agree with their seat side.
- Edge: the closing review's composed sections are § Premise findings, § Binding items and unrecorded choices, § Questions and § Location, as today.
- Error: no dangling citation (the reference scanner).
- Integration: the suite is green; `brainstorming/SKILL.md`'s byte size quoted before and after.

### T7 — using-git-worktrees and systematic-debugging

Review: branch only — it builds no mechanism and nothing later builds on it: two self-contained skills, a trim and three drift fixes whose intended versions the decision records state.

**Why.** D3: using-git-worktrees, outside the kept-close record, comes to crucible's grain; systematic-debugging changes only for the drift its record treats as a defect.

**Files.** `skills/using-git-worktrees/SKILL.md`; `skills/systematic-debugging/SKILL.md` (and its references only where the drift reaches them); `tests/prose-budget.txt`. Consumers: citations of using-git-worktrees' "Steps 0–1", "Steps 2–3", § Step 0 and § 1b, and of systematic-debugging's § When Process Reveals "No Root Cause" (by search), which keep resolving.

**Contract.** Enacts D3 and P3, and the corrections: systematic-debugging's test-first copies, using-git-worktrees' Step 0 and Quick Reference rows.

**Acceptance.**
- Happy: each correction holds, command and output quoted.
- Edge: every cited heading and step number above still exists.
- Error: systematic-debugging changes nowhere its record does not allow (its diff read against `docs/decisions/upstream-skills-kept-close.md`).
- Integration: the suite is green.

### T8 — Docs, backlog and the measurement

Review: branch only — it builds no mechanism and nothing later builds on it: it records what T1–T7 made true and measures it, and the branch review reads it beside the whole diff.

**Why.** A3 (paired texts), A5, A6's remainder, A7 and A8's Interfaces line, and D14.

**Files.** `docs/authoring.md` (D14; the paired-texts list); `docs/decisions/authoring-crucible.md` (placement of seat rules); `docs/backlog/skill-text-rewrite.md` (A7); `docs/backlog/cross-skill-anchor-citations.md` (deleted); `docs/crucible/2026-11-01-skill-text-rewrite/umbrella.md` (the Interfaces line on what `placement` provides); `tests/prose-budget.txt` (final counts). Inputs: `.crucible/placement/brainstorm-decisions.md` for the records' bases.

**Contract.** Enacts D14, A5, A7 and A8's Interfaces line; consumes the paired-texts contract.

**Acceptance.**
- Happy: A5's figures reported against `8332a00`; `docs/authoring.md` states D14 and lists the pairs; each pair agrees (A3), quoted.
- Edge: the backlog item keeps exactly A7's list, the action on a review missing a verdict added.
- Error: no file links the deleted backlog item (by search).
- Integration: the suite is green.
