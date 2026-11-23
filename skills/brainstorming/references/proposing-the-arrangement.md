### Proposing the arrangement

A feature's arrangement is four choices: review before code (spec campaign or none), the plan's form (separate with its plan phase, folded into the spec, or none), per-task review (every task, or the branch review alone) and execution (inline or subagent). The branch review is no choice: every arrangement runs it, at full scope. Three presets combine the choices, standard the usual one:

| Preset | Review before code | Plan | Per-task review | Execution |
|---|---|---|---|---|
| standard | spec campaign | separate | per task, the plan's call | per task |
| folded | spec campaign | folded into the spec | per task, the plan's call | per task |
| very-small | none: a lane note | none: the note's change list | none | inline only where `crucible:subagent-driven-development` § Inline mode's test holds |

Choose the preset by the overturn question (`skills/subagent-driven-development/references/review-terms.md` § The arrangement questions):

- Overturn expected → spec campaign.
- Not expected, for one of that section's two usual cases or another stated reason, and one implementer can carry it → very-small.
- Not expected, but needing several tasks → spec campaign too, as only the campaign presets carry a plan; it can be expected to stop after round 1, still the stop rule's call.
- Between the campaign presets: folded where the plan's tasks are disjoint enough that no seam between them is worth its own review, and their entries short enough for every seat to read them all, as folded seats do; standard for the rest.
- Width is no test of risk, since the branch review reads the whole diff, but it shapes the arrangement where work needs coordinating.
- Never use or offer file, line or task counts as the test.
- An umbrella's review goes by its content (`crucible:brainstorming` § Umbrellas): it has no code of its own to review after.

As you close the design presentation, state the preset you choose by name, with the overturn answer and its reason and, for a campaign preset, the reason the fold fits or does not; where a spec campaign follows, state its shape too: its seats with their lenses and models, and its expected rounds, sized per `crucible:redteaming` § Panels. A departure you expect only later ("most tasks will likely be branch review only") is a heads-up, not part of the call: per-task review is the plan's call, reported at the close of the phase that reviews the plan, and execution is chosen per task.

Route-specific:

- Folded: `crucible:redteaming` § The folded lane carries the campaign, deferral, exit and unfolding rules.
- Very-small: once the operator approves the design that proposes the lane, write the lane note from it (`crucible:brainstorming` § The very-small lane).
