# Slim the decision records, and settle when an edit needs a Changes line

## Observation

- The records in `docs/decisions/` total about 36,600 words, against about
  48,800 in the shipped skills. Their Decision sections restate skill
  procedure in about 1,370 lines. The reference scanner catches a renamed
  or removed heading a record cites, but not changed content, so a skill
  edit can leave a record untrue with no test failing.
- `docs/decisions/decision-records.md` and `AGENTS.md` require a dated
  Changes line for every edit to a record, including edits that change no
  decision, such as a citation fix a renamed heading forces.
- Known slips left from the records' first writing:
  - The rules crucible declined (`docs/decisions/rejected-machinery.md`)
    are restated in `shared-tree.md`, `git-steps.md` and
    `evidence-and-findings.md`. The copies agree today.
  - `routes.md` says "inline implementation" where the very-small lane
    also allows one implementer
    (`skills/subagent-driven-development/references/very-small-lane.md`).
  - `the-spec.md` says "contradiction" without redteaming's "with binding
    content".
  - `authoring-crucible.md` ("the scanner checks it exists") and the
    `tests/test_references.py` docstring state the anchor check without
    its limit: a heading counts as found when the cited text begins with
    it.
  - Most Rejected entries in `plans.md`, `task-loop.md`,
    `adjudication.md`, `branch-review.md` and `test-rules.md` point at Why
    without a why-not phrase.
  - `docs/dual-runtime.md`'s Effort bullet points at "the rules above",
    whose bullet does not name escalation.
- `docs/backlog/second-runtime-seat.md` says no skill text mentions
  cross-runtime seats; `skills/redteaming/SKILL.md` § Panels does.

## Follow-up

- Cut each record's Decision to its positions in a sentence or two, with
  a pointer to the skill heading that holds the procedure; keep Why,
  Rejected and Changes.
- Decide whether a Changes line is required only when a decision or its
  reasoning changes, and state the rule in `AGENTS.md` and
  `docs/decisions/decision-records.md`.
- Fix the slips above on the way.
