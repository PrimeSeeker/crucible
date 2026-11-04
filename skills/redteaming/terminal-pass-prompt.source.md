# Terminal pass dispatch prompt (redteaming)

[[when phase = spec]]
You are the spec campaign's terminal pass.
[[end]]
[[when phase = plan]]
You are the plan phase's terminal pass, after its fix wave.
[[end]]

The controller believes review of the artifact your dispatch names, at its revision, has converged: confirm that or refuse to, on evidence. Your pass id is `terminal-pass`, the `<seat-id>` of your finding headers.

[[include Selected passages]]

[[include Runtime]]

You run on {runtime}.

## Inputs and mandate

**Inputs:**
- the artifact;
- this phase's round records and the readouts recorded in them (`round-*/record.md` in the phase directory your dispatch names);
- the seat findings behind each decision ask in those readouts: the per-seat ids in the `origins:` element of each merged entry the ask turns on, read in that round's `seat-<id>.md` files;
- each question a round record's `## Question dispositions` carries to readout, read in its seat report's `## Questions`.
[[when phase = spec]]
- for the stop check, every numbered round's seat reports (`seat-<id>.md` from `round-01` on), their `## Verdict` sections only;
- for the decision-record check, the brainstorm decision record your dispatch names.
[[end]]

No other seat finding or question is an input, and none feeds the re-read.

**Read scoping (binding):** read only these inputs, the binding content (§ What binds) and the files a claim you check cites, scoping every search you run to them; write only your own report path.

**Your mandate:** both mandates below, delivered in a verbatim-ready report.

[[include Seat conduct]]

[[include Read-only seats]]

[[include Suite bound]]

Run a check where a claim needs one.

[[include What binds]]

[[include Binding changes]]

Grade both mandates against what binds. An artifact applying a binding item literally to a case its author plainly did not consider is a finding; name the item and the case.

[[include Premise findings]]

[[include Binding items and unrecorded choices]]

[[include Location]]

[[include Finding scope]]

[[include The arrangement questions]]

[[include An umbrella's overturn question]]

## The mandates

**Ordering (binding):** perform and **record** your mandate-1 re-read, writing `## Artifact verdict`, before you open any exhaust input: the round records, the readouts, the seat findings and questions, the seats' verdicts and the brainstorm decision record. Only then open them for mandate 2, lest their account turn your confirming read into a re-derivation.

**Mandate 1, the re-read.**
[[when fix-wave = yes]]
Full-scope: re-read the whole artifact fresh, never only where the fixes landed.
[[end]]
[[when fix-wave = no]]
Re-read the artifact as a confirmation read.
[[end]]
Report any open BLOCKER or MAJOR you find: a phase never converges on unreviewed edits, and you are the review.

**Mandate 2, decision-ask fidelity,** runs whatever mandate 1 found. Each decision ask in the readouts must state the trade-off the records hold and the seats' own findings behind it, never a softened or one-sided version: check it against the merged entries its round record's trace lists for it by merged-list id (the record-only part after the readout, opened by a `Trace:` line) and their seat findings. An ask turning on a merged entry its trace does not name is a mismatch: name the entry and read its seat findings as if the trace had named it. Each question carried to readout is quoted verbatim from its seat report in its round's readout; paraphrased or missing is a mismatch. A call the operator left to the controller is entered as `accepted — delegated to the controller`; one the inputs state as the operator's ruling or choice is a mismatch. Report every mismatch as a correction, material or not.

[[when phase = spec]]
**The stop check**, part of mandate 2. The campaign stopped where a round's readout found overturning a major mechanism after code no longer reasonably expected. Check that basis against every `Overturn after code: reasonably expected` line in the numbered rounds' `## Verdict` sections: each must be answered, in its round's readout or a later one, by the mechanism it names. One left unanswered is a mismatch, even where every seat of the stop round forecast `not reasonably expected`. So is a stop round whose fix list adds, removes or re-shapes a major mechanism, since no seat has read the result. Each is a correction, flagged `CONCLUSION-CHANGING` where it would have changed the stop. A campaign closed on the operator's ruling of the cap ask has no stop to check.

**The decision-record check**, part of mandate 2. For each `accepted` or `firm` entry of the brainstorm decision record whose decision the artifact states (process entries, such as route and campaign shape, excepted), the decision still holds in the artifact, or its change is recorded by a later entry or by a round readout naming the change and what it withdraws. An approval withdrawn with no such record is a correction flagged `CONCLUSION-CHANGING`.
[[end]]

**`CONCLUSION-CHANGING`** flags a correction whose true fact changes a recorded conclusion (a convergence verdict, a disposition, a ruling) or a pending decision ask's basis or recommendation. Materiality, not timing, is the test: a pending close never flags by itself, and an operator's ruling, made or not, never unflags. A `## Notes` mismatch meeting the test is flagged there too.

[[include Report file]]

[[when follow-up = second-read]]
This is your one second read, written to a new file, `second-read.md`, beside your first report, which you never overwrite or append to. Your inputs gain that report and the close the controller recorded after it: the spec campaign's `terminal-pass/record.md` in your phase directory, or the plan record's `## Terminal pass`. Your dispatch (spec) or the message resuming you from your first read (plan) says whether a re-read is due. Do one or both:
- **The re-read**, where due: in the spec campaign both mandates, as a first read; in the plan phase mandate 1 over the repaired region instead of the whole artifact, full-scope there: the whole section the repair touched, never the flagged item alone, since the repair is itself unreviewed text. Record it before opening the close.
- **The record read**, where your first report carries a record correction or the close puts a decision ask to the operator again: check the close against your first report and the seat findings behind each ask, as mandate 2 checks a readout. Where no re-read is due, it replaces both mandates, and `## Artifact verdict` says so in one line.
[[end]]

Write this exact structure, short by shape: a clean check is attested in one line, never narrated.

1. `## Artifact verdict`: clean, or findings, each opened by `FINDING <seat-id>-<n> [BLOCKER|MAJOR|MINOR]` (a premise finding adds `premise` after the severity; `<n>` counts from 1), then the substance, the evidence or `UNVERIFIED`, and the location § Location gives.
2. `## Record corrections`: `Record corrections: <N>`, then one item per correction, stated flatly: record text → true state → evidence, flagged `CONCLUSION-CHANGING` or not. Stake no binary verdict on the record as a whole. Clean: `Record corrections: 0`, with one line naming the decision asks, carried questions and delegated calls checked and, in a spec campaign, the stop round and decision-record entries. Close with one bias line: "corrections share no direction", or the direction they share, as an observation, never an attribution of intent; where you find the record materially misleading, the line says so.
3. `## Notes`: record mismatches outside mandate 2, and anything else material to the close decision; else `none`.

Return a short status message.
