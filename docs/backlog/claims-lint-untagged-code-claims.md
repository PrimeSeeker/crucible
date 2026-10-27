# A claims lint for untagged code-shaped claims

## Observation

Crucible's evidence rules are prose only: a spec, plan, fix list, readout
or implementer report that states something mechanically checkable about
code, files or tool behaviour carries its evidence or the tag
`UNVERIFIED`. Mechanical enforcement was a deliberate non-goal when those
rules shipped: a lint built before the rules are seen eroding spends the
effort on a problem that may not exist.

## Follow-up

Conditional, not scheduled. Open this item only if the prose rules are
seen eroding: a campaign or a first use in which such text again carries
checkable claims about code, files or tool behaviour that were neither
verified when written nor tagged `UNVERIFIED`.

Then design a check that flags a line asserting something mechanically
checkable about code without evidence beside it and without an
`UNVERIFIED` tag. It should scan lines rather than model a document's
structure. Undecided: its host (crucible has no summary step or committed
summary for it to join), the corpus, its severity (advisory or blocking),
the false-positive budget, and whether a line scan can be made precise
enough to be worth its noise.
