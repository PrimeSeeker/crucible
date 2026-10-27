Lane: very-small (operator-confirmed 2026-10-27)

## Intent

Adopt, in crucible's form, the nine improvements the v7.0.1 upstream
review took on the maintainer's rulings of 2026-10-27
(`docs/crucible/2026-10-27-upstream-review/dispositions.md`
§ Improvements). Each closes a gap where an agent could pass over a real
defect or misreport its own work.

## Change list

1. The branch and task reviewers (`code-reviewer.md`,
   `task-reviewer-prompt.md`): a spec's silence is not permission; a
   failure on an input the spec implies but never names is graded by its
   effect on a reasonable user, not by whether the spec mentions it.
2. writing-plans, a task's Acceptance: the edge and error scenarios name
   the inputs the spec implies but never names.
3. The implementer's report: test evidence names every failing test,
   whether the change caused it or not.
4. SDD Finish's close readout: lists every ruling the controller made
   (pre-flight, plan conflicts, plan patches, the breaker), not only
   dismissed or parked BLOCKER/MAJOR findings.
5. The redteam seats' Finding scope (`seat-prompt.md`): a consequential
   choice the artifact takes for granted with no Decision entry
   (platform, language, the form of the deliverable) is a finding.
6. brainstorming's Context gathering: a throwaway probe in scratch that
   answers a question is context gathering, never committed, and not the
   code the HARD-GATE forbids.
7. dispatching-parallel-agents, its step 4 and Verification: check each
   agent's diff, not its summary.
8. writing-skills' Portability bullet: invoke a bundled script through
   its interpreter, never by bare path, since packagers can strip
   executable bits.
9. The task reviewer and re-reviewer: evidence that looks truncated, or
   results that cannot be located, are re-read at their stated path
   before being reported missing.

Also: regenerate `agents/`; raise the prose budgets; `docs/upstream.md`'s
verification row stops deferring the diff check to the backlog; delete
`docs/backlog/upstream-adoptions.md`; edit the decision records whose
stated position changes, each with a Changes line (expected:
`adjudication.md` and `records-and-workspace.md` for the close readout,
`plans.md` for the scenario categories, `upstream-skills-kept-close.md`
for dispatching-parallel-agents beyond step 3).

## Acceptance

1. Each of the nine rules is stated once, at the site the change list
   names, with a pointer, not a copy, for any other reader that needs
   it. Checked by the branch reviewer reading each site; no grep pins
   the wording.
2. No added rule contradicts the text around it; in particular, the
   probe clause is consistent with brainstorming's HARD-GATE.
3. `grep -n upstream-adoptions docs/upstream.md` finds nothing, and
   `docs/backlog/upstream-adoptions.md` does not exist.
4. Each decision record whose stated position changed carries the edit
   and a dated Changes line.
5. `python tools/instrument_agents.py check` passes, and
   `python -m pytest tests/` passes.

## Out of scope

Inline execution; spikes beyond scratch probes; a "decided by the
operator" mark; the cost-if-wrong field; a truncation rule for the
branch reviewer; upstream's declined-to-judge list; the skill text
rewrite items; the 0.4.0 release.
