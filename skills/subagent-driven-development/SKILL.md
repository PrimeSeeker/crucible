---
name: subagent-driven-development
description: Use when executing an implementation plan or a very-small-lane note.
---

# Subagent-Driven Development

Execute a plan by dispatching a fresh implementer subagent per task and a single fresh-context reviewer after each, then hand the branch to `crucible:requesting-code-review` for its capped whole-branch review. The one route with no plan is the operator-confirmed very-small lane: § The very-small lane executes its lane note, and the rest of this skill applies to it only where that section says so.

**Why subagents:** a seat never inherits your session's history — you construct exactly what it needs, which keeps it focused and keeps your own context for coordination.

**Narration:** between tool calls, narrate at most one short line — the ledger and the tool results carry the record.

**Continuous execution:** do not pause to check in with the operator between tasks. Stop only for a BLOCKED status you cannot resolve, a stop-and-ask trigger, a decision ask that genuinely needs the operator, or all tasks complete — never a "should I continue?". A decision ask is analyst-language with a recommendation: it never requires reading plan, code or a diff, and may quote the few lines it turns on.

**Dispatch reference:** read `skills/using-crucible/references/<runtime>-dispatch.md` from the plugin root when this skill starts, and again after compaction — it holds your adapter's instrument-dispatch, resume and effort operations.

## Setup

**A plan crucible did not produce** goes to `crucible:brainstorming` as its input before any Setup step creates anything.

**Find the feature workspace first** — `.crucible/<feature-slug>/`, before the worktree step and before provisioning:

- **In this checkout:** proceed.
- **In another checkout** (`git worktree list`): continue there, working from that checkout's path; create no worktree and provision no empty workspace here. Where your host cannot work from another path, stop and tell the operator where the workspace is.
- **Nowhere:** create the isolated worktree with `crucible:using-git-worktrees`, and provision the workspace in the checkout that step leaves you in.

In every case, implementation on a main/master checkout needs the operator's explicit consent first. In the checkout you work from, run the provisioning step (`skills/redteaming/references/formats.md` § Feature workspace root and layout) — re-running it changes nothing, so run it rather than assume. Then run `crucible:using-git-worktrees` Steps 2–3 there, the project setup and the clean baseline — unless that skill just ran them, creating the worktree above — and record the result in the ledger (below) under `## Progress` as `Baseline: <result> at <sha7>`. A ledger that already carries that line means both ran: skip them on resume.

The workspace's `sdd/` subtree holds this plan's execution state: `ledger.md`, `reports/`, `branch-review/`. Another feature's workspace is never yours to read or write, except to follow a declared predecessor link (below).

**The ledger** (`sdd/ledger.md`). Conversation memory does not survive compaction; controllers that lost their place have re-dispatched whole completed task sequences, the most expensive failure observed. Track progress in the ledger, not only in todos.

- Line 1 is the identity line: `# SDD ledger — plan: <plan file path>`.
- Sections: `## Progress` for the running lines, then `## Adjudication rulings` and `## Deferred minors`.
- **The deferred list** carries one entry per row of the plan's deferred-items routing table — id, one-line intent, owning task — seeded at the close of the phase that produced the plan (`crucible:redteaming § The plan phase — one verification round`; where the plan is folded into the spec, the spec campaign's close). **Whenever a plan you execute has routing rows and its ledger has none — on resume or first entry alike — seed them yourself before dispatching:** they are the only record that the items were deferred rather than forgotten, and their closure chain (the implementer's Decision Log entry, checked at that task's review, swept at the branch review) starts here.
- **Contained amendments** the plan phase made are seeded at its close under `## Adjudication rulings`, as your rulings (`skills/redteaming/references/plan-phase.md`). **Whenever the plan record's `## Fix list` (`campaigns/plan/round-01/record.md`) names a `Contained amendment:` item the ledger lacks, copy it there yourself before dispatching, in the item's own form:** the branch review and the close readout find it only in the ledger.
- **Resume rule:** if line 1 names your plan, a task with a `Task <N>: complete` line is done — never re-dispatch it — unless a later `Task <N>: reverted` line supersedes it (§ Revert-and-replan); resume at the first task not done. A task whose last line is a fix wave is mid-loop: resume at the next wave. On the very-small lane, re-read its reference first.
- **Predecessor links:** when a plan is superseded mid-flight, the successor ledger's line 1 names the successor plan and its line 2 links the predecessor ledger, moved aside (e.g. `sdd/ledger-superseded.md`). On resume, follow predecessor links **before declaring any task not done** — the sanctioned exception to workspace isolation. If the predecessor records are gone, recover as from a lost workspace (below).
- A ledger whose line 1 names a plan that is neither yours nor a declared predecessor is another run's: leave it in place and escalate, never overwrite it.
- After compaction, trust the ledger and `git log` over your recollection. `git clean -fdx` destroys the gitignored workspace: the in-flight phase restarts from the committed spec or plan and `git log`, and the session transcripts hold the lost records if they are needed.

**Read the plan once** — its spec pointer included: the header line naming the spec at its pinned revision and what the pin makes binding — and create a todo per task. The spec is a shared input each seat opens for itself from that pointer; no dispatch copies it.

**Pre-flight plan-conflict scan.** Before Task 1, scan the plan once for tasks that contradict each other or the spec at its pinned revision — or, where the spec's preamble carries an `Umbrella:` line, what binds through it, as the Deviations paragraph of § The Task Loop states; a task calling for a change to the umbrella's Constraints & invariants, [LOAD-BEARING] marks or firm decisions up the chain, or to this feature's own entry in it other than a clarification the spec states that changes nothing another entry waits on, is such a contradiction — and for anything the plan mandates that the review rubric treats as a defect. Rule on each as a plan conflict, under § Disputes and adjudication, which names those the operator rules on, and proceed. The review loop remains the net for conflicts that only emerge from implementation.

## Runtime identity in every dispatch

Every seat you start carries the seven-item dispatch composition in `skills/subagent-driven-development/references/dispatch-composition.md` — read it before your first dispatch and again after compaction; it binds as if written here. In the task loop the plan header's spec pointer carries the binding pin for every seat: point at the plan and restate no revision.

**Instruments.** Three seats are instruments, each with a slot card beside its template: instrument `implementer` ([implementer-prompt.slots.md](implementer-prompt.slots.md)) for every implementer seat, a task's fresh wave-4–5 one included; instrument `task-reviewer` ([task-reviewer-prompt.slots.md](task-reviewer-prompt.slots.md)); instrument `re-reviewer` ([re-review-prompt.slots.md](re-review-prompt.slots.md)). Read the card, not the template ([implementer-prompt.md](implementer-prompt.md), [task-reviewer-prompt.md](task-reviewer-prompt.md), [re-review-prompt.md](re-review-prompt.md)), and dispatch the instrument with its filled card through your adapter's instrument-dispatch operation. Set every selector to one value; a passage left unselected — `lane` set `off` — is dropped, not narrated. The two controller-composed dispatches no template serves, the adjudicator (§ Disputes and adjudication) and the snapshot-blessing blind agent (§ The Task Loop, step 4), carry the seven items in the prompt you compose.

**Report files.** Every review seat and the adjudicator writes its own report file, at a path no earlier dispatch used, and replies with a short verdict and that path. Confirm the file is on disk before taking the reply as the report; a missing file follows the dispatch composition's item 5.

## Models

The rules every dispatch shares — name the model, the three roles and the floor, effort — are in `skills/subagent-driven-development/references/dispatch-composition.md` § Models and effort. This skill's seats:

- **Implementer:** the default role, or the alternate role where one of its triggers selects this seat; a clearly bounded task may drop to the bounded role.
- **Task reviewer and re-reviewer:** the bounded role or better, always.
- **Adjudicator:** the default role — its dismissals close findings without further review.
- **Snapshot-blessing agent:** the bounded role or better — a blind check of one stated claim.
- **Escalation, fix waves 4–5:** a tier bump where one exists (the bounded role → the default role); at the default role, its ceiling, fresh eyes at the same tier.

## The Task Loop

Everything you paste into a dispatch prompt — and everything a seat prints back — stays resident in your context for the rest of the session. Hand artifacts over as files.

### 1. Dispatch the implementer

Record BASE (`git rev-parse HEAD`) before dispatching — the task's review range starts there. Where the spec's preamble carries an `Umbrella:` line, take the receiving step of `skills/redteaming/references/flip-paths.md` § Under an umbrella: binding changes and late splits first, so a binding change it takes in falls before BASE, outside the task's range.

Dispatch instrument `implementer` with its card filled per its slot rules: the plan's path and the task's number as `[REQUIREMENTS]`, `sdd/reports/task-<N>-report.md` as `[REPORT_FILE]`. The seat reads the plan in its worktree — the header and its own task's section, or the whole document where the plan is folded into the spec. Where routing-table rows name its task, the plan reminder adds that **each routed item gets its own Decision Log entry** recording the call made. Never paste accumulated prior-task history, and never quote the spec: each seat opens it at the pinned revision the plan header names.

**Record the implementer's agent identity in the ledger as soon as the dispatch reports it**, as `Task <N>: implementer <agent id>` — fix waves 1–3 resume that identity. Never run two implementers at once: they share the tree.

### 2. Handle the report

- **DONE:** dispatch the reviewer (step 3).
- **DONE_WITH_CONCERNS:** read the concerns first. Correctness or scope concerns are addressed before review; observations are noted and review proceeds.
- **NEEDS_CONTEXT:** provide the missing context and re-dispatch.
- **BLOCKED:** assess — a context problem gets context and a re-dispatch; a reasoning problem a tier bump where one exists (the bounded role → the default role), and at the default role the operator's call, who may name the alternate role; an oversized task a split; a defective plan an escalation (§ Plan changes mid-execution). A report that a binding item is wrong names the item, its evidence and a proposed correction: an item the evidence does not show wrong stands, and you re-dispatch with your reason, recorded as your ruling; otherwise the correction, proposed or yours, passes `skills/redteaming/references/flip-paths.md` § The containment test — a contained one you confirm and record as that section states, then re-dispatch; any other goes to the operator as a decision ask carrying the proposal. Never ignore an escalation or make the same model retry without changes.

**Deviations.** The implementer may depart from advisory content, each departure in its Decision Log (what, why, blast radius). What the plan's spec pointer names — the spec's Constraints & invariants, its [LOAD-BEARING] marks, any preamble convention it declares binding and the decisions it records as the operator's firm preference, at the pinned revision — is binding, and so, where the spec's preamble carries an `Umbrella:` line, are this feature's own entry in that umbrella and the umbrella's Constraints & invariants, [LOAD-BEARING] marks and firm decisions, up the chain through each umbrella's own line, each seat reading them in its own worktree. The spec is a hypothesis, probably subtly wrong: binding means never changed silently, and binding text is read for its intent — a case its literal reading reaches that its author plainly did not consider is raised for a ruling, never applied literally. Implementing what binds is the job; changing or contradicting it is BLOCKED, with the evidence and a proposed correction (BLOCKED, above), never improvised. Within a reviewed range, a change to the umbrellas' Constraints, marks or firm decisions is a finding, and so is a change to the entry other than the feature's own mark or a clarification its spec states that changes nothing another entry waits on; a binding change taken in from the base by a merge is not. Routed deferred items are the implementer's call, and the Decision Log entry recording it is what the review checks. Stop-and-ask triggers, for the implementer and for you: insufficient context, an unresolved trade-off, conflicting findings, ambiguity above task authority. Plan ambiguity is never license. Drift found after the fact goes to § Revert-and-replan.

### 3. Review the task

One fresh-context reviewer per task. Never skip it, never accept a report missing any verdict; implementer self-review never replaces it.

Dispatch instrument `task-reviewer` with its card filled: the plan pointer, the implementer's report (its Decision Log is the deviation audit's input), the range BASE..HEAD, and `sdd/reports/task-<N>-review.md` as its report file. Use the BASE you recorded — never `HEAD~1`, which silently drops all but the last commit of a multi-commit task. The reviewer builds the diff itself, so it never enters your context. The tree check applies (§ Shared-tree rules).

**Mandate:** adversarial — "attempt to reject this task". The stance governs the search, not the conclusion: a clean verdict is a legitimate outcome, and a manufactured finding costs a fix wave. Severity vocabulary everywhere: **BLOCKER / MAJOR / MINOR**, staked with evidence; improvements, style and formatting no repo tool enforces are not findings.

**Four verdicts, all required:**

- **intent** — every requirement implemented, against the plan's intent;
- **scope** — nothing outside the task changed; a weakened test is a scope finding, and so is a deleted test or case unless the Decision Log names a justification the code bears out: the subject removed, a covering test, a requirement or finding the deletion fulfils, or a warning sign from `skills/subagent-driven-development/writing-good-tests.md` the test shows;
- **deviation audit** — each Decision Log entry justified; undisclosed deviations are findings; **every deferred item the plan routes to this task has a Decision Log entry recording the call**, since this review is its only scheduled check before the branch-review sweep; work done test-first shows RED output before GREEN, or the Decision Log records the exception;
- **quality** — defects, not style. New-test adequacy is the reviewer's own judgment.

The reviewer may also return **cannot-verify items** — requirements living outside the diff. Resolve each yourself before the task completes (you hold the plan and the cross-task context); a confirmed gap is a failed intent verdict.

**Loop wiring:** a failed intent, scope or deviation-audit verdict enters the fix loop **regardless of the finding's severity label**; quality findings enter by severity — BLOCKER/MAJOR in, MINOR to the ledger.

Dispatch hygiene: no open-ended directives ("check all uses") without a concrete task-specific reason; never ask the reviewer to re-run tests the report already evidences; never pre-judge findings ("do not flag…", "at most MINOR").

### 4. Verification gates

Every acceptance criterion in the task maps to a standing test, a one-time check or a stated why-not — confirm the report shows each: a standing test passing in its quoted run; a one-time check's command and quoted output, plus its failing pre-change run where it checks a state the change brings about.

- **Snapshot/golden blessing** (where behavior preservation is the claim): **never autonomous.** A fresh blind agent — given the old/new output pair and the behavior-preservation claim, nothing else — verdicts the change: it writes `sdd/reports/task-<N>-snapshot-<k>.md`, `<k>` numbering the task's blessings, and replies with its verdict, preserved or intent-visible, and that path. One it judges intent-visible goes to the operator as a decision ask: what changed and why it matters, never a raw diff to read.

### 5. The fix loop

The loop triggers on a failed intent, scope or deviation-audit verdict, a BLOCKER or MAJOR quality finding, or a cannot-verify item you confirmed as a real gap. **MINOR findings** never enter it: they go to the ledger as they arrive (`Task <N>: minor (deferred): <one-liner>`, under `## Deferred minors`), for the branch review to triage. A contested finding goes to § Disputes and adjudication.

**Caught errors — your own included — are the loop working, not a verdict on the author:** report them in the same flat register as any finding (`crucible:redteaming § Operating stance — baseline error rate`).

**The ladder.** A fix wave is one fix dispatch plus its scoped re-review. **Five waves at most per task** — the cap, with the breaker, is the loop's termination guarantee. A wave whose fix dispatch only disputes is still a wave.

- **Waves 1–3 — resume the recorded implementer identity** with the open findings verbatim. Its context is intact, and resuming it is the rule: a fix wave never starts a new agent in place of a live one.
- **Waves 4–5 — escalate** (§ Models): a fresh instrument `implementer`, its card filled by the card's fix-only rules — the plan pointer, the open findings verbatim with their source report files, and the task's report file to append to, which holds what was tried. A loop that survives three resumes usually means the implementer cannot see its own problem.
- Where your dispatch reference states this host exposes no resume operation, that fresh seat is the path from wave 1: record that in the ledger.

**Every wave.** The implementer confirms each defect and names its cause before editing, checks the task's diff for sibling instances of the pattern, and answers each finding **fixed** or **NOT CONFIRMED** in a fix report appended to its report file — with a Decision Log entry for any departure, as in its first report. Before going on, confirm each fixed answer names the covering tests, the command, the output and the sibling instances (or none), and each NOT CONFIRMED its evidence. Then:

- **Findings answered fixed** get the scoped re-review: instrument `re-reviewer` with its card filled — the plan pointer, those findings verbatim, the task's report file as the fix report, the range FIX_BASE..HEAD (FIX_BASE = the head the previous review saw), and `sdd/reports/task-<N>-re-review-w<W>.md` as its report file. It verdicts each finding ADDRESSED or NOT ADDRESSED and flags new breakage in the fix diff only: new BLOCKER/MAJOR breakage joins the open findings; out-of-scope observations go to the ledger as deferred minors. A wave that only disputes has nothing to re-review.
- **Findings answered NOT CONFIRMED** go to the adjudicator as one batch.

Once the wave's re-review, if any, and its adjudication have returned, append `Task <N>: fix wave <W>/5 (<X> addressed, <Y> open, <Z> disputed — <one-liners>; commits <a7>..<b7>)`, with `commits none` for a wave that only disputes.

Never fix findings yourself in the controller session: your context stays clean for coordination, and controller fixes skip review. Inline mode is the sanctioned path for a task you implement, and the very-small lane's inline fix waves are the one other exception.

**The breaker.** When wave 5 leaves findings open, stop dispatching and rule on each — you hold the plan and the cross-task context the reviewer lacks:

- **One you judge wrong** goes to the adjudicator, as at any wave; one it upholds stays open for the rulings below.
- **Real, but nothing downstream builds on it:** park it — `Task <N>: parked — <finding> — ruling: <why it is deferred>`. On a diff you wrote, this ruling too goes to the adjudicator.
- **Real and load-bearing** — a later task builds on it, or it reveals a plan defect: STOP. Append `Task <N>: BLOCKED — <reason>` and report to the operator as a decision ask with a recommendation: the finding, the plan text it collides with, and the fix history. Parking a structural failure lets every dependent task build on it.

### 6. Complete the task

When the review comes back clean — or every open finding is dismissed or parked with a ruling at the cap — append the completion line:

- `Task <N>: complete (commits <base7>..<head7>, review clean)`
- `Task <N>: complete (commits <base7>..<head7>, <K> parked)` after a tripped breaker

Mark the todo complete and move on. Never move to the next task while an open BLOCKER/MAJOR finding is neither fixed nor dismissed nor parked with a ruling at the cap.

## Rules every route shares

These hold in the task loop, in the branch review `crucible:requesting-code-review` runs, and on the very-small lane.

### Disputes and adjudication

A finding is fixed or disputed, never dropped: a silent discard is forbidden, and every ruling is a ledger entry.

**Who rules.** You rule on two kinds only: a plan-conflict finding — one that collides with plan text, or a reviewer's finding that a binding item's literal reading reaches a case its author did not consider — on a diff you did not write (is the plan or the work wrong?), and the breaker's consequence rulings at the task-loop cap. Your rulings go to `## Adjudication rulings` too. A plan conflict that is a design judgment goes to the operator as a decision ask instead; a ruling of yours that touches binding content (the Deviations paragraph of § The Task Loop) passes `skills/redteaming/references/flip-paths.md` § The containment test, and one it does not find contained goes to the operator as a decision ask. Everything else contested goes to a fresh adjudicator seat: an implementer's NOT CONFIRMED, a finding you judge wrong (at the cap included), and any plan-conflict finding on a diff you wrote (inline mode, the very-small lane). A finding that both fails a verdict and conflicts with plan text is ruled on first as a plan conflict; if the ruling upholds the plan, the verdict failure stands and enters the loop.

**The adjudicator dispatch.** Disputes go in batches — one wave's NOT CONFIRMED findings, or your own disputes raised together at any point — and each batch goes to one fresh adjudicator seat, composed by you with the seven items. Its inputs: each disputed finding verbatim with its id; the evidence for each (the fix report's, or yours); the requirements inputs the finding was graded against — the plan pointer in the task loop, the spec at its pinned revision and the plan in the branch review, the lane note at its pinned revision on the very-small lane; where the spec's preamble (on the lane, the note's) carries an `Umbrella:` line, the umbrellas up the chain, by path — this feature's own entry and their Constraints & invariants, [LOAD-BEARING] marks and firm decisions binding, and a change to them within the range graded, as the Deviations paragraph of § The Task Loop states; and per finding, the range of the review that raised it — in the task loop, with the amendment commits inside it (§ Plan changes mid-execution). Once `git cat-file -t` prints `commit` for each end and `git merge-base --is-ancestor` confirms the range's base an ancestor of its head, the seat has git write each range's commit list, stat summary and `-U10` diff into files in its scratch subdirectory (its report's path less `.md`, in the workspace's `scratch/` directory: `.crucible/<feature-slug>/scratch/…` from the worktree root) with `--output`, and reads them there; an end that is not a commit, a base that is not an ancestor of the head, or a failing git command, is reported, never ruled on as an empty diff. Its mandate: for each finding, UPHELD or DISMISSED with a ruling, marking any ruling that touches binding content — what the Deviations paragraph of § The Task Loop names, an umbrella's included; it reads only in the worktree and writes only its report file and its scratch subdirectory. The tree check applies. Its report file:

- task loop: `sdd/reports/task-<N>-adjudication-<b>.md`, where `<b>` numbers the task's dispute batches; `sdd/reports/task-<N>-x<X>-adjudication-<b>.md` in re-run `<X>` after revert-and-replan;
- branch review: `sdd/branch-review/adjudication-<b>.md`, `<b>` numbering the branch review's batches;
- a replacement seat adds `-r<R>` before `.md`.

**Outcomes.** Write each to `## Adjudication rulings` — the finding, UPHELD or DISMISSED, the ruling, the report path — so a resumed controller rebuilds the open set from the ledger. An upheld finding re-enters the loop and cannot be disputed again; one upheld at the task-loop cap goes to the breaker. A dismissed finding is closed by its ruling. A ruling the adjudicator marks as touching binding content passes `skills/redteaming/references/flip-paths.md` § The containment test before you act on it — on the very-small lane, one changing the note's binding parts is the operator's, as its reference states: a contained one you record as your ruling, as that section states; any other goes to the operator as a decision ask: record it as `pending operator`, and the finding stays open until the answer. Record an operator's answer to any decision ask in this section beside the ruling it settles; it also enters the brainstorm decision record (`skills/redteaming/references/formats.md` § Feature workspace root and layout). Adjudication adds no wave. Every dismissed or parked BLOCKER/MAJOR reaches the operator with its ruling in the close readout (§ Finish).

### Shared-tree rules

- **No commits while a seat works.** While a dispatched seat works in the worktree, commit nothing there: the index is shared, so a bare commit sweeps in whatever it staged. Queue the commit until the seat returns.
- **The tree check, every review seat** — task reviewer, re-reviewer, adjudicator, branch reviewer. Start it with no tracked and no staged change; untracked files present at the start are tolerated. Record `git rev-parse HEAD` and `git status --porcelain --untracked-files=all` before the seat and again when it returns. A moved HEAD, any tracked or staged change, or any untracked path that appeared or disappeared voids the review: re-run it on a clean tree before acting on it. An edit inside a file already untracked at the start is invisible to the check — an accepted residual. Seats' `scratch/` lives in the gitignored workspace and never shows.
- **Replacing a seat is gated** — this is where two agents quietly end up writing the same tree. Start a replacement for a seat that already holds the work only when the **host confirms** the prior owner is terminal or absent, or that it acknowledged an interrupt. That confirmation revokes the prior owner's write admission; your inference from silence does not.
  - **Ambiguous liveness is BLOCKED.** Append a BLOCKED line naming the seat — `Task <N>: BLOCKED — ambiguous seat liveness` in the task loop — and escalate to the operator. Never dispatch a replacement to find out: that *is* the failure.
  - **A sanctioned replacement writes to a fresh report path** — its card's path with `-r<R>` before `.md` — never the revoked seat's file, which stays as the record. Give it the requirements, the prior report path to read, and the open findings.

### Revert-and-replan

**Drift discovered after the fact** — work already off-plan without a logged decision, found by the task review's deviation audit, by you, or by a branch-review pass in a completed task — is never patched forward: **revert to the last good commit and replan the task**, task-scoped, with an audit of the tasks that depend on it. **Materiality bound:** this applies to undisclosed deviations from *binding* content or with cross-task blast radius; undisclosed advisory-level choices (implementers do not log every micro-choice) and *disclosed-but-unjustified* Decision Log entries enter the fix loop instead.

- Append `Task <N>: reverted — <reason>; replanned as attempt <X>` (`<X>` from 2). It supersedes the task's `complete` line, so a resumed controller re-runs the task.
- The replanned task runs the task loop from step 1, its report paths taking `-x<X>` after `task-<N>` (`sdd/reports/task-<N>-x<X>-report.md`, and likewise for its review, re-reviews, adjudications and snapshot blessings). Replanning that changes plan text follows § Plan changes mid-execution.
- Handed one by the branch review, return the branch to `crucible:requesting-code-review` once the replanned task completes; it resumes with a full-scope pass.

## Inline mode

You may implement a task directly in the controller session — typically a small mechanical task where a dispatch costs more than it protects. Review applies **unchanged**: write your report at the same `sdd/` path, and dispatch the same reviewer with the same plan pointer, four verdicts and gates. **Any loop-entering finding converts the task to standard dispatch** — at any severity — and a fresh implementer owns the fixes: controller fixes that skip review are the case this rule exists for. A finding you contest on your inline diff goes to the adjudicator (§ Disputes and adjudication).

## Plan changes mid-execution

Executing defective or superseded plan text produces reviewable-but-wrong work, so such text found mid-execution — a BLOCKED escalation of a defective plan, replanning that changes plan text, an adjudication or a ruling of yours that patches the plan — takes a flip path, as do binding content a finding shows wrong (what the Deviations paragraph of § The Task Loop names, or binding-by-construction contract content) and a supersede called for, an unfold included; a scoped amendment is yours to confirm where § The containment test of the reference named below finds the change contained. The reference named below also governs a feature found to need splitting and, where the spec's preamble carries an `Umbrella:` line, a binding change its umbrella needs or one landed on the base that the feature has not taken in, checked for at each task boundary (§ The Task Loop, step 1) and before each branch-review pass and wave (`crucible:requesting-code-review` § The branch-review loop). **Before acting on any of them, read `skills/redteaming/references/flip-paths.md` in full; it binds as if written here**, and re-read it after compaction: a flip in flight shows in the ledger through its recorded decision ask or ruling.

## Whole-Branch Review

After the last task completes, run `crucible:requesting-code-review`: it owns the branch-review loop. Hand it the ledger's deferred minors — the plan's routed items still open included, since that sweep is the last link of their closure chain — and the adjudication rulings from execution: the execution-phase visibility surface, where a roll-up nobody reads would be a silent discard. Its disputes follow § Disputes and adjudication, its seats § Shared-tree rules, and drift it finds in a completed task § Revert-and-replan. When it ends, go to § Finish.

## The very-small lane

The third route, alongside the standard route and the folded lane: a small change executed from a lane note, with no spec campaign, no plan and no per-task review, entered only on the operator's confirmation at brainstorming, recorded in the brainstorm decision record. **On entering the lane, read `skills/subagent-driven-development/references/very-small-lane.md` in full, and re-read it after compaction; it binds as if written here**, and where it says so it supersedes this skill's rules for the lane.

## Finish

The order is binding. After any loop activity, restart at step 1, so new records — rulings included — are checked and reach the close readout.

1. **Record checks:** inspect the feature workspace against the ledger — the campaign records where their phases ran (round records, readouts, fix lists, the digest); the ledger's sections; under `sdd/reports/`, per task, `task-<N>-report.md`, `task-<N>-review.md`, each wave's `task-<N>-re-review-w<W>.md`, each dispute batch's `task-<N>-adjudication-<b>.md` and each snapshot blessing's `task-<N>-snapshot-<k>.md`, with their `-x<X>` and `-r<R>` forms, and `sdd/reports/lane-report.md` where the lane dispatched an implementer; under `sdd/branch-review/`, each `pass-<k>.md`, `wave-<n>-fix.md`, `wave-<n>-re-review.md` and `adjudication-<b>.md`. List every gap explicitly; never paper over one.
2. **The umbrella mark:** where the spec, folded document or lane note carries an `Umbrella:` line, mark this feature's entry in that umbrella `landed`, in the form `skills/brainstorming/references/umbrellas.md` § Marks states, and commit it on this branch, so the suite runs on the tree that lands. A feature with no line marks too where an umbrella on the base branch holds an unmarked entry opening with its slug (`git grep -n "<feature-slug>" <base-branch> -- "*/umbrella.md"`) and its feature folder was born on a tree without that umbrella — `git cat-file -e <commit>:<umbrella-path>` fails for its folder's first commit, the last line of `git log --diff-filter=A --format=%h -- <feature-folder>`: it was in flight when that umbrella was written. A feature born on a tree that held the umbrella is not that entry's child. Where its tree lacks that umbrella, it merges the base branch in first, never rebasing. A feature no umbrella names writes no mark; an entry already marked needs nothing.
3. **The suite:** run the full suite, or the project's declared merge gate, on HEAD. Do not classify a red run: it is a BLOCKER finding against the branch, handed to `crucible:requesting-code-review`'s loop and counted against its cap, the wave's fix base being the HEAD the suite ran on. That a failure is not the branch's — it fails on the merge base too, or is environmental — is a dispute like any other (§ Disputes and adjudication), which you may raise before the wave opens. A failure the adjudicator dismisses is recorded with its ruling and not raised again while it fails the same way; `crucible:finishing-a-development-branch` then presents the red run to the operator.
4. **Close readout** to the operator — a message, not a file: dismissed or parked BLOCKER/MAJOR findings with their rulings; every ruling you made yourself, with its reason — pre-flight and later plan conflicts, the plan patches they led to, the contained amendments, the plan phase's included, the breaker's; the minors left for the operator, the lane's departures on the lane, the record-check gaps, and the suite result. It assembles from `## Adjudication rulings`, `## Deferred minors`, the `Task <N>: parked` lines and the lane section, following the ledger's predecessor link where one exists. It is the only hand-over of the work left open: crucible files it nowhere durable, and filing it — a backlog item, a PR body — is the operator's call or the host repo's convention.
5. **Workspace deletion:** delete `.crucible/<feature-slug>/` and nothing else, and report to the operator anything you could not delete.
6. Then use `crucible:finishing-a-development-branch`.

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Close enough on spec compliance" | A failed intent, scope or deviation verdict enters the loop at any severity. Fix it, dispute it with evidence, or reach the cap — the only exits. |
| "I'll fix it myself, dispatching is overhead" | Controller fixes pollute your context and skip review. Resume the implementer — or use inline mode, where any loop-entering finding converts back to dispatch. |
| "This finding is obviously wrong, I'll drop it" | Dispute it with evidence: the adjudicator rules — you, only on a plan conflict in a diff you did not write — and the ruling reaches the ledger and the close readout. Silent drops are forbidden. |
| "One more wave will converge" | Past the cap, waves don't converge — the failure is structural. The breaker exists for this. |
| "The implementer deviated but the result looks fine" | Undisclosed drift from binding content reverts — never patch forward. Disclosed-but-unjustified goes to the fix loop. |
| "The fix was small, skip the re-review" | Unreviewed fixes are how regressions land. Every wave that changes code ends with a scoped re-review. |
| "Ledger bookkeeping is overhead" | The ledger is what survives compaction — and what the close readout is assembled from. |
