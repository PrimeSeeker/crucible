# Operator steering

## Decision

**Collaborative design, autonomous execution.** The operator's judgment
enters while the design is made, in brainstorming and through the spec
campaign's decision asks. From the plan on, work runs without check-ins
and stops only for a BLOCKED status it cannot resolve, a stop-and-ask
trigger, a decision ask that needs the operator, or completion
(`skills/subagent-driven-development/SKILL.md`, its continuous-execution
rule).

**The analyst stance.** No step requires the operator to read a spec,
plan, code or a diff, none is withheld, and a decision ask may quote the
few lines it turns on. The controller makes technical calls itself and
reports them; design judgments reach the operator as plain-language
decision asks with a recommendation (`crucible:redteaming § Round
readout`). The README states the stance to newcomers (`README.md` § Who
it is for). There is no profile switch: the router's precedence line is
the override.

**The digest gate approves the launch.** At brainstorming's digest gate
the operator reviews the digest (major designs) or the decision record's
decisions, the open asks, and the campaign shape: seats, lenses, models
and expected rounds. Approving the design approves that shape, which the
decision record keeps; the campaign then starts with an announcement
naming any departure, not a pause. The gate shows no token figure
(`crucible:brainstorming § Digest gate`). The digest's format is stated
once (`skills/redteaming/references/formats.md` § Design digest format).

## Why

### Autonomous execution

The design philosophy the maintainer confirmed on 2026-08-06: "A human
checkpoint between tasks is a design defect; safety comes from gates and
review, not attendance." The maintainer's own amendment to that text
records that the plan phase's asks were answered "proceed" more than 95%
of the time in practice (no count is recorded). Upstream's
subagent-driven development already ran tasks without check-ins
(`superpowers/skills/subagent-driven-development/SKILL.md` at v6.2.0);
crucible keeps that and extends it to the plan, which announces its
shape and proceeds (`skills/redteaming/references/plan-phase.md`).
(Basis: judgment, accepted by the maintainer, for the principle; the
maintainer's preference, for the amendment; external, for upstream.)

### Never required, never withheld

The stance began as the maintainer's own way of working: reading agents'
output, not code or diffs. Because human code review is not the
backstop, review has to hold without it, which is why crucible's review
is agentic and evidence-grounded (`docs/decisions/evidence-and-findings.md`).
(Basis: the maintainer's preference, for the way of working; judgment,
accepted by the maintainer, for what review owes it; 2026-08-06.)

On 2026-10-07 the stance became crucible's stated default, as "never
required", not "never shown": that already removes what hurts a reader
who wants to see more, a second mode would double every later route's
paths, and nobody had asked for one. Per-site "overridable" marks went
the same way, since the precedence line already ranks instruction files
and the operator's requests above the skills. (Basis: judgment, accepted
by the maintainer.)

Each decision ask lists every option the findings behind it propose and
states what its change withdraws from an earlier operator approval. That
rule comes from one ask in crucible's own review of its redteaming
rewrite: the ask left out the seats' middle option and did not say that
its fix withdrew relief the operator had approved. The terminal pass
caught it; re-asked, the operator chose the middle option. (Basis: a
single incident, 2026-10-08.)

### One gate for design and launch

The digest replaced the maintainer's habit of mining an intermediate spec
revision for its decisions, trade-offs and omitted but material details.
Upstream's brainstorming has the user review the written spec file
before planning (`superpowers/skills/brainstorming/SKILL.md` at v6.2.0,
its checklist's step 8); crucible's gate asks for decisions instead, and
shows any part of the spec the operator asks for. A separate pause to
approve the campaign launch had been, in the maintainer's words, only a
visibility checkpoint: "I basically never adjusted the shape". (Basis:
the maintainer's preference, 2026-08-06 and 2026-08-07.)

Launch approval moved into the digest gate on 2026-10-07. The only cost
data is the maintainer's runs on one project, so a token range at the
gate would be false precision. The shape has named each seat's model
since 2026-10-09. (Basis: judgment, accepted by the maintainer.) Round
1's alternate-role seat has been named in it since 2026-10-13, at the
maintainer's request for a round-1 replacement of the highest-level
seat (`crucible:redteaming § Panels`). (Basis: the maintainer's
preference.)

## Rejected

- **A human checkpoint between tasks**: a design defect (§ Why).
- **An analyst profile switch**, or per-site "overridable" marks: the
  precedence line already does it (§ Why).
- **A separate approval pause before the campaign**: never used to
  change the shape (§ Why).
- **A token estimate at the gate**: false precision (§ Why). The README's
  comparisons carry token figures as the maintainer's labelled
  impressions; the gate does not (`docs/decisions/publication.md`).

## What a project may change

The operator's instruction files and direct requests outrank the skills
(`skills/using-crucible/SKILL.md`, the precedence line), so an operator
who wants to read and approve every spec or plan says so, and crucible
shows them; nothing is ever withheld.

## Changes

- 2026-10-19: the analyst stance stated openly in the README: reading is
  never required and nothing is withheld.
- 2026-10-13: the digest gate approves the campaign launch, its shape
  naming seats, lenses, models and expected rounds.
- 2026-08-06: collaborative design, autonomous execution.
