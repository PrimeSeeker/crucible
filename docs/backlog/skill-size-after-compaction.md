# Skills too long to survive compaction whole

## Observation

- Claude Code's "Extend Claude with skills" page, as read on 2026-10-27,
  says that after compaction the most recent invocation of each skill is
  re-attached, keeping its first 5,000 tokens, within a combined budget
  of 25,000 tokens filled from the most recently invoked skill; older
  skills can be dropped entirely.
- `skills/redteaming/SKILL.md` is about 33,700 characters and
  `skills/subagent-driven-development/SKILL.md` about 31,200, roughly
  8,400 and 7,800 tokens at four characters a token (an estimate, not a
  tokenizer count). Both are above the budget; the other skills are
  below it.
- In maintainer sessions on 2026-10-20 and 2026-10-27 the re-attached
  copy of the subagent-driven-development skill ended in a truncation
  notice after compaction.
- The router now tells an agent to invoke a skill again when its text
  came back cut short. That restores the whole text at the cost of a
  second copy in context; it does not help a skill dropped entirely, and
  whether agents follow it is unmeasured.

## Follow-up

Bring the largest skills under the per-skill budget, moving
route-conditional text into references read on demand
(`skill-text-rewrite.md`). Measure the token counts with a tokenizer
first, and check the budget against the current Claude Code
documentation.
