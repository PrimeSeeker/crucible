Lane: very-small (operator-confirmed 2026-11-01)

# Open items go where the project says

## Request

- "Alright, we need to address the open items issue. Ideas on a
  discoverable default?"
- "Backlog is this repo's feature, people might want not to have it in
  repo. I'd propose memory, but I'm not sure it fits Codex well (per-user
  there instead of per-project)"
- "IDK. Maybe don't have a default at all, keep in workspace and ask the
  user insistently before the deletion if there is no configured
  destination? / I think this as a feature is surprising"
- "Yes, I agree; if the session ends, the workspace doesn't get deleted
  and we're returning to the question naturally. Unless the user asked
  for it, bypassing the normal flow, in which case oh well - not worth
  covering the case"
- Background, the maintainer on 2026-10-30, quoted in
  `docs/backlog/open-items-location.md`: "In retrospect, open items
  stored like this are definitely going to be lost."

## Intent

Crucible keeps no store of its own for open items. They live in the
workspace until the project's own home receives them, or the operator
drops them.

- Where the project's instructions name a home for open items, they go
  there, as now.
- Where none is named, at each point where open items leave the
  workspace — SDD's Finish, an umbrella's landing, an umbrella's closing
  review — the operator is asked where they go, or whether to drop them.
  The workspace is not deleted until that answer: a session that ends
  unanswered returns to the question on its own.
- The ask offers to record the answer in an instruction file the
  operator picks — committed in the project, or private and uncommitted
  — so that it does not recur.
- Brainstorming's context gathering reads the configured home, which is
  what makes open items discoverable.
- This repository names `docs/backlog/` as its home.

## Change list

- `skills/redteaming/references/formats.md`: § Feature folder drops
  `open-items.md` from the roles and from its opening sentence; the
  Lifecycle in § Feature workspace root and layout says items go to the
  configured home or as the operator answers, and deletion waits for it.
- `skills/subagent-driven-development/SKILL.md` § Finish: step 2 asks for
  a home where none is configured, with the offer to record it; step 4
  writes to the home or as answered, and needs that answer; the
  pull-request sentence about `open-items.md` goes.
- `skills/brainstorming/references/umbrellas.md`: the same at Landing
  step 3 and in Closing review's records.
- `skills/brainstorming/SKILL.md` § Context gathering: one clause for the
  configured home.
- `skills/finishing-a-development-branch/SKILL.md`: the pull-request
  question loses its `open-items.md` clause.
- `skills/requesting-code-review/code-reviewer.md`: the reopened-range
  paragraph names items written to an in-repository home instead of
  `open-items.md`; then `python tools/instrument_agents.py write`
  regenerates `agents/`.
- Decision records `docs/decisions/records-and-workspace.md`,
  `umbrellas.md` and `branch-review.md`: the new position, each with a
  `## Changes` line.
- `README.md` and `docs/dual-runtime.md`: match the new behaviour.
- `AGENTS.md`: names `docs/backlog/` as the home for open items; the
  feature-folder paragraph drops `open-items.md`.
- `docs/backlog/open-items-location.md` deleted;
  `docs/backlog/records-retention-config.md` loses its open-items
  paragraph.
- `tests/prose-budget.txt` follows the counts.

## Acceptance

1. `grep -rn "open-items\.md" skills agents README.md AGENTS.md
   docs/dual-runtime.md` finds nothing (15 lines before).
2. `docs/backlog/open-items-location.md` does not exist.
3. `python -m pytest tests/` passes; the agent-generator check and the
   prose budget run inside it.
4. The branch reviewer judges, against the Intent: every route's Finish,
   the very-small lane's included, and both umbrella sites ask where no
   home is configured, and nothing deletes a workspace holding open
   items before an answer; the offer to record names no host-specific
   file (the adapters name the instruction files); the decision records
   state the new position.

## Out of scope

- The never-commit records mode (`records-retention-config.md`), beyond
  the paragraph above.
- Migrating `open-items.md` files projects already hold.
- A SessionStart reminder, and any tracker integration.
- A workspace deleted by an ad-hoc request outside the flow.
