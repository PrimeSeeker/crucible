# Whether improvements should stay out of review findings

## Observation

- Crucible's reviewers count no improvement or style preference as a
  finding: the redteam seat (`skills/redteaming/seat-prompt.md`), the
  task reviewer (`skills/subagent-driven-development/task-reviewer-prompt.md`
  § Finding Hygiene and Severity), the branch reviewer
  (`skills/requesting-code-review/code-reviewer.md` § Calibration) and
  SDD's review mandate (`skills/subagent-driven-development/SKILL.md`).
  The rule and its reasons: `docs/decisions/evidence-and-findings.md`.
- Upstream's reviewer filed code style and optimization under Minor and
  asked for recommendations. Crucible dropped the Recommendations
  section, and the upstream map lists that drop as pending on this item
  (`docs/upstream.md`).
- The maintainer called the rule probably suboptimal and worth an item
  (2026-10-20).

## Follow-up

Decide whether improvements stay out of findings, return as findings, or
get a channel of their own that costs no fix wave. Then settle the
Recommendations row in `docs/upstream.md` and update
`docs/decisions/evidence-and-findings.md`.
