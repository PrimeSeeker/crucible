Lane: very-small (operator-confirmed 2026-11-24)

# Backlog rulings: the goal check, the review mark, the ledger exclusion

## Intent

The maintainer ruled on four backlog items and on the observations the
re-audit of 2026-11-23 left unruled (over 36 features of one code project
on crucible 0.33.1). This lane carries those rulings into the skills and
records, and closes the two text gaps of
`docs/backlog/spec-campaign-close-text-gaps.md`.

- **The goal check leaves the branch review, except on the very-small
  lane.** All 85 branch-review passes in the re-audit ran it and none
  raised a premise finding or a goal mismatch; several noted a request
  holding only approvals, so the scope they checked came from the
  controller's summaries. Round-1 goal checks changed designs in several
  campaigns, and on the very-small lane the branch reviewer's goal check
  is the one check of the note's exclusions against what was asked, so
  both keep it. The branch reviewer keeps the request file among its
  inputs.
- **`request.md` carries what an approval approved.** The maintainer's
  account: in many sessions the work is an existing backlog item they
  sanity-check, or the controller expands a brief idea and the operator
  approves; either way the quoted messages hold little of the goal. So
  beside an operator message that approves a proposal, the request file
  quotes the option it approved, and where an asking message points at a
  document (a backlog item, an issue), it names the document's path. The
  quote is the controller's text the operator approved, marked as such.
- **A `Review: branch only` task's concerns become leads.** Any concern
  sent a marked task to its task review, and 114 of 144 implementers
  reported concerns, so 3 of 17 marked tasks completed branch review
  only; 4 of the 14 reviewed anyway drew fixes, all prose defects a branch
  review would plausibly catch. A marked task reporting concerns now
  completes branch review only like one reporting none, its concerns
  reaching the branch reviewer as leads, as on the very-small lane. The
  mark's criterion already excludes tasks whose details something else
  builds on. A failed gate or a `plan changed` re-run still sends it to
  its task review.
- **The branch reviewer's exclusion of the ledger's `## Questions` goes.**
  A section of a file a seat is told to read cannot be withheld: three
  reviewers read it, and no effect on a review is on record. Accepted by
  the maintainer as tentative: a later read showing passes re-raising
  earlier passes' questions reopens it, a file of their own being the
  form that holds.
- **A conflict resolved by hand is a change no pass has read.** One
  landing carried six hand-merged rebase conflicts no reviewer read. A
  conflict the controller resolves by hand, in a rebase or at the merge,
  gets a full-scope branch-review pass on the result before landing.
- **The terminal pass's justification is restated.** Its record rests the
  pass on a 2026-10-12 count (a BLOCKER or MAJOR after the stop in 27 of
  74 campaigns); the re-audit's first reads found one MAJOR in 22 spec
  first passes, and their record corrections changed what happened next
  in 5 of 21 campaigns. The record says the pass's place now rests on its
  record check and on being the one read of the last wave, with both
  counts. No process change.
- **Rulings that change nothing are recorded with their reasons.** The
  very-small lane gets no check for a change outgrowing it: the boundary
  is judgment by nature, and in the two sightings the signals that
  mattered belonged to other mechanisms (a recurring class of finding is
  the fresh look's sign; a test that overwrote live state ran before any
  review on any route). Fresh looks firing at a passage's third patch
  stay a matter of the router's signs, not a trigger.
- **The two text gaps close.** The terminal-pass record states its state
  order when a second read runs, so a resume never redelivers a close
  whose second read is still out. The decision record's sentence on a
  ruling after the last round matches the procedure's ordering.

Premise: the figures are the re-audit's, measured by one reader over one
project's transcripts; the rulings are the maintainer's, of 2026-11-24.

Break: a branch reviewer off the very-small lane no longer restates the
goal, and its report loses the Goal Check section; a marked task's
concerns no longer buy it a task review. Permanent.

## Change list

- **Goal check.** `skills/requesting-code-review/code-reviewer.source.md`
  runs § The goal check only on the very-small lane (a selector as the
  redteam seat's `goal-check`, or the lane text in
  `very-small-lane-review.md` carrying it), with its `### Goal Check`
  report section, the output-format line naming it and the
  `[MANDATE_REMINDER]` slot's mention (`code-reviewer.slots.md`)
  following; standalone mode included.
  Records: `docs/decisions/evidence-and-findings.md`,
  `docs/decisions/branch-review.md`, `docs/decisions/routes.md`,
  `docs/decisions/instruments.md`, `docs/decisions/the-spec.md` where
  they state the branch reviewer's goal check; `README.md`'s mention.
- **Request file.** `skills/brainstorming/SKILL.md` § Workspace
  provisioning, and `skills/redteaming/references/formats.md` "Later
  changes to the ask" for approvals after brainstorm exit; the record
  holding the request's position (`docs/decisions/the-spec.md`).
- **Marked tasks.** `skills/subagent-driven-development/references/task-loop.md`
  (the marked-task paragraph),
  `skills/subagent-driven-development/references/what-a-report-voices.md`
  (where concerns go); records `docs/decisions/task-loop.md` and
  `docs/decisions/branch-review.md`; any other site the consumer sweep
  finds stating that a concern sends a marked task to its task review.
- **Ledger exclusion.** `code-reviewer.source.md` § Read Scoping;
  `docs/decisions/branch-review.md` § Decision, Leads and questions.
- **Hand-resolved conflicts.** `skills/finishing-a-development-branch/SKILL.md`
  (the merge step) and, if a rebase before landing has no home there,
  wherever `crucible:requesting-code-review` decides a full-scope pass is
  owed; the branch-review record.
- **Terminal pass.** `docs/decisions/terminal-pass.md` § Why a pass at all.
- **Text gaps.** `skills/redteaming/references/round-record.md`, the
  terminal-pass special record; `docs/decisions/fix-verification-and-merge.md`,
  "A ruling after the last round".
- **No-change rulings.** `docs/decisions/routes.md` § The very-small lane
  (Why), `docs/decisions/model-roles-and-effort.md` § A fresh look.
- **Backlog.** Delete `goal-check-request-file.md`, `lane-shape.md`,
  `review-mark-overridden.md`, `reviewer-reads-ledger-questions.md` and
  `spec-campaign-close-text-gaps.md`; cut the unruled list ("What the read
  saw and nobody has ruled on") from `skill-rewrite-reaudit.md`, and any
  of its follow-up threads that read a ruled item.
- Every record edit changing a position or its reasoning gets a
  `2026-11-24` line in its `## Changes`. Regenerate templates and agents
  (`python tools/instrument_agents.py write`); update
  `tests/prose-budget.txt`. If the skills' total passes `TOTAL_CAP`, stop
  and ask the operator.

## Acceptance

1. `python -m pytest tests/` passes, the generator's check mode and the
   prose budget included.
2. None of the five backlog files listed above exists on the branch.
3. `git diff master...HEAD` adds a `- 2026-11-24:` line under `## Changes`
   in each of `evidence-and-findings.md`, `branch-review.md`,
   `task-loop.md`, `terminal-pass.md`, `routes.md` and
   `model-roles-and-effort.md` under `docs/decisions/`.

## Out of scope

- Cutting `skill-rewrite-reaudit.md`'s remaining threads to those whose
  answer would change something.
- A rule keeping tests inside the worktree.
- The redteam seat's goal check, and round 1's.
- An install update or trial.
