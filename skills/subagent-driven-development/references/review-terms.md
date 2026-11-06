# Review terms

A section cited but not held here is in `seat-rules.md`. Each site applying an arrangement question says what its answer decides there.

## What binds in a spec

What binds in a spec is its Constraints & invariants, the preamble conventions it declares binding and the decisions it records as the operator's firm preference; where its preamble carries an `Umbrella:` line, also the feature's own entry in that umbrella, the one naming its feature folder's slug, and the umbrella's Constraints & invariants and firm decisions, up the chain (the line, and which changes in a reviewed range are findings: `skills/brainstorming/references/umbrella-children.md` § Children). The spec is a hypothesis, probably subtly wrong and certainly locally imperfect: binding means never changed silently, not never changed without the operator. Binding text is read for its intent: a case its literal reading reaches that its author plainly did not consider is raised for a ruling, never applied literally.

## The arrangement questions

**The overturn question.** Is overturning a major mechanism after code reasonably expected? A major mechanism is a part of the design other parts build on: a component, a rule others key on, a file role, a data flow, an interface between parts. Overturning one replaces, removes or re-shapes it; an addition, or a correction leaving its shape standing, does not. Before code the answer is a forecast from the design and its records; after code it is read from the code too.

Before any review the answer is no in two usual cases:

- the work has no major mechanism: it adds to, corrects or removes within mechanisms that stay as they are;
- the work, a whole design or a single task, is **overdetermined**: every decision in it is forced by what is already fixed (the codebase, binding items, earlier decisions) so firmly that no alternative survives: a careful independent reader would make the same choices, leaving review before code and a fresh reader's pass no choice to change.

A no for any other reason states that reason.

## An umbrella's overturn question

For an umbrella's campaign the code is its children's: once they are implemented, is overturning a major mechanism the umbrella fixes (such as its split into children, an interface between them or a constraint they share) reasonably expected?

## The mark's criterion

A plan task may take the branch review as its first review when it builds no major mechanism, leaves its implementer little of how it works to decide, and nothing outside it depends on its details: later tasks, contracts and readers build on what it delivers, never on how it does it. The branch review runs only after every later task, too late for a detail something else builds on.

## Around the diff

An improvement or bug fix an implementer comes across in the files its task changes, or in what the changed code directly calls or is called by, is part of the task: the implementer makes it where tests cover it, one it adds included, and nothing outside the task relies on what it changes, and logs it in one line in the Decision Log. One needing another task's file, binding content, a new capability or a restructure is proposed, never made. A fix wave makes only what its dispatch lists. In review, a logged one inside this boundary is not extra and passes scope, and is judged on quality; one beyond it fails scope.

## Finding scope

- The artifact's advisory register (mechanism sketches, solution shapes an implementer may replace) is graded only for contradiction with binding content or infeasibility; missing or imperfect detail there is not a finding.
- Missing local mechanism detail (inside one implementer's natural scope) is not a finding at spec or plan stage; missing non-local mechanism is: cross-task or cross-component contracts, shared formats, orderings or state, consumers outside the change's own files.
- Content a format requires (a plan task's required fields and acceptance, a spec's required sections) is never local detail: its absence is a finding.
- Contradictions and infeasibility are findings at any locality, as are the two findings § Binding items and unrecorded choices names.

## Suite bound

A check you run stays focused: never a package-wide suite, a race-detector run, or a repeated or high-count loop. Recommend heavy validation in your report instead.
