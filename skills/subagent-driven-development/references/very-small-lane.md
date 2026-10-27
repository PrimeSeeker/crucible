## The very-small lane

The third route, alongside the standard route and the folded lane: a small change with no design decision worth reviewing before code, executed from a **lane note** — with no spec campaign, no plan, no digest and no per-task review. The diff is the review object, and the branch-review loop of `crucible:requesting-code-review` reviews it. This reference states where the lane differs; everything else runs as elsewhere.

**Entry is the operator's, and only at brainstorming.** You arrive here from `crucible:brainstorming`'s handoff, after the operator confirmed the lane at its present-the-design step and the brainstorm decision record carries that confirmation. You never declare the lane, and nothing converts to it mid-flight: without that record entry this section does not apply, and the change goes back to brainstorming.

**The note is the lane's only artifact, and it is frozen.** Its four parts — Intent, Change list, Acceptance, Out of scope — are defined at `crucible:brainstorming § The very-small lane — the lane note (step 5)`: Intent, Acceptance and Out of scope are binding, the change list advisory. It is committed before implementation starts. From then on, a change to its binding parts is an operator decision ask with a recommendation, never your edit; an approved change is committed and re-pinned in the ledger. Work that departs from the change list is a ledger line, not a note edit.

**What runs, in order:**

1. **Setup, where it applies** (`crucible:subagent-driven-development` § Setup): the workspace check and provision, the project setup and baseline, and the ledger. There is no plan to read, no routing table to seed and no pre-flight plan-conflict scan.
2. **Implementation, inline by default.** You implement, run the repo's verification gates and commit, under the discipline [implementer-prompt.md](../implementer-prompt.md) carries — test-first where a seam exists, evidence before done. Where the change is mechanical but wide enough to crowd your context, you may instead dispatch instrument `implementer` with its card filled, its `lane` selector set `very-small`: the note at its pinned revision is its requirements, and its report goes to `sdd/reports/lane-report.md`. Log your judgment and its agent identity under `## Progress`, as `Implementer: <agent id> — <why dispatched>`, and transcribe each change-list departure its Decision Log records into a `Departure:` ledger line, since the ledger — not the report — reaches the branch reviewer. The no-commit rule (`crucible:subagent-driven-development` § Shared-tree rules) holds while that implementer works. Inline mode (`crucible:subagent-driven-development` § Inline mode) is a per-task-review device and does not apply.
3. **The branch review** (`crucible:requesting-code-review`). The note at its pinned revision is the requirements input of every seat in it: the branch reviewer's spec-pointer and requirements slots, and the re-reviewer's and the adjudicator's requirements. Where the note's preamble carries an `Umbrella:` line, the umbrellas up the chain are every seat's inputs too, by path — each card's `[UMBRELLAS]` slot, the adjudicator's inputs — and bind beside the note's binding parts: this feature's own entry in that umbrella and the umbrellas' Constraints & invariants and [LOAD-BEARING] marks. Within the reviewed range, a change to those Constraints or marks is a finding, and so is a change to the entry other than the feature's own mark or a clarification the note states that changes nothing another entry waits on; a binding change taken in from the base by a merge is not. The ledger's `Departure:` lines reach the reviewer with the rulings input. Both review cards' `lane` selector is set `very-small`; on the branch reviewer's card it selects the template's lane text, under which the reviewer also states whether the change stays within the lane's qualifying shape. Drift from the note's binding parts is a wave finding here, not a revert-and-replan trigger — there is no plan to replan.
4. **Finish** (`crucible:subagent-driven-development` § Finish), unchanged; its close readout lists the lane's departures.

**Fix waves run inline.** For each wave you apply the findings yourself, run the gates, commit, and write the wave's fix report to `sdd/branch-review/wave-<n>-fix.md`, which the scoped re-review reads as its fix report. It answers each finding **fixed** — what changed, the covering tests, the command and its output, the sibling instances of the defect pattern or none — or **NOT CONFIRMED** with evidence. Every lane diff counts as your own, the optional implementer's included, so a finding you contest goes to the adjudicator (`crucible:subagent-driven-development` § Disputes and adjudication) at any wave; you never dismiss or park one yourself. **For this lane only**, this supersedes the rule that the controller never fixes findings (`crucible:subagent-driven-development` § The Task Loop and `crucible:requesting-code-review`).

**The lane ledger** (binding on this lane; the ledger's other structure is SDD's). Line 1 keeps SDD's identity-line shape with the note's pin where the plan path goes — `# SDD ledger — plan: <note-path> @ <rev>` — so the resume rule's identity check reads it unchanged, and the predecessor-link line keeps its slot. The lane's own lines sit under a `## Lane` section, each on its own line, in these shapes:

```
Lane: very-small (operator-confirmed <date>)
Gates: <what ran> — <result>
Implementation complete: <commit>
Departure: <change-list item> — <what was done instead>
Wave <n>: <X> findings (<b>B/<m>M/<k>m); re-review: <verdict>
Note re-pinned: <note-path> @ <rev> — <operator decision>
Hatch: <decision>
```

written as the lane moves:

- `Lane:` — first, with the confirmation date from the decision record;
- `Gates:` — after implementation, and again after each wave's fixes;
- `Implementation complete:` — once the implementation is committed, citing the commit by hash;
- `Departure:` — one per change-list item the work departed from, zero or more;
- `Wave <n>:` — once the wave's re-review, if any, and its adjudication have returned; `re-review: none` for a wave that only disputes;
- `Note re-pinned:` — on an operator-approved change to the note's binding parts;
- `Hatch:` — when the lane moves to the standard route (below).

The lane has no `Task <N>` lines, so a resumed controller takes its restart point from the last lane line. Adjudications go where every adjudication goes, `## Adjudication rulings`.

**The upgrade hatch.** A reviewer statement that the change exceeds the lane's qualifying shape is an operator decision ask with a recommendation: continue on the lane, or move to the standard route with the note as the spec's seed and the existing diff as a starting point. The standard route's spec and plan are written into the lane's feature folder beside the note, which stays in place as the forensic record, under the names `skills/redteaming/references/formats.md` § Feature folder gives — the folder its resolve step finds, never a new one. Where the note's preamble carries an `Umbrella:` line, the spec's preamble carries the same line. On the move, append the `Hatch:` line, then move the ledger aside. The standard route's ledger names the moved-aside lane ledger on its second line — the predecessor link of `crucible:subagent-driven-development` § Setup — and the new plan's tasks own the carried-over diff, each reviewed under its own task. The folded lane is never a hatch target: its entry is before any artifact is written.
