# Routes

## Decision

**Four choices, three presets.** A feature's arrangement is four
choices: review before code, the plan's form, per-task review, and
inline or subagent execution. The branch review is no choice: every
arrangement runs it, at full scope. The routes are presets over the
choices, standard the usual one, folded and very small the others, and
a combination with no known use is unsupported; the presets and the
unsupported list are stated once, in `skills/brainstorming/SKILL.md`
§ Proposing the arrangement (step 4). Each choice is made where its
information exists: the preset at brainstorming's present-the-design
step, per-task review in the plan (`docs/decisions/plans.md`), execution
per task (`docs/decisions/task-loop.md`). A campaign's width stays where
it was chosen, at the digest gate and by the stop rule
(`docs/decisions/spec-campaign.md`).

**The preset is the operator's.** The controller proposes a preset as it
closes the design presentation, naming it, the overturn answer with its
reason and, for folded, the plan-size reason; the operator confirms or
vetoes it there, and the answer is the route entry in the brainstorm
decision record, written for every preset. The operator confirms the
preset only: a departure expected later, such as tasks the plan may
route to the branch review alone, is a heads-up. The controller never
declares a preset, and no feature enters one mid-flight; the lane's
upgrade hatch and an operator-confirmed downshift (`docs/decisions/plans.md`)
are the exceptions. An umbrella, the document holding an effort of
several features, takes no preset: it is campaigned or approved by what
it carries, and each of its children takes a preset of its own
(`docs/decisions/umbrellas.md`).

**The overturn question chooses.** A feature takes a spec campaign where
overturning one of its major mechanisms after code is plausible, and
none where it is not; the question, and the two cases in which it
answers no before any review, are defined in
`skills/subagent-driven-development/references/premise-and-questions.md`
§ The arrangement questions. Between the campaign presets, folded fits
a plan of one or two tasks with no seam worth its own review, standard
the rest. Width is no test of risk, since the branch review reads the
whole diff whatever its width, but it shapes the arrangement where work
needs coordinating: a settled change one implementer can carry takes
the very-small preset; a settled change that needs several coordinated
tasks takes standard, whose campaign can be expected to stop after its
first round. File and line counts are not the test.

- **Folded:** spec and plan in one document, `folded.md`, no plan phase,
  and every review instrument unchanged
  (`skills/redteaming/references/folded-lane.md`).
- **Very small:** a frozen lane note (the request, intent, change list,
  acceptance as runnable checks, out of scope), implemented inline by
  default, the repository's own gates and the branch review, with no
  spec campaign, plan, digest or per-task review
  (`skills/subagent-driven-development/references/very-small-lane.md`).
  The branch reviewer, the lane's first review, states in its Lane Fit
  whether overturning a major mechanism of the change is plausible now
  that it is coded, EXCEEDS SHAPE opening the upgrade hatch and WITHIN
  SHAPE keeping the lane, and whether the note's Intent matches the goal
  its request asks for; it rules on a dispatched implementer's concerns,
  questions and proposals, which the controller transcribes to the
  ledger as leads.

**The origin question.** A feature with non-trivial impact may skip
review before code where the overturn question answers no at
brainstorming and the change is one implementer's worth: the mandatory
full-scope branch review, with its goal and premise checks, is the
independent check, and an unsettled mechanism is the risk, not size.
This is a hypothesis, with the evidence and limits below.

**The trivial-edit waiver.** For a change it judges trivial, the agent
may offer in one line to make it without crucible's process, with no
lane and no artifact; the operator's yes covers that edit only, and the
project's own rules still apply (`skills/using-crucible/SKILL.md`).

## Why

### One process for review, lighter documents

The process started uniform: small edits have surprising blast radius,
and in the maintainer's experience no spec had come through its first
review round without a major finding, small ones included (2026-08-07).
That still holds for the review instruments, which is why the folded
lane drops none of them. What was disproportionate on a small change was
the plan phase and oversized panels: in one run the maintainer described,
a change of four file deletions took about 15 agent dispatches, while
its terminal pass caught a real major defect. Findings scale with the
artifact's surface, not the change's, so the fold removes an artifact,
not a check (2026-08-21). Undoing a fold is an operator decision ask on
the supersede path, and the route is known from `folded.md` and the
decision record's entry, with no folded-lane marker written anywhere.
(Basis: the maintainer's preference, for the uniform review; judgment,
accepted by the maintainer, for the fold; a single incident, for the
run.)

### Separable choices

The maintainer observed that a route fixed several decisions together,
"redteaming usage and then width, separate/folded plan and possibly
per-task review usage, direct/subagent execution", that "are correlated,
but don't have to be always aligned" (2026-10-28). (Basis: the
maintainer's preference, for separating them.) Of three forms an agent
offered, presets over the choices, the choices as fields alone, and the
routes plus two toggles, the maintainer took presets ("Agreed on form"),
and only combinations with a known use are supported. The step-4
confirmation covers the preset alone because per-task review needs the
tasks and execution needs the task in hand, which only the plan and the
task loop have. (Basis: judgment, accepted by the maintainer,
2026-10-29.)

The folded preset was kept rather than retired: about nineteen features
used it, on crucible before its move to this repository and on one other
project. Whether the overturn question leaves it a niche is left for
later. (Basis: measured, for the count; judgment, accepted by the
maintainer, for keeping it.)

A lane note with a plan, for a settled change that needs several
coordinated tasks, and a spec implemented with no plan after its
campaign were both left out, each an agent's proposal the maintainer
accepted ("your call", and "Agreed"); both wait in
`docs/backlog/lane-entry-and-downshift.md`, the first with its trigger: a
settled change campaigned only to get a plan. (Basis: judgment, accepted
by the maintainer, 2026-10-29.)

### The overturn question as the selector

The effort that brought it began with the maintainer's question, "is
routing features with potentially non-trivial impacts through very small
lane sound?", and the maintainer proposed the criterion: "do we
reasonably expect major mechanisms to be overturned further down the
line?", which "probably also should be used as the primary very-small
trigger - say, for lack of major mechanisms, or overdetermined
decisions" (2026-10-28). (Basis: the maintainer's preference, for the
selector, approved as a hypothesis like every approval, never firm.)

The test it replaced measured size: the two small routes qualified by
the change's novelty, reach across subsystems and touch on
[LOAD-BEARING] content, and were told apart by whether a design decision
deserved review before code, so a change with non-trivial impact whose
mechanism was already settled went to a campaign for its size. The
question replaces both. Width moved to the plan and execution choices,
where coordination is what it costs. The [LOAD-BEARING] clause went:
shipped specs are frozen, and under an umbrella a change to its marks is
already a binding change with its own path; the residual, a lane outside
any umbrella changing what another feature in flight builds on, is
accepted as rare and visible at the merge. The alternatives offered were
the question plus a blast-radius limit, and the shape test kept beside
the question. (Basis: judgment, accepted by the maintainer, 2026-10-29.)

Lane Fit asks the same question of the diff, and keeps its verdict words
because other files, and features in flight on older installs, read
them. (Basis: judgment, accepted by the maintainer, 2026-10-29.)

### The origin question's answer

The answer rests on the branch review: it is mandatory on every
arrangement, reads the whole diff, and since 2026-10-29 checks the
goal against the request and may raise premise findings
(`docs/decisions/evidence-and-findings.md`). Two probes, read from
records outside this repository (session transcripts, the repository
crucible was developed in before its move here, and one other project's
feature folders), bear on it, as aggregates this tree cannot reproduce:

- Under the hypothesis-specs umbrella, the effort's own spec campaigns
  were stopped by the overturn question three times, after one, one and
  two panel rounds. Nothing the later phases found overturned a major
  mechanism: seven MAJORs came after the stops, each closed by one fix
  wave; one reshaped a decision, a widening the mandatory branch review
  caught; and every post-stop spec-level MAJOR whose origin could be
  traced was drift from a recent fix. The contrast case, umbrella-specs,
  ran four rounds under the earlier trigger: rounds 1–3 each overturned
  a mechanism, no readout foresaw the next, and the gap that escaped, a
  rule whose trigger never fires, is one the overturn question does not
  judge.
- Across 109 features' histories on crucible and one other project
  (2026-10-28), branch reviews staked a BLOCKER or MAJOR on 41% of
  very-small lanes against 24% of planned routes, and caught both
  premise-level MAJORs that task reviews let through; on one project a
  small change on the full route cost about 36 million input-equivalent
  tokens against about 10.6 million for five fixes in a direct-fix
  session (§ The very-small lane).

Limits: three stops, all prose changes to crucible's own skills, with
no counterfactual; the controller made each stop call and wrote the
readout justifying it, and terminal passes found readouts shaded toward
done in all four campaigns, one stop basis among them overstated. No
probe bears on whether a feature with no review before code ships
worse; the branch review is where its cost lands. (Basis: measured, for
the probes; judgment, accepted by the maintainer, for the answer.)

### The very-small lane

Measured on crucible's runs on one project (2026-09-27), in
input-equivalent tokens (input 1×, cache write 1.25×, cache read 0.1×,
output 5×): a small mechanical change on the full route, a 700-line spec
with its campaign, per-task review and branch review, cost about 36
million, 23% of it implementation; a direct-fix session with no spec and
an iterated branch review landed five fixes for about 10.6 million, and
its first scoped re-review caught a major defect the first fix had left
open. So for a change with nothing left to decide before code, the diff
is the review object and the branch-review loop iterates on it to its
severity floor. The comparison offers no counterfactual for what a spec
round would have caught. (Basis: measured.)

The note binds through its intent, acceptance and out of scope; a
departure from its change list is logged, and a Lane Fit verdict of
EXCEEDS SHAPE is an operator decision ask: stay, or move to the standard
route, never to the folded one, whose entry comes before any artifact is
written. The note and the lane's ledger carry a `Lane: very-small` line.
(Basis: judgment, accepted by the maintainer.)

Nothing checked the lane's goal premise, whether the note's Intent is
what was asked. The maintainer found it "especially concerning for the
very-small, where we don't have independent review of the premises, but
it doesn't seem worth to introduce a redteam round" (2026-10-28). Lane
Fit gained the goal check beside its other verdict, read against the
note's quoted request
(`docs/decisions/evidence-and-findings.md`): an agent's proposal, which
the maintainer accepted. (Basis: the maintainer's preference, for the
aim; judgment, accepted by the maintainer, for the form.)

The note and the lane proposal share one gate (2026-10-07): a separate
gate re-presented decisions just made and never showed the note whose
acceptance binds the reviewer. (Basis: judgment, accepted by the
maintainer.)

### The waiver

A trivial change is a typo, a comment or wording the operator dictated;
if the work turns out larger, the agent stops and returns to the
operator. The maintainer's ruling of 2026-10-07 chose an offered waiver
over two alternatives: no route for trivial edits at all, which keeps
the overhead, and an agent-declared route, which hands the agent the
judgment the router exists to check. On 2026-10-12 brainstorming's hard
gate was left as written: the waiver is offered before brainstorming
loads, and the router's precedence line ranks the operator's yes above
any skill. The waiver is unmeasured. (Basis: the maintainer's preference,
for the ruling; judgment, accepted by the maintainer, for the hard
gate.)

## Rejected

- **One uniform process for every change**: on a small change the plan
  document, not the review, was the disproportionate part, and a change
  with nothing left to decide before code is best reviewed as its diff
  (§ Why).
- **Choosing a preset by file or line counts**: the risk is an
  unsettled mechanism, which a count does not measure.
- **The shape test**, and the split of the small routes by whether a
  decision deserved review before code: both measured size, not risk;
  and the overturn question beside a blast-radius limit or beside the
  shape test (§ Why).
- **The choices as fields with no presets, or the routes plus two
  toggles** (§ Why).
- **A separate gate for the lane note** (§ Why).
- **No route for trivial edits, or an agent-declared one** (§ Why).

## What a project may change

The waiver never skips the project's own rules, worktrees and tests
included. The operator's instruction files and direct requests outrank
the skills (the router's precedence line), so a project can rule out a
small preset or the waiver for its work.

## Changes

- 2026-10-29: the routes became presets over four choices, each made
  where its information exists, the step-4 proposal naming a preset and
  the route entry written for every preset; the overturn question
  replaced the shape test and the "worth reviewing" split as the
  selector, and Lane Fit asks it of the diff; the origin question's
  answer is recorded with its evidence and limits; after the
  maintainer's observation that the choices need not align and proposal
  of the overturn criterion.
- 2026-10-29: the lane note carries the request, and the branch
  reviewer's Lane Fit checks the note's Intent against it beside the
  shape check and rules on a dispatched implementer's leads; after the
  maintainer's concern that the lane's premises had no independent
  review.
- 2026-10-28: an umbrella takes none of the three routes, since it has
  no plan or code of its own; its review follows what it carries, and
  its children take routes of their own.
- 2026-10-13: the folded lane: spec and plan in one document, every
  review instrument unchanged, the route known from `folded.md` and the
  decision record.
- 2026-10-12: the very-small lane: a frozen lane note, review moved to
  the diff, the repository's own gates.
- 2026-10-12: the trivial-edit waiver, offered by the router before
  brainstorming loads.
