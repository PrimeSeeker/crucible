Lane: very-small (operator-confirmed 2026-11-23)

# The lane and the last full read: five follow-ups

## Intent

Five small changes to rules, from two backlog items
(`docs/backlog/very-small-lane-proposals.md`, and the last two Follow-up
bullets of `docs/backlog/review-seat-report-write.md`).

1. **Record corrections.** The pass that ends a branch review may leave a
   minor finding against a statement in a decision record or an open item
   that it found false or misattributed. Today the controller can only
   file it, so the false statement lands. The controller may now correct
   it before Finish, with no fix wave and no further pass, and names each
   correction in the close readout. This holds on every route and never
   covers the spec, plan, lane note, skill text or code.
2. **The lane note is the controller's document.** The operator approves
   the design, which proposes the lane, as on the other routes. The
   controller then writes the note from it, and the note is no longer
   shown for approval. In exchange, the branch reviewer checks the note's
   exclusions, not only its Intent, against the operator's recorded
   request. A change to a committed note's binding parts stays the
   operator's decision.
3. **No wording searches.** A lane note's Acceptance no longer checks
   prose by searching for its words. The Intent states the outcome, the
   reviewer judges it, and Acceptance holds the suite and checks of
   structure.
4. **Hand-written seats get the reason too.** A seat the controller
   composes is given the reason the report file is the deliverable,
   beside the sentence on what was off.
5. **The quote.** The instruments record quotes the maintainer on the
   probe where it now paraphrases them.

Premise. Three observations from a controller's process notes on the two
features before this one, as the first backlog item records them: what the
last full-scope pass finds at MINOR can only be filed; on both features
the controller showed the design and wrote the note fuller; and searches
for wording in Acceptance cost two operator decisions and never failed.
The counts came from those features' ledgers, deleted with their
workspaces. Nothing was probed: each change removes a step or states a
reason, and shows its effect only in later runs.

No break.

## Change list

- `skills/requesting-code-review/SKILL.md` § The branch-review loop: a
  paragraph after the cleanup wave's, giving the controller the
  correction. `skills/subagent-driven-development/references/finish.md`,
  step 2: the close readout lists each correction.
- `skills/brainstorming/references/lane-note.md`: the note is written at
  step 5 from the approved design, its self-review run before it is
  committed; Acceptance takes no search for wording.
  `skills/brainstorming/references/proposing-the-arrangement.md`, the
  very-small bullet, and `skills/brainstorming/SKILL.md` (§ Proposing the
  arrangement, and the two clauses on a draft that step 4 approved): the
  lane is entered by the approval of the design that proposes it.
  `skills/brainstorming/references/umbrellas.md` § Review: an umbrella
  with no campaign states its own procedure, no longer "as a lane note
  is"; the procedure itself is unchanged.
- `skills/requesting-code-review/very-small-lane-review.md`: the goal
  check reads the note's Out of scope with its Intent.
- `skills/subagent-driven-development/references/dispatch-composition.md`,
  item 5: a composed dispatch copies the reason beside the sentence on
  what was off.
- `docs/decisions/branch-review.md`, `docs/decisions/routes.md` and
  `docs/decisions/instruments.md`: the positions above, their reasons, and
  a `## Changes` line each. `docs/decisions/instruments.md` § Why › Report
  files: the maintainer quoted on the probe. `docs/decisions/umbrellas.md`:
  the two sentences that say an umbrella is approved "as a lane note is".
- `README.md`: the sentence saying the very small preset waits for the
  approval of its lane note.
- `docs/backlog/very-small-lane-proposals.md` is deleted, its three
  proposals resolved. `docs/backlog/review-seat-report-write.md` loses the
  two Follow-up bullets this change resolves and their two Observation
  bullets. `docs/backlog/skill-rewrite-reaudit.md`: the next read also
  counts record corrections and whether any was wrong.
- `tests/prose-budget.txt`: the changed counts, the commit saying what the
  words buy.

## Acceptance

1. `python -m pytest tests/` passes, with `TOTAL_CAP` in
   `tests/test_prose_budget.py` still 47387.
2. `git ls-files docs/backlog/very-small-lane-proposals.md` prints
   nothing.
3. `git grep -c "^- 2026-11-23:" -- docs/decisions/branch-review.md docs/decisions/routes.md docs/decisions/instruments.md`
   prints a count for each of the three files.

On the tree before the change, check 1 passes, check 2 prints the path and
check 3 prints nothing. No check searches for the new wording: the Intent
states each outcome and the branch reviewer judges it. Whether a
correction is ever wrong, and whether a note written without being shown
departs from its design, show only in later sessions.

## Out of scope

- The full-scope pass after every fix wave, the cleanup wave's rules and
  the wave cap.
- Corrections to anything but decision records and open items.
- The note's freeze and re-pin, its four parts and what binds.
- Acceptance in specs and plans.
- How an umbrella without a campaign is approved: it is still shown to
  the operator.
- The criteria for choosing a route, which stay in the backlog
  (`docs/backlog/skill-rewrite-reaudit.md`).
- The counts of report-file misses and the absolute report path, which
  stay in `docs/backlog/review-seat-report-write.md`.
- `TOTAL_CAP`.
