# Adjudication

## Decision

**One dispute rule on every SDD route.** A finding is fixed or disputed,
never dropped. The implementer answers a finding it disputes NOT
CONFIRMED, with evidence, and edits nothing for it. The rule holds at
any wave, on the standard route, the folded lane and the very-small
lane, in the task loop and the branch review. An upheld finding
re-enters the loop, or after a task's third wave the operator ask, and
cannot be disputed again. A dismissed finding is closed by its ruling.
Every outcome is written under the ledger's `## Adjudication rulings`,
with its reason and the evidence or the adjudicator's report. A ruling
that touches binding content, what binds in the spec or its umbrellas
(`docs/decisions/the-spec.md`), or answers a literal-reading finding,
passes the containment test before the controller acts on it: a contained one the controller
records as its own ruling, and any other goes to the operator as a
decision ask, the finding open until the answer; on the very-small
lane, one changing the note's binding parts is the operator's
(`skills/redteaming/references/flip-paths.md` § The containment test).
A ruling adds no wave; a wave whose fix dispatch only disputes is still
a wave. Every ruling the controller makes, with its reason, and every
dismissed or parked BLOCKER or MAJOR reach the operator in the close
readout (`crucible:subagent-driven-development § Rules every route
shares`).

**Who rules.** The controller rules, with its evidence, on an
implementer's NOT CONFIRMED, a finding it judges wrong and a plan
conflict (is the plan or the work wrong?); a reviewer's finding that a
binding item's literal reading reaches a case its author did not
consider is such a plan conflict. A fresh adjudicator seat, on the
default role (`docs/decisions/model-roles-and-effort.md`), rules
instead on any of these that touches binding content, as a
literal-reading finding always does, or the Intent, and on every
dispute about
a diff the controller wrote: a task it implemented inline, which its
ledger line `Task <N>: inline` records, and any very-small-lane diff.
Its disputes go in batches, one wave's or those the controller raises
together; the seat builds the diff of each finding's review range
itself, and its inputs point to the one full statement of what binds,
the Deviations paragraph of `crucible:subagent-driven-development § The
Task Loop`, rather than restating it. A plan conflict that is a design
judgment goes to the operator as a decision ask. The contained
amendments the controller confirms, the plan phase's included, are
among its rulings in the ledger and the close readout. A finding that
both fails a verdict and conflicts with plan text is ruled first as a
plan conflict; if the plan stands, the verdict failure enters the loop.
The controller never parks a
BLOCKER or MAJOR on its own ruling: in the task loop a finding is
parked on the operator's answer after the third wave. A red suite at
Finish that the controller judges not the branch's is a dispute under
the same rule, and the red run goes to the operator with its ruling,
whoever made it: the operator's acceptance, not the ruling, lets
finishing proceed.

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

Crucible kept upstream's pre-flight scan, the controller reading the
plan once before Task 1 for tasks contradicting each other, the spec or
what binds, and ruling on each as a plan conflict. It went on
2026-11-02: conflicts that emerge from implementation are the review
loop's, as they already were. (Basis: the skill-text-rewrite umbrella's
D3, the controller's proposal on its audit's counts, accepted by the
maintainer.)

### Disputes at any wave

With disputes heard only at the breaker, a wrong finding cost up to five
waves or landed as an edit made only to comply, while the very-small lane
had sent a contested finding to a fresh adjudicator at any wave since
2026-09-27. On 2026-10-07 that became the rule on every route, replacing
inline mode's guard and the lane's own rule, and the maintainer asked for
it to be part of that feature. An upheld finding cannot come back as a
dispute, and adjudication adds no wave, so the caps on a task's waves and
a branch's still terminate the loops. (Basis: judgment, accepted
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
content passes the containment test instead, so the adjudicator marks
what touches binding content and the controller confirms what is
contained. A reviewer's finding that a binding item's
literal reading reaches a case its author did not consider is a plan
conflict, whether the binding text or the work is wrong; until
2026-11-02 the controller ruled on it, not sending it to the
adjudicator as an ordinary dispute, except on a diff it wrote (§ The
controller rules, with three independent reads). Either seat's ruling on such a finding passes the
containment test whichever way it goes, since upholding the literal
reading changes no binding content and would otherwise go untested.
(Basis: judgment, accepted by the maintainer, 2026-10-28; judgment, a
branch review's proposal accepted by the maintainer, for testing the ruling.)

### The controller rules, with three independent reads

From 2026-10-07 every contested finding went to a fresh adjudicator,
and the controller ruled only on plan conflicts in diffs it did not
write. The skill-text-rewrite umbrella's audit found adjudication had
run 5 times and upheld nothing, and the controller's lean toward its own
position documented repeatedly in the terminal pass's record checks.
(Basis: measured.) Since 2026-11-02 the controller rules on a dispute with its
evidence, and the independent read stays where that lean would cost
most: a dispute touching binding content or the Intent (the umbrella's
D4), and one on a diff the controller wrote, since a ruling on its own
diff that only the close readout lists would be silent to an operator
who does not read diffs (the umbrella's D2). The `Task <N>: inline`
line keeps that trigger readable after a compaction. A plan conflict
is one of the disputes this sorts: one touching binding content, as a
literal-reading finding always does, or the Intent goes to the
adjudicator, whose ruling still passes the containment test; one
touching neither stays the controller's; one that is a design judgment
goes to the operator. The adjudicator's inputs point to the Deviations
paragraph, so no partial restatement of what binds can drop a clause.
A red suite judged not the branch's needs the operator's acceptance
whoever ruled, so the controller's ruling never lets finishing proceed
by itself. (Basis: the umbrella's D4, the controller's proposal
accepted by the maintainer; the read on the controller's own diff, the
controller's proposal accepted by the maintainer at this change's
brainstorm; for plan conflicts, the controller's ruling on a task
review's finding against a narrower first draft, read from the
umbrella's D4 and this change's spec.)

## Rejected

- **Adjudicating only at the cap**, upstream's rule (§ Why).
- **Every dispute to a fresh adjudicator**, the rule from 2026-10-07 to
  2026-11-02 (§ Why).
- **The controller ruling on findings against its own diff**, or parking
  a BLOCKER or MAJOR on its own ruling (§ Why).
- **Asking the operator which governs** on every plan conflict: only a
  design judgment, or a change to binding content the containment test
  does not find contained, reaches the operator (§ Why).
- **An operator ask for every ruling touching a mark**, the rule until
  2026-10-28 (§ Why).
- **A pre-flight plan-conflict scan** before Task 1, the rule until
  2026-11-02 (§ Why).

## Changes

- 2026-11-02: the pre-flight plan-conflict scan retired, with its
  rulings and the close readout's "pre-flight" plan conflicts; after the
  skill-text-rewrite umbrella's audit (§ Why).
- 2026-11-02: the controller rules on disputes with its evidence; a
  fresh adjudicator rules only where a dispute, a plan conflict
  included, touches binding content or the Intent (a literal-reading
  finding always does), or concerns a diff the controller wrote, which the new
  ledger line `Task <N>: inline` records; the adjudicator's inputs point
  to the Deviations paragraph instead of restating what binds; a red
  suite ruled not the branch's goes to the operator with its ruling,
  whoever made it, the operator's acceptance letting finishing proceed.
  The every-dispute-to-a-fresh-seat rule goes, and
  the Rejected bullet on parking now covers every route. After the
  skill-text-rewrite umbrella's audit (§ Why).
- 2026-11-02: the breaker retired: the controller no longer rules on
  consequences at the task-loop cap or parks a finding there, and a
  finding upheld after a task's third wave joins the operator ask that
  stops the task; after the skill-text-rewrite umbrella's audit found the
  breaker never ran (`docs/decisions/task-loop.md`).
- 2026-11-02: the containment rule's present-tense wording drops the
  words naming a mark beside binding content, since marks no longer exist and binding content is all
  it names. (Basis: judgment, accepted by the maintainer, in retiring
  marks.)
- 2026-10-28: testing a literal-reading ruling, accepted by the
  maintainer at the landing.
- 2026-10-28: a ruling on a literal-reading finding, the controller's or
  the adjudicator's, passes the containment test whichever way it goes,
  after a branch review found an upheld literal reading untested.
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
