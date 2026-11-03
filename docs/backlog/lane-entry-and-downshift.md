# Plans without a campaign

## Observation

- Two arrangements are unsupported (`docs/decisions/routes.md`):
  - **A campaigned spec implemented with no plan**, lane-style, once its
    campaign has stopped. Left out when the arrangement choices became
    separable (2026-10-29).
  - **A lane note with a plan.** A settled change that needs several
    tasks takes a campaign preset, folded or standard, whose campaign is
    expected to stop after its first round, because only the campaign
    presets carry a plan.

## Follow-up

- Consider implementing from a campaigned spec with no separate plan.
- Consider a lane note with a plan. Trigger: a settled multi-task change
  run through a spec campaign only to get a plan.
