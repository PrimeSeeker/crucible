# Codex controllers: how they wait on seats

## Observation

- Crucible's Codex host map says only that `wait_agent` waits for agents
  to reach a final status (`skills/using-crucible/references/codex.md`,
  **Wait**). It says nothing about the timeout to pass or what to do when
  a wait times out.
- Upstream's `codex-tools.md` (superpowers v6.3.0 to v7.0.1) treats
  `wait_agent` as an event subscription: do local work first, then wait
  in stretches of 5 to 10 minutes, list live agents after a stretch that
  times out, and never short-poll. Its basis is a reading of Codex's
  source and a corpus in which 60 to 78% of `wait_agent` calls timed out
  (superpowers' Codex efficiency spec, 2026-07-30). Neither is measured
  on crucible's controllers or on codex-cli 0.164.0.
- Codex controller cost is open elsewhere: the agent-role decision waits
  on a cost audit of Codex controllers (`docs/decisions/runtime-adapters.md`
  § Rejected).

## Follow-up

From the rollout of one Codex SDD or redteam run, count the controller's
`wait_agent` calls, their timeouts and the timeouts that ended with no
agent finished. If short timeouts recur, add the waiting rule to the
**Wait** operation in `codex.md`, stated as host mechanics.
