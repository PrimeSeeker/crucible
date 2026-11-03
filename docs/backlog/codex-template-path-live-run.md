# Codex seats reading their template by path: no live run yet

## Observation

- On the template path (every Codex dispatch, and a Claude Code dispatch
  where the instrument agent is not offered), the controller sends a
  card's filled Slots and Selectors under one line naming the template's
  absolute path, and the seat reads the template itself
  (`skills/using-crucible/references/codex-dispatch.md`;
  `docs/decisions/instruments.md`).
- Two probes backed the change, each a fresh `codex exec` session handed
  a filled card: a redteam seat and a task reviewer, one per instrument
  family. Both read the template and wrote its report shape. The branch
  reviewer's family was not probed, and no seat has yet been started
  this way by a Codex controller's `spawn_agent`.
- A seat that skipped the read would run without its instructions, and
  its report would lack the template's sections.

## Follow-up

On the first Codex run of a feature since the change, check each seat's
report against its template's report shape, the branch reviewer's
included, and record any miss by instrument.
