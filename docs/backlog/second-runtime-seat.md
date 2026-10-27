# An opt-in cross-family (second runtime) redteam seat

## Observation

- Every campaign panel runs on one host's model family. The self-preference
  bias of a single-family panel is an accepted, documented risk, with a
  revisit trigger of a working cross-runtime path. Crucible now meets that
  trigger on the mechanism side only: Codex is a host runtime, but no panel
  is composed across runtimes, and no skill text mentions cross-runtime or
  cross-family seats.
- The redteaming skill crucible grew from said: "Bring in a second runtime
  (e.g. Codex) **only when the user asks.** A non-native runtime's
  false-positive rate is typically higher, so always verify its findings
  against the real files." Crucible's first design deferred such seats "on
  plumbing, not on measured value", noting that the record held at least
  one cross-runtime BLOCKER catch the single-family panel missed.
- A user whose instructions ask for a second runtime in every redteam
  gets no path for it from crucible.
- One audit of crucible ran a Codex seat beside the native panel: it found
  nothing the others missed but independently converged on the top
  findings; about half its claims verified only partly, mostly on
  attribution (inherited upstream text presented as crucible's own).

## Follow-up

- Introduce it properly, as a feature of its own.
- Design the opt-in seat: how its report enters seat records and
  `conserve`, verification against the files, quota and time-box
  discipline.
- Record the decision on the single-family panel's bias risk.
