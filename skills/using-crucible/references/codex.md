# Runtime reference — Codex

Host mechanics for this runtime; the skills carry the process rules.

**Instruction files.** This host reads the user-level `AGENTS.md` in its
home directory (`$CODEX_HOME`, default `~/.codex`; an `AGENTS.override.md`
there wins over it) and the project's `AGENTS.md`.

**Planning mode.** Plan Mode is not the checklist tool below, which is
refused while it runs; the router's brainstorm-before-planning rule covers
entering it.

## Operations

- **Load a skill** — expand the root alias of the skill's listed
  `SKILL.md` location and read that file completely before any task action.
- **Track a checklist** — `update_plan`: one step per item, at most one
  `in_progress`. On codex-cli 0.162.1 it exists only where the Codex
  config sets `[tools.update_plan]` `enabled = true`; without it, keep the
  checklist in your messages.
- **Dispatch a fresh agent** — `spawn_agent` with `fork_turns: "none"`, so
  the agent gets your task text and none of this session's history. The
  fresh-context guarantee is never left to a host default: with
  `fork_turns` omitted the host forks the full history. Name the model
  every time.
- **Wait** — `wait_agent` waits for agents to reach a final status and
  returns it; the final answer also arrives as a notification. Never
  predict or paraphrase the result of an agent that has not returned.
- **Parallel fan-out** — only where the tasks are genuinely independent: no
  shared state, no ordering, neither reading the other's output. Where that
  holds, spawn each and then `wait_agent`; otherwise run them one at a time
  whatever the host permits.
- **Select model** — `model` on the dispatch; roles below.
- **Edit** — `apply_patch`.
- **Shell** — `exec_command`. The dispatch tools above are direct tool
  calls and cannot be reached from inside a shell command.
- **Worktree** — no native worktree operation here: create one with
  individual Git invocations through the shell operation. With one shared
  working directory, isolation comes from the worktree, never from the
  dispatch.

## Model roles

Read on codex-cli 0.164.0.

- **Default** — `gpt-6.1-sol`.
- **Bounded** — `gpt-6.1-terra`.
- **Alternate** — `gpt-6-astra`.
- **Weak spots of the default role** — visual and graphics work.

Never a weak, fast or mini tier, Luna-class included, nor a model this
host lists as previous, older or legacy (on 0.164.0, `gpt-6-sol` and the
5.x models). Every model named here qualifies.
