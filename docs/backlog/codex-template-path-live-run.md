# Codex seats reading their template by path: most instruments unseen under `spawn_agent`

## Observation

- On the template path (every Codex dispatch, and a Claude Code dispatch
  where the instrument agent is not offered), the controller sends a
  card's filled Slots and Selectors under one line naming the template's
  absolute path, and the seat reads the template itself
  (`skills/using-crucible/references/codex-dispatch.md`;
  `docs/decisions/instruments.md`).
- Two probes backed the change, each a fresh `codex exec` session handed
  a filled card: a redteam seat and a task reviewer. Both read the template
  and wrote its report shape.
- A branch reviewer started by a Codex controller's `spawn_agent` on a
  docs-only lane (2026-11-06): its first command named its template and its
  report has the template's shape; whether it read the template in full was
  not checked. No other instrument has been started by `spawn_agent`.
- A seat that skipped the read would run without its instructions, and
  its report would lack the template's sections.

## Follow-up

On the next Codex run with a campaign or a task loop, check each seat's
report against its template's report shape, and record any miss by
instrument.
