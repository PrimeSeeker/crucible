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
- Changing how umbrella content binds beyond D1's `firm` class: what an
  umbrella binds, a feature's own entry included, keeps its decision ask
  (`skills/brainstorming/references/umbrellas.md` § Edits).
- A licence for task reviewers and the branch reviewer to find binding
  content itself wrong, which redteam seats already hold
  (`skills/redteaming/seat-prompt.md`): that premise-level mandate is
  `seat-voice`'s. Here a reviewer raises only the literal-reading case
  (D2).
- The small routes' qualifying shape, "no change to [LOAD-BEARING]
  content", stays as worded at its sites
  (`skills/brainstorming/SKILL.md` § The folded lane and § The very-small
  lane, `skills/redteaming/references/folded-lane.md`,
  `skills/requesting-code-review/code-reviewer.md`'s Lane Fit,
  `docs/decisions/routes.md`): `arrangements` re-expresses it with U3.
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
  probably subtly wrong, certainly locally imperfect. What binds in the
  spec is its Constraints & invariants, its `[LOAD-BEARING]` marks, the
  preamble conventions it declares binding, the decisions it records as
  the operator's firm preference (D4), and the umbrella content its
  umbrella line brings in, an umbrella's firm decisions included. What
  binds in the plan is unchanged: what `skills/writing-plans/SKILL.md`
  § Binding vs advisory and the implementer prompt state (requirements,
  interfaces, non-goals, acceptance, the routing table's rows, values
  marked verbatim). D1 adds the `firm` class to those lists and replaces
  none of them. Binding means never changed silently, where it meant
  never changed without the operator. Binding text is read for its
  intent: where its literal reading reaches a case its author plainly
  did not consider, that is raised for a ruling, never applied
  literally. As today, the bar applies from the spec campaign's close;
  during the spec's own campaign its fixes correct binding text like any
  other. Basis: the maintainer's request (above) and the umbrella's U1;
  the literal-reading rule is from the sample's literalism case.
- **D2. The contained scoped amendment.** From the spec campaign's
  close, every change to binding content, a ruling that patches the plan
  included, is either contained or put to the operator. It is
  **contained** when everything that builds on or consumes the changed
  item lies inside this feature (a mark names what builds on it; for any
  other item, or a mark that names nothing, the controller judges what
  does), and it is none of: a change to umbrella content, the feature's
  own entry included; a change to a decision recorded as `firm` (D4); a
  change after which the same work, unchanged, passes a check it failed;
  a structural change, one that redefines a mechanism rather than
  correcting content inside one that stands, which takes a supersede. A
  contained change to the spec is a scoped amendment the controller
  confirms, with no decision ask, and is a scoped amendment in every
  other respect: the same marker, plan patch, re-pin and naming of its
  commit to the reviews whose range holds it, so every rule that names a
  scoped amendment covers it; a contained plan-patching ruling stays as
  today. The controller records each as one of its own rulings in the
  ledger, with its reason, so the branch review receives it with the
  rulings and the close readout lists it. In the plan phase a contained
  amendment lands as an item of that phase's fix list, is named in its
  readout as a technical call, and is seeded into the ledger at the
  phase's close. A change that is not contained keeps the operator's
  confirmation, and a plan conflict that is a design judgment still goes
  to the operator. Reversing a contained amendment is a scoped amendment
  the operator confirms, made before the branch lands. Producers: an
  implementer's BLOCKED report on a binding item, now carrying its
  evidence and a proposed correction; a redteam seat's finding; a
  reviewer's finding that a binding item's literal reading reaches a
  case its author did not consider, which the controller rules on as a
  plan conflict; and the controller's own plan-conflict rulings and the
  adjudications it acts on. The adjudicator marks, and the controller
  routes through this test, a ruling that touches binding content, not
  only a mark. Basis: judgment, accepted by the maintainer (option (a)
  of three: controller, a fresh adjudicator per correction, or a batched
  non-blocking operator ask); the failing-check exclusion is from the
  sample's acceptance-threshold case.
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
  approval. A route entry (the fold, the very-small lane) confirms the
  route by being present, whatever its status. A `firm` decision that
  reaches a spec or an umbrella is stated there as the operator's firm
  preference, and binds (D1). It is not thereby marked: a mark records
  what builds on a decision, `firm` the operator's preference. Every
  operator ruling on a decision ask after the brainstorm, in a campaign,
  the plan phase or execution, is entered in the brainstorm decision
  record too, with its status; that is stated once, where the record is
  defined. In `docs/decisions/`, a record states a position as held
  firmly only where the maintainer said so; "the maintainer's
  preference" names a position's origin, not its strength, and no
  existing record is re-read as firm. Basis: the maintainer's
  observation quoted above; the three statuses and their separation
  from marks are judgment, accepted by the maintainer ("your call").
- **D5. Decision-record tasks.** A plan task that writes or edits a
  decision record names the brainstorm decision record among its inputs,
  for its implementer and its task reviewer, so each position's basis is
  attributed when it is written and checked when it is reviewed, from
  the record's proposer and status (D4). Basis: the umbrella's entry,
  from a follow-up the maintainer agreed to
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
  `firm` decision, a change after which the same work, unchanged, passes
  a check it failed, a structural change, or one something outside the
  feature builds on or consumes: each of those keeps an operator
  decision ask.
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
    confirmation by the controller where contained, the containment
    test (C3), and plan-patching rulings under the same test.
  - `skills/redteaming/SKILL.md`: § Flip paths, which routes binding
    content a finding shows wrong; the mark on its reporting stance (D3).
    Its § Fix application sentence making a fix's acceptance item
    binding already agrees with D1 and stays.
  - `skills/redteaming/references/plan-phase.md`: a contained amendment
    made in the plan phase lands in its fix list, is named in its
    readout and is seeded into the ledger; its "structural plan finding
    — the spec's premise is wrong" reworded to D2's sense of structural.
  - `skills/redteaming/references/formats.md` § Design digest format:
    the statuses.
  - `skills/subagent-driven-development/SKILL.md`: the Deviations
    paragraph; § Disputes and adjudication, where a plan conflict or an
    adjudicator's ruling that touches binding content passes the
    containment test; § Plan changes mid-execution.
  - The six seat templates, each stating what binds (D1's set, its
    intent reading and its stance; in the umbrella clause, firm
    decisions): `skills/redteaming/seat-prompt.md`,
    `skills/redteaming/terminal-pass-prompt.md`,
    `skills/requesting-code-review/code-reviewer.md`,
    `skills/subagent-driven-development/task-reviewer-prompt.md`,
    `skills/subagent-driven-development/re-review-prompt.md` and
    `skills/subagent-driven-development/implementer-prompt.md`. The
    reviewer templates send the literal-reading case to the controller
    (D2); the implementer prompt carries BLOCKED with a proposed
    correction; the implementer and task-reviewer templates read a
    decision record their plan task names (D5). The controller-facing
    statement of the same: `skills/subagent-driven-development/references/dispatch-composition.md`
    item 4 and `skills/writing-plans/SKILL.md` § Plan header's spec
    pointer.
  - `skills/brainstorming/references/umbrellas.md`: § Children's binding
    sentence and § Edits' unmarked Decisions gain the `firm` class.
  - `skills/requesting-code-review/SKILL.md`: the mark on its wave cap
    (D3).
  - `skills/brainstorming/SKILL.md`: § Spec contract's decision-weight
    convention (D1, D3, D4's `firm` in the spec); § Workspace
    provisioning's decision record (statuses, proposer, later operator
    rulings); the fold and lane entries that record an answer as
    settled.
  - `skills/writing-plans/SKILL.md`: D5; § Binding vs advisory, which
    gains the `firm` class.
  - `docs/decisions/`: `the-spec.md`, `decision-records.md`,
    `adjudication.md` (the routing of mark-touching rulings),
    `task-loop.md` (the implementer contract), `branch-review.md` and
    `spec-campaign.md` (their citations of the dropped marks),
    `umbrellas.md` where it states what binds a child, each with a
    Changes line.
  - The backlog: the two items of D6, and
    `docs/backlog/nested-orchestration.md`, whose observation lists
    mark-touching rulings among mid-run asks. `agents/`, regenerated
    from the changed templates; `tests/prose-budget.txt`.
- **Unchanged:** `skills/subagent-driven-development/references/very-small-lane.md`
  and the qualifying-shape sites (Non-goals).

Deferred to implementation: the wording each template uses for D1, at the altitude of its existing binding paragraph.

## Acceptance

- **A1.** `flip-paths.md` states the containment test of D2, and no
  other file under `skills/` restates it. One-time check: a whole-word
  search of `skills/` for `contained` and `firm`, and a search for the
  phrase `check it failed`, its output quoted, each hit outside `flip-paths.md` classed as a pointer to it, a
  statement of the binding set or the `firm` status (D1, D4), or another
  sense of the word.
- **A2.** No skill records an operator answer as `settled`; the
  brainstorm record and the digest use `open`, `accepted` and `firm`.
  One-time check: a search for `settled` across `skills/`, its output
  quoted; the hits that remain are the incoming-document sense
  (`skills/brainstorming/SKILL.md` § Context gathering,
  `skills/brainstorming/references/umbrellas.md` § Children).
- **A3.** The six templates state D1; the implementer prompt states the
  proposed correction with BLOCKED; the spec contract states D3's form
  and guidance and D4's `firm`; the routing and visibility of D2 and C2
  (SDD's routing of rulings that touch binding content, the plan
  phase's handling, the ledger ruling, the close-readout line) are in
  place. Review-judged: prose fidelity, no reader parses it.
- **A4.** `writing-plans` names the brainstorm decision record as an
  input of a decision-record task for its implementer and reviewer, and
  the record's entries carry a proposer. Review-judged.
- **A5.** `docs/backlog/load-bearing-marks-audit.md` is gone, and
  `review-catch-and-implementers.md` carries neither the decision-record
  follow-up nor the observation that supports only it. One-time check:
  `git ls-files` for the first, a search for `brainstorm decision record`
  and `could not see` in the second, each quoted.
- **A6.** The decision records and the backlog item listed above state
  the new positions, each record edit with its Changes line.
  Review-judged.
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
