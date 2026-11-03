# Verifier verdicts: what the repair path leaves open

## Observation

- Since 2026-11-04 an item the blind verifier finds not landed or partly
  landed, and a delta claim found FALSE, take one scoped repair and a
  re-check by whoever gave the failing verdict, in both redteam phases
  (`skills/redteaming/references/fix-application.md`;
  `docs/decisions/fix-verification-and-merge.md`). Three cases around it
  have no stated path:
  - **The re-check's report.** Where the wave's verifier gave the
    failing verdict, the re-check is the verifier's, but nothing says how
    it is dispatched or where it writes. The verifier's card names one
    report path, `round-NN/verifier.md`, and the round directory's file
    names are fixed (`skills/redteaming/references/round-record.md`),
    with none for a re-check; resuming the verifier would overwrite the
    verdicts the verifier block points to.
  - **An untraced hunk.** The verifier's nothing-outside-the-list-moved
    verdict has no next step when a diff hunk traces to no fix item, and
    the `verified` state does not wait on it.
  - **The spec campaign's terminal-pass follow-up wave.** That wave is
    verified like every wave and now takes the repair, but the
    terminal-pass record carries fields 1, 2, 6 and 8 only, with no
    verifier block, and there `verified` means `second-read.md` is on
    disk. Where that wave's verdicts and repairs are recorded is
    unstated; the gap predates the repair.

## Follow-up

- Name the re-check's dispatch (a resume of the wave's verifier) and its
  report file, and add the file to the round directory's layout.
- Decide what follows an untraced hunk: revert it, attribute it to an
  item, or the scoped repair.
- Give the terminal-pass record a verifier block, or say where its
  follow-up wave's verdicts and repairs go.
