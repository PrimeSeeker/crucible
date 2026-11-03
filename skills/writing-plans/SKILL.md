---
name: writing-plans
description: Use when a spec has closed its redteam campaign and needs an implementation plan, before touching code.
---

# Writing Plans

## Overview

A plan is an agent coordination artifact. Its readers are strong fresh-context implementers and reviewers who each see one task — and each of them also reads the spec, which is a shared input, not something the plan re-tells. So the plan carries only what the spec does not: ownership, dependency order, seams, and where each acceptance criterion lands. Leave implementation to the implementer and defer detail to them by default. Re-read cost is a design constraint — detail migrates from *how* to *check*.

**Announce at start:** "I'm using the crucible:writing-plans skill to create the implementation plan."

**Input:** a spec that has closed its own redteam campaign, and any foreign plan brainstorming kept in the feature folder, read beside it for tasks to reuse. Given anything else — a requirements document, an issue — start at `crucible:brainstorming` with it as the input. **Save to** `<feature-folder>/plan.md`, beside the spec, in the folder the resolve step of `skills/redteaming/references/formats.md` § Feature folder finds; that section also names a supersede's successor plan. Commit it where every consuming agent can reach it — parallel worktree agents cannot read gitignored files.

## Plan header

Every plan opens with these sections, each required:

- **Spec pointer** — one line naming the spec path at its pinned revision, and what the pin makes binding, as the opening of `skills/redteaming/references/flip-paths.md` § Flip paths — scoped amendment and supersede states, the umbrella content `skills/brainstorming/references/umbrellas.md` § Children names included. A task calling for a change to the spec's binding content, or for a binding change to an umbrella in the chain (`skills/brainstorming/references/umbrellas.md` § Edits), is a plan defect. Write it as a header line opening with `Spec`, carrying the pin in the backticked form `` `<path>` @ `<rev>` `` (e.g. ``Spec: `docs/crucible/<YYYY-MM-DD>-<feature-slug>/design.md` @ `<rev>` ``). This is the header's only pin, and every seat reads it from here. **Folded form:** in a combined spec+plan document (`crucible:redteaming § The folded lane`), which cannot carry its own revision, the header line reads `Spec: this document`, and seats read the whole document.
- **Goal** — what exists when the plan completes.
- **Task dependency order** — which tasks block which, as the order SDD runs them in.
- **File ownership + overlap census** — every file the plan touches, against exactly one owning task. State the overlaps and how they are ordered, or state that there are none. This section is arithmetic, and the plan phase runs it rather than reading it.
- **Inter-task contracts** — the seams: signatures, formats, and pins one task produces and another consumes, each stated with both sides named. This is how a task's implementer learns what neighboring tasks provide and expect.
- **Acceptance mapping** — each spec acceptance criterion against the task that discharges it, or a stated why-not.

The advisory register — the shape of the solution, the sketch an implementer may replace — lives in the spec's Mechanism sketches, not in the plan.

## Deferring detail

Detail is deferred to implementers by default; the plan pins only binding content and non-local mechanism: cross-task or cross-component contracts, shared formats, orderings or state, and consumers outside the change's own files. Mark any other detail `Deferred to implementation: <what>` on its own line or bullet, in the task that owns it. Name each of the spec's markers, by its site, in the Contract of each task that owns it; one whose call spans several tasks is named in each, each owner making the call for its own sites. Every campaign deferral lands its marker in the artifact under review, and the markers are grep-able, so the plan phase's pre-pass checks mechanically that each has an owning task.

Binding content and non-local mechanism are never deferrable — a deferral covering either is a defect in the plan, and so is a misplaced one: named by a task whose scope it does not touch, or sitting in a task other than one whose scope it falls in. "The detail is missing" is not a defect in a recorded deferral; it is the point of one.

## Per-task structure

Four fields, all required:

- **Why** — one paragraph: the task's role in the design, and the rationale it inherits.
- **Files** — touch list, matching this task's row in the ownership census. Every existing consumer of what the task changes or deletes, found as the consumer sweep finds them (`crucible:brainstorming` § Spec self-review), lands in this list or in the census, or the task is not yet scoped. A task that writes or edits a decision record names the brainstorm decision record (`.crucible/<feature-slug>/brainstorm-decisions.md`) among its inputs, so its implementer attributes, and its task reviewer (for a task completed branch review only, the branch reviewer) checks, each position's basis from its entry's proposer and status.
- **Contract** — interfaces consumed and produced: signatures, not bodies; plus the spec decisions this task enacts, named by their ids, and the spec's deferral markers it owns (§ Deferring detail).
- **Acceptance** — observable behaviors, plus test scenarios by category — happy / edge / error / integration — as scenario descriptions, not test code. The edge and error scenarios name the inputs the spec implies but never names (an empty file, a missing directory, a second run).

**The review mark** is optional and not a field. A task that meets the mark's criterion (`skills/subagent-driven-development/references/seat-rules.md` § The arrangement questions) may carry, on its own line below the task's heading, `Review: branch only — <reason>`, the reason saying how the task meets it; SDD's task loop says how it is reviewed (`crucible:subagent-driven-development` § The Task Loop). A task with no mark is reviewed. A mark is added only before the plan's review closes; after that, the task keeps its review.

## What a plan never contains

Explicitly excluded: function bodies, test code, shell sequences, TDD step scripts, commit messages, per-step checkboxes, and copies of spec content. Writing any of these into a plan is a plan defect, not extra helpfulness — implementation detail in a plan is text a stronger-context implementer must re-read and may wrongly treat as binding, and copied spec text is text that can go stale against the artifact it copies.

## Binding vs advisory

**Binding:** requirements, interfaces, non-goals, acceptance, and everything the header's spec pointer names as binding in the spec; how binding text is read and changed is `skills/redteaming/references/flip-paths.md`, from its opening.

**Advisory:** everything about *how*, and every item marked `Deferred to implementation:`. An implementer may depart from it where the codebase contradicts its assumptions, logging each departure.

Write the plan so the split is visible: mark advisory content as advisory; keep binding sections free of mechanism detail.

## Acceptance maps to checks

Every acceptance criterion maps, in the header's Acceptance mapping section, to one of the two kinds of check below, by name, or states why not — the why-not is written into the plan, never left implicit. Prose-fidelity criteria that only review can judge are legitimate why-nots; an unexamined criterion, or a mapping that names no kind, is not.

- **Standing test** — kept in the suite, where a plausible later change could break the outcome.
- **One-time check** — run once by the implementer, its command and quoted output recorded in the task report for review to read, not re-run. Where it checks a state the change brings about, it is also run before the change and must fail there: that failure shows it can fire.

An absence or removal criterion ("X is gone") is a one-time check unless the plan names the later change that could undo it. Outcomes observed on one run are assertions in one test, not one test each.

## Task sizing

A task is the smallest unit that carries its own test cycle and its own review verdict — a fresh task reviewer's gate, or, for a marked task, the branch reviewer's read of its range — split where a reviewer could reject one task while approving its neighbor; fold setup, configuration, and scaffolding into the task whose deliverable needs them. (Calibration, advisory: a task's Why+Contract+Acceptance around a page; plans in the low-teens of tasks.)

## Self-review

Before the plan phase, re-read the plan once and fix what turns up — the folded lane's combined-document author included, who reaches these formats through `crucible:brainstorming` and runs these checks at its self-review step:

1. **Placeholder scan:** "TBD", "TODO", incomplete sections, vague requirements. A `Deferred to implementation:` marker is exempt.
2. **Header arithmetic:** the ownership census against the tasks' Files rows, the acceptance mapping against the spec's criteria, every named decision id against the spec.
3. **Name consistency:** a type, function or format carries the same name and signature in every task and contract that uses it.
4. **Evidence:** every signature, format and pin stated about existing code was read from the code as it was written, never recalled, or carries `UNVERIFIED`.

The plan phase's mechanical pre-pass stays the independent check, never the first one.

## Exit — review phase, then execution

A finished plan never goes straight to execution:

1. Run the plan's own review phase — invoke `crucible:redteaming`, which runs it (`skills/redteaming/references/plan-phase.md`).
2. On its close, invoke `crucible:subagent-driven-development`, as the close readout states (`crucible:redteaming` § Exit).
