## The Task Loop

### 1. Dispatch the implementer

Where the spec's preamble carries an `Umbrella:` line, first take the receiving step of `skills/brainstorming/references/umbrella-children.md` § Under an umbrella, so a binding change it takes in falls before BASE. Record BASE (`git rev-parse HEAD`), where the task's review range starts (a `plan changed` line's re-run keeps the BASE that line names, and names to its reviewer any merge the receiving step took), then dispatch instrument `implementer`, its card filled.

As soon as the dispatch reports the implementer's agent identity, record `Task <N>: implementer <agent id>` in the ledger: fix waves resume it.

### 2. Handle the report

- DONE or DONE_WITH_CONCERNS: step 3 (a marked task: below).
- NEEDS_CONTEXT: provide the missing context and re-dispatch.
- BLOCKED: assess the cause.
  - Context problem: provide context and re-dispatch.
  - Reasoning problem: bump the tier where one exists (bounded → default role); at the default role the operator decides, and may name the alternate role.
  - Oversized task: split it.
  - Defective plan: escalate (`crucible:subagent-driven-development § Plan changes mid-execution`).
  - A binding item reported wrong: rule that it stands, with your reason, where the evidence does not show it wrong; otherwise a correction, proposed or yours. The ruling passes `skills/redteaming/references/flip-paths.md` § The containment test: confirm and record a contained one as that section states, then re-dispatch; any other is a decision ask carrying the proposal.
  - A premise finding: the task waits for the operator's ruling.

Where the cause leaves the task waiting on the operator (a decision ask, a premise finding), append `Task <N>: BLOCKED — <what it waits on>` as you raise it, the line the resume rule reads as that wait; the re-dispatch after the answer appends step 1's line, which ends it.

Never ignore an escalation or make the same model retry without changes. Whatever the status, route what the report voices beyond its work by `crucible:subagent-driven-development § What a report voices`.

**A marked task** (dispatched, its plan section carrying `Review: branch only`) reporting DONE with no concern runs step 4's gates here, which also confirm the report shows what the task review would read: RED output before GREEN, or the exception logged (you check presence; the branch reviewer judges substance). All passing: no task review and no fix loop; append its completion line (step 6), the task then completed branch review only, the branch reviewer its first review. A concern, a failed gate or a `plan changed` re-run sends it to step 3, the loop running from there.

**Deviations.** The implementer logs each departure from advisory content in its Decision Log (what, why, blast radius); a deferred item is its call, logged where it departs from advisory content. It implements what binds, reading the plan's spec pointer as `skills/subagent-driven-development/references/review-terms.md` § What binds in a spec states, with its task's Contract and Acceptance and the plan's inter-task contracts; changing or contradicting it is BLOCKED (above), with the evidence and a proposed correction, never improvised. Stop-and-ask triggers, for the implementer and for you: insufficient context, an unresolved trade-off, conflicting findings, ambiguity above task authority. Plan ambiguity is never license.

### 3. Review the task

One fresh-context reviewer per task, a task completed branch review only aside (step 2): never skip it; implementer self-review never replaces it. Dispatch instrument `task-reviewer`, its card filled, its base the BASE you recorded; the status check applies (`crucible:subagent-driven-development § Rules every route shares`). Its template ([task-reviewer-prompt.md](../task-reviewer-prompt.md)) requires all four verdicts: intent, scope, deviation audit (ruling on each concern the implementer reported), quality. Never accept a review missing a verdict (`crucible:subagent-driven-development § Rules every route shares`); an unruled concern is one.

Severities: BLOCKER / MAJOR / MINOR. A failed intent, scope or deviation-audit verdict enters the fix loop whatever the finding's severity label; quality findings enter by severity: BLOCKER/MAJOR in, MINOR to the ledger.

Dispatch hygiene: no open-ended directive ("check all uses") without a concrete task-specific reason, no request to re-run tests the report already evidences, no pre-judging findings ("do not flag…", "at most MINOR").

### 4. Verification gates

Confirm the report shows what the task maps each acceptance criterion to: a standing test passing in its quoted run, a one-time check's command and quoted output (plus its failing pre-change run where it checks a state the change brings about), or a stated why-not.

Snapshot or golden output changed under a behavior-preservation claim is blessed only by a fresh blind snapshot-blessing agent given only the old and new output and the claim; it writes `sdd/reports/task-<N>-snapshot-<k>.md`, `<k>` numbering the task's blessings. A change it finds visible is a decision ask: what changed and why it matters, never a raw diff.

### 5. The fix loop

MINOR findings never enter the loop: as each arrives, append `Task <N>: minor (deferred): <one-liner>` under `## Deferred minors`, for the branch review to triage.

Report caught errors, your own included, in the flat register of any finding (`crucible:redteaming § Operating stance`): they are the loop working, not a verdict on the author.

A **fix wave** is one fix dispatch plus its scoped re-review; one whose fix dispatch only disputes still counts. Each wave resumes the recorded implementer with the open findings verbatim, never a new agent in place of a live one; where your dispatch reference says the host exposes no resume operation, each wave dispatches a fresh instrument `implementer`, its card filled by its fix-only rules, and you record that in the ledger.

Every wave:

- The implementer answers each finding fixed or NOT CONFIRMED in a fix report appended to its report file. Before going on, confirm each fixed answer names the covering tests, command, output and sibling instances (or none), and each NOT CONFIRMED its evidence.
- Fixed: scoped re-review by instrument `re-reviewer`, its card filled, ruling each finding ADDRESSED or NOT ADDRESSED. New BLOCKER/MAJOR breakage it flags joins the open findings; its out-of-scope observations go to the ledger as deferred minors. A fix-report concern it leaves unruled is a missing verdict.
- Dispute-only wave: nothing to re-review; the fix report's concerns become leads, routed as in step 2.
- NOT CONFIRMED: ruled on under `crucible:subagent-driven-development § Disputes and adjudication`, those for the adjudicator as one batch.
- Re-review, if any, and dispute rulings in: append `Task <N>: fix wave <W>/3 (<X> addressed, <Y> open, <Z> disputed — <one-liners>; commits <a7>..<b7>)`, `commits none` for a dispute-only wave.

Never fix findings yourself; the exceptions are inline mode, for a task you implement, and the very-small lane's inline fix waves.

### 6. Complete the task

When the review comes back clean, or every open finding is dismissed, or parked by the operator's answer, or step 2 completes a marked task, append the completion line:

- `Task <N>: complete (commits <base7>..<head7>, review clean)`
- `Task <N>: complete (commits <base7>..<head7>, <K> parked)` after a park answer
- `Task <N>: complete (commits <base7>..<head7>, branch review only)` for a task completed branch review only, its leads written first

Mark the todo complete and move on. An open premise finding is a decision ask, not an open BLOCKER/MAJOR: by itself it holds no completion (`skills/redteaming/references/premise-asks.md` § Premise findings).
