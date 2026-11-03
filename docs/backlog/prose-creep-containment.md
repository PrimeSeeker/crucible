# Contain prose creep after the compaction

## Observation

- Crucible's skill text has regrown after every rewrite within two to three weeks: hand-edited skill words went from about 38k to 71.3k to 47.7k to 57.2k between August and November 2026. Since 0.2.0 the prose budget recorded 67 raises against 27 lowers, and no raise was refused.
- The 2026-11-03 compaction cut every route's every-run load by 28–36% and the corpus by about a quarter (`docs/crucible/2026-11-03-prose-compaction/effort.md`). Nothing in place stops the regrowth: the prose budget counts words per directory at commit time, raised by the commit's own author.
- The effort's record ranks the growth mechanisms and the containment ideas, among them a suite test billing each route's every-run tokens against an operator-owned cap, a compaction trigger at 10% over this baseline, replace-before-adding for fixes, a per-spec token allowance, and periodic re-derivation of a file from its rule inventory.
- A per-file rewrite loses rules that two files each drop on the strength of the other ("stated elsewhere"); the effort's whole-branch review caught one such pair.

## Follow-up

The operator picks which containment to adopt, if any, and whether `skills/writing-skills/SKILL.md` takes what this effort learned (its cut patterns are `docs/crucible/2026-11-03-prose-compaction/style.md`). The baseline for any trigger or cap is that folder's `resident-tokens.md`, counted with `resident-tokens.json` beside it.
