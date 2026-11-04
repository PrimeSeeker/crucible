# Record wording slips

## Observation

Two decision records state a position in the wrong place. Neither changes a
decision, and the skill text each describes is right.

- **`docs/decisions/authoring-crucible.md`, the retired re-open trigger.** Its
  Why closes "An agent's proposal, which the maintainer accepted", beside the
  sentence that the first clause has no replacement. The maintainer accepted
  the retirement on 2026-11-03 and left that it stands without a replacement
  to the agent on 2026-11-05. The Changes line says so; the Why does not
  (`docs/decisions/decision-records.md`).
- **`docs/decisions/records-and-workspace.md`, commit conventions.** The
  Decision says only that a pull request puts the repository's conventions
  first. Reading them before a feature's first commit and handing them to
  implementers appear in the Why and the Changes line.

## Follow-up

Add the delegated clause to the first Why, and to the second Decision one
sentence pointing at `crucible:using-git-worktrees`. Do each with the next edit
to its record.
