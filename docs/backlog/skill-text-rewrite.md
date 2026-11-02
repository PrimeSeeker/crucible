# Skill text rewrite: what stays open

## Observation

- **Resident cost.** A measurement on one project's very large features
  put skill prose resident in controllers at about 5% of their spend
  (subagents 0.2%), and a full rewrite of the controller skills was
  declined then, with a re-open trigger: skill prose above about 10% of
  controller spend in a later measurement, or a rule change that has to
  land in a trimmed router or adapter with no headroom left. On a small
  project a redteam controller loaded the redteaming skill plus
  `formats.md`, about 27K tokens, before any work, so the trigger likely
  trips there. Cost was measured in tokens, not duties or adherence.
- **Separability of review before code and plan form.** An audit of the
  hypothesis-specs umbrella's three features (2026-10-29) found that the
  route presets treat review before code and the plan's form as separate
  choices, while a feature's spec is always campaigned and a note never
  is.
- **How a tension gets closed.** A tension a review finds is closed
  today by adding a distinction. For a fix-list clause asking whether a
  removing or merging resolution exists, the maintainer agreed it looked
  weak and deferred the restructuring ("probably later").
- **Two rule gaps:**
  - when the operator answers the after-three-waves ask with another
    approach by a plan change rather than a revert, nothing says what
    happens to the task's open findings: its latest line stays
    `fix wave 3/3`, and the resume rule sends it to an ask already
    answered;
  - the plan phase's close after an upgrade hatch seeds every unruled
    lane lead as `Lane: lead (concern):`, whatever its kind, so the
    branch reviewer cannot rule a carried question or proposal
    RECOMMENDED.
- **Umbrella landings.** Whether a clause-sized binding change to an
  umbrella entry needs a landing of its own on the base branch first:
  one feature needed two such landings for one-clause edits.
- **A review missing a verdict.** `crucible:subagent-driven-development`
  § The Task Loop says never to accept a review report missing any
  verdict, and `crucible:requesting-code-review` sends its two cases (a
  pass leaving a lead it was handed unruled, a re-review leaving a
  fix-report concern unruled) there for the action; neither says what
  the controller then does: resume the seat for the verdict, dispatch a
  fresh one, or rule itself.

## Follow-up

- `compaction-fit`: restate the resident-cost re-open trigger as
  resident tokens per route, or retire it.
- Weigh the separability point and the tension-closing restructuring as
  design targets of a later rewrite.
- Fill the two rule gaps and state the action on a review missing a
  verdict, each in the skill that owns the step.
- The umbrella-landing question: weigh it when the umbrella procedure is
  next edited.
