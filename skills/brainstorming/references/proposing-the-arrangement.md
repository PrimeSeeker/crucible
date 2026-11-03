### Proposing the arrangement (step 4)

A feature's arrangement is four choices: review before code (a spec campaign, or none), the plan's form (separate with its plan phase, folded into the spec, or none), per-task review (every task, or the branch review alone), and execution (inline or subagent). The branch review is no choice: every arrangement runs it, at full scope. Three presets combine the choices, standard the usual one:

| Preset | Review before code | Plan | Per-task review | Execution |
|---|---|---|---|---|
| standard | spec campaign | separate, with its plan phase | per task, the plan's call | per task |
| folded | spec campaign | folded into the spec, no plan phase | per task, the plan's call | per task |
| very-small | none: a lane note | none: the note's change list | none | inline where overdetermined |

Each choice is made where its information exists: the preset here; per-task review in the plan, where a task may carry `Review: branch only` (`crucible:writing-plans` § Per-task structure — four fields, all required); execution per task (`crucible:subagent-driven-development` § Inline mode, and on the very-small lane its reference). A campaign's width, its seats and rounds, is set at the campaign gate and by the stop rule (`crucible:redteaming` § Stop rule and terminal pass).

**Unsupported**, each for its reason: per-task review with no plan (there are no tasks); a plan phase without a separate plan (the spec campaign reviews a folded one); a campaign on a lane note, or a spec with no campaign (a feature's spec is always campaigned, a note never is; an umbrella approved without a campaign is a spec of its own kind); a lane note with a plan, or a spec with no plan (work that needs a plan takes a campaign preset, and a campaigned spec is planned).

**Choose the preset by the overturn question** (`skills/subagent-driven-development/references/seat-rules.md` § The arrangement questions): where overturning a major mechanism after code is reasonably expected, the feature takes a spec campaign; where it is not, for one of that section's two usual cases or another stated reason, it takes none where one implementer can carry it. Between the campaign presets, folded fits a plan of one or two tasks with no seam worth its own review, and standard fits the rest. Width is no test of risk, since the branch review reads the whole diff whatever its width, but it shapes the arrangement where work needs coordinating: a settled change one implementer can carry takes the very-small preset, implemented inline only where `crucible:subagent-driven-development` § Inline mode's test holds, its implementer dispatched otherwise; a settled change that needs several coordinated tasks needs a plan, which only the campaign presets carry, so it takes standard, whose campaign can be expected to stop after its first round, the stop still the stop rule's call. File and line counts are not the test and are not offered as one. An umbrella's review is chosen by its content instead (`crucible:brainstorming` § Umbrellas — an effort that takes several features): it has no code of its own to review after.

**The proposal.** As you close the design presentation, propose a preset: name it, give the overturn answer with its reason and, for folded, the plan-size reason; recommend one and let the operator rule, presenting a close call as one. Per-task review is the plan's, reported at the close of the phase that reviews the plan, and execution is chosen per task, so a departure you expect only later ("most tasks will likely be branch review only") is a heads-up, not something to confirm.

What stays route-specific:

- **Folded.** `crucible:redteaming` § The folded lane carries the campaign, deferral, exit and unfolding rules.
- **Very-small.** Draft the lane note (`crucible:brainstorming` § The very-small lane — the lane note (step 5)) and run the self-review on the draft before proposing, and show it with the proposal: the operator's one answer confirms or vetoes the preset and approves or amends the note, and the file is written only after it; a veto discards the draft.
