# Codex status after the 6.2 model line

Lane: very-small (operator-confirmed 2026-11-27)

## Intent

Crucible's public statement of its Codex support says "experimental" and
reports two checks failed on codex-cli 0.162.1. Since then Codex has
released a new model line, which its model list puts first, and the
statement no longer tells a newcomer what to expect. This change brings the
statement, and the decision records it rests on, up to what was measured on
2026-11-27 and to the maintainer's ruling on it. It changes documents only:
no skill, adapter, template, hook, tool or test, so no session behaves
differently and no version moves.

The premise was measured (codex-cli 0.172.0, crucible 0.38.0-rc.3, fresh
`codex exec` sessions at medium reasoning effort, one small feature request
each, in a scratch repository whose instruction file does not mention
crucible; tool calls read from the event stream, not the sessions' own
accounts):

- `gpt-6.2-sol`, the first model Codex lists: six sessions. All six read
  the router and brainstorming, four of them after one earlier command,
  which listed or checked the repository in three and searched Codex's own
  memory file in two. Five then edited the code without the design
  approval brainstorming's gate requires; one stopped and asked for it.
  Three of the five ran each in a clone of its own; the other two shared
  one repository with the session that stopped.
- `gpt-6.1-sol`, the default role in the Codex host map: three sessions,
  each in its own clone. All three read the router first and stopped to
  ask for the approval; none edited.
- Codex's model list on 0.172.0 describes `gpt-6.1-sol` and `gpt-6-astra`,
  the host map's default and alternate roles, as previous generation.
- Not measured: `gpt-6.2-astra`; any request but the one; an interactive
  session; anything past the design gate; a review seat on either line.

What a reader of the result should find, for the reviewer to judge:

- The README and `docs/codex.md` state Codex's two uses separately. As a
  host it is unmaintained, no longer "experimental": it installs and its
  sessions reach the router, the design gate mostly failed on the model
  Codex now lists first, with the counts and their conditions, and no
  further measurement is planned. A review seat started from a Claude Code
  session is the maintained use.
- They recommend no workaround. That the gate held on the host map's
  default-role model is stated as a measurement, with that model's label,
  not as the way to run crucible on Codex.
- The README names no model, as the claude-ism scanner requires of it.
- The Codex host map's roles stay as read on codex-cli 0.164.0, against
  the floor's own test (a model the host labels previous generation), and
  the model-roles record says so with the maintainer's reason: on the
  first reports the new line is treated as unfit for a review-driven loop,
  until further evidence. What the roles govern in practice is the seat
  started from Claude Code, which takes the default role's model.
- The runtime-adapters record carries the measurement, its limits, the
  public roundup of user reports that prompted it, marked as anecdotal,
  and the ruling.
- Nothing committed describes a private install: no config values, plan or
  quota.

No break: nothing the base does today stops working.

## Change list

- `README.md`: the opening sentence and the hosts line of § Platforms and
  prerequisites state Codex as a host as unmaintained; § Codex rewritten
  around the two uses and the measurement, the two checks failed on
  codex-cli 0.162.1 kept.
- `docs/codex.md`: the opening paragraph and § Status rewritten the same
  way: the label, the measurement, what the host map's models are and why
  they stay, the earlier failed checks, what is untested.
- `docs/decisions/runtime-adapters.md`: the Codex position in Decision;
  a paragraph under § Codex as a host; a line under Rejected; a Changes
  line.
- `docs/decisions/model-roles-and-effort.md`: the floor's exception on
  Codex in Decision; a paragraph in Why; a Changes line.
- `docs/decisions/publication.md`: the clause naming how the README states
  Codex.
- `docs/backlog/codex-read-only-writes.md`, new: five of the measured
  sessions edited a tracked file though started with `-s read-only`, the
  flag crucible's seat on another host is started with; cause not
  established.
- `docs/backlog/codex-host-unmaintained.md`, new: remove the Codex host or
  revive it, and when to decide; what the repository still carries for
  it.
- `docs/backlog/codex-seat-model-trial.md`, new: a review seat on the new
  line is untried; the comparison that would be the further evidence.

## Acceptance

- `python -m pytest tests/` passes.
- `git diff --stat master...HEAD -- skills agents hooks tools tests
  .claude-plugin .codex-plugin` prints nothing.
- `docs/decisions/runtime-adapters.md` and
  `docs/decisions/model-roles-and-effort.md` each have a line under
  `## Changes` dated 2026-11-27.
- `docs/backlog/codex-read-only-writes.md`,
  `docs/backlog/codex-host-unmaintained.md` and
  `docs/backlog/codex-seat-model-trial.md` exist.

## Out of scope

- The Codex host map (`skills/using-crucible/references/codex.md`): its
  roles and its floor sentence stay as they are; that the sentence is now
  untrue by Codex's labels joins the backlog item on the host.
- Any mechanism to make the gate hold on the new line.
- Measuring `gpt-6.2-astra`, an interactive session, a whole feature or a
  review seat on the new line.
- Establishing why `-s read-only` let the edits through.
- Removing Codex as a host.
