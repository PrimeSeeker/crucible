# Adjudication

## Decision

**One dispute rule on every SDD route.** A finding is fixed or disputed,
never dropped. The implementer answers a finding it disputes NOT
CONFIRMED, with evidence, and edits nothing for it. Disputes go in
batches, one wave's NOT CONFIRMED findings or the controller's own
disputes raised together, to one fresh adjudicator seat, at any wave, on
the standard route, the folded lane and the very-small lane, in the task
loop and the branch review. The seat builds the diff of each finding's
review range itself and rules each finding UPHELD or DISMISSED with a
ruling. An upheld finding re-enters the loop and cannot be disputed again;
one upheld at the task-loop cap goes to the breaker. A dismissed finding
is closed by its ruling. Every outcome is written under the ledger's
`## Adjudication rulings`. A ruling the adjudicator marks as touching
binding content, what binds in the spec or its umbrellas
(`docs/decisions/the-spec.md`), passes the containment test before the
controller acts on it: a contained one the controller records as its own
ruling, and any other goes to the operator as a decision ask, the
finding open until the answer; on the very-small lane, one changing the
note's binding parts is the operator's. Adjudication adds no wave; a wave whose fix
dispatch only disputes is still a wave. Every dismissed or parked BLOCKER
or MAJOR reaches the operator with its ruling in the close readout, and
so does every ruling the controller made itself, with its reason. The
adjudicator runs on the default role
(`docs/decisions/model-roles-and-effort.md`;
`crucible:subagent-driven-development § Rules every route shares`).

**What the controller rules on.** Two kinds only: a plan-conflict finding
on a diff it did not write (is the plan or the work wrong?), and the
breaker's consequence rulings at the task-loop cap. A reviewer's finding
that a binding item's literal reading reaches a case its author did not
consider is such a plan conflict. A plan conflict that is a design judgment
goes to the operator as a decision ask instead, and a ruling of the
controller's that touches binding content passes the containment test,
one it does not find contained going to the operator as a decision ask
(`skills/redteaming/references/flip-paths.md` § The containment test).
The contained amendments the controller confirms, the plan phase's
included, are among its rulings in the ledger and the close readout. Everything else contested goes to the
adjudicator: an implementer's NOT CONFIRMED, a finding the controller
judges wrong, at the cap included, and any plan-conflict finding or park
ruling on a diff the controller wrote (inline mode, the very-small lane).
A finding that both fails a verdict and conflicts with plan text is ruled
first as a plan conflict; if the plan stands, the verdict failure enters
the loop. The pre-flight scan before Task 1, which has no diff yet, is
ruled on by the controller as plan conflicts. In the branch review the
controller never parks a BLOCKER or MAJOR on its own ruling.

**Outside the loops.** The standalone branch review is not an SDD route:
the invoking agent handles its findings, and a disagreement that survives
its evidence goes to the operator (`crucible:receiving-review § Who
rules`).

## Why

### Upstream's rule and the first port

Upstream's controller adjudicates open findings itself, and only at the
breaker: "Adjudicate only at the cap. Adjudicating earlier to end a loop
is pre-judging with a different name." A finding that conflicts with plan
text is put to the human, and so is the pre-flight scan's batch of
conflicts (`superpowers/skills/subagent-driven-development/SKILL.md`).
Crucible's first design (2026-08-06) made plan conflicts the controller's
authority, since no step requires the operator to read a plan or code
(`docs/decisions/operator-steering.md`), with two guards: every rejected
BLOCKER or MAJOR stays visible to the operator with its ruling, and no
self-adjudication, a fresh adjudicator seat ruling on findings against a
diff the controller wrote. Ending a fix loop by adjudication stayed
cap-gated. (Basis: external; judgment, accepted by the maintainer.)

### Disputes at any wave

With disputes heard only at the breaker, a wrong finding cost up to five
waves or landed as an edit made only to comply, while the very-small lane
had sent a contested finding to a fresh adjudicator at any wave since
2026-09-27. On 2026-10-07 that became the rule on every route, replacing
inline mode's guard and the lane's own rule, and the maintainer asked for
it to be part of that feature. An upheld finding cannot come back as a
dispute, and adjudication adds no wave, so the caps of five waves per task
and three per branch still terminate the loops. (Basis: judgment, accepted
by the maintainer.)

### Who rules

The controller holds the plan and the cross-task context a reviewer
lacks, which is why the plan-conflict ruling on others' work stays with
it; on its own diff it would be grading itself. The adjudicator runs on
the default role because its dismissals close findings without further
review. Rulings go to the ledger so a resumed controller rebuilds the open
set from it, and to the close readout so a ruling is never the last
anyone hears of a finding. (Basis: judgment, accepted by the maintainer,
2026-08-06 and 2026-10-07.) The readout lists every ruling the
controller made itself, as upstream's executing-plans lists its rulings
in its final message (v6.4.1): the ledger is deleted at Finish, so a
wrong ruling of the controller's is otherwise seen by no one. (Basis:
external, for upstream's list; judgment, accepted by the maintainer,
2026-10-27.)

Until 2026-10-28 every ruling that touched a [LOAD-BEARING] mark went
to the operator. With the spec read as a hypothesis
(`docs/decisions/the-spec.md`), a ruling that touches any binding
content, not only a mark, passes the containment test instead, so the
adjudicator marks what touches binding content and the controller
confirms what is contained. A reviewer's finding that a binding item's
literal reading reaches a case its author did not consider is ruled on
as the plan conflict it is, whether the binding text or the work is
wrong, and not sent to the adjudicator as an ordinary dispute; on a
diff the controller wrote it goes to the adjudicator, as every plan
conflict there does. (Basis: judgment, accepted by the maintainer,
2026-10-28.)

## Rejected

- **Adjudicating only at the cap**, upstream's rule (§ Why).
- **The controller ruling on findings against its own diff**, or parking
  a branch-review BLOCKER or MAJOR on its own ruling (§ Why).
- **Asking the operator which governs** on every plan conflict: only a
  design judgment, or a change to binding content the containment test
  does not find contained, reaches the operator (§ Why).
- **An operator ask for every ruling touching a mark**, the rule until
  2026-10-28 (§ Why).

## Changes

- 2026-10-28: a ruling touching any binding content, not only a mark,
  passes the containment test, a contained one becoming the controller's
  ruling and any other an operator ask; a reviewer's literal-reading
  finding is ruled on as a plan conflict.
- 2026-10-27: the close readout lists every ruling the controller
  made itself, not only dismissed or parked BLOCKER/MAJOR findings: the
  ledger is deleted at Finish, so the readout is the one place the
  operator can find a wrong ruling (after upstream's final message, at
  the v7.0.1 review).
- 2026-10-07: one dispute rule: NOT CONFIRMED answers and the
  controller's own disputes go in batches to a fresh adjudicator seat at
  any wave on every SDD route; the controller rules
  only on plan conflicts in diffs it did not write and on the breaker's
  consequences; rulings go to the ledger and the close readout.
