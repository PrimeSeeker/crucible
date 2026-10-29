# Arrangements: separable choices, the overturn question as selector and stop

Umbrella: `docs/crucible/2026-10-28-hypothesis-specs/umbrella.md`

## Request

The umbrella carries no request block of its own, so the effort's
request is quoted here whole, as evidence of what was asked for, not as
the standard. The opening message (2026-10-28):

> OK, the next one is big, but it seems to me that its various strands
> are intertwined, and it's better to address it now
>
> 1) I believe that, generally, reasoning about the existing or
> in-progress code is easier than about planned one. We seem to spend an
> awful lot of time planning, especially on smaller features, and the
> last rounds seem to be dedicated to fixing compact errors. I believe we
> could shift this load to the "after" review, with the criterion like
> "do we reasonably expect major mechanisms to be overturned further down
> the line?" (additions or smaller correctrions are OK). It probably also
> should be used as the primary very-small trigger - say, for lack of
> major mechanisms, or overdetermined decisions
>
> 2) We would probably need to explicitly state the assumption that the
> spec is likely subtly flawed (and almost certainly has some local
> errors as well, given that we're trying to stop redteaming early)
> throughout the process. Given the occasional "doesn't actually launch"
> issues (OK, that was quite a while ago, but still), it's probably not
> far from the truth, and it's likely to be a useful frame
>
> 3) I think the reviewer agents have a narrower mandate (they're still
> evolved from normal code review, after all) than the redteaming ones,
> and we should extend it to parity. I don't expect broad corrections to
> trigger often, but that's the last line of defense (maybe only
> full-branch, rather than task reviews?). Especially concerning for the
> very-small, where we don't have independent review of the premises, but
> it doesn't seem worth to introduce a redteam round
>
> 4) It feels to me that redteaming operates with too much human
> deference and/or narrow mandate as well. I'm not aiming precisely for
> the "wrong problem using the wrong methods based on a wrong model of the
> world", but it'd be directionally useful (maybe something something
> assume incomplete goal factoring?). Generally, I wonder if we could get
> agents to cast "it doesn't smell right" of various kinds in calibrated
> manner
>
> 5) Probably more proactivity throughout the process? I believe we
> disallowed improvement suggestions, for example.
>
> I suppose I'm missing something logically connected here. Also, might
> be worth checking if we have more relevant backlog items
>
> Thoughts?

and the reply that changed what was asked (same day):

> 1-3: Yes, agreed
> 4: Calibration is not the key point here (probably I'm consuming too
> much rationalism), the idea is - can we have the process to detect that
> things aren't right when there is no specific issue to point to, in a
> sensible manner? Say, something like "your intents don't mean what you
> seem to think they do" is not a finding in a normal sense, but
> potentially useful
> 5: OK
> 6: Not sure if it fits here, but maybe we could be more flexible with
> arrangements. We've got several separate decisions (redteaming usage
> and then width, separate/folded plan and possibly per-task review
> usage, direct/subagent execution) that are correlated, but don't have
> to be always aligned
> Also of note: we might want to extend the lightly-held stance. Most of
> my approvals are shaped like "no strong preference, let's go with this
> until new evidence arrives" (and then occasionally become design
> pillars), seems like load-bearing marks are used too liberally and
> result in bureaucracy
>
> Agreed with an umbrella
>
> Yes, this plan. I started with "is routing features with potentially
> non-trivial impacts through very small lane sound?", and then the
> (meta?)-feature expanded by association

This child takes up point 1, the reply's point 6 and the origin question
of its last paragraph. In this child's own brainstorm (2026-10-29), one
message changed what was asked of it:

> On inline execution - now is a good moment, actually. We probably
> don't want to expand inline execution "much"; I'm not sure what
> constitutes it. Pros are cost and speed (there mork work there is, the
> less important overhead becomes), the con is expected quality (fresh
> eyes, fresh context). There are cases where spinning up a subagent is
> obviously unwise, but I don't see a clear separating criterion
>
> Agreed on form

This feature's own entry in the umbrella states what it must deliver.

## Intent

**Problem.** A route fixes four choices together: review before code
and its width, the plan's form, per-task review, and inline or subagent
execution (umbrella U7). The tests that choose between routes measure
size, not risk:

- The two small routes qualify by shape — no new mechanism, no blast
  radius across subsystems, no change to [LOAD-BEARING] content
  (`skills/brainstorming/SKILL.md` § The folded lane — proposing the
  fold, § The very-small lane — proposing the lane) — and are told apart
  by whether a design decision is "worth reviewing before code". A
  change with non-trivial impact whose mechanism is already settled is
  sent to a campaign for its size.
- The spec campaign stops at "the first round producing zero BLOCKERs
  and no structural finding" (`skills/redteaming/SKILL.md` § Stop rule
  and terminal pass), so a round spent repairing the drift of the last
  round's fixes keeps the campaign going. On one project, 60–90% of
  the findings of rounds 2 and later were introduced by the
  previous round's fixes (`docs/backlog/campaign-early-stop-investigation.md`).
- Every task gets a task review (`skills/subagent-driven-development/SKILL.md`
  § The Task Loop, step 3: "Never skip it"). On prose tasks run in
  sequence on shared files they catch little: on crucible's
  umbrella-specs feature the five task reviews approved everything while
  the implementers' concerns and the branch review found what mattered
  (`docs/backlog/review-catch-and-implementers.md`).
- Inline execution has no stated criterion: inline mode is for "a small
  mechanical task where a dispatch costs more than it protects", and the
  very-small lane dispatches an implementer where the change is "wide
  enough to crowd your context"
  (`skills/subagent-driven-development/SKILL.md` § Inline mode;
  `skills/subagent-driven-development/references/very-small-lane.md`).
- No arrangement can move down once chosen; the very-small lane can
  only move up (`docs/backlog/lane-entry-and-downshift.md`).

**Evidence.** Two context-gathering probes on crucible's own runs, read
from records outside this repository (session transcripts, the
repository crucible was developed in before its move here, and one
other project's feature folders); their figures are aggregates this
tree cannot reproduce:

- *U6's track record.* This effort stopped its own campaigns by the
  overturn question (umbrella U6) three times, after one, one and two
  panel rounds. Nothing the later phases found overturned a major
  mechanism: seven MAJORs after the stops, each closed by one fix wave;
  one reshaped a decision (a widening the mandatory branch review
  caught); every post-stop spec-level MAJOR whose origin could be traced
  was drift from a recent fix. The contrast case, umbrella-specs, ran
  four rounds under the current trigger; rounds 1–3 each overturned a
  mechanism, no readout foresaw the next, and the gap that escaped — a
  rule whose trigger never fires — is one the overturn question does
  not judge. Limits: three stops, all prose changes to crucible's skills,
  no counterfactual; the controller made each stop call and wrote the
  readout justifying it, and terminal passes found readouts shaded toward
  done in all four campaigns, one stop basis among them overstated.
- *The lane's cost and catch.* On one project, a small change on the
  full route cost about 36 million input-equivalent tokens, and a
  direct-fix session with an iterated branch review landed five fixes for
  about 10.6 million (`docs/decisions/routes.md`). Across 109 features'
  histories on crucible and one other project (2026-10-28), branch
  reviews staked a BLOCKER or MAJOR on 41% of very-small lanes against
  24% of planned routes, and caught both premise-level MAJORs the task reviews
  let through (`docs/crucible/2026-10-29-seat-voice/design.md` § Intent).
  No probe bears on whether a feature with no review before code ships
  worse; the branch review is where its cost lands.

**Goals.**

- **G1.** The four choices are separable, each made where its
  information exists, and the existing routes are presets over them.
- **G2.** The overturn question — after code, is overturning a major
  mechanism plausible? — selects review before code and stops the spec
  campaign.
- **G3.** The origin question is answered and recorded: when a feature
  with non-trivial impact may skip review before code.
- **G4.** A plan may route a task's review to the branch review alone,
  with nothing the task review checked left without an owner.
- **G5.** A stated criterion separates inline from subagent execution,
  expanding neither default.
- **G6.** An operator-confirmed way down exists where one is cheap.

**Non-goals.**

- Skipping the plan after a campaign, implementing from the spec
  lane-style: left out by the maintainer's ruling (2026-10-29); D2 now
  produces its case, a settled change that needs several tasks, which
  the backlog item names as its trigger. It is added to
  `docs/backlog/lane-entry-and-downshift.md`, beside that item's digest
  follow-up.
- Retiring the folded preset: in steady use, about nineteen features
  on crucible before its move to this repository and on one other
  project; whether the overturn question
  leaves it a niche is for later.
- New verdict tokens, ledger forms or file roles for the existing
  routes.
- A change to the task reviewer's or branch reviewer's mandate beyond
  what D4 and D12 state.
- Expanding inline execution: the maintainer's ruling of 2026-10-27,
  "not extended for now"
  (`docs/crucible/2026-10-27-upstream-review/dispositions.md`).
- The skill-text rewrite (`docs/backlog/skill-text-rewrite.md`).

## Decisions

All lightly held. Basis tags follow `docs/decisions/decision-records.md`.

- **D1. Four choices, three presets.** The choices are review before
  code (a spec campaign, or none), the plan's form (separate with its
  plan phase, folded into the spec, or none), per-task review (every
  task, or the branch review alone), and execution (inline or subagent);
  the branch review is no choice (umbrella C1). The routes stay as
  presets, standard the usual one:

  | Preset | Review before code | Plan | Per-task review | Execution |
  |---|---|---|---|---|
  | standard | campaign | separate, plan phase | per task, the plan's call (D10) | per task (D14) |
  | folded | campaign | folded, no plan phase | per task, the plan's call | per task |
  | very-small | none: a lane note | none: the note's change list | none | inline by default (D14) |

  Each choice is made where its information exists: the preset at step 4,
  per-task review in the plan, execution per task. Review's width — a
  campaign's seats and rounds — stays where it is chosen today: the
  campaign shape approved at the digest gate, and the stop rule (D6). Unsupported, each for
  the reason given: per-task review with no plan (no tasks); a plan phase
  without a separate plan; a campaign on a lane note (the umbrella's
  non-goal); a spec with no campaign (write a note); a note with a plan,
  or a spec with no plan (no case on record); any arrangement without the
  branch review. Basis: the maintainer's preference (the reply's point 6),
  for separability; judgment, accepted by the maintainer, for presets
  over fields.

- **D2. The overturn question selects review before code.** At step 4,
  review before code is chosen where overturning a major mechanism after
  code is plausible, and none where it is not: the design has no major
  mechanism, or its decisions are overdetermined (both defined in the
  arrangement questions' home, Interfaces). The question replaces both
  the small routes' shape test and the "design decision worth reviewing"
  split. Between the two campaign presets, folded fits a plan of one or
  two tasks with no seam worth its own review; standard fits the rest. A
  folded feature stays a minor design, with no digest: its plan is small
  enough that the decision record's list, presented inline at the digest
  gate, steers it. An umbrella's review stays chosen by its content
  (`skills/brainstorming/references/umbrellas.md` § Review), since it has
  no code of its own to review after.
  Width is no test of risk, since the branch review reads the whole diff
  whatever its width, but it still shapes the arrangement where the work
  needs coordinating: a settled change one implementer can carry takes
  the very-small preset with a dispatched implementer (D14); one that
  needs several coordinated tasks needs a plan, which only the campaign
  presets carry, so it takes the standard preset, whose campaign the
  overturn question then stops after its first round. The [LOAD-BEARING]
  clause is dropped: shipped specs are frozen, and under an umbrella a
  change to its marks is already a binding change with its own path; the
  residual — a lane outside any umbrella changing what another feature in
  flight builds on — is accepted as rare and visible at the merge. Basis:
  the maintainer's preference (opening point 1: "the primary very-small
  trigger - say, for lack of major mechanisms, or overdetermined
  decisions"), for the selector; judgment, accepted by the maintainer,
  for the rest.

- **D3. The step-4 proposal.** One brainstorming subsection, "proposing
  the arrangement", replaces the two route-entry subsections: it holds
  D1's table and unsupported list, and the proposal names a preset, the
  overturn answer with its reason and, for folded, the plan-size reason.
  A departure expected only later ("most tasks will likely be
  branch-review-only") is a heads-up, not confirmed. The operator's
  answer is a route entry in the brainstorm decision record, now written
  for every preset, in the form the fold's and the lane's take today. What stays route-specific stays: the very-small lane's note shown
  with the proposal and written as approved; no entry mid-flight, the
  downshifts of D13 and the lane's upgrade hatch aside. This clarifies
  the umbrella entry's "the operator confirms": the operator confirms the
  preset; per-task review is the plan's, reported (D10), and execution is
  chosen per task (D14). The clarification changes nothing another
  entry waits on. Basis: judgment, accepted by the maintainer.

- **D4. Lane Fit after code.** The branch reviewer's Lane Fit keeps its
  verdict words WITHIN SHAPE and EXCEEDS SHAPE
  (`skills/requesting-code-review/code-reviewer.md`); "shape" becomes the
  overturn question asked after code: EXCEEDS SHAPE where overturning a
  major mechanism of the change is plausible, one the note states
  included. EXCEEDS SHAPE opens the upgrade hatch as now (the
  upgrade-hatch paragraph of
  `skills/subagent-driven-development/references/very-small-lane.md`,
  which reads it as a statement that the change "exceeds the lane's
  qualifying shape"). Basis: judgment, accepted by the maintainer.

- **D5. The origin question's answer.** Routing a feature with
  non-trivial impact to no review before code is sound, a hypothesis
  like D6, where the overturn question answers no at step 4, because the mandatory
  full-scope branch review, with its goal and premise checks, is the
  independent check; size is not the risk, an unsettled mechanism is. It
  is recorded in `docs/decisions/routes.md` with its evidence and limits
  (§ Intent). Basis: judgment, accepted by the maintainer.

- **D6. The stop trigger is the overturn question.** A spec campaign
  stops after the first numbered panel round once overturning a major
  mechanism after code is no longer plausible: the controller's judgment
  over the round's records, the seats' forecast lines (D7) included.
  Severity leaves the trigger: the stop round's open findings of any
  severity, premise findings aside, take the existing one fix wave with
  blind verification, and the terminal pass's re-read backstops it; a
  BLOCKER that would overturn a mechanism keeps the campaign going by
  the question itself. A round whose own fix wave adds, removes or
  re-shapes a major mechanism is not the stop round: no seat has read
  the result. Once a campaign is chosen, at least one numbered panel
  round runs. Basis: the maintainer's preference (opening point 1),
  adopted as a hypothesis with no demonstrated accuracy (§ Intent).

- **D7. The seats forecast; the terminal pass checks the stop.** In a
  spec campaign, every panel seat's `## Verdict` carries a second line,
  `Overturn after code: plausible — <which mechanism, why>` or `Overturn
  after code: not plausible`. The round readout's structural item
  becomes whether overturning a major mechanism after code is still
  plausible, and why, answering each plausible forecast by the mechanism
  it names, the seats' ids kept to the readout's trace; it is stated in
  every numbered spec-campaign round. The terminal pass's decision-ask
  fidelity mandate also checks the stop: the stated basis against the
  stop round's forecast lines, its inputs gaining that round's seat
  reports, their `## Verdict` sections only, and the stop round's fix
  list against D6's re-shape rule. A mismatch that would have changed
  the stop is flagged `CONCLUSION-CHANGING`, a decision ask by the
  existing rule. Basis: judgment, accepted by the maintainer, after the
  U6 probe found the stop caller writing its own justification.

- **D8. The cap.** The cap stays at four rounds, its termination
  guarantee; at the cap, a still-plausible overturn goes to the operator
  as the existing cap ask (another round, supersede, accept with parked
  rulings). Beside it: the cap bounds rounds, not spend. That sentence is the
  second half of the downshift follow-up this child takes up; the
  umbrella's Intent lists "caps as cost bounds" among the follow-ups
  staying in the backlog, and this child drops those words from it, a
  lightly held edit to the umbrella's Intent riding this branch. Basis:
  judgment, accepted by the maintainer.

- **D9. "Structural" keeps its other work.** The word stays where it
  does work beyond the stop: the flip paths' supersede and containment
  (`skills/redteaming/references/flip-paths.md`). Four sites tie it to
  the stop and are re-expressed: a premise ruling's change that re-shapes
  a mechanism "makes its round structural" (the same file, § Premise
  findings), which becomes a change that makes an overturn plausible
  again; the folded preset's unfolding, judged today "under the stop
  rule's structural vocabulary" (the unfolding paragraph of
  `skills/redteaming/references/folded-lane.md`), judged instead by
  whether the work turns out to need a separate plan; the panel
  calibration's "post-structural-stability rounds"
  (`skills/redteaming/SKILL.md` § Panels), which become rounds that read
  a re-shaping wave's result (D6), 1–2 seats; and "any non-structural
  BLOCKER/MAJOR at the cap" (the same file, § Stop rule and terminal
  pass), which becomes any BLOCKER or MAJOR still open at the cap. The
  README's paraphrase of the trigger is corrected with them (D15).
  Basis: judgment, accepted by the maintainer.

- **D10. The plan's per-task mark.** A plan task may carry the line
  `Review: branch only — <reason>` where it meets the mark's criterion:
  low in mechanism, with nothing outside it depending on its details
  (defined in the arrangement questions' home, Interfaces); with no mark,
  the task is reviewed. The mark applies to a dispatched task: a task
  done inline (D14) keeps its task review whatever its mark, as inline
  mode states today. The seats that grade the plan grade marks as plan
  content — the plan phase's, or on the folded preset the spec
  campaign's — and that phase's close readout lists the marked tasks for
  the operator, as information. The asymmetry with D13 is deliberate:
  marks written at plan time pass that review, while marks added later
  change a reviewed plan. Basis: judgment, accepted by the maintainer
  (the per-task-review follow-up of
  `docs/backlog/review-catch-and-implementers.md`, agreed 2026-10-28).

- **D11. A marked task in execution.** It runs no task review and no fix
  loop. Its verification gates run, widened to what the report must
  show: each acceptance check, RED output before GREEN or a logged
  exception, and a Decision Log entry for each deferred item the plan
  routes to it. The implementer's concerns, `Questions` items and
  out-of-task proposals become leads for the branch reviewer; its
  premise finding goes where it goes now. Where a concern touches
  something a later task builds on, the controller dispatches the marked
  task's own review after all, and the task runs the task loop from
  step 3. Every site stating that each task gets a task review, tying
  routed items to it or expecting its report files is corrected: in SDD
  (the task loop, and § Finish's per-task record check, which expects no
  review file for a task completed branch review only), writing-plans
  (§ Task sizing's reviewer-gate rationale included), requesting-code-review,
  the implementer's template (its routed-item paragraph), the task
  reviewer's card and the branch reviewer's template. Basis: judgment,
  accepted by the maintainer.

- **D12. The branch reviewer learns which tasks went unreviewed.** It
  receives the tasks completed branch-review-only (Interfaces) and is the
  first review of each: the task review's judgments over the task's range
  — intent, scope (a deleted or weakened test against the Decision Log
  included), the deviation audit of its Decision Log, quality — and, for
  a task that writes a decision record, each position's basis against
  the brainstorm decision record; it rules on the task's leads as now.
  Routed items still open reach it through the existing sweep, and drift
  reaches revert-and-replan through the existing path. Basis: judgment,
  accepted by the maintainer.

- **D13. Downshifts.** One is the operator's to confirm: marking tasks
  that have not run `Review: branch only`, a plan patch put to the
  operator as a decision ask, never a contained amendment of the
  controller's: its home is the containment test's list of changes that
  are never contained (`skills/redteaming/references/flip-paths.md`
  § The containment test). The campaign stop (D6) also lightens review, and stays
  the controller's call under the stop rule, reported in the readout and
  checked by the terminal pass (D7). Otherwise the arrangement stays as
  confirmed at step 4. Basis: judgment, accepted by the maintainer.

- **D14. The inline criterion.** On the campaign presets, a task is
  worked inline only where it is overdetermined (the arrangement
  questions' home, the sense D2 uses) and fits the controller's remaining
  context without pushing out coordination state before the branch
  review; otherwise it is dispatched. On the very-small lane, whose
  change the step-4 answer already found settled, the context test alone
  decides: inline by default, an implementer dispatched where the work
  would crowd the controller's context. It replaces inline mode's "costs
  more than it protects" and the lane's "wide enough to crowd your
  context". Defaults are unchanged: subagents on the campaign presets,
  inline on the lane. The lane's branch-review fix waves stay the
  controller's, as today, whatever the change's width: a residual
  accepted, since a lane change is one implementer's worth (D2) and its
  waves are smaller. What a dispatched implementer buys is an
  independent read of the spec before code, worth more as review before
  code shrinks, and the controller's context. Basis: judgment, accepted
  by the maintainer ("OK, I guess").

- **D15. Records and backlog.** The decision records `routes.md`,
  `spec-campaign.md`, `task-loop.md`, `branch-review.md` and `plans.md`
  take these positions with their bases; other records and the README
  are corrected where they state what changed, `umbrellas.md`'s
  rationale for review by content among them (it cites the retired
  "worth reviewing" line).
  `docs/backlog/review-catch-and-implementers.md` is deleted;
  `docs/backlog/lane-entry-and-downshift.md` keeps the digest follow-up,
  drops the downshift and caps sentence, and gains the plan-skip path
  with its trigger (D2's settled multi-task changes); `docs/backlog/campaign-early-stop-investigation.md`
  keeps three research questions — whether a multi-round campaign is
  net-positive, fix altitude and deferral as drift reducers, what would
  settle the cap — and drops the trigger question (adopted) and the
  drift-share threshold (the overturn question covers it). Basis:
  judgment, accepted by the maintainer.

## Constraints & invariants

- **C1. Every rule has one home.** D1's table and unsupported list, the
  overturn question's definition, "overdetermined" and the mark's
  criterion are each stated once; every other site points to that home.
- **C2. Existing identifiers stay.** The route entry in the brainstorm
  decision record, the lane ledger's lines, the file roles `design.md`,
  `folded.md` and `note.md`, and the verdict words WITHIN SHAPE and
  EXCEEDS SHAPE keep their names and forms: other files, and features in
  flight on older installs, read them.
- **C3. No check of the task review disappears unowned.** For a marked
  task, every check the task review performs
  (`skills/subagent-driven-development/SKILL.md` § The Task Loop, step 3,
  and the task reviewer's template) has a named owner: the controller's
  gate check for what the report must show, the branch reviewer for the
  rest.
- **C4. A downshift is never the controller's alone.** A change to the
  arrangement confirmed at step 4 is the operator's to confirm; the stop
  rule's own stop is no such change.

## Interfaces & boundaries

- **The arrangement questions** — the overturn question, how it reads
  for an umbrella's campaign (after its children's code), what
  "overdetermined" means, and the mark's criterion — defined once, in
  one new section of the shared reference
  `skills/subagent-driven-development/references/premise-and-questions.md`,
  whose opening scope sentence widens to the controllers that apply it.
  The section lists the seat template and the branch reviewer's template
  give for that file each gain it; the terminal pass reaches it through
  a plugin-root slot added to its card
  (`skills/redteaming/terminal-pass-prompt.slots.md`) and through
  § Dispatch composition's grant of the shared reference
  (`skills/redteaming/SKILL.md`), which extends to instrument
  `terminal-pass`. Consumed by brainstorming's step-4 subsection, the stop rule
  (`skills/redteaming/SKILL.md`), the seat template's forecast line, the
  terminal pass's stop check, Lane Fit
  (`skills/requesting-code-review/code-reviewer.md`), the lane
  reference, SDD § Inline mode, writing-plans' mark, and the seats
  grading a plan's marks.
- **The seat's forecast line** — produced by `skills/redteaming/seat-prompt.md`
  in seats whose artifact kind is `spec` (a folded document's included);
  consumed by the controller's stop call and the terminal pass, whose
  inputs gain the stop round's seat reports' `## Verdict` sections
  (`skills/redteaming/terminal-pass-prompt.md`, and the input list in
  `skills/redteaming/SKILL.md` § Stop rule and terminal pass). Form as
  in D7.
- **The readout item** — stated in `skills/redteaming/SKILL.md` § Round
  readout and in `skills/redteaming/references/formats.md` § Round record
  format; both sites change together.
- **The per-task mark** — produced in a plan task as its own line,
  `Review: branch only — <reason>` (`skills/writing-plans/SKILL.md`); consumed by
  the seats grading the plan, by SDD § The Task Loop, and through the
  completion line by the branch reviewer.
- **The completion line** — `Task <N>: complete (commits <base7>..<head7>,
  branch review only)`, beside the two existing forms; the resume rule
  reads it as any `complete` line.
- **The branch reviewer's new slot** — `[BRANCH_ONLY_TASKS]`, the tasks
  the ledger completed branch-review-only, each with its commit range,
  the report path of its latest attempt not reverted
  (`sdd/reports/task-<N>-report.md`, or its `-x<X>` form after
  revert-and-replan), which the slot makes readable under the reviewer's
  read scoping, and, where its plan entry names the brainstorm decision
  record, that record's path; or "none". Filled by
  `crucible:requesting-code-review` from the ledger and the plan, read by
  `skills/requesting-code-review/code-reviewer.md`, declared in
  `code-reviewer.slots.md` within the card's character budget
  (`tests/instrument_corpus.py`); `agents/` is regenerated.
- **The route entry** — the brainstorm decision record's entry for the
  confirmed preset, now written for every preset, in its existing form; read by the folded-lane and
  very-small-lane references as now.

Deferred to implementation: the wording and placement of each pointer to the arrangement questions' home.

Deferred to implementation: where in the branch reviewer's template the text for branch-review-only tasks sits.

Deferred to implementation: how the new slot fits the card's character budget — a terse rule, a trim of existing card text, or a raised budget with its reason.

## Acceptance

- **A1.** The shape test and the "worth reviewing" split are gone from
  `skills/`, `README.md` and `docs/decisions/routes.md`, its Changes
  section aside. One-time: a whitespace-normalized search, so a phrase wrapped
  across lines is found, for "no new mechanism", "blast radius across
  subsystems", "cross-subsystem blast radius" and "worth reviewing" over
  those paths and `docs/decisions/umbrellas.md`, quoted, run before (hits) and after (none in
  that sense).
- **A2.** D1's table and unsupported list, the overturn question's
  definition, "overdetermined" and the mark's criterion each have one
  home (C1). One-time:
  a search for a key phrase of each, quoted.
- **A3.** The stop rule states the overturn trigger, the old trigger's
  phrase "zero BLOCKERs and no structural finding" is gone, and the
  readout item reads the same at both its sites. One-time: a
  whitespace-normalized search over `skills/`, `docs/decisions/` (Changes
  sections aside) and `README.md`, before (hits) and after (none); and a
  search for "structural" over `skills/redteaming/` and `README.md`, each
  hit kept by D9 or re-expressed, quoted.
- **A4.** The seat template asks for the forecast line in spec-campaign
  seats only, and the terminal pass checks the stop basis against it.
  Why neither test kind: prose fidelity, judged by review.
- **A5.** The plan mark, the marked task's handling, the completion line
  and the branch reviewer's slot are consistent across writing-plans,
  SDD, the branch-review skill, the reviewer template and its card.
  Standing: the suite's slot-card and generated-agents checks
  (`python tools/instrument_agents.py check`); the rest by review.
- **A6.** C3 holds: each check the task review performs has its owner
  for a marked task. Why neither test kind: a trace judged by review,
  task by check.
- **A7.** The inline criterion replaces both phrasings. One-time: a
  search for "costs more than it protects" and "wide enough to crowd"
  over `skills/` and `docs/decisions/`, before (hits) and after (none).
- **A8.** Each changed decision record carries a Changes line; the
  backlog items match D15. One-time: the file list and a diff stat,
  quoted.
- **A9.** The suite passes, its prose budget included. Standing.
- **A10.** The landing states the net word change to the skills and what
  was removed (umbrella U5). Why neither test kind: a report.
- **A11.** `docs/decisions/routes.md` states the origin question's
  answer (D5) with its evidence and limits, closing the umbrella's G1
  with `seat-voice`'s goal check. Why neither test kind: prose, judged
  by review.

## Mechanism sketches

Advisory.

- **Step 4.** One subsection, about the size of one of the two it
  replaces: the overturn question with its two "no" cases; D1's table;
  the unsupported list; what the proposal names; then a line per preset
  pointing to what stays route-specific (the lane note drafted with the
  proposal; the folded document's reference).
- **The plan mark**, as its own line in the task:

      Review: branch only — prose in one skill, after T2; nothing later
      reads its wording

- **SDD step 2** gains the decision point: after reading a marked task's
  report, either complete it branch-review-only, writing its leads, or,
  where a concern touches what a later task builds on, go to step 3.
- **The seat's Verdict:**

      ## Verdict
      Sound for planning, two local contradictions.
      Overturn after code: not plausible

- **Size.** Removing the two shape statements and the two route-entry
  subsections' overlap should offset most of the additions; U5 tracks
  the figure.
