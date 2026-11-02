# Skills too long to survive compaction whole

## Observation

- Claude Code's "Extend Claude with skills" page, as read on 2026-10-27,
  says that after compaction the most recent invocation of each skill is
  re-attached, keeping its first 5,000 tokens, within a combined budget
  of 25,000 tokens filled from the most recently invoked skill; older
  skills can be dropped entirely.
- `skills/redteaming/SKILL.md` is about 39,000 bytes,
  `skills/subagent-driven-development/SKILL.md` about 43,900 and
  `skills/brainstorming/SKILL.md` about 22,700 (2026-11-02), roughly
  9,800, 11,000 and 5,700 tokens at four characters a token (an
  estimate, not a tokenizer count). All three are above the budget; the
  other skills are below it.
- In maintainer sessions on 2026-10-20, 2026-10-27 and 2026-10-28 the
  re-attached copy of the subagent-driven-development skill ended in a
  truncation notice after compaction.
- In a session that spanned a plugin update, compaction re-attached the
  copies of skills invoked before the update, from the old version's
  directory; invoking them again loaded the new version. A controller
  that does not notice runs the old rules.
- The router now tells an agent to invoke a skill again when its text
  came back cut short. That restores the whole text at the cost of a
  second copy in context; it does not help a skill dropped entirely, and
  whether agents follow it is unmeasured.
- Upstream met the same failure (a session that lost the fix loop's cap
  to the cut ran 18 rounds, superpowers #2481) and in v7.0.1 moved SDD's
  always-run sections into references read at their step, the fix loop's
  before every round, and added a test failing any `SKILL.md` of 20,000
  bytes or more. That is about the same line as 5,000 tokens at four
  characters a token, so the three `SKILL.md` files named earlier are over it;
  the others are under 17,500 bytes. In SDD the line falls inside the fix loop:
  Disputes and adjudication, Shared-tree rules, Drift found after the
  fact and Finish all lie past it.
- Crucible's authoring rule (`docs/decisions/authoring-crucible.md`)
  sends only route-conditional procedures to references; text every
  route runs stays in the skill. Following upstream means widening it.

## Follow-up

Bring the largest skills under the per-skill budget, moving
route-conditional text, and where the rule is widened always-run sections,
into references read at their step (`skill-text-rewrite.md`). Measure the
token counts with a tokenizer first, and check the budget against the
current Claude Code documentation. Once the skills fit, a structural test
holds each `SKILL.md` under the line, as upstream's does; the host's
compaction is its reader.
