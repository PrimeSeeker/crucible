Lane: very-small (operator-confirmed 2026-11-05)

# A full-scope pass after a wave that changes no rule

## Intent

Settle whether a small wave needs more than its scoped re-review. It does: every wave that changes text keeps the full-scope pass after it. A skip for a wave changing no rule or behavior was built on this branch and withdrawn before landing, because each full pass found another hole in its conditions, and it would rarely apply. Record the evidence and the rejection so the question does not come back unanswered. No break.

## Change list

- Restore the skill, template, generated and budget files, and `docs/decisions/evidence-and-findings.md`, to the base.
- `docs/decisions/branch-review.md`: a Why section with the evidence and the withdrawal, Rejected entries for the skip and for counting size, and a Changes line.
- `docs/backlog/small-wave-full-pass.md` deleted.

## Acceptance

- `git diff --stat <base> HEAD -- skills agents tests docs/decisions/evidence-and-findings.md` prints nothing.
- A throwaway check script confirms the record's section, Rejected entries and Changes line, and that the backlog item is gone. It fails on the branch as it stood before this change (run once).
- `python tools/instrument_agents.py check` exits 0.
- `python -m pytest tests/` is green.

## Out of scope

Any change to the branch-review loop, the re-reviewer or the close readout; any new rule for waiving a pass.
