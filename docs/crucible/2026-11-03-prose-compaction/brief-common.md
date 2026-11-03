# Prose compaction — shared brief

Crucible is a process plugin: skills that instruct Claude Code and Codex
agents through brainstorm, spec campaign (redteaming), plan, subagent-driven
execution, branch review and finish. Its skill text lives under `skills/` in
the worktree (the repo
root for every path below).

- About 60 hand-edited files (57,177 words at the start; structural steps have since moved text and added five references: `skills/subagent-driven-development/references/review-terms.md`, `skills/redteaming/references/round-record.md`, `skills/redteaming/references/premise-asks.md`, `skills/brainstorming/references/umbrella-children.md`, `skills/using-git-worktrees/references/git-fallback.md`). The seven dispatch templates (`*-prompt.md`, `code-reviewer.md`) are generated from their `*.source.md` plus sections spliced from `skills/subagent-driven-development/references/seat-rules.md` and `review-terms.md` (`[[include <heading>]]` lines); `agents/` is generated too. Slot cards (`*.slots.md`) are what a
  controller fills to dispatch a seat.
- File inventory with words, headings and where each heading is cited:
  `.crucible/prose-compaction/corpus-map.json`.
- Which files a controller loads on each route, by phase:
  `docs/crucible/2026-11-03-compaction-fit/resident-tokens.json`; the
  latest per-route token counts: `resident-tokens.md` beside it.
- Authoring rules for this repo: `AGENTS.md` (already in your context),
  `docs/authoring.md`, and the Size and placement bullet of
  `skills/writing-skills/SKILL.md`.
- Why rules exist (incidents, measurements, trade-offs):
  `docs/decisions/*.md`.

**The goal.** Cut the tokens agents read while running crucible — what a
controller loads per run and what seats read — as far as reasonably
achievable, while keeping crucible's functionality. Words are a proxy for
tokens. The operator judges the skills somewhat over-detailed and expects
information density can rise; restructuring is in scope. Minor functional
losses are acceptable where the saving justifies them (some accumulated
details may not be worth keeping); significant losses are not. Every loss
is named, never hidden.

**Hard constraints on you.** You are read-only on the repository: no edits,
no git commands that change anything (checkout, commit, stage, stash,
branch). Write files only where your task says. Start no agents or
subagents of your own. Publish nothing (no claude.ai artifacts, no posts).
Call no model API.
