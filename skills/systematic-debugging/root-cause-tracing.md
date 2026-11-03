# Root Cause Tracing

## Overview

Never fix only where the error appears, which treats a symptom: trace backward through the call chain to the original trigger and fix there.

Use this when the error happens deep in execution rather than at the entry point, the stack trace shows a long call chain, it is unclear where invalid data came from, or you need to find which test or code triggers the problem.

## The Tracing Process

1. Observe the symptom, the error as reported: `git init` failed in `~/project/packages/core`.
2. Find the immediate cause, the code that directly produces it: `execFileAsync('git', ['init'], { cwd: projectDir })`.
3. Ask what called it, and build the caller chain: `WorktreeManager.createSessionWorktree` ← `Session.initializeWorkspace` ← `Session.create` ← the test at `Project.create`.
4. Keep tracing up, checking the value passed at each level: `projectDir` is `''`, and an empty `cwd` resolves to `process.cwd()`, the source directory.
5. Find the original trigger, where the bad value came from: `setupCoreTest()` returns `tempDir: ''`, read at top level before `beforeEach` sets it.

A dead end, where you cannot trace further back, calls for instrumentation (§ Adding Stack Traces) and another trace, never a fix where the error appears. If instrumentation finds no earlier cause either, follow `SKILL.md` § When Process Reveals "No Root Cause".

After fixing at the source (here, `tempDir` became a getter that throws if read before `beforeEach`), add validation at each layer the bad value passed through, so the bug becomes impossible. The example's layers: `Project.create()` validates the directory, `WorkspaceManager` rejects an empty one, a `NODE_ENV` guard refuses `git init` outside tmpdir, and a stack trace is logged before `git init`.

## Adding Stack Traces

When you cannot trace by hand, instrument the function that performs the problematic operation: just before the operation, not after it fails, log `new Error().stack` under a tag such as `'DEBUG git init:'`, with context: directory, cwd, environment variables, timestamps. In tests log with `console.error()`, not the project logger, whose output may not show.

Run the tests with stderr merged and filter for the tag: `npm test 2>&1 | grep 'DEBUG git init'`. In the captured traces, look for test file names, find the line number that triggers the call, and identify the pattern: same test? same parameter?

## Finding Which Test Causes Pollution

When something appears during tests and you don't know which test creates it, run the bisection script from the project being debugged as `bash <script> '.git' 'src/**/*.test.ts'`, where `<script>` is `<plugin-root>/skills/systematic-debugging/find-polluter.sh`; its usage lines show the arguments. It runs the tests one by one and stops at the first polluter.

The script is POSIX/Bash-only (it uses find, sort and wc). On Windows, run it from WSL or Git Bash, or bisect by hand: run the candidate test files one at a time and check after each whether the polluting file or directory appeared. The script only automates that loop.
