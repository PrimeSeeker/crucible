# Decision records not yet cut

## Observation

Twenty-two of the 30 records in `docs/decisions/` have not been cut to positions and pointers: about 78 KB of Decision text. `docs/decisions/decision-records.md` now cuts a position only when an edit rewrites it, so nothing brings these records to that shape on any schedule, and their restated procedure can go untrue with no test failing.

## Follow-up

Cut them in a lane of their own once that is worth its review, the records restating most first, as the first cut did (`docs/decisions/decision-records.md` § A Decision points at procedure); or retire the goal if the restatements are not going untrue in practice.
