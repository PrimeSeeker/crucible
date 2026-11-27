# Codex status after the 6.2 model line

Lane: very-small (operator-confirmed 2026-11-27)

## Intent

Crucible's public statement of its Codex support says "experimental" and
reports two checks failed on codex-cli 0.162.1. Since then Codex has
released a new model line, which its model list puts first, and the
statement no longer tells a newcomer what to expect. This change brings the statement,
and the two decision records it rests on, up to what was measured on
2026-11-27. It changes documents only: no skill, adapter, template, hook,
tool or test, so no session behaves differently and no version moves.

The premise was measured (codex-cli 0.172.0, crucible 0.38.0-rc.3, fresh
`codex exec` sessions at medium reasoning effort, one small feature request
each, in a scratch repository whose instruction file does not mention
crucible; tool calls read from the event stream, not the sessions' own
accounts):

- `gpt-6.2-sol`, the first model Codex lists: six sessions. All six read
  the router and brainstorming, three of them after one command listing or
  checking the repository and one after a search of Codex's own memory
  file. Five then edited the code without the design
  approval brainstorming's gate requires; one stopped and asked for it.
  Three of the five ran each in a clone of its own; the other two shared
  one repository with the session that stopped.
- `gpt-6.1-sol`, the default role in the Codex host map: three sessions,
  each in its own clone. All three read the router first and stopped to
  ask for the approval; none edited.
- Codex's model list on 0.172.0 describes `gpt-6.1-sol` and `gpt-6-astra`,
  the host map's default and alternate roles, as previous generation.
- Not measured: `gpt-6.2-astra`; any request but the one; an interactive
  session; anything past the design gate.

What a reader of the result should find, for the reviewer to judge:

- The README and `docs/codex.md` say that on the model Codex now lists
  first the design gate mostly failed, with the counts and their conditions, say
  that it held on the host map's default-role model, and tell a Codex user
  to run crucible on the host map's models while Codex offers them.
- They say that no further measurement is planned for now.
- The README names no model, as the claude-ism scanner requires of it.
- The Codex host map's roles stay as read on codex-cli 0.164.0, against
  the floor's own test (a model the host labels previous generation), and
  the model-roles record says so with the reason: the measurement above
  for the default role, and for the alternate that the new line's other
  model was not run. A seat started from Claude Code takes the default
  role's model, so it stays off the new line as well.
- The runtime-adapters record carries the measurement, its limits, and the
  public roundup of user reports that prompted it, marked as anecdotal.
- Nothing committed describes a private install: no config values, plan or
  quota.

No break: nothing the base does today stops working.

## Change list

- `README.md` § Codex: the status rewritten around the measurement; the
  two checks failed on codex-cli 0.162.1 kept. § Platforms and
  prerequisites: the Codex host line names the version last measured.
- `docs/codex.md`: the opening paragraph points at § Status and the
  version last measured; § Status rewritten: the measurement, which model
  to run crucible on and how, the earlier failed checks, what is untested,
  and that no further measurement is planned.
- `docs/decisions/runtime-adapters.md`: the Codex position in Decision;
  a paragraph under § Codex as a host; a Changes line.
- `docs/decisions/model-roles-and-effort.md`: the floor's exception on
  Codex in Decision; a paragraph in Why; a Changes line.
- `docs/backlog/codex-read-only-writes.md`, new: five of the measured
  sessions edited a tracked file though started with `-s read-only`, the
  flag crucible's seat on another host is started with; cause not
  established.

## Acceptance

- `python -m pytest tests/` passes.
- `git diff --stat master...HEAD -- skills agents hooks tools tests
  .claude-plugin .codex-plugin` prints nothing.
- `docs/decisions/runtime-adapters.md` and
  `docs/decisions/model-roles-and-effort.md` each have a line under
  `## Changes` dated 2026-11-27.
- `docs/backlog/codex-read-only-writes.md` exists.

## Out of scope

- The Codex host map (`skills/using-crucible/references/codex.md`): its
  roles and its floor sentence stay as they are.
- Any mechanism to make the gate hold on the new line.
- Measuring `gpt-6.2-astra`, an interactive session or a whole feature.
- Establishing why `-s read-only` let the edits through.
- Dropping Codex as a host.
