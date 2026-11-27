# Codex sessions started with `-s read-only` edited a tracked file

## Observation

- Crucible starts a seat on another host with `codex exec -C <worktree>
  -s read-only`, and tells the seat that the sandbox refuses writes
  (`skills/using-crucible/references/claude-code-dispatch.md`, **Seat on
  another host**).
- On 2026-11-27 (codex-cli 0.172.0, Windows) five `codex exec -s
  read-only` sessions, each asked for a feature, edited a tracked file in
  the directory `-C` named: three through the patch tool, two by a script
  run in the shell. In the same sessions pytest could not create a
  temporary file, so the sandbox was in force for some writes. Why these
  went through was not established.
- Those sessions were asked for a change; a review seat is not, and the
  status check after each review window would show a write to the tree
  (`docs/decisions/shared-tree.md`), which has no review seat on record
  writing into its tree.

## Follow-up

Establish what lets a write through under `-s read-only` (the platform,
the Codex version, a config setting), and whether the seat's command needs
another flag. Until then the flag is no guarantee, and the dispatch's
sentence that the sandbox refuses writes may be untrue.
