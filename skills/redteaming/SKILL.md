---
name: redteaming
description: Use on a just-written spec or plan, before accepting it.
---

# Redteaming — review controller

## Overview

A **spec campaign** is an iterated loop on one artifact: dispatch a panel of fresh-context seats, merge their findings, apply fixes, verify them blind, read out to the operator; repeat until the stop rule says converged, then run the terminal pass and hand off. Every step writes records; every judgment is computed from the records, never from conversation memory. The operator steers through decision asks without having to read the artifact. A plan is not campaigned: the plan phase reuses the dispatch composition, the merge and finding-hygiene rules and the readout, and § Round 0 through § Stop rule and terminal pass are the spec campaign's unless they say otherwise. Panels serve specs and plans only: open-ended project-wide issue-mining is not a campaign, and whole-branch review of code is `crucible:requesting-code-review`'s.

**Dispatch references:** when this skill starts and after compaction, read `skills/subagent-driven-development/references/dispatch-composition.md` and your adapter's `skills/using-crucible/references/<runtime>-dispatch.md`; both bind as if written here.

**Stubs.** A reference a section names to read in full binds as if written here. Read it when its step comes, unless read since your last compaction; after compaction, re-read the step in progress's reference first.

## Inputs and state

**The artifact** is one spec or one plan at a fixed path and revision; every seat in a round reads that one revision. **The feature workspace** is `<repo>/.crucible/<feature-slug>/`, provisioned at brainstorm exit (if missing, run the provisioning step in `formats.md` § Feature workspace root and layout); records live under its `campaigns/spec/` or `campaigns/plan/`, their paths composed by plain path-join from the repo root. When this skill starts, read `skills/redteaming/references/round-record.md`; it and `formats.md` define every record and the workspace. If this skill and either file conflict, stop and report BLOCKED; never improvise a format.

**State line.** Write each `round-NN/record.md`'s `state:` line (`round-record.md` § Round record format, field 2) at each phase boundary, each state only after that phase's outputs are on disk.

**Rehydration** after compaction resumes from the workspace: the current round is the highest record number, and its state line says where to pick up. A fix list recorded while the state is short of `fix-applied` is re-checked item by item against the artifact before any re-apply. A resume at `state: readout` delivers the recorded readout again, without its trace. In the plan phase or on the folded lane, re-read that route's reference first.

**Artifact freeze and shared tree (binding).** Never edit the artifact while any seat, verifier or pass is reading it. The dispatch composition's § Shared-tree rules bind every seat you start; its status check runs after every dispatch window: panel seats (one window per concurrent batch), the round-0 pre-pass, the blind verifier, the terminal pass, and the plan phase's pre-pass and coherence seats. Dispatch each window with your fixes committed; your fixes land between windows, never inside one.

## Dispatch composition

Every seat you start carries the dispatch composition's seven items; the round-0 pre-pass is the one controller-composed dispatch here, and the blind verifier gets no binding pointer (item 4). Three seats are instruments, each dispatched from the slot card beside its template: `redteam-seat` (`seat-prompt.md`, `seat-prompt.slots.md`), `blind-verifier` (`verifier-prompt.md`, `verifier-prompt.slots.md`), `terminal-pass` (`terminal-pass-prompt.md`, `terminal-pass-prompt.slots.md`). Seat models: the dispatch composition's § Models and effort; only the verifier's card has a Model line, other seats taking its default role, and round 1's swap to the alternate role is § Panels'.

## Round 0 — mechanical pre-pass

On every spec campaign, before any panel, dispatch one standalone agent producing a claim table: each "the code does X" claim (with no code baseline, each claim about the artifact's inputs: the request, the decision record, cited documents) marked TRUE or FALSE with evidence. It also checks liveness (every declared mechanism has a producer and a consumer within the artifact) and runs regex and CLI claims rather than reading them. Its prompt carries `skills/subagent-driven-development/references/review-terms.md` § Suite bound, copied; a scratch line putting code it runs under the workspace's `scratch/campaigns/spec/round-00/`, never the tracked tree; and a staked severity on each finding, which decides what its fix list takes. Record it as `round-00/` per `round-record.md` and apply its fix list before round 1. Round 0 gets no blind verifier: the round-1 panel's full-scope read checks those fixes.

## Panels

Before you size, staff or dispatch any panel round or plan-phase seat, and whenever a dispatched seat is lost, **read `skills/redteaming/references/panels.md` in full**. A degraded round counts toward neither convergence nor the cap; two consecutive degraded rounds are an infrastructure escalation to the operator.

## Merge and finding hygiene

Whenever you merge seat reports or disposition a finding or question, **read `skills/redteaming/references/merge-and-finding-hygiene.md` in full**. **Record hygiene** is finding hygiene's seat rule turned on what you author: in every record, readout and decision ask, a code-shaped claim shows its evidence (what was read or run) or carries `UNVERIFIED`, the one tag. The tag marks a claim; it never admits an `UNVERIFIED` finding to a fix list. A decision ask resting on an untagged unverified mechanical fact is a defect in the ask.

### Operating stance

Errors in controller-authored text are expected and budgeted for: report them, yours included, flatly like any finding; shading a record, not erring in it, is the reporting duty's one reportable failure, and this stance never excuses skipping, softening or summarizing any reporting duty.

## Fix application and blind verification

Whenever you judge which findings a fix list takes, or write, apply or verify a fix list or repair edit, **read `skills/redteaming/references/fix-application.md` in full**. Before applying any cut, you and fix waves consult the right-sizing seats' over-subtraction attestations; cutting attested content needs a ruling logged in the round record. A proposed cut that would remove binding content, or a declared mechanism's only producer or consumer, is a finding against the cut, not a cut.

## Round readout

At every round and campaign close, for any other readout that points here to put decision asks, and whenever an operator ruling or record correction arrives after a round closed, **read `skills/redteaming/references/round-readout.md` in full**.

## Stop rule and terminal pass

Throughout this section a premise finding (§ Premise findings) is a decision ask, never an open finding.

**The stop trigger** is the first numbered panel round after which overturning a major mechanism after code is no longer reasonably expected: the overturn question of `skills/subagent-driven-development/references/review-terms.md` § The arrangement questions, read for an umbrella's campaign by that file's § An umbrella's overturn question. Answer it by your judgment over the round's records: the merged list, the fix list and the seats' forecast lines in their reports' `## Verdict`. Severity is not the trigger: a BLOCKER that would overturn a mechanism keeps the campaign going through the overturn question. A round whose own fix wave adds, removes or re-shapes a major mechanism is never the stop round: no seat has read the result. Recording a deferral never re-shapes one; the binding outcome its item lands is judged like any other edit. Once a campaign is chosen, at least one numbered panel round runs. The stop round's open findings that a fix list takes get that round's one fix wave plus blind verification, backstopped by the terminal pass's full-scope re-read.

**The terminal pass** (one seat) always runs at campaign close, since a campaign never converges on unreviewed edits: instrument `terminal-pass`, `phase` set `spec`. Its mandates, the same in both phases, and their ordering are its template's: an artifact re-read, full-scope where the final round produced a fix wave (the card's `fix-wave` selector), and decision-ask fidelity, in a spec campaign also over the stop's basis and the decision record. Its report stays as the pass wrote it. A correction, or a mismatch in its Notes, flagged `CONCLUSION-CHANGING` is itself a decision ask to the operator; an unflagged correction is reported and does not escalate. Its bias line is a decision ask only where the pass states the record is materially misleading.

**After the pass.** Terminal-pass findings a fix list takes get at most one further fix wave. One second read (instrument `terminal-pass`, `follow-up` set `second-read`) runs after that wave and, record-only, whenever the pass's report carries a record correction or you put a decision ask to the operator again on it; one read covers both. Record the close readout first (a spec campaign's in the terminal-pass record), since the second read checks it against the pass's report and the seat findings behind each ask; deliver the close after the second read, its corrections added. Of what the second read leaves open, a MINOR not against binding text takes `deferred-minor`; the rest, and any BLOCKER or MAJOR still open at the cap, is a decision ask.

**The cap** is 4 rounds; degraded rounds, round 0 and the terminal pass consume none. It bounds rounds, not spend. Where at the cap overturn is still reasonably expected, or the cap round's own fix wave adds, removes or re-shapes a major mechanism, put a decision ask: another round / supersede / accept-with-parked-rulings. Cap arithmetic is derived from the records, never a stored counter: rounds consumed = the count of records numbered ≥ 01 with `degraded: no`.

## The plan phase

Before the plan phase's first dispatch, **read `skills/redteaming/references/plan-phase.md` in full**.

## The folded lane

Where the brainstorm decision record carries the operator's confirmation of the folded preset (`crucible:brainstorming` § Proposing the arrangement), **read `skills/redteaming/references/folded-lane.md` in full** before the campaign's round 0.

## Exit

On convergence the handoff is your explicit move, stated in the close readout, which also carries any open premise ask (§ Premise findings) unless a line says otherwise:

- a spec campaign: `crucible:writing-plans`;
- one on a combined spec+plan document: `crucible:subagent-driven-development`, the document being the plan;
- one on an umbrella (`<feature-folder>/umbrella.md`): the umbrella's landing, by `skills/brainstorming/references/umbrellas.md` § Landing, open asks included;
- the plan phase: `crucible:subagent-driven-development`, an open premise ask carried in the plan record.

## Flip paths

Before raising a decision ask or taking a path on binding content a finding shows wrong from the spec campaign's close on (no fix wave flips it), or on any supersede (the cap ask's supersede option, an unfold), **read `skills/redteaming/references/flip-paths.md` in full**, and re-read it after compaction (a flip in flight shows as its decision ask or your ruling in the round record, the plan record's fix list or the ledger). `skills/brainstorming/references/umbrella-children.md` § Under an umbrella governs a split found after the spec campaign closes and, for a feature with an umbrella line, a binding change its umbrella needs or one landed on the base and not yet taken in, checked for at each round boundary. Before raising either, and before the first such check, read that section, and re-read it after compaction. A split found earlier is no supersede: the campaign stops and the feature returns to brainstorming (that file's § Children).

## Premise findings

Before raising a decision ask or taking a path on a premise finding, at any phase including the spec campaign, **read `skills/redteaming/references/premise-asks.md` in full**, and re-read it after compaction.
