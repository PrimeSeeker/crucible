### The folded lane — the combined spec+plan document (step 5)

Where the operator confirmed the fold at step 4, this step writes **one combined spec+plan document** in place of a spec, under this fork of the spec contract in `crucible:brainstorming`. Everything the contract already says still holds. The **full six-section shape stays**, in order and in full — Intent, Decisions, Constraints & invariants, Interfaces & boundaries, Acceptance, Mechanism sketches. None of them folds away, and **Constraints & invariants** least of all: every binding-content pointer in the seat, terminal-pass, implementer and task-reviewer prompts names that section by name, so a folded document missing it aims all of them at nothing.

On top of that shape, the document carries the plan half **in the formats `crucible:writing-plans` owns**. Read that skill for the shapes and follow them exactly — don't restate them here and don't invent lane variants of them (and don't invoke it: this skill's terminal state is unchanged).

- **Task entries** in its per-task format.
- **Every plan-header section, at lane scale.** **Goal** folds into Intent and is not repeated, and the **Spec pointer** takes the folded form, `Spec: this document`, under that skill's rules for it. Every other section is present, a one-liner where trivially satisfied; the ownership census is the round-0 pre-pass's arithmetic input and is never omitted.
- **The deferred-items routing table** whenever any deferral is recorded, under the heading and in the row format that skill fixes.

Persistence: `folded.md` in the feature folder, created by the birth step at this first write exactly as for a spec (the spec contract's persistence rule in `crucible:brainstorming`; layout in `skills/redteaming/references/formats.md` § Feature folder), committed like any spec. The rest of the flow is unchanged — self-review, provisioning, the gate, and the handoff to `crucible:redteaming`, which runs the standard campaign on this artifact.
