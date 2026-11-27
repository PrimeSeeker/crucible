# Codex review seat: the 6.2 line untried

## Observation

- A seat on another host runs on the Codex host map's default role,
  `gpt-6.1-sol`. It is kept though Codex now labels it previous
  generation, the 6.2 line being deemed inadequate for a review-driven
  loop on first reports, pending further evidence
  (`docs/decisions/model-roles-and-effort.md`).
- Those reports are a design-gate check of sessions asked to build, and a
  roundup of users' anecdotes, in which the new line's reviews are both
  praised and called prone to scope creep
  (`docs/decisions/runtime-adapters.md` § Codex as a host). Neither
  measured a review seat.

## Follow-up

On a real redteam round 1, run the Codex seat twice from the same card,
once on each line, and compare how much of each report holds against the
files. Then move the default role, or record why it stays.
