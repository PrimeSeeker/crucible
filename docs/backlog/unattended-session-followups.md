# Unattended sessions: what the hook's note leaves open

## Observation

Since 2026-11-04 a Claude Code session whose hook environment has
`CLAUDE_CODE_SESSION_ATTENDED=0` gets a short note in place of the router
(`hooks/README.md` § SessionStart injection;
`docs/decisions/session-start-hook.md`).

The variable was measured in the CLI only: 0 in a
  `claude -p` hook, 1 in an interactive session's hook at startup and at
  compaction. IDE extensions, the desktop app and web sessions were not
  measured. A front-end with a person attending that showed 0 would swap
  the router for the note, and nothing visible would say so.

## Follow-up

Measure a front-end where one comes into use. If any attended one shows
  0, replace the hook's keying; consider a person-visible line on the note
  so a misfire gets noticed.
