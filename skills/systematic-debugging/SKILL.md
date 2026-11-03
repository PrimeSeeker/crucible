---
name: systematic-debugging
description: Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes
---

# Systematic Debugging

## Overview

Use for any technical issue, including performance problems, build failures and integration issues.

## The Iron Law

NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST. Propose no fix until Phase 1 is complete: its applicable steps done and you understand what fails and why. Symptom fixes are failure. Violating the letter of this process is violating its spirit.

## The Four Phases

Complete each phase before starting the next.

### Phase 1: Root Cause Investigation

1. Read error messages carefully: skip no error or warning, read stack traces completely, note line numbers, file paths and error codes. They often hold the solution.
2. Reproduce consistently: the exact steps, and whether it happens every time. If you can't, gather more data; don't guess.
3. Check recent changes: git diff, recent commits, new dependencies, config changes, environmental differences.
4. In a system of several components (CI → build → signing, API → service → database), instrument every component boundary before proposing fixes: log the data entering and leaving each component, verify environment and config propagate, check state at each layer. Run once to see where it breaks, analyze that evidence to find the failing component, then investigate that component. Example: in CI signing, check at each layer (workflow, build script, keychain, codesign call) whether the identity is present.
5. When the error is deep in the call stack, trace backward: where does the bad value originate, and what called this code with it? Keep tracing up until you find the source, and fix there, not at the symptom. The full technique: `root-cause-tracing.md`.

### Phase 2: Pattern Analysis

1. Find similar working code in the same codebase.
2. If you are implementing a pattern, read the reference implementation completely, every line, and understand it fully before applying it.
3. List every difference between the working and the broken code, however small; don't assume any of them can't matter.
4. Understand the dependencies: the other components it needs, its settings, config and environment, and the assumptions it makes.

### Phase 3: Hypothesis and Testing

1. Form one specific hypothesis and write it down: "I think X is the root cause because Y."
2. Test it with the smallest possible change, one variable at a time; never fix several things at once.
3. Confirmed: go to Phase 4. Not confirmed: form a new hypothesis; don't add fixes on top.
4. When you don't know, say "I don't understand X". Don't pretend to know; ask for help and research more.

### Phase 4: Implementation

1. Write the failing test before the fix; where no test or script can reproduce the bug, say why. Make it the simplest reproduction: an automated test where possible, a one-off script where there is no framework. Test craft: `skills/subagent-driven-development/writing-good-tests.md`.
2. Implement a single fix that addresses the root cause: one change at a time, no "while I'm here" improvements, no bundled refactoring.
3. Verify: the test passes, no other test breaks, the issue is actually resolved. Claim success only on fresh evidence: run the covering tests and show their output.
4. If the fix doesn't work or reveals a new problem elsewhere, stop and count the fixes tried. Fewer than 3: return to Phase 1 and re-analyze with the new information. 3 or more: step 5.
5. Question the architecture. Signs of an architectural problem: each fix reveals new shared state, coupling or a problem in a different place; fixes would need massive refactoring; each fix creates new symptoms elsewhere. Ask whether the pattern is fundamentally sound, whether it survives only through inertia, and whether to refactor the architecture instead of fixing symptoms. Discuss with your human partner before attempting any more fixes: this is a wrong architecture, not a failed hypothesis.

## Red Flags

Any of these thoughts means STOP and return to Phase 1:

- "Quick fix for now, investigate later": the first fix sets the pattern.
- "Just try changing X and see if it works."
- "Multiple fixes at once saves time": you can't isolate what worked, and it causes new bugs.
- "Skip the test, I'll verify manually" or "I'll write the test once the fix works": untested fixes don't stick; the test written first proves the fix.
- "I see the problem", "It's probably X" or "I don't fully understand, but this might work": seeing symptoms is not understanding the root cause.
- "The reference is too long, I'll adapt the pattern": partial understanding guarantees bugs; read it completely.
- "The issue is simple" or "It's an emergency", so skip the process: simple issues have root causes too, and systematic debugging is faster than guess-and-check thrashing.
- "One more fix attempt", after 2 or more failed fixes: at 3 or more, Phase 4 step 5 instead.

## When Process Reveals "No Root Cause"

Suspect an incomplete investigation first. If systematic investigation shows the issue is truly environmental, timing-dependent or external, the process is complete: document what you investigated, implement appropriate handling (retry, timeout, error message), and add monitoring or logging for future investigation.

## Supporting Techniques

Part of this process, in this directory: `condition-based-waiting.md`, `defense-in-depth.md`, `root-cause-tracing.md`. In order, they replace arbitrary timeouts with condition polling, add validation at several layers once the root cause is found, and detail Phase 1 step 5's backward trace.
