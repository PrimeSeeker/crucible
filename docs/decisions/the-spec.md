# The spec

## Decision

**Decision weights.** A [LOAD-BEARING] mark binds exactly the sentence or
bullet it annotates, and the Constraints & invariants section binds by
construction; everything else is lightly held, and downstream work may
flip it with a logged rationale (`crucible:brainstorming § Spec
contract`).

**Flip paths.** From the spec campaign's close on, binding content found
wrong changes only through a scoped amendment (contained blast radius;
no new campaign or plan phase) or a supersede (a successor with its own
review), each opened by a decision ask; a ruling that patches the plan
mid-execution needs no ask. The procedure is stated once, in
`skills/redteaming/references/flip-paths.md`.

**Requirements by pointer.** The converged spec is a shared input every
downstream agent reads for itself; isolation covers the campaign's
exhaust, never the spec. Nothing is copied into plans or briefs: a
task-loop seat is given the plan's path and its task number
(`crucible:subagent-driven-development § The Task Loop`), a task the
controller implements inline is reviewed with the same pointer, and the
plan header's spec pointer is the only pin. A task-loop review names the
amendment and ruling commits in its range, and any other change there to
the plan, a folded document or the spec is a scope finding. The branch
review reads the spec at its pinned revision and the plan.

**Intent-weighted content.** Mechanism sketches are advisory. A spec
pins what binds or crosses tasks and defers local mechanism to the
implementer at any severity; non-local mechanism, binding and cross-task
content are never deferred. Fixes land at the altitude of the text around
them, and the spec states the current design only. Seats grade sketches
only for contradiction or infeasibility, and raise missing detail only
when it is non-local (`crucible:redteaming § Merge and finding hygiene`;
`crucible:redteaming § Fix application and blind verification`).

**Restated rules are interfaces.** A rule stated in several places has
every stating site as a consumer: brainstorming's consumer sweep and a
plan task's Files field enumerate them, and a fix report names the
sibling instances of its defect (`crucible:brainstorming § Spec
self-review`, check 5).

## Why

### Weights and flip paths

The maintainer's amendment to the design philosophy of 2026-08-06: a
design does not freeze at plan acceptance. A spec carries many lightly held
positions that downstream work is expected to flip, while a load-bearing
decision either holds or goes through an explicit event, "never a quiet
in-flight rewrite". The scoped amendment, for a contained flip with no
new campaign, was adopted on 2026-08-07, and on 2026-08-22 the maintainer
ruled that the bar binds only from the campaign's close: during its own
campaign the spec is the artifact under review. The procedure moved to
one shared reference on 2026-10-13, after its two copies in redteaming
and SDD had drifted apart; the maintainer chose that option. (Basis: the
maintainer's preference.)

Downstream, an implementer may depart from what is lightly held, logging
each departure, but one who finds binding content wrong reports BLOCKED
and never improvises around it
(`skills/subagent-driven-development/implementer-prompt.md` § Binding vs
Advisory: the Deviation License). (Basis: judgment, accepted by the
maintainer, 2026-08-05.)

### Pointers, not copies

Copying spec content into the plan and then into every task brief made
the copy the reviewed object. Measured on crucible's own dual-runtime
spec and plan campaigns (2026-08): the share of findings caused by
earlier rounds' own edits rose rather than fell (plan campaign, by round:
17, 53, 80, 87 and 83%), a recurring finding was "X is uncarried, inline
it", and 35 test functions over 1,147 lines existed only to check the
copying. Isolation was the reason for copying, yet all four recorded
cases of a seat seeing what it should not were campaign exhaust, none the
spec; the blind fix verifier stays the one seat kept from the spec.
Carriage retired on 2026-08-17. On 2026-10-11 the brief extractor
went too: a 649-line script that parsed agent-written plan markdown and
grew its rules one misread input shape at a time, for a seat that can
read one section of a plan itself. (Basis: measured.)

### Intent at the spec's altitude

Agents read literally, so what binds must be explicit and everything
else visibly advisory (the design philosophy of 2026-08-06; judgment,
accepted by the maintainer). Measured over four large spec campaigns crucible
ran on one project (2026-09-27): Decisions sections grew 2.8 to 5.4 times
across a campaign and bare numbers about 3.5 to 4.2 times, rounds 4 and 5
still produced blockers, and in the three campaigns instrumented for it,
60 to 90% of the findings from round 2 on were introduced by earlier fix
waves. That fits fixes landing below the altitude of the text around
them and carrying their mechanism in, which the rule then in force made
necessary by forbidding the deferral of any blocker or major finding.
(Basis: measured.)

### Restated rules

In a 2026-08-27 classification of about 1,620 findings from 24 campaign
records, fix waves that failed to land were dominated by a correct fix
applied at one site while sibling statements of the same content stood
unedited; an unenumerated consumer is one of the two largest finding
classes `crucible:brainstorming § Spec self-review` names. Treating every
restating site as a consumer puts those siblings in the sweep. (Basis:
measured.)

## Rejected

- **Carriage**: copying the spec's [LOAD-BEARING] decisions into a plan's
  global constraints and per-task constraints fields, and extracting a
  brief per task (§ Why).
- **Plan revisions stamped into dispatches**: the plan header's spec
  pointer is the only pin; seats read the live plan, and the commits that
  patched it are named instead.
- **Deferral bounded to minor findings**: it forced blockers and majors
  to land their mechanism in the spec (§ Why).
- **Annotating a fix in the spec** with finding citations or changelog
  prose: what changed and why lives in the round records.

## Changes

- 2026-10-13: flip paths: the scoped amendment and the supersede, stated
  once in a shared reference.
- 2026-10-11: requirements by pointer: the plan's path and task number,
  with no brief extracted.
- 2026-10-01: a rule restated in several places is an interface whose
  consumers are its restating sites.
- 2026-09-27: intent-weighted content: local mechanism deferred at any
  severity, fixes at the text's own altitude.
- 2026-08-06: decision weights: [LOAD-BEARING] marks bind, everything
  else is lightly held.
