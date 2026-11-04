### The very-small lane

A **lane note** takes the spec's place as the lane's only artifact: drafted and shown with the lane proposal at step 4, written at step 5 as the operator approved it. About a page, in four parts:

- **Intent** — what the change is for, and any break, as the spec contract states it.
- **Change list** — what changes, at file or behavior level.
- **Acceptance** — runnable checks.
- **Out of scope**.

Parts a backlog item already carries may be copied in verbatim. Advisory shape: the four parts as `##` headings under a `Lane: very-small (operator-confirmed <date>)` line.

Intent, Acceptance and Out of scope bind the branch reviewer. The change list is advisory: a departure is recorded in the SDD ledger, never edited into the note.

Verification at writing and quoting no operator message hold as in the spec contract. Run the self-review, with its evidence check (claims verified at writing, the consumer sweep), on the draft before showing it. Run each mechanical Acceptance check once, as you write it: a check of the state the change brings about must fail on the pre-change tree, which shows it can fire.

The note is `note.md` in the feature folder, born and committed as a spec is; commit it as approved on the feature branch, before the handoff. From that commit on it is frozen: a change to its binding parts is an operator decision ask, never a controller edit, and SDD's lane section re-pins an approved change in its ledger.

Under an umbrella the note's preamble carries the umbrella line (`skills/brainstorming/references/umbrella-children.md`).
