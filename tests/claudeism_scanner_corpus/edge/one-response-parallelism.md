# Parallelism by response shape

Multiple dispatch calls in one response = parallel execution. One per response = sequential.

A variant of the same claim: send several tool calls in a single message and
the host runs them in parallel.

The replacement property carries no host mechanic: dispatches are parallel
when the tasks are independent — no shared state, no ordering, neither
reading the other's output.
