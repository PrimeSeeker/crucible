## The plan phase — one verification round

A plan gets **one verification round**, recorded as the single record `campaigns/plan/round-01` — no plan `round-00`, no plan `terminal-pass/`. The phase **never loops**: one fix wave at most, no round cap, no cap arithmetic. A plan finding that shows the spec wrong takes the flip path against the spec (`crucible:redteaming` § Flip paths — load-bearing content mid-campaign or mid-execution), never another plan round; a contained amendment lands in this phase's wave (below).

**The seats.** Four dispatches; the pre-pass and the coherence seat(s) run in parallel against one frozen plan revision:

1. **Mechanical pre-pass** (one agent, instrument `redteam-seat`): liveness (every declared mechanism has a producer and a consumer), ownership closure and the overlap arithmetic — **run it, don't read it**. Its report, `campaigns/plan/round-01/seat-p0.md`, is a seat report wherever seat reports count, so it carries `## Index`, `## Findings` and `## Questions` like any seat's; its arithmetic goes in `## Worksheet`, before `## Findings` (slot card `worksheet` selector `pre-pass`).
2. **Coherence seat** (instrument `redteam-seat`) — one, reading spec and plan **together**, full-scope; **two for a large plan** (your judgment, lightly held; roughly mid-teens tasks or unusually high interface density is the advisory proxy).
3. **Blind verifier** (instrument `blind-verifier`) on the fix wave, under its unchanged input contract; its fix-list scope is the coherence seat's items.
4. **Terminal pass** (instrument `terminal-pass`, `phase` set `plan`) — one fresh seat after the fix wave, scoped to this single round.

**Every dispatch follows `crucible:redteaming` § Panels and § Dispatch composition** — model, effort, roster and filled slot card — and the tree check in `crucible:redteaming` § Inputs and state. **Announce the phase shape** — seats, lenses, dispatch count — in the phase-start readout and proceed; the announcement is not an approval gate.

**One merged wave.** Pre-pass and coherence findings are merged under the spec campaign's finding hygiene, disposition and merge-conservation rules. A fix item for a `deferred-to-implementation` finding lands its marker in the plan and appends that marker's routing-table rows — one per owning task, the source cell naming the plan site, owner assigned — so the close seeds them like any other row.

**A contained amendment** — a correction to the spec that `skills/redteaming/references/flip-paths.md` § The containment test finds contained — lands in the same wave as an item of the record's `## Fix list` opening `Contained amendment:`, naming the binding item, the change and its reason, why it is contained, and, on an indented continuation line once it is made, the amendment commit. The phase readout names it among its technical calls.

**Post-wave verification, in order:** you re-run the pre-pass's liveness, ownership and overlap arithmetic over the amended plan yourself, booking no dispatch, and record it in the `Verifier block`; the blind verifier checks the wave; then the terminal pass performs its two mandates under their ordering (`skills/redteaming/terminal-pass-prompt.md`).

**Two sanctioned repair paths, neither a loop.** A NOT-LANDED verdict permits **one scoped repair edit** and a re-check **of that item only**, by the verifier whose verdict it was — never a new wave. A terminal-pass finding takes the same path, then the pass's **second read**: resume that pass with a message setting its `follow-up` selector to `second-read` and naming a new report file, `campaigns/plan/round-01/second-read.md`; it re-reads **full-scope over the repaired region**, not the flagged item alone. After a repair on either path, re-run the arithmetic over the repaired plan yourself, again booking no dispatch. Anything still open goes to the operator as a **decision ask**. Neither path opens a wave or books a dispatch beyond its own.

**Dispatch arithmetic:** at most 4 (pre-pass, coherence seat, blind verifier, terminal pass), 5 with two coherence seats, plus one per repair path taken — up to two.

**A degraded round is not a loop:** a lost seat is re-dispatched under the host-confirmed top-up rule (`crucible:redteaming` § Panels); the quorum block is kept for lost seats, and cap arithmetic does not apply.

**The record.** One record, the plan-phase record of `formats.md` § Round record format, its states running through `confirmed`, written last. The terminal pass's report lands as `campaigns/plan/round-01/terminal-pass.md` and its second read as `second-read.md`; the pass's `Record corrections: <N>` outcome goes under the record's `## Terminal pass`.

**Close.** After the terminal pass and any repair, and before the handoff, **seed the SDD ledger's deferred list from the plan's deferred-items routing table** — one entry per row, carrying the item's id, its one-line intent and its owning task — and **seed each `Contained amendment:` item of the fix list under the ledger's `## Adjudication rulings`** as one of your own rulings, in that item's form.
