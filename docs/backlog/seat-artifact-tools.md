# Seats the artifact-tool deny list does not reach

## Observation

- Since 2026-11-24 the generated instrument agents deny the host's four
  artifact tools on Claude Code, after eight review agents used the
  artifact tool's publish call with edits on their own reports
  (`docs/decisions/instruments.md`).
- Whether the host honours the list for a plugin's agents is unverified:
  the deny list reaches no session until an install update, and the one
  measurement, on Claude Code 2.1.330, showed only that an agent whose list
  names tools absent from the session still launches.
- The list reaches only the generated agents. Seats on the template path
  (Claude Code's fallback when an instrument agent is not offered) and the
  seats a controller composes itself (the pre-pass, adjudicators, a fresh
  look, readers) keep the tools; no incident has involved one.

## Follow-up

- At the first session after an install update carrying the list, check
  that a crucible instrument agent launches and that its tool list lacks
  the four tools; if launches fail, revert the list.
- If a template-path or composed seat calls an artifact tool, decide how to
  reach it: one line in the seat rules, or a sentence in the composed
  dispatch.
