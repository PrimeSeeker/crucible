# Task sizing ignores implementer load

## Observation

- Measured on 2026-10-26 from the session transcripts of five consecutive
  features on one Python project, each run through brainstorming, a
  redteam campaign, a plan and subagent-driven development on an
  Opus-class default role. Cost is in input-token equivalents at list
  price ratios (cache write 1.25, cache read 0.1, output 5).
- Implementers took 53–57% of the cost in four features and 33% in the
  smallest. Cache reads were 69–79% of each feature's cost, so a session's cost is roughly turns times context and
  grows close to the square of its length.
- A single task dominated twice: one took 15% of its feature's cost
  (269 turns, average context 635k tokens, peak 954k), another 17% of
  its feature's (458 turns, average 495k, peak 966k). Most other tasks
  in the same plans stayed between 2% and 9% each.
- The first task's plan text was 663 words, inside writing-plans'
  advisory calibration ("around a page"). The plan's file-ownership
  table gave it edits in about 40 files, against 9–28 for its
  neighbours. Page length did not predict the load; the number and size
  of files the implementer had to read and change did.
- Most of that context was file reads: in the first task, 1.18M of 1.6M
  characters of tool output. Four of the features built on the same
  code, which grew 2.3× across them, so the same plan shape costs more
  with each feature that builds on it.
- Cost per changed line was flat where it could be measured (9.6–11
  units per thousand lines over three features), so the features were
  not inefficient overall. The oversized tasks are where splitting could
  save, since a session's cost grows faster than its length; that saving
  is not yet measured.
- subagent-driven-development splits a task only when its implementer
  reports BLOCKED as oversized. An implementer that finishes, however
  long it took, never triggers a split.

## Follow-up

Give writing-plans a sizing signal for implementer load: the files a task
edits and must read, with their sizes, as the ownership census already
lists them. A task far above its neighbours on that measure is split at
plan time, or the plan phase flags it. Consider whether a redteam plan
seat should check it. Measure on the next features whether the costliest
task's share falls, rather than assuming it does.
