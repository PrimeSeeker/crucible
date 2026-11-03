# Defense-in-Depth Validation

## Overview

When you fix a bug caused by invalid data, one validation point feels sufficient, but other code paths, refactoring or mocks can bypass it. Validate at every layer the data passes through, so the bug becomes structurally impossible, not just fixed.

## The Four Layers

1. Entry point validation: reject obviously invalid input at the API boundary (`createProject` throws if the path is blank, nonexistent or not a directory).
2. Business logic validation: ensure the data makes sense for this operation (`initializeWorkspace` throws if `projectDir` is missing or empty).
3. Environment guards: prevent dangerous operations in specific contexts (under `NODE_ENV=test`, `gitInit` refuses to run outside the temp directory, comparing normalized, resolved paths).
4. Debug instrumentation: capture context for forensics (debug-log the directory, cwd and a stack trace before `git init`).

## Applying the Pattern

When you find any bug:

1. Trace the data flow: where the bad value originates and is used.
2. Map every checkpoint the data passes through.
3. Add validation at each layer: entry, business, environment, debug.
4. Test each layer: try to bypass layer 1 and verify layer 2 catches it.
