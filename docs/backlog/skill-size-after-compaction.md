# Skills too long to survive compaction whole

## Observation

- Claude Code's "Extend Claude with skills" page, as read on 2026-10-20,
  says an invoked skill is re-attached after compaction within a budget,
  about the first 5,000 tokens of each skill. Not re-read since.
- `skills/redteaming/SKILL.md` is 5,322 words and
  `skills/subagent-driven-development/SKILL.md` 4,890, both likely above
  5,000 tokens.
- In a maintainer session on 2026-10-20, the re-attached copies of both
  skills after compaction ended in a truncation notice. The controller
  then worked from the truncated text until the skill was invoked again.
- The skills tell the controller to re-read their references after
  compaction (the dispatch reference, the route references), but not the
  skill itself.

## Follow-up

Measure each skill's token count against the budget. Then either bring
the largest skills under it, moving route-conditional text into
references read on demand, or have the skills say to re-invoke
themselves after compaction. Check the budget against the current Claude
Code documentation first.
