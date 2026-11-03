---
name: subagent-driven-development
description: Use when executing an implementation plan or a very-small-lane note.
---

# Subagent-Driven Development

Execute a plan by dispatching a fresh implementer subagent per task and a single fresh-context reviewer after each (unless the plan routes that task's review to the branch review); then hand the branch to `crucible:requesting-code-review` for its capped whole-branch review. The one route with no plan is the operator-confirmed very-small lane: § The very-small lane executes its lane note, and the rest of this skill applies to it only where that section says so.

**Why subagents:** a seat never inherits your session's history — you construct exactly what it needs, which keeps it focused and keeps your own context for coordination.

**Narration:** between tool calls, narrate at most one short line — the ledger and the tool results carry the record.

**Continuous execution:** do not pause to check in with the operator between tasks. Stop only for a BLOCKED status you cannot resolve, a stop-and-ask trigger, a decision ask that genuinely needs the operator, or all tasks complete — never a "should I continue?". A decision ask takes the form `crucible:using-crucible` § Decision asks states.

**Dispatch references:** when this skill starts, and again after compaction, read from the plugin root `skills/subagent-driven-development/references/dispatch-composition.md`, the rules every dispatch shares, and your adapter's `skills/using-crucible/references/<runtime>-dispatch.md`; both bind as if written here.

**Stubs.** Where a section names a reference to read in full, read it when the section's step comes; it binds as if written here. After compaction, re-read the reference of the step in progress before you act, and each other one only when its step next comes.

## Setup

When this skill starts, read `skills/subagent-driven-development/references/setup.md` in full before any task. Implementation on a main/master checkout needs the operator's explicit consent first.

### Workspace, ledger and dispatch rules

The workspace's `sdd/` subtree holds this plan's execution state: `ledger.md`, `reports/`, `branch-review/`. Another feature's workspace is never yours to read or write, except to follow a declared predecessor link (below).

**The ledger** (`sdd/ledger.md`). Conversation memory does not survive compaction: track progress in the ledger, not only in todos.

- Line 1 is the identity line: `# SDD ledger — plan: <plan file path>`.
- Sections: `## Progress` for the running lines, then `## Adjudication rulings`, `## Deferred minors` and `## Questions`.
- **Leads** are `## Deferred minors` lines the branch reviewer rules on rather than triages (`crucible:requesting-code-review`): each opens with its source — `Task <N>`; `Lane` on the very-small lane and for what its upgrade hatch carries over; `Branch wave <n>` for a branch-review fix report's — then `lead (<kind>):`, `<kind>` one of `question`, `proposal`, `concern`, then the one-line item, as in `Task 3: lead (question): <one-liner>`; a finding the lane left open carries its severity first, `Lane: lead (concern): <severity> — <one-liner>`. **`## Questions`** holds the branch review's own questions, each `Branch review pass <k>: <item> — <your disposition>` or `Branch wave <n>: <item> — <your disposition>`, and what earlier phases left open, each `<phase>: <item> — carried` (below). No seat reads that section; the close readout lists it.
- **Contained amendments** the plan phase made are seeded at its close under `## Adjudication rulings`, as your rulings (`skills/redteaming/references/plan-phase.md`). **Whenever the plan record's `## Fix list` (`campaigns/plan/round-01/record.md`) names a `Contained amendment:` item the ledger lacks, copy it there yourself before dispatching, in the item's own form, with the reason and why it is contained from the ruling of the merged entry that led to it:** the item alone carries neither, and the branch review and the close readout find it only in the ledger.
- **Open premise asks, what earlier phases left open and `deferred-minor` entries** (`## Deferred minors` lines, source `Spec` or `Plan`) are seeded at the close that seeds the ledger (`skills/redteaming/references/plan-phase.md`: **Close**, **What earlier phases left open**); on the very-small lane you seed the `— carried` lines at Setup, from the brainstorm decision record. **Whenever the campaign records or the brainstorm decision record hold an open premise ask, an item for a `— carried` line or a `deferred-minor` entry that the ledger lacks, seed it yourself before dispatching** — the ask under `## Adjudication rulings` as open.
- **Resume rule:** if line 1 names your plan, a task whose latest `Task <N>` line under `## Progress` is a completion line is done — never re-dispatch it; a later `reverted` line reopens it. Resume at the first task not done; one whose latest line is `Task <N>: BLOCKED — …` waits on its open ask and is never re-dispatched. A task whose last line is a fix wave is mid-loop: resume at the next wave, or, after `3/3`, at its open operator ask (§ The Task Loop, step 5), never a fourth wave. On the very-small lane, re-read its reference first.
- **Predecessor links:** when a plan is superseded mid-flight, the successor ledger's line 1 names the successor plan and its line 2 links the predecessor ledger, moved aside (e.g. `sdd/ledger-superseded.md`); after the very-small lane's upgrade hatch, the lane's, as `sdd-lane/ledger.md`. On resume, follow predecessor links **before declaring any task not done** — the sanctioned exception to workspace isolation. If the predecessor records are gone, recover as from a lost workspace (below).
- A ledger whose line 1 names a plan that is neither yours nor a declared predecessor is another run's: leave it in place and escalate, never overwrite it.
- After compaction, trust the ledger and `git log` over your recollection. A lost workspace — `git clean -fdx` destroys it, since it is gitignored — is recovered as `skills/redteaming/references/formats.md` § Feature workspace root and layout states.

**Every dispatch.** The spec is a shared input each seat opens for itself from the plan's spec pointer; no dispatch copies it. Everything you paste into a dispatch prompt — and everything a seat prints back — stays resident in your context for the rest of the session. Hand artifacts over as files. Never run two implementers at once: they share the tree.

## Instruments and report files

**Instruments.** Three seats are instruments, each with a slot card beside its template: instrument `implementer` ([implementer-prompt.slots.md](implementer-prompt.slots.md)) for every implementer seat, a fresh fix-wave one included; instrument `task-reviewer` ([task-reviewer-prompt.slots.md](task-reviewer-prompt.slots.md)); instrument `re-reviewer` ([re-review-prompt.slots.md](re-review-prompt.slots.md)). Fill the card, not the template ([implementer-prompt.md](implementer-prompt.md), [task-reviewer-prompt.md](task-reviewer-prompt.md), [re-review-prompt.md](re-review-prompt.md)), as `skills/subagent-driven-development/references/dispatch-composition.md` § Filling a card states.

**Report files.** Each review seat and the adjudicator writes its report file at a path no earlier dispatch used, and replies with a short verdict and that path. Confirm every seat's report file, an implementer's included, as the dispatch composition's item 5 states.

## Models

The rules every dispatch shares — name the model, the three roles and the floor, effort — are in `skills/subagent-driven-development/references/dispatch-composition.md` § Models and effort. This skill's seats:

- **Implementer:** the default role, or the alternate role where one of its triggers selects this seat; a clearly bounded task may drop to the bounded role.
- **Task reviewer:** the default role, every task it reviews, or the alternate role where one of its triggers selects this seat.
- **Re-reviewer:** the bounded role or better, always.
- **Adjudicator:** the default role — its dismissals close findings without further review.
- **Snapshot-blessing agent:** the bounded role or better — a blind check of one stated claim.

## The Task Loop

Run each task through this loop, in plan order: when Setup is done, read `skills/subagent-driven-development/references/task-loop.md` in full. **Three fix waves at most per task.** After the third wave, findings it leaves open stop the task: put them to the operator as a decision ask — park a finding, with its reason; block the work; or another approach — recorded under `## Adjudication rulings` as open, the answer beside it. Park: a `Task <N>: parked — <finding> — ruling: <the answer>` line per finding, then the completion line with its parked count. Block: `Task <N>: BLOCKED — <the ruling>`, and execution stops at that task until the operator rules again. Another approach: the answer names it — a plan change (§ Plan changes mid-execution) or a revert (§ Drift found after the fact), whose re-run starts at wave 1. Further waves are not an answer.

## Rules every route shares

These hold in the task loop, in the branch review `crucible:requesting-code-review` runs, and on the very-small lane.

**The shared tree.** `skills/subagent-driven-development/references/dispatch-composition.md` § Shared-tree rules bind every seat you start. The status check's windows are the review seats — task reviewer, re-reviewer, adjudicator, snapshot-blessing agent, branch reviewer — and a replacement seat writes to its card's path with `-r<R>` before `.md` and reads the first seat's file.

### Disputes and adjudication

A finding is fixed or disputed, never dropped: a silent discard is forbidden, and every ruling is a ledger entry. Whenever a finding is disputed, read `skills/subagent-driven-development/references/disputes-and-adjudication.md` in full. Record an operator's answer to any decision ask under `## Adjudication rulings` beside the ruling it settles, and where `skills/redteaming/references/formats.md` § Feature workspace root and layout sends it.

### What a report voices

Before routing what a report carries beside its work, read `skills/subagent-driven-development/references/what-a-report-voices.md` in full.

### Drift found after the fact

When work is found off-plan without a logged decision, read `skills/subagent-driven-development/references/drift.md` in full.

## Inline mode

Before implementing a task yourself instead of dispatching it, read `skills/subagent-driven-development/references/inline-mode.md` in full.

## Plan changes mid-execution

Executing defective or superseded plan text produces reviewable-but-wrong work, so such text found mid-execution — a BLOCKED escalation of a defective plan, an operator's answer that changes plan text, an adjudication or a ruling of yours that patches the plan, an operator's ruling on a premise finding given during the task loop — takes a flip path, as do binding content a finding shows wrong (what the Deviations paragraph of § The Task Loop names, or binding-by-construction contract content) and a supersede called for, an unfold included; a scoped amendment is yours to confirm where § The containment test of the reference named below finds the change contained. The reference named below also governs a feature found to need splitting and, where the spec's preamble carries an `Umbrella:` line, a binding change its umbrella needs or one landed on the base that the feature has not taken in, checked for at each task boundary (§ The Task Loop, step 1) and before each branch-review pass and wave (`crucible:requesting-code-review` § The branch-review loop). **Before acting on any of them, read `skills/redteaming/references/flip-paths.md` in full**, and re-read it after compaction: a flip in flight shows in the ledger through its recorded decision ask or ruling.

## Whole-Branch Review

After the last task completes, run `crucible:requesting-code-review`: it owns the branch-review loop and its inputs, the ledger's deferred minors, leads and adjudication rulings among them. Its disputes follow § Disputes and adjudication, its seats the shared tree (§ Rules every route shares), and drift it finds in a completed task § Drift found after the fact. When it ends, after its cleanup wave where you open one, go to § Finish.

## The very-small lane

The third route, alongside the standard and folded presets: the very-small preset (`crucible:brainstorming` § Proposing the arrangement (step 4)), executed from a lane note and entered only as its reference states. **On entering the lane, read `skills/subagent-driven-development/references/very-small-lane.md` in full**; where it says so it supersedes this skill's rules for the lane.

## Finish

When the branch review ends, read `skills/subagent-driven-development/references/finish.md` in full. The order is binding. After any loop activity, restart at step 1, so new records — rulings included — are checked and reach the close readout. **Step 3, the answer:** wait for it; integration stays the operator's decision. An answer that asks for more work, or a ruling that opens a wave, reopens the loop (`crucible:requesting-code-review` § The branch-review loop) before any later step, and Finish restarts at step 1. Where loop activity follows an answer, a red suite's included, the next readout reports what changed, and the earlier answer stands only where nothing new was left open; otherwise you ask again. An answer choosing an integration option runs steps 4–7 in order. Where step 2 asked where open items go, steps 4–7 wait until the answer says, or drops them; ask again, and leave the workspace in place, until it does. An answer that discards the work skips steps 4 and 5, and takes finishing's typed `discard` confirmation before step 6, deleting the feature workspace; one left unconfirmed counts as an answer that chose no option. An answer that leaves the work in place but chooses no option runs them too, and at step 7 finishing presents its options with your recommendation.

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Close enough on spec compliance" | A failed intent, scope or deviation verdict enters the loop at any severity. Fix it, dispute it with evidence, or reach the cap — the only exits. |
| "I'll fix it myself, dispatching is overhead" | Controller fixes pollute your context and skip review. Resume the implementer — or use inline mode, where any loop-entering finding converts back to dispatch. |
| "This finding is obviously wrong, I'll drop it" | Rule on it with your evidence — the adjudicator rules where it touches what binds, the Intent or your own diff — and the ruling reaches the ledger and the close readout. Silent drops are forbidden. |
| "One more wave will converge" | Past the cap, waves don't converge — the failure is structural. Put it to the operator. |
| "The implementer deviated but the result looks fine" | Undisclosed drift from binding content is the operator's call — never yours. Disclosed-but-unjustified goes to the fix loop. |
| "The fix was small, skip the re-review" | Unreviewed fixes are how regressions land. Every wave that changes code ends with a scoped re-review. |
| "Ledger bookkeeping is overhead" | The ledger is what survives compaction — and what the close readout is assembled from. |
