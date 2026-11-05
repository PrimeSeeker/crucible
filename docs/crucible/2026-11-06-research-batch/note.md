Lane: very-small (operator-confirmed 2026-11-06)

# Research batch: controller cost, reviewers' reach, campaign rounds

## Intent

Record what the transcripts on disk show on three backlog items, and resolve what they answer. No break; nothing shipped behaves differently.

- `nested-orchestration`: not worth building, since the most it could save is about 8% of a run, before overhead, and a nested controller can't reach the operator. The Codex half stays unmeasured and is dropped, saying so.
- `reviewer-research-reach`: reads do go beyond the stated scope, and they carry findings, so no scope tightens and no template changes. The methods follow-up is closed as overtaken; the model comparison is recorded as thin.
- `campaign-early-stop-investigation`: multi-round campaigns are not shown net-positive, and this design can't show it either way. The rule and the cap stay, and only the cap experiment remains open.

## Change list

- `docs/decisions/spec-campaign.md`: the campaign figures with their limits, the Codex comparison, a Changes line; its "stay open" sentence narrows to the cap.
- `docs/decisions/model-roles-and-effort.md`: the controller's cost share, the implementers' cost share and the Fable comparison in Why, the nested controller under Rejected, a Changes line.
- `docs/decisions/instruments.md`: the reach figures in Why, a Changes line.
- `docs/upstream.md`: its row points at the record.
- `docs/backlog/`: `nested-orchestration.md` and `reviewer-research-reach.md` deleted; `campaign-early-stop-investigation.md` cut to the cap experiment. Observations no record holds move to the matching record first.

## Acceptance

- The two deleted files are gone, and nothing outside `docs/crucible/` cites them.
- `campaign-early-stop-investigation.md` no longer contains "net-positive", "drift reducers" or "outcome record", and still names the fresh-panel round.
- All three records carry a `2026-11-06` Changes line, and `spec-campaign.md` no longer says whether a campaign is net-positive "stay[s] open".
- The branch reviewer re-runs the research scripts and every recorded figure matches that run.
- Nothing changes under `skills/`, `agents/`, `hooks/`, `tools/` or `tests/`.
- `python -m pytest tests/` passes.

## Out of scope

- Rewording the seat scope sentence, and a new outcome record.
- Measuring the Codex controller, and reading the audit report's method section.
- Committing the scripts: they name another project, so they stay in the session's scratchpad and the records describe the method in words.
- A release.
