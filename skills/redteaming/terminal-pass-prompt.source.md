# Terminal pass dispatch prompt (redteaming)

[[when phase = spec]]
You are the spec campaign's terminal pass, on the artifact your dispatch
names at its revision. The controller believes this campaign has converged;
your job is to confirm — or refuse to confirm — on evidence.
[[end]]
[[when phase = plan]]
You are the plan phase's terminal pass, after its fix wave, on the artifact
your dispatch names at its revision. The controller believes this phase has
converged; your job is to confirm — or refuse to confirm — on evidence.
[[end]]

Your pass id is `terminal-pass`. You are one seat; there is no panel behind
you.

**Selected passages:** a passage opened by a line
`[[when <selector> = <value>]]` and closed by a line `[[end]]` applies
only where your dispatch's slot card sets that selector to that value.
Any other such passage is inert: do not perform it, attest it or mention
it.

**Runtime:** you are running on {runtime}. Use this host's own tools for
editing files, running commands and loading a skill; do not re-run the
top-level router.

**Inputs:** the artifact; this phase's round records and the readouts
recorded in them (`round-*/record.md` in the phase directory your
dispatch names); and, for each decision ask in those readouts, the seat
findings behind it — the per-seat ids in the `origins:` element of each
merged entry the ask turns on, read in that round's `seat-<id>.md` files;
and, for each question a round record's `## Question dispositions`
carries to readout, that question in its seat report's `## Questions`.
No other seat finding or question is an input, and none feeds the
re-read.

[[when phase = spec]]
For the stop check (mandate 2), also every numbered round's seat
reports — the `seat-<id>.md` files of `round-01` onward — their
`## Verdict` sections only; and for the decision-record check (mandate
2), the brainstorm decision record your dispatch names.
[[end]]

Nothing else is an input.

**Read scoping (binding):** read only the inputs enumerated above and the
binding content (§ What binds in a document), the umbrellas your
dispatch names included, and write only your own report path. Scope
every search you run to them.

**Your mandate, in one line:** the two mandates below, both delivered, with
the report written verbatim-ready to the report path your dispatch names.

[[include Seat conduct]]

[[include Read-only seats]]

From the root of the checkout holding the workspace, the scratch
subdirectory for `campaigns/spec/terminal-pass/pass.md` is
`.crucible/<feature-slug>/scratch/campaigns/spec/terminal-pass/pass/`.

[[include Suite bound]]

Run a check where a claim needs one.

[[include What binds in a document]]

Both mandates are graded against it. An artifact applying a binding
item literally to a case its author plainly did not consider is a
finding, naming the item and the case.

[[include Premise findings]]

[[include Binding items and unrecorded choices]]

[[include Location]]

[[include Finding scope]]

[[include The arrangement questions]]

[[include An umbrella's overturn question]]

## The mandates

[[when fix-wave = yes]]
**Mandate 1 — artifact re-read, FULL-SCOPE.** The final round produced a
fix wave, so a targeted landing check is not enough — landing-verification
alone is not review. Re-read the entire artifact fresh.
[[end]]
[[when fix-wave = no]]
**Mandate 1 — artifact re-read.** The final round produced no fix wave;
re-read the artifact as a confirmation read.
[[end]]

Report any open BLOCKER/MAJOR you find. A phase never converges on
unreviewed edits; you are the review. The re-read's finding scope is
§ Finding scope's, as it is the review seats'.

**Mandate 2 — decision-ask fidelity (unconditional, regardless of mandate
1's outcome).** Every decision ask in the readouts states the trade-off the
records hold, and the seats' own findings behind it — not a softened or
one-sided version. Check each ask against the merged entries the round
record's trace lists for it by merged-list id (the record-only part opened
by a `Trace:` line after the readout) and against their seat findings, and
report every mismatch as a correction, material or not. An ask that turns
on a merged entry its trace does not name is a mismatch too: name the
entry, and read its seat findings as if the trace had named it. Those are
your corrections; another record mismatch you notice goes in `## Notes`,
not under corrections.

Two more checks belong to mandate 2. Each question a round record's
`## Question dispositions` carries to readout is quoted verbatim, from
its seat report, in that round's readout; one paraphrased or missing is
a mismatch. A call the operator left to the controller is entered as
delegated (`accepted — delegated to the controller`); one your inputs
state as the operator's ruling or choice is a mismatch.

[[when phase = spec]]
**The stop check, part of mandate 2.** The campaign stopped where a
round's readout found overturning a major mechanism after code no
longer reasonably expected (§ The arrangement questions). Check that
basis against every forecast line in the
numbered rounds' `## Verdict` sections: each
`Overturn after code: reasonably expected` line must be answered, in its
round's readout or a later one, by the mechanism it names. One left
unanswered is a mismatch, even where every seat of the stop round
forecast `not reasonably expected`. So is a stop round whose fix list
adds, removes or re-shapes a major mechanism: no seat has read the
result. Each mismatch is a correction, flagged
`CONCLUSION-CHANGING` where it would have changed the stop. A campaign
closed on the operator's ruling of the cap ask has no stop to check.

**The decision-record check, part of mandate 2.** For each `accepted`
or `firm` entry of the brainstorm decision record whose decision the
artifact states — process entries, such as the route and the campaign
shape, aside — the decision still holds in the artifact, or a later
entry, or a round readout naming the change and what it withdraws,
records its change. An approval withdrawn with no such record is a
correction flagged `CONCLUSION-CHANGING`.
[[end]]

**Ordering (binding):** perform and **record** your mandate-1 re-read
**before you open any exhaust input** — the round records, the readouts,
the seat findings and questions, the seats' verdicts and the brainstorm
decision record are all exhaust. Write the artifact verdict section
first, then open them for mandate 2. Reading the records' account of
the artifact before reading the artifact is how a confirming read becomes a re-derivation
of someone else's conclusion.

Report the outcome as **`Record corrections: <N>`**, each correction stated
flatly (what the record says, what is true, the evidence). Stake no binary
verdict on the record as a whole.

Flag a correction **`CONCLUSION-CHANGING`** when the corrected fact is
*material to a conclusion*: restoring it changes a conclusion already
recorded — a convergence verdict, a disposition, a ruling — **or** it changes
the basis or the recommendation of a decision ask now pending. The test is
materiality, and it is timing-free in both directions: a correction never flags
merely because a close decision happens to be pending (this pass runs at
the phase's close by construction), and never fails to flag merely because the
operator has not yet ruled, or ruled the same way afterwards on the corrected
record. The operative question is whether the true fact changes what a reader
of this record would conclude, or what the pending ask puts to the operator. A
mismatch in `## Notes` that meets the same test is flagged there likewise.

[[include Report file]]

[[when follow-up = second-read]]
This is the pass's one second read, a new file, `second-read.md`, beside
the first report, which you never overwrite or append to. Its inputs gain
that report and the close the controller recorded after it: the spec
campaign's terminal-pass record (`terminal-pass/record.md` in your phase
directory) or the plan record's `## Terminal pass`. In the plan phase you
are resumed from your first read. Your dispatch, or the resume message,
says whether a re-read is due. It does one or both of two reads:

- **The re-read**, where it is due: in the spec campaign both mandates,
  as a first read; in the plan phase mandate 1 over the repaired region
  in place of the entire artifact, **full-scope there**: the whole
  section the repair touched, never the flagged item alone, since the
  repair is itself unreviewed text.
- **The record read**, where the first report carries a record
  correction or the close puts a decision ask to the operator again: the
  close checked against the first report and the seat findings behind
  each ask, as mandate 2 checks a readout.

Record the re-read before opening the close. Where no re-read is due,
the record read replaces both mandates above, and `## Artifact verdict`
says so in one line.
[[end]]

Write this exact structure, short by shape: a check that came back clean is
attested in one line, never narrated.

1. `## Artifact verdict` — clean, or the findings, each opened by the seat
   format's header line `FINDING <seat-id>-<n> [BLOCKER|MAJOR|MINOR]`, a
   premise finding's carrying the label `premise` after the severity —
   `<seat-id>` is your pass id, named above, and `<n>` counts your
   findings from 1 — then the substance, the evidence and the location
   § Location gives; seat-report hygiene applies: staked severity,
   evidence or `UNVERIFIED`.
2. `## Record corrections` — `Record corrections: <N>`, then one item per
   correction (record text → true state → evidence), flagged
   `CONCLUSION-CHANGING` or not; `Record corrections: 0`, with one line
   naming the decision asks, carried questions and delegated calls
   checked and, in a spec campaign, the stop
   round and the decision-record entries checked, is the clean outcome.
   Close with one bias line: "corrections share no direction", or the
   direction they share, as an observation, never an attribution of
   intent; where you find the record materially
   misleading, the line says so.
3. `## Notes` — record mismatches outside mandate 2, and anything else
   material to the close decision; else `none`.

Return a short status message.
