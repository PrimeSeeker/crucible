# Runtime reference — Claude Code

Host mechanics for this runtime; the skills carry the process rules.

**Instruction files.** This host reads the user-level and the project
`CLAUDE.md`.

**Planning mode.** This host has a plan mode; the router's
brainstorm-before-planning rule covers entering it.

## Operations

- **Load a skill** — invoke it with the Skill tool, by the namespaced name
  the Skill Index lists.
- **Track a checklist** — TodoWrite: one item per checklist entry, moved to
  in-progress and completed as the work moves. Where your tool list has no
  TodoWrite, keep the checklist in your messages.
- **Dispatch a fresh agent** — the Agent tool. A dispatch starts an agent
  carrying none of this session's history, which is the fresh-context
  guarantee the workflows depend on. Name the model every time; an omitted
  model silently inherits the session's.
- **Wait** — a dispatch returns that agent's final report when it finishes,
  and you are notified then. Never predict or paraphrase the result of an
  agent that has not returned.
- **Parallel fan-out** — only where the tasks are genuinely independent: no
  shared state, no ordering, neither reading the other's output. Where that
  holds this host can run several dispatches concurrently; otherwise run
  them one at a time whatever the host permits.
- **Select model** — stated on the dispatch itself; roles below.
- **Edit** — the Edit and Write tools.
- **Shell** — the host shell tool (`Bash`, or `PowerShell` where the
  session registers it).
- **Worktree** — prefer a native worktree tool where the harness exposes
  one; otherwise create one with individual Git invocations through the
  shell operation.

## Model roles

- **Default** — Opus.
- **Bounded** — the Sonnet-class row.
- **Alternate** — Fable.

Never a weak, fast or mini tier, Haiku-class included, nor an earlier
generation: a model the host lists as previous or legacy, or an earlier
Opus or Sonnet version. Every model named here qualifies.
