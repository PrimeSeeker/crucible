# Hypothesis specs: review after code, wider seat voice, separable arrangements

## Intent

**Problem.** Crucible spends most of its review before implementation,
on artifacts that are harder to reason about than code, and its later
campaign rounds mostly fix wording and the drift earlier fixes brought
in. On crucible's own umbrella-specs feature (2026-10-28), four spec
rounds and a terminal pass missed the one structural gap; an
implementer and the branch review found it
(`docs/backlog/campaign-early-stop-investigation.md`).

Its seats meanwhile grade against the spec as given:

- [LOAD-BEARING] marks are used liberally
  (`docs/backlog/load-bearing-marks-audit.md`), and brainstorming
  records an operator's answer as settled (`skills/brainstorming/SKILL.md`
  § Workspace provisioning (brainstorm exit)), while most such answers mean
  "no strong preference; this until new evidence arrives".
- The branch reviewer cites file:line for every finding and its output
  format has no section for questions
  (`skills/requesting-code-review/code-reviewer.md` § Calibration,
  § Output Format), so a doubt about the premise has no form to take.
- Improvements and style are not findings for any reviewer
  (`docs/backlog/review-improvements.md`).
- No seat sees the operator's original request, so none can check the
  spec's Intent against what was asked for.

The very-small lane runs no review before code, and nothing independent
checks its premises. The effort began with that question: is routing
features with potentially non-trivial impact through the very-small
lane sound?

**Goals.**

- **G1.** Answer the origin question: when a feature with non-trivial
  impact may take the very-small lane, and an independent check of the
  lane's premises.
- **G2.** Move review load from artifacts to code wherever overturning
  a major mechanism after implementation is unlikely.
- **G3.** Let seats and implementers say that the spec, or the goal
  behind it, is wrong, and voice misgivings with no specific issue to
  point to, without either costing a fix wave.
- **G4.** Hold decisions lightly by default; a mark names what builds on
  the decision it marks.
- **G5.** Make the arrangement choices separable, with named presets:
  review before implementation and its width, the plan's form, per-task
  review, and direct or subagent execution.

**Non-goals.**

- A premise-level finding mandate for task reviewers. They share the
  non-finding channels (U4, and improvements as `seat-voice` settles
  them); their mandate changes only if `seat-voice`'s probes show it
  filtering out problems it could see.
- A redteam round on the very-small lane.
- A measurement or calibration programme.
- The skill-text rewrite (`docs/backlog/skill-text-rewrite.md`) and the
  umbrella follow-ups (`docs/backlog/umbrella-followups.md`), which stay
  separate items.

## Decisions

All lightly held.

- **U1. The spec is a hypothesis.** Every seat, implementer and
  controller reads the spec as probably subtly wrong and certainly
  locally imperfect. Correcting it once code shows it wrong is routine
  and recorded; `binding-and-marks` defines the path and what binds
  under it. Basis: the maintainer's proposal, and the umbrella-specs run
  above, where implementers and the branch review found the gap the
  campaign missed.
- **U2. Lightly held by default.** An operator's approval is recorded as
  accepted until new evidence arrives, not as settled; a [LOAD-BEARING]
  mark names what builds on the decision it marks. Basis: the
  maintainer's observation that most approvals are of that shape, and
  that marks are used too liberally.
- **U3. The overturn question.** "After implementation, is overturning
  a major mechanism still plausible?" Additions and smaller corrections
  do not count. The question selects the arrangement and stops review
  before implementation. Basis: the maintainer's proposed trigger.
- **U4. Doubts without a specific issue are an output of their own.**
  They are not findings: no severity, no fix wave. A seat raises at most
  a few, and none is the normal case. They reach the operator through a
  readout or the branch review; a task reviewer's go to the branch
  reviewer as leads. Basis: the maintainer's proposal ("your intents
  don't mean what you seem to think they do" is not a finding, but
  potentially useful).
- **U5. Size is tracked, not capped.** Each child's spec states its net
  word change to the skills and what it removed; the Children list keeps
  the running total. Nothing is triggered by it. Basis: the maintainer's
  ruling, with wide priors on this effort's natural size.
- **U6. This effort applies U3 now.** Its own campaigns stop once
  overturning a major mechanism is no longer plausible, recording that
  judgment and its reason at each round close, ahead of `arrangements`
  writing it into the process. Basis: the maintainer's waiver.

## Constraints & invariants

- **C1.** The branch review stays mandatory on every arrangement, at
  full scope and with its premise check. Pre-implementation review
  shrinks only because the review after code stays and widens;
  `arrangements` may make any other review optional, never this one.

## Interfaces & boundaries

- **`binding-and-marks` provides** what binds a seat under U1, the
  correction path for a spec shown wrong, and how strongly an approval
  is recorded. `seat-voice` consumes the first two: what its seats
  grade against, and what a premise-level finding can lead to.
  `arrangements` consumes the correction path as the safety valve for
  stopping review early.
- **`seat-voice` provides** the misgivings channel, the premise-level
  mandate at the branch review (the very-small lane's included), the
  original request as a seat input, and the improvements ruling.
  `arrangements` consumes the branch review's premise check as the
  condition for lightening review before implementation, so G1 is the
  two children's joint result.
- **Shared files.** All three children edit the same skills (the
  reviewer templates, subagent-driven-development, the lane references,
  brainstorming). They run in order, each brainstormed from a base that
  holds its predecessors.

## Acceptance

The Children list, in order:

- `binding-and-marks` — what binds a seat under U1; a correction path
  for a spec that code shows wrong, routine, recorded and lighter than a
  supersede; guidance for [LOAD-BEARING] marks per U2; how strongly an
  approval is recorded, in the brainstorm decision record and in
  `docs/decisions/`. Takes up `docs/backlog/load-bearing-marks-audit.md`.
  Waits on nothing.

- `seat-voice` — first two probes: a differential probe, one fresh
  default-role seat with no rubric on 6–10 past task reviews that came
  back clean or with only minors, from crucible and from one other
  project, the latter reported as aggregate figures only; and an escape
  analysis of later fixes on git history. Then: a premise-level mandate
  for the branch review (the very-small lane's included) and for redteam
  seats, such findings reaching the operator as decision asks without
  opening a fix wave; the operator's original request as a seat input,
  for an independent restatement of the goal; the misgivings channel of
  U4 across seats, task reviewers and implementers included; the format
  barriers (file:line on every finding, the branch reviewer's missing
  question section); the improvements ruling; implementers' standing;
  reviewers' research reach. Task reviewers' mandate changes only on
  the probes' evidence. Takes up `docs/backlog/review-improvements.md`,
  `review-catch-and-implementers.md`, `reviewer-research-reach.md` and
  `decision-ask-framing.md`. Waits on `binding-and-marks`.

- `arrangements` — the four arrangement choices as separate settings,
  with named presets and the invalid combinations stated; the
  controller proposes a preset naming its departures and the operator
  confirms; U3 as the selector and the stop trigger; the very-small
  lane's entry test, and the origin question's answer recorded in
  `docs/decisions/`, closing G1; the folded lane kept, absorbed into a
  preset or retired; per-task review as a plan choice. Takes up
  `docs/backlog/campaign-early-stop-investigation.md` and
  `lane-entry-and-downshift.md`. Waits on `seat-voice`.

Each child's own Acceptance carries the checks. Running word total
(U5): none landed yet.
