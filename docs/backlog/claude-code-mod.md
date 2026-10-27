# A Claude Code mod for router injection and a `conserve` tool

## Observation

A Claude Code mod (plugin code running inside the host) could do two jobs
crucible now does with scripts:

- **Router injection.** The mod adds the router and the Claude Code host
  map to the session's context, in place of the bash SessionStart hook
  (`hooks/session-start`).
- **A `conserve` tool.** The redteaming merge's conservation check, now
  `skills/redteaming/scripts/conserve.py`, registered as a tool the
  controller calls.

What it would buy:

- No bash on the session-start path. The bash hook does not serve Windows
  without Git Bash: the host runs the command under PowerShell, where it
  exits nonzero with no crucible message (`hooks/README.md` § Porting to
  another host; unmeasured end to end).
- No interpreter for `conserve`. A host with bash but no usable Python
  loads the router and learns of the missing interpreter only at the
  first `conserve.py` run, where the controller stops. A tool needs
  neither.

Why it is not taken now:

- The port it was first designed into (a JS core, a mod adapter, a CLI
  and an `sh` fallback) came to three delivery paths for one check and a
  concatenation.
- **API stability.** The mod API's own reference (the plugin-authoring
  skill's `reference.md`, Claude Code 2.1.296) says it "is early access and
  moves between releases". A mod is Claude Code only; the bash hook ports
  to another host by one `case` arm.

## Follow-up

Re-open on any of: a host without bash that crucible should serve, a
missing interpreter at `conserve.py` meeting users in practice, or the mod
API leaving early access.

Then, before any design work, run a probe that answers whether a mod can
carry both jobs. It takes a few interactive turns, so a person runs it.

- A throwaway `--plugin-dir` mod. In `session.start` it registers a tool,
  `echo_probe`, whose `tool.call` also runs
  `$.process.run(['git','rev-parse','HEAD'])` and `$.fs.read`.
- It adds a `prompt.context` block of N characters (9k, 20k, 60k), with a
  codeword at the start and one at the end.
- It has a `classic.SessionStart` observer that logs `source`.
- Questions:
  - Do registered tools reach subagents?
  - Is `prompt.context` size-capped?
  - Does it re-fire after `/clear` and after compaction?
  - How much do `$.process` and `$.fs` cover?
  - How stable is the API (`claude plugin validate --strict --json`, the
    version)?
- Record the results in this item.
