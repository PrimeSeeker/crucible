---
name: writing-plans
description: Use when a spec has closed its redteam campaign and needs an implementation plan, before touching code.
---

# Writing Plans

## Overview

A plan is an agent coordination artifact. Its readers are strong fresh-context implementers and reviewers who each see one task — and each of them also reads the spec, which is a shared input, not something the plan re-tells. So the plan carries only what the spec does not: ownership, dependency order, seams, and where each acceptance criterion lands. Leave implementation to the implementer and defer detail to them by default. Re-read cost is a design constraint — detail migrates from *how* to *check*.

**Announce at start:** "I'm using the crucible:writing-plans skill to create the implementation plan."

**Input:** a spec that has closed its own redteam campaign, and any foreign plan brainstorming kept in the feature folder, read beside it for tasks to reuse. Given anything else — a requirements document, an issue — start at `crucible:brainstorming` with it as the input. **Save to** `<feature-folder>/plan.md`, beside the spec in the feature's feature folder — the folder brainstorming created, found by the resolve step of `skills/redteaming/references/formats.md` § Feature folder, which creates nothing (a successor plan under supersede takes the next numeric suffix, `<feature-folder>/plan-2.md`, …; layout in the same section). Commit it where every consuming agent can reach it — parallel worktree agents cannot read gitignored files.

## Plan header

Every plan opens with these sections, each required:

- **Spec pointer** — one line naming the spec path at its pinned revision, and what the pin makes binding: the spec's **Constraints & invariants**, its **[LOAD-BEARING]** marks, and any preamble convention the spec declares binding; and, where the spec's preamble carries an `Umbrella:` line, this feature's own entry in that umbrella and the umbrella's Constraints & invariants and [LOAD-BEARING] marks, up the chain through each umbrella's own line, which each seat reads in its worktree. A task calling for a change to those Constraints or marks, or to the entry other than a clarification the spec states that changes nothing another entry waits on, is a plan defect. Write it as a header line opening with `Spec`, carrying the pin in the backticked form `` `<path>` @ `<rev>` `` (e.g. ``Spec: `docs/crucible/<YYYY-MM-DD>-<feature-slug>/design.md` @ `<rev>` ``) — the backticks make the pin unambiguous in a prose line. This is the header's only pin, and every seat reads it from here. **Folded form:** where a small change has folded its plan into its spec — one combined spec+plan document and no separate plan file (`crucible:redteaming § The folded lane`) — a file cannot carry its own revision, so the header line reads `Spec: this document`, and seats read the whole document. Point, never copy: a block of spec text reproduced in the plan is a plan defect, because the copy and the spec drift and no reader knows which binds.
- **Goal** — what exists when the plan completes.
- **Task dependency order** — which tasks block which, as the order SDD runs them in.
- **File ownership + overlap census** — every file the plan touches, against exactly one owning task. State the overlaps and how they are ordered, or state that there are none. This section is arithmetic, and the plan phase runs it rather than reading it.
- **Inter-task contracts** — the seams: signatures, formats, and pins one task produces and another consumes, each stated with both sides named. This is how a task's implementer learns what neighboring tasks provide and expect.
- **Acceptance mapping** — each spec acceptance criterion against the task that discharges it, or a stated why-not.
- **Deferred-items routing table** — under its own heading, `## Deferred-items routing table`, where every seat looks for it. Every deferred item, one row per owning task, in this binding format:

  `| id | source (spec or plan site) | one-line intent | owning task |`

  The owning-task cell carries the canonical form `T<N>` and nothing else — each seat finds its task's rows by it. Assemble the table from the `Deferred to implementation:` markers alone — the spec's and the plan's own — each row's source cell naming the spec or plan site its marker sits at. Every campaign deferral lands its marker in the artifact under review, so the markers are the whole input. From plan time on, an empty owner cell is a defect: assigning owners is what plan time is for.

The advisory register — the shape of the solution, the sketch an implementer may replace — lives in the spec's Mechanism sketches, not in the plan.

## Deferring detail

Detail is deferred to implementers by default; the plan pins only what is binding or crosses tasks. Mark any non-binding detail `Deferred to implementation: <what>` on its own line or bullet — the marker is grep-able, which is what lets the routing table be assembled mechanically rather than remembered.

Every marker earns its routing-table rows (§ Plan header), and each row is the item's closure chain for its owning task: the implementer records the call in their Decision Log, the task's reviewer checks it, and anything still open is swept at branch review.

Binding or cross-task content is never deferrable — a deferral covering it is a defect in the plan, and so is a deferral whose content sits in a section the routing table would hand to the wrong owner. "The detail is missing" is not a defect in a recorded deferral; it is the point of one.

## Per-task structure — four fields, all required

- **Why** — one paragraph: the task's role in the design, and the rationale it inherits.
- **Files** — touch list, matching this task's row in the ownership census. Enumerate the existing consumers of every symbol, file, or interface the task changes or deletes — mechanically, by search, not from memory — and account for each: it lands in this list or in the census, or the task is not yet scoped. A rule stated in more than one place — docs, prompts, templates — is such an interface, and every site that states it is a consumer.
- **Contract** — interfaces consumed and produced: signatures, not bodies; plus the spec decisions this task enacts, named by their ids. Naming is the mechanism — a task never quotes the spec's binding text.
- **Acceptance** — observable behaviors, plus test scenarios by category — happy / edge / error / integration — as scenario descriptions, not test code. The edge and error scenarios name the inputs the spec implies but never names (an empty file, a missing directory, a second run).

There is no per-task constraints field. Every seat reads the header's spec pointer, so a task's binding content is read from the spec at its pinned revision; a per-task restatement would be a second copy to keep true.

## What a plan never contains

Explicitly excluded: function bodies, test code, shell sequences, TDD step scripts, commit messages, per-step checkboxes, and copies of spec content. Writing any of these into a plan is a plan defect, not extra helpfulness — implementation detail in a plan is text a stronger-context implementer must re-read and may wrongly treat as binding, and copied spec text is text that can go stale against the artifact it copies.

## Binding vs advisory

**Binding:** requirements, interfaces, non-goals, acceptance, the routing table's rows, and everything the header's spec pointer names as binding in the spec. An implementer who cannot implement binding content stops and escalates (BLOCKED) — changing or contradicting it is never theirs to improvise.

**Advisory:** everything about *how*, and every item marked `Deferred to implementation:`. Implementers may deviate from advisory content when the codebase contradicts its assumptions, logging every deviation in their Decision Log.

Write the plan so the split is visible: mark advisory content as advisory; keep binding sections free of mechanism detail.

## Acceptance maps to checks

Every acceptance criterion maps, in the header's Acceptance mapping section, to one of the two kinds of check below, by name, or states why not — the why-not is written into the plan, never left implicit. Prose-fidelity criteria that only review can judge are legitimate why-nots; an unexamined criterion, or a mapping that names no kind, is not.

- **Standing test** — kept in the suite, where a plausible later change could break the outcome.
- **One-time check** — run once by the implementer, its command and quoted output recorded in the task report for review to read, not re-run. Where it checks a state the change brings about, it is also run before the change and must fail there: that failure shows it can fire.

An absence or removal criterion ("X is gone") is a one-time check unless the plan names the later change that could undo it. Outcomes observed on one run are assertions in one test, not one test each.

## Task sizing

A task is the smallest unit that carries its own test cycle and is worth a fresh reviewer's gate — split where a reviewer could reject one task while approving its neighbor; fold setup, configuration, and scaffolding into the task whose deliverable needs them. (Calibration, advisory: a task's Why+Contract+Acceptance around a page; plans in the low-teens of tasks.)

## Self-review

Before the plan phase, re-read the plan once and fix what turns up — the folded lane's combined-document author included, who reaches these formats through `crucible:brainstorming` and runs these checks at its self-review step:

1. **Placeholder scan:** "TBD", "TODO", incomplete sections, vague requirements. A `Deferred to implementation:` marker is exempt.
2. **Header arithmetic:** the ownership census against the tasks' Files rows, the acceptance mapping against the spec's criteria, every named decision id against the spec.
3. **Name consistency:** a type, function or format carries the same name and signature in every task and contract that uses it.
4. **Evidence:** every signature, format and pin stated about existing code was read from the code as it was written, never recalled, or carries `UNVERIFIED`.

The plan phase's mechanical pre-pass stays the independent check, never the first one.

## Exit — review phase, then execution

A finished plan never goes straight to execution:

1. Run the plan's own review phase — invoke `crucible:redteaming`, which runs it as a single verification round. Announce its shape (seats, lenses, dispatch count) in the phase-start readout and proceed; the announcement is not an approval gate.
2. On close, the phase hands off to SDD execution — invoke `crucible:subagent-driven-development`. The handoff is the controller's explicit move, stated in the close readout.
