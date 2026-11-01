Lane: very-small (operator-confirmed 2026-11-01)

This note applies its own rule early: the request that asked for it is
quoted in the feature's workspace, not here (operator-approved departure
from the installed `## Request` requirement).

## Intent

The operator's messages asking for a feature must not reach committed
text: crucible's feature folders are committed and often pushed, so
quoting the request there publishes private conversation in every
project that runs crucible. The request moves into the feature's
uncommitted workspace; seats still run the goal check against it.

## Change list

- Spec contract, folded document, lane note, umbrella shape: drop the
  `## Request` section and the redaction rule. Committed text states the
  goal in its own words and quotes no message from the operator.
- Workspace layout and provisioning: `<workspace>/request.md`, written
  at brainstorm exit with the quoted messages; later messages that change
  the ask are appended while the workspace lives; it is deleted with the
  workspace.
- Goal check (`premise-and-questions.md`) and premise findings: read the
  request from the file the dispatch names; with none, say it was
  unavailable. An umbrella child checks against its own request, the
  umbrella's Intent and its own entry; the closing review reads fidelity
  to the umbrella's Intent.
- Seat dispatch: redteam seat, branch reviewer (the very-small lane's
  Lane Fit included) and closing-review seats get the request path in
  their read scope; regenerate `agents/`.
- Decision records (`the-spec`, `evidence-and-findings`, `umbrellas`,
  `routes`, `records-and-workspace`): current position plus Changes
  lines. Remove the request-block entry from
  `docs/backlog/skill-text-rewrite.md`. Update `tests/prose-budget.txt`.

## Acceptance

- `grep -rn "## Request\|redacted:" skills agents` finds nothing
  (one-time; it hits today in `brainstorming/SKILL.md`, `seat-prompt.md`,
  `premise-and-questions.md`, `agents/redteam-seat.md`).
- The workspace layout in `formats.md` lists `request.md` (one-time).
- `python -m pytest tests/` passes, including the agents check and the
  prose budget.

## Out of scope

Editing shipped specs or git history; pointing seats at transcripts; how
open items and backlog entries cite their sources.
