---
name: requesting-code-review
description: Use when a branch's tasks are complete or before merging.
---

# Requesting Code Review

Dispatch a whole-branch reviewer: a fresh seat handed precisely crafted context, never your session's history. Mandatory when `crucible:subagent-driven-development` hands over a branch whose tasks are all complete, and before merging any branch; optional, in standalone mode, when stuck, before refactoring or after fixing a complex bug. After an SDD run, run § The branch-review loop; on a branch with no SDD run, § Standalone mode.

**When this skill starts and after compaction, read** `skills/subagent-driven-development/references/dispatch-composition.md` and your adapter's `skills/using-crucible/references/<runtime>-dispatch.md`; both bind as if written here.

## Dispatch the branch reviewer

The range is MERGE_BASE..HEAD, MERGE_BASE = `git merge-base main HEAD` or the recorded branch point; once the base has been merged into the branch, `git merge-base` alone: from the branch point, the range would carry every change that merge brought in. The reviewer builds the diff itself; it never enters your context.

Dispatch instrument `branch-reviewer` from its card, [code-reviewer.slots.md](code-reviewer.slots.md) (template [code-reviewer.md](code-reviewer.md)), on the role the card names. Every deferred minor and lead in the ledger reaches it: its triage is the last stage that reads them.

Confirm each seat's report file as the dispatch composition's item 5 states. Its § Shared-tree rules bind every seat this review dispatches, the status check every review seat (in standalone mode, its `tree-check.txt` in the host's temporary directory).

## The branch-review loop

Severities: BLOCKER / MAJOR / MINOR.

Where the spec's preamble (on the lane, the note's) carries an `Umbrella:` line, take the receiving step of `skills/brainstorming/references/umbrella-children.md` § Under an umbrella before each full-scope pass builds its range and before each fix wave records FIX_BASE, so a binding change it takes in falls outside the range reviewed.

1. **A full-scope pass** reads the whole branch. One that leaves no open or new BLOCKER or MAJOR ends the review; one that raises one opens a fix wave. A premise finding or an `unstated break` (below) is a decision ask, not an open BLOCKER or MAJOR (`skills/redteaming/references/premise-asks.md` § Premise findings): a pass leaving only those open ends the review too. The pass that ends it is **the branch review's terminal pass**, a `branch-reviewer` dispatch, never the campaign's terminal-pass instrument; earlier passes are not terminal.
2. **A fix wave**, one fix dispatch plus its scoped re-review, takes what a pass left open. Record FIX_BASE (`git rev-parse HEAD`) as it opens. Dispatch one fresh instrument `implementer` with the complete findings list, its card `skills/subagent-driven-development/implementer-prompt.slots.md` filled by its branch-review fix-wave rules: never per-finding fixers, and off the very-small lane never your own fixes. It answers each finding fixed or NOT CONFIRMED, and each labelled change applied or declined.
   - Findings answered fixed, and changes applied, get the scoped re-review: instrument `re-reviewer`, its card `skills/subagent-driven-development/re-review-prompt.slots.md` filled for a branch-review wave. New BLOCKER or MAJOR breakage joins the open findings; out-of-scope observations go to the ledger as deferred minors.
   - Findings answered NOT CONFIRMED go to Disputes (below). A wave that only disputes has no re-review but counts as a wave; its fix report's concerns become leads for the next full-scope pass.
   - Once the re-review, if any, and the rulings on its disputes are in, append the wave's ledger line (below). After compaction, read the cap from these lines.
3. **After a wave** that leaves no BLOCKER or MAJOR open, each fixed and re-reviewed or dismissed by ruling, run a full-scope pass: scoped re-reviews verify waves, only a full-scope read clears the branch. Skip it where nothing changed since the last full-scope pass: that pass left no BLOCKER or MAJOR open, or a ruling dismissed every one it raised. Skip it too where the wave took no BLOCKER or MAJOR, no merge came in since the last full-scope pass, and its re-review addressed every listed finding, raised no out-of-scope observation and reads None on its `Rule or behavior change` line, since the last full-scope read still stands; a missing line runs the pass. On this skip, append `full pass skipped` to the wave's ledger line.
4. **Cap: 3 waves**; a dispute's ruling adds no wave. A BLOCKER or MAJOR that would need a fourth is BLOCKED: escalate it to the operator as a decision ask, and enter the answer in `brainstorm-decisions.md` (status: `crucible:brainstorming` § Workspace provisioning). Where the cap is spent, the operator's answer or ruling is the escalation's answer and may open the wave.

A review missing a verdict (a pass that leaves a lead it was handed unruled, a re-review that leaves a fix-report concern unruled) is handled as `crucible:subagent-driven-development § Rules every route shares` states.

**An `unstated break`** goes to the operator as a decision ask, written open under `## Adjudication rulings`: repair opens a wave; acceptance, with until when or that it is permanent, is a ruling that closes the finding.

**What opens a wave**, each counted against the cap:

- a BLOCKER or MAJOR; a lead the reviewer CONFIRMED as an intent or scope gap counts as one, whatever its staked severity;
- a red suite at Finish (`crucible:subagent-driven-development § Finish`, step 5);
- a premise ruling that `skills/redteaming/references/premise-asks.md` sends to a branch-review wave;
- the operator's ruling to repair an `unstated break`;
- work the operator's close-readout answer asks for, where the spec and plan already require it or the readout listed it as a minor, improvement or lead; other work is new scope, a feature of its own;
- a drift repair, which rides the next fix wave, opening one where none is open, never before the first full-scope pass;
- the cleanup wave (below).

Nothing else opens one: a minor, a question, a lead or a premise finding never does by itself. Premise findings, a pass's or a fix report's, go where `skills/redteaming/references/premise-asks.md` sends them.

**What rides the open wave**, joining its fix dispatch's findings list:

- trivial minors and the reviewer's FIX-IN-WAVE items;
- labelled changes (an improvement you adopt, an operator's ruling, requested work), each as `Change (<kind>): <the change> — apply it, or decline it with a reason`, `<kind>` being `improvement`, `ruling` or `requested`. With no defect to confirm, none is answered NOT CONFIRMED or disputed. An applied one goes to the re-review, which checks it landed and broke nothing. A declined ruling or requested change goes back to the operator in the next close readout; a declined improvement is work left open.

Every minor that rode no wave becomes a line under `## Deferred minors`, listed for the operator in the close readout: no ruling per minor, never chased by you.

An improvement you adopt, from a question or a RECOMMENDED lead, is a lightly held change you name in the close readout; it rides the next fix wave and opens none but the cleanup wave. Where no wave follows, it goes to the operator in the close readout, as does a RECOMMENDED lead you don't adopt, its verdict added to its ledger line.

**The cleanup wave.** Once the review has ended with no BLOCKER or MAJOR open and a wave remains under the cap, you may, before returning to Finish, open one cleanup wave of the minors, and the leads the reviewer ruled CONFIRMED or RECOMMENDED, that you judge worth fixing; improvements alone may make one. It runs as any wave: its scoped re-review, then step 3. One per branch: minors it or a later pass raises open no other wave; a BLOCKER or MAJOR opens a normal one.

**Disputes** follow `crucible:subagent-driven-development § Disputes and adjudication`. Raise a finding you judge wrong before the next wave opens or with a wave's disputes. Never drop a BLOCKER or MAJOR, nor park one on your own ruling; each dismissed one reaches the operator with its ruling in the close readout.

**Ledger lines:**

- under `## Progress`, per wave: `Branch wave <n>/3 (<X> fixed, <Z> disputed — <one-liners>; commits <a7>..<b7> or none)`; the cleanup wave's, `Branch wave <n>/3 (cleanup, <X> fixed, …)`, so a resumed controller sees it spent. On the lane, the lane ledger's `Wave <n>:` line or its cleanup form instead.
- under `## Deferred minors`, a dispute-only wave's fix-report concerns: `Branch wave <n>: lead: <one-liner>`.
- under `## Questions`, each Questions item with your disposition, which carries it to the operator or rules on it (the close readout lists them; no seat reads them): a pass's as `Branch review pass <k>: <item> — <your disposition>`, a fix report's as `Branch wave <n>: <item> — <your disposition>`; and each declined change, `Branch wave <n>: <the change> — declined: <its reason>`.

When the review ends, return to `crucible:subagent-driven-development § Finish`.

## Standalone mode

For a branch with no SDD run: no ledger, no workspace, no wave loop, no cap.

1. Dispatch the branch reviewer as above, its card filled by its standalone-mode rules. It returns its report as its final message, the record of everything it raises, questions included.
2. Handle the findings yourself, under `crucible:receiving-review`: you are not an SDD controller. Fix the BLOCKER and MAJOR findings you confirm, and after substantial fixes run this mode again. A premise finding or an `unstated break` goes to the operator as a decision ask, never to a fix on your own. The operator decides what remains open.

## Common Rationalizations

| Excuse | Reality |
|---|---|
| "I'll just review the diff myself instead of dispatching a reviewer" | The diff and its evaluation belong in the reviewer's context, not yours. |
