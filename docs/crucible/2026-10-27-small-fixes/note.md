Lane: very-small (operator-confirmed 2026-10-27)

# Small fixes and the Codex bounded role

## Intent

Fix defects that cost crucible's users today, and map Codex's bounded role
to its new middle tier:

- after compaction a long skill comes back cut short, and the agent works
  from the fragment;
- review seats return their report as text instead of writing the file, or
  put scratch files in the tree they review;
- the folded lane never meets the plan self-review's name-consistency
  check;
- three text-audit gaps: the snapshot-blessing agent has no model, report
  path or reply; the implementer's ledger identity line has no shape;
  lenses in the roster lack the one-line description the seat card
  requires;
- Codex now lists a current-generation middle tier, `gpt-6.1-terra`, so the
  bounded role takes it instead of the default model.

## Change list

- `skills/using-crucible/SKILL.md`: one line: after compaction, a skill
  whose text came back cut short is invoked again before acting on it.
  `docs/backlog/skill-size-after-compaction.md` keeps the size reduction,
  with today's measurements.
- `re-review-prompt.md` and `verifier-prompt.md` § Report: the file is
  required even where the host advises returning findings as text; the
  reply carries only the verdict and the path.
- The seven "under `scratch/`" sites in the review and seat templates: the
  scratch path given from the worktree root.
  `docs/backlog/review-seat-report-write.md` keeps only the post-release
  check of the miss rate.
- `skills/writing-plans/SKILL.md` § Self-review: on the folded lane it runs
  at brainstorming's self-review step.
  `docs/backlog/front-end-pass-followups.md` deleted.
- `skills/subagent-driven-development/SKILL.md`: a § Models bullet for the
  snapshot-blessing agent (the bounded role or better), its report path and
  reply at step 4; the implementer identity line's shape, and its
  counterpart in the very-small-lane reference.
- `skills/redteaming/SKILL.md` lens roster: one-line descriptions where
  missing.
- `skills/using-crucible/references/codex.md` Model roles: Bounded is
  `gpt-6.1-terra`; its read-on line and floor examples updated.
  `codex-dispatch.md`: the no-tier-bump sentence removed.
  `docs/decisions/model-roles-and-effort.md`: Why updated, with a Changes
  line. `tests/claudeism-allowlist.txt` as the scanner needs.
  `docs/backlog/skill-text-rewrite.md`: the fixed defects removed from its
  list.
- `tests/prose-budget.txt` raised where skills grow.

## Acceptance

1. `grep -n -i "truncat" skills/using-crucible/SKILL.md` finds the
   compaction line (nothing before).
2. ``grep -rn 'under `scratch/`' skills`` finds nothing (7 before).
3. `grep -rn "current-generation tier" skills docs` finds nothing (2
   before); `codex.md`'s Bounded line names `gpt-6.1-terra`.
4. `grep -nE '^- \*\*(correctness|evidence-and-inference)\*\*$'
   skills/redteaming/SKILL.md` finds nothing (2 before).
5. SDD's § Models has a bullet for the snapshot-blessing agent (none
   before).
6. `docs/backlog/front-end-pass-followups.md` does not exist.
7. `python -m pytest tests/` passes.
8. The cut tool's leak search over the worktree reports no unexplained
   hit, apart from the `feature-folder` pattern on this feature's own
   folder.

## Out of scope

- Shrinking redteaming and SDD under the compaction budget (the rewrite).
- The re-review template's partial comment rule and the other duplicated
  seat rules (the rewrite's shared seat reference).
- The decision-record slips (with the records-upkeep item).
- Measuring the re-reviewer's report miss rate (after the release).
- The release itself, and Claude Code's model map.
