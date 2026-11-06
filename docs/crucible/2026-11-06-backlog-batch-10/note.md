Lane: very-small (operator-confirmed 2026-11-06)

# Backlog batch 10: close three design items

## Intent

Three backlog items hold questions that can now be answered, and the answers are to decline. `escalation-and-effort` asks for a stuck trigger on the alternate role; a read of late waves and rounds found failed fixes rare and no sign of repeats. `lane-entry-and-downshift` and the separability point of `skill-text-rewrite` are one question, whether a lane note may carry a plan or a campaigned spec may skip one. The rest of `skill-text-rewrite` has been overtaken or has one sighting. Each answer goes in its decision record, with what the evidence could not show, and the items are deleted.

Goals: the three items gone, each decision and its limits in a record, every pointer at the items updated, and the re-audit asked to count repeats on real code.

Non-goals: no skill, template, hook or test changes, and so no release. This breaks nothing.

## Change list

**`docs/decisions/model-roles-and-effort.md`.** In § Why, replace from "Nothing escalates a stuck seat to it." to "`docs/backlog/escalation-and-effort.md`." with the text below, keeping the sentence that follows it:

> Nothing escalates a stuck seat to it. The maintainer: "Late waves are generally not stuck, just slowly mining the residual issues." A seat is stuck when the same finding fails its re-review on successive fix attempts. Script counts over the transcripts on disk (2026-11-06; about 120 features, on this repository and one other project whose runs ended by 2026-10-23) agree as far as they can see. 11 of 740 parsed re-review verdicts failed, and at most one feature failed at two separate re-reviews. Text matching linked none of the 11 to any later verdict, so it shows no repeat without ruling one out. Of 496 implementers, 6 reported BLOCKED in an explicit status line, none on a fix-wave dispatch, though a status was readable on only 188; none ran on the alternate role, so nothing shows that role would unstick a seat. Of the 70 tasks whose fix-wave lines the script captured from the ledgers, none reached a third wave. In campaigns, findings worded as repeats were as common in round 1 (6.9%) as later (6.5%), and rounds past the first kept raising about 2 to 4 BLOCKER or MAJOR findings per campaign, among those that reached them. None of this was read by eye, and little of it is real code under the current rules, so the re-audit counts repeats there (`docs/backlog/skill-rewrite-reaudit.md`). A task's third wave already goes to the operator, who may name the alternate role, so the trigger is declined.

In § Rejected, replace the stuck-trigger entry with:

> - **A stuck trigger for the alternate role**: failed fixes are rare, nothing shows a repeat, and a task's third wave already reaches the operator (§ Why).

Add at the top of § Changes:

> - 2026-11-06: a stuck trigger is declined, no longer open, on a read of late waves and rounds whose limits § Why states; because failed fixes were rare and a task's third wave already reaches the operator.

**`docs/decisions/task-loop.md`.** Point "A stuck trigger stays out" at `docs/decisions/model-roles-and-effort.md` in place of the backlog item. A citation, so no Changes line.

**`docs/decisions/routes.md`.** In § Separable choices, replace "; both wait in `docs/backlog/lane-entry-and-downshift.md`, the first with its trigger: a settled change campaigned only to get a plan." with:

> . Both stay out (2026-11-06): each would add a route to maintain for a need not yet shown. Every feature with a role file after `compaction-fit` has been a lane note, though whether a batch among them would have gone better with a plan is unmeasured. The first reopens on its trigger, a settled change campaigned only to get a plan.

In § The overturn question as the selector, replace "The wider question of how far the choices separate is the skill-text rewrite's (`docs/backlog/skill-text-rewrite.md`)." with "The wider question of how far the choices separate closed on 2026-11-06, with both arrangements left out (§ Separable choices)."

Add to § Rejected:

> - **A lane note with a plan, or a campaigned spec with no plan** (§ Separable choices).

Add at the top of § Changes:

> - 2026-11-06: a lane note with a plan and a campaigned spec with no plan stay out, no longer waiting in the backlog, and the wider question of how far the choices separate closes with them; because each would add a route for a need not yet shown. The first's trigger stands in § Separable choices.

**`docs/decisions/umbrellas.md`.** At the end of § Binding changes off the child's branch, add:

> A clause-sized binding change gets no exemption from that landing (2026-11-06). One feature needing two landings for one-clause edits is the one sighting, a child's clarification of its own entry already rides its branch, and only two umbrellas have run; a second sighting reopens it. (Basis: judgment, accepted by the maintainer.)

Add to § Rejected:

> - **A clause-sized exemption from a binding change's own landing** (§ Binding changes off the child's branch).

Add at the top of § Changes:

> - 2026-11-06: a clause-sized binding change keeps its own landing, no longer an open question in the backlog; because the need has one sighting and a child's clarification of its own entry already rides its branch.

**`docs/decisions/fix-verification-and-merge.md`.** Add to § Rejected:

> - **A restructuring of how a tension gets closed**, deferred by the maintainer as "probably later" and declined on 2026-11-06: the fix list already takes fix-by-deletion as a first-class resolution, removing machinery outranking adding it, all else equal (`skills/redteaming/references/fix-application.md`). Whether reviews still close tensions by adding distinctions is unmeasured; a fresh sighting reopens it. (Basis: judgment, accepted by the maintainer.)

Add at the top of § Changes:

> - 2026-11-06: a restructuring of how a tension gets closed is declined, no longer open in the backlog; because the fix list already ranks removing machinery above adding it, all else equal.

**`docs/backlog/skill-rewrite-reaudit.md`.** Add to its Follow-up, after the paragraph on controllers re-reading a moved step's reference:

> In the same runs, count findings that fail their re-review on successive waves. A stuck trigger was declined on evidence with little real code under the current rules (`docs/decisions/model-roles-and-effort.md` § Why), and repeats there reopen it.

**`docs/backlog/`.** Delete `escalation-and-effort.md`, `lane-entry-and-downshift.md` and `skill-text-rewrite.md`.

## Acceptance

Run from the worktree root in PowerShell:

1. `python -m pytest tests/` passes, quoting its summary line.
2. `git grep -n -E "escalation-and-effort|lane-entry-and-downshift|skill-text-rewrite\.md" -- . ":!docs/crucible"` prints nothing.
3. `(git ls-files docs/backlog).Count` prints 9.
4. `git grep -c -E "11 of 740 parsed" -- docs/decisions/model-roles-and-effort.md` finds one line.
5. `git diff --name-only 178f6ed...HEAD -- skills agents hooks tests tools .claude-plugin .codex-plugin` prints nothing.

## Out of scope

Skill text, the version and a release. The two Codex backlog items, which this lane's own run informs and which are recorded after it. Any other backlog item. Re-running the transcript scripts: their figures are checked on the Claude side, where they ran.
