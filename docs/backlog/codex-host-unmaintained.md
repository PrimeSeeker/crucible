# Codex as a host: unmaintained, to remove or to revive

## Observation

- Since 2026-11-27 Codex as a host is labelled unmaintained: on the model
  Codex lists first the design gate failed in five fresh sessions of six,
  and no further measurement is planned (`docs/codex.md` § Status;
  `docs/decisions/runtime-adapters.md`).
- The repository still carries the host: the Codex adapter pair
  (`skills/using-crucible/references/codex.md`, `codex-dispatch.md`), the
  Codex manifest (`.codex-plugin/plugin.json`), the guide (`docs/codex.md`)
  and the rule that skills stay runtime-neutral, with the scanner that
  checks it (`AGENTS.md` § Authoring rules), which every skill edit works
  under. The seat on another host needs part of this whatever is decided:
  it reads the same templates, and takes its model from the Codex host
  map.
- The Codex host map says every model it names meets the floor. By
  Codex's labels on codex-cli 0.172.0 two of the three no longer do, and
  they are kept (`docs/decisions/model-roles-and-effort.md`).
- Two items wait on a Codex-hosted run, which nothing now schedules:
  `docs/backlog/codex-template-path-live-run.md` and
  `docs/backlog/codex-wait-cadence.md`.

## Follow-up

Decide between removing the host and reviving it when Codex retires the
host map's default-role model or a newer line passes the design-gate check
(`docs/codex.md` § Status), whichever comes first. Removing keeps what the
seat on another host needs and closes the two waiting items; reviving
starts from that check on the line current then. Either way the host
map's floor sentence is corrected or goes.
