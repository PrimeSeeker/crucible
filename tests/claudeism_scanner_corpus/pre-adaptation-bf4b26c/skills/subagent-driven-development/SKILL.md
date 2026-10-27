---
name: subagent-driven-development
description: Use when executing an implementation plan - fresh implementer and reviewer subagents per task, adjudicated review loops, verification gates, and a capped whole-branch review
---

# Subagent-Driven Development

Execute a plan by dispatching a fresh implementer subagent per task, a single fresh-context reviewer after each task, and an iterative, capped whole-branch review at the end.

**Why subagents:** You delegate tasks to agents with isolated context. By precisely crafting their instructions and context, you ensure they stay focused and succeed. They never inherit your session's history — you construct exactly what they need, which also preserves your own context for coordination.

**Core principle:** Fresh implementer per task + adversarial task review + verification gates + capped whole-branch review = high quality without a human in the loop.

**Narration:** between tool calls, narrate at most one short line — the ledger and the tool results carry the record.

**Continuous execution:** Do not pause to check in with the operator between tasks. The only reasons to stop are: a BLOCKED status you cannot resolve, a stop-and-ask trigger (below), a decision ask that genuinely needs the operator, or all tasks complete. "Should I continue?" prompts waste their time — they asked you to execute the plan, so execute it. Decision asks, when they do fire, are analyst-language with a recommendation — never plan or code text to read.

## Setup

Work happens in an isolated workspace: use `crucible:using-git-worktrees` to create one or verify the existing one. Never start implementation on a main/master branch without the operator's explicit consent.

**Feature workspace.** SDD state lives in the `sdd/` subtree of the feature workspace — `<repo>/.crucible/<feature-slug>/` per `skills/redteaming/references/formats.md`, provisioned at brainstorm exit (`crucible:brainstorming`). At skill start, ensure it exists — provision is idempotent, so call it rather than assume:

```
python <plugin-root>/skills/redteaming/scripts/workspace.py provision <feature-slug>
```

The `sdd/` subtree holds everything for THIS plan's execution: `ledger.md`, `briefs/`, `reports/`, `review-packages/`, `branch-review/`. Another feature's workspace is never yours to read or write — with one sanctioned exception: following a declared predecessor link (below).

**The ledger** (`sdd/ledger.md`). Conversation memory does not survive compaction. Controllers that lost their place have re-dispatched entire completed task sequences — the single most expensive failure observed. Track progress in the ledger, not only in todos.

- First line is the ledger's identity: `# SDD ledger — plan: <plan file path>`.
- Structure the file so the feature summary assembles from it (formats.md § Committed feature summary format): a `## Progress` section for the running lines below, then `## Adjudication rulings`, `## Decision Log digests` (per task: what / why / blast radius, compacted, plus BLOCKED escalations), and `## Deferred minors and gate lines`.
- **Resume rule:** if the first line names your plan file, tasks with a `Task <N>: complete` line are DONE — do not re-dispatch them; resume at the first task without one. A task whose last line is a fix round is mid-loop: resume the loop at the next round.
- **Predecessor links (supersede identity):** when a plan is superseded mid-flight, the successor ledger's **first line names the successor plan** and its **second line links the predecessor ledger** (move the predecessor aside, e.g. `sdd/ledger-superseded.md`, and link that path); the successor plan's header records which completed tasks carry over vs are invalidated. On resume, follow predecessor links **before declaring any task not-done** — this is the sanctioned exception to workspace isolation. If the predecessor records are gone, recover from the committed feature summary and `git log`.
- A ledger whose first line names a plan that is neither yours nor a declared predecessor is another run's progress: leave it in place and escalate rather than overwrite.
- The ledger is your recovery map: the commits it names exist in git even when your context no longer remembers creating them. After compaction, trust the ledger and `git log` over your own recollection. `git clean -fdx` destroys the workspace (gitignored scratch); recover from the committed feature summary + `git log`.

Read the plan once, note its Global Constraints (the complete [LOAD-BEARING] list and the Constraints & invariants content — every dispatch carries them), and create a todo per task.

**Pre-flight plan-conflict scan.** Before dispatching Task 1, scan the plan once for tasks that contradict each other or the Global Constraints, and for anything the plan explicitly mandates that the review rubric treats as a defect. These findings are **controller authority** (see Adjudication below): adjudicate each one yourself, log the ruling in the ledger, and proceed — escalate to the operator only a conflict that is a design judgment or touches a [LOAD-BEARING] decision, as an analyst-language decision ask with a recommendation. The review loop remains the net for conflicts that only emerge from implementation.

## Models

The floor replaces cost-tiering: **Opus is the default; simpler tasks may drop to Sonnet-class (Codex-side: Terra); never lower** — no Haiku/Luna-class dispatches. Plans are written for strong models; writing plan content down to weak-model needs is the failure this design exists to remove.

- **Reviewers:** mid-tier or better, always.
- **Branch reviewer:** Opus.
- **Fix ladder rounds 4–5:** a tier bump where one exists (Sonnet → Opus); fresh eyes at the same tier once at the Opus ceiling (see the fix loop). Opus is the escalation ceiling — Fable is never an automatic escalation.

**Fable (Mythos-class) is an operator-authorized exception, never a default.** Its two sanctioned uses: the whole-branch review of a branch the operator has flagged as a major feature (once, at that terminal review), and the occasional spec-redteam seat whose findings turn on large-scale architectural judgment (see `crucible:redteaming`). Anything else on Fable is unauthorized spend — ask first.

Always specify the model explicitly when dispatching a subagent — an omitted model silently inherits the session's, and sessions commonly run on Fable, so omission is an accidental Fable dispatch.

## The Task Loop

Everything you paste into a dispatch prompt — and everything a subagent prints back — stays resident in your context for the rest of the session. Hand artifacts over as files.

### 1. Dispatch the implementer

Record BASE (`git rev-parse HEAD`) before dispatching — the review package and fix-round diffs need it.

Extract the brief so it stays the **single source of requirements**:

```
bash <plugin-root>/skills/subagent-driven-development/scripts/task-brief <feature-slug> PLAN_FILE N
```

It writes `sdd/briefs/task-<N>-brief.md` and prints the path. The dispatch contains:

1. one line on where this task fits in the project;
2. the brief path, introduced as "read this first — it is your requirements, with the exact values to use verbatim";
3. **interfaces and decisions from neighboring tasks** that the brief cannot know;
4. the **global-constraints block**: the plan header's complete [LOAD-BEARING] list and Constraints & invariants content, copied verbatim;
5. the **plan-reminder line**: one line restating THIS task's binding acceptance criteria and the Decision Log obligation (the measured cheap compliance lever);
6. the report-file path (`sdd/reports/task-<N>-report.md`) and report contract: full report to the file — including the Decision Log and test evidence — return only status, commits, a one-line test summary, and concerns;
7. a pointer to any ledger entry parked in the area this task touches.

Exact values (numbers, magic strings, signatures) appear only in the brief. Never make a subagent read the whole plan file, and never paste accumulated prior-task history. Record the implementer's agent identity — fix-loop rounds 1–3 resume it. Never dispatch multiple implementers in parallel (conflicts).

Template: [implementer-prompt.md](implementer-prompt.md) — it carries the implementer-side contract: test-first as the default (exceptions logged in the Decision Log), evidence-before-done (run the covering tests, show output in the report), the deviation license, the model floor, and the protected-checkout conduct rules.

### 2. Handle the report

Implementers report one of four statuses:

- **DONE:** generate the review package and dispatch the reviewer (step 3).
- **DONE_WITH_CONCERNS:** read the concerns first. Correctness or scope concerns get addressed before review; observations are noted and review proceeds.
- **NEEDS_CONTEXT:** provide the missing context and re-dispatch.
- **BLOCKED:** assess — a context problem gets context and a re-dispatch; a reasoning problem gets a more capable model; an oversized task gets split; a defective plan escalates (a possible amendment — see Plan changes below). Never ignore an escalation or force the same model to retry without changes.

**Deviation handling.** Implementers may deviate from advisory content and flip lightly-held positions when the codebase contradicts their assumptions — every deviation logged in the report's **Decision Log** (what, why, blast radius). Content carried in the brief's Constraints (including propagated [LOAD-BEARING] marks) is **binding: implementing it is the job; changing or contradicting it is BLOCKED**, never improvised. Stop-and-ask triggers: insufficient context, unresolved trade-off, conflicting findings, ambiguity above task authority. Plan ambiguity is never license.

**Drift discovered after the fact** — work already off-plan without a logged decision, whether you or the reviewer's deviation audit finds it: **revert to the last good commit and replan the task**. Never patch forward over undocumented drift. **Materiality bound:** revert-and-replan applies to undisclosed deviations from *binding* content or with cross-task blast radius; undisclosed advisory-level choices (implementers do not log every micro-choice) and *disclosed-but-unjustified* Decision Log entries enter the fix loop normally.

### 3. Review the task

One fresh-context reviewer per task. Never skip it, and never accept a report missing any verdict. Implementer self-review never replaces it.

Package the diff so it never enters your context:

```
bash <plugin-root>/skills/subagent-driven-development/scripts/review-package <feature-slug> BASE HEAD
```

Use the BASE you recorded before dispatching — never `HEAD~1`, which silently drops all but the last commit of a multi-commit task. Never dispatch a reviewer without a diff file.

**Reviewer inputs:** the brief, the report (including its Decision Log), the printed review-package path, and the same global-constraints block the implementer got — it is the reviewer's attention lens. Copy binding requirements verbatim; the template carries the process rules.

**Mandate:** the stance is **adversarial** — the framing is "attempt to reject this task": hunt intent gaps, scope creep, and hidden deviations; refute the implementer's "done" rather than confirm it. **The stance governs the search, not the conclusion: a clean verdict is a legitimate outcome and does not weaken the review** — a manufactured finding costs a fix round. Finding hygiene bounds the hunt: staked severity plus evidence; improvements and style are not findings. Severity vocabulary everywhere: **BLOCKER / MAJOR / MINOR**.

**Four verdicts, all required:**

- **intent** — every requirement implemented, against the plan's intent;
- **scope** — nothing outside the task changed; weakened or deleted tests are a scope finding;
- **deviation audit** — each Decision Log entry justified; undisclosed deviations are findings;
- **quality** — defects, not style. New-test adequacy is backed by the verification gates (step 4), not reviewer judgment alone.

The reviewer may also return **⚠️ cannot-verify items** — requirements living outside the diff. Resolve each one yourself before task completion (you hold the plan and cross-task context); a confirmed gap is a failed intent verdict.

**Loop wiring:** a failed intent, scope, or deviation-audit verdict enters the fix loop **regardless of the finding's severity label**; quality findings enter per severity — BLOCKER/MAJOR in, MINOR to the ledger.

Dispatch hygiene: no open-ended directives ("check all uses") without a concrete task-specific reason; don't ask the reviewer to re-run tests the implementer's report already evidences; never pre-judge findings ("do not flag…", "at most MINOR") — let the reviewer raise them and adjudicate in the loop.

Template: [task-reviewer-prompt.md](task-reviewer-prompt.md)

### 4. Verification gates

Every acceptance criterion in the task maps to an executable check or a stated why-not — confirm the report shows this.

- **Mutation testing (test adequacy):** a scoped-to-diff mutation run is **mandatory where the task's diff touches test files** — waiving it there requires a logged reason. Elsewhere it is discretionary. Either way, the ledger gets a **run-or-waive line** (`Task <N>: mutation run — <result>` or `Task <N>: mutation waived — <reason>`, under `## Deferred minors and gate lines`); a waive with no line is a process defect. Tooling is language-appropriate; where none exists for the diff's language (markdown/bash process code), the waive path with a logged reason is the expected route, not a defect.
- **Snapshot/golden blessing** (where behavior-preservation is the claim): **never autonomous.** A fresh blind agent — inputs: the old/new output pair and the behavior-preservation claim, nothing else — verdicts the change. If it judges the change intent-visible, it goes to the operator as an analyst-language decision ask (what changed and why it matters — never a raw diff).

### 5. The fix loop

The loop triggers on any failed intent/scope/deviation-audit verdict, any BLOCKER or MAJOR quality finding, or a cannot-verify item you confirmed as a real gap. Two routes leave before the loop:

- **MINOR findings** go to the ledger as they arrive (`Task <N>: minor (deferred): <one-liner>`, under `## Deferred minors and gate lines`); the whole-branch review triages them. They never enter the loop.
- **Plan-conflict findings** go to adjudication:

**Adjudication.** Findings that conflict with plan text — including plan-mandated findings and the pre-flight scan's — are **controller authority: adjudicate, log the ruling in the ledger's `## Adjudication rulings`; a silent discard is forbidden.** Two guards on that authority:

- **Visibility:** every rejected BLOCKER/MAJOR appears in the next readout with its ruling — a ruling is never the last anyone hears of a finding.
- **No self-adjudication:** findings on a diff you implemented yourself (inline mode) are exempt from your rulings and always enter the loop; if such a finding is still contested at the fix-loop cap, a **fresh adjudicator seat** (not you) rules on it, escalating to the operator only if its ruling touches a [LOAD-BEARING] decision.

This authority governs the plan-conflict class only — **ending a fix loop by adjudication remains cap-gated**: the breaker at the cap is the only adjudication exit from a live loop, and adjudicating earlier to end one is pre-judging with a different name. A finding that both fails a verdict *and* conflicts with plan text is **adjudicated first** (is the plan or the work wrong?); if the ruling upholds the plan, the verdict failure stands and enters the loop — the ruling never quietly absorbs the finding. Escalate to the operator only when the conflict is a design judgment or touches a [LOAD-BEARING] decision — analyst-language, with a recommendation.

**The ladder.** A fix round is one fix dispatch plus one scoped re-review. **Five rounds maximum per task** — the cap, with the breaker, is the loop's termination guarantee.

- **Rounds 1–3 — resume the original implementer** with the open findings verbatim. Its context is intact. If the harness cannot resume a live subagent, dispatch fresh with the brief path, report-file path, and findings — the report file is the persistent memory either way.
- **Rounds 4–5 — escalate:** a **tier bump where one exists** (a Sonnet-implemented task goes to Opus); **at the Opus ceiling, fresh eyes at the same tier** — a fresh implementer with the brief path, report-file path, open findings, and this framing: "A prior implementer attempted this task N times; you own it now. Read the report file for what was tried." A loop that survives three resumes usually means the implementer cannot see its own problem.

**Every round:** the implementer fixes, re-runs the tests covering the amended code, appends its fix report to the same report file, and returns the short contract. Confirm the fix report names the covering tests, the command, and the output before re-dispatching review. Then run the scoped re-review: `review-package <feature-slug> FIX_BASE HEAD` (FIX_BASE = the head the previous review saw) and dispatch [re-review-prompt.md](re-review-prompt.md) with the findings list, brief, report file, and diff path. The re-reviewer verdicts each finding ADDRESSED or NOT ADDRESSED and flags new breakage in the fix diff only; new BLOCKER/MAJOR breakage joins the open findings; out-of-scope observations go to the ledger as deferred minors. After each round, append: `Task <N>: fix round <R>/5 (<X> addressed, <Y> open — <one-liners>; commits <a7>..<b7>)`.

Never fix findings yourself in the controller session — your context stays clean for coordination, and controller fixes skip review (see Inline mode for the sanctioned path).

**The breaker.** When round 5's re-review still leaves findings open, stop dispatching and adjudicate each open finding — you hold the plan and cross-task context the reviewer lacks:

- **The reviewer is wrong, or the point is contestable:** park it — `Task <N>: parked — <finding> — ruling: <why the code stands>`. The branch review sees both sides.
- **Real, but nothing downstream builds on it:** park it the same way, with a ruling that says it's real and deferred.
- **Real and load-bearing** — a later task builds on it, or it reveals a plan defect: STOP. Append `Task <N>: BLOCKED — <reason>` and report to the operator, analyst-language with a recommendation: the finding, the plan text it collides with, and the fix history. Parking a structural failure lets every dependent task build on it.

Every adjudication is a ledger entry — a silent discard is forbidden. (Findings on inline-mode diffs are not yours to breaker-adjudicate: fresh adjudicator seat, above.)

### 6. Complete the task

When the review comes back clean — or every open finding is parked with a ruling at the cap — check the gate lines are in the ledger (mutation run-or-waive), then append the completion line:

- `Task <N>: complete (commits <base7>..<head7>, review clean)`
- `Task <N>: complete (commits <base7>..<head7>, <K> parked)` after a tripped breaker

Mark the todo complete and move on. Never move to the next task while open BLOCKER/MAJOR findings are neither fixed nor parked-with-ruling at the cap.

## Inline mode

You may implement a task directly in the controller session (typical: small mechanical tasks where a dispatch costs more than it protects). Review applies **unchanged**: author your own brief and report at the same `sdd/` paths so the reviewer's inputs exist, and dispatch the same reviewer with the same four verdicts and gates. Two hard rules:

- **Any loop-entering finding converts the task to standard dispatch** — not just BLOCKER/MAJOR; a failed verdict at any severity converts. A fresh implementer owns the fixes. Controller fixes that skip review are the prohibited case this rule exists for.
- Findings on your inline diff always enter the loop — never self-adjudicate them (Adjudication, above).

## Plan changes mid-execution

Executing a defective or superseded plan text produces reviewable-but-wrong work; these are the two sanctioned paths (both start as an operator decision ask with a recommendation):

**Scoped amendment** (default when blast radius is contained — controller judgment, logged): on confirmation the spec is amended in place with an amendment marker, the plan is patched, and then — binding procedure — **briefs for open or in-loop tasks are re-extracted** (`task-brief` again; completed tasks keep their briefs) **and their global-constraints blocks refreshed**: a reviewer never grades against a superseded brief. The same re-extraction rule applies to adjudication rulings that patch the plan. Work continues; no re-campaign.

**Supersede** (structural blast radius): execution halts; a successor spec and plan are derived (their own campaigns); the successor ledger carries the identity lines from Setup — first line the successor plan, second line the predecessor-ledger link — and the successor plan's header records which completed tasks carry over vs are invalidated.

## Whole-Branch Review

After all tasks: the branch review reuses the review principles — evidence grounding, staked severity, full-scope reads, blind fix verification — not the panel apparatus.

Package the whole branch: `review-package <feature-slug> MERGE_BASE HEAD` (MERGE_BASE = `git merge-base main HEAD` or the recorded branch point). Dispatch the branch reviewer on **Opus** (Fable only on an operator-flagged major feature — see Models), mandate per `skills/requesting-code-review/code-reviewer.md` (`crucible:requesting-code-review`). The dispatch includes the package path **plus the ledger's deferred minors and the adjudication rulings from execution** — the execution-phase visibility surface; a roll-up nobody reads is a silent discard.

**Iterative:** fix wave → scoped re-review, repeating as needed — fixes unmask problems and drift. Each wave is **ONE fix dispatch with the complete findings list, executed by a fresh implementer — never the controller** (per-finding fixers and controller fixes are both prohibited), followed by one scoped re-review of the wave range ([re-review-prompt.md](re-review-prompt.md)). Record wave findings lists, fix reports, and re-review verdicts under `sdd/branch-review/`.

**Stop rule = severity floor:** a pass with no **open or new** BLOCKER/MAJOR ends the review — and the **closing pass is full-scope**: scoped re-reviews verify waves; only a full-scope read can clear the branch.

**Cap [LOAD-BEARING]: 3 waves** — the caps are the loop's only termination guarantee. Open BLOCKER/MAJOR findings at the cap = BLOCKED, escalated to the operator as a decision ask.

**Precedence with deviation handling:** a wave finding of *undisclosed drift from binding content* in a completed task is not wave material — revert-and-replan governs it (task-scoped, with an audit of dependent tasks) — **but the pass that triggered it consumes a wave against the cap** (otherwise revert-replan cycles bypass the termination guarantee). The wave handles everything else.

**Minors:** never chase nontrivial minors on your own — trivial minors may ride a fix wave; nontrivial minors are parked with a ruling and surfaced in the readout.

## Finish

The order is binding — record checks, then summary commit, then deletion:

1. **Record checks:** inspect the feature workspace — round records, readouts, fix lists, Decision Logs, adjudication rulings, and the digest are present where their phases ran; gaps are listed explicitly, never papered over.
2. **Summary commit:** `python <plugin-root>/skills/redteaming/scripts/workspace.py summarize <feature-slug>` assembles the committed feature summary (`docs/crucible/<feature-slug>.md`) from the records — including the SDD ledger's rulings, Decision Log digests, and gate lines. Commit it.
3. **Workspace deletion:** `python <plugin-root>/skills/redteaming/scripts/workspace.py finish <feature-slug>` — it verifies the summary is committed, then deletes the workspace. An uncommitted summary is a refusal, not a warning.

Then use `crucible:finishing-a-development-branch`.

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Close enough on spec compliance" | A failed intent/scope/deviation verdict enters the loop at any severity. Fix, or hit the cap and adjudicate — the only exits. |
| "I'll fix it myself, dispatching is overhead" | Controller fixes pollute your context and skip review. Resume the implementer — or go inline-mode, where any loop-entering finding converts back to dispatch. |
| "This finding is obviously wrong, I'll drop it" | Plan-conflict findings you may adjudicate — with a ledger ruling, visible in the next readout. Everything else: silent discards are forbidden. |
| "One more round will converge" | Past the cap, rounds don't converge — the failure is structural. The breaker exists for this. |
| "The implementer deviated but the result looks fine" | Undisclosed drift from binding content reverts — never patch forward. Disclosed-but-unjustified goes to the fix loop. |
| "Skip the mutation line, the tests look thorough" | A waive with no ledger line is a process defect. Run or waive-with-reason — either way, a line. |
| "The fix was small, skip the re-review" | Unreviewed fixes are how regressions land. Every round ends with a scoped re-review. |
| "Ledger bookkeeping is overhead" | The ledger is what survives compaction — and what the feature summary is assembled from. |
