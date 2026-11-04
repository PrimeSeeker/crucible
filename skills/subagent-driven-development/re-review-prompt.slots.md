# Slot card — re-reviewer

## Slots

- [WORKTREE_PATH]: the fixed branch's worktree, absolute.
- [PLUGIN_ROOT]: the plugin root you read this card from, absolute.
- [MANDATE_REMINDER]: one line restating the binding output: a verdict per listed finding, a ruling per fix-report concern, new breakage in the fix diff only, and the wave verdict, in the report file; a reply of the wave verdict and the file's path.
- [REQUIREMENTS]: in a task's fix wave, the plan's path and task number as the implementer's card named them, then the hash of each FIX_BASE..HEAD commit that landed a scoped amendment or plan-patching ruling, or "no amendment commits"; in a branch-review wave, the spec at its pinned revision and the plan (one document where folded); on the very-small lane, the lane note at its pinned revision.
- [UMBRELLAS]: per the dispatch composition's item 2; else "none".
- [FINDINGS]: one bullet per finding this wave's fix report answers fixed, verbatim from the review that raised it, never one answered NOT CONFIRMED (ruled on separately); and each `Change (…)` it applied, ADDRESSED where it landed and broke nothing.
- [FIX_REPORT]: in a task's fix wave, the implementer's report file, this wave's fix report appended; in a branch-review wave, `sdd/branch-review/wave-<n>-fix.md` — on the very-small lane your own, held to the fix-report contract.
- [REPORT_FILE]: in the feature workspace, `sdd/reports/task-<N>-re-review-w<W>.md` for task fix wave <W>; `sdd/branch-review/wave-<n>-re-review.md` for branch-review wave <n>; then the line `Write this file with your <tool> tool before replying.`, `<tool>` being the tool that creates a file in your host map's **Edit** entry.
- [SCRATCH_DIR]: the seat's scratch directory, absolute.
- [FIX_BASE_SHA]: in a task's fix wave, the head the previous review saw; in a branch-review wave, the FIX_BASE recorded as it opened.
- [HEAD_SHA]: the current commit.

## Selectors

- lane: very-small | off
  - very-small: the lane passage under Requirements; every re-review on that lane
  - off: none; every other re-review

## Dispatch

- Description: `Re-review Task <N> fix wave <W>` or `Re-review branch wave <n>`.
- Model: the bounded role or better, even for a small fix diff.
