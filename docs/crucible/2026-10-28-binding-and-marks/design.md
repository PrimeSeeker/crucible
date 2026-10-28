# Binding and marks: what binds a hypothesis spec, and how it is corrected

Umbrella: `docs/crucible/2026-10-28-hypothesis-specs/umbrella.md`

## Intent

**The request.** The maintainer's words, from the umbrella's dialogue
(2026-10-28), quoted as evidence of what was asked for:

> We would probably need to explicitly state the assumption that the spec
> is likely subtly flawed (and almost certainly has some local errors as
> well, given that we're trying to stop redteaming early) throughout the
> process. Given the occasional "doesn't actually launch" issues (OK, that
> was quite a while ago, but still), it's probably not far from the truth,
> and it's likely to be a useful frame

> Also of note: we might want to extend the lightly-held stance. Most of
> my approvals are shaped like "no strong preference, let's go with this
> until new evidence arrives" (and then occasionally become design
> pillars), seems like load-bearing marks are used too liberally and
> result in bureaucracy

This feature's own entry in the umbrella states what it must deliver.

**Problem.** Once a spec's campaign has closed, its binding content (its
Constraints & invariants and its `[LOAD-BEARING]` marks, plus the
umbrella content its umbrella line brings in) changes only through a
scoped amendment or a supersede, and both open with a decision ask to the
operator (`skills/redteaming/references/flip-paths.md`). An implementer
who finds a binding item wrong reports BLOCKED
(`skills/subagent-driven-development/implementer-prompt.md` § Binding vs
Advisory: the Deviation License), and an adjudication or a plan conflict
that touches a mark goes to the operator
(`skills/subagent-driven-development/SKILL.md` § Disputes and
adjudication). Every correction to binding content, however contained,
therefore costs an operator ask, while the spec is, under the umbrella's
U1, expected to be wrong in places.

A sample measured in this feature's context gathering (four features
with marks that went through implementation, on crucible and one other
project; session transcripts searched by keyword, so order-of-magnitude
only; the sample's report is not in this repository, so its figures are
`UNVERIFIED` for any seat):

- 3 of 29 marks and 9 of 36 Constraints items had any binding event
  after their campaign closed.
- Most events were a review finding citing the item and rejecting a
  real drift, at the cost of at most a fix round.
- The costly or harmful cases took three shapes: ceremony (a mark on
  the wording of a command recipe forced a scoped amendment and a
  re-pin of the plan); literalism (a controller applied a Constraint
  literally to an edge case its author plausibly never considered,
  removing existing behaviour, with no ask); and a probably blocked
  improvement (a Constraint reverted an implementer's prompt
  improvement; the revert itself was not seen).
- The one stop-and-two-asks chain started at an Acceptance threshold and
  ended in a Constraint change the operator accepted with "OK, I guess";
  the host's permission classifier refused the spec edit as "rewriting a
  binding acceptance threshold so a failing gate would pass".
- Unmarked operator rulings flipped downstream went fine, protected by
  the logged-rationale rule.

Brainstorming meanwhile records every operator answer as `settled`
(`skills/brainstorming/SKILL.md` § Workspace provisioning (brainstorm
exit), `skills/redteaming/references/formats.md` § Design digest
format), though most answers mean "this until new evidence arrives";
and a plan task writing a decision record cannot see the brainstorm
decision record, so it attributed every position to "judgment, accepted
by the maintainer", the maintainer's own included
(`docs/backlog/review-catch-and-implementers.md`).

**Goals.**

- **G1.** State the umbrella's U1 stance where every seat reads it, and
  what binds under it.
- **G2.** Contained corrections of binding content decided by the
  controller, routine and recorded; the operator asked where a
  correction is not contained.
- **G3.** A mark names what builds on the decision it marks; guidance on
  what earns one, and on what belongs in Constraints & invariants.
- **G4.** Approvals recorded as accepted by default, firm only on the
  operator's word, in the brainstorm record, the digest and
  `docs/decisions/`.
- **G5.** A plan task that writes a decision record takes the brainstorm
  decision record as an input, with what it needs to attribute each
  position.

**Non-goals.**

- The very-small lane's note: its binding parts (Intent, Acceptance, Out
  of scope) are the operator's approval of the goal and still change only
  on the operator's word (`skills/subagent-driven-development/references/very-small-lane.md`).
  Checking the lane's goal premise is `seat-voice`'s.
- Umbrella content: what an umbrella binds, a feature's own entry
  included, keeps its decision ask
  (`skills/brainstorming/references/umbrellas.md` § Edits).
- A licence for task reviewers and the branch reviewer to find binding
  content itself wrong, which redteam seats already hold
  (`skills/redteaming/seat-prompt.md`): that premise-level mandate is
  `seat-voice`'s. Here a correction starts from an implementer's BLOCKED
  report, a redteam seat's finding, or a controller's ruling.
- Re-marking past specs. Shipped specs are frozen; the guidance applies
  to specs written from this feature's landing on.
- A shared reference every seat template points to for what binds. Six
  templates state it today; the skill-text rewrite
  (`docs/backlog/skill-text-rewrite.md`) may consolidate them.
- The doubts channel, implementers' standing (`seat-voice`), and the
  arrangement choices (`arrangements`).

## Decisions

All lightly held, as the umbrella's U2 makes the default.

- **D1. What binds, and how it is read.** The spec is a hypothesis:
  probably subtly wrong, certainly locally imperfect. What binds is
  Constraints & invariants, `[LOAD-BEARING]` marks, preamble conventions
  the spec declares binding, decisions the spec records as the
  operator's firm preference (D4), and the umbrella content its umbrella
  line brings in. Binding means never changed silently, where it meant
  never changed without the operator. Binding text is read for its
  intent: where its literal reading reaches a case its author plainly
  did not consider, that is a correction to raise, never a literal
  ruling to apply. As today, the bar applies from the spec campaign's
  close; during the spec's own campaign its fixes correct binding text
  like any other. Basis: the maintainer's request (above) and the
  umbrella's U1; the literal-reading rule is from the sample's
  literalism case.
- **D2. The contained scoped amendment.** The scoped amendment is
  confirmed by the controller, with no decision ask, where it is
  **contained**: everything that builds on the changed item lies inside
  this feature (for a mark, what the mark names; for a Constraints item,
  the work that must keep it), and the change is none of: a change to
  umbrella content, the feature's own entry included; a change to a
  decision the spec records as `firm` (D4); a change that turns a failing
  check into a passing one; a structural change, which takes a
  supersede. Anything else keeps the operator's confirmation. A
  contained amendment is a scoped amendment in every other respect: the
  same marker, plan patch, re-pin and naming of its commit to the
  reviews whose range holds it, so every rule that names a scoped
  amendment covers it. The controller records each as one of its own
  rulings in the ledger, with its reason, so the branch review receives
  it with the rulings and the close readout lists it; one made in the
  plan phase is recorded in the plan record and seeded into the ledger
  at the phase's close. The operator may reverse any. Producers: an
  implementer's BLOCKED report on a binding item, now carrying its
  evidence and a proposed correction; a redteam seat's finding; and the
  controller's own plan-conflict rulings and the adjudications it acts
  on, which today go to the operator whenever they touch a mark and now
  go through this test. Basis: judgment, accepted by the maintainer
  (option (a) of three: controller, a fresh adjudicator per correction,
  or a batched non-blocking operator ask); the failing-check exclusion
  is from the sample's acceptance-threshold case.
- **D3. Marks name what builds on them.** A mark in a spec takes the
  form `[LOAD-BEARING: <what builds on it>]` and binds, as today, exactly
  the sentence or bullet it annotates. It is earned only when something
  beyond its own sentence is built on the decision: other tasks, other
  features or children, an outside commitment. A wording, a threshold
  only this feature uses, and the operator's preference earn none; the
  last is `firm`'s (D4). Constraints & invariants holds invariants every
  task must keep, not a requirement one site meets. Marks are a spec
  convention: the two the skills place on their own text (the branch
  review's wave cap, the redteaming reporting stance) are dropped, their
  wording kept. Basis: the umbrella's U2 and the maintainer's judgment
  that marks are used too liberally; the form is judgment, accepted by
  the maintainer.
- **D4. Approval strength.** The brainstorm decision record and the
  digest record each decision as `open`, `accepted` or `firm`, and each
  record entry names who proposed it, the operator or the controller.
  `accepted` is the default for any approval, a "+", an "OK" or a "your
  call" included, and means "this until new evidence arrives"; `firm` is
  recorded only on the operator's explicit word, never inferred from an
  approval. A `firm` decision that reaches the spec is stated there as
  the operator's firm preference, and binds (D1). It is not thereby
  marked: a mark records what builds on a decision, `firm` the
  operator's preference. An operator ruling on a campaign's decision ask
  is entered in the brainstorm decision record too, with its status. In
  `docs/decisions/`, a record states a position as held firmly only
  where the maintainer said so; "the maintainer's preference" names a
  position's origin, not its strength, and no existing record is re-read
  as firm. Basis: the maintainer's observation quoted above; the three
  statuses and their separation from marks are judgment, accepted by the
  maintainer ("your call").
- **D5. Decision-record tasks.** A plan task that writes or edits a
  decision record names the brainstorm decision record among its inputs,
  so each position's basis is attributed when it is written, from the
  record's proposer and status (D4). Basis: the umbrella's entry, from a
  follow-up the maintainer agreed to
  (`docs/backlog/review-catch-and-implementers.md`).
- **D6. Backlog.** `docs/backlog/load-bearing-marks-audit.md` is
  deleted: the sample above took the place of its count, and D3 is the
  guidance it asked for. The decision-record follow-up of
  `docs/backlog/review-catch-and-implementers.md` is removed with the
  observation that supports only it, its other follow-ups staying for
  `seat-voice` and `arrangements`. Basis: the umbrella's closing rule;
  the sample in place of a full count is the maintainer's ruling.

## Constraints & invariants

- **C1.** The controller never confirms a change to umbrella content, a
  `firm` decision, a change that turns a failing check into a passing
  one, a structural change, or one something outside the feature builds
  on: each of those keeps an operator decision ask.
- **C2.** Every contained amendment is visible: its marker at the
  changed text, its commit named as a scoped amendment's is, a ruling
  in the ledger that reaches the branch review, and a line in the close
  readout.
- **C3.** The containment test is stated once, in
  `skills/redteaming/references/flip-paths.md`; every other site that
  routes a binding-content finding points there.

## Interfaces & boundaries

- **What `seat-voice` and `arrangements` consume** (the umbrella's
  Interfaces & boundaries): D1 is what binds a seat; D2 is what a
  premise-level finding can lead to, and the safety valve for stopping
  review early.
- **Sites that change.** Found by searching for the mark, "binding",
  "settled", "lightly", the flip-path references and the routing of
  mark-touching rulings:
  - `skills/redteaming/references/flip-paths.md`: the scoped amendment's
    confirmation by the controller where contained, and the containment
    test (C3).
  - `skills/redteaming/SKILL.md`: § Flip paths, which routes binding
    content a finding shows wrong; § Round readout, where an operator
    ruling is also entered in the brainstorm decision record (D4); the
    mark on its reporting stance (D3).
  - `skills/redteaming/references/plan-phase.md`: a contained amendment
    made in the plan phase recorded and seeded into the ledger.
  - `skills/redteaming/references/formats.md` § Design digest format:
    the statuses, and contained amendments among the derivation rule's
    sources beside the scoped-amendment asks.
  - `skills/subagent-driven-development/SKILL.md`: the Deviations
    paragraph; § Disputes and adjudication, where a plan conflict or an
    adjudicator's ruling that touches a mark now passes the containment
    test; § Plan changes mid-execution.
  - The six seat templates, each stating what binds (D1's set, its
    intent reading and its stance): `skills/redteaming/seat-prompt.md`,
    `skills/redteaming/terminal-pass-prompt.md`,
    `skills/requesting-code-review/code-reviewer.md`,
    `skills/subagent-driven-development/task-reviewer-prompt.md`,
    `skills/subagent-driven-development/re-review-prompt.md` and
    `skills/subagent-driven-development/implementer-prompt.md`, the
    last also carrying BLOCKED with a proposed correction, and reading a
    decision record its plan task names; and the controller-facing
    statement of the same in
    `skills/subagent-driven-development/references/dispatch-composition.md`
    item 4 and `skills/writing-plans/SKILL.md` § Plan header's spec
    pointer.
  - `skills/requesting-code-review/SKILL.md`: the mark on its wave cap
    (D3).
  - `skills/brainstorming/SKILL.md`: § Spec contract's decision-weight
    convention (D1, D3, D4's `firm` in the spec); the decision record's
    statuses and proposer; the fold and lane entries that record an
    answer as settled.
  - `skills/writing-plans/SKILL.md`: D5; § Binding vs advisory where it
    names what binds.
  - `docs/decisions/`: `the-spec.md`, `decision-records.md`,
    `adjudication.md` (the routing of mark-touching rulings),
    `task-loop.md` (the implementer contract), `branch-review.md` and
    `spec-campaign.md` (their citations of the dropped marks), each with
    a Changes line.
  - The two backlog items (D6); `agents/`, regenerated from the changed
    templates; `tests/prose-budget.txt`.
- **Unchanged:** `skills/brainstorming/references/umbrellas.md` and
  `skills/subagent-driven-development/references/very-small-lane.md`
  (Non-goals).

Deferred to implementation: the wording each template uses for D1, at the altitude of its existing binding paragraph.

## Acceptance

- **A1.** `flip-paths.md` states the containment test of D2, and no
  other file under `skills/` restates it. One-time check: a search of
  `skills/` for `contained`, `firm` and `failing check`, its output
  quoted, every hit outside `flip-paths.md` either a pointer to it or
  another sense of the word.
- **A2.** No skill records an operator answer as `settled`; the
  brainstorm record and the digest use `open`, `accepted` and `firm`.
  One-time check: a search for `settled` across `skills/`, its output
  quoted; the hits that remain are the incoming-document sense
  (`skills/brainstorming/SKILL.md` § Context gathering,
  `skills/brainstorming/references/umbrellas.md` § Children).
- **A3.** The six templates state D1; the implementer prompt states the
  proposed correction with BLOCKED; the spec contract states D3's form
  and guidance and D4's `firm`. Review-judged: prose fidelity, no reader
  parses it.
- **A4.** `writing-plans` names the brainstorm decision record as an
  input of a decision-record task, and the record's entries carry a
  proposer. Review-judged.
- **A5.** `docs/backlog/load-bearing-marks-audit.md` is gone, and
  `review-catch-and-implementers.md` carries neither the decision-record
  follow-up nor the observation that supports only it. One-time check:
  `git ls-files` for the first, a search for `brainstorm decision record`
  and `could not see` in the second, each quoted.
- **A6.** The decision records listed above state the new positions,
  each edit with its Changes line. Review-judged.
- **A7.** No `[LOAD-BEARING]` mark remains on the skills' own text.
  One-time check: a search of `skills/` for `LOAD-BEARING`, its output
  quoted, every hit naming the mark rather than placing one.
- **A8.** The suite passes, its prose budget and generated agents
  included. Standing.
- **A9.** The landing states the net word change to the skills, from
  `tests/prose-budget.txt`, and what it removed (the umbrella's U5).
  One-time, in the landing's readout.

## Mechanism sketches (advisory)

- In `flip-paths.md`, the scoped amendment's opening line ("on the
  operator's confirmation") gains its second confirmer and the
  containment test; its steps stay as they are.
- The ledger ruling for a contained amendment under
  `## Adjudication rulings`: the item, what changed and why, the
  containment reason, the commit.
- In the spec contract, `firm` stated in a Decision's basis ("the
  operator's firm preference"), so it needs no new syntax.
- A decision-record entry's proposer as a word in its status line
  (`accepted — proposed by the controller`).
