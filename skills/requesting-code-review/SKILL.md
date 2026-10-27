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

**The range** is MERGE_BASE..HEAD, MERGE_BASE = `git merge-base main HEAD` or the recorded branch point — never `HEAD~1`, which silently drops all but the last commit. The reviewer builds the diff itself, so it never enters your context.

**Dispatch** instrument `branch-reviewer` on **the default role** — this seat's floor, never lowered to save cost, or the alternate role where one of its triggers selects this seat — with its filled slot card, [code-reviewer.slots.md](code-reviewer.slots.md), through your adapter's instrument-dispatch operation (the template is [code-reviewer.md](code-reviewer.md)). Every seat this skill starts carries the seven items of `skills/subagent-driven-development/references/dispatch-composition.md`, whose § Models and effort holds the rules every dispatch shares.

Its inputs: the range; the plan as the requirements; the spec at its pinned revision, the pointer the plan's header carries (on the very-small lane, the lane note at its pinned revision is both); where its preamble carries an `Umbrella:` line, the umbrellas up the chain, by path — this feature's own entry in that umbrella and the umbrellas' Constraints & invariants and [LOAD-BEARING] marks bind too, and within the range a change to those Constraints or marks is a finding, and so is a change to the entry other than the feature's own mark or a clarification its spec states that changes nothing another entry waits on, a binding change taken in from the base by a merge aside; the ledger's deferred minors — both kinds, the minors parked during execution and the plan's routed items still open after their tasks' reviews, triaged under one rubric, since this sweep is the last link of their closure chain and an item omitted here is closed nowhere; and the adjudication rulings, execution's and the branch review's own so far. That is the execution phase's visibility surface: a roll-up nobody reads is a silent discard. Set the card's `lane` selector `very-small` on the very-small lane, `off` elsewhere.

Full-scope pass `<k>` writes `sdd/branch-review/pass-<k>.md`; confirm each seat's report file as `crucible:subagent-driven-development § Runtime identity in every dispatch` says. `crucible:subagent-driven-development § Shared-tree rules` binds every seat this review dispatches: the no-commit rule all of them, the tree check every review seat among them, the replacement gate any replacement.

## The branch-review loop

Severity vocabulary: **BLOCKER / MAJOR / MINOR.** Only a BLOCKER or MAJOR opens a wave.

1. **A full-scope pass** reads the whole branch. One that leaves no open or new BLOCKER or MAJOR ends the review.
2. **A fix wave** — one fix dispatch plus its scoped re-review — takes what a pass left open. Record FIX_BASE (`git rev-parse HEAD`) as it opens.
   - **The fix dispatch:** one fresh instrument `implementer` with the complete findings list — never per-finding fixers, never you off the lane (below) — its card, `skills/subagent-driven-development/implementer-prompt.slots.md`, filled by its branch-review fix-wave rules: `[REQUIREMENTS]` the spec at its pinned revision and the plan, the findings verbatim in `[CONTEXT]`, `[REPORT_FILE]` `sdd/branch-review/wave-<n>-fix.md`. Its model is the implementer row of `crucible:subagent-driven-development § Models`. It answers each finding fixed or NOT CONFIRMED.
   - **Findings answered fixed** get the scoped re-review: instrument `re-reviewer` with its card, `skills/subagent-driven-development/re-review-prompt.slots.md`: `[REQUIREMENTS]` as above (the lane note on the lane), `[FIX_BASE_SHA]` FIX_BASE, `[FINDINGS]` those findings only, `[FIX_REPORT]` `sdd/branch-review/wave-<n>-fix.md`, `[REPORT_FILE]` `sdd/branch-review/wave-<n>-re-review.md`. New BLOCKER or MAJOR breakage joins the open findings; out-of-scope observations go to the ledger as deferred minors.
   - **Findings answered NOT CONFIRMED** go to the adjudicator as one batch (Disputes, below). A wave that only disputes has no re-review, since nothing changed, and is still a wave.
   - Once the wave's re-review, if any, and its adjudication have returned, append its ledger line — off the lane, under `## Progress`: `Branch wave <n>/3 (<X> fixed, <Z> disputed — <one-liners>; commits <a7>..<b7> or none)`; on the lane, the lane ledger's `Wave <n>:` line instead. After compaction, read the cap from these lines.
3. **Then a full-scope pass again.** A wave that leaves no BLOCKER or MAJOR open — each fixed and re-reviewed, or dismissed by the adjudicator — leaves one step, a full-scope pass: scoped re-reviews verify waves, only a full-scope read clears the branch. One that raises a new BLOCKER or MAJOR opens the next wave. The pass is skipped when nothing changed since the last full-scope pass — it left no BLOCKER or MAJOR open, or the adjudicator dismissed every one it raised. The full-scope pass that ends the review is **the branch review's terminal pass**: a `branch-reviewer` dispatch, never the campaign's terminal-pass instrument; earlier full-scope passes are not terminal.
4. **Cap [LOAD-BEARING]: 3 waves** — the loop's termination guarantee. Adjudication adds no wave. A BLOCKER or MAJOR that would need a fourth wave is BLOCKED: escalate it to the operator as a decision ask with a recommendation, which never requires reading plan, code or a diff and may quote the few lines it turns on.

**Minors.** A minor rides a wave a BLOCKER or MAJOR opened — trivial minors and the reviewer's FIX-IN-WAVE items join that fix dispatch's findings list — and never opens one. Every minor that rode no wave becomes a ledger line under `## Deferred minors`, listed for the operator in the close readout (`crucible:subagent-driven-development § Finish`): no ruling per minor, and never chased by you.

**Disputes** follow `crucible:subagent-driven-development § Disputes and adjudication`, with the spec at its pinned revision and the plan (the lane note on the lane) as the adjudicator's requirements inputs and `sdd/branch-review/adjudication-<b>.md` as its report file. You rule only on a plan conflict in a diff you did not write; a finding you judge wrong goes to the adjudicator, raised before the next wave opens or with a wave's batch. You never park a BLOCKER or MAJOR on your own ruling, and never drop one: each dismissed one reaches the operator with its ruling in the close readout.

**Drift**, off the lane — on it, drift from the note is a wave finding. A pass that finds undisclosed drift from binding content in a completed task (flagged DRIFT) hands that task to `crucible:subagent-driven-development § Revert-and-replan`, and that pass consumes a wave against the cap — append its `Branch wave` line, `commits none` — or revert-and-replan cycles would bypass the termination guarantee. Once the replanned task completes, the review resumes with a full-scope pass, which re-grades the rest of that pass's findings.

**Finish's red suite.** A red run `crucible:subagent-driven-development § Finish` hands over is a BLOCKER finding against the branch: it opens the next wave, counted against the same cap, its FIX_BASE being the HEAD the suite ran on. That the failure is not the branch's — it fails on the merge base too, or is environmental — is a dispute you may raise before the wave opens.

**Fixes are never yours** off the very-small lane: your context stays for coordination, and controller fixes skip review. On the lane you apply each wave's fixes inline and write `wave-<n>-fix.md` yourself; the lane's inputs, its lane-fit statement and its other differences are in `crucible:subagent-driven-development § The very-small lane`, and the rest of this loop runs there as stated here, route conditions included.

When the review ends, return to `crucible:subagent-driven-development § Finish`.

## Standalone mode

For a branch with no SDD run: no ledger, no workspace, no loop.

1. Dispatch the branch reviewer as above, its card filled with `[SPEC_POINTER]` the spec at its pinned revision where the branch has one and "none" otherwise, `[LEDGER_MINORS]`, `[RULINGS]` and `[REPORT_FILE]` "none", and `lane` `off`. It returns its report as its final message, builds its diff and runs code under the host's temporary directory, and — with no Decision Log to check against — reports deviations as ordinary findings, not DRIFT.
2. Handle the findings yourself, under `crucible:receiving-review`; you are not an SDD controller. Fix the BLOCKER and MAJOR findings you confirm, and after substantial fixes run this mode again. There is no wave loop and no cap: the operator decides what remains open.

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "I'll just review the diff myself instead of dispatching a reviewer" | You're the coordinator — reviewing the diff inline burns the context window you need to keep driving the work. Dispatch a reviewer: the diff and the evaluation live in its context, and only the findings come back to you. |
| "The reviewer needs my whole session history to understand the change" | Hand it precisely crafted context, never your session's history. That keeps the reviewer on the work product, not your thought process. |
| "The ledger minors are noise, skip them" | They reached the dispatch deliberately — a deferred minor nobody re-reads is a silent discard. The reviewer triages them, the plan's routed items included. |
| "The reviewer can read the spec campaign's records for context" | It cannot: the campaign's exhaust is out of scope for every fresh seat. The spec at its pinned revision is the shared input; the argument that produced it is not. |

## Red Flags

**Never:**
- Skip review because "it's simple"
- Ignore a BLOCKER, or merge with an open BLOCKER/MAJOR
- Fix findings yourself in the loop, off the very-small lane
- Dispatch the branch reviewer below the default role to save cost
