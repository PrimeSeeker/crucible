### Disputes and adjudication

**Who rules** on a disputed finding (an implementer's NOT CONFIRMED, one you judge wrong, or a plan conflict: it collides with plan text, or a reviewer finds a binding item's literal reading reaches a case its author did not consider; is the plan or the work wrong?):

- you, with your evidence;
- instead, a fresh adjudicator seat, where it touches binding content (a literal-reading finding always does) or the Intent, and on every dispute about a diff you wrote: any commit of yours, such as an inline task (`Task <N>: inline`) or Finish's open items, and any lane diff;
- the operator, as a decision ask, on a plan conflict that is a design judgment.

A finding that fails a verdict and collides with plan text is ruled on first as a plan conflict; if the plan is upheld, the verdict failure stands and enters the loop.

**The adjudicator.** Send each batch of its disputes (a wave's, or any you raise together) to one fresh adjudicator seat, with a prompt you compose:

- each finding verbatim with its id, and its evidence (the fix report's or yours);
- what it was graded against: the plan pointer (task loop); the spec at its pinned revision and the plan (branch review); the note at its pinned revision (very-small lane); plus the umbrellas `skills/subagent-driven-development/references/dispatch-composition.md` item 2 adds;
- per finding, its review's range, in the task loop with the amendment commits inside it;
- copied in, `skills/subagent-driven-development/references/seat-rules.md` § What binds, § Binding changes and § Building the diff, the last applied to each range in turn, each range's files named apart, in its scratch subdirectory (`dispatch-composition.md` § Filling a card);
- the mandate: per finding, UPHELD or DISMISSED with a ruling, marking each ruling that touches binding content; read only in the worktree, write only the report and the scratch subdirectory;
- the report path: `sdd/reports/task-<N>-adjudication-<b>.md` (task loop) or `sdd/branch-review/adjudication-<b>.md` (branch review), `<b>` numbering that task's or review's batches.

The status check applies.

**Outcomes** go under `## Adjudication rulings`: the finding, UPHELD or DISMISSED, the ruling and its reason, and your evidence or the adjudicator's report path. An upheld finding cannot be disputed again: it re-enters the loop, or joins the operator ask after the task's third wave. A dismissed one is closed. A ruling adds no wave.

An adjudicator's ruling marked as touching binding content, or made on a literal-reading finding, passes `skills/redteaming/references/flip-paths.md` § The containment test before you act on it: record a contained one as your ruling, as that section states; any other is a decision ask, recorded as `pending operator`, its finding open until answered. On the very-small lane, one changing the note's binding parts is the operator's, contained or not.
