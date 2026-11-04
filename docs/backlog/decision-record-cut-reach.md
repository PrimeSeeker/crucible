# How far "cut when next edited" reaches in a decision record

## Observation

`docs/decisions/decision-records.md` says a record not yet cut to its short shape follows when its Decision is next edited, and `AGENTS.md` repeats it. Taken literally, a clause-sized edit to one Decision sentence requires cutting the whole record. On a 2026-11-04 lane of nine small rule changes, this would have meant cutting five records totalling about 117 KB, far more text than the lane changed. The lane left them uncut and said so in its commit; earlier lanes that day also edited uncut Decisions without cutting them, so the rule is not being followed as written.

## Follow-up

Narrow the rule so that only a real rewrite of a Decision triggers a cut, leaving a clause-sized edit alone; this is the controller's recommendation, on a call the maintainer left to the agent. The rule's reason, that restated procedure can go untrue with no test failing, stands, so the uncut records stay worth cutting on their own schedule.
