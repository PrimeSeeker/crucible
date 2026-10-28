# Task loop

## Decision

**The spine.** SDD executes a plan task by task: a fresh implementer, then
one fresh-context reviewer, with progress kept in a ledger that survives
compaction. The controller records BASE before each implementer, never
runs two implementers at once, and fixes no finding itself, inline mode
and the very-small lane's fix waves excepted
(`crucible:subagent-driven-development § The Task Loop`). The very-small
lane runs no per-task loop (`docs/decisions/routes.md`).

**The implementer contract.** What the plan's spec pointer names binds,
the decisions the spec records as the operator's firm preference
included (`docs/decisions/the-spec.md`), with requirements, interfaces,
non-goals and acceptance; the approach is advice. Binding text is read
for its intent. The implementer may depart from advisory content,
logging each departure in its report's Decision Log with what, why and
blast radius, and logs its call on every deferred item routed to its
task; changing or contradicting binding content, or applying it
literally to a case its author plainly did not consider, is BLOCKED,
the report naming the item, the evidence that shows it wrong and a
proposed correction
(`skills/subagent-driven-development/implementer-prompt.md` § Binding vs
Advisory: the Deviation License). The controller lets an item the
evidence does not show wrong stand, re-dispatching with its ruling, and
passes any other correction through the containment test: a contained
one it confirms, any other goes to the operator as a decision ask
carrying the proposal (`crucible:subagent-driven-development § The Task
Loop`, step 2). It reports BLOCKED or NEEDS_CONTEXT
rather than guess on insufficient context, an unsettled trade-off,
conflicting findings, ambiguity above its authority, or reading file
after file without progress, and is told that escalating is never
penalized (`skills/subagent-driven-development/implementer-prompt.md`
§ Stop-and-Ask Triggers). Its dispatch carries a one-line reminder of the
binding acceptance criteria and the Decision Log obligation; it writes
its report to a file and replies with a short status. A task that changes
text instructing agents sends it to `skills/writing-skills/SKILL.md`. It
commits with the identity git already has, sets none, and reports BLOCKED
when none is configured. Every implementer seat, fix waves' included, is
dispatched as instrument `implementer`, on the role SDD's Models section
names for it: the default role, the alternate role where one of its
triggers selects the seat, the bounded role for a clearly bounded task
(`docs/decisions/model-roles-and-effort.md`).

**Task review.** One fresh reviewer per task, never skipped. Its stance
is adversarial, "attempt to reject this task", governing the search and
not the conclusion. Four verdicts, all required: intent, scope, the
deviation audit (each Decision Log entry justified, nothing undisclosed,
every routed item's call recorded, RED before GREEN or a logged
exception) and quality (defects, not style; new-test adequacy is the
reviewer's own judgment). Cannot-verify items go to the controller, and
one it confirms is a failed intent verdict. The reviewer takes the
reported test output as given and builds its own diff
(`docs/decisions/branch-review.md`). Where a binding item's literal
reading reaches a case its author plainly did not consider, it reports a
literal-reading finding naming the item and the case, for the
controller's ruling (`docs/decisions/adjudication.md`). Task reviewers and re-reviewers run
on the bounded role or better (`docs/decisions/model-roles-and-effort.md`).

**Loop wiring.** A failed intent, scope or deviation-audit verdict enters
the fix loop whatever the finding's severity label; quality findings enter
by severity, BLOCKER and MAJOR in, MINOR to the ledger's deferred minors
for the branch review.

**Fix waves and the breaker.** A fix wave is one fix dispatch and its
scoped re-review; a task gets five. Waves 1–3 resume the recorded
implementer; waves 4–5 go to a fresh one, a tier bump where one exists
and at the default role fresh eyes at the same tier
(`docs/decisions/model-roles-and-effort.md`). Each finding is answered
fixed, with its covering run and sibling instances, or NOT CONFIRMED with
evidence for the adjudicator (`docs/decisions/adjudication.md`). When
wave 5 leaves findings open, the controller parks a real finding nothing
downstream builds on, with a ruling, and stops BLOCKED on a load-bearing
one, with a decision ask. A BLOCKED reasoning problem gets a tier bump
where one exists, and at the default role goes to the operator. No
trigger escalates a stuck seat further.

**Revert-and-replan.** Drift found after the fact, undisclosed and from
binding content or with cross-task blast radius, is reverted to the last
good commit and the task replanned, with an audit of the tasks that
depend on it. Undisclosed advisory choices and disclosed but unjustified
entries go to the fix loop instead
(`crucible:subagent-driven-development § Rules every route shares`).

**Snapshot blessing.** Where a task claims behaviour is preserved, a
changed snapshot or golden output is never blessed autonomously: a fresh
blind agent given only the old and new output and the preservation claim
verdicts the change, and one it judges intent-visible goes to the
operator as a decision ask saying what changed and why it matters, never
a raw diff.

**Inline mode.** The controller may implement a task itself, typically a
small mechanical one where a dispatch costs more than it protects. Review
applies unchanged, and any loop-entering finding, at any severity,
converts the task to standard dispatch, a fresh implementer owning the
fixes (`crucible:subagent-driven-development § Inline mode`).

## Why

### The spine

The spine is upstream's v6 SDD: a fresh implementer and reviewer per task,
a report file with a short status reply, a ledger, five fix rounds that
resume and then escalate, and a breaker at the cap
(`superpowers/skills/subagent-driven-development/SKILL.md`). Crucible's
first design (2026-08-05) judged it orthogonal to how lean a plan is and
kept it. A seat never inherits the controller's history, which keeps the
seat focused and the controller's context for coordination; upstream's
reason for the ledger stands, controllers that lost their place after
compaction having re-dispatched whole completed task sequences. (Basis:
external; judgment, accepted by the maintainer.)

### The implementer contract

The split between binding and advisory content, with every departure
logged, comes from the first design (2026-08-05): review then concentrates
on where the plan and the code disagree (`docs/decisions/the-spec.md`).
Stop-and-ask covers judgment, not mechanics: the implementer never guesses
at a decision above its authority and never reads ambiguity as licence.
Upstream's assurance that stopping is always acceptable, and its
file-after-file trigger, were dropped at the port with no reason and came
back on 2026-10-15. The dispatch's plan reminder rests on "From Plan to
Action: How Well Do Agents Follow the Plan?", where periodic plan
reminders mitigated plan violations and improved task success
(https://arxiv.org/abs/2604.12147). (Basis: judgment, accepted by the
maintainer; external.)

Dispatching every implementer seat as one instrument (2026-10-07) brings
the whole contract, the NOT CONFIRMED answer and the test rules included,
to every route. The pointer to writing-skills came on 2026-10-14: the
router tells dispatched seats to ignore it, and no template named
writing-skills, so its guidance reached an implementer writing skill text
only by accident; the skill's evaluations need fresh agents, which a seat
does not start, so the seat logs the prose-only exception and leaves them
to the controller. (Basis: judgment, accepted by the maintainer.)

On 2026-10-28, with the spec read as a hypothesis
(`docs/decisions/the-spec.md`), a binding item found wrong became a
correction to propose, not only a stop: the implementer holds the
evidence, so its BLOCKED report carries it with a proposed correction,
and the containment test decides whether the controller or the operator
confirms it. Reading binding text for its intent, with the
literal-reading case raised rather than applied, answers a sample's
case of a controller applying a Constraint literally to an edge case its
author plausibly never considered. Since that controller is also the
one who rules on such a case, its ruling, like an adjudicator's on a
diff the controller wrote, passes the containment test
whichever way it goes, and one applying the text where something
outside the feature builds on the behaviour it changes goes to the
operator. (Basis: judgment, accepted by the maintainer; measured, for
the case; judgment, a branch review's proposal accepted by the maintainer, for testing the
ruling.)

On 2026-08-23 an implementer seat committed under an identity taken from
its session context in place of the configured one; the rule against
setting one followed on 2026-10-07. (Basis: a single incident.)

### Task review

The maintainer kept a review per task: mistakes of the "this shouldn't be
here" kind had happened with Sonnet-era implementers (2026-08-05). Its
mandate moved from the letter of the requirements to their intent. Upstream's reviewer returns two verdicts, spec compliance
and code quality (`superpowers/skills/subagent-driven-development/task-reviewer-prompt.md`);
the first design (2026-08-06) split compliance into intent, scope and the
deviation audit, so that the "shouldn't be here" class has a verdict of
its own and the Decision Log is checked against the diff. (Basis: the
maintainer's preference, for keeping the review; judgment, accepted by
the maintainer, for the verdicts.)

The adversarial stance was ruled on 2026-08-06, bounded by finding
hygiene (`docs/decisions/evidence-and-findings.md`); a clean verdict is a
legitimate outcome because a manufactured finding costs a fix wave.
(Basis: judgment, accepted by the maintainer.)

Adequacy became the reviewer's own judgment, and RED before GREEN part
of the deviation audit, on 2026-10-07 (`docs/decisions/test-rules.md`).

### Loop wiring

Intent, scope and the deviation audit are pass-or-fail questions about
whether the task is what was asked; a failed one is a gap whatever label
the reviewer staked, so severity does not gate it, and neither a MINOR
label nor "close enough" keeps it out of the loop. Quality findings are
graded defects, and a MINOR one costs the branch review a triage line
rather than a wave. The wiring dates from crucible's first design
(2026-08-06). (Basis: judgment, accepted by the maintainer.)

### Fix waves and escalation

Waves 4–5 go to a fresh implementer for upstream's reason: a loop that
survives three resumes usually means the implementer cannot see its own
problem. Upstream also moves those waves, and a BLOCKED reasoning
problem, to a more capable model
(`superpowers/skills/subagent-driven-development/SKILL.md`); crucible's
escalation stops at the default role, since no escalation reaches the
alternate role, and a reasoning problem there goes to the operator, who
may name it (2026-10-13). On a stuck trigger the maintainer said: "Late
waves are generally not stuck, just slowly mining the residual issues.
We'll probably introduce a stuck trigger later." That also questions the
reason for fresh eyes at waves 4–5
(`docs/backlog/escalation-and-effort.md`). (Basis: external; the
maintainer's preference, for no stuck trigger; judgment, accepted by the
maintainer, for the routing.)

The cap, with the breaker, is the loop's termination guarantee. Upstream's
breaker let the controller park a finding it judged wrong; crucible sends
that finding to the adjudicator (`docs/decisions/adjudication.md`).
(Basis: judgment, accepted by the maintainer.)

### Revert-and-replan

Patching forward builds on work nobody reviewed against the plan, so
drift from binding content found after the fact goes back to the last good
commit (2026-08-05). The materiality bound came with the first design
(2026-08-06): implementers do not log every micro-choice, and a disclosed
entry is already visible to review. Whether impact evidence should choose
between revert and repair is open
(`docs/backlog/implementer-dispute-channel.md`). (Basis: judgment,
accepted by the maintainer.)

### Snapshot blessing

The first design (2026-08-06) made snapshot blessing and mutation runs the
compensating controls for leaving test files unlocked
(`docs/decisions/test-rules.md`). An implementer whose change alters
golden output could otherwise bless its own result; a blind agent shown
only the outputs and the claim judges the change without the author's
rationale, as blind fix verification does
(`docs/decisions/fix-verification-and-merge.md`); and since no step
requires the operator to read a diff, an intent-visible change reaches
them in words (`docs/decisions/operator-steering.md`). The mutation half
went on 2026-10-12; this half stands. (Basis: judgment, accepted by the
maintainer.)

### Inline mode

Upstream's executing-plans ran a plan in a separate session with review
checkpoints and no reviewer subagent, and sent users whose host has
subagents to SDD instead (`superpowers/skills/executing-plans/SKILL.md`). Both hosts
crucible supports dispatch subagents, and its review gates need a fresh
reviewer seat that a host without them cannot supply; the maintainer
confirmed that reason on 2026-10-20. What survives is the controller
implementing a task inside SDD, under unchanged review. A controller that
fixed its own findings would skip review, which the conversion rule
prevents; on 2026-10-07 the mode's guard against ruling on its own diff
became the general dispute rule. (Basis: external; judgment, accepted by
the maintainer.)

## Rejected

- **A stuck trigger** escalating a seat past the default role, for now
  (§ Why).
- **Patching undisclosed drift forward** (§ Why).
- **Severity labels gating a failed intent, scope or deviation-audit
  verdict** (§ Why).
- **Execution with no subagents**, upstream's executing-plans fallback
  (§ Why).
- **Autonomous snapshot blessing** by the implementer or the controller
  (§ Why).

## Changes

- 2026-10-28: testing a literal-reading ruling, accepted by the
  maintainer at the landing.
- 2026-10-28: an adjudicator's ruling on a literal-reading case passes
  the containment test too, closing the same gap on its path.
- 2026-10-28: a ruling on a literal-reading case, or on BLOCKED about a
  binding item, passes the containment test whichever way it goes, after
  a branch review found the controller's own literal application
  unguarded.
- 2026-10-28: the implementer contract: firm decisions bind, binding
  text is read for its intent, and BLOCKED on a binding item carries the
  evidence and a proposed correction, which the controller triages
  through the containment test; task review reports a literal-reading
  case for the controller.
- 2026-10-27: the identity incident no longer says whose address the
  seat used, which is private context.
- 2026-10-15: the implementer contract: binding and advisory content, a
  Decision Log entry per departure and per routed item, stop-and-ask on
  judgment with escalation never penalized, the plan reminder, the
  writing-skills pointer, no git identity set, one instrument for every
  implementer seat.
- 2026-10-13: the task-loop spine: fresh implementer and reviewer per
  task, five fix waves resuming then escalating by tier to fresh eyes at
  the default role, the breaker, BLOCKED reasoning at the default role to
  the operator, no stuck trigger, and revert-and-replan for undisclosed
  binding drift.
- 2026-10-07: task review: one adversarial reviewer per task with four
  required verdicts, cannot-verify items for the controller, adequacy the
  reviewer's judgment and RED before GREEN audited.
- 2026-10-07: inline mode: the controller implements a task under
  unchanged review, any loop-entering finding converting it to dispatch.
- 2026-08-06: loop wiring: failed intent, scope and deviation-audit
  verdicts enter the loop at any severity, quality findings by severity.
- 2026-08-06: snapshot blessing by a fresh blind agent, intent-visible
  changes to the operator as a decision ask.
