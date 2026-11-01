# A Claude Code mod for router injection

## Observation

A Claude Code mod (plugin code running inside the host) could add the
router and the Claude Code host map to the session's context, in place of
the bash SessionStart hook (`hooks/session-start`).

What it would buy: no bash on the session-start path. The bash hook does
not serve Windows without Git Bash: the host runs the command under
PowerShell, where it exits nonzero with no crucible message
(`hooks/README.md` § Porting to another host; unmeasured end to end).

Why it is not taken now:

- The port it was first designed into (a JS core, a mod adapter, a CLI
  and an `sh` fallback) came to three delivery paths for one
  concatenation and a check since retired (merge conservation).
- **API stability.** The mod API's own reference (the plugin-authoring
  skill's `reference.md`, Claude Code 2.1.296) says it "is early access and
  moves between releases". A mod is Claude Code only; the bash hook ports
  to another host by one `case` arm.

## Follow-up

Re-open on either of: a host without bash that crucible should serve, or
the mod API leaving early access.

Then, before any design work, run a probe that answers whether a mod can
carry the job. It takes a few interactive turns, so a person runs it.

- A throwaway `--plugin-dir` mod. It adds a `prompt.context` block of N
  characters (9k, 20k, 60k), with a codeword at the start and one at the
  end, and reads a file of its own with `$.fs.read`.
- It has a `classic.SessionStart` observer that logs `source`.
- Questions:
  - Is `prompt.context` size-capped?
  - How much does `$.fs` cover?
  - Does it re-fire after `/clear` and after compaction?
  - How stable is the API (`claude plugin validate --strict --json`, the
    version)?
- Record the results in this item.
