Lane: very-small (operator-confirmed 2026-11-06)

# Repeat hits

## Intent

A campaign's fix lists can patch one passage round after round, each fix
adding a clause for the case just found, leaving it jagged and with holes for
later rounds to find. Make a repeat hit on a passage a rewrite of that passage,
adding no capability beyond what the finding requires. No break.

## Change list

- `skills/redteaming/references/fix-application.md` gains, after Fix altitude:
  "**Repeat hits** (binding): where a finding hits a passage an earlier round
  of this campaign already fixed, the item replaces the passage, stated from
  what it is for and keeping what those fixes required, rather than adding a
  clause. The replacement adds no capability the artifact does not already
  have."
- `skills/writing-skills/SKILL.md`: the fix sentence becomes "A fix revises the
  sentence that owns the case, restated over its whole class where that covers
  the case; any words it adds are the rule's new condition or action, stated as
  the sentence states its others, while the finding's reasons, its failure
  scenario and what a pointer already defines stay out of the text."
- `docs/decisions/fix-verification-and-merge.md`: the rule in its Decision, the
  test's figures and limits under a new `### Repeat hits`, seat-level class
  naming under Rejected, and a Changes line. `docs/decisions/authoring-crucible.md`:
  a Changes line.
- `docs/backlog/tension-closing.md`: states that the rule covers repeat hits
  only, and that the wider restructuring and the measurement stay open.
- `tests/prose-budget.txt`: raised for both skills.

## Acceptance

- A search finds `**Repeat hits**` once in
  `skills/redteaming/references/fix-application.md`, `restated over its whole
  class` once in `skills/writing-skills/SKILL.md`, `### Repeat hits` once in
  `docs/decisions/fix-verification-and-merge.md`, and `Repeat hits` in
  `docs/backlog/tension-closing.md`.
- `python -m pytest tests/` passes.

## Out of scope

- Seat templates.
- Branch review and implementer text.
- Any wider restructuring of how tensions close.
- Measuring real campaigns.
