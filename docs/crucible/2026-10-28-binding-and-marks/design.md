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
project; transcripts searched by keyword, so order-of-magnitude only):

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
  what still binds under it.
- **G2.** A correction path for binding content a seat shows wrong:
  routine and recorded where the correction is contained, an operator
  ask where it is not.
- **G3.** A mark names what builds on the decision it marks; guidance on
  what earns one, and on what belongs in Constraints & invariants.
- **G4.** Approvals recorded as accepted by default, firm only on the
  operator's word, in the brainstorm record, the digest and
  `docs/decisions/`.
- **G5.** A plan task that writes a decision record takes the brainstorm
  decision record as an input.

**Non-goals.**

- The very-small lane's note: its binding parts (Intent, Acceptance, Out
  of scope) are the operator's approval of the goal and still change only
  on the operator's word (`skills/subagent-driven-development/references/very-small-lane.md`).
  Checking the lane's goal premise is `seat-voice`'s.
- Umbrella content: what an umbrella binds is never contained in one
  child, so its binding changes keep their decision ask
  (`skills/brainstorming/references/umbrellas.md` § Edits).
- Re-marking past specs. Shipped specs are frozen; the guidance applies
  to specs written from this feature's landing on.
- Seats' premise-level mandate, the doubts channel and implementers'
  standing (`seat-voice`), and the arrangement choices (`arrangements`).

## Decisions

All lightly held, as the umbrella's U2 makes the default.

- **D1. What binds, and how it is read.** The spec is a hypothesis:
  probably subtly wrong, certainly locally imperfect. The binding set is
  unchanged (Constraints & invariants, `[LOAD-BEARING]` marks, preamble
  conventions the spec declares binding, and the umbrella content its
  umbrella line brings in); binding now means never changed silently,
  where it meant never changed without the operator. Binding text is read
  for its intent: where its literal reading reaches a case its author
  plainly did not consider, that is a correction to raise, never a
  literal ruling to apply. As today, the bar applies from the spec
  campaign's close; during the spec's own campaign its fixes correct
  binding text like any other. Basis: the maintainer's request (above)
  and the umbrella's U1; the literal-reading rule is from the sample's
  literalism case.
- **D2. The correction path.** A seat that finds binding content wrong
  stops on that item with its evidence and a proposed correction: an
  implementer reports BLOCKED, a reviewer files a finding. The controller
  then checks what builds on the item: for a mark, what the mark names;
  for a Constraints item, the work that must keep it. The correction is
  **contained** when everything that builds on the item lies inside this
  feature and the correction is none of: a change to an item the spec
  records as `firm` (D4); a change that turns a failing check into a
  passing one; a structural change, which takes a supersede. A contained
  correction is the scoped amendment without its decision ask: the
  controller amends the spec in place with a correction marker, patches
  the plan to match, records it in the ledger, and names its commit to
  the reviews whose range holds it as an amendment commit is named; the
  close readout lists every correction, and the operator may reverse
  any. Everything else takes the existing decision ask, a scoped
  amendment or a supersede. Basis: judgment, accepted by the maintainer
  (option (a) of three: controller, a fresh adjudicator per correction,
  or a batched non-blocking operator ask); the failing-check exclusion
  is from the sample's acceptance-threshold case.
- **D3. Marks name what builds on them.** A mark takes the form
  `[LOAD-BEARING: <what builds on it>]`, and binds, as today, exactly
  the sentence or bullet it annotates. It is earned only when something
  beyond its own sentence is built on the decision: other tasks, other
  features or children, an outside commitment. A wording, a threshold
  only this feature uses, and the operator's preference earn none; the
  last is `firm`'s (D4). Constraints & invariants holds invariants every
  task must keep, not a requirement one site meets. Basis: the umbrella's
  U2 and the maintainer's judgment that marks are used too liberally;
  the form is judgment, accepted by the maintainer.
- **D4. Approval strength.** The brainstorm decision record and the
  digest record each decision as `open`, `accepted` or `firm`.
  `accepted` is the default for any approval, a "+", an "OK" or a "your
  call" included, and means "this until new evidence arrives"; `firm` is
  recorded only on the operator's explicit word, never inferred from an
  approval. A `firm` decision that reaches the spec says so there, so a
  seat that would flip it raises it instead (D2). A `firm` decision is
  not thereby marked: a mark records what builds on a decision, `firm`
  the operator's preference. In `docs/decisions/`, a record states a
  position as held firmly only where the maintainer said so; everything
  else is its current position until new evidence. Basis: the
  maintainer's observation quoted above; the three statuses and their
  separation from marks are judgment, accepted by the maintainer
  ("your call").
- **D5. Decision-record tasks.** A plan task that writes or edits a
  decision record takes the brainstorm decision record as an input, so
  each position's basis is attributed when it is written. Basis: the
  umbrella's entry, from a follow-up the maintainer agreed to
  (`docs/backlog/review-catch-and-implementers.md`).
- **D6. Backlog.** `docs/backlog/load-bearing-marks-audit.md` is
  deleted: the sample above took the place of its count, and D3 is the
  guidance it asked for. The decision-record follow-up of
  `docs/backlog/review-catch-and-implementers.md` is removed, its other
  follow-ups staying for `seat-voice` and `arrangements`. Basis: the
  umbrella's closing rule; the sample in place of a full count is the
  maintainer's ruling.

## Constraints & invariants

- **C1.** The correction path never decides a change that reaches beyond
  the feature, a `firm` item, a change that turns a failing check into a
  passing one, or a structural change: each of those still opens with an
  operator decision ask.
- **C2.** Every correction is visible: a marker at the changed text, a
  ledger record, its commit named to the reviews whose range holds it,
  and a line in the close readout.
- **C3.** The containment conditions are stated once, in
  `skills/redteaming/references/flip-paths.md`; every other site that
  routes a binding-content finding points there.

## Interfaces & boundaries

- **What `seat-voice` and `arrangements` consume** (the umbrella's
  Interfaces & boundaries): D1 is what binds a seat; D2 is what a
  premise-level finding can lead to, and the safety valve for stopping
  review early.
- **Sites that change.** Found by searching for the mark, "binding",
  "settled", "lightly" and the flip-path references:
  - `skills/redteaming/references/flip-paths.md`: the correction path
    beside the scoped amendment and the supersede (C3).
  - `skills/subagent-driven-development/SKILL.md`: the Deviations
    paragraph; § Disputes and adjudication, where a plan conflict or an
    adjudicator's ruling that touches a mark goes to the operator today
    and passes the containment check instead; § Plan changes
    mid-execution; § Finish's close readout listing corrections.
  - `skills/subagent-driven-development/implementer-prompt.md`: BLOCKED
    on a binding item with a proposed correction; binding text read for
    its intent.
  - `skills/subagent-driven-development/references/dispatch-composition.md`
    item 4, the binding pointer every seat template points at; a
    template's own restatement of it where one carries D1's change.
  - `skills/brainstorming/SKILL.md`: § Spec contract's decision-weight
    convention (D1, D3, D4's `firm` in the spec); the decision record's
    statuses; the fold and lane entries that record an answer as
    settled.
  - `skills/redteaming/references/formats.md` § Design digest format:
    the statuses.
  - `skills/redteaming/SKILL.md`: where it routes binding content a
    finding shows wrong to the flip paths.
  - `skills/writing-plans/SKILL.md`: D5; § Binding vs advisory where it
    names what binds.
  - The skills' own uses of the mark on their own text
    (`skills/requesting-code-review/SKILL.md`'s wave cap,
    `skills/redteaming/SKILL.md`'s reporting stance).
  - `docs/decisions/the-spec.md` and `docs/decisions/decision-records.md`,
    each with a Changes line.
  - The two backlog items (D6); `agents/`, regenerated where a template
    changes; `tests/prose-budget.txt`.
- **Unchanged:** `skills/brainstorming/references/umbrellas.md` and
  `skills/subagent-driven-development/references/very-small-lane.md`
  (Non-goals).

Deferred to implementation: whether each of the skills' own marks on their own text takes the new form or is dropped.

Deferred to implementation: the correction marker's wording and the ledger line's form.

## Acceptance

- **A1.** `flip-paths.md` carries the correction path with the
  containment conditions of D2, and every other site routing a
  binding-content finding points there rather than restating them.
  One-time check: a search for the conditions' key terms, its output
  quoted.
- **A2.** No skill records an operator answer as `settled`; the
  brainstorm record and the digest use `open`, `accepted` and `firm`.
  One-time check: a search for `settled` across `skills/`, its output
  quoted and each remaining hit accounted for.
- **A3.** The spec contract states D1's reading and D3's form and
  guidance; the implementer prompt states the proposed correction with
  BLOCKED; the SDD close readout lists corrections. Review-judged: prose
  fidelity, no reader parses it.
- **A4.** `writing-plans` names the brainstorm decision record as an
  input of a decision-record task. Review-judged.
- **A5.** `docs/backlog/load-bearing-marks-audit.md` is gone and
  `review-catch-and-implementers.md` has no decision-record follow-up.
  One-time check.
- **A6.** `docs/decisions/the-spec.md` and `decision-records.md` state
  the new positions, each edit with its Changes line. Review-judged.
- **A7.** The suite passes, its prose budget and generated agents
  included. Standing.
- **A8.** The landing states the net word change to the skills, from
  `tests/prose-budget.txt`, and what it removed (the umbrella's U5).
  One-time, in the landing's readout.

## Mechanism sketches (advisory)

- The correction path in `flip-paths.md` as a third subsection after the
  scoped amendment: its steps are the scoped amendment's steps 1–4 with
  the decision ask replaced by the containment check, and a pointer to
  `crucible:subagent-driven-development` § Finish for the readout line.
- A ledger line `Correction: <item> — <what changed and why> — <commit>`
  under `## Progress`, which the close readout assembles from.
- In the spec contract, `firm` stated in a Decision's basis ("the
  operator's firm preference"), so it needs no new syntax.
