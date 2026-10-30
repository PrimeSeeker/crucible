# Where open items go

## Observation

- **The default.** The skills write a feature's work left open to
  `open-items.md` in its feature folder, and an umbrella's to
  `open-items.md` in the umbrella's folder at its landing and after its
  closing review. A project's instructions that name another home for
  open items override the file. The skills state it in
  `skills/redteaming/references/formats.md` § Feature folder (the file's
  role) and § Feature workspace root and layout (the Lifecycle
  paragraph), `crucible:subagent-driven-development` § Finish (step 4),
  and `skills/brainstorming/references/umbrellas.md` § Landing and
  § Closing review.
- **Nothing reads the file again.** A feature folder is frozen once its
  feature ships, and no skill step reads a shipped feature's
  `open-items.md`. The one reader the skills name is a feature started
  to fix an umbrella's closing-review findings, which takes the file as
  its incoming document.
- **The maintainer's view (2026-10-30)**, on a feature's open items
  stored in that file: "In retrospect, open items stored like this are
  definitely going to be lost. Backlog, please, we'll find a better
  location later."
- **In this repository** `AGENTS.md` keeps the default, an open item
  becoming a backlog item on the operator's word. The audit-corrections
  feature (2026-10-30) wrote no `open-items.md`: on the maintainer's
  word, its work left open went to `docs/backlog/`.

## Follow-up

- Find a home for open items where they are seen again. The question is
  open: where that is, and whether the skills' default and this
  repository's instructions change with it.
