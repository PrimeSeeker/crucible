### The very-small lane — the lane note (step 5)

On the very-small lane a **lane note** takes the spec's place — drafted and shown with the lane proposal at step 4, written at this step as the operator approved it — the lane's only artifact, about a page, in four parts:

- **Intent** — what the change is for.
- **Change list** — what changes, at file or behavior level.
- **Acceptance** — runnable checks.
- **Out of scope**.

Intent, Acceptance and Out of scope are **binding** for the branch reviewer; the change list is **advisory**, and a departure from it is recorded in the SDD ledger, never edited into the note. A backlog item that already carries all four parts may be copied into the note verbatim. Verification at the moment of writing holds here as in the spec contract, and the self-review runs on the draft before it is shown, its evidence check — claims verified at writing, the consumer sweep — included. A mechanical Acceptance check is run once as it is written: a check of the state the change brings about must fail on the pre-change tree, and that failure is the evidence it can fire.

**The note freezes at its commit.** Commit it on the feature branch as approved — before the handoff, so before implementation starts. From that commit on, a change to its binding parts is an operator decision ask, never a controller edit; SDD's lane section re-pins an approved change in its ledger.

**A lane note under an umbrella** carries the umbrella line in its preamble (`skills/brainstorming/references/umbrellas.md`).

Advisory shape: four `##` headings (Intent, Change list, Acceptance, Out of scope) under a `Lane: very-small (operator-confirmed <date>)` line. Persistence: `note.md` in the feature folder, created by the birth step at this first write exactly as for a spec (the spec contract's persistence rule in `crucible:brainstorming`; layout in `skills/redteaming/references/formats.md` § Feature folder), committed like any spec.
