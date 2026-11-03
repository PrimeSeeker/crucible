# Runtime reference — Claude Code

**Instruction files** — this host reads the user-level and project `CLAUDE.md`, and a project's `AGENTS.md` where it has no `CLAUDE.md`.

**Planning mode** — this host's plan mode.

## Operations

- **Load a skill** — the Skill tool, by the namespaced name in the Skill Index.
- **Track a checklist** — TodoWrite: one item per entry, moved to in-progress and completed as the work moves. Where your tool list has no TodoWrite, keep the checklist in your messages.
- **Dispatch a fresh agent** — the Agent tool. The agent carries none of this session's history: the fresh-context guarantee the workflows depend on.
- **Wait** — when the agent finishes, the dispatch returns its final report and notifies you.
- **Parallel fan-out** — several dispatches can run concurrently.
- **Select model** — stated on the dispatch; roles below.
- **Edit** — the Edit and Write tools.
- **Shell** — `Bash`, or `PowerShell` where the session registers it.
- **Worktree** — prefer a native worktree tool where the harness exposes one; otherwise individual Git invocations through the shell operation.

## Model roles

- **Default** — Opus.
- **Bounded** — the Sonnet-class row.
- **Alternate** — Fable.

Never a weak, fast or mini tier (Haiku-class included), a model the host lists as previous or legacy, or an earlier Opus or Sonnet version. Every model named here qualifies.
