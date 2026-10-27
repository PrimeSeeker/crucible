# Supported host versions, and the smallest publishable core

## Observation

- Crucible depends on undocumented host behaviour that drifts between
  releases, such as Claude Code's write filter on subagent report file
  names (measured on 2.1.289). The docs name the versions crucible was
  tested on (Claude Code 2.1.310, codex-cli 0.162.1) but no supported
  range, and the suite launches no model, so host drift shows only in real
  use. No probe set exists to catch it.
- The skills' Markdown is about 315 KB, against about 279 KB for upstream
  superpowers when last measured. Upstream's guidance is that
  project-specific workflow belongs in a separate plugin.

## Follow-up

- Decide the smallest core worth publishing against optional profiles.
- State the supported host versions, and decide who detects host
  regressions, and how.
