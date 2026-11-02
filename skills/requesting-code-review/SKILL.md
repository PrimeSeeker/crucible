---
name: requesting-code-review
description: Use when a branch's tasks are complete or before merging.
---

# Requesting Code Review

Dispatch the whole-branch reviewer: a fresh seat handed precisely crafted context, never your session's history. It applies the review principles — evidence grounding, staked severity, full-scope reads, blind fix verification — without the panel apparatus. After an SDD run this skill runs § The branch-review loop, the one statement of that loop; on a branch with no SDD run, § Standalone mode.

**Dispatch reference:** read
`skills/using-crucible/references/<runtime>-dispatch.md` from the plugin
root when this skill starts, and again after compaction — it holds your
adapter's instrument-dispatch, resume and effort operations.

## When to Request Review

- **Mandatory:** when `crucible:subagent-driven-development` hands over a branch whose tasks are all complete, and before merging any branch.
- **Optional, in standalone mode:** when stuck, before refactoring, after fixing a complex bug.

## Dispatch the branch reviewer

**The range** is MERGE_BASE..HEAD, MERGE_BASE = `git merge-base main HEAD` or the recorded branch point — never `HEAD~1`, which silently drops all but the last commit. Once the base has been merged into the branch, MERGE_BASE is `git merge-base` alone: from the recorded branch point, the range would carry every change that merge brought in. The reviewer builds the diff itself, so it never enters your context.

**Dispatch** instrument `branch-reviewer` on **the default role** — this seat's floor, never lowered to save cost, or the alternate role where one of its triggers selects this seat — with its filled slot card, [code-reviewer.slots.md](code-reviewer.slots.md), through your adapter's instrument-dispatch operation (the template is [code-reviewer.md](code-reviewer.md)). Every seat this skill starts carries the seven items of `skills/subagent-driven-development/references/dispatch-composition.md`, whose § Models and effort holds the rules every dispatch shares.

Its inputs: the range; the plan as the requirements; the spec at its pinned revision, the pointer the plan's header carries (on the very-small lane, the lane note at its pinned revision is both); `<workspace>/request.md`, for the goal check; where its preamble carries an `Umbrella:` line, the umbrellas up the chain, by path — this feature's own entry in that umbrella and the umbrellas' Constraints & invariants and firm decisions (those recorded as the operator's firm preference) bind too, and within the range a change to those Constraints or firm decisions is a finding, and so is a change to the entry other than the feature's own mark or a clarification its spec states that changes nothing another entry waits on, a binding change taken in from the base by a merge aside; the ledger's deferred minors — both kinds, the minors parked during execution and the spec and plan reviews' `deferred-minor` entries (source `Spec` or `Plan`), triaged under one rubric, since this triage is the last stage that reads them and an item omitted here is closed nowhere — and its leads, which the reviewer rules on instead, never its `## Questions`; the adjudication rulings, execution's and the branch review's own so far; and, in `[FIRST_REVIEW_TASKS]`, each task whose latest `Task <N>` line under `## Progress` is `Task <N>: complete (commits <base7>..<head7>, branch review only)`, the branch reviewer its first review: that range; its report, `sdd/reports/task-<N>-report.md` or its `-x<X>` form; the brainstorm decision record's path where its plan section names it; and the amendment commits the range holds (`skills/redteaming/references/flip-paths.md`, step 3), or "no amendment commits". That is the execution phase's visibility surface: a roll-up nobody reads is a silent discard. Set the card's `lane` selector `very-small` on the very-small lane, `off` elsewhere.

Full-scope pass `<k>` writes `sdd/branch-review/pass-<k>.md`; confirm each seat's report file as `crucible:subagent-driven-development § Runtime identity in every dispatch` says. `crucible:subagent-driven-development § Shared-tree rules` binds every seat this review dispatches: the no-commit rule all of them, the status check every review seat among them, the replacement line any replacement.

## The branch-review loop

Severity vocabulary: **BLOCKER / MAJOR / MINOR.** Only a BLOCKER or MAJOR opens a wave, apart from the cleanup wave and the waves a ruling or requested work opens (below); a premise finding, a question or a lead never opens one by itself. A lead the reviewer CONFIRMED as an intent or scope gap counts as a BLOCKER or MAJOR in this loop, whatever its staked severity, as the task loop wires a failed verdict.

Where the spec's preamble (on the lane, the note's) carries an `Umbrella:` line, take the receiving step of `skills/redteaming/references/flip-paths.md` § Under an umbrella: binding changes and late splits before each full-scope pass builds its range and before each fix wave records FIX_BASE, so a binding change it takes in falls outside the range the pass or wave reviews.

1. **A full-scope pass** reads the whole branch. One that leaves no open or new BLOCKER or MAJOR ends the review. A premise finding is a decision ask, not an open BLOCKER or MAJOR (`skills/redteaming/references/flip-paths.md` § Premise findings): a pass that leaves only premise findings open ends it too. A pass that leaves a lead it was handed unruled is missing a verdict: treat it as `crucible:subagent-driven-development § The Task Loop` treats any review missing one.
2. **A fix wave** — one fix dispatch plus its scoped re-review — takes what a pass left open. Record FIX_BASE (`git rev-parse HEAD`) as it opens.
   - **The fix dispatch:** one fresh instrument `implementer` with the complete findings list — never per-finding fixers, never you off the lane (below) — its card, `skills/subagent-driven-development/implementer-prompt.slots.md`, filled by its branch-review fix-wave rules: `[REQUIREMENTS]` the spec at its pinned revision and the plan, the findings verbatim in `[CONTEXT]`, `[REPORT_FILE]` `sdd/branch-review/wave-<n>-fix.md`. Its model is the implementer row of `crucible:subagent-driven-development § Models`. It answers each finding fixed or NOT CONFIRMED, and each labelled change applied or declined (Changes that ride a wave, below).
   - **Findings answered fixed**, and changes applied, get the scoped re-review: instrument `re-reviewer` with its card, `skills/subagent-driven-development/re-review-prompt.slots.md`: `[REQUIREMENTS]` as above (the lane note on the lane), `[FIX_BASE_SHA]` FIX_BASE, `[FINDINGS]` those findings and changes only, `[FIX_REPORT]` `sdd/branch-review/wave-<n>-fix.md`, `[REPORT_FILE]` `sdd/branch-review/wave-<n>-re-review.md`. New BLOCKER or MAJOR breakage joins the open findings; out-of-scope observations go to the ledger as deferred minors. It also rules on each concern the fix report raises: a re-review that leaves one unruled is missing a verdict, and you treat it as `crucible:subagent-driven-development § The Task Loop` treats any review missing one.
   - **Findings answered NOT CONFIRMED** are ruled on under Disputes, below. A wave that only disputes has no re-review, since nothing changed, and is still a wave; its fix report's concerns become leads for the next full-scope pass, each a `## Deferred minors` line `Branch wave <n>: lead (concern): <one-liner>`.
   - Once the wave's re-review, if any, and the rulings on its disputes are in, append its ledger line — off the lane, under `## Progress`: `Branch wave <n>/3 (<X> fixed, <Z> disputed — <one-liners>; commits <a7>..<b7> or none)`; on the lane, the lane ledger's `Wave <n>:` line instead. After compaction, read the cap from these lines.
3. **Then a full-scope pass again.** A wave that leaves no BLOCKER or MAJOR open — each fixed and re-reviewed, or dismissed by a ruling — leaves one step, a full-scope pass: scoped re-reviews verify waves, only a full-scope read clears the branch. One that raises a new BLOCKER or MAJOR opens the next wave. The pass is skipped when nothing changed since the last full-scope pass — it left no BLOCKER or MAJOR open, or a ruling dismissed every one it raised. The full-scope pass that ends the review is **the branch review's terminal pass**: a `branch-reviewer` dispatch, never the campaign's terminal-pass instrument; earlier full-scope passes are not terminal.
4. **Cap: 3 waves** — the loop's termination guarantee. A ruling adds no wave. A BLOCKER or MAJOR that would need a fourth wave is BLOCKED: escalate it to the operator as a decision ask with a recommendation, which never requires reading plan, code or a diff and may quote the few lines it turns on; the operator's answer also enters the brainstorm decision record, and one that changes what was asked enters `<workspace>/request.md` too (`skills/redteaming/references/formats.md` § Feature workspace root and layout).

**Minors.** A minor, such a confirmed lead aside, rides a wave something else opened — trivial minors and the reviewer's FIX-IN-WAVE items join that fix dispatch's findings list — and never opens one by itself. Every minor that rode no wave becomes a ledger line under `## Deferred minors`, listed for the operator in the close readout (`crucible:subagent-driven-development § Finish`): no ruling per minor, and never chased by you.

**The cleanup wave.** Once the review has ended with no BLOCKER or MAJOR open and a wave remains under the cap, you may, before returning to Finish, open one cleanup wave of the minors, and the leads the reviewer ruled CONFIRMED or RECOMMENDED, that you judge worth fixing; improvements alone may make one. It runs as any wave — counted against the cap, its scoped re-review, then a full-scope pass — and its ledger line reads `Branch wave <n>/3 (cleanup, <X> fixed, …)` (on the lane, the lane ledger's cleanup form, `crucible:subagent-driven-development § The very-small lane`), so a resumed controller sees it spent. One per branch: minors the cleanup wave or a later pass raises open no other wave; a BLOCKER or MAJOR opens a normal one, and one raised at the cap takes step 4's escalation. Standalone mode has no cleanup wave.

**Changes that ride a wave** — an improvement you adopt, an operator's ruling, work the operator asked for — enter its findings list as `Change (<kind>): <the change> — apply it, or decline it with a reason`, `<kind>` being `improvement`, `ruling` or `requested`. With no defect to confirm, none is answered NOT CONFIRMED or disputed; one applied goes to the re-review, which checks it landed and broke nothing. Write each one declined under `## Questions` as `Branch wave <n>: <the change> — declined: <its reason>`: a declined ruling or requested change goes back to the operator in the next close readout; a declined improvement is work left open.

**Rulings and requested work.** A ruling that `skills/redteaming/references/flip-paths.md` § Premise findings sends to a branch-review wave opens the next wave, as does work the operator's close-readout answer asks for that the spec and plan already require or that the readout listed as a minor, improvement or lead; other work asked for is new scope, a feature of its own. Where the cap is spent, the operator's answer is the escalation's answer and may open the wave.

**Premise findings**, a pass's or a fix report's, go where `skills/redteaming/references/flip-paths.md` § Premise findings sends them.

**Questions and leads.** Write each `Questions` item of a pass under the ledger's `## Questions` as `Branch review pass <k>: <item> — <your disposition>` (a fix report's as `Branch wave <n>: …`), the disposition carrying it to the operator or ruling on it; the close readout lists them, and no seat reads them. An improvement you adopt — a question's, or a lead the reviewer ruled RECOMMENDED — is a lightly held change you name in the close readout, and rides the next fix wave as a labelled change (above) and opens none but the cleanup wave; where no wave follows, it goes to the operator in the close readout, as does a RECOMMENDED lead you do not adopt, its verdict added to its ledger line.

**Disputes** follow `crucible:subagent-driven-development § Disputes and adjudication`, which says when you rule and when the adjudicator does, with its branch-review inputs and report path. Raise a finding you judge wrong before the next wave opens or with a wave's disputes. You never park a BLOCKER or MAJOR on your own ruling, and never drop one: each dismissed one reaches the operator with its ruling in the close readout.

**Drift**, off the lane — on it, drift from the note is a wave finding. Undisclosed drift from binding content that a pass finds in a completed task (flagged DRIFT) goes to the operator as `crucible:subagent-driven-development § Drift found after the fact` states: a repair rides a fix wave, counted against the cap; after a revert, once the re-run tasks complete, the review resumes with a full-scope pass, which re-grades the rest of that pass's findings.

**Finish's red suite.** A red run `crucible:subagent-driven-development § Finish` hands over is a BLOCKER finding against the branch: it opens the next wave, counted against the same cap, its FIX_BASE being the HEAD the suite ran on. That the failure is not the branch's — it fails on the merge base too, or is environmental — is a dispute you may raise before the wave opens.

**Fixes are never yours** off the very-small lane: your context stays for coordination, and controller fixes skip review. On the lane you apply each wave's fixes inline and write `wave-<n>-fix.md` yourself; the lane's inputs, its lane-fit statement and its other differences are in `crucible:subagent-driven-development § The very-small lane`, and the rest of this loop runs there as stated here, route conditions included.

When the review ends, return to `crucible:subagent-driven-development § Finish`.

## Standalone mode

For a branch with no SDD run: no ledger, no workspace, no loop.

1. Dispatch the branch reviewer as above, its card filled with `[SPEC_POINTER]` the spec at its pinned revision where the branch has one and "none" otherwise, `[REQUEST_FILE]`, `[LEDGER_MINORS]`, `[RULINGS]`, `[FIRST_REVIEW_TASKS]` and `[REPORT_FILE]` "none", and `lane` `off`. It returns its report as its final message, builds its diff and runs code under the host's temporary directory, and — with no Decision Log to check against — reports deviations as ordinary findings, not DRIFT. With no ledger, that report is the record of everything it raises, its questions included.
2. Handle the findings yourself, under `crucible:receiving-review`; you are not an SDD controller. Fix the BLOCKER and MAJOR findings you confirm, and after substantial fixes run this mode again. A premise finding goes to the operator as a decision ask with your recommendation, never to a fix. There is no wave loop and no cap: the operator decides what remains open.

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "I'll just review the diff myself instead of dispatching a reviewer" | You're the coordinator — reviewing the diff inline burns the context window you need to keep driving the work. Dispatch a reviewer: the diff and the evaluation live in its context, and only the findings come back to you. |
| "The reviewer needs my whole session history to understand the change" | Hand it precisely crafted context, never your session's history. That keeps the reviewer on the work product, not your thought process. |
| "The ledger minors are noise, skip them" | They reached the dispatch deliberately — a deferred minor nobody re-reads is a silent discard. The reviewer triages them. |
| "The reviewer can read the spec campaign's records for context" | It cannot: the campaign's exhaust is out of scope for every fresh seat. The spec at its pinned revision is the shared input; the argument that produced it is not. |

## Red Flags

**Never:**
- Skip review because "it's simple"
- Ignore a BLOCKER, or merge with an open BLOCKER/MAJOR — an open premise finding is a decision ask, not one (`skills/redteaming/references/flip-paths.md` § Premise findings)
- Fix findings yourself in the loop, off the very-small lane
- Dispatch the branch reviewer below the default role to save cost
