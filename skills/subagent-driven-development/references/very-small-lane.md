## The very-small lane

The very-small preset: a settled change one implementer can carry, run from a **lane note**, its only artifact, with no spec campaign, plan or per-task review. The diff is the review object. Only the lane's differences are stated here; everything else runs as elsewhere.

Entry is the operator's, only at brainstorming: you arrive from its handoff once the operator confirmed the lane at its present-the-design step and the brainstorm decision record carries that confirmation. You never declare the lane and nothing converts to it mid-flight; without that record entry this section does not apply and the change goes back to brainstorming.

The note's parts, and which bind, are defined at `crucible:brainstorming § The very-small lane`. What was asked is quoted in the workspace's `request.md`, never in the note. A change to the note's binding parts is an operator decision ask, never your edit: commit an approved one, re-pin it in the ledger, and enter the answer in `brainstorm-decisions.md` (status: `crucible:brainstorming` § Workspace provisioning). A departure from the change list is a ledger line, not a note edit.

What runs, in order:

1. Setup, where it applies (`crucible:subagent-driven-development` § Setup): workspace check and provision, project setup and baseline, and the ledger, seeded with the brainstorm decision record's `— carried` lines. There is no plan to read.
2. Implementation. Where the test of `crucible:subagent-driven-development` § Inline mode holds (the change overdetermined and fitting your remaining context), implement test-first where a seam exists, evidence before done; run the repo's verification gates; commit. Only that test applies, not the section's review clause: the lane has no task review. Otherwise dispatch instrument `implementer`, its card filled for the lane; log `Implementer: <agent id> — <why dispatched>` under `## Progress`, and commit nothing while it works. Its premise finding goes where `skills/redteaming/references/premise-asks.md` § Premise findings sends it. Transcribe each change-list departure its Decision Log records into a `Departure:` line, and each concern, `Questions` item and out-of-task proposal in its report into a `## Deferred minors` lead, `Lane: lead: <one-liner>`: the ledger, not the report, reaches the branch reviewer, the lane's first review, which rules on them.
3. The branch review (`crucible:requesting-code-review`), each seat's card filled for the lane. Drift from the note's binding parts is a wave finding, not an operator ask: the lane has no tasks to revert.
4. Finish (`crucible:subagent-driven-development` § Finish).

Fix waves run inline, the cleanup wave included, **for this lane only** superseding the rule that you never fix findings: for each wave, apply the findings yourself, run the gates, commit, and write `sdd/branch-review/wave-<n>-fix.md`, the scoped re-review's fix report. It answers each finding fixed or NOT CONFIRMED with what [implementer-prompt.md](../implementer-prompt.md) § After Review Findings asks of that answer, and each labelled change (`Change (<kind>): …`) applied, with what changed and its covering tests, or declined, with its reason. Every lane diff counts as your own, the optional implementer's included, so a finding you contest, at any wave, goes to the adjudicator; you never dismiss or park one yourself.

**The lane ledger** keeps SDD's structure but for these rules. Line 1 is `# SDD ledger — plan: <note-path> @ <rev>`, SDD's identity line with the note's pin for the plan path, so the resume rule's identity check reads it unchanged. The lane's own lines go under `## Lane`, written as the lane moves:

- `Lane: very-small (operator-confirmed <date>)` — first, the date from the decision record.
- `Gates: <what ran> — <result>` — after implementation and after each wave's fixes.
- `Implementation complete: <commit>` — once the implementation is committed, by hash.
- `Departure: <change-list item> — <what was done instead>` — one per change-list item departed from, zero or more.
- `Wave <n>: <X> findings (<b>B/<m>M/<k>m); re-review: <verdict>` — once the wave's re-review, if any, and its adjudication have returned; `re-review: none` for a wave that only disputes.
- `Wave <n> (cleanup): <X> findings (<b>B/<m>M/<k>m); re-review: <verdict>` — for the cleanup wave, so a resumed controller sees it spent.
- `Note re-pinned: <note-path> @ <rev> — <operator decision>` — on an operator-approved change to the note's binding parts.

With no `Task <N>` lines, a resumed controller restarts from the last line under `## Lane`; a `Lane: lead` line sits under `## Deferred minors` and is not one. Adjudications go under `## Adjudication rulings`, as everywhere.

**The upgrade hatch.** Where a reviewer's finding or question, or your own reading, shows that overturning a major mechanism of the change is reasonably expected now that it is coded (`review-terms.md` § The arrangement questions), staying on the lane or moving to the standard route is an operator decision ask. On the move, record the answer as `crucible:brainstorming` § Proposing the arrangement states; move `sdd/` aside whole as `sdd-lane/`, so no later report reuses a path the lane wrote; then invoke `crucible:brainstorming` with the note, the diff, and the lane's open findings, unruled leads and departures as its incoming document, proposing no preset. Its spec goes into the lane's feature folder beside the note; the plan's tasks build on the carried-over diff. The folded lane is never a hatch target: its entry precedes any artifact.
