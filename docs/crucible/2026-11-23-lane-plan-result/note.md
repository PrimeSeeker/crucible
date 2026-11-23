Lane: very-small (operator-confirmed 2026-11-23)

# A lane note with a plan: checked, and rejected

## Intent

A lane note with a plan is the arrangement for a settled change that
needs several coordinated tasks: no spec campaign, the plan's tasks and
the task loop kept, the same branch review. It was left out, then met the
condition that reopens it, and waited on one check: would the stages it
keeps have caught what such campaigns' first rounds found. The maintainer
asked for that check on the five campaigns already run, and on its result
closed the arrangement as rejected. This change records the result and
the ruling, and changes no skill text.

1. The routes record states the check's result with its limits, and that
   a lane note with a plan is rejected on it, no longer waiting.
2. The re-audit item no longer carries the check, and says what was
   decided.
3. One observation from the same read takes a backlog item of its own:
   on those five campaigns most of what the round-0 pre-pass found, the
   implementers and their tests would have met anyway. The item designs
   no change to round 0.

Outcomes the reviewer judges, since no check can:

- Every figure is an aggregate; nothing names the project the campaigns
  ran on, its features or its content.
- The result is stated as strongly as its count supports: five campaigns
  of one project and one operator on crucible 0.33.1, selected because
  each stopped after one round, and every verdict on who would have met a
  finding a reader's judgment of what did not happen.
- The ruling is recorded as an agent's recommendation the maintainer
  accepted, with the case against as it was put.

Premise, measured: one reader seat on the default role read the round
records, ledgers and reviews of the five campaigns and judged each
BLOCKER or MAJOR of rounds 0 and 1. The transcripts are not in this
repository.

Break: none.

## Change list

- `docs/decisions/routes.md` § Separable choices: the check's result and
  the ruling, in place of the sentence saying what the arrangement waits
  on; the Rejected bullet; a `## Changes` line.
- `docs/backlog/skill-rewrite-reaudit.md`: the check's paragraph goes;
  the first Observation bullet says the arrangement was checked and
  rejected.
- `docs/backlog/pre-pass-on-settled-changes.md`: new.

## Acceptance

1. `python -m pytest tests/` passes.
2. `git diff --name-only master...HEAD` lists only paths under `docs/`.
3. `git ls-files docs/backlog/pre-pass-on-settled-changes.md` prints one
   path.
4. `git diff master...HEAD -- docs/decisions/routes.md` adds a line
   beginning `- 2026-11-23:`.

## Out of scope

- Any change to round 0, to the routes, or to any skill text.
- Building or designing a lighter campaign for settled changes.
- The other points the re-audit item holds.
