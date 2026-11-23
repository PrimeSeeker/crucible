# Nothing notices a lane outgrowing the lane

## Observation

- Lane Fit's shape verdict retired on 2026-11-02, leaving one stop-and-ask
  line, which the controller raises on a reviewer's finding or question or
  its own reading (`docs/decisions/routes.md` § The very-small lane).
- In the re-audit of 2026-11-23, over 36 features of one code project on
  crucible 0.33.1, 13 features ran on the lane. Two outgrew it, judged by
  passes, waves and severity: one drew a BLOCKER and two MAJORs at its first
  full-scope pass and ran four waves, one of whose tests overwrote live
  state on the operator's machine; the other ran five passes and four waves
  on one recurring class of finding. Neither was raised as a shape problem,
  the stop-and-ask line was never used, and both landed on the lane, the
  operator approving or delegating the waves past the cap.
- The lane's first reviewed ranges ran from 4 to 34 files; one grew from 10
  files to 16 and over 2,000 added lines, more lines than one folded
  feature's whole range. The 13 lane features drew 7 of the 10 BLOCKERs and MAJORs the
  branch reviews raised, in 3 features.

## Follow-up

- Decide whether the lane needs something that notices a change outgrowing
  it, and on what signal; the two sightings are one reader's judgment. No
  fix is designed here.
