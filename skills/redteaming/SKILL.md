---
name: redteaming
description: Use on a just-written spec or plan, before accepting it.
---

# Redteaming — review controller

## Overview

You are the review **controller**. A **spec campaign** is an iterated loop: dispatch a panel of fresh-context review seats at one artifact, merge their findings, apply fixes, verify them blind, read out to the operator, and repeat until the stop rule says converged — then run the terminal pass and hand off. Every step writes records; every judgment is computed from the records, never from conversation memory.

**A plan is not campaigned**: it gets the **plan phase** (§ The plan phase — one verification round), which reuses the dispatch composition, the merge and finding-hygiene rules, and the readout; everything from § Round 0 to § Stop rule and terminal pass describes the spec campaign except where it says otherwise.

**The operator steers through decision asks without being required to read the artifact.** That is why the readouts exist and why the terminal pass checks each ask's fidelity to the findings behind it.

**Scope:** the panel apparatus exists for specs and plans, nothing else. Open-ended project-wide issue-mining is out of scope and gets its own framing. Whole-branch review of implemented code is not a campaign either; it is `crucible:requesting-code-review`'s.

**Announce at start:** "I'm using the crucible:redteaming skill to run the spec campaign." — or "… to run the plan phase."

**Dispatch references:** when this skill starts, and again after compaction, read from the plugin root `skills/subagent-driven-development/references/dispatch-composition.md`, the rules every dispatch shares, and your adapter's `skills/using-crucible/references/<runtime>-dispatch.md`; both bind as if written here.

**Stubs.** Where a section names a reference to read in full, read it when the section's step comes; it binds as if written here. After compaction, re-read the reference of the step in progress before you act, and each other one only when its step next comes.

## Inputs and state

- **The artifact**: one spec or one plan, at a fixed path and revision. Every seat in a round reads that one revision.
- **The feature workspace**: `<repo>/.crucible/<feature-slug>/`, provisioned at brainstorm exit (if missing: the provisioning step in `formats.md` § Feature workspace root and layout). Records live under its `campaigns/spec/` or `campaigns/plan/`.
- **The formats contract**: `skills/redteaming/references/formats.md` defines the workspace layout, the round record, the state vocabulary, the special records and the feature folder; records are composed by plain path-join from the repo root. If this skill and that file conflict, stop and report BLOCKED — never improvise a format.

**Round records and state lines** (producer: you, at each phase boundary; consumers: your rehydration, the stop rule, the blind verifier, the terminal pass): each `round-NN/record.md` carries a `state:` line, each state written only after its phase's outputs are on disk (`formats.md` § Round record format, field 2). **Rehydration:** after compaction, resume from the workspace — the current round is the highest record number, and its state line says where to pick up; a fix list recorded while state is short of `fix-applied` is re-checked item by item against the artifact before any re-apply. A resume at `state: readout` delivers the recorded readout again, without its trace; re-delivering a readout is harmless. In the plan phase or on the folded lane, re-read that route's reference first (§ The plan phase — one verification round, § The folded lane).

**Artifact freeze** (binding): the artifact is never edited while any seat, verifier or pass is reading it — fixes land between dispatches.

**Shared tree** (binding): `skills/subagent-driven-development/references/dispatch-composition.md` § Shared-tree rules bind every seat you start. The status check runs after every dispatch window — panel seats (one window per concurrent batch), the round-0 pre-pass, the blind verifier, the terminal pass, and the plan phase's pre-pass and coherence seats — each dispatched with your fixes committed. Your fix apply lands between windows, never inside one.

## Dispatch composition

Every seat you start — panel seat, round-0 pre-pass, blind verifier, terminal pass, and the plan phase's mechanical pre-pass and coherence seat — carries the seven-item dispatch composition in `skills/subagent-driven-development/references/dispatch-composition.md`. Its input paths are the artifact at its revision, the workspace paths its inputs live at, the supporting inputs its card lists, the umbrellas up the chain where the binding artifact's preamble carries an `Umbrella:` line (every seat but the blind verifier; that file's item 2) and, for the blind verifier, the tracked files a delta claim names; nothing else. The round-0 pre-pass is the one controller-composed dispatch here. **The binding pointer** differs for these seats: where the artifact under review is a **plan**, it is the spec the plan's header names, and the **blind verifier gets none**: the fix list is its whole normative input, and anything more destroys its blindness.

**Seat models:** every dispatch runs on the default role but one: **the blind verifier runs on the bounded role** and never lower — checking a fix list against a diff is a bounded task, and its mandate is unchanged by the tier. Round 1's swap to the alternate role is § Panels'. The roles, the alternate role's other triggers, model naming and effort follow `skills/subagent-driven-development/references/dispatch-composition.md` § Models and effort.

**Dispatching an instrument.** Three seats are instruments, each with a slot card beside its template: instrument `redteam-seat` (`seat-prompt.md`, `seat-prompt.slots.md`), instrument `blind-verifier` (`verifier-prompt.md`, `verifier-prompt.slots.md`) and instrument `terminal-pass` (`terminal-pass-prompt.md`, `terminal-pass-prompt.slots.md`). Fill the card as `skills/subagent-driven-development/references/dispatch-composition.md` § Filling a card states.

## Round 0 — mechanical pre-pass

On **every** spec campaign, before any panel, dispatch one standalone agent to produce a claim table — every "the code does X" claim, or with no code baseline every claim about the artifact's inputs (the request, the decision record, the documents it cites), → TRUE/FALSE with evidence — plus a liveness check (every declared mechanism has a producer and a consumer within the artifact) and execution of regex/CLI claims (run them, don't read them). Its prompt carries § Suite bound, copied from `skills/subagent-driven-development/references/seat-rules.md`; the scratch line, that code it runs goes under the workspace's `scratch/campaigns/spec/round-00/`, never the tracked tree; and a staked severity on each finding, which decides what its fix list takes (§ Fix application and blind verification). Record it as `round-00/` per the formats reference and apply its fix list before round 1. **No dedicated verifier for round 0** — the round-1 panel's full-scope read is the check on those fixes.

## Panels

**Before you size, staff or dispatch any panel round or plan-phase seat, and whenever a dispatched seat is lost, read `skills/redteaming/references/panels.md` in full.** A degraded round never counts toward convergence and does not consume the cap; **two consecutive degraded rounds = infrastructure escalation to the operator**.

## Merge and finding hygiene

**Whenever you merge seat reports or disposition a finding or question, read `skills/redteaming/references/merge-and-finding-hygiene.md` in full.** **Record hygiene** (the seat rule of finding hygiene, turned on the records and readouts *you* author): a code-shaped claim in a fix list, a merged entry, a ruling, a verification outcome, a readout or a decision ask shows its evidence — what you read or ran — or carries `UNVERIFIED`, and that tag is the whole vocabulary here. It tags a *claim*; it never admits an `UNVERIFIED` *finding* to a fix list. A decision ask resting on an untagged unverified mechanical fact is a defect in the ask.

### Operating stance — baseline error rate

A baseline defect rate in controller-authored text is a design assumption of this process; blind verification and the terminal pass are budgeted for it. A caught error is the loop functioning, not a verdict on the author: report errors, your own included, in the flat register of any other finding — the fact, the correction, the consequence — editorializing about no one.

Because the rate is expected and non-punitive, disclosure against interest stays cheap — shading a record, not erring in it, is the only reportable failure *of the reporting duty itself*; every other reporting obligation in this skill stands unchanged, and this stance may never be cited to skip, soften, or summarize any of them.

## Fix application and blind verification

**Whenever you judge which findings a fix list takes, or write, apply or verify a fix list or a repair edit, read `skills/redteaming/references/fix-application.md` in full.** You and fix waves consult the right-sizing seats' over-subtraction attestations before applying any cut — cutting attested content requires a logged ruling in the round record.

## Round readout

**At every round and campaign close, for any other readout that puts decision asks to the operator and points here, and whenever an operator ruling or a record correction arrives after a round closed, read `skills/redteaming/references/round-readout.md` in full.**

## Stop rule and terminal pass

**Stop trigger: the first numbered panel round after which overturning a major mechanism after code is no longer reasonably expected** — the overturn question, defined with its reading for an umbrella's campaign in `skills/subagent-driven-development/references/seat-rules.md` § The arrangement questions. The answer is **your judgment over the round's records** — its merged list, its fix list and the seats' forecast lines in their reports' `## Verdict` sections — never a mechanical threshold and never conversation memory. Severity is not the trigger: a BLOCKER that would overturn a mechanism keeps the campaign going by the question itself. Finding provenance and finding counts are not signals. **A round whose own fix wave adds, removes or re-shapes a major mechanism is never the stop round**: no seat has read the result. Recording a deferral never re-shapes one; the binding outcome a deferral's item lands is judged like any other edit. Once a campaign is chosen, at least one numbered panel round runs. **A premise finding is a decision ask, never an open finding anywhere in this section** (`skills/redteaming/references/flip-paths.md` § Premise findings).

The stop round's open findings a fix list takes (§ Fix application and blind verification) get that round's **one fix wave + blind verification**, backstopped by the terminal pass's full-scope re-read.

A campaign never converges on unreviewed edits: the **terminal pass (1 seat) always runs at campaign close**. Dispatch it as instrument `terminal-pass`, `phase` set `spec`; its inputs are the artifact, the campaign's round records and readouts, the brainstorm decision record (`brainstorm-decisions.md`), the seat findings behind each decision ask, each question carried to readout in its seat report and, for its stop check, every numbered round's seat reports, their `## Verdict` sections only. Its two mandates, the same in both phases, are an **artifact re-read**, full-scope where the final round produced a fix wave (its card's `fix-wave` selector), and **decision-ask fidelity**, the stop's basis and the decision record included in a spec campaign; they and their binding ordering are its template's (`skills/redteaming/terminal-pass-prompt.md`).

**Its report stays as the pass wrote it** — never transcribed, paraphrased, or trimmed by you. A correction, or a mismatch in the report's Notes, flagged `CONCLUSION-CHANGING` is itself a decision ask to the operator; an unflagged correction is reported and does not escalate. Its **bias line**, whether its corrections share a direction favoring the record's author, is a decision ask only where the pass states the record is **materially misleading**. Mechanics: the pass consumes no round against the cap (neither does round 0); its findings a fix list takes get **at most one further fix wave**. **One second read** (instrument `terminal-pass`, `follow-up` set `second-read`; the spec campaign's last report) runs after that wave and, record-only, whenever the pass's report carries a record correction or you put a decision ask to the operator again on it, checking the close readout you recorded in the terminal-pass record against that report and the seat findings behind each ask; one read covers both, and you deliver the close after it, its corrections added. Of what it leaves open, a MINOR not against binding text takes `deferred-minor`; the rest, and any BLOCKER or MAJOR still open at the cap, goes to the operator as a decision ask.

**Cap: 4 rounds (degraded rounds excluded, per § Panels), its guarantee that the campaign ends; the cap bounds rounds, not spend. Where overturning a major mechanism after code is still reasonably expected at the cap, or the cap round's own fix wave adds, removes or re-shapes one, that goes to the operator as a decision ask: another round / supersede / accept-with-parked-rulings.** Cap arithmetic is derived from records, never a stored counter: rounds consumed = count of records numbered ≥ 01 with `degraded: no`.

## The plan phase — one verification round

**Before the plan phase's first dispatch, read `skills/redteaming/references/plan-phase.md` in full.**

## The folded lane

**Where the brainstorm decision record carries the operator's confirmation of the folded preset** (`crucible:brainstorming` § Proposing the arrangement (step 4)), **read `skills/redteaming/references/folded-lane.md` in full before the campaign's round 0.**

## Exit

On convergence, the handoff is your **explicit move, stated in the close readout**. An open premise ask passes on at each close as `skills/redteaming/references/flip-paths.md` § Premise findings states, each bullet naming this close's step:

- a **spec campaign** hands off to `crucible:writing-plans`, an open premise ask carried in this close readout;
- **a spec campaign whose artifact is a combined spec+plan document names `crucible:subagent-driven-development` in its close readout, not the plan skill** — the combined document already is the plan (§ The folded lane). **That close also owns the ledger seeding** — open premise asks, `deferred-minor` entries and what earlier phases left open — in the forms `skills/redteaming/references/plan-phase.md` gives the plan phase's close;
- **a spec campaign whose artifact is an umbrella** (`<feature-folder>/umbrella.md`) **names the umbrella's landing in its close readout, not the plan skill**, and the umbrella lands by `skills/brainstorming/references/umbrellas.md` § Landing, open asks included;
- the **plan phase** hands off to `crucible:subagent-driven-development`, its close (ledger seeding, open premise asks and what earlier phases left open included) as written in § The plan phase — one verification round.

## Flip paths — load-bearing content mid-campaign or mid-execution

**Before raising a decision ask or taking a path on any of these, read `skills/redteaming/references/flip-paths.md` in full**: binding content a finding shows wrong from the spec campaign's close onward, which no fix wave flips; a supersede called for at any point, the cap ask's supersede option and an unfold included; a premise finding at any phase, the spec campaign included; a feature found to need splitting after its spec campaign closes; and, for a feature whose preamble carries an umbrella line, a binding change its umbrella needs or one landed on the base that the feature has not taken in, checked for at each round boundary. A feature found to need splitting before its spec campaign closes is no supersede: the campaign stops, and the feature goes back to brainstorming as `skills/brainstorming/references/umbrellas.md` § Children states. Re-read the reference after compaction: a flip in flight shows through its decision ask or your ruling, recorded in the round record, the plan record's fix list or the ledger you rehydrate from.
