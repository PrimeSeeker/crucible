# Cross-skill anchor citations outrun the frozen-target list

## Observation

- `docs/authoring.md` § Reference convention, class 3, sanctions the form
  `crucible:<skill> § <exact full heading text>` only for the headings
  § Anchor stability names as frozen citation targets. That section names
  one skill heading: `Operating stance — baseline error rate` in
  `skills/redteaming/SKILL.md`.
- The skills use the form far more widely: `git grep -hoE
  'crucible:[a-z-]+`? § ' -- skills | wc -l` counts 43, one of them the
  named target. The others cite headings in redteaming,
  subagent-driven-development and brainstorming, such as § Merge and
  finding hygiene, § Round readout, § Panels, § Finish and § The
  very-small lane.
- The reference scanner (`tests/test_references.py`, check 6) already
  fails the suite when a cited heading does not exist, listed or not. A
  rename of an unlisted heading therefore breaks the build rather than
  leaving a dangling citation; what the class-3 restriction adds is that
  the rename counts as an interface change to plan, not an edit.

## Follow-up

- Either widen § Anchor stability to the headings the skills cite (or to
  every `##` heading of a SKILL.md), or retire the class-3 restriction and
  let the scanner's check be the guard. Then make `docs/authoring.md` and
  the skills agree.
- If the list is widened, decide whether a test keeps it in step with the
  citations.
