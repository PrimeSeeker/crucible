Lane: very-small (operator-confirmed 2026-11-05)

# Backlog batch 7

## Intent

Close what the backlog can settle now, preferring deletion to new rules. A
change too big for one implementer no longer has a stay-and-split procedure:
moving to the standard route is the upgrade hatch's ask, and an answer to stay
is the operator's direction on how the work continues. This break is permanent,
on a path no run has used. Nothing else stops working.

## Change list

- `docs/backlog/lane-split-seams.md`: retire stay-and-split in
  `very-small-lane.md` and its slot card; the fix-wave line in `task-loop.md`
  covers any fresh seat, not only a host with no resume. The item goes.
- `docs/backlog/umbrella-followups.md`: drop the red-suite FIX_BASE clause from
  `finish.md`; move the build-history exemption from `code-reviewer.source.md`
  into the rule's own list in `seat-rules.md`, so it covers umbrella landings
  too; accept the three leftovers (the unreviewed `landed` mark, an
  approval-only umbrella's workspace, a pending open-items ask with no carrier)
  in the umbrellas record. The item goes.
- `docs/backlog/worktree-exclude-followups.md`: one sentence in
  `git-fallback.md`: a check still failing or a refused write goes to the
  operator and creation waits. Run the route once on each host. The item goes.
- `docs/backlog/record-wording-slips.md`: the two record edits in
  `authoring-crucible.md` and `records-and-workspace.md`. The item goes.
- `docs/backlog/release-metadata-and-versioning.md`: test whether Codex fetches
  a new copy when the content changes but the version does not, and state the
  result in `docs/dual-runtime.md`; run a name search, which is not legal
  clearance; the version stays in both `plugin.json` and the marketplace entry;
  record formats take no version marker. The item goes.
- `docs/backlog/skill-text-rewrite.md`: close the plugin-root exception (no
  development install exists) and the terminal pass's uncheckable claim (its
  report form allows `UNVERIFIED`). The rest stays.
- `docs/backlog/skill-size-after-compaction.md`: add the 2026-11-05 sighting of a
  re-attached copy from 0.23.0 under 0.27.0. The item stays.
- The `routes` and `task-loop` records for the retirement, each with a Changes
  line. Regenerate the templates and lower the prose budget.

## Acceptance

- `very-small-lane.md` and the implementer's slot card hold no split procedure:
  no `part <k>`, no fresh implementer per part, no last part's Acceptance, no
  resume from a report section, no later part.
- The `fix wave <W>: implementer` line in `task-loop.md` is not limited to a host
  with no resume.
- `finish.md` does not mention FIX_BASE.
- `code-reviewer.source.md` has no build-history exemption clause, and the
  build-history rule in `seat-rules.md` places open items.
- The safety step of `git-fallback.md` says what a check that still exits 1 and
  a refused write do.
- The Decision of `records-and-workspace.md` points at
  `crucible:using-git-worktrees` for commit conventions, and the retired
  trigger's Why in `authoring-crucible.md` says the call was left to the agent.
- `docs/dual-runtime.md` states the Codex result rather than calling it
  unverified.
- The five items named above as going are deleted, `skill-text-rewrite.md` no
  longer holds the two closed points, and `skill-size-after-compaction.md`
  records the sighting.
- `docs/decisions/routes.md` and `docs/decisions/task-loop.md` each carry a
  Changes line for the retirement.
- `python -m pytest tests/` passes, `python tools/instrument_agents.py check`
  included.

## Out of scope

The other 19 backlog items (`skill-rewrite-reaudit` among them), new rules for
the accepted leftovers, and any release decision before the close readout.
