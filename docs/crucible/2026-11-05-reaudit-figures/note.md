Lane: very-small (operator-confirmed 2026-11-05)

# Re-audit figures

## Intent

Record what `docs/backlog/skill-rewrite-reaudit.md` could settle now, and hold
what it cannot. Since the retirements about 20 features have run, all on
crucible's own repository in one session, and only two used a campaign or the
task loop, so a transcript audit cannot yet show whether a retirement hurt real
work. The counted figures, the compaction check and the verifier's runs go on
the record; the audit waits for features on real code. Nothing shipped changes,
and nothing stops working.

## Change list

- `docs/crucible/2026-11-05-reaudit-figures/`: the figures and the script that
  counts them, at six revisions with the two reads the umbrella's closing review
  found omitted, and what seats read beside what controllers load.
- `docs/decisions/authoring-crucible.md`: the resident-token table extended to
  the head with those reads, the seat figures, the compaction check, and a
  Changes line.
- `docs/decisions/fix-verification-and-merge.md`: the verifier's runs since the
  retirements, and a Changes line.
- `docs/backlog/skill-rewrite-reaudit.md`: keeps only the transcript audit and
  its trigger, the figures being done.
- `docs/backlog/prose-creep-containment.md`: the regrowth since its baseline.

## Acceptance

- `python docs/crucible/2026-11-05-reaudit-figures/resident_tokens_reaudit.py`
  reproduces every every-run total the record held at `a3db87f`, `d78398c` and
  `4026f6b`, and every prose-compaction total at `56e8475`.
- Every total in the record's table for `5546425` appears in the figures file.
- `docs/decisions/authoring-crucible.md` and
  `docs/decisions/fix-verification-and-merge.md` each carry a 2026-11-05 Changes
  line for this measurement.
- `docs/backlog/skill-rewrite-reaudit.md` holds no re-count task and names the
  trigger: features on real code, on 0.13.0 or later.
- `docs/backlog/prose-creep-containment.md` states the regrowth, with its figures
  file named.
- `git diff master -- skills agents hooks tools tests` is empty, and no version
  changes.
- `python -m pytest tests/` passes.

## Out of scope

The transcript audit, any change to the blind verifier, any containment of
prose creep, any skill text, and a release.
