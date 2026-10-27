# Dispatch reference — Claude Code

Dispatch mechanics for a skill that starts seats on this runtime; the host
map beside this file, `claude-code.md`, carries the rest.

- **Dispatch an instrument** — the Agent tool with `subagent_type`
  `crucible:<name>` for the instrument the skill names, the model named
  explicitly, and the filled slot card as the whole prompt; the agent
  already carries the template's fixed text. If this host does not offer
  `crucible:<name>`, fill the slot card and the template and dispatch them
  together through the host map's **Dispatch a fresh agent**.
- **Resume an agent** — send a follow-up to the agent identity you recorded
  at dispatch, where the harness exposes one; its context is intact. Where
  it does not, dispatch fresh with the requirements, the report-file path
  and the open findings — the report file is the persistent memory either way.
- **Select effort** — the Agent tool's `effort` setting, used only on the
  operator's request.
- **Report-name filter** — this host's Write tool refuses a subagent's
  write to any file whose basename matches
  `^(REPORT|SUMMARY|FINDINGS|ANALYSIS).*\.md$`, case-blind ("Subagents
  should return findings as text, not write report files"), whatever the
  dispatch authorized. The host also advises subagents in prose to return
  findings as text instead of writing report files, so an instrument can
  hand back its report without having written it.
- **Compaction** — the host compacts the controller's context automatically
  near its window limit; the operator may set an earlier point with
  `/autocompact` or `CLAUDE_CODE_AUTO_COMPACT_WINDOW`. Expect compaction
  at that point, not at the window limit, and rehydrate from the records
  as after any compaction.
