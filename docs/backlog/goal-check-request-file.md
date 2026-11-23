# The goal check reads a request that may hold only approvals

## Observation

- A spec campaign's round-1 seats and every branch-review pass restate the
  goal from the workspace's `request.md`, which quotes the operator's
  messages that asked for the work or changed the ask
  (`docs/decisions/evidence-and-findings.md` § Premise findings, the goal
  check and questions).
- In the re-audit of 2026-11-23, over 36 features of one code project on
  crucible 0.33.1, all 85 branch-review passes ran the goal check and none
  raised a premise finding or a goal mismatch. In three features a pass
  noted that the request held only approvals, so the scope it checked came
  from the controller's summaries; another could not confirm the approach
  because the request did not say what the approved option was.
- Round-1 seats' goal checks in the same runs raised doubts that changed a
  design in several campaigns.
- No operator message after a branch review or a landing said shipped work
  missed the request.

## Follow-up

- Decide whether a goal check against a request holding only approvals is
  worth its paragraph per pass, and if not, what it would need. No fix is
  designed here.
