---
name: requesting-code-review
description: Use when a branch's tasks are complete or before merging - dispatch the whole-branch reviewer with the execution ledger's deferred minors and rulings in its inputs
---

# Requesting Code Review

Dispatch the whole-branch reviewer — a fresh subagent that gets precisely
crafted context for evaluation, never your session's history. This is the
invocation skill for the branch-review mandate: evidence grounding, staked
severity, full-scope reads — the review principles without the panel
apparatus.

**Core principle:** the branch review is the last gate before merge; it reads
everything, and its findings are fixed by dispatched implementers, never by
the controller.

## When to Request Review

**Mandatory:**
- After all tasks in `crucible:subagent-driven-development` complete (its
  Whole-Branch Review step — that section owns the loop this skill invokes)
- Before merging any substantial branch

**Optional but valuable:**
- When stuck (fresh perspective)
- Before refactoring (baseline check)
- After fixing a complex bug

## How to Request

**1. Package the branch** — the diff never enters your context:

```bash
bash <plugin-root>/skills/subagent-driven-development/scripts/review-package <feature-slug> MERGE_BASE HEAD
```

MERGE_BASE = `git merge-base main HEAD` or the recorded branch point — never
`HEAD~1`, which silently drops all but the last commit.

**2. Dispatch the branch reviewer** on **Opus** — or on **Fable only when the
operator has flagged this branch as a major feature** (once, at this terminal
review; unasked Fable dispatches are unauthorized spend) — filling the
template at [code-reviewer.md](code-reviewer.md).

The dispatch includes the review-package path and the requirements source,
**plus the SDD ledger's deferred minors and the adjudication rulings from
execution** — the execution-phase visibility surface; a roll-up nobody reads
is a silent discard.

**Placeholders:**
- `[DESCRIPTION]` — brief summary of what was built
- `[REQUIREMENTS]` — what it should do (plan file path, task text, or
  requirements)
- `[BASE_SHA]` / `[HEAD_SHA]` — the reviewed range
- `[DIFF_FILE]` — the path `review-package` printed
- `[LEDGER_MINORS]` — the deferred minors from the SDD ledger, verbatim
- `[RULINGS]` — the adjudication rulings from execution, verbatim

**3. Act on findings.** Severity vocabulary: **BLOCKER / MAJOR / MINOR.**
The loop machinery — fix waves (one fix dispatch with the complete findings
list, executed by a fresh implementer, never the controller), scoped
re-reviews, the full-scope closing pass, the severity-floor stop rule, and
the **3-wave cap** — has a single source: `crucible:subagent-driven-development`
§ Whole-Branch Review. Follow it from there; do not improvise a variant here.

- A pass with no open or new BLOCKER/MAJOR ends the review.
- Trivial minors may ride a fix wave; nontrivial minors are parked with a
  ruling and surfaced — never chased by the controller.
- A finding you judge wrong is parked with a ruling, never silently dropped.

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "I'll just review the diff myself instead of dispatching a reviewer" | You're the coordinator — reviewing the diff inline burns the context window you need to keep driving the work. Dispatch a reviewer subagent: the diff and the evaluation live in its context, and only the findings come back to you. |
| "The reviewer needs my whole session history to understand the change" | Hand it precisely crafted context, never your session's history. That keeps the reviewer on the work product, not your thought process. |
| "The ledger minors are noise, skip them" | They reached the dispatch deliberately — a deferred minor nobody re-reads is a silent discard. The reviewer triages them. |

## Red Flags

**Never:**
- Skip review because "it's simple"
- Ignore BLOCKER findings
- Merge with open BLOCKER/MAJOR findings
- Fix findings yourself in the controller session
- Dispatch below Opus to save cost — Opus is this seat's contract floor
- Dispatch on Fable without the operator flagging the branch as a major
  feature — Fable is operator-authorized, never a default

See template at: [code-reviewer.md](code-reviewer.md)
