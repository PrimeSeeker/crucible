# Writing Good Tests

## Overview

A test exists to catch a specific break: every test names that break and exercises the real thing. Tests ship with the implementation: the TDD cycle (failing test, minimal implementation, refactor) is what "complete" means. Ship the tests the behavior needs and only those; a test written to satisfy process costs maintenance forever.

## Principle 1: Name the Break

Before writing the test body, name the production change that should make it fail, and whether that change is a bug or a decision; if you cannot name one, or it is only a decision, redesign the test around an observable behavior. A test earns its place by catching a wrong branch, missing side effect, wrong argument, boundary case or broken contract.

**Derive expectations independently**, from literals and hand-checked fixtures; prefer table-driven tests with literal `want` values. An expectation computed by the code under test or its helpers passes whatever that code does:

```typescript
// ❌ Mirror assertion: the same builder computes both sides — always true
const expected = buildSearchQuery({ tag: 'urgent' });
expect(buildSearchQuery({ tag: 'urgent' })).toBe(expected);

// ✅ Hand-derived literal
expect(buildSearchQuery({ tag: 'urgent' })).toBe('tag:"urgent"');
```

**No change detectors.** A test that only intentional decisions can fail (a constant's value, exact message wording, private structure) fires on redesign and sleeps through bugs. Test the behavior that depends on the decision: not `expect(MAX_RETRIES).toBe(5)` but "a failing call is retried 5 times and the 6th attempt never happens."

**Behavior, not text.** Asserting that a script, skill or config contains an exact line proves only that the source is the source. Run scripts against controlled inputs and assert outputs, side effects or exit codes. Documents that instruct agents are tested by the consuming agent's behavior (crucible:writing-skills); prose for humans earns no test.

**Your code, not the framework.** Test the contract your code makes at its boundaries: the route you register, the query you emit, the payload you produce. Upstream mechanics, such as your router invoking a registered handler, are their maintainers' tests. Only when upstream behavior genuinely surprised you, write one narrow characterization test naming the assumption. Constructors, getters, constants and trivial forwarding earn tests only when they validate, normalize, default, derive, enforce or cause side effects; otherwise assert the first consumer-visible result that depends on them.

## Principle 2: Exercise the Real Thing

**The mock earns no assertions.** A mock assertion checks only that the mock is there, not the component. Assert the real component's behavior; if the mock is what you are checking, unmock it or delete the assertion. Good: `expect(screen.getByRole('navigation')).toBeInTheDocument()`. Bad: `expect(screen.getByTestId('sidebar-mock')).toBeInTheDocument()`.

**Mock at the right level.** Before mocking a method, learn every side effect of the real one; mock the slow or external operation and keep what the test depends on real. When unsure, run the test against the real implementation first and observe what needs to happen. Bad: mocking `ToolCatalog.discoverAndCacheTools` swallows the config write that duplicate detection reads. Good: mock only `MCPServerManager` (slow startup) and keep the config write real.

**Make doubles specific.** When arguments, call counts or ordering are part of the contract, assert them: a fake that accepts anything verifies nothing. Give each branch (success, error, malformed) its own fixture or spy, so the wrong branch cannot satisfy the expectation.

**Mirror real data completely.** Mock responses carry every documented field of the real structure, not just those your test reads: a partial mock passes the test while integration breaks on the omitted field.

**Production classes carry production methods only.** A method only tests call, cleanup included, lives in test utilities, never as a `destroy()` on the production class. Ask: is this method called only from tests? Does this class own this resource's lifecycle? Wrong answers → test utility.

**Prefer real components.** When mock setup outgrows the test logic, mocks miss methods the real components have, or tests break when the mock changes, switch to an integration test with real components.

## The Mutation Check

Before finishing, mentally mutate the production code; at least one test should fail for each realistic mutation:

- Wrong constant or argument
- Wrong branch handler
- Missing state change or side effect
- Empty or default return
- Missing validation for zero, empty, nil, unauthorized, or malformed input

A mutation nothing catches marks the behavior as unprotected, or the test as tautological.

## Warning Signs

- Setup and assertion share the same object, guaranteeing equality
- The test can fail only through a panic, crash, or missing selector
- The test fails on every intentional change, never on accidental breakage
- Expected values are hidden behind loops, builders, or helpers
- The test greps source text, or asserts a removed symbol stays removed
- The test would still matter if only the framework remained
- The test exists for coverage, checking no side effect or outcome
- An assertion checks a `*-mock` test ID, or fails if you remove the mock
- A method is called only from test files
- Mock setup is more than half the test, or you can't explain why the mock is needed
- Mocking "just to be safe"
