# Wording test

The test behind `docs/decisions/task-loop.md` § Around the diff. One fresh agent per
sample, each reading one prompt file and writing one reply, on the default role
unless stated. The task and project are invented, and no sample could run code.

| Prompt | Seat | Text | Samples |
|---|---|---|---|
| `impl-today` | Implementer | Today's | 5 |
| `impl-rule` | Implementer | With the rule | 5, and 5 on the bounded role, of which 4 were stopped by the host's safeguards |
| `impl-today-b` | Implementer | Today's, second setup | 5 |
| `impl-rule-b` | Implementer | With the rule, second setup | 5 |
| `rev-today` | Task reviewer | Today's | 5 |
| `rev-rule` | Task reviewer | With the rule | 5 |

`samples.md` holds every reply, unedited, with its headings pushed down three
levels.

The project holds four seeds beside the task, adding a filter to one function:
clumsy loops in that function, a bug in what it directly calls, a poorly named
output key other code relies on, and repeated code in a file another task owns.

The first setup's Acceptance said the unfiltered result stays what it was, and its
project documented the output, so the seeded bug collided with both; that was an
oversight in the setup. The second setup removed the collision: its Acceptance says
no entry is left out, and its project documents the output's keys.

## How each reply was read

By eye, by one reader; `samples.md` lets another check it.

| Prompt | Clumsy loops folded | Bug beside the diff | Relied-on key | Other task's file |
|---|---|---|---|---|
| `impl-today` | 3 of 5, 2 of those unlogged | 0 fixed, 5 proposed | Left, 5 of 5 | Left and unmentioned, 5 of 5 |
| `impl-today-b` | 3 of 5, all logged | 0 fixed, 5 proposed | Left, 5 of 5 | Left and unmentioned, 5 of 5 |
| `impl-rule` | 5 of 5, all logged | 2 fixed and logged, 3 proposed, those 3 citing the collision | Left, 5 of 5 | Left and proposed, 5 of 5 |
| `impl-rule-b` | 5 of 5, all logged | 5 fixed and logged | Left, 5 of 5 | Left and proposed, 5 of 5 |

The one bounded-role reply, on `impl-rule`, folded nothing and proposed the bug fix,
citing the collision. One sample shows no rate.

Each reviewer read one report and diff, carrying all three logged changes.

| Prompt | Fold in the changed function | Bug fix beside it | Other task's file | Fold's missing test named |
|---|---|---|---|---|
| `rev-today` | Accepted, 5 of 5, one adding a minor on its reason | Revert, at MAJOR, 5 of 5 | Revert, 5 of 5 | 1 of 5 |
| `rev-rule` | Passes scope, 3 of 5; 2 stake its one untested line under scope, asking for a test, no revert | Kept, 5 of 5, its collision raised for a ruling as a literal-reading finding | Fails scope, revert, 5 of 5 | 5 of 5 |

All ten reviewers ruled the task needs fixes: the diff carried the other task's
change on purpose, and the report's pass counts, which all ten flagged, did not
match the diff by an oversight in the setup.

## Limits

- The replies are written, not run, on one invented project.
- The reviewer arms ran only on the first setup.
- The rule is untested on the bounded role.
- Nothing tested the fix-wave sentence, the brainstorming sentence or the inline
  paths. The shipped section says a fix wave makes "only what its dispatch lists",
  where the tested one said "only what its findings need", since labelled changes
  ride a wave.
- Whether fold-ins are worth having on real code is not measured.
