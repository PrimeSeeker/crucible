# Runtime reference — Codex

This host reads the user-level `AGENTS.md` in `$CODEX_HOME` (default `~/.codex`; an `AGENTS.override.md` there wins over it) and the project's `AGENTS.md`.

Plan Mode is not the checklist tool below, which is refused while it runs; the router's brainstorm-before-planning rule covers entering it.

## Operations

- **Load a skill** — expand the root alias of the skill's listed `SKILL.md` location and read that file completely before any task action.
- **Track a checklist** — `update_plan`: one step per item, at most one `in_progress`. On codex-cli 0.162.1 it exists only where the Codex config sets `[tools.update_plan]` `enabled = true`; without it, keep the checklist in your messages.
- **Dispatch a fresh agent** — `spawn_agent`, always with `fork_turns: "none"`; omitting it forks the full history.
- **Wait** — `wait_agent` waits for agents' final status and returns it; the final answer also arrives as a notification.
- **Parallel fan-out** — spawn each, then `wait_agent`.
- **Select model** — `model` on the dispatch; roles below.
- **Edit** — `apply_patch`.
- **Shell** — `exec_command`. The dispatch tools are direct tool calls, unreachable from inside a shell command.
- **Worktree** — no native operation: create one with individual Git invocations through the shell. Agents share one working directory, so isolation comes from the worktree, never the dispatch.

## Model roles

Read on codex-cli 0.164.0.

- **Default** — `gpt-6.1-sol`; weak spots: visual and graphics work.
- **Bounded** — `gpt-6.1-terra`.
- **Alternate** — `gpt-6-astra`.

Never a weak, fast or mini tier, Luna-class included, nor a model this host lists as previous, older or legacy (on 0.164.0, `gpt-6-sol` and the 5.x models). Every model named here qualifies.
