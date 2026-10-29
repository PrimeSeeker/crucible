# Plans

## Decision

**What a plan carries.** A plan's readers are strong fresh-context
implementers and reviewers who also read the spec, so it carries only
what the spec does not: ownership, dependency order, seams, and where
each acceptance criterion lands. Detail is deferred to the implementer by
default. Its input is a spec that has closed its own campaign; anything
else starts at brainstorming (`crucible:writing-plans § Overview`).

**The header.** A spec pointer, the header's only pin (`Spec: this
document` where the plan is folded into the spec); the goal; the task
dependency order; a file-ownership and overlap census; the inter-task
contracts; the acceptance mapping; and the deferred-items routing table,
under its own `## Deferred-items routing table` heading, one backticked
row per owning task with `T<N>` alone in the owner cell, assembled from
the `Deferred to implementation:` markers. Each row's closure chain is the
owning implementer's Decision Log entry, that task's review (for a task
completed branch review only, the controller's presence check and then
the branch reviewer) and the branch review's sweep. There is no
test-namespace allocation and no parallelizable tier
(`crucible:writing-plans § Plan header`;
`crucible:writing-plans § Deferring detail`).

**Four task fields.** Why, Files, Contract and Acceptance, all required,
and no per-task constraints field. Files enumerates, by search, the
consumers of everything the task changes; Contract gives signatures, not
bodies, and names the spec decisions the task enacts by id. A plan never
contains function bodies, test code, shell sequences, TDD step scripts,
commit messages, per-step checkboxes or copies of spec content
(`crucible:writing-plans § Per-task structure — four fields, all
required`; `crucible:writing-plans § What a plan never contains`). Each
acceptance criterion maps to a kind of check or says why neither applies
(`docs/decisions/test-rules.md`). Its edge and error scenarios name the
inputs the spec implies but never names.

**The review mark.** A task that meets the mark's criterion, defined in
`skills/subagent-driven-development/references/premise-and-questions.md`
§ The arrangement questions, may carry the line `Review: branch only —
<reason>`, the reason saying how it meets it; a task with no mark is
reviewed. Dispatched, a marked task takes the branch review as its first
review (`docs/decisions/task-loop.md`). Marks are plan content: the
review that grades the plan grades them, the plan phase's coherence
seats or, on the folded preset, the spec campaign's seats, and that
phase's close readout lists the marked tasks for the operator as
information. Marking a task that has not run after that review has
closed is a downshift from the arrangement the operator confirmed: never
a contained amendment, it goes to the operator as a decision ask
(`skills/redteaming/references/flip-paths.md` § The containment test;
`crucible:writing-plans § Per-task structure — four fields, all
required`).

**Task sizing.** A task is the smallest unit with its own test cycle and
its own review verdict, a fresh task reviewer's gate or, for a marked
task, the branch reviewer's judgments over its range: split where a
reviewer could reject one task while approving its neighbour, and fold
setup into the task that needs it. The calibration, about a page per
task and plans in the low
teens of tasks, is advisory (`crucible:writing-plans § Task sizing`).

**Self-review.** The author re-reads the plan once before the plan phase:
a placeholder scan, the header's arithmetic, name consistency, and
evidence for every claim about existing code. The plan phase's pre-pass
stays the independent check (`crucible:writing-plans § Self-review`).

**The plan phase.** A plan gets one verification round and never a loop:
a mechanical pre-pass whose report carries the seat id `p0` and whose
arithmetic is run rather than read, one coherence seat reading spec and
plan together (two for a large plan), one merged fix wave, the blind
verifier and the plan phase's terminal pass
(`docs/decisions/terminal-pass.md`). After a not-landed verdict or a
terminal-pass finding, one scoped repair; anything still open goes to the
operator as a decision ask, and a finding that shows the spec wrong takes
the flip path against the spec. A correction to the spec that the
containment test finds contained lands in the phase's own fix wave, as a
`Contained amendment:` item of its fix list naming the binding item and
the change, and is named in its readout as a technical call
(`docs/decisions/the-spec.md`). Its reason, and why it is contained, go
in the ruling of the merged entry that led to it, never in the item: the
fix list is the blind verifier's input. The verifier verdicts the item
from its plan-side hunks, the re-pin and any plan patch, and the
controller confirms that the amendment commit landed. The shape is
announced and the phase proceeds, with no approval gate. It is called the
plan phase, never a campaign; its directory `campaigns/plan/` and
argument value `plan` keep their names. At close the controller seeds
SDD's ledger from the routing table, with each contained amendment as
one of its own rulings, the item and its reason together, which SDD's
setup copies there if the ledger lacks it, and with each premise finding
still open as open (`docs/decisions/evidence-and-findings.md`), and
hands off to execution (`skills/redteaming/references/plan-phase.md`).

## Why

### A lean contract

Upstream's writing-plans writes for an engineer with "zero context for
our codebase and questionable taste": every task is bite-sized steps of
two to five minutes, each with its code, test code, commands and commit
(`superpowers/skills/writing-plans/SKILL.md`). Crucible writes for strong
models that read the spec themselves, and implementation detail in a plan
is text such an implementer must re-read and may wrongly treat as
binding. The four fields and the exclusions follow a proposal in
upstream's own tracker, filed 2026-03-23: Why, Files, Contract and
Acceptance, plus a Constraints field, with function bodies, test code,
shell commands, TDD step sequences and commit messages left out
(https://github.com/obra/superpowers/issues/895). The design merged it
with the plan skill of Compound Engineering's plugin, `ce-plan`
(https://github.com/EveryInc/compound-engineering-plugin), whose units
list test scenarios by category, happy path, edge cases, error and
failure paths, and integration, and whose plans leave out implementation
code, commit messages and red-green-refactor micro-steps (the skill's
plan-structure reference, as read on 2026-10-20); the Acceptance field's
scenario categories are that skill's. Crucible adopted the merged format
at its first design (2026-08-05). In "From Plan to Action: How Well Do
Agents Follow the Plan?", a study of SWE-agent trajectories under several plan
variants, a subpar plan hurt performance more than no plan, and inserting
additional task-relevant phases early could degrade it
(https://arxiv.org/abs/2604.12147). (Basis: external; judgment, accepted
by the maintainer.)

The Constraints field went on 2026-08-17 with the rest of carriage, the
binding content being read from the spec at its pin
(`docs/decisions/the-spec.md`). On 2026-10-07 the header lost its
test-namespace allocation and parallelizable tiers, which served a mode of
parallel implementers that SDD forbids, since implementers share the tree;
the inter-task contracts stayed, because redteaming lands non-local fixes
there (`crucible:redteaming § Merge and finding hygiene`). On 2026-10-11,
with the brief extractor deleted, the rules that existed only for it went
too, a single accepted shape and a fail-closed rule against rival pins;
what readers find things by stayed: the routing table's heading, its row
format, one owner per row and the folded pointer. (Basis: judgment,
accepted by the maintainer.)

The edge and error scenarios name the inputs a spec implies but never
names, after the Review Focus section of upstream's writing-plans
(v6.4.1): those are the inputs no task tests unless a plan names them,
and the reviewers grade a failure on one by its effect on a reasonable
person (`docs/decisions/evidence-and-findings.md`). (Basis: external;
judgment, accepted by the maintainer, 2026-10-27.)

### Task sizing

The sizing rule is upstream's (`superpowers/skills/writing-plans/SKILL.md`,
its Task Right-Sizing section). Crucible's first design (2026-08-06) added
the calibration, advisory like that design's other numeric calibrations;
no measurement stands behind the numbers. (Basis: external, for the rule;
judgment, accepted by the maintainer, for the calibration.)

### The review mark

Per-task review is one of the choices the maintainer asked to separate
from the route (2026-10-28; `docs/decisions/routes.md`), and the plan is
where the tasks exist to choose it for. A mark carries its reason so the
seats grading the plan can judge it, and the criterion asks what a late
review would cost: the branch review runs after every later task, too
late for a detail something else builds on. Marks written at plan time
pass that review; a mark added later changes a reviewed plan, so it is
the operator's to confirm, a deliberate asymmetry. (Basis: the
maintainer's preference, for the choice; judgment, accepted by the
maintainer, for the mark, its grading and the downshift rule,
2026-10-29.)

### Self-review

Upstream's plan author runs a self-review: spec coverage, a placeholder
scan, type consistency (`superpowers/skills/writing-plans/SKILL.md`). The
port dropped it, and it returned on 2026-10-07 with crucible's own checks.
The evidence check is the plan author's share of the author-side evidence
rules (`docs/decisions/evidence-and-findings.md`). (Basis: external;
judgment, accepted by the maintainer.)

### One round for the plan

Until 2026-08-17 a plan got its own multi-round campaign, and in the
campaign on crucible's dual-runtime plan most late findings were caused by
the campaign's own edits (`docs/decisions/the-spec.md`). With carriage
retired, the design content that justified a plan campaign sits in the
spec, where the spec campaign reviews it. What remains in a plan is
mechanically checkable, which the pre-pass runs; caught downstream by
execution; or visible to a pass after the fix wave. The one plan terminal
pass then on record had caught a MAJOR that the campaign's own last fix
wave had just introduced, which no earlier round could have seen, and the
maintainer confirmed adding the closing pass during that design's
campaign. (Basis: measured; judgment, accepted by the maintainer.)

The plan phase called a finding that shows the spec's premise wrong
"structural", while the containment test calls a change structural when
it redefines a mechanism, and sends it to a supersede; on 2026-10-28 the
phase's wording became a finding that shows the spec wrong, leaving one
sense. A contained amendment the phase makes is seeded into the ledger
because the branch review and the close readout find the controller's
rulings only there, as they find execution's. (Basis: judgment, accepted
by the maintainer.)

As first written, a `Contained amendment:` item carried its reason,
which the blind verifier must never see, and named a spec change that
lands outside the verifier's diff and read scope; a probe of past
reviews found it on 2026-10-28. The reason moved to the merged entry's
ruling and travels with the item into the ledger, so the ruling still
says what changed and why, and the verifier checks only what its diff
holds. An agent's proposal, which the maintainer accepted. (Basis:
measured, by the probe; judgment, accepted by the maintainer.)

The maintainer's amendment to the design philosophy (2026-08-06): the
spec phase expects steering, while the plan phase is autonomous by
default, the maintainer reporting over 95% "proceed" in practice. When the
spec campaign's launch approval moved into the digest gate (2026-10-07),
the plan phase kept proceeding without one. (Basis: the maintainer's
preference.)

On 2026-10-09 "campaign" came to name the spec's review only. The
directory and the argument value are interfaces that records and
`skills/redteaming/scripts/conserve.py` read, so they kept their names.
(Basis: judgment, accepted by the maintainer.)

## Rejected

- **Code in plans**: bodies, test code, shell sequences, TDD step scripts,
  commit messages (§ Why).
- **A multi-round plan campaign** (§ Why).
- **An approval gate before the plan phase** (§ Why).
- **Parallelizable tiers and test-namespace allocation** (§ Why).

## Changes

- 2026-10-29: a task may carry `Review: branch only — <reason>` where it
  meets the mark's criterion, graded as plan content and listed at the
  close of the phase that reviews the plan; marking an unrun task later
  is the operator's call; task sizing and the routed items' closure
  chain name the branch reviewer for a marked task; per-task review made
  a plan choice at the maintainer's request.
- 2026-10-29: a `Contained amendment:` item names the binding item and
  the change, its reason going to the merged entry's ruling and beside
  the item in the ledger, and the verifier verdicts it from the plan's
  hunks, since a probe found the reason reaching the blind verifier and
  the spec change outside its diff; the plan phase's close seeds open
  premise asks into the ledger, so execution carries them until ruled.
- 2026-10-28: the plan phase: a finding that shows the spec wrong takes
  the flip path, and a contained amendment lands in the phase's fix
  list, is named in its readout and is seeded into the ledger at close.
- 2026-10-27: a task's edge and error scenarios name the inputs the
  spec implies but never names, after upstream's Review Focus (v7.0.1
  review): those are the inputs no one else will think to test.
- 2026-10-15: the lean plan contract: a header whose spec pointer is the
  only pin, four task fields with no constraints field, the excluded
  content, the routing table's heading and row format, acceptance mapped
  to a kind of check, and the author's self-review.
- 2026-10-09: the plan phase: one verification round with a `p0`
  pre-pass, coherence seats, one fix wave, the blind verifier and a
  terminal pass, one scoped repair per path, no approval gate and no loop.
- 2026-08-06: task sizing by a reviewer's gate, with an advisory
  calibration of about a page per task and plans in the low teens of
  tasks.
