Lane: very-small (operator-confirmed 2026-11-04)

## Intent

Carry out three operator rulings from the backlog's rulings group.

1. An operator who wants a reviewer from the other model family gets a
   written way to run one. Crucible never proposes it. It runs read-only
   beside the round's seats, losing it costs the round nothing, and its
   findings are checked against the files before they merge. The README
   carries the maintainer's recommendation with its thin evidence.
2. The mode that never commits the spec and plan is closed, as no project
   needing it is known. The record keeps the cheaper route to try first
   and what that route leaves dangling.
3. The visual companion is postponed indefinitely, and someone looking
   for it finds a visible note that crucible doesn't have it.

## Change list

Advisory.

- `skills/redteaming/references/panels.md`: a passage saying when the seat
  runs (only where the operator's instructions or request ask for one), that
  it is an extra seat and never one in place of a seat on this host, and that
  a run ending with no report goes in the quorum block, with no top-up and no
  degraded round.
- `skills/redteaming/references/merge-and-finding-hygiene.md`: one sentence
  saying to open each of its findings and check it against the files before
  merging.
- `skills/using-crucible/references/claude-code-dispatch.md`: the
  `codex exec` command, with a read-only sandbox, the other host's
  default-role model, high effort, and the final message saved as the
  report.
- `skills/using-crucible/references/codex-dispatch.md`: a line saying this
  hasn't been measured from that host.
- `docs/dual-runtime.md`: one row in the operations table.
- `README.md` § Configuration, the recommendation:

  > **A reviewer from the other model family.** Crucible's review panels
  > run on one model family, which can share blind spots. If you use both
  > hosts, the maintainer recommends adding one reviewer from the other
  > family to a redteam's first round: a line in your instruction file asks
  > for it (say, "add a seat on Codex to each redteam's first round"), and
  > crucible never starts one unasked. The evidence is anecdotal: on record
  > it once caught a blocking flaw the other reviewers had missed, and
  > elsewhere it added little or nothing; in one audit about half its claims
  > held only partly, so crucible checks each of its findings against the
  > files. It spends the other host's usage. Only Codex started from Claude
  > Code has been measured, not the reverse.

- `README.md` § Coming from superpowers: a short paragraph saying crucible
  doesn't have the visual companion, pointing to the backlog item.
- Records, each with a 2026-11-04 Changes line:
  - `docs/decisions/spec-campaign.md`: the opt-in seat, the single-family
    risk still accepted when none is asked for, and crucible offering it at
    the campaign gate rejected.
  - `docs/decisions/umbrellas.md`: the operator's ruling on the closing
    review's dropped seat.
  - `docs/decisions/records-and-workspace.md`: the mode closed, the route of
    rewriting a copy of the branch at push time, and its limits.
  - `docs/decisions/brainstorming-first.md`: the companion postponed.
- `docs/upstream.md`: the visual-companion row says postponed.
- Backlog: delete `docs/backlog/second-runtime-seat.md` and
  `docs/backlog/records-retention-config.md`, remove the stale line in
  `docs/backlog/decision-records-upkeep.md`, and rewrite
  `docs/backlog/visual-companion.md` as postponed.
- `tests/prose-budget.txt`: raised for redteaming and using-crucible.

## Acceptance

Ten mechanical checks, each of which fails on master at `b5ad3d1`:

- `grep -q '\*\*A seat on another host' skills/redteaming/references/panels.md`
- `grep -q '\*\*A seat on another host' skills/redteaming/references/merge-and-finding-hygiene.md`
- `grep -q '\*\*Seat on another host\*\*' skills/using-crucible/references/claude-code-dispatch.md`
- `grep -q '\*\*Seat on another host\*\*' skills/using-crucible/references/codex-dispatch.md`
- `README.md` holds both `maintainer recommends` and `other model family`.
- Neither `docs/backlog/second-runtime-seat.md` nor
  `docs/backlog/records-retention-config.md` exists.
- `git grep 'second-runtime-seat\|records-retention-config' -- . ':!docs/crucible'`
  finds nothing.
- `grep -q 'Postponed indefinitely' docs/backlog/visual-companion.md`
- `README.md` § Coming from superpowers names the `visual companion`.
- `grep -c 'restoring it opt-in is open' docs/upstream.md` prints 0.

Then:

- `python -m pytest tests/` passes.
- One real seat, run by the new dispatch entry with crucible enabled on
  Codex, against this note and the changed files: its report appears at
  its path with an `## Index`, and the tree is unchanged. If the Codex
  usage limit stops it, this check is reported as not run.

## Out of scope

- Crucible proposing or detecting another host's seat.
- Such a seat at the branch review or terminal pass.
- Measuring Claude started from Codex.
- Building the rewrite into finishing, or warning about dangling references
  there.
- Any visual-companion mechanism.
- Slimming the decision records.
