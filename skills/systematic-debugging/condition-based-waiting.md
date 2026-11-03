# Condition-Based Waiting

## Overview

Flaky tests often guess timing with arbitrary delays, creating races: they pass on fast machines and fail under load or in CI. Wait for the condition you care about, not a guessed duration.

## When to Use

Use it when tests have arbitrary delays (`setTimeout`, `sleep`, `time.sleep()`), are flaky (pass sometimes, fail under load), time out in parallel runs, or wait for async operations to complete. Don't use it when testing actual timing behavior (debounce, throttle intervals); write that delay as in When Arbitrary Timeout IS Correct.

## Core Pattern

Instead of sleeping 50ms before reading `getResult()`, wait until `getResult() !== undefined`, then read the result and assert on it as before.

Typical conditions: event `events.find(e => e.type === 'DONE')`, state `machine.state === 'ready'`, count `items.length >= 5`, file `fs.existsSync(path)`, compound `obj.ready && obj.value > 10`.

## Implementation

```typescript
async function waitFor<T>(
  condition: () => T | undefined | null | false,
  description: string,
  timeoutMs = 5000
): Promise<T> {
  const startTime = Date.now();
  while (true) {
    const result = condition();
    if (result) return result;
    if (Date.now() - startTime > timeoutMs) {
      throw new Error(`Timeout waiting for ${description} after ${timeoutMs}ms`);
    }
    await new Promise(r => setTimeout(r, 10));
  }
}
```

- Poll every 10ms; polling too fast (`setTimeout(check, 1)`) wastes CPU.
- Always set a timeout with a clear error; without one, an unmet condition loops forever.
- Call the getter inside the loop; state cached before the loop is stale.

`condition-based-waiting-example.ts` in this directory holds a complete implementation with domain helpers (`waitForEvent`, `waitForEventCount`, `waitForEventMatch`): copy its pattern into your project's test helpers, adapting the types. It is not a runnable script, so it carries no platform requirement.

## When Arbitrary Timeout IS Correct

Wait first for the triggering condition, then for the timed behavior: a delay derived from known timing (a tool ticking every 100ms needs 200ms for two ticks), not a guess, with a comment saying why.
