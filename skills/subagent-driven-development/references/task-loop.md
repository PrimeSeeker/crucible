## The Task Loop

### 1. Dispatch the implementer

Record BASE (`git rev-parse HEAD`) before dispatching — the task's review range starts there. Where the spec's preamble carries an `Umbrella:` line, take the receiving step of `skills/redteaming/references/flip-paths.md` § Under an umbrella first, so a binding change it takes in falls before BASE, outside the task's range.

Dispatch instrument `implementer`, its card filled.

**Record the implementer's agent identity in the ledger as soon as the dispatch reports it**, as `Task <N>: implementer <agent id>` — its fix waves resume that identity.

### 2. Handle the report

- **DONE:** dispatch the reviewer (step 3; a marked task: below).
- **DONE_WITH_CONCERNS:** dispatch the reviewer (step 3).
- **NEEDS_CONTEXT:** provide the missing context and re-dispatch.
- **BLOCKED:** assess — a context problem gets context and a re-dispatch; a reasoning problem a tier bump where one exists (the bounded role → the default role), and at the default role the operator's call, who may name the alternate role; an oversized task a split; a defective plan an escalation (`crucible:subagent-driven-development § Plan changes mid-execution`). On a report that a binding item is wrong, your ruling — the item stands where the evidence does not show it wrong, with your reason; otherwise the correction, proposed or yours — passes `skills/redteaming/references/flip-paths.md` § The containment test: a contained one you confirm and record as that section states, then re-dispatch; any other goes to the operator as a decision ask carrying the proposal. A task blocked on a premise finding waits for the operator's ruling. Never ignore an escalation or make the same model retry without changes.

**A marked task** — dispatched, its plan section carrying `Review: branch only` (`crucible:writing-plans` § Per-task structure) — gets no task review and no fix loop where its report is DONE, raises no concern and passes the gates of step 4. Append its completion line (step 6): it is then a task completed branch review only, the branch reviewer its first review. A report raising a concern or failing a gate sends the task to step 3, to run the task loop from there.

Whatever the status, route what the report voices beyond its work by `crucible:subagent-driven-development § What a report voices`.

**Deviations.** The implementer may depart from advisory content, each departure in its Decision Log (what, why, blast radius); a deferred item is its call, logged where it departs from advisory content. What binds is what the plan's spec pointer names, at the pinned revision, read as the opening of `skills/redteaming/references/flip-paths.md` § Flip paths — scoped amendment and supersede states. Under an umbrella, the umbrella content `skills/brainstorming/references/umbrellas.md` § Children names binds too, and within a reviewed range a binding change to it, as § Edits defines one, is a finding. Implementing what binds is the job; changing or contradicting it is BLOCKED, with the evidence and a proposed correction (BLOCKED, above), never improvised. Stop-and-ask triggers, for the implementer and for you: insufficient context, an unresolved trade-off, conflicting findings, ambiguity above task authority. Plan ambiguity is never license. Drift found after the fact goes to `crucible:subagent-driven-development § Drift found after the fact`.

### 3. Review the task

One fresh-context reviewer per task, a task completed branch review only aside (step 2). Never skip it, never accept a report missing any verdict — a concern the implementer reported and the review left unruled is a missing verdict; implementer self-review never replaces it.

Dispatch instrument `task-reviewer`, its card filled, its base the BASE you recorded. The status check applies (`crucible:subagent-driven-development § Rules every route shares`). Its template ([task-reviewer-prompt.md](../task-reviewer-prompt.md)) holds its adversarial mandate and the **four verdicts, all required** — intent, scope, deviation audit, quality — each concern the report raises ruled on in the deviation audit.

**Loop wiring:** severities are **BLOCKER / MAJOR / MINOR**. A failed intent, scope or deviation-audit verdict enters the fix loop **regardless of the finding's severity label**; quality findings enter by severity — BLOCKER/MAJOR in, MINOR to the ledger.

Dispatch hygiene: no open-ended directives ("check all uses") without a concrete task-specific reason; never ask the reviewer to re-run tests the report already evidences; never pre-judge findings ("do not flag…", "at most MINOR").

### 4. Verification gates

Every acceptance criterion in the task maps to a standing test, a one-time check or a stated why-not — confirm the report shows each: a standing test passing in its quoted run; a one-time check's command and quoted output, plus its failing pre-change run where it checks a state the change brings about.

For a marked task they run at step 2 and also confirm what the task review would read in the report: RED output before GREEN, or the exception logged. You check it is there; the branch reviewer judges its substance.

- **Snapshot or golden output** changed under a behavior-preservation claim is blessed only by a fresh blind snapshot-blessing agent, given the old and new output and the claim, nothing else, writing `sdd/reports/task-<N>-snapshot-<k>.md` (`<k>` numbering the task's blessings); a change it finds visible goes to the operator as a decision ask: what changed and why it matters, never a raw diff.

### 5. The fix loop

**MINOR findings** never enter the loop: they go to the ledger as they arrive (`Task <N>: minor (deferred): <one-liner>`, under `## Deferred minors`), for the branch review to triage. A contested finding goes to `crucible:subagent-driven-development § Disputes and adjudication`.

**Caught errors — your own included — are the loop working, not a verdict on the author:** report them in the same flat register as any finding (`crucible:redteaming § Operating stance`).

**Waves.** A fix wave is one fix dispatch plus its scoped re-review. A wave whose fix dispatch only disputes is still a wave. Each wave **resumes the recorded implementer** with the open findings verbatim: a fix wave never starts a new agent in place of a live one. Where your dispatch reference states this host exposes no resume operation, each wave dispatches a fresh instrument `implementer`, its card filled by its fix-only rules: record that in the ledger.

**Every wave.** The implementer answers each finding **fixed** or **NOT CONFIRMED** in a fix report appended to its report file, as its template states. Before going on, confirm each fixed answer names the covering tests, the command, the output and the sibling instances (or none), and each NOT CONFIRMED its evidence. Then:

- **Findings answered fixed** get the scoped re-review: instrument `re-reviewer`, its card filled. It verdicts each finding ADDRESSED or NOT ADDRESSED; new BLOCKER/MAJOR breakage it flags joins the open findings, and its out-of-scope observations go to the ledger as deferred minors. A re-review that leaves a fix-report concern unruled is missing a verdict. A wave that only disputes has nothing to re-review: its fix report's concerns become leads (`crucible:subagent-driven-development § What a report voices`).
- **Findings answered NOT CONFIRMED** are ruled on under `crucible:subagent-driven-development § Disputes and adjudication`, those for the adjudicator as one batch.

Once the wave's re-review, if any, and the rulings on its disputes are in, append `Task <N>: fix wave <W>/3 (<X> addressed, <Y> open, <Z> disputed — <one-liners>; commits <a7>..<b7>)`, with `commits none` for a wave that only disputes.

Never fix findings yourself in the controller session. Inline mode is the sanctioned path for a task you implement, and the very-small lane's inline fix waves are the one other exception.

### 6. Complete the task

When the review comes back clean — or every open finding is dismissed, or parked on the operator's answer, or step 2 completes a marked task — append the completion line:

- `Task <N>: complete (commits <base7>..<head7>, review clean)`
- `Task <N>: complete (commits <base7>..<head7>, <K> parked)` after a park answer
- `Task <N>: complete (commits <base7>..<head7>, branch review only)` for a task completed branch review only, its leads written first

Mark the todo complete and move on. Never move to the next task while an open BLOCKER/MAJOR finding is neither fixed nor dismissed nor parked on the operator's answer. An open premise finding is a decision ask, not an open BLOCKER/MAJOR: it holds no completion by itself (`skills/redteaming/references/flip-paths.md` § Premise findings).
