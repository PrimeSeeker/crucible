# Contain prose creep after the compaction

## Observation

- Crucible's skill text has regrown after every rewrite within two to three weeks: hand-edited skill words went from about 38k to 71.3k to 47.7k to 57.2k between August and November 2026. Since 0.2.0 the prose budget recorded 67 raises against 27 lowers, and no raise was refused.
- The 2026-11-03 compaction cut every route's every-run load by 28–36% and the corpus by about a quarter (`docs/crucible/2026-11-03-prose-compaction/effort.md`). Nothing in place stops the regrowth: the prose budget counts words per directory at commit time, raised by the commit's own author.
- The effort's record ranks the growth mechanisms and the containment ideas, among them a suite test billing each route's every-run tokens against an operator-owned cap, a compaction trigger at 10% over this baseline, a per-spec token allowance, and periodic re-derivation of a file from its rule inventory.
- Since 2026-11-03 writing-skills carries the write-time rules (`crucible:writing-skills § Reader cost`: a fix that keeps the finding's reasons out of the text, excess as a review finding, measuring written text) and the compaction procedure (`skills/writing-skills/compacting.md`). Replace-before-adding was micro-tested then and found unneeded: fixers already revise the sentence that owns the case (`docs/decisions/authoring-crucible.md`).
- Token costs are reliably underestimated before implementation (the maintainer, 2026-11-03), which weighs against a per-spec allowance: a control measures the written text.
- A per-file rewrite loses rules that two files each drop on the strength of the other ("stated elsewhere"); the effort's whole-branch review caught one such pair.

## Follow-up

The operator picks which project-side containment to adopt, if any. The baseline for any trigger or cap is `docs/crucible/2026-11-03-prose-compaction/resident-tokens.md`, counted with `resident-tokens.json` beside it.
