Lane: very-small (operator-confirmed 2026-11-26)

# Report file as the host rule's exception

## Intent

Seats on Claude Code read two instructions that contradict each other: the
host's notes to subagents say not to write report `.md` files and to return
findings as the final message, because the caller reads that message; every
crucible template says to write the report file, and gives the opposite
reason. Seats asked what was off in their instructions keep reporting the
clash (a redteam seat, round verifiers and a branch reviewer in one run on
0.38.0-rc.2), and in that run one blind verifier wrote no file, saying it took
the host's "Do NOT Write report/summary/findings/analysis .md files" to
override its dispatch. The two templates that answer the host at all
(verifier, re-reviewer) call its text advice, and so does the host map; it is
a prohibition.

The change frames the report file, in the one rule all seven templates take
and composed seats copy, as the exception to such a host rule, with a reason
that is true: the controller strongly prefers the file because it outlives the
controller's context (the controller does read the reply). The rule stays
runtime-neutral and conditional, since a Codex seat may get no such note
(unverified); the host's own wording is stated where host mechanics live, the
Claude Code dispatch reference. The separate "Report file required" section
the two seats take is retired as covered.

Premise: observed, not measured as an effect. The clash reports and the miss
are on record; the host's wording was quoted verbatim by a subagent on
2026-11-26. Whether the reframing reduces clash reports or misses is untested.

No break: nothing that works today stops working. The skills' word total does
not rise (the prose budget sits at its cap).

## Change list

- `skills/subagent-driven-development/references/seat-rules.md` § Report file:
  the first paragraph becomes, near this wording: "Write your report, in this
  template's structure, to the report file your dispatch names: the file is
  the deliverable. Where your host tells subagents to write no report files,
  because the caller reads only their reply, this dispatch is the exception:
  your controller strongly prefers the file, as it outlives the controller's
  context. If the host refuses the write, say so and put the full report in
  your final reply."
- Same file: delete § Report file required; drop its include from
  `skills/redteaming/verifier-prompt.source.md` and
  `skills/subagent-driven-development/re-review-prompt.source.md`.
- `skills/using-crucible/references/claude-code-dispatch.md` **Report-name
  filter**: the host's notes to subagents bar report files (in place of
  "advises ... text").
- Regenerate templates and `agents/` (`python tools/instrument_agents.py
  write`); lower `tests/prose-budget.txt` lines to the new counts.
- `docs/decisions/instruments.md`: the Decision's report-file sentence, § Why
  › Report files (what this run showed, the reframing, the retired section),
  the Rejected entry on seat-facing wording, and a `## Changes` line.
- `docs/backlog/review-seat-report-write.md`: the miss joins the count since
  2026-11-22. `docs/backlog/skill-rewrite-reaudit.md`: the expectation that
  clash reports stop once the rule gives its reason did not hold on this run.

## Acceptance

- `git grep -n -e "^## Report file required" -e "include Report file
  required" -- skills` prints nothing (exits 1).
- `python tools/instrument_agents.py check` passes.
- `python -m pytest tests/` passes, the prose budget's total at or under
  `TOTAL_CAP` unchanged.
- The Intent's outcomes (accurate attribution of the host's rule, the
  exception framing reaching all seven templates and composed seats, a true
  reason, runtime neutrality) are for the reviewer to judge.

## Out of scope

- The verifier's and re-reviewer's card line naming the file-writing tool;
  the report-name filter and its test; the controller's confirm, resume and
  save of a missing report.
- The host's own contradiction between its Notes (final message) and its
  hand-back tool (plain text not delivered): host-side.
- `TOTAL_CAP`.
