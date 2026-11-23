Lane: very-small (operator-confirmed 2026-11-23)

# The re-audit's results, recorded

## Intent

The skill text rewrite retired and simplified mechanisms on thin evidence
and left a re-audit owed: on runs of real code, did a retired mechanism's
failure reach a later stage or the operator, and does the blind verifier
earn its keep. Later features attached further questions to the same
re-audit. It ran on 2026-11-23. This change records what it found and
what the maintainer ruled, and changes no skill text.

1. **Results go into the decision records**, each into the record that
   holds its question, as measured outcomes with their limits. Three
   rulings change a position:
   - the blind verifier stays, no longer "for now";
   - a stuck trigger is closed as not needed, no longer waiting on the
     re-audit;
   - a lane note with a plan has met the condition that reopens it and is
     not built yet.
2. **The figures of the read of 2026-11-19 are corrected.** That read's
   script counts ran on an index holding 640 of 880 seats, and its tally
   of severities was wrong. A figure the new read recounted is replaced.
   A figure it did not recount stays, and its record says the count ran
   on a partial index. No decision taken on those figures is reversed:
   the new counts point the same way where they were recounted.
3. **The backlog holds what stays open.** The re-audit item shrinks to
   the questions that still have no evidence, under one trigger, with
   what the read saw and nobody ruled on. Three observations take items
   of their own. Others join the items that already cover them.

Outcomes the reviewer judges, since no check can:

- Every figure is an aggregate. Nothing names the project the runs came
  from, its domain, its features or its content.
- Each result states its limits where it is recorded or by pointing at
  them: one project, one operator, one crucible version (0.33.1), the
  default role implementing, and "a later stage would have caught it"
  being a reader's judgment.
- A result is stated as strongly as its count supports and no more. A
  retirement the runs never tested is recorded as untested, not as
  holding.
- A record states its position and how it was learned; it does not
  restate procedure, and it grows by sentences, not by a section per
  result.

Premise, measured: the re-audit read the transcripts and records of 36
features of one code project over two weeks on crucible 0.33.1, 931
dispatched seats, by six reader seats on the default role and one pass on
another host. The figures cannot be reproduced from this repository: the
transcripts are not in it. The index fault is measured too: the earlier
script took dispatches from an event that repeats them without a
timestamp and overwrote the originals. No run on 0.34 or later existed
when the read ran, so nothing here measures the changes made since.

Break: none.

## Change list

- `docs/decisions/fix-verification-and-merge.md`: the verifier's runs,
  what its catches were, what it cannot see, its cost, and the ruling;
  what the runs showed of retired merge conservation.
- `docs/decisions/model-roles-and-effort.md`: the stuck trigger closed,
  with the count; what the fresh looks did.
- `docs/decisions/task-loop.md`: the stuck trigger's pointers; the fix
  ladder's and the pre-flight scan's outcomes where the loop records
  them; the `Review: branch only` mark and around-the-diff results.
- `docs/decisions/routes.md`: a lane note with a plan; what the runs
  showed after Lane Fit's shape verdict retired.
- `docs/decisions/adjudication.md`, `docs/decisions/branch-review.md`,
  `docs/decisions/terminal-pass.md`: corrected figures, and results that
  belong to each.
- `docs/decisions/shared-tree.md`, `docs/decisions/evidence-and-findings.md`,
  `docs/decisions/operator-steering.md`,
  `docs/decisions/authoring-crucible.md`,
  `docs/decisions/spec-campaign.md`: the outcome of the retirement or
  question each holds, a sentence or two; the partial-index statement
  where a figure of the earlier read stays.
- Other records citing the earlier read's figures: the partial-index
  statement by pointer, where a figure they cite came from the script
  counts.
- `docs/backlog/skill-rewrite-reaudit.md`: rewritten to what stays open.
- `docs/backlog/review-mark-overridden.md`,
  `docs/backlog/goal-check-request-file.md`,
  `docs/backlog/lane-shape.md`: new.
- `docs/backlog/review-seat-report-write.md`,
  `docs/backlog/tension-closing.md`,
  `docs/backlog/campaign-early-stop-investigation.md`: what the read
  adds to each.
- A `## Changes` line in each record whose decision or reasoning changes.

## Acceptance

1. `python -m pytest tests/` passes.
2. `git diff --name-only master...HEAD` lists only paths under `docs/`.
3. `git ls-files docs/backlog/review-mark-overridden.md
   docs/backlog/goal-check-request-file.md docs/backlog/lane-shape.md`
   prints three paths.
4. `git diff --stat master...HEAD -- docs/crucible/2026-11-19-lean-gates
   docs/crucible/2026-11-01-skill-text-rewrite` prints nothing.
5. For each of `fix-verification-and-merge`, `model-roles-and-effort`,
   `task-loop`, `routes`, `branch-review`, `terminal-pass` and
   `adjudication`, `git diff master...HEAD -- docs/decisions/<name>.md`
   adds a line beginning `- 2026-11-23:`.

## Out of scope

- Any change to skill text, templates, tests, tools or versions.
- The frozen feature folders, the lean-gates document included: their
  figures stay as written.
- Acting on what the three new backlog items observe.
- The questions the re-audit could not reach for lack of runs on 0.34 or
  later; they stay in the re-audit item.
- Building a lane note with a plan.
