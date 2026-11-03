---
name: writing-plans
description: Use when a spec has closed its redteam campaign and needs an implementation plan, before touching code.
---

# Writing Plans

## Overview

A plan coordinates agents: strong fresh-context implementers and reviewers, each seeing one task. Each also reads the spec, so the plan never re-tells it and carries only what the spec does not: ownership, dependency order, seams, and where each acceptance criterion lands. Leave implementation to the implementer, deferring detail by default. Re-read cost is a design constraint: detail migrates from *how* to *check*.

**Input:** a spec that has closed its redteam campaign, plus any foreign plan brainstorming kept in the feature folder, read beside it for tasks to reuse. Given anything else (a requirements document, an issue), start at `crucible:brainstorming` with it as input.

Save to `<feature-folder>/plan.md` beside the spec, in the folder `skills/redteaming/references/formats.md` § Feature folder resolves; that section also names a supersede's successor plan. Commit it where every consuming agent can reach it: parallel worktree agents cannot read gitignored files.

## Plan header

Every plan opens with these sections, each required:

- **Spec pointer** — one header line naming the pinned spec, ``Spec: `<path>` @ `<rev>` `` (e.g. ``Spec: `docs/crucible/<YYYY-MM-DD>-<feature-slug>/design.md` @ `<rev>` ``), and what the pin makes binding (`skills/subagent-driven-development/references/review-terms.md` § What binds in a spec). It is the header's only pin; every seat reads it here. A task calling for a change to the spec's binding content, or for a binding change to an umbrella in the chain (`skills/brainstorming/references/umbrella-children.md` § Edits), is a plan defect. In a combined spec+plan document (`crucible:redteaming` § The folded lane) the line reads `Spec: this document`, and seats read the whole document.
- **Goal** — what exists when the plan completes.
- **Task dependency order** — which tasks block which: the order SDD runs them in.
- **File ownership + overlap census** — every file the plan touches against exactly one owning task. State the overlaps and how they are ordered, or that there are none. The plan phase recomputes it.
- **Inter-task contracts** — the seams: signatures, formats and pins one task produces and another consumes, each with both sides named: how an implementer learns what neighboring tasks provide and expect.
- **Acceptance mapping** — each spec acceptance criterion against the task that discharges it, or a stated why-not.

The advisory register (the solution's shape, sketches an implementer may replace) lives in the spec's Mechanism sketches, not in the plan.

## Deferring detail

The plan pins only binding content and non-local mechanism: cross-task or cross-component contracts, shared formats, orderings or state, and consumers outside the change's own files. Mark any other detail `Deferred to implementation: <what>` on its own line or bullet, in the task that owns it.

Name each spec `Deferred to implementation:` marker, by its site, in the Contract of each task owning it; a marker whose call spans several tasks is named in each, each owner making the call for its own sites. Every campaign deferral lands a grep-able marker in the artifact under review, so the plan phase's pre-pass checks mechanically that each has an owning task.

Binding content and non-local mechanism are never deferrable: a deferral covering either is a plan defect, and so is a misplaced one, named by a task whose scope it does not touch, or sitting in one whose scope it does not fall in. Missing detail is no defect in a recorded deferral; it is the point of one.

- **Binding:** requirements, interfaces, non-goals, acceptance, and everything the spec pointer names as binding, read as `skills/subagent-driven-development/references/review-terms.md` § What binds in a spec states; how it changes: `skills/redteaming/references/flip-paths.md`.
- **Advisory:** everything about *how*, and every item marked `Deferred to implementation:`. An implementer may depart from it where the codebase contradicts its assumptions, logging each departure.

Keep the split visible: mark advisory content as advisory; keep binding sections free of mechanism detail.

## Per-task structure

Four fields, all required:

- **Why** — one paragraph: the task's role in the design and the rationale it inherits.
- **Files** — the touch list, matching this task's census row. Every existing consumer of what the task changes or deletes, as the consumer sweep (`crucible:brainstorming` § Spec self-review) finds them, lands here or in the census, or the task is not yet scoped. A task writing or editing a decision record names `.crucible/<feature-slug>/brainstorm-decisions.md` among its inputs; its implementer attributes, and its task reviewer (or the branch reviewer, for a marked task without one) checks, each position's basis from its entry's proposer and status.
- **Contract** — interfaces consumed and produced as signatures, not bodies; the spec decisions enacted, by id; the spec deferral markers owned (§ Deferring detail).
- **Acceptance** — observable behaviors, plus test scenarios by category (happy / edge / error / integration) as descriptions, not test code. Edge and error scenarios name the inputs the spec implies but never names (an empty file, a missing directory, a second run).

**The review mark** is optional and not a field. A task meeting `skills/subagent-driven-development/references/review-terms.md` § The mark's criterion may carry `Review: branch only — <reason>` on its own line below its heading, the reason saying how it meets the criterion; `crucible:subagent-driven-development` § The Task Loop says how it is reviewed. An unmarked task gets a task review. A mark is added only before the plan's review closes.

## What a plan never contains

Function bodies, test code, shell sequences, TDD step scripts, commit messages, per-step checkboxes, copies of spec content: writing any is a plan defect.

## Acceptance maps to checks

In the header's Acceptance mapping, every acceptance criterion maps to one of the two kinds of check below, naming which, or the plan states why not. Prose-fidelity criteria only review can judge are legitimate why-nots; an unexamined criterion, or a mapping naming no kind, is not.

- **Standing test** — kept in the suite, where a plausible later change could break the outcome.
- **One-time check** — run once by the implementer, its command and quoted output recorded in the task report for review to read, not re-run. Where it checks a state the change brings about, it also runs before the change and must fail there, showing it can fire.

An absence or removal criterion ("X is gone") is a one-time check unless the plan names the later change that could undo it. Outcomes observed on one run are assertions in one test, not one test each.

## Task sizing

A task is the smallest unit with its own test cycle and review verdict (a fresh task reviewer's gate; for a marked task, the branch reviewer's read of its range). Split where a reviewer could reject one task and approve its neighbor; fold setup, configuration and scaffolding into the task whose deliverable needs them. Calibration, advisory: split a task whose census row is far above its neighbors' in the number and size of the files it edits, or say why not in its Why; plans in the low teens of tasks.

## Self-review

Before the plan phase, re-read the plan once and fix what turns up, so the phase's mechanical pre-pass stays the independent check, never the first one. The folded lane's combined-document author runs these checks too, at its self-review step in `crucible:brainstorming`.

1. Placeholder scan: TBD, TODO, incomplete sections, vague requirements; a `Deferred to implementation:` marker is exempt.
2. Header arithmetic: the census against the tasks' Files rows, the acceptance mapping against the spec's criteria, every named decision id against the spec.
3. Name consistency: a type, function or format carries the same name and signature in every task and contract using it.
4. Evidence: every signature, format and pin stated about existing code was read from the code as it stands, never recalled, or carries `UNVERIFIED`.

## Exit

A finished plan never goes straight to execution: invoke `crucible:redteaming` to run the plan's review phase; on its close, invoke `crucible:subagent-driven-development`, as the close readout states (`crucible:redteaming` § Exit).
