Lane: very-small (operator-confirmed 2026-11-07)

# A fresh look

## Intent

Rethinks that helped came mostly from the operator asking for one, and controllers
rarely start one themselves. Give controllers a standing way to do it: at any
phase, where the design or code seems overfitted, fragile, finicky, jagged or
inelegant, or where the operator asks, a fresh seat on the alternate role
challenges the assumptions and looks for another shape. No break.

## Change list

- New `skills/subagent-driven-development/references/fresh-look.md`: a
  controller-composed, read-only seat on the alternate role, with the dispatch
  composition's seven items, under its § Shared-tree rules as a review seat. Its
  prompt holds the goal, the artifact or code at issue, and the symptoms, not the
  controller's diagnosis. Its mandate: state the assumptions the shape rests on and
  challenge them, find other shapes with what each would lose, recommend one or
  say the shape is fine; no defect list, no edits. Report at
  `<workspace>/fresh-look-<k>.md`, or the host's temporary directory before a
  workspace exists. The result is the controller's to weigh: it opens no wave,
  takes no round and spends no cap; an adopted change takes the route its phase
  has for a change of its kind; one altering what the operator approved is a
  decision ask. The controller appends what it did and why to the report and names
  the run in its next readout. A second look at the same problem is a decision ask
  instead of a seat, unless the operator asked for it.
- `skills/using-crucible/SKILL.md`: the trigger, read by every controller at every
  phase: at any phase, where the design or code seems overfitted, fragile, finicky,
  jagged, inelegant or otherwise wrong, or the operator asks, read that reference
  and dispatch its seat before going on. Signs include a second patch to one
  passage, a fix that adds a special case, a rule you cannot state without its
  exceptions, and a seat saying so.
- `skills/subagent-driven-development/references/dispatch-composition.md`: the
  alternate role gains this as a fourth trigger.
- `skills/subagent-driven-development/references/finish.md`: the close readout
  lists each fresh look with what was done with it.
- `skills/redteaming/references/formats.md`: the layout gains the report.
- `docs/decisions/model-roles-and-effort.md`: the position and its basis, what the
  transcripts showed and their limits, why the wording test was skipped, that
  fresh context and model are confounded; the automatic stuck trigger stays
  declined, this one replacing no seat; a Changes line.
- `docs/backlog/skill-rewrite-reaudit.md`: read whether fresh looks fired where
  they should and whether adopted ones helped.
- `tests/prose-budget.txt` raised.

## Acceptance

- A search finds `fresh-look.md` in `skills/using-crucible/SKILL.md` and in
  `dispatch-composition.md`, and the reference exists.
- A search finds `fresh-look-<k>` in `finish.md` and `formats.md`.
- A case-blind search finds no `exactly three triggers` in `skills` or
  `docs/decisions`.
- `python -m pytest tests/` passes.

## Out of scope

- An automatic trigger, a new instrument or template, or seat templates telling
  seats to raise this.
- The wave and round caps, and the repeat-hits rule.
- A host map naming no alternate role: none does today.
- A wording test, or measuring real features.
