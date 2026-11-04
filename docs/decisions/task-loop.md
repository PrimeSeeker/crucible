# Task loop

## Decision

**The spine.** SDD executes a plan task by task: a fresh implementer, then one fresh-context reviewer, unless the plan routes the task's review to the branch review (below), with progress kept in a ledger that survives compaction. The controller records BASE before each implementer, never runs two implementers at once, and fixes no finding itself, inline mode and the very-small lane's fix waves excepted (`crucible:subagent-driven-development § The Task Loop`; `skills/subagent-driven-development/references/task-loop.md`). The very-small lane runs no per-task loop (`docs/decisions/routes.md`).

**The implementer contract.** What the plan's spec pointer names binds, with each task's Contract and Acceptance and the plan's inter-task contracts, a lightly-held decision a Contract cites staying lightly held, read for its intent (`docs/decisions/the-spec.md`; `crucible:writing-plans § Deferring detail`); the approach is advice, and the implementer may depart from it, logging each departure in its report's Decision Log with what, why and blast radius. Changing or contradicting binding content, or applying it literally to a case its author plainly did not consider, is BLOCKED, the report naming the item, the evidence that shows it wrong and a proposed correction (`skills/subagent-driven-development/implementer-prompt.md` § Binding vs Advisory: the Deviation License); the controller lets an item the evidence does not show wrong stand and passes any other correction through the containment test (`skills/subagent-driven-development/references/task-loop.md` § 2. Handle the report). It reports BLOCKED or NEEDS_CONTEXT rather than guess, and is told that escalating is never penalized (`skills/subagent-driven-development/implementer-prompt.md` § Stop-and-Ask Triggers). Beside its work, its report may carry concerns, `Questions` items, a premise finding (`docs/decisions/evidence-and-findings.md`) and a fix it proposes outside its task, which it never makes; the controller handles none of these before review (`crucible:subagent-driven-development § What a report voices`). Its dispatch carries a one-line reminder of the binding acceptance criteria and the Decision Log obligation (`skills/subagent-driven-development/implementer-prompt.slots.md`). Every implementer seat, fix waves' included, is dispatched as instrument `implementer` (`skills/subagent-driven-development/references/dispatch-composition.md` § Models and effort; `docs/decisions/model-roles-and-effort.md`). What else it follows, its report file, writing-skills for text instructing agents and the git identity among them, is its template's (`skills/subagent-driven-development/implementer-prompt.md` § Where You Work, § Tests: Test-First, Evidence Before Done, § Report Format).

**Task review.** One fresh reviewer per task, never skipped, a task completed branch review only aside (below). Its stance is adversarial, "attempt to reject this task", governing the search and not the conclusion, and it returns four verdicts, all required: intent, scope, the deviation audit and quality (`skills/subagent-driven-development/task-reviewer-prompt.md`). A concern is confirmed as a finding at a staked severity or dismissed with a one-line reason, and a review or re-review that leaves one unruled is missing a verdict (`skills/subagent-driven-development/references/seat-rules.md` § Concerns; `crucible:subagent-driven-development § What a report voices`). A missing verdict goes back to its seat, never to the controller's ruling (`crucible:subagent-driven-development § Rules every route shares`). Its own `Questions` items, a premise doubt among them, become leads (`docs/decisions/evidence-and-findings.md`). It takes the reported test output as given and builds its own diff (`docs/decisions/branch-review.md`), and a literal-reading finding goes to the adjudicator (`docs/decisions/adjudication.md`). The task reviewer runs on the default role, every task it reviews, and the re-reviewer on the bounded role or better (`docs/decisions/model-roles-and-effort.md`). An open premise finding holds no task's completion by itself.

**Branch review only.** A dispatched task whose plan section carries `Review: branch only` (`docs/decisions/plans.md`) runs no task review and no fix loop where its report is DONE, raises no concern and passes the verification gates, which for it also check that the report shows RED output before GREEN or a logged exception. The controller checks that each is there; the branch reviewer, the task's first review, judges its substance (`docs/decisions/branch-review.md`). A report raising a concern or failing a gate sends the task to the task review after all, and a task worked inline keeps its task review whatever its mark (`skills/subagent-driven-development/references/task-loop.md` § 2. Handle the report; `crucible:subagent-driven-development § Inline mode`).

**Loop wiring.** A failed intent, scope or deviation-audit verdict enters the fix loop whatever the finding's severity label; quality findings enter by severity, BLOCKER and MAJOR in, MINOR to the ledger's deferred minors for the branch review (`skills/subagent-driven-development/references/task-loop.md` § 3. Review the task, § 5. The fix loop).

**Fix waves.** A fix wave is one fix dispatch and its scoped re-review, and a task gets three, each resuming the recorded implementer where the host can (`skills/subagent-driven-development/references/task-loop.md` § 5. The fix loop). Findings still open after the third wave stop the task: the controller puts them to the operator as a decision ask, and further waves are not an answer (`crucible:subagent-driven-development § The Task Loop`). An answer of a plan change short of a supersede closes the open findings, and the task runs again with its BASE, its review re-grading them. A BLOCKED reasoning problem gets a tier bump where one exists, and at the default role goes to the operator; a task waiting on the operator after BLOCKED carries a ledger line saying so, which the resume rule reads. No trigger escalates a stuck seat further.

**Drift found after the fact.** Drift undisclosed and from binding content or with cross-task blast radius is a decision ask to the operator with the controller's recommendation, revert or repair; undisclosed advisory choices and disclosed but unjustified entries go to the fix loop instead (`crucible:subagent-driven-development § Drift found after the fact`; `skills/subagent-driven-development/references/drift.md`).

**Snapshot blessing.** Where a task claims behaviour is preserved, a changed snapshot or golden output is never blessed autonomously: a fresh blind agent given only the old and new output and the claim rules on the change, and one it finds visible goes to the operator as a decision ask, never a raw diff (`skills/subagent-driven-development/references/task-loop.md` § 4. Verification gates).

**Inline mode.** The controller may implement a task itself only where the task is overdetermined and fits its remaining context without pushing out the coordination state it needs through the branch review; otherwise it dispatches, the default. Review applies unchanged, and any loop-entering finding, at any severity, converts the task to standard dispatch (`crucible:subagent-driven-development § Inline mode`; `skills/subagent-driven-development/references/inline-mode.md`). On the very-small lane the same test decides, only its review clause not applying, and the lane's branch-review fix waves stay the controller's (`skills/subagent-driven-development/references/very-small-lane.md`).

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

What binds is stated per document since 2026-11-04. The spec's list and
the plan's had stood side by side since 0.2.0 without saying so:
writing-plans listed a spec's own sections beside the spec pointer's,
which read as a wider list for the spec, and the implementer template's
Binding line named none of them, though the 2026-10-28 spec of the firm
class took it to. A plan task's Contract and Acceptance and the
inter-task contracts bind as plan content, and what binds in a spec is
unchanged, its own Acceptance, interfaces and non-goals staying lightly
held there (`docs/decisions/the-spec.md`). So an Acceptance item a task
takes up binds as that task's, and changing it mid-execution takes the
containment test, while a lightly-held decision a Contract cites stays
lightly held: citing it by id is not restating it. An agent's recommendation, on which
the maintainer left the call to the agent. (Basis: judgment, accepted by
the maintainer.)

On crucible's umbrella-specs feature (2026-10-28, five tasks, all
prose), the issues that mattered surfaced in the implementers'
`DONE_WITH_CONCERNS` reports: a duplicated rule, ceremony for an
approval-only document, a rule two phases could never reach, and wrong
Basis tags in a decision record. The controller then noted concerns
that did not bear on correctness or scope and sent the task to review;
the five task reviewers approved every task with minors only, and the
branch review confirmed the unreachable rule as its one MAJOR. The
maintainer's view was that implementers should probably be empowered
further. A
concern now goes to the review of the work it is about, which must rule
on it, and what reaches beyond the task has `Questions`, a premise
finding or a proposal, so an implementer that sees a fix elsewhere says
so instead of making it. (Basis: a single incident; the maintainer's
preference, for the aim; judgment, accepted by the maintainer, for the
form.)

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

From 2026-10-07 to 2026-11-02 a requirement the reviewer could not
verify from the diff came back as a cannot-verify item, after upstream's
cannot-verify reference, for the controller to resolve, a confirmed gap
failing the intent verdict and entering the fix loop. Since 2026-11-02
the reviewer checks such a requirement in the code it needs, one focused
check, and its verdicts carry the result. (Basis: the skill-text-rewrite
umbrella's D3, the controller's proposal on its audit's counts, accepted
by the maintainer.)

The task reviewer moved to the default role on 2026-10-29, after a
differential probe of past task reviews found the reviews on the bounded
role missing what a default-role seat with no rubric saw, on small
samples and with model and rubric confounded
(`docs/decisions/model-roles-and-effort.md`). Its mandate stayed: on
code the probe found the rubric hiding nothing, so a premise doubt is
one of its questions, not a finding (`docs/decisions/evidence-and-findings.md`).
(Basis: measured; judgment, accepted by the maintainer.)

### Branch review only

The maintainer named per-task review among the choices a route fixes
that need not align with the others (2026-10-28), and asked whether the
reviewers' widened mandate belonged "maybe only full-branch, rather than
task reviews?". (Basis: the maintainer's preference, for making it a
choice.) The evidence above points the same way for some tasks: on the
umbrella-specs feature the task reviews of prose tasks run in sequence on
shared files approved everything while the implementers' concerns and
the branch review found what mattered, and an escape analysis of 109
features' histories found task reviews letting through 12 real defects,
10 minor slips and 2 premise-level MAJORs that needed other tasks'
knowledge, both caught by the branch review
(`docs/decisions/evidence-and-findings.md`). (Basis: a single incident;
measured.)

The mark is the plan's call, written with the plan, so it needs no
confirmation of its own at brainstorming; a task review is dropped only
where the plan says why the task meets the criterion. The controller's
part is a presence check, not a ruling: it rules on no concern, and any
concern sends the task to its own review. As first adopted, only a
concern touching what a later task builds on did, because the branch
review runs too late for that, the rest becoming leads, and the branch
reviewer made the task review's four judgments and owed a line per
task; the alternatives offered then were leads alone, with no escape to
a task review, and the controller ruling on the concerns itself.
(Basis: judgment, accepted by the maintainer, 2026-10-29.) The skill
text rewrite reduced the mark to one field and its reason, with no
grading chain: every concern goes to the task review, and the
branch reviewer reads the report's Decision Log against the diff, its
findings opening waves by their staked severity. (Basis: the
skill-text-rewrite umbrella's D4, with the maintainer's judgment that
marks were used too liberally; judgment, the controller's proposal
accepted by the maintainer, for the defaults, 2026-11-02.) An inline task keeps its task
review whatever its mark: without it no fresh seat would read the task
before the branch review, and inline mode stays where the maintainer's
ruling of 2026-10-27 left it, "not extended for now". That was an
agent's proposal, the maintainer leaving the call to it ("your call").
(Basis: judgment, accepted by the maintainer, 2026-10-29.)

### Loop wiring

Intent, scope and the deviation audit are pass-or-fail questions about
whether the task is what was asked; a failed one is a gap whatever label
the reviewer staked, so severity does not gate it, and neither a MINOR
label nor "close enough" keeps it out of the loop. Quality findings are
graded defects, and a MINOR one costs the branch review a triage line
rather than a wave. The wiring dates from crucible's first design
(2026-08-06). (Basis: judgment, accepted by the maintainer.)

### Fix waves and escalation

Until 2026-11-02 a task got five waves. Waves 4–5 went to a fresh
implementer, a tier up where one existed, for upstream's reason: a loop
that survives three resumes usually means the implementer cannot see its
own problem (`superpowers/skills/subagent-driven-development/SKILL.md`).
At the cap a breaker had the controller park a real finding nothing
downstream built on and stop BLOCKED on a load-bearing one. The audit
behind the skill-text-rewrite umbrella (2026-11-01) found the breaker
never ran in the runs it read, and the maintainer had said of late
waves: "Late waves are generally not stuck, just slowly mining the
residual issues. We'll probably introduce a stuck trigger later." Under
the umbrella's rule that a guard which never ran keeps only its trigger,
as a stop-and-ask line or a short cap with an operator ask, the fresh
implementer, its tier step and the breaker went: three resumed waves,
then the operator chooses what happens to the findings left open. The
cap and that answer are the loop's termination guarantee. (Basis:
external, for upstream's reason; measured, for the audit's count, a
lower bound; judgment, accepted by the maintainer, for the umbrella's
retirement and, at the execution-retirements brainstorm, for the cap of
three and the ask's options.)

Upstream also moves a BLOCKED reasoning problem to a more capable model;
crucible's escalation stops at the default role, since no escalation
reaches the alternate role, and a reasoning problem there goes to the
operator, who may name it (2026-10-13). A stuck trigger stays out
(`docs/backlog/escalation-and-effort.md`). (Basis: external; the
maintainer's preference, for no stuck trigger; judgment, accepted by the
maintainer, for the routing.)

Three next steps stayed unstated until 2026-11-04. A task waiting on an
ask after an implementer's BLOCKED had no ledger line, so the resume rule
read it as resumable (a closing review, 2026-11-03). A plan change after
the third wave left the latest line at `3/3`, and the resume rule sent
the task to an ask already answered; its open findings close rather than
being tracked one by one, since the review reads the whole task again
from its BASE. A review missing a verdict had no action: the seat owes
the verdict, and a controller's ruling in its place would not be an
independent one, so a replacement's miss goes to the operator. The
re-run's review reads every run's report, since its range holds the
earlier runs' commits and its scope and evidence checks read the report.
(Basis: judgment, an agent's proposal accepted by the maintainer, for the
ledger line, the plan-change line and the seat owing the verdict;
judgment, an agent's call the maintainer has not ruled on, for the
replacement's miss and for what the re-run's review is given.)

### Drift found after the fact

Patching forward builds on work nobody reviewed against the plan, so
from 2026-08-05 drift from binding content found after the fact went
back to the last good commit and the task was replanned, an attempt
number in its `reverted` line. The materiality bound came with the first
design (2026-08-06): implementers do not log every micro-choice, and a
disclosed entry is already visible to review. The umbrella's audit found
revert-and-replan never ran, and whether impact evidence should choose
between revert and repair had been left open; on 2026-11-02 drift became
a decision ask, the operator choosing revert or repair on the
controller's recommendation. A revert's line reopens the task with no
attempt number, since the resume rule reads a task's latest line; a
DRIFT pass at the branch review no longer spends a wave, since a revert
is the operator's answer each time and adds no cycle the operator did
not choose (`docs/decisions/branch-review.md`). (Basis: judgment,
accepted by the maintainer, for the first design and, at the
execution-retirements brainstorm, for the operator ask.)

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
maintainer.) On 2026-11-02 its procedure became one line: the seat, its
inputs, its report path and the operator ask, the verdict's two labels
dropped (the skill-text-rewrite umbrella's D4, the controller's
proposal, accepted by the maintainer).

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

Until 2026-10-29 the mode had no stated criterion: inline mode was for a
small mechanical task, by a loose judgment of a dispatch's cost against
its protection, and the lane dispatched by the change's width. The
maintainer raised the question, cost and speed against "fresh eyes,
fresh context", with "no clear separating criterion", and wanted inline
execution not expanded "much" (2026-10-29). A dispatched implementer buys
an independent read of the spec before code, worth more as review
before code shrinks, and the controller's context; a task with nothing
left to decide gains nothing from the first, so it may run inline where
the second allows. The defaults stayed: subagents on the campaign
presets, inline on the lane. The lane's branch-review fix waves stay the
controller's whatever the change's width, a residual accepted since a
lane change is one implementer's worth. An agent's proposal, which the
maintainer accepted ("OK, I guess"). (Basis: the maintainer's
preference, for not expanding the mode; judgment, accepted by the
maintainer, for the criterion.)

That left the lane's inline test looser than everywhere else, context
alone, while the lane's population widened to changes with non-trivial
impact whose mechanism is settled (`docs/decisions/routes.md`). The
controller's brainstorm argument for widening the lane had relied on
inline work being limited to overdetermined changes, and a spec-round
fix removed that safeguard (the audit,
`docs/decisions/evidence-and-findings.md`). Since
2026-10-30 the lane takes the same test as any task, the change
overdetermined and fitting the controller's context, and dispatches its
implementer otherwise, as it already could; the lane's fix waves stay
inline by the lane's own design. An agent's proposal, which the
maintainer accepted. (Basis: measured, for the audit's finding;
judgment, accepted by the maintainer, for the test.)

## Rejected

- **A spec's Acceptance, interfaces and non-goals binding as well:** every
  change to them after the campaign would be an amendment, against the
  spec read as a hypothesis (`docs/decisions/the-spec.md`), whose sample's
  longest chain of asks began at an Acceptance threshold.
- **The spec's list alone binding an implementer, plan text included:**
  reviewers and the implementer's own reminder hold a task to its
  acceptance, so this would change what they enforce.
- **A stuck trigger** escalating a seat past the default role, for now:
  the maintainer judged late waves generally not stuck, just slowly
  mining residual issues (§ Why).
- **Repairing or reverting undisclosed binding drift without the
  operator's answer**: the automatic revert never ran in the audit's runs,
  and the choice between revert and repair had been left open (§ Why).
- **Five fix waves, a fresh implementer at waves 4–5 and the breaker**,
  retired 2026-11-02: the breaker never ran in the audit's runs, and a
  guard that never ran keeps only its trigger (§ Why).
- **Severity labels gating a failed intent, scope or deviation-audit
  verdict**: a failed one is a gap whatever label the reviewer staked
  (§ Why).
- **Execution with no subagents**, upstream's executing-plans fallback:
  both supported hosts dispatch subagents, and the review gates need a
  fresh reviewer seat (§ Why).
- **A marked task's concerns as leads alone, or ruled on by the
  controller**: the branch review runs too late for what a later task
  builds on, and the controller's part is a presence check, not a ruling
  (§ Why).
- **Autonomous snapshot blessing** by the implementer or the controller:
  an implementer could bless its own result, where a blind agent judges
  the change without the author's rationale (§ Why).
- **Cannot-verify items for the controller**, the rule from 2026-10-07
  to 2026-11-02: the reviewer checks such a requirement itself, in the
  code it needs, and its verdicts carry the result (§ Why).

## Changes

- 2026-11-04: a task waiting on the operator after BLOCKED gets a ledger line; a plan change short of a supersede after the third wave records a line with the task's BASE, closes the open findings and re-runs the task with that BASE, reviewed even where it is marked, on every run's report; a missing verdict goes back to its seat or a replacement, then to the operator, never the controller's ruling; because each left the controller with no stated next step.
- 2026-11-04: what binds is stated per document: a plan task's Contract and Acceptance and the inter-task contracts as plan content, the spec's list unchanged; because writing-plans' list of a spec's own sections read as a second list for the spec, and the implementer template named no plan items.
- 2026-11-03: the implementer's role is cited at the dispatch composition's § Models and effort and its slot card's Model line, no longer at SDD's Models section; because SDD dropped the implementer's row when the default role came to be stated once for every seat (`docs/decisions/model-roles-and-effort.md`).
- 2026-11-03: the arrangement questions' citation follows their move from the shared seat reference to `skills/subagent-driven-development/references/review-terms.md`, a reference of their own, so a controller that applies them no longer loads the seat rules.
- 2026-11-02: the shared seat reference's citations follow its rename
  to `seat-rules.md`.
- 2026-11-02: a task marked `Review: branch only` completes branch review
  only where its report is DONE, raises no concern and passes the
  gates; any concern sends it to its task review, no longer only one
  touching what a later task builds on, and its concerns no longer
  become leads; the branch reviewer reads its report's Decision Log in
  every full-scope pass, owing no line per task. After the
  skill-text-rewrite umbrella reduced the mark to one field and its
  reason (`docs/decisions/branch-review.md`).
- 2026-11-02: the implementer's Decision Log entry per routed deferred
  item, the task review's per-row check of routed items and its
  `Routed deferred items` report line, and the routed-item entry in a
  marked task's gate retired with the plan's routing table; a deferred
  call is logged where it departs from advisory content
  (`docs/decisions/plans.md`).
- 2026-11-02: the task review's cannot-verify items retired, with the
  report's "Cannot verify from diff" line and the fix-loop trigger they
  fed: the reviewer checks a requirement outside the diff in the code it
  needs. Snapshot blessing stated as one line, its verdict labels
  `preserved` and `intent-visible` dropped. After the
  skill-text-rewrite umbrella's audit (§ Why).
- 2026-11-02: a NOT CONFIRMED answer goes to a ruling, the
  controller's or the adjudicator's, no longer always the adjudicator's;
  an inline task gets the ledger line `Task <N>: inline`, which keeps
  the adjudicator's read on its diff after a compaction; a
  literal-reading finding goes to the adjudicator, not the controller's
  ruling (`docs/decisions/adjudication.md`).
- 2026-11-02: the fix loop: three resumed waves, the `<W>/5` fix-wave
  line now `<W>/3`, then an operator ask with park, block or another
  approach, recorded under `## Adjudication rulings`; the fresh
  implementer at waves 4–5, its tier escalation, the breaker and its
  sense of "load-bearing" retired. Drift found after the fact an
  operator ask, revert or repair; the revert-and-replan section, the
  `reverted` line's attempt number (`replanned as attempt <X>`) and the
  rule that a DRIFT pass spends a wave retired. After the
  skill-text-rewrite umbrella's audit found the breaker and
  revert-and-replan never ran.
- 2026-10-30: the very-small lane implements inline only where the
  inline test holds, the change overdetermined and fitting the
  controller's context, reversing the 2026-10-29 lane dispatch by
  context alone; its fix waves stay inline, a cleanup wave's included;
  after an audit found the lane's test looser than everywhere else.
- 2026-10-29: a task the plan marks `Review: branch only`, dispatched,
  runs no task review where its report passes the widened gates and no
  concern touches a later task's ground, its concerns becoming leads and
  the branch reviewer its first review, completed by a new ledger line;
  an inline task keeps its review; inline mode only for an overdetermined
  task that fits the controller's context, the lane's dispatch by context
  alone, in place of "costs more than it protects" and "wide enough to
  crowd"; after the maintainer's request to separate per-task review and
  question about inline execution.
- 2026-10-29: implementers' standing: the review of the work rules on
  every concern the implementer reports, a missing ruling counting as a
  missing verdict, and the controller handles none before it; an
  implementer may add `Questions`, a premise finding and fixes proposed
  outside its task, never made; the task reviewer runs on the default
  role; after the umbrella-specs run and a differential probe.
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
