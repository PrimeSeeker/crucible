# Runtime adapters

## Decision

**One skill tree, an adapter pair per host.** One canonical skill tree
serves Claude Code and Codex; no host gets a copied or forked workflow,
and the one generated artifact is Claude Code's instrument agents
(`docs/decisions/instruments.md`). Each host's mechanics live in its
adapter, a pair of files under `skills/using-crucible/references/`:

- the **host map** (`claude-code.md`, `codex.md`): the instruction files
  the host reads, its planning mode, the operations (load a skill, track
  a checklist, dispatch a fresh agent, wait, parallel fan-out, select
  model, edit, shell, worktree) and the Model roles. Every session reads
  it: on Claude Code the SessionStart hook inlines it, and a Codex session
  reads it from its path.
- the **dispatch reference** (`claude-code-dispatch.md`,
  `codex-dispatch.md`): dispatch an instrument, resume an agent and select
  effort, and on Claude Code the report-name filter and compaction. SDD,
  redteaming and requesting-code-review read it when they start and again
  after compaction.

The router's § Runtime reference defines the pair as the runtime adapter.
An adapter maps operations and may not redefine workflow policy: a rule
that would read differently on the two hosts belongs in neither
(`docs/dual-runtime.md` § The separation). Adapter text carries no
reference into crucible's own repository. Some host-neutral rules are
still restated there (never predicting an agent's result, fan-out
independence, effort only on request); moving them out is
`docs/backlog/skill-text-rewrite.md`'s. Host mechanics stay in the
adapter pair, and model names in it and the generator's alias map; the
claude-ism scanner checks the rest of the shipped text for host-specific
terms against its allowlist (`AGENTS.md`, Skills stay runtime-neutral;
one sanctioned exception is in `docs/decisions/worktrees.md`).

**Codex: experimental, on the CLI.** Codex is a native host runtime, a
plugin reading the same tree. It is labelled experimental on the CLI,
the one surface tested; the desktop app and the IDE extension are neither
tested nor maintained, and are assumed similar enough for the skills
(`docs/codex.md` § Status). On Codex:

- crucible registers no hook: `.codex-plugin/plugin.json` declares
  `"hooks": {}`, exactly, and a session reaches crucible through skill
  discovery and the router's instruction to read the host map from its
  path;
- instruments go by the template path, since a plugin cannot ship Codex
  agent roles;
- the checklist tool, `update_plan`, exists on codex-cli 0.162.1 only
  where the config turns it on; the host map gives a fallback;
- the adapter has no operation for closing an agent;
- crucible's install sets no `[features] multi_agent` key: it is on by
  default on codex-cli 0.163.0.

**The Codex guide.** `docs/codex.md` is what a Codex user follows:
install, the two config keys (seat effort, the checklist tool), one rule
(no other router on), a check that crucible is the only router, the
routing check, the status, and rollback.

## Why

### One tree, adapters by reader

On 2026-08-15 Codex became a supported host on one condition: one
canonical tree, with adapters that map host mechanics and may not
redefine policy, so the workflows read the same on both hosts. (Basis:
judgment, accepted by the maintainer.)

The adapter split by reader on 2026-10-07. The session-start envelope was
then 8,412 characters against upstream's 3,051-character router
(`superpowers/skills/using-superpowers/SKILL.md` at v6.2.0), most of the
gap the Claude Code adapter, which mixed the host map every session needs
with procedure only a dispatching controller uses. The host map stayed
in every session, Model roles included so that every session that
dispatches keeps the floor; the dispatch procedure went to the second
file, read by the skills that dispatch. (Basis: measured; judgment,
accepted by the maintainer.)

Restatements leave the adapters as they are found. On 2026-10-12 the
Codex reference dropped a paragraph restating crucible's interpreter
policy; on 2026-10-20 the Claude Code dispatch reference dropped its
restatement of the escalation rule, which
`skills/subagent-driven-development/references/dispatch-composition.md`
§ Models and effort and SDD's Models section own. Codex's matching
sentence stayed while it stated a host fact, that the bounded role used
the default role's model there, and went on 2026-10-27, when the bounded
role moved to a model of its own (`docs/decisions/model-roles-and-effort.md`).
(Basis: judgment, accepted by the maintainer.)

### Codex as a host

On 2026-08-06 Codex was to be an optional extension: reached from inside
a Claude Code session through a subprocess bridge, both sampled arms had
failed mechanically, on a missing CLI and on a 10-minute shell cap. On
2026-08-15 that evidence was read as the bridge's, not Codex's: a
natively registered plugin has neither failure, and codex-cli 0.146.1
offered a fresh-context dispatch with explicit history control, agent
continuation and per-dispatch model and effort. (Basis: measured;
judgment, accepted by the maintainer.)

Support was declared at merge, while the design left the activation gate
to the operator, post-merge and deferrable; no workflow step scheduled
it, and it ran first on 2026-10-15, on codex-cli 0.162.1. Of three fresh
sessions given a feature request in a repository whose instruction file
did not mention crucible, one read the target file before the router, and
two of three followed the process, against Codex's own base prompt, which
tells the model to "bias towards action" (the phrase is in the codex-cli
0.163.0 binary). The
smoke passed loading a skill, a dispatch and continuing a seat from a new
process, and failed the checklist. The maintainer kept the gate as
written and labelled Codex experimental, from options an agent put, so a
later run that passes can lift the label. (Basis: measured; judgment,
accepted by the maintainer.)

The surfaces are the maintainer's call: crucible is maintained on the
Codex CLI only, and the desktop app and the IDE extension are assumed to
be similar enough for skill purposes. That is an assumption, not
evidence, and the desktop app can bundle its own Codex, older than the
CLI. (Basis: the maintainer's preference.)

The template path follows from a probe on codex-cli 0.157.1 (2026-09-28):
roles loaded from the Codex home, a trusted project and the config, never
from a plugin (`docs/backlog/codex-agent-role-install.md`). `update_plan`
was off by default on 0.162.1; with `[tools.update_plan]` `enabled = true`
a two-item call was accepted, and whether it tracked the items was not
observed. As far as a session's own listing of its tools showed on
0.162.1 (spawn, wait, follow-up, message, interrupt, list), no tool
closes an agent, and a completed seat continues by `followup_task`, so
upstream's instruction to close reviewer agents has nothing to map to;
its Codex App finishing section concerns the desktop app, out of scope
with it (`superpowers/skills/using-superpowers/references/codex-tools.md`
at v6.2.0). (Basis: measured; external, for upstream.)

The same upstream file opens with a prerequisite,
`[features] multi_agent = true`, to enable the agent tools. On codex-cli
0.163.0, `codex features list` prints `multi_agent  stable  true` with
no such key in the config (2026-10-20), so `docs/codex.md` sets none.
(Basis: measured; external, for upstream.)

### No hook on Codex

Codex first registered the same SessionStart hook as Claude Code
(2026-08-15). An isolated probe on codex-cli 0.160.0 (2026-10-05) found
that Codex's command hook has no `args` field, so crucible's registration
ran a bare interpreter and never started the handler: no Codex session
had had the router injected. A single command string does run, but a
hook was not needed. Codex already routes through skill discovery and the
router's fallback, with a known gap: a session that never reads the
router runs without crucible. Upstream dropped its own Codex SessionStart
hook in v6.1.0: "Codex reliably triggers skills on its own, and the
bootstrap hook made the UX worse rather than better"
(`superpowers/RELEASE-NOTES.md` at v6.2.0). The maintainer ruled: "we
don't need the sessionstart hook". (Basis: measured; external; the
maintainer's preference.)

The manifest's value is exactly `{}` because an absent field makes Codex
auto-discover `hooks/hooks.json` and run it (measured on codex-cli
0.160.0, Windows 11); upstream's v6.1.1 release notes report the same
fallback for an absent field, `[]` and an empty list. The registration recipe and
the dormant provenance tool kept for a future Codex hook were deleted on
2026-10-07, since no flow used them. A need for a Codex hook would reopen
this, starting from a fresh measurement of the hook command's shape on
the Codex release at hand. (Basis: measured; external; judgment, accepted
by the maintainer.)

### The Codex guide

On 2026-10-19 `docs/codex.md` replaced a cutover runbook. Its flip
record, three obligations, inventory cross-product, four-capability smoke
and first-feature evaluation served one cautious cutover onto a project
already in use; a newcomer installing crucible needs the install, the
config keys, the one-router rule and its check, the routing check, the
status and a rollback. Turning another router off versus uninstalling it
is the user's choice; only never running two routers at once is a
decision (`docs/decisions/fork-and-own.md`). (Basis: the maintainer's
preference.)

## Rejected

- **Codex as an optional extension reached through a bridge** from a
  Claude Code session: the bridge failed mechanically, and a native plugin
  has neither failure.
- **A SessionStart hook on Codex**: it never ran, routing works without
  it, and upstream dropped its own; reopened only by a need.
- **Installing crucible's instrument roles into the user's Codex
  configuration**: a new kind of side effect for an unmeasured saving,
  waiting on a cost audit of Codex controllers (backlog).
- **Maintaining the desktop app and the IDE extension**: untested and
  unused by the maintainer.
- **A cutover runbook** with a flip record, obligations and a capability
  smoke: built for one project's cutover, not for a newcomer's install.

## Changes

- 2026-10-27: the Codex dispatch reference's no-tier-bump sentence is
  gone, since the bounded role there no longer uses the default role's
  model.
- 2026-10-27: the surfaces paragraph states the position and the
  bundled-Codex fact without quoting the maintainer's own usage or dating
  their desktop app's state, which is private context.
- 2026-10-20: no `[features] multi_agent` key in crucible's Codex
  install: on by default on codex-cli 0.163.0.
- 2026-10-20: one canonical tree; each host's adapter a host map and a
  dispatch reference, mapping host mechanics with no policy and no
  references into the repository; the Claude Code dispatch reference's
  restatement of the escalation rule removed.
- 2026-10-19: the Codex guide, `docs/codex.md`, in place of the cutover
  runbook.
- 2026-10-15: Codex a native host runtime, experimental on the CLI, the
  desktop app and IDE extension untested; routing by skill discovery and
  the router's fallback; instruments by the template path; the checklist
  tool behind its config key, with a fallback; no agent-close operation.
- 2026-10-07: no hook on Codex, the manifest's `"hooks": {}` exact, and
  the Codex registration recipe and provenance tool deleted.
