# Seat voice — plan

Spec: `docs/crucible/2026-10-29-seat-voice/design.md` @ `e14f895` — binding: its Constraints & invariants (C1–C4), and through its `Umbrella:` line this feature's entry in `docs/crucible/2026-10-28-hypothesis-specs/umbrella.md` and that umbrella's Constraints & invariants (C1); the spec records no firm decision and no marks, the umbrella none either. A task calling for a change to those is a plan defect.

## Goal

The seat-side rules of D1–D4 live in one new shared reference and the controller-side premise routing in `flip-paths.md`; every seat template, controller skill and route reference that the spec's owners list names points to them and carries the spec's other decisions (D5–D9); the decision records, `docs/upstream.md` and the two backlog items state the new positions; the suite passes and `agents/` matches its templates.

## Task dependency order

T1 → T2 → T3 → T4 → T5 → T6, strictly sequential: every task edits `tests/prose-budget.txt`, T2–T4 point to what T1 writes, and T6's sweeps read the finished skills.

## File ownership + overlap census

| File | Owner |
|---|---|
| `skills/subagent-driven-development/references/findings-and-questions.md` (new) | T1 |
| `skills/redteaming/references/flip-paths.md` | T1 |
| `skills/redteaming/seat-prompt.md`, `skills/redteaming/seat-prompt.slots.md` | T2 |
| `skills/redteaming/SKILL.md` | T2 |
| `skills/redteaming/references/formats.md` | T2 |
| `skills/redteaming/references/plan-phase.md` | T2 |
| `skills/redteaming/references/folded-lane.md` | T2 |
| `skills/redteaming/verifier-prompt.md`, `skills/redteaming/verifier-prompt.slots.md` | T2 |
| `agents/redteam-seat.md`, `agents/blind-verifier.md` (generated) | T2 |
| `skills/requesting-code-review/code-reviewer.md`, `skills/requesting-code-review/code-reviewer.slots.md` | T3 |
| `skills/requesting-code-review/SKILL.md` | T3 |
| `agents/branch-reviewer.md` (generated) | T3 |
| `skills/subagent-driven-development/task-reviewer-prompt.md`, `task-reviewer-prompt.slots.md` | T4 |
| `skills/subagent-driven-development/re-review-prompt.md`, `re-review-prompt.slots.md` | T4 |
| `skills/subagent-driven-development/implementer-prompt.md`, `implementer-prompt.slots.md` | T4 |
| `skills/subagent-driven-development/SKILL.md` | T4 |
| `skills/subagent-driven-development/references/very-small-lane.md` | T4 |
| `agents/task-reviewer.md`, `agents/re-reviewer.md`, `agents/implementer.md` (generated) | T4 |
| `skills/brainstorming/SKILL.md` | T5 |
| `skills/brainstorming/references/lane-note.md`, `folded-lane-document.md`, `umbrellas.md` | T5 |
| `docs/decisions/evidence-and-findings.md`, `model-roles-and-effort.md`, `the-spec.md`, `task-loop.md`, `branch-review.md`, `spec-campaign.md`, `routes.md`, `umbrellas.md` | T6 |
| `docs/decisions/authoring-crucible.md`, `brainstorming-first.md`, `plans.md` (edited only where a position they state changes) | T6 |
| `docs/upstream.md` | T6 |
| `docs/backlog/review-improvements.md` (deleted), `docs/backlog/review-catch-and-implementers.md` | T6 |
| `tests/prose-budget.txt` | T1–T5, each its own skills' lines |

**Overlaps:** `tests/prose-budget.txt` only, each task changing the lines of the skill directories it edits (T1: `subagent-driven-development` and `redteaming`; T2: `redteaming`; T3: `requesting-code-review`; T4: `subagent-driven-development`; T5: `brainstorming`), ordered by the sequence. No other file has two owners.

## Inter-task contracts

- **The shared reference** (T1 produces; T2, T3, T4 point to it by path and section): path `skills/subagent-driven-development/references/findings-and-questions.md`, with exactly these `##` sections, their names the anchors pointers cite: `## Premise findings` (D1's seat side), `## The goal check` (D2), `## Questions` (D3), `## Location` (D4). A seat reads it under the plugin root its dispatch names.
- **Premise routing** (T1 produces; T2, T3, T4 point to it): `skills/redteaming/references/flip-paths.md` gains a `### Premise findings` section stating D1's controller side once: always the operator as a decision ask; an open decision ask, not an open BLOCKER or MAJOR, holding no gate keyed on one (C1); work goes on unless later work builds on the challenged premise; the ruling's route by kind; the carry chain across closes (below); and the precedence where a finding is both a premise finding and a binding item found wrong. Its opening scope sentence widens so that this section applies at any phase.
- **The carry chain**, including the second read's two open MINORs (T1 states it in the section above; T2 and T4 implement its steps): an open premise ask raised by a plan-phase seat is carried in the plan record until the plan phase's close seeds it into the ledger's `## Adjudication rulings` as open; one open when a spec campaign closes is carried in the digest's `## Open judgments` (a minor design's close readout where there is no digest) and seeded at the plan phase's close, or at the campaign's close on the folded lane; one raised after the ledger exists is written there directly; an umbrella's campaign cannot close its landing with one open, since its children build on it, so the umbrella lands only once it is ruled.
- **The goal check's input for a plan** (T1 states it; T2 implements the seat's read scope): a plan-phase seat restates the goal from the `## Request` section of the spec its plan's header names; the seat's read scoping admits that section beside the binding content.
- **Fixed names** (each producer named; consumers use them verbatim): the label `premise` (T1); the section heading `## Request` (T5 defines it in the spec contract; T1's goal check and T3's Lane Fit read it); the lead verdicts `CONFIRMED`, `RECOMMENDED`, `LEFT` (T3 defines them in the branch-reviewer template; T4's ledger text names them); the ledger section `## Questions` (T4 defines it in SDD § Setup; T3's read-scoping exclusion and the close readout name it); a fix-list item may name a question id `<seat-id>-q<n>` as what it resolves (T2, in `formats.md`).
- **The redteam seat's plugin root** (T2, internal): its slot card gains a plugin-root slot like the other instruments' cards; redteaming § Dispatch composition's closed input list admits the shared reference.
- **The task reviewer's tier** (T4 produces; T6 records it): SDD § Models gives the task reviewer its own row, the default role; the re-reviewer keeps "the bounded role or better"; both slot cards follow their rows.

## Acceptance mapping

| Spec criterion | Task | Check |
|---|---|---|
| A1 | T1 (reference), T2–T4 (pointers); sweep in T6 | One-time: search over `skills/` for the reference's key phrases finds them only in the reference |
| A2 | T1; sweep in T6 | One-time search: `flip-paths.md` states it; redteaming, SDD and `requesting-code-review` point to it |
| A3 | T2 | Standing: `tests/test_conserve.py`, unchanged, passes |
| A4 | T4 (skills), T6 (records); search in T6 | One-time search over `skills/` and the records' Decision sections |
| A5 | T5 | One-time search |
| A6 | T3 (Lane Fit, trace question), T5 (check 5) | One-time search, in each task |
| A7 | T4 | One-time search |
| A8 | T2 (the contained-amendment item), T6 (the two record defects) | One-time check per item |
| A9 | T6 | One-time: backlog listing; each edited record's diff adds a Changes line |
| A10 | every task | Standing: the suite, `instrument_agents.py check` included |
| A11 | — | Why neither: a statement at the landing, read by the operator; the controller writes it at Finish |
| A12 | T2 (stop trigger, cap escalation), T3 (review end, merge red flag), T4 (task completion); sweep in T6 | One-time search |
| A13 | T2 (fix-list question id, carry steps), T3 (lead verdicts, read exclusion), T4 (ledger `## Questions`, close readout, re-reviewer ruling, seeding); sweep in T6 | One-time search per site |

## Deferred-items routing table

| id | source (spec or plan site) | one-line intent | owning task |
|---|---|---|---|
| DI-1 | spec § Mechanism sketches, last bullet | wording and placement of each pointer | T2 |
| DI-1 | spec § Mechanism sketches, last bullet | wording and placement of each pointer | T3 |
| DI-1 | spec § Mechanism sketches, last bullet | wording and placement of each pointer | T4 |
| DI-1 | spec § Mechanism sketches, last bullet | wording and placement of each pointer | T5 |
| DI-2 | spec § Mechanism sketches, last bullet | the ledger line forms for a lead and a question | T4 |
| DI-3 | plan T1 | the shared reference's wording within its four sections | T1 |

## Tasks

### T1 — The two homes

**Why.** C4 puts the seat-side rules once in a shared reference and the controller-side routing once in `flip-paths.md`; every later task points to them, so they land first. This task also settles the second read's two open MINORs as contracts (the carry chain; a plan-phase seat's Request input).

**Files.** The new shared reference; `skills/redteaming/references/flip-paths.md`; `tests/prose-budget.txt` (`subagent-driven-development`, `redteaming`). Consumers: none yet point here; T2–T4 add them.

**Contract.** Produces the shared reference and the `### Premise findings` section, as the inter-task contracts state, the carry chain and the goal check's input for a plan included. Enacts D1 (both sides), D2, D3's definition, D4, C1, C4.

Deferred to implementation: the shared reference's wording within its four sections (DI-3).

**Acceptance.**
- Happy: the reference has the four sections; `flip-paths.md`'s new section states each element the contract lists, and its scope sentence covers any phase.
- Edge: the reference states the fallback where no `## Request` exists (D5's last sentence) and a plan-phase seat's input; the `flip-paths.md` section states the precedence for a firm decision or a lane note's Intent found wrong.
- Error: the reference restates no routing (that is `flip-paths.md`'s), and `flip-paths.md` restates no seat rule (one-time search for the label's definition in both).
- Integration: the suite passes (the reference is reachable as a cited file wherever later cited).

### T2 — Redteaming

**Why.** Redteam seats raise premise findings and widened `Questions`; the controller merges them, keeps them out of the stop rule's BLOCKER count, carries open asks across closes and lets an adopted improvement ride the fix list. D9's contained-amendment item also lives here.

**Files.** `skills/redteaming/seat-prompt.md`, `seat-prompt.slots.md`, `SKILL.md`, `references/formats.md`, `references/plan-phase.md`, `references/folded-lane.md`, `verifier-prompt.md`, `verifier-prompt.slots.md`; `agents/redteam-seat.md`, `agents/blind-verifier.md` (regenerated); `tests/prose-budget.txt` (`redteaming`). Consumers: every site stating "a binding item is itself wrong", "Improvements and style preferences are not findings", the `## Questions` definition, the stop trigger and cap escalation, the fix-list item form and the `Contained amendment:` form, found by search.

**Contract.** Consumes T1's two homes. Enacts D1 (merge: a premise entry parked as a decision ask; the stop trigger and cap escalation read it as an ask), D2 (seats, plan-phase seats via the spec's `## Request`), D3 (seats' section; an adopted improvement as a fix-list item naming the question id), D4, D9's third bullet (item form; the verifier verdicts the item from its plan-side hunks; the reason and why it is contained in the merged entry's ruling; the ledger copy carries both), and the carry chain's spec-campaign, folded-lane and plan-phase steps. Produces the fix-list question-id form and the seat's plugin-root slot.

**Acceptance.**
- Happy: a seat report with a `premise` finding and widened `Questions` still parses for `conserve.py` (standing `tests/test_conserve.py`).
- Edge: a round whose only BLOCKER is a premise finding can be the stop round; a `Contained amendment:` item names no reason; the verifier template says how such an item is verdicted.
- Error: an adopted improvement never opens a wave by itself (the fix-list text says it rides one).
- Integration: `instrument_agents.py check` and the suite pass after regeneration.

### T3 — The branch review

**Why.** The branch reviewer is the last review on every arrangement and the lane's first: it raises premise findings, runs the goal check (on the lane inside Lane Fit), carries `Questions`, rules on leads and asks the trace question; its loop must not count a premise finding as an open MAJOR.

**Files.** `skills/requesting-code-review/code-reviewer.md`, `code-reviewer.slots.md`, `SKILL.md`; `agents/branch-reviewer.md` (regenerated); `tests/prose-budget.txt` (`requesting-code-review`). Consumers: the Calibration and Output Format sections, the Lane Fit passage, the Execution Trail triage, the loop's end condition, Red Flags, the standalone mode, found by search.

**Contract.** Consumes T1's homes and the fixed names. Enacts D1 (raising; the loop's end condition and merge red flag read a premise finding as an ask), D2 (with the lane's Lane Fit verdict), D3 (its section; its items to the ledger's `## Questions`; a fix wave's `Questions` items there too; an adopted improvement riding the next wave), D4, D7's lane ruling, D8's review question, C2's standalone case. Produces the verdicts `CONFIRMED`, `RECOMMENDED`, `LEFT` and the read-scoping exclusion of the ledger's `## Questions`.

**Acceptance.**
- Happy: the template has the goal check, the trace question, the `Questions` section and the lead verdicts (one-time search).
- Edge: standalone mode says its report is the record (C2); without a `## Request`, the goal check says the request was unavailable.
- Error: a pass with only a premise finding open ends the review (the end condition's text).
- Integration: suite and agent check pass.

### T4 — Subagent-driven development

**Why.** The task loop, its reviewers and the implementer carry D3, D4, D6 and D7; SDD owns the ledger, so it defines `## Questions`, the lead lines, the seeding of open premise asks after the ledger exists, and the close readout's sources.

**Files.** `skills/subagent-driven-development/task-reviewer-prompt.md`, `task-reviewer-prompt.slots.md`, `re-review-prompt.md`, `re-review-prompt.slots.md`, `implementer-prompt.md`, `implementer-prompt.slots.md`, `SKILL.md`, `references/very-small-lane.md`; `agents/task-reviewer.md`, `agents/re-reviewer.md`, `agents/implementer.md` (regenerated); `tests/prose-budget.txt` (`subagent-driven-development`). Consumers: § Models' reviewer row and both slot cards' model lines, step 2's `DONE_WITH_CONCERNS`, step 3's missing-verdict rule, task completion, § Setup's sections and the contained-amendment copy, § Finish's close readout, the lane's transcription, every "file:line" and "not findings" site, found by search.

**Contract.** Consumes T1's homes and the fixed names. Enacts D3 (task reviewer and implementer sections; their items as leads), D4, D6 (the split row), D7 (the task reviewer's and re-reviewer's concern rulings; a missing ruling is a missing verdict; no pre-review handling; the implementer's premise heading and status; out-of-task proposals routed), C3, the carry chain's after-ledger step, and the ledger's `## Questions` read by the close readout.

Deferred to implementation: the ledger line forms for a lead and a question (DI-2).

**Acceptance.**
- Happy: one-time searches find the concern line in the deviation audit, the re-reviewer's ruling, the default-role task-reviewer row, the ledger's `## Questions` among § Setup's sections and in the close readout's sources.
- Edge: on the very-small lane a dispatched implementer's concerns are transcribed as leads; a confirmed MINOR concern goes to the ledger, a confirmed intent gap fails intent.
- Error: no text still has the controller "note" a concern or handle it before review; a review missing a concern's ruling is treated as missing a verdict.
- Integration: suite and agent check pass.

### T5 — Brainstorming

**Why.** The request is written where every route's document is written, and the author-side trace check sits in brainstorming's self-review.

**Files.** `skills/brainstorming/SKILL.md`, `references/lane-note.md`, `references/folded-lane-document.md`, `references/umbrellas.md`; `tests/prose-budget.txt` (`brainstorming`). Consumers: the spec contract's section list, check 5, the lane note's and folded document's section lists, the umbrella § Shape and § Children, found by search.

**Contract.** Produces `## Request` (the name T1 and T3 read). Enacts D5 (placement outside binding parts; what counts; redaction and the ask-once default; a child's pointer, and the whole request where its umbrella has none; the fallback) and D8's author side.

**Acceptance.**
- Happy: each of the four shapes lists `## Request` before the Intent (one-time search).
- Edge: the lane note's binding parts stay Intent, Acceptance and Out of scope; the umbrella shape says what a child quotes.
- Error: check 5's trace names routes and phases, not only sites.
- Integration: suite passes.

### T6 — Records, backlog and the integration sweep

**Why.** The positions changed in T1–T5 are recorded where crucible keeps why it is as it is; D9's two record defects are fixed; the backlog is resolved; and the one-time sweeps that need every skill finished run here.

**Files.** The decision records in the census, `docs/upstream.md`, the two backlog items. Inputs: the brainstorm decision record, `.crucible/seat-voice/brainstorm-decisions.md`, for each position's basis from its entry's proposer and status. Consumers: every record stating a position the spec changes, found by searching the spec's key terms (premise, Questions, improvements, file:line, the task reviewer's tier, Lane Fit, the request, concerns).

**Contract.** Enacts D9's first two bullets, the records' side of D1–D8, and the backlog changes A9 names. Runs the integration sweeps A1, A2, A4, A12, A13.

**Acceptance.**
- Happy: each changed record states the new position and adds a dated Changes line; `review-improvements.md` is gone; `review-catch-and-implementers.md` keeps only the per-task-review follow-up; `docs/upstream.md`'s Recommendations row names the new home.
- Edge: a record whose position did not change is not edited.
- Error: no record tags a controller proposal as the maintainer's preference (checked against the decision record).
- Integration: the sweeps' commands and outputs in the report; suite passes.
