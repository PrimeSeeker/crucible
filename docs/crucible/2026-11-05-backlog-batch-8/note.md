Lane: very-small (operator-confirmed 2026-11-05)

# Backlog batch 8: compaction, copied findings, report files, seat effort

## Intent

Resolve what measurements already on disk can resolve in four backlog items. A controller whose skill copy did not come back after compaction is told to invoke it again, as it already is for a cut copy. No break.

## Change list

1. `skills/using-crucible/SKILL.md`: the compaction line also covers a skill still being worked under that did not come back; `tests/prose-budget.txt`.
2. `docs/dual-runtime.md`: after an upgrade, a running session keeps the copies it invoked until each is invoked again.
3. `docs/decisions/authoring-crucible.md`: the reasoning, and the two rejected signals (a version line in the session-start text, re-invoking at every compaction); delete `docs/backlog/skill-size-after-compaction.md`.
4. A decision record gets the rejected findings-by-reference with its figures; delete `docs/backlog/findings-by-reference.md`.
5. `docs/backlog/review-seat-report-write.md`: the count since the card change, with the item narrowed to the verifier.
6. `docs/decisions/model-roles-and-effort.md`: the effort measurement replaces both "unmeasured" passages; `docs/backlog/escalation-and-effort.md` keeps only the stuck-trigger question.

## Acceptance

- `python -m pytest tests/` passes.
- `skills/using-crucible/SKILL.md` contains "did not come back".
- The two deleted items' names appear nowhere outside `docs/crucible/`.
- `docs/decisions/model-roles-and-effort.md` no longer calls Claude Code's unset effort unmeasured.

## Out of scope

A version signal, passing findings by reference, the absolute report path, any change to the effort rule, the stuck trigger, every other backlog item.
