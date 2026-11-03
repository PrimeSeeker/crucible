## The plan phase

A plan gets one verification round, the single record `campaigns/plan/round-01`. The phase never loops: one fix wave at most, no round cap. A plan finding showing the spec wrong takes the flip path against it (`crucible:redteaming` § Flip paths), never another plan round; a contained amendment lands in this phase's wave (below).

**The seats.** Four roles; the pre-pass and the coherence seat(s) run in parallel against one frozen plan revision:

1. **Mechanical pre-pass** (one agent, instrument `redteam-seat`, lens text in `skills/redteaming/references/panels.md`): liveness (every declared mechanism has a producer and a consumer), ownership closure, overlap arithmetic and the set census, its supporting inputs widened to the repository's tracked text. Run it, don't read it. Its report, `campaigns/plan/round-01/seat-p0.md`, is a seat report for every purpose.
2. **Coherence seat** (instrument `redteam-seat`): one, reading spec and plan together, full-scope; two for a large plan (your call, lightly held; advisory proxy: roughly mid-teens tasks or unusually high interface density).
3. **Blind verifier** (instrument `blind-verifier`) on the fix wave, its input contract unchanged; its fix-list scope is the coherence seat's items.
4. **Terminal pass** (instrument `terminal-pass`, `phase` set `plan`): one fresh seat, after the blind verifier where a wave ran, scoped to this round, running its two mandates in their order (`skills/redteaming/terminal-pass-prompt.md`). Its report lands as `campaigns/plan/round-01/terminal-pass.md`.

Announce the phase shape (seats, lenses, dispatch count) in the phase-start readout and proceed; it is no approval gate.

**One merged wave.** Merge pre-pass and coherence findings under `crucible:redteaming` § Merge and finding hygiene; the fix list takes what `crucible:redteaming` § Fix application and blind verification states. A `deferred-to-implementation` finding's fix item lands its marker in the task that owns it (`crucible:writing-plans` § Deferring detail).

**A contained amendment**, a spec correction that `skills/redteaming/references/flip-paths.md` § The containment test finds contained, lands in the same wave as a `## Fix list` item opening `Contained amendment:`, naming the binding item and the change and, on an indented continuation line once made, the amendment commit. Its reason and why it is contained go in the ruling of the merged entry behind it, never in the item: the fix list is the blind verifier's input. The verifier sees only the item's plan-side hunks, the re-pin and any plan patch; you confirm in the `Verifier block` that the amendment commit landed. The phase readout names it among its technical calls.

**Two sanctioned repair paths, neither a loop.** A NOT-LANDED verdict permits one scoped repair edit and a re-check of that item only, by the verifier whose verdict it was. A terminal-pass finding a fix list would take takes the same path; its other MINORs take the dispositions of `crucible:redteaming` § Merge and finding hygiene. Neither path opens a wave or books a dispatch beyond its own. An item still not landed after its re-check is a decision ask.

**The second read, at most one,** follows the repair of a terminal-pass finding and, record-only, the cases `crucible:redteaming` § Stop rule and terminal pass names. Record the close under the record's `## Terminal pass` first, then resume the pass with a message setting `follow-up` to `second-read`, naming the report file `campaigns/plan/round-01/second-read.md` and whether a re-read is due; after a repair the re-read is full-scope over the repaired region, not the flagged item alone. Deliver the close and dispose of what stays open as `crucible:redteaming` § Stop rule and terminal pass states.

**The record:** the plan-phase record of `round-record.md` § Round record format, `confirmed` written last; the pass's `Record corrections: <N>` outcome goes under its `## Terminal pass`.
