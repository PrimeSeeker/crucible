# Rejected machinery

## Decision

Crucible carries none of the machinery below. Each piece was built,
planned or proposed once, and each would plausibly be proposed again.

**No calibration instruments in the review loop.** No per-lens
resolution telemetry (tallies of each lens's findings applied, parked or
rejected), no seeded-defect calibration, no competitive framing of the
seats. Demoting a lens stays the maintainer's call, made from the
records (`docs/decisions/spec-campaign.md`).

**The one seeded-defect calibration ran and is discharged.** It was an
acceptance check of the first design, not a standing instrument.

**No position-swap rule.** No step compares an artifact's old and new
text side by side, so the rule that such a comparison swap the two
positions went with nothing left to govern. A step that compares them
brings the rule back.

**No config file and no optional gates.** There is no
`.crucible/config.json`, no declared optional verification gate and no
configured feature-folder root. A project changes a default through its
instruction files, which outrank the skills (`README.md`
§ Configuration). The very-small lane's `Gates:` lines record the
repository's own verification gates. Why there is no mutation gate:
`docs/decisions/test-rules.md`.

**Four rules not adopted** (2026-10-05), not to be proposed again without
new evidence: a start-and-end `git status` attestation in every
read-only seat's report, with a conservation check for it; recording a
check's result both before and after a change, with a written argument
that it is not vacuous; a fan-out procedure with a target count, a
re-run threshold of twice that count and a tiling check; a staging rule
for two sessions sharing one branch.

## Why

### Calibration instruments

The first design made per-lens resolution telemetry its validity
instrument and the input to demoting a lens (2026-08-07). Across the
nine campaigns run from 2026-08-17 to 2026-08-21, no demotion or
calibration decision was ever taken from a tally, so the telemetry
retired on 2026-08-21, with nothing in its place. Its assembler also
misread real records, but that was repairable; the reason is that
nothing used the output. (Basis: measured.)

Seeded-defect calibration and competitive framing were optional in the
first redteam design, with no procedure in the skill. Competitive
framing, telling a seat it competes with others to find more, also works
against the finding
hygiene that keeps manufactured findings out
(`docs/decisions/evidence-and-findings.md`). Both left the skill on
2026-10-09. (Basis: judgment, accepted by the maintainer.)

### The calibration that ran

On 2026-08-07 the first design gave its acceptance discriminating power:
every earlier criterion checked that the process ran, none that it
worked, so a fresh agent planted five defects in a copy of the artifact
under review and a two-seat panel had to catch at least three. It ran once, on
2026-08-08, beside round 0 of a spec campaign on another project, and
caught five of five. The maintainer settled it as discharged on
2026-10-17. Evidence on whether crucible's reviews work now comes from
the outcome review (`docs/decisions/publication.md`). (Basis: measured,
a single run; judgment, accepted by the maintainer.)

### Position swap

The first redteam design (2026-08-06) forbade comparing an artifact's
old and new text pairwise without swapping their positions, against a
judge favouring one position or the added detail. By 2026-10-13 no step
made such a comparison, and the rule went as an orphan. (Basis:
judgment, accepted by the maintainer.)

### No config file

Optional gates were declared per repository in a tracked
`.crucible/config.json` from 2026-08-21, after a standing mutation
mandate produced only per-task waiver lines, never a run, in
repositories without mutation tooling; the file could also name another
feature-folder root. No repository ever wrote it:
`git log --all -- .crucible/config.json` lists no commit in crucible's
history (re-run 2026-10-20) and listed none in the one other project
checked (2026-10-12). The root key went on 2026-10-11 and the gates on
2026-10-12; instruction files already outrank the skills, so a key
duplicated what a project can say there. (Basis: measured; judgment,
accepted by the maintainer.)

### Rules not adopted

On 2026-10-05 the maintainer reviewed four proposed rules for added
bureaucracy and ruled that only what each one's evidence supported would
land. The attestation duplicates the controller's own tree check, one
command per dispatch window instead of a section in every report
(`crucible:redteaming § Inputs and state`;
`crucible:subagent-driven-development § Shared-tree rules`). The
before-and-after record is carried by the rule that a check of a state
the change has not reached must fail on today's tree
(`crucible:redteaming § Fix application and blind verification`). The
fan-out procedure and the staging rule each rested on a single
occurrence. (Basis: judgment, accepted by the maintainer.)

## Changes

- 2026-10-17: the seeded-defect calibration, run once, discharged.
- 2026-10-13: no position-swap rule, since no step compares old and new
  text side by side.
- 2026-10-12: no config file and no optional gates; defaults change
  through a project's instruction files.
- 2026-10-09: no per-lens telemetry, seeded-defect calibration or
  competitive framing in the review loop.
- 2026-10-05: no per-report git-status attestation, two-result check
  record, fan-out procedure or two-session staging rule.
