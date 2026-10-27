# Crucible on Codex

Crucible's Codex support is experimental (§ Status). This guide covers
installing it, the two config keys it needs, checking that it is the one
router and that sessions reach it, and rolling back. The command forms are
those of codex-cli 0.163.0; the version tested is codex-cli 0.162.1.

Companions: `docs/dual-runtime.md` (what the two hosts share; releases,
updates and version rollback), `hooks/README.md` (why crucible registers no
hook on Codex).

## One router at a time

Crucible's router, the `using-crucible` skill, decides which workflow a
session follows, and two routers in one session fight over that. Before
installing, turn off any other process router (superpowers, for one) and
any standalone skill sharing a name with one of crucible's (§ Turning
another router off). Never start a session with two routers on.

## Install

```bash
codex plugin marketplace add PrimeSeeker/crucible
codex plugin add crucible@crucible
```

The repository's default branch, `stable`, holds the latest release. To
try a local checkout instead, give its path:
`codex plugin marketplace add ./path/to/crucible`.

Then set two keys in your Codex config (`~/.codex/config.toml`):

```toml
[agents]
default_subagent_reasoning_effort = "high"

[tools.update_plan]
enabled = true
```

- **Seat effort.** Crucible names each seat's model and leaves its effort
  to this key; `high` is the recommended level. Without it a seat runs at
  its model's default (`low` for crucible's default model), not at your
  session's effort, and crucible's review and execution workflows say so
  before their first dispatch.
- **The checklist tool.** Crucible tracks checklists with `update_plan`,
  which on codex-cli 0.162.1 exists only with this key set. Without it,
  sessions keep the checklist in their messages.

Crucible registers no hook on Codex, so there is no hook to trust: a
session reaches crucible by reading the router.

## Turning another router off

Codex keeps plugin and skill switches in its config:

```toml
[plugins."<plugin>@<marketplace>"]
enabled = false

[[skills.config]]
path = "/path/to/skill-folder"
enabled = false
```

The first turns off a plugin; the second, one standalone skill (the folder
holding its `SKILL.md`). Set them in your user config so they cover every
session, and make sure no trusted project's own Codex config turns the
other router back on, since it can override user settings. Uninstalling
works as well; either way, the check below is what counts.

## Check: one router

In a fresh session, ask Codex to list the skills it has, with their paths.
Each of crucible's twelve skills appears exactly once: `using-crucible`,
`brainstorming`, `writing-plans`, `subagent-driven-development`,
`redteaming`, `requesting-code-review`, `receiving-review`,
`dispatching-parallel-agents`, `systematic-debugging`,
`using-git-worktrees`, `finishing-a-development-branch`, `writing-skills`.
The only router listed is crucible's `using-crucible`. A skill listed
twice, or another router listed, means something is still on: find it by
its path and turn it off.

## Check: routing

A Codex session runs crucible only if it reads the router. To check:

1. Open a fresh session and ask for a piece of feature work.
2. Watch its tool calls, not its own account of them. It reads
   `skills/using-crucible/SKILL.md` before its first task action, and
   `skills/using-crucible/references/codex.md` before it plans or
   dispatches.
3. Stop once you have seen it; the work need not be finished.

Routing is a rate, not a switch: repeat the check over several fresh
sessions. A session whose first task action comes before the router read
ran without crucible.

## Status

Experimental. On codex-cli 0.162.1 crucible failed two checks:

- **Routing.** In the routing check above, one fresh session in three
  acted before reading the router.
- **The checklist tool.** It is off by default, and with its key set, a
  call has been seen to be accepted, not to track the checklist's items.

Untested:

- **The desktop app and the IDE extension.** They are assumed similar
  enough to the CLI, unmeasured. The desktop app has been seen running its
  own bundled Codex, older than the CLI's, so a fact measured on the CLI
  may not hold there.
- **Parallel fan-out.** Crucible's Codex tests never dispatched agents in
  parallel.

## Rollback

1. Turn crucible off: `enabled = false` under
   `[plugins."crucible@crucible"]` in your Codex config, or
   `codex plugin remove crucible@crucible`.
2. Turn your previous router back on: undo what you set under § Turning
   another router off.
3. In a fresh session, run § Check: one router the other way round: the
   previous router's skills each listed once, crucible's not at all.

Make both changes before starting a session, so none starts with two
routers or none.

Going back to an earlier crucible version is a different operation:
`docs/dual-runtime.md` § Upgrades and rollback.
