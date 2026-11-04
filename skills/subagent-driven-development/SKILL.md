---
name: subagent-driven-development
description: Use when executing an implementation plan or a very-small-lane note.
---

# Subagent-Driven Development

Execute a plan by dispatching a fresh implementer subagent per task and one fresh-context reviewer after each, unless the plan routes that task's review to the branch review. The one route with no plan is the operator-confirmed very-small lane: § The very-small lane executes its lane note, and the rest of this skill applies to it only where that section says so.

Between tool calls, narrate at most one short line; the ledger and tool results carry the record. Never ask "should I continue?" or pause between tasks to check in with the operator; stop only for a BLOCKED status you cannot resolve, a stop-and-ask trigger, a decision ask that genuinely needs the operator, or all tasks complete.

**Dispatch references:** when this skill starts and after compaction, read `skills/subagent-driven-development/references/dispatch-composition.md` and your adapter's `skills/using-crucible/references/<runtime>-dispatch.md`; both bind as if written here.

**Stubs.** A reference a section names to read in full binds as if written here. Read it when its step comes, unless read since your last compaction; after compaction, re-read the step in progress's reference first.

## Setup

When this skill starts, read `skills/subagent-driven-development/references/setup.md` in full before any task. Implementation on a main/master checkout needs the operator's explicit consent first.

### Workspace, ledger and dispatch rules

The workspace's `sdd/` subtree holds this plan's execution state: `ledger.md`, `reports/`, `branch-review/`. Never read or write another feature's workspace, except to follow a declared predecessor link.

**The ledger** (`sdd/ledger.md`) is what survives compaction and what the close readout is assembled from: track progress there, not only in todos. Line 1 is the identity line, `# SDD ledger — plan: <plan file path>`; then `## Progress` for the running lines, `## Adjudication rulings`, `## Deferred minors` and `## Questions`. Setup seeds it with what earlier phases left. After compaction, trust the ledger and `git log` over your recollection.

**Resume rule**, if line 1 names your plan: never re-dispatch a task whose latest `Task <N>` line under `## Progress` is a completion line (it is done; a later `reverted` line reopens it) or `Task <N>: BLOCKED — …`, until an answer under `## Adjudication rulings` releases it, which a ruling to block does not. Resume at the first task not done; one whose latest line is a fix wave is mid-loop: resume at the next wave or, after `3/3`, at its open operator ask (§ The Task Loop), never a fourth wave; one whose latest line is a released `BLOCKED — wave <W>` or a `fix wave <W>: implementer` line resumes inside that wave, which counts once. On the very-small lane, re-read its reference first.

**Predecessor links:** when a plan is superseded mid-flight, the successor ledger's line 1 names the successor plan and line 2 links the predecessor ledger, moved aside (e.g. `sdd/ledger-superseded.md`). On resume, follow them before declaring any task not done. A ledger whose line 1 names a plan neither yours nor a declared predecessor is another run's: leave it untouched and escalate. Recover a lost workspace (gitignored, so `git clean -fdx` destroys it), or lost predecessor records, as `skills/redteaming/references/formats.md` § Feature workspace root and layout states.

No dispatch copies the spec: each seat opens it from the plan's spec pointer. Hand artifacts over as files: what you paste into a dispatch and what a seat prints back stay resident in your context. Never run two implementers at once: they share the tree.

## Instruments and report files

**Instruments**, each with a slot card beside its template: `implementer` ([implementer-prompt.slots.md](implementer-prompt.slots.md)) for every implementer seat, a fresh fix-wave one included; `task-reviewer` ([task-reviewer-prompt.slots.md](task-reviewer-prompt.slots.md)); `re-reviewer` ([re-review-prompt.slots.md](re-review-prompt.slots.md)). Fill the card, not the template ([implementer-prompt.md](implementer-prompt.md), [task-reviewer-prompt.md](task-reviewer-prompt.md), [re-review-prompt.md](re-review-prompt.md)).

Each review seat and the adjudicator replies with a short verdict and its report's path; confirm every seat's report file, an implementer's included, as the dispatch composition's item 5 states.

## Models

Instrument cards name their seats' roles. The seats you compose:

- **Adjudicator:** the default role, since its dismissals close findings without further review.
- **Snapshot-blessing agent:** the bounded role or better, a blind check of one stated claim.

## The Task Loop

Run each task through this loop, in plan order: when Setup is done, read `skills/subagent-driven-development/references/task-loop.md` in full. Three fix waves at most per task. Findings the third wave leaves open stop the task and are a decision ask, recorded open under `## Adjudication rulings` with the answer beside it; further waves are not an answer. The options:
- park a finding, with its reason: a `Task <N>: parked — <finding> — ruling: <the answer>` line per finding, then the completion line with its parked count;
- block: `Task <N>: BLOCKED — <the ruling>`, and execution stops at that task until the operator rules again;
- another approach: a plan change (§ Plan changes mid-execution) or a revert (§ Drift found after the fact), whose re-run starts at wave 1. A plan change short of a supersede, once it lands, appends `Task <N>: plan changed — <the ruling> (BASE <base7>)`, which closes the open findings: run the task again from step 1 on the changed plan, that BASE kept and the findings and its earlier report in the implementer's context, its report going to step 3 even where the task is marked, so its review, given every run's report, re-grades them.

## Rules every route shares

These hold in the task loop, in the branch review `crucible:requesting-code-review` runs, and on the very-small lane. The dispatch composition's § Shared-tree rules bind every seat you start; the status check's windows are the review seats (task reviewer, re-reviewer, adjudicator, snapshot-blessing agent, branch reviewer), and a replacement seat reads the first seat's file. A review missing a verdict goes back to its seat: resume it for that verdict; where the host cannot resume or the verdict is still missing, start a replacement seat; one that leaves it out too is a decision ask. You never rule on it yourself.

### Disputes and adjudication

A finding is fixed or disputed, never dropped; every ruling is a ledger entry. Whenever a finding is disputed, collides with plan text or carries the `literal-reading` label, read `skills/subagent-driven-development/references/disputes-and-adjudication.md` in full before acting on it. Record an operator's answer to any decision ask under `## Adjudication rulings` beside the ruling it settles, and enter it in `brainstorm-decisions.md` (status: `crucible:brainstorming` § Workspace provisioning).

### What a report voices

Before routing what a report carries beside its work, read `skills/subagent-driven-development/references/what-a-report-voices.md` in full.

### Drift found after the fact

When work is found off-plan without a logged decision, read `skills/subagent-driven-development/references/drift.md` in full.

## Inline mode

Before implementing a task yourself instead of dispatching it, read `skills/subagent-driven-development/references/inline-mode.md` in full.

## Plan changes mid-execution

Defective or superseded plan text found mid-execution takes a flip path, since executing it produces reviewable-but-wrong work. Triggers: a BLOCKED escalation of a defective plan; an operator's answer, an adjudication or a ruling of yours that changes plan text; an operator's ruling on a premise finding during the task loop; binding content a finding shows wrong (what the Deviations paragraph of § The Task Loop names, or binding-by-construction contract content); a supersede called for, an unfold included. **Before acting on any of them, read `skills/redteaming/references/flip-paths.md` in full**, and re-read it after compaction; a scoped amendment is yours to confirm where that file's § The containment test finds the change contained, and a flip in flight shows in the ledger as its recorded decision ask or ruling. `skills/brainstorming/references/umbrella-children.md` § Under an umbrella governs a feature found to need splitting and, where the spec preamble has an `Umbrella:` line, a binding change its umbrella needs or one landed on the base the feature has not taken in; check for these at each task boundary and before each branch-review pass and wave. **Before raising either, and before the first such check, read that section**, and re-read it after compaction.

## Whole-Branch Review

After the last task completes, run `crucible:requesting-code-review` for its capped whole-branch review: it owns the branch-review loop and its inputs, the ledger's deferred minors, leads and adjudication rulings among them. When it ends, after its cleanup wave where you open one, go to § Finish.

## The very-small lane

The third route, beside the standard and folded presets: the very-small preset (`crucible:brainstorming` § Proposing the arrangement), executed from a lane note and entered only as its reference states. **On entering the lane, read `skills/subagent-driven-development/references/very-small-lane.md` in full**; where it says so, it supersedes this skill's rules for the lane.

## Finish

When the branch review ends, read `skills/subagent-driven-development/references/finish.md` in full; its step order is binding. After any loop activity, restart at step 1, so new records, rulings included, are checked and reach the close readout.

## Common Rationalizations

| Excuse | Reality |
|---|---|
| "I'll fix it myself, dispatching is overhead" | Your fix skips review: resume the implementer, or use inline mode, where any loop-entering finding converts back to dispatch. |
| "The implementer deviated but the result looks fine" | Undisclosed drift from binding content is the operator's call, never yours; disclosed but unjustified, it goes to the fix loop. |
| "The fix was small, skip the re-review" | Every wave that changes code ends with a scoped re-review. |
