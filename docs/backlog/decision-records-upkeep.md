# Slim the decision records, and settle when an edit needs a Changes line

## Observation

- At `a709dbc` the records in `docs/decisions/` total 60,484 words,
  against 65,636 in the shipped skills (whitespace-separated tokens in
  `*.md`, as `tests/prose-budget.txt` counts them). Their Decision
  sections run to about 1,940 non-blank lines, much of it restating
  skill procedure. The reference scanner catches a renamed
  or removed heading a record cites, but not changed content, so a skill
  edit can leave a record untrue with no test failing.
- `docs/decisions/decision-records.md` and `AGENTS.md` require a dated
  Changes line for every edit to a record, including edits that change no
  decision, such as a citation fix a renamed heading forces.
- Known slips, most left from the records' first writing:
  - The rules crucible declined (`docs/decisions/rejected-machinery.md`)
    are restated in `shared-tree.md`, `git-steps.md` and
    `evidence-and-findings.md`. The copies agree today.
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
  - Decision paragraphs that restate the skill text clause by clause:
    in `umbrellas.md`, "Edited by weight until it closes", "Marks, not
    derived state" and "One closing review, a step and not a gate"
    (`skills/brainstorming/references/umbrella-children.md` § Edits,
    § Marks; `skills/brainstorming/references/umbrellas.md` § Closing,
    § Closing review); in `records-and-workspace.md`, "Work
    left open" and "Finish" (`crucible:subagent-driven-development`
    § Finish, `crucible:finishing-a-development-branch`).
  - Two bases in `routes.md` (at `a709dbc`, lines 143 and 255) read
    "the maintainer's preference, for the …", a phrasing older than the
    rule that attributes a basis from the brainstorm decision record's
    proposer and status (`decision-records.md`); neither was checked
    against a decision record entry.
  - `records-and-workspace.md` states that a home for open items
    recorded in a user-level file counts as the project's only in its
    Changes line; its Decision ("Work left open") and "What a project
    may change" leave it out.

## Follow-up

- Cut each record's Decision to its positions in a sentence or two, with
  a pointer to the skill heading that holds the procedure; keep Why,
  Rejected and Changes.
- Decide whether a Changes line is required only when a decision or its
  reasoning changes, and state the rule in `AGENTS.md` and
  `docs/decisions/decision-records.md`.
- Fix the slips above on the way.
