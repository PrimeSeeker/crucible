# Dispatch reference — Codex

Dispatch mechanics for a skill that starts seats on this runtime; the host
map beside this file, `codex.md`, carries the rest.

- **Dispatch an instrument** — the template path, since a plugin cannot
  ship Codex agent roles: fill the slot card and the template and dispatch
  the whole through the host map's **Dispatch a fresh agent** —
  `spawn_agent` with `fork_turns: "none"`.
- **Resume an agent** — `followup_task` gives an agent you spawned a new
  task and triggers a turn; `send_message` passes a message without one.
  Address it by the canonical task name recorded at spawn — record that
  identity before relying on continuation.
- **Select effort** — `reasoning_effort` on the dispatch, used only on the
  operator's request. `ultra` is a reasoning level, not a model, and
  carries automatic task delegation, which breaks a seat's no-delegation
  instruction. With `reasoning_effort` omitted and the model named, a
  seat runs at `default_subagent_reasoning_effort` from the `[agents]`
  table of the operator's Codex config, else at its model's default
  (`low` for the default role's model), never at your own effort
  (measured on codex-cli 0.162.1). Before your first dispatch in a
  session, read `config.toml` once in the Codex home that holds this
  plugin: the directory above `plugins/cache/` in the plugin root's
  path, not `~` or `CODEX_HOME`, which a Windows sandbox maps to its own
  account. If you cannot read it, or the key is absent, tell the
  operator which, that their seats run at the model's default unless the
  key is set, and recommend `high`. An override is accepted only
  with `fork_turns` at `"none"` or a turn count (a
  full-history fork inherits model and effort); an unsupported effort is
  rejected, naming the levels that model supports.
