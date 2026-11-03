# Skill copies after compaction: stale or dropped

## Observation

- In a session that spanned a plugin update, compaction re-attached the
  copies of skills invoked before the update, from the old version's
  directory; invoking them again loaded the new version. A controller
  that does not notice runs the old rules. Seen again in a maintainer
  session on 2026-11-03: copies from 0.13.0 and 0.12.0 re-attached under
  0.14.0.
- Claude Code's "Extend Claude with skills" page (read 2026-11-03) says
  the re-attached skills share a combined budget of 25,000 tokens,
  filled from the most recently invoked skill, so an older skill can be
  dropped entirely; upstream's issue #2481 (obra/superpowers) records
  one. The router's line on a skill whose text came back cut short does
  not fire for a skill that did not come back at all. With every
  `SKILL.md` under the compaction line (`tests/test_skill_size.py`),
  about five skills fit the budget, which makes a drop rarer, not
  impossible.

## Follow-up

Find a signal a controller can act on for each: a re-attached skill from
an older version than the installed one, and a skill invoked before
compaction that did not come back. Either would be invoked again, as a
cut copy is.
