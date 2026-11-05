Lane: very-small (operator-confirmed 2026-11-05)

# Backlog batch 9: four decisions and the record check's corrections

## Intent

Resolve four backlog items as the operator decided them, and correct what a one-off check of the 22 uncut decision records confirmed against the shipped text. No break.

- `publication-scope-and-support`: no supported host range, regressions found through use and issues, no split into a core and profiles.
- `decision-ask-framing`: a decision ask also gives the strongest case against its recommendation, as a trial. The per-round independent read and the delivery check are not built.
- `decision-records-uncut`: the bulk cut of the remaining records is retired, with a one-off repair in its place.
- `outcome-evidence`: recalibrating seat counts, the round cap and plan sizes joins `skill-rewrite-reaudit` under its trigger, reading the same runs.

## Change list

- `skills/using-crucible/SKILL.md`, § Decision asks: "with your recommendation and the strongest case against it"; `tests/prose-budget.txt` follows.
- `docs/decisions/operator-steering.md`: the clause as a trial, the deleted item's observations, the two candidates under Rejected, a Changes line. `docs/decisions/terminal-pass.md` drops its pointer to the deleted item.
- `docs/decisions/publication.md`: the support position, its Why and Rejected, a Changes line, and its pointer moved to `docs/backlog/skill-rewrite-reaudit.md`, with any outcome-review figures the record lacks. `README.md`: Claude Code tested on 2.1.318.
- `docs/backlog/skill-rewrite-reaudit.md`: takes the recalibration question.
- `docs/decisions/decision-records.md`: the bulk cut under Rejected, with the check's figures; its Why and a Changes line.
- Corrections the check confirmed by hand, clause-sized, in the records: `brainstorming-first.md` (the skip on the operator's word), `fix-verification-and-merge.md` (the report's section order, round 0's lack of a verifier, carried questions keeping their ids), `authoring-crucible.md` or the closing review (below), `model-roles-and-effort.md` (a new model name's scanner term and allowlist row), `terminal-pass.md` (a flagged Notes mismatch is a decision ask).
- The shipped sentences that share those errors: `skills/redteaming/references/merge-and-finding-hygiene.md` (the report does not open with its index), `skills/redteaming/references/fix-application.md` (round 0 takes no verifier), `skills/brainstorming/references/umbrellas.md` (the closing review's seats also read the host's dispatch reference).
- The check's nine other problems, each read by hand: a clause fix where it holds, recorded in the ledger where it does not.
- `docs/backlog/`: `publication-scope-and-support.md`, `decision-ask-framing.md`, `decision-records-uncut.md` and `outcome-evidence.md` deleted.

## Acceptance

- The four backlog files are gone and nothing outside `docs/crucible/` and the scanner corpus cites them.
- The router's decision ask reads "with your recommendation and the strongest case against it".
- `README.md` names Claude Code 2.1.318; `docs/decisions/publication.md` states that there is no supported range; `docs/backlog/skill-rewrite-reaudit.md` names plan sizes among what its audit reads.
- `merge-and-finding-hygiene.md` and `fix-verification-and-merge.md` no longer say a seat report opens with its index; `fix-application.md` no longer dispatches the verifier after every apply without excepting round 0; `umbrellas.md`'s closing review names the host's dispatch reference; `decision-records.md` rejects cutting the remaining records.
- `python -m pytest tests/` passes.

## Out of scope

- A recurring check of records against the skills.
- The three upstream statements the check could not test, for want of the upstream text at that version.
- Extending the terminal pass: its second mandate already forbids a one-sided ask.
- The options menu in `crucible:finishing-a-development-branch`.
- A wording test of the router clause: the failure is on record and the clause is a trial.
