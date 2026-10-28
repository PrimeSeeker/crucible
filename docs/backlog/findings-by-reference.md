# Fix-wave prompts copy findings verbatim

## Observation

The re-review card's `[FINDINGS]` slot and the fix dispatch's
`[CONTEXT]` take findings verbatim from the review that raised them, so
a controller copies each wave's findings into two or three prompts,
and every copy stays in its context for the rest of the session. The
findings already sit in a report file the seats can read.

## Follow-up

Pass findings by reference: the report file's path and the finding ids,
with the seat reading the bodies itself. Check first that the verbatim
copy is not what keeps a seat from re-grading or narrowing a finding.
