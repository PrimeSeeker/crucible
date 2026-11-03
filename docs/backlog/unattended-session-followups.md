# Unattended sessions: what the hook's note leaves open

## Observation

Since 2026-11-04 a Claude Code session whose hook environment has
`CLAUDE_CODE_SESSION_ATTENDED=0` gets a short note in place of the router
(`hooks/README.md` § SessionStart injection;
`docs/decisions/session-start-hook.md`).

- **The failure contract.** With the variable at 0 the hook reads neither
  the router nor the host map. On a broken install it exits 0 with a note
  naming a host map that is missing, where `hooks/README.md` says any
  missing router or host-map file means one `crucible: router not loaded`
  line and exit 1.
- **The allowlist's reason.** The `claude` entry for `hooks/session-start`
  in `tests/claudeism-allowlist.txt` justifies only the `claude-code`
  argument; the script's comment now also says `claude -p`.
- **Other front-ends.** The variable was measured in the CLI only: 0 in a
  `claude -p` hook, 1 in an interactive session's hook at startup and at
  compaction. IDE extensions, the desktop app and web sessions were not
  measured. A front-end with a person attending that showed 0 would swap
  the router for the note, and nothing visible would say so.

## Follow-up

- Check the host map's file in the note's branch, or qualify the README
  sentence.
- Widen the allowlist entry's reason, or reword the comment.
- Measure a front-end where one comes into use. If any attended one shows
  0, replace the hook's keying; consider a person-visible line on the note
  so a misfire gets noticed.
