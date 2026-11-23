Lane: very-small (operator-confirmed 2026-11-23)

# Process notes: the closing line says what deserves attention

## Intent

Two changes.

1. **The closing line.** When work ends, a controller gives the operator
   one line on its process notes. Until now the line held the count of
   notes, the main one and an offer of the rest. It now says what in the
   notes deserves the operator's attention, with an offer of the rest. A
   hunch counts, named as one. A routine note counts once it has recurred
   or its cost is material. With nothing that deserves attention, a
   feature's close readout says so and other work says nothing, which
   takes the place of the line saying that no notes were made. The count
   goes. What is noted, as it happens, stays as broad as it is; an
   operator's instruction asking for more, or for none, governs the line
   as before.
2. **The releases record** says that the first trial installed from the
   GitHub form of a branch ref on both hosts, in place of saying that
   form is unmeasured.

Premise. On three features built back to back on crucible itself, one
controller made six to nine notes each, most of them routine (expected
costs, the session running an older installed copy, small slips), and
reported each time a count and one note. The maintainer, shown a count of
nine, asked whether anything in them was significant and said the notes
were starting to look endless. Nothing else was measured: three features,
one controller, crucible's own text. An exclusion of issues that cannot
be fixed was considered by the maintainer and left out as too finicky;
recurrence was accepted as a test, though what a controller knows of
earlier features is its own memory of one project.

Break: an operator's line no longer carries the count of notes. Nothing
else changes for them.

## Change list

- `skills/using-crucible/SKILL.md`, the Process notes paragraph: the
  closing line as above.
- `docs/decisions/operator-steering.md`: the Decision's sentence on the
  line, § Process notes (the default and the nothing-to-say case, the
  rule's size in words and characters), the rejected count, and a
  `## Changes` line.
- `README.md`: the Process notes paragraph's sentence on what the
  operator sees.
- `docs/backlog/skill-rewrite-reaudit.md`: the read of process notes also
  asks whether the line named what deserved attention.
- `docs/decisions/releases.md` § A testing branch: the first trial's
  result, with a `## Changes` line.
- `tests/prose-budget.txt`: the changed count, the commit saying what the
  words buy.

## Acceptance

1. `python -m pytest tests/` passes, with `TOTAL_CAP` in
   `tests/test_prose_budget.py` still 47387; the suite holds the
   always-loaded text under its 10,000 characters.
2. `git grep -c "^- 2026-11-23:" -- docs/decisions/operator-steering.md`
   prints a count.
3. `git grep -c "^- 2026-11-23:" -- docs/decisions/releases.md` prints 2.

On the tree before the change, check 1 passes, check 2 prints nothing and
check 3 prints 1. No check searches for the new wording: the Intent
states the outcome and the branch reviewer judges the text against it.
Whether controllers' lines then name what deserves attention shows only
in later sessions, which the re-audit read covers.

## Out of scope

- What a controller notes and when: collection stays as it is.
- The rules for the full list
  (`skills/using-crucible/references/process-notes.md`).
- The seats' sentence on what was off, and the close readout's item in
  `skills/subagent-driven-development/references/finish.md`.
- A store for notes beyond the feature workspace.
- Excluding notes on what cannot be fixed.
- `TOTAL_CAP`.
