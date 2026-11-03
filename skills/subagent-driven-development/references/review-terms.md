# Review terms

The review terms controllers read and seat templates take by splice, each template the sections its seat follows. A section cited here and not held here is in `skills/subagent-driven-development/references/seat-rules.md`.

## The arrangement questions

Each site that applies one of these says what its answer decides there.

**The overturn question.** Is overturning a major mechanism after code
reasonably expected? A major mechanism is a part of the design other
parts build on: a component, a rule others key on, a file role, a data
flow, an interface between parts. Overturning one replaces, removes or
re-shapes it; an addition, or a correction that leaves its shape
standing, does not count. Before code the answer is a forecast from the
design and its records; after code it is read from the code as well.

Before any review, the answer is no in either of two usual cases:

- the work has no major mechanism: it adds to, corrects or removes
  within mechanisms that stay as they are;
- its decisions are overdetermined.

A no for any other reason states that reason.

For an umbrella's campaign, the code is its children's: the question
asks whether, once the children are implemented, overturning a major
mechanism the umbrella fixes is reasonably expected, such as its split
into children, an interface between them or a constraint they share.

**Overdetermined.** Work, a whole design or a single task, is
overdetermined when every decision in it is forced by what is already
fixed (the codebase, binding items, decisions taken earlier) so firmly
that no alternative survives them: a careful independent reader would
make the same choices, so neither review before code nor a fresh
reader's pass has one left to change.

**The mark's criterion.** A plan task may take the branch review as its
first review, with no task review of its own, where it is low in
mechanism and nothing outside it depends on its details: it builds no
major mechanism and leaves little of how it works for its implementer
to decide, and later tasks, contracts and readers build on what it
delivers, never on how it does it. The branch review runs only after
every later task, too late for a detail something else builds on.

## Finding scope

- The artifact's advisory register — its mechanism sketches, the shape of
  a solution an implementer may replace — is graded only for contradiction
  with binding content or infeasibility; missing or imperfect detail there
  is not a finding.
- Missing local mechanism detail — detail inside one implementer's natural
  scope — is not a finding at spec or plan stage. Missing non-local
  mechanism is: cross-task or cross-component contracts, shared formats,
  orderings or state, consumers outside the change's own files.
- Content a format makes binding — a plan task's required fields and
  acceptance, a spec's required sections — is never local detail: its
  absence is a finding.
- Contradictions and infeasibility are findings at any locality, and so
  are the two § Binding items and unrecorded choices names.

## Suite bound

A check you run stays focused: never a package-wide suite, a
race-detector run, or a repeated or high-count loop. Recommend heavy
validation in your report instead.
