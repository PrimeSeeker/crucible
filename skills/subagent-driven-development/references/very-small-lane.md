## The very-small lane

The very-small preset (`crucible:brainstorming` § Proposing the arrangement): a settled change one implementer can carry, executed from a **lane note** — with no spec campaign, no plan and no per-task review. The diff is the review object, and the branch-review loop of `crucible:requesting-code-review` reviews it. This reference states where the lane differs; everything else runs as elsewhere.

**Entry is the operator's, and only at brainstorming.** You arrive here from `crucible:brainstorming`'s handoff, after the operator confirmed the lane at its present-the-design step and the brainstorm decision record carries that confirmation. You never declare the lane, and nothing converts to it mid-flight: without that record entry this section does not apply, and the change goes back to brainstorming.

**The note is the lane's only artifact, and it is frozen.** Its four parts — Intent, Change list, Acceptance, Out of scope — are defined at `crucible:brainstorming § The very-small lane`: Intent, Acceptance and Out of scope are binding, the change list advisory. What was asked is quoted in the workspace's `request.md`, never in the note. It is committed before implementation starts. From then on, a change to its binding parts is an operator decision ask, never your edit; an approved change is committed and re-pinned in the ledger, and the operator's answer is entered in `brainstorm-decisions.md`. Work that departs from the change list is a ledger line, not a note edit.

**What runs, in order:**

1. **Setup, where it applies** (`crucible:subagent-driven-development` § Setup): the workspace check and provision, the project setup and baseline, and the ledger. There is no plan to read.
2. **Implementation, inline where overdetermined.** Where the test of `crucible:subagent-driven-development` § Inline mode holds — the change overdetermined, and fitting your remaining context — you implement, run the repo's verification gates and commit, under the discipline [implementer-prompt.md](../implementer-prompt.md) carries — test-first where a seam exists, evidence before done. Only that test applies: the section's review clause does not, the lane having no task review. Otherwise dispatch instrument `implementer`, its card filled for the lane. Log your judgment and its agent identity under `## Progress`, as `Implementer: <agent id> — <why dispatched>`, and transcribe each change-list departure its Decision Log records into a `Departure:` ledger line, and each concern, `Questions` item and out-of-task proposal its report carries into a lead under `## Deferred minors`, `Lane: lead (<kind>): <one-liner>` (`crucible:subagent-driven-development` § Setup), since the ledger — not the report — reaches the branch reviewer, the lane's first review, which rules on them. Its premise finding goes where `skills/redteaming/references/flip-paths.md` § Premise findings sends it. The no-commit rule (`skills/subagent-driven-development/references/dispatch-composition.md` § Shared-tree rules) holds while that implementer works.
3. **The branch review** (`crucible:requesting-code-review`), each card filled for the lane: the note at its pinned revision is every seat's requirements input, the adjudicator's included. Where the note's preamble carries an `Umbrella:` line, the umbrella content `skills/brainstorming/references/umbrellas.md` § Children names binds beside the note's binding parts, and within the reviewed range a binding change to it, as § Edits defines one, is a finding. Before each full-scope pass and fix wave, take the receiving step `crucible:requesting-code-review` § The branch-review loop names. Drift from the note's binding parts is a wave finding here, not an operator ask: the lane has no tasks to revert.
4. **Finish** (`crucible:subagent-driven-development` § Finish), unchanged; its close readout lists the lane's departures.

**Fix waves run inline.** For each wave you apply the findings yourself, run the gates, commit, and write the wave's fix report to `sdd/branch-review/wave-<n>-fix.md`, which the scoped re-review reads as its fix report. It answers each finding **fixed** — what changed, the covering tests, the command and its output, the sibling instances of the defect pattern or none — or **NOT CONFIRMED** with evidence — and each labelled change (`Change (<kind>): …`, `crucible:requesting-code-review` § The branch-review loop) **applied**, with what changed and its covering tests, or **declined** with its reason, as that section states. A cleanup wave runs inline the same way. Every lane diff counts as your own, the optional implementer's included, so a finding you contest goes to the adjudicator (`crucible:subagent-driven-development` § Disputes and adjudication) at any wave; you never dismiss or park one yourself. **For this lane only**, this supersedes the rule that the controller never fixes findings (`crucible:subagent-driven-development` § The Task Loop and `crucible:requesting-code-review`).

**The lane ledger** (binding on this lane; the ledger's other structure is SDD's). Line 1 keeps SDD's identity-line shape with the note's pin where the plan path goes — `# SDD ledger — plan: <note-path> @ <rev>` — so the resume rule's identity check reads it unchanged, and the predecessor-link line keeps its slot. The lane's own lines sit under a `## Lane` section, each on its own line, in these shapes:

```
Lane: very-small (operator-confirmed <date>)
Gates: <what ran> — <result>
Implementation complete: <commit>
Departure: <change-list item> — <what was done instead>
Wave <n>: <X> findings (<b>B/<m>M/<k>m); re-review: <verdict>
Wave <n> (cleanup): <X> findings (<b>B/<m>M/<k>m); re-review: <verdict>
Note re-pinned: <note-path> @ <rev> — <operator decision>
```

written as the lane moves:

- `Lane:` — first, with the confirmation date from the decision record;
- `Gates:` — after implementation, and again after each wave's fixes;
- `Implementation complete:` — once the implementation is committed, citing the commit by hash;
- `Departure:` — one per change-list item the work departed from, zero or more;
- `Wave <n>:` — once the wave's re-review, if any, and its adjudication have returned; `re-review: none` for a wave that only disputes; `Wave <n> (cleanup):` for the cleanup wave (`crucible:requesting-code-review` § The branch-review loop), so a resumed controller sees it spent;
- `Note re-pinned:` — on an operator-approved change to the note's binding parts.

The lane has no `Task <N>` lines, so a resumed controller takes its restart point from the last line under `## Lane`; a `Lane: lead` line sits under `## Deferred minors` and is not one. Adjudications go where every adjudication goes, `## Adjudication rulings`.

**The upgrade hatch.** Where overturning a major mechanism of the change is reasonably expected now that it is coded (`skills/subagent-driven-development/references/review-terms.md` § The arrangement questions), whether a reviewer's finding or question or your own reading shows it, put staying on the lane or moving to the standard route to the operator as a decision ask. On the move, record the answer as `crucible:brainstorming` § Proposing the arrangement states. Move `sdd/` aside whole, as `sdd-lane/`, so no later report reuses a path the lane wrote, and invoke `crucible:brainstorming` with the note and the existing diff as its incoming document, proposing no preset. Its spec goes into the lane's feature folder beside the note; the plan phase's close links the lane ledger and carries the lane's open findings and unruled leads (`skills/redteaming/references/plan-phase.md`); the plan's tasks build on the carried-over diff. The folded lane is never a hatch target: its entry is before any artifact is written.
