# Install crucible's instrument roles into the user's Codex configuration

## Observation

On Claude Code a templated dispatch names an instrument agent (generated
under `agents/`) and sends only its filled slot card. Codex keeps the
template path: the controller fills the card and the template, the
runtime name in its runtime slot, and dispatches the whole, because a
plugin cannot ship Codex agent roles. A probe on codex-cli 0.157.1 found:

- named roles load from `CODEX_HOME/agents/`, from a trusted project's
  `.codex/agents/` and from `[agents.<name>]` in config, and a child
  spawned with `agent_type` obeys its role's `developer_instructions`;
- roles shipped by a plugin never loaded, in any of three forms (a
  manifest `agents` key, a bare `agents/` directory, a manifest
  `subagents` key): spawning one failed with `unknown agent_type`.

So a Codex controller reads and pastes each template's fixed text on
every dispatch. The size of that cost is unmeasured: no token-cost audit
has yet isolated Codex controllers.

## Follow-up

Open when a token-cost audit covers Codex controllers, so the saving can
be weighed against what the install costs.

Then write crucible's seven roles into a location Codex loads (the
user's `CODEX_HOME/agents/` or config, or a project's `.codex/agents/`)
and change the **Dispatch an instrument** line in
`skills/using-crucible/references/codex-dispatch.md` to spawn the role
with its filled slot card. The skills do not change: host mechanics live
in the adapter pair, so this is one adapter line.

Open questions:

- Writing into the user's Codex configuration is a new kind of side
  effect for crucible: who runs the install, how it is reversed, and how
  `docs/codex.md` covers it beside install and rollback.
- How installed roles track the plugin version, so a role and its slot
  card do not skew across an upgrade.
- Whether a newer Codex release loads plugin-shipped roles, which would
  make the install unnecessary; re-run the probe first.
