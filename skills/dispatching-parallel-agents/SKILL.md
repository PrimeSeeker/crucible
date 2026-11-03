---
name: dispatching-parallel-agents
description: Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies
---

# Dispatching Parallel Agents

## Overview

Dispatch one agent per independent problem domain and let them work concurrently. Construct each agent's instructions and context precisely, so it stays focused and succeeds; never let it inherit your session's context or history, which also keeps your own context for coordination.

## When to Use

Use when each problem can be understood without context from the others and the investigations share no state, such as 3+ test files failing with different root causes or subsystems broken independently.

Don't use when:
- the failures are related (fixing one might fix the others): investigate them together first;
- understanding the problem requires seeing the whole system;
- you don't yet know what is broken (exploratory debugging);
- agents would interfere, editing the same files or using the same resources.

## The Pattern

### 1. Identify Independent Domains

Group the failures by what is broken.

### 2. Create Focused Agent Tasks

Give each agent a self-contained prompt with:
- Scope: one problem domain, such as one named test file or subsystem.
- Goal: e.g. make these tests pass.
- Context: everything needed to understand the problem, such as the error messages and the failing tests' names.
- Constraints: what it must not do, e.g. change code outside the scope, or just raise a timeout instead of finding the cause.
- Output: what to return, e.g. a summary of the root cause found and the changes made.

### 3. Start Them All Before Waiting

Start every independent agent before waiting for any of them to finish, then wait on the set. Your host's parallel fan-out operation starts them; where it admits fewer at once, start the rest as capacity frees. Tasks are independent only where they share no state, need no ordering and neither reads the other's output; tasks that are not independent run one at a time, whatever the host permits.

### 4. Review and Integrate

When the agents return:
1. Read each summary, then check the diff of the files it changed: a summary reports what the agent meant to do, the diff what it did.
2. Check for conflicts: did agents edit the same code?
3. Run the full test suite to verify the fixes work together.
4. Spot check the work: agents can make systematic errors.
5. Integrate all changes.
