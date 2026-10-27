---
name: receiving-review
description: Use when review feedback arrives from outside crucible's own review loops — the operator, a pull request's reviewers or bots, a standalone branch review — before acting on it.
---

# Receiving Review

Review feedback is a claim about the code. Check it before you act on it, whoever sent it.

**Scope.** Feedback from the operator, a pull request's human reviewers and bots, the findings `crucible:requesting-code-review`'s standalone mode hands back, and any other reviewer. Crucible's own loops carry their own rules for findings, and this skill does not apply inside them: task review and the branch-review loop (`crucible:subagent-driven-development`, `crucible:requesting-code-review`), and redteam campaigns (`crucible:redteaming`).

## Before implementing anything

- **Read every item first, and restate each in your own words.** An item you cannot restate counts as unclear: restating catches a misreading that asking alone misses. If any item is unclear, ask about all the unclear ones before implementing any: items are often related, and a partial understanding implements the wrong thing.
- **Verify each item against the codebase.** Is it correct for this code? Would it break something that works? Is there a reason for the current code the reviewer could not see — a platform or version constraint, a caller, an earlier decision?
- **Say when you cannot verify an item**, and what checking it would take. Never proceed as if you had checked it.
- **"Do it properly" gets the YAGNI check.** Search for actual use before building out what the reviewer asks for; where nothing uses it, propose removing it instead.

## Responding

- **Push back with evidence where an item is wrong**: the code, the test or the constraint that shows it. Where pushing back feels uncomfortable, name that tension and raise the issue anyway.
- **Correct your own pushback plainly.** If checking shows the reviewer was right, say so in one line, with what you found, and implement it.
- **Replies carry content**: what changed and where, or the evidence behind a disagreement.
- **Reply where the comment was made** — on a pull request, in the comment's own thread, not as a new top-level comment.

## Who rules

The same discipline applies to every source, the operator included: the operator's feedback can rest on a wrong premise about the code like anyone's, and your check is where that gets caught.

- **The operator rules.** Put your pushback to them in analyst language, which never requires reading code, then do what they decide.
- **An outside reviewer never rules.** A disagreement that survives your evidence, or an item that conflicts with an earlier operator decision, goes to the operator as a decision ask with your recommendation.

## Implementing

Implement accepted items one at a time — blocking issues first, then simple fixes, then complex ones — and run the tests covering each change before moving to the next. Feedback that turns out to be new scope is a new feature for `crucible:brainstorming`, not part of this change.

The thread, or your conversation with the operator, is the record; this skill keeps no files of its own.
