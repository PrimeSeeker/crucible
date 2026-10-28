# Hypothesis specs: review after code, wider seat voice, separable arrangements

## Intent

**Problem.** In the maintainer's assessment, crucible spends most of its
review before implementation, on artifacts that are harder to reason
about than code, and its later campaign rounds mostly fix wording and
the drift earlier fixes brought in. On crucible's own umbrella-specs
feature (2026-10-28), four spec rounds and a terminal pass missed the
one structural gap; an implementer and the branch review found it
(`docs/backlog/campaign-early-stop-investigation.md`). The same item
records the counter-evidence: a recount of past campaigns found
stopping earlier as untested as stopping later, and at least 7 of 75
stop calls overturned, reopened or flagged `CONCLUSION-CHANGING`.

Its seats meanwhile grade mostly against the spec as given. Some room
exists: the spec contract holds unmarked decisions lightly
(`skills/brainstorming/SKILL.md` § Spec contract), and redteam seats
have a `## Questions` section and may find that a binding item is
itself wrong (`skills/redteaming/seat-prompt.md`). What is missing:

- The maintainer judges [LOAD-BEARING] marks to be used too liberally;
  `docs/backlog/load-bearing-marks-audit.md` counts 0 to 7 per recent
  feature and has not counted how often one bound anything. Brainstorming
  records an operator's answer as settled (`skills/brainstorming/SKILL.md`
  § Workspace provisioning (brainstorm exit)), while most such answers
  mean "no strong preference; this until new evidence arrives".
- The branch reviewer cites file:line for every finding and its output
  format has no section for questions
  (`skills/requesting-code-review/code-reviewer.md` § Calibration,
  § Output Format), so a doubt about the premise has no form to take.
- Improvements and style are not findings for any reviewer
  (`docs/backlog/review-improvements.md`).
- No seat sees the operator's original request, and no step records
  it, so none can check the spec's Intent against what was asked for.

The arrangement choices (review before implementation and its width,
the plan's form, per-task review, direct or subagent execution) are
correlated but need not always align, in the maintainer's observation;
the three routes fix them together.

The very-small lane runs no review before code. On it, the branch
reviewer's Lane Fit section checks one premise, that the change keeps
the lane's qualifying shape, and an EXCEEDS SHAPE statement opens the
upgrade hatch (`skills/requesting-code-review/code-reviewer.md`,
`skills/subagent-driven-development/references/very-small-lane.md`).
Nothing checks the goal premise: whether the note's Intent is what was
asked. The effort began with that question: is routing features with
potentially non-trivial impact through the very-small lane sound?

**Goals.**

- **G1.** Answer the origin question: when a feature with non-trivial
  impact may take the very-small lane; and give the lane an independent
  check of its goal premise, extending the existing Lane Fit check.
- **G2.** Move review load from artifacts to code wherever overturning
  a major mechanism after implementation is unlikely.
- **G3.** Let seats and implementers say that the spec, or the goal
  behind it, is wrong, and voice misgivings with no specific issue to
  point to, without either costing a fix wave.
- **G4.** Record approvals as lightly held by default, as the spec
  contract already holds unmarked decisions; a mark names what builds
  on the decision it marks.
- **G5.** Make the arrangement choices separable.

**Non-goals.**

- A premise-level finding mandate for task reviewers. They share the
  non-finding channels (U4, and improvements as `seat-voice` settles
  them); their mandate changes only if `seat-voice`'s probes show it
  filtering out problems it could see.
- A redteam round on the very-small lane.
- A standing measurement or calibration programme. One-off probes inside
  a child, such as `seat-voice`'s, are not one.
- The skill-text rewrite (`docs/backlog/skill-text-rewrite.md`) and the
  umbrella follow-ups (`docs/backlog/umbrella-followups.md`), which stay
  separate items.
- The backlog follow-ups no entry below names, which stay in the
  backlog: the digest at the first round close and caps as cost bounds
  (`docs/backlog/lane-entry-and-downshift.md`),
  `docs/backlog/decision-ask-framing.md` and
  `docs/backlog/reviewer-research-reach.md`.

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
  before implementation. Basis: the maintainer's proposed trigger,
  adopted as a hypothesis under U1; the recount above neither supports
  nor refutes it.
- **U4. Doubts without a specific issue are an output of their own.**
  They are not findings: no severity, no fix wave, and none is the
  normal case. Basis: the maintainer's proposal ("your intents don't
  mean what you seem to think they do" is not a finding, but
  potentially useful).
- **U5. Size is tracked, not capped.** Each child's landing states its
  net word change to the skills, from `tests/prose-budget.txt`, and what
  it removed; the effort's total is the sum of the children's figures.
  Nothing is triggered by it. Basis: the maintainer's ruling,
  with wide priors on this effort's natural size.
- **U6. This effort applies U3 now.** Its own campaigns stop once
  overturning a major mechanism is no longer plausible, ahead of
  `arrangements` writing it into the process; the round readout's
  statement of whether the round drove structural change carries that
  judgment and its reason. Until the installs carry `seat-voice`'s
  premise check (U8), the existing full-scope branch review is the only
  safeguard after code: the risk the maintainer accepted with the waiver
  and confirmed as an exception to C1. Basis: the maintainer's waiver.
- **U7. The arrangement choices become separable.** Review before
  implementation and its width, the plan's form, per-task review, and
  direct or subagent execution are chosen per feature rather than fixed
  together by a route. The form (presets over the choices, fields of
  the step-4 route proposal, or another) is `arrangements`'s to choose.
  Basis: the maintainer's proposal ("several separate decisions …
  correlated, but don't have to be always aligned").
- **U8. Each child runs under its predecessors' rules.** Before a
  child's brainstorm, the maintainer's installs carry every child landed
  before it; "waits on" in the Children list means landed and installed.
  The means is open: a release, a pre-release on the existing channel
  (`docs/dual-runtime.md` § Release metadata), or installs tracking a
  long-lived effort branch. A host fetches a new copy only when the
  version changes, so each means bumps the version. Basis: the
  maintainer's ruling after the umbrella's first review round, and their
  note that nothing forces a release.

## Constraints & invariants

- **C1.** The branch review stays mandatory on every arrangement, at
  full scope, and, once the installs carry `seat-voice`'s premise check,
  with that check; `arrangements` may make any other review
  optional, never this one. Pre-implementation review shrinks only
  because the review after code stays and widens, with one exception:
  under U6 this effort's own campaigns shrink it before then.

## Interfaces & boundaries

- **`binding-and-marks` provides** what binds a seat under U1, the
  correction path for a spec shown wrong, and how strongly an approval
  is recorded. `seat-voice` consumes the first two: what its seats
  grade against, and what a premise-level finding can lead to.
  `arrangements` consumes the correction path as the safety valve for
  stopping review early.
- **`seat-voice` provides** the U4 channel, the premise-level mandate
  at the branch review on every arrangement, the operator's request
  quoted in the spec or lane note, and the improvements ruling.
  `arrangements` consumes the branch review's premise check as the
  condition for lightening review before implementation, so G1 is the
  two children's joint result.
- **Shared files.** All three children edit the same skills (the
  reviewer templates, subagent-driven-development, the lane references,
  brainstorming). They run in order, each brainstormed from a base that
  holds its predecessors (U8).

## Acceptance

The Children list, in order:

- `binding-and-marks` — what binds a seat under U1; a correction path
  for a spec that code shows wrong, routine, recorded and lighter than a
  supersede; guidance for [LOAD-BEARING] marks per U2; how strongly an
  approval is recorded, in the brainstorm decision record and in
  `docs/decisions/`; decision-record tasks take the brainstorm decision
  record as an input. Takes up `docs/backlog/load-bearing-marks-audit.md`,
  its count done in context gathering or dropped, as the child's
  brainstorm decides, and the decision-record follow-up of
  `docs/backlog/review-catch-and-implementers.md`.
  Waits on nothing.

- `seat-voice` — first two one-off probes: a differential probe, one
  fresh default-role seat with no rubric on 6–10 past task reviews that
  came back clean or with only minors, from crucible and from one other
  project, the latter reported as aggregate figures only; and an escape
  analysis of later fixes on git history. Then: a premise-level mandate
  for the branch review on every arrangement and for redteam seats,
  extending what exists (seats' Questions, Lane Fit, a binding item
  found wrong) rather than adding beside it, such findings reaching the
  operator as decision asks without opening a fix wave; the operator's
  request, quoted verbatim in the spec or lane note itself, where every
  seat already reads it (a part the no-local-context rule keeps out of a
  public repository is redacted, saying so), for an independent
  restatement of the goal, the request being evidence and not the
  standard (a seat may find the request itself wrong); the U4 channel
  across seats, task reviewers and implementers, a few items at most
  per seat, reaching the operator
  through a readout or the branch review, a task reviewer's going to the
  branch reviewer as leads; the format barriers (file:line on every
  finding, the branch reviewer's missing question section); the
  improvements ruling; implementers' standing; a trace check for rules
  tied to a trigger. Task reviewers' mandate changes only on the probes'
  evidence. Takes up `docs/backlog/review-improvements.md` and the
  trace-check and implementers'-standing follow-ups of
  `review-catch-and-implementers.md`. Waits on `binding-and-marks`.

- `arrangements` — the arrangement choices made separable per U7, in a
  form the child chooses, with the invalid combinations stated and the
  existing routes re-expressed in its terms; the controller proposes an
  arrangement naming its departures from the usual one, and the operator
  confirms; U3 as the selector and the stop trigger, and how it relates
  to the very-small lane's current qualifying shape; the origin
  question's answer recorded in `docs/decisions/`, closing G1; the
  folded lane kept, absorbed or retired; per-task review as a plan
  choice. Takes up `docs/backlog/campaign-early-stop-investigation.md`,
  the downshift follow-up of `lane-entry-and-downshift.md` and the
  per-task-review follow-up of `review-catch-and-implementers.md`.
  Waits on `seat-voice`.

Each child's own Acceptance carries the checks. A child taking up a
backlog item resolves it or trims it to what stays open, and its spec
says which follow-ups it closes; an item shared between children is
trimmed by each, and deleted once nothing in it stays open.

## Mechanism sketches

None at umbrella level: design detail is each child's, in its entry and
its own spec.
