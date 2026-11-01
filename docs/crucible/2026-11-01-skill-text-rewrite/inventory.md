> The mechanism inventory the umbrella's audit (2026-11-01) built at `a3db87f`, kept as the baseline for the re-audit (`umbrella.md` D9). Committed as written, local paths removed; word figures are its estimates.

# Crucible mechanism inventory

Tree: the crucible repository, master `a3db87f8ddc0eb2a84c88f19cbebb72f4cf3ab58` (Release 0.11.0), working tree clean when the run started. Built 2026-11-01. Nothing in the repository was modified.

## Method

- **Read in full:** every `SKILL.md` under `skills/`, every file under `skills/**/references/`, every dispatch template and slot card (`seat-prompt*`, `terminal-pass-prompt*`, `verifier-prompt*`, `code-reviewer*`, `implementer-prompt*`, `task-reviewer-prompt*`, `re-review-prompt*`), and the four host adapters. The upstream technique files (`systematic-debugging/*.md` supporting files, `writing-good-tests.md`, `dispatching-parallel-agents`) were skimmed for checks and breakers only.
- **Word counts:** whitespace-separated tokens, as `tests/prose-budget.txt` counts them. Per-heading totals came from a script over each `.md` file. Every `SKILL.md` writes one paragraph per line, so a second script gave per-paragraph counts. Where a paragraph serves one mechanism, its count is **counted**. Where it serves several, the split is an **estimate**, marked `~`. All figures are rounded. Per-mechanism figures carry roughly ±20% error, and the ordering among mechanisms within 10% of each other is not meaningful.
- **Cost buckets** (column 4). **R** is words in `SKILL.md` bodies. They load when the skill is invoked and stay until compaction. `using-crucible` is also injected at every session start. **Ref** is words in `references/*.md`, loaded on demand at the step named. **Seat** is words in templates plus slot cards. They are not in the controller's resident text: the template loads into each dispatched seat (on Claude Code the generated `crucible:<name>` agent carries it), so the cost repeats per dispatch, and the controller reads the card once per dispatch. Where a mechanism is stated in several skills, R sums the sites, and the owner skill's table carries the whole sum.
- **Restatements:** found with Grep over `skills/` on each mechanism's key terms. Counts are matching lines per file, from Grep's count mode. A few term searches had false positives (for example, "contained" in `writing-skills`); those were dropped by reading.
- **Justification:** the `(Basis: …)` tags of every record in `docs/decisions/` were extracted by script (364 tags). The Why sections of the records that hold the main mechanisms were read in full: spec-campaign, fix-verification-and-merge, terminal-pass, task-loop, evidence-and-findings, records-and-workspace, the-spec, plans, shared-tree, branch-review, operator-steering, routes, umbrellas, adjudication, instruments, decision-records. Classes:
  - **M** (measured): the Why cites a count or study over several runs: an audit, a recount, a study, or several incidents.
  - **S** (single incident): the Why cites one incident.
  - **N** (no incident): judgment, preference or an external source only.
  - A mixed Why is given its strongest class, with the rest named.
- **Reach codes.** Routes: Std (standard), Fold (folded), VS (very-small), Umb (umbrella). Phases: BS (brainstorm), SC (spec campaign), PP (plan phase), EX (execution task loop), BR (branch review), FIN (SDD Finish plus finishing), UL (umbrella landing), UC (umbrella closing review). "All" means every route.
- Anything I could not tie to a source is marked `UNVERIFIED`.

Mechanism IDs are prefixed by the skill that owns the text: UC using-crucible, BS brainstorming, UM brainstorming's umbrella reference, RT redteaming, ST shared-tree rules, SDD subagent-driven-development, CR requesting-code-review, WP writing-plans, FIN finishing, WT using-git-worktrees, RR receiving-review, SD systematic-debugging, WS writing-skills. **147 mechanisms.**

---

## Tables per skill

### using-crucible (`skills/using-crucible/SKILL.md`, 797 words; always loaded through the SessionStart envelope)

| ID | Name | Owner text | Resident cost | Reach | Observable signature |
|---|---|---|---|---|---|
| UC1 | skill-check rule | using-crucible § The Rule (¶1–2), § Red Flags, § Skill Priority, § Skill Index | R ~470 (always loaded) | All; every session | "Using [skill] to [purpose]" announcements; Skill tool calls before any action |
| UC2 | trivial-edit waiver | using-crucible § The Rule (**Trivial-edit waiver.**) | R ~85 | Pre-route, before BS | A one-line offer to make a change "without crucible's process", then the operator's yes |
| UC3 | evidence-before-claims | using-crucible § The Rule (**Evidence before claims:**) | R ~25 (+ restatements, see section) | All phases | A completion claim followed by quoted check output |
| UC4 | compaction re-read | using-crucible § The Rule (**After compaction:**) plus "re-read … after compaction" at each reference stub | R ~200 total (16 sites, ~12 words each) | All phases, after compaction | Skill re-invoked or reference re-Read right after a compaction marker |

### brainstorming (`SKILL.md` 3,764; refs `umbrellas.md` 2,256, `lane-note.md` 328, `folded-lane-document.md` 303)

| ID | Name | Owner text | Resident cost | Reach | Observable signature |
|---|---|---|---|---|---|
| BS1 | brainstorm-first gate | brainstorming `<HARD-GATE>` block and "Too simple" ¶ (preamble) | R 88 + router 25 | All; BS | "I'm using … brainstorming"; no code edits before the spec commit |
| BS2 | worktree before the spec | brainstorming § Spec contract (Persistence ¶, worktree part); § The dialogue (closing sentence of **Presenting the design**) | R ~125 | All; BS | Design message naming the feature worktree; worktree created before `design.md` is written |
| BS3 | arrangement presets | brainstorming § Proposing the arrangement (step 4), ¶1–4 (choices, preset table, **Unsupported**) | R 318 (counted) | All; BS step 4 | Proposal naming `standard` / `folded` / `very-small` |
| BS4 | overturn selector (step 4) | brainstorming § Proposing the arrangement (step 4), **Choose the preset by the overturn question**; question defined in premise-and-questions § The arrangement questions | R 210; Ref ~240 (overturn ~170 + overdetermined ~70; p&q, read at step 4) | All; BS step 4 | The proposal states "the overturn answer with its reason" |
| BS5 | preset confirmation and route entry | brainstorming § Proposing the arrangement (step 4), **The proposal.** and **Record the operator's answer…** | R 185 (counted) | All; BS step 4 | Route entry in `brainstorm-decisions.md` with status `accepted` / `firm` |
| BS6 | verification at writing | brainstorming § Spec contract (**Verification happens at the moment of writing.**) | R 70; Ref ~25 (lane-note) | All; BS | `UNVERIFIED` tags inside spec or note text |
| BS7 | spec contract format | brainstorming § Spec contract (Audience ¶ and section list) | R ~140 | Std, Fold, Umb; BS | `design.md` headings Intent / Decisions / Constraints & invariants / Interfaces & boundaries / Acceptance / Mechanism sketches |
| BS8 | binding-content model | brainstorming § Spec contract (**What binds** ¶, Constraints bullet); flip-paths § Flip paths — scoped amendment and supersede (intro) | R ~420 across 3 skills; Ref ~230; Seat ~900 (6 templates) | All; SC through BR | BLOCKED reports naming a binding item with a proposed correction; "binding" in rulings |
| BS8b | literal-reading finding | same owner (intent-reading clause), plus templates' Binding Content passages | R ~60 (in SDD); Seat ~200 | Std, Fold, VS; EX, BR, SC | `literal-reading` label on task-review, re-review or branch-review findings |
| BS9 | `[LOAD-BEARING]` mark | brainstorming § Spec contract (**Decisions** bullet) | R ~45 (+ ~5 words at each binding clause) | Std, Fold, Umb; BS onward | `[LOAD-BEARING: <what builds on it>]` in the spec |
| BS10 | decision statuses | brainstorming § Workspace provisioning (brainstorm exit), ¶1 (statuses, proposer, delegated) | R ~110; Ref ~45 | All; BS onward | `open`, `accepted — proposed by the controller`, `accepted — delegated to the controller`, `firm` |
| BS12 | deferral chain | brainstorming § Spec contract (**Deferral device.**); writing-plans § Deferring detail and § Plan header (routing table) | R ~870 across 4 skills; Ref ~185; Seat ~240 | Std, Fold; BS → BR | `Deferred to implementation:` lines; `## Deferred-items routing table`; Decision Log entries per routed item; "Routed deferred items: LOGGED/MISSING" |
| BS13 | spec self-review | brainstorming § Spec self-review (checks 1–4, evidence half of 5) | R ~200 | All spec kinds (note and approval-only umbrella on the draft); BS | Rarely visible: inline fixes after drafting |
| BS14 | consumer sweep | brainstorming § Spec self-review (check 5, **consumer sweep**) | R ~145 (BS 85 + WP Files ~60) | All; BS, plan writing, fix lists | Enumerated consumer lists in a plan's Files field; Grep runs before writing |
| BS15 | trace (routes × phases) | brainstorming § Spec self-review (check 5, **trace**) | R 62; Seat ~35 (code-reviewer) | All; BS, SC fix lists, BR | Rarely visible; branch-review findings about an unreached trigger |
| BS16 | feature workspace | formats.md § Feature workspace root and layout (Provisioning, Self-ignition, Lifecycle) | R ~245 (BS 45, SDD ~150, RT ~50); Ref ~650 | All; BS → FIN, UL, UC | `.crucible/<slug>/`; `.crucible/.gitignore`; `git check-ignore -q .crucible/<slug>/probe`; deletion at Finish |
| BS17 | brainstorm decision record | brainstorming § Workspace provisioning (brainstorm exit), ¶1; formats.md § Feature workspace root and layout (**Later operator rulings enter the decision record**) | R ~180; Ref ~110 | All; BS → FIN | Writes to `<workspace>/brainstorm-decisions.md` |
| BS18 | request file | brainstorming § Workspace provisioning (brainstorm exit), ¶2; formats.md (**Later changes to the ask enter `request.md`**) | R ~155; Ref ~70; Seat ~30 (cards) | All; BS → BR | Writes and appends to `<workspace>/request.md`; `{request-path}` / `[REQUEST_FILE]` filled |
| BS19 | design digest | brainstorming § Design digest; formats.md § Design digest format | R ~135; Ref 195 | Std (major designs), campaigned Umb; BS, SC | `<workspace>/digest.md`; digest-update item in readouts |
| BS20 | digest gate | brainstorming § Digest gate; redteaming § Panels (**Launch:**) | R ~210 | Std, Fold (inline asks), campaigned Umb; BS → SC start | Gate message with digest, asks and seat shape; gate entry in `brainstorm-decisions.md`; campaign-start readout |
| BS21 | lane note | brainstorming/references/lane-note.md § The very-small lane — the lane note (step 5) | R ~130; Ref 328 (read before drafting at step 4) + ~130 (very-small-lane freeze ¶); Seat ~135 (lane passages) | VS; BS → BR | `<feature-folder>/note.md` under a `Lane: very-small (operator-confirmed <date>)` line |
| BS22 | folded document | brainstorming/references/folded-lane-document.md § The folded lane — the combined spec+plan document (step 5) | R ~97; Ref 303 (read at step 5) | Fold; BS | `<feature-folder>/folded.md`; header `Spec: this document` |
| BS23 | feature folder | formats.md § Feature folder (birth / resolve, role names) | R ~220 (BS ~140, WP ~60, FIN ~20); Ref ~425 | All; BS onward | `docs/crucible/<YYYY-MM-DD>-<slug>/` with `design.md`, `plan.md`, `folded.md`, `note.md` or `umbrella.md`; root listed before the first write |
| UM1 | umbrella file | umbrellas.md § Umbrellas…, #### Shape, #### Resuming | R ~72 (stub); Ref ~510 (read before proposing, writing, a child's brainstorm or resuming) | Umb; BS | `umbrella.md` with an ordered Children list |
| UM2 | umbrella review choice | umbrellas.md #### Review | R ~57; Ref 152 | Umb; BS step 4 | Route entry for the umbrella: campaign or approval |
| UM3 | umbrella landing | umbrellas.md #### Landing | R ~100 (RT § Exit 69, Handoff ~30); Ref 242 | Umb; UL | Landing ask; umbrella workspace deleted before the landing |
| UM4 | umbrella line binding | umbrellas.md #### Children (**The umbrella line.**); receiving step in flip-paths § Under an umbrella: binding changes and late splits | R ~465; Ref ~700; Seat ~720 | Umb children (all routes); SC, PP, EX, BR | `Umbrella:` preamble line; `{umbrella-paths}` / `[UMBRELLAS]` filled; `git diff HEAD...<base> -- <umbrella paths>`; base merged in |
| UM5 | umbrella marks | umbrellas.md #### Marks, #### Closing; SDD § Finish step 4 | R ~170; Ref 184 | Umb children; FIN, UL | Children-list entry ending `— landed` / `umbrella` / `dropped`; `git grep -n "<slug>" <base> -- "*/umbrella.md"`; `git cat-file -e` |
| UM6 | umbrella binding-change protocol | umbrellas.md #### Edits; flip-paths § Under an umbrella… (**Raising.**) | R ~40; Ref ~300 | Umb; any phase of a child | Decision ask naming every open umbrella and every child in flight; separate landing branch |
| UM7 | late split | umbrellas.md #### Children (**A split.**) | R ~60; Ref ~180 | All under Umb; after SC close or note commit | Feature abandoned; new umbrella listing it; old entry marked `dropped` |
| UM8 | umbrella closing review | umbrellas.md #### Closing review | R ~50 (SDD Finish, finishing Option 1); Ref 490 | Umb; UC | `.crucible/<umbrella-slug>/closing-<lens>.md` (e.g. `closing-seams.md`); 2–3 controller-composed default-role dispatches |

### redteaming (`SKILL.md` 6,374; refs `formats.md` 3,613, `flip-paths.md` 1,957, `plan-phase.md` 1,066, `folded-lane.md` 583; templates and cards 5,872; `scripts/conserve.py` 1,308 words of code, outside the prose budget)

| ID | Name | Owner text | Resident cost | Reach | Observable signature |
|---|---|---|---|---|---|
| RT1 | redteam panel | redteaming § Panels (sizing, **Lens roster**, **Full-scope mandate always**, seat dispatch) | R ~400; Ref ~35; Seat ~380 + card ~300 | Std, Fold, campaigned Umb; SC (PP via RT34) | `crucible:redteam-seat` dispatches; `campaigns/spec/round-NN/seat-<id>.md` |
| RT2 | round-0 pre-pass and ordered-first hunt | redteaming § Round 0 — mechanical pre-pass | R ~157; Ref ~130; Seat ~165 | SC with a code baseline (always on Fold); greenfield takes the round-1 ordered-first hunt | `round-00/record.md` with `## Claim table`; controller-composed agent; `worksheet: ordered-first` |
| RT3 | right-sizing seat and over-subtraction guard | redteaming § Panels (**right-sizing** bullet) | R 139; Ref ~12; Seat ~115 | SC (round 1, then periodically); Fold round 1 always | `## Right-sized — do not cut` in a seat report; `right-sizing: on` |
| RT3b | wave line counts (re-seat signal) | redteaming § Round readout (trace ¶); formats.md § Round record format field 8 (**Trace**) | R ~35; Ref ~110 | SC numbered rounds | `git diff --numstat <base-rev> <head-rev> -- <artifact>`; two numbers in `Trace:` |
| RT4 | round-1 alternate-role swap | redteaming § Panels (**Seat models:**, Round 1's swap) | R ~124; Ref ~80 (dispatch-composition) | SC round 1 with ≥2 seats | One round-1 seat on the alternate role (Claude Code: Fable; Codex: `gpt-6-astra`), named in the campaign shape |
| RT5 | quorum, degraded rounds and top-up | redteaming § Panels (**Quorum and degraded rounds**, **Topping up is gated**) | R ~213; Ref ~120 | SC, PP | `## Quorum block`; `degraded: yes|no`; `topped-up` |
| RT6 | round records, state line and rehydration | redteaming § Inputs and state (**Round records and state lines**, formats contract); formats.md § Round record format (fields 1–2, special records) | R ~187; Ref ~600 | SC, PP | `round-NN/record.md`; `state: dispatched → … → readout` (`confirmed` on the plan record) |
| RT7 | merged finding list and dispositions | redteaming § Merge and finding hygiene ¶1; formats.md field 5 | R 85; Ref ~330 | SC, PP | `## Merged finding list`; `- F3 MAJOR … origins: s2-4 … disposition: applied|partly-applied|parked|rejected|deferred-to-implementation` |
| RT8 | seat index and merge from indexes | redteaming § Merge and finding hygiene (**Merge from the indexes.**, first half) | R ~70; Seat ~110 | SC, PP | `## Index` opening each seat report |
| RT9 | sub-point check | redteaming § Merge and finding hygiene (**Merge from the indexes.**, second half) | R ~100 | SC, PP | Hard to see: sub-points added to fix items, or ruled in the entry |
| RT10 | merge conservation | redteaming § Merge and finding hygiene (**Merge conservation**, **Check it; do not reconcile by hand**, degraded-round ¶); seat-id rule in § Panels | R ~312; Ref ~170; script 1,308 (code) | SC, PP numbered rounds | `python <plugin-root>/skills/redteaming/scripts/conserve.py <slug> <phase> <round>`; `conservation: … clean` or `unaccounted:` |
| RT11 | question dispositions | redteaming § Merge and finding hygiene (Question ¶ inside **Merge conservation**) | R ~240; Ref ~100 | SC, PP | `## Question dispositions`; ids `<seat>-q<n>`; verbatim questions in readouts |
| RT12 | finding hygiene | redteaming § Merge and finding hygiene (**Finding hygiene**) | R ~60; Seat ~310 (seat, terminal, task-reviewer, code-reviewer, implementer claim discipline) | All review seats; SC, PP, EX, BR | Staked `BLOCKER/MAJOR/MINOR`; `UNVERIFIED` tags; UNVERIFIED findings verified or discarded on an indented line |
| RT13 | finding scope | redteaming § Merge and finding hygiene (**Finding scope**) | R 108; Seat ~300 | SC, PP | `rejected` dispositions carrying a scope ruling |
| RT14 | record hygiene | redteaming § Merge and finding hygiene (**Record hygiene**) | R 103 | SC, PP | `UNVERIFIED` in controller records and asks |
| RT15 | operating stance | redteaming § Operating stance — baseline error rate | R ~170 (RT 143 + SDD ~25); Seat ~40 | SC, PP, EX | Tone only: flat-register error reports |
| RT16 | fix-list contract | redteaming § Fix application and blind verification (fix list, **Fix altitude**, reproducers, **The artifact states the current design only.**) | R ~268; Ref ~60 | SC, PP | `## Fix list` items naming finding ids; acceptance items stating input and result |
| RT17 | propagation sweep | redteaming § Fix application… (**Propagation sweep**) | R ~96; Ref ~50 | SC, PP | Fix items listing restating sites |
| RT18 | fix-item trace | redteaming § Fix application… (**Trace each rule an item adds or changes**) | R 80 | SC, PP (every fix list RT freezes) | Restating sites the trace finds, listed in items; hard to see otherwise |
| RT19 | predicate is run, not read | redteaming § Fix application… (**A predicate is run, not read**) | R 118; Ref ~40 (lane-note) | SC, PP; VS note writing | Command and output under a fix item; a failing pre-change run |
| RT20 | blind verifier | redteaming § Fix application… (after-apply ¶); § Dispatch composition (binding-pointer bullet) | R ~124; Ref ~100; Seat ~743 + card 206 | SC, PP, terminal follow-up wave | `crucible:blind-verifier`; `round-NN/verifier.md`; `## Per-item verdicts`, `## Outside-the-list` |
| RT20b | delta-claims check | redteaming § Fix application… (delta-claims clause, check of unchecked claims) | R ~69; Seat ~90 | SC, PP | `## Delta claims` in `verifier.md`; the controller's outcomes in `## Verifier block` |
| RT21 | round readout, trace and coverage check | redteaming § Round readout | R ~383; Ref ~200 | SC, PP | `## Round readout` then `Trace:`; delivered readout message; `## Rulings and corrections` |
| RT22 | decision-ask format | redteaming § Round readout (technical-calls bullet) | R ~112 across 3 skills; Ref ~80 | All; SC, PP, EX, BR, FIN, UL | Asks in analyst language with a recommendation, listing every option and naming what they withdraw |
| RT23 | stop rule (overturn question) | redteaming § Stop rule and terminal pass (**Stop trigger**, re-shape rule, stop round's one wave) | R ~185 | SC (all campaigned routes) | Readout line saying overturn "is no longer reasonably expected", with its reason |
| RT24 | seat forecast lines | seat-prompt.md (Report item 1, second line); redteaming § Round readout (overturn item) | R ~83; Ref ~70; Seat ~70 | SC numbered rounds | `Overturn after code: reasonably expected — …` or `… not reasonably expected` in `## Verdict`; seat ids in `Trace:` |
| RT25 | premise hold on the stop | redteaming § Stop rule and terminal pass (premise sentence) | R ~70; Ref ~30 | SC | Campaign paused at a round close pending a premise ruling |
| RT26 | campaign cap | redteaming § Stop rule and terminal pass (**Cap: 4 rounds**) | R 112; Ref ~40 | SC | Ask "another round / supersede / accept-with-parked-rulings" |
| RT27 | terminal pass (artifact re-read) | redteaming § Stop rule and terminal pass (terminal pass ¶, mandate 1); terminal-pass-prompt.md | R ~143; Ref ~80; Seat ~985 + card 304 | SC close, PP close | `crucible:terminal-pass`; `campaigns/spec/terminal-pass/pass.md` or `campaigns/plan/round-01/terminal-pass.md`; `## Artifact verdict`; `Record corrections: <N>` |
| RT28 | decision-ask fidelity and `CONCLUSION-CHANGING` | redteaming § Stop rule and terminal pass (mandate 2, report ¶); terminal-pass-prompt.md (**Mandate 2**) | R ~75; Seat ~390 | SC, PP | `## Record corrections` items; `CONCLUSION-CHANGING` flags raised as asks |
| RT29 | stop check | terminal-pass-prompt.md (**The stop check, part of mandate 2.**) | R ~35; Seat ~195 | SC | Corrections about unanswered forecasts or a re-shaping stop round |
| RT30 | decision-record check | terminal-pass-prompt.md (**The decision-record check, part of mandate 2.**) | R ~24; Seat ~100 | SC | Correction flagged for an approval withdrawn without a record |
| RT31 | directional-bias statement | redteaming § Stop rule and terminal pass (bias sentences); § Operating stance… (last ¶) | R ~127; Seat ~125 | SC, PP | "corrections share no direction", or the shared direction, in `## Record corrections` |
| RT32 | terminal tail (follow-up wave and second read) | redteaming § Stop rule and terminal pass (Mechanics sentence) | R ~70; Ref ~60; Seat ~150 | SC, PP | `second-read.md`; `follow-up: second-read` |
| RT33 | artifact freeze | redteaming § Inputs and state (**Artifact freeze**) | R 22 | SC, PP | None directly (no artifact commits inside a window) |
| RT34 | plan phase | redteaming/references/plan-phase.md § The plan phase — one verification round | R ~260 (RT ~197 + WP exit 63); Ref ~520 (read before the phase's first dispatch) | Std; PP | `campaigns/plan/round-01/record.md`; `seat-p0.md`; `state: confirmed`; phase-start readout |
| RT35 | plan arithmetic and post-wave re-run | writing-plans § Plan header (**File ownership + overlap census**); plan-phase.md (seat 1, **Post-wave verification**) | R ~70; Ref ~180; Seat ~55 | Std PP; Fold SC | `## Worksheet` in `seat-p0.md` or `round-00`; controller re-run recorded in `## Verifier block` |
| RT36 | set census | seat-prompt.md (`[[when worksheet = pre-pass]]`); plan-phase.md seat 1 | Ref ~40; Seat ~110 | Std PP; Fold round 0 | Census table in `## Worksheet`; `git grep` over tracked text |
| RT37 | plan-phase repair paths | plan-phase.md (**Two sanctioned repair paths, neither a loop.**) | Ref ~140 | Std; PP | One-item re-check by the same verifier; `round-01/second-read.md` |
| RT38 | folded-lane campaign rules | redteaming/references/folded-lane.md § The folded lane | R ~120; Ref ~300 (read before round 0 when the fold is recorded) | Fold; SC | `folded.md` campaign with no `campaigns/plan/` |
| RT39 | flip paths (scoped amendment, supersede) | flip-paths.md § Flip paths — scoped amendment and supersede | R ~480 (RT stub 233, SDD § Plan changes mid-execution 206, ~40 elsewhere); Ref ~650 (read before any flip) | All; SC close onward, EX, BR | Amendment marker in the spec; re-stamped `Spec:` pin; `design-2.md` / `plan-2.md`; `ledger-superseded.md`; amendment commits named in dispatches |
| RT40 | containment test | flip-paths.md § The containment test | R ~295; Ref ~525; Seat ~160 | All; from SC close: PP, EX, BR | `Contained amendment:` fix items; contained rulings under `## Adjudication rulings`; listed in the close readout |
| RT41 | premise findings | premise-and-questions.md § Premise findings (definition); flip-paths.md § Premise findings (controller side) | R ~250; Ref ~950; Seat ~125 | All; SC, PP, EX, BR, UL, UC | `FINDING s2-3 [MAJOR] premise`; `- F4 MAJOR premise`; `open premise ask:` in umbrella entries |
| RT42 | earlier-phase carriage (`— carried`) | plan-phase.md (**What earlier phases left open.**) | R ~75; Ref ~170 | Std, Fold, VS; PP close / SC close / SDD Setup; UL | Ledger `## Questions` lines `brainstorm|spec|plan: <item> — carried` |
| RT43 | focused checks and scratch | redteaming § Round 0 — mechanical pre-pass (scratch line, suite bound) | R ~45; Seat ~600 (7 templates) | SC, PP, EX, BR | `.crucible/<slug>/scratch/<report path less .md>/`; no package-wide suite runs by seats |
| RT44 | read scoping | each template's Read scoping / § Read Scoping (no single owner; dispatch-composition item 2) | R ~43; Seat ~735 (7 templates) | All seats | None directly |
| RT45 | report-file contract | dispatch-composition.md item 5; formats.md (**A report the controller saved carries a mark**) | R ~112; Ref ~230; Seat ~280 | All seats | File confirmed on disk; one resume asking the seat to write; first line saying the controller saved it |
| RT46 | instruments, slot cards and selectors | redteaming § Dispatch composition (**Dispatching an instrument.**); SDD § Runtime identity in every dispatch (**Instruments.**) | R ~245; Seat ~795 | All seats | `subagent_type: crucible:<name>` with a filled card as the prompt; `[[when …]]` passages |
| RT47 | seven-item dispatch composition | dispatch-composition.md § Dispatch composition | R ~225; Ref ~265 (read before first dispatch, re-read after compaction); Seat ~420 | All seats | Worktree path, runtime, no-delegation and never-touch-another-checkout lines in every prompt |
| RT48 | model roles and effort | dispatch-composition.md § Models and effort | R ~220; Ref ~170; Seat ~245 | All seats | Explicit `model` on each dispatch; effort unset unless the operator asked |

### Shared-tree rules (owned jointly: SDD § Shared-tree rules and redteaming § Inputs and state)

| ID | Name | Owner text | Resident cost | Reach | Observable signature |
|---|---|---|---|---|---|
| ST1 | no commit while a seat works | SDD § Shared-tree rules (**No commits while a seat works.**); redteaming § Inputs and state (**Shared tree**) | R ~83; Seat ~30 | All dispatching phases | Commits queued until the seat returns |
| ST2 | tree check | SDD § Shared-tree rules (**The tree check, every review seat**); redteaming § Inputs and state | R ~263; Ref ~75 | SC, PP, EX, BR | `git rev-parse HEAD` plus `git status --porcelain --untracked-files=all` before and after each window; readings in record sections |
| ST3 | seat replacement gate | SDD § Shared-tree rules (**Replacing a seat is gated**); redteaming § Panels (**Topping up is gated**) | R ~236 | All dispatching phases | `BLOCKED — ambiguous seat liveness`; `-r<R>` report names |

### subagent-driven-development (`SKILL.md` 7,288; refs `dispatch-composition.md` 853, `premise-and-questions.md` 1,040, `very-small-lane.md` 1,398; templates and cards 7,657; `writing-good-tests.md` 1,312)

| ID | Name | Owner text | Resident cost | Reach | Observable signature |
|---|---|---|---|---|---|
| SDD1 | ledger | SDD § Setup (**The ledger**, resume rule, predecessor links); § The Task Loop, 6. Complete the task | R ~480; Ref ~210 (lane ledger) | Std, Fold, VS; EX → FIN | `sdd/ledger.md`; `# SDD ledger — plan: …`; `Task <N>: complete (…)` |
| SDD2 | baseline line | SDD § Setup (provisioning ¶) | R ~45 | Std, Fold, VS; EX start | `Baseline: <result> at <sha7>` |
| SDD3 | pre-flight plan-conflict scan | SDD § Setup (**Pre-flight plan-conflict scan.**) | R 142 | Std, Fold; EX start | Rulings under `## Adjudication rulings` before Task 1 |
| SDD4 | task review | SDD § The Task Loop, 3. Review the task; task-reviewer-prompt.md | R ~318; Seat ~1,700 + card 276 | Std, Fold; EX | `crucible:task-reviewer`; `sdd/reports/task-<N>-review.md` with `### Intent`, `### Scope`, `### Deviation Audit`, `### Quality` |
| SDD5 | cannot-verify items | SDD § The Task Loop, 3. Review the task (**cannot-verify items**) | R 36; Seat ~40 | Std, Fold; EX | "⚠️ Cannot verify from diff" |
| SDD6 | loop wiring | SDD § The Task Loop, 3. Review the task (**Loop wiring:**) | R ~66; Seat ~90 | Std, Fold; EX, BR | Fix wave opened on a MINOR-labelled intent or scope failure |
| SDD7 | verification gates | SDD § The Task Loop, 4. Verification gates (¶1–2) | R ~90 | Std, Fold; EX | Rarely visible: re-dispatch over missing evidence |
| SDD8 | snapshot blessing | SDD § The Task Loop, 4. Verification gates (**Snapshot/golden blessing**) | R 74 | Std, Fold; EX | `sdd/reports/task-<N>-snapshot-<k>.md`; controller-composed blind agent; `preserved` / `intent-visible` |
| SDD9 | fix ladder and 5-wave cap | SDD § The Task Loop, 5. The fix loop (**The ladder.**); 1. Dispatch the implementer (identity ¶) | R ~234; Seat ~60 | Std, Fold; EX | `Task <N>: implementer <agent id>`; `Task <N>: fix wave <W>/5 (…)`; fresh implementer at waves 4–5 |
| SDD10 | fix-report contract | SDD § The Task Loop, 5. The fix loop (**Every wave.**); implementer-prompt.md § After Review Findings | R 82; Ref ~80; Seat ~260 | Std, Fold, VS; EX, BR | `fixed` / `NOT CONFIRMED` answers appended to the report file |
| SDD11 | scoped re-review | SDD § The Task Loop, 5. The fix loop (fixed-findings bullet); re-review-prompt.md | R ~250 (SDD ~160 + CR ~91); Seat ~1,360 + card 439 | Std, Fold, VS; EX, BR | `crucible:re-reviewer`; `task-<N>-re-review-w<W>.md` / `wave-<n>-re-review.md`; `ADDRESSED` / `NOT ADDRESSED` |
| SDD12 | breaker | SDD § The Task Loop, 5. The fix loop (**The breaker.**) | R ~168 | Std, Fold; EX at wave 5 | `Task <N>: parked — … — ruling:`; `Task <N>: BLOCKED — …` |
| SDD13 | adjudication | SDD § Disputes and adjudication | R ~766 (SDD ~670 + CR 96) | All; EX, BR, FIN (red suite) | Controller-composed adjudicator; `task-<N>-adjudication-<b>.md` / `branch-review/adjudication-<b>.md`; `UPHELD` / `DISMISSED`; `pending operator` |
| SDD14 | no controller fixes | SDD § The Task Loop, 5. The fix loop ("Never fix findings yourself…") | R ~150 | Std, Fold; EX, BR (lifted on VS) | Fixes always from implementer dispatches |
| SDD15 | what a report voices | SDD § What a report voices | R ~227; Seat ~260 | All; EX, BR | `Concerns:`, `Questions: Q1…`, "Proposals outside the task" headings in reports |
| SDD16 | leads | SDD § Setup (**Leads** bullet); requesting-code-review § The branch-review loop (**Questions and leads.**) | R ~230; Ref ~40; Seat ~120 | All; EX → BR | `Task 3: lead (question): …`; `CONFIRMED` / `RECOMMENDED` / `LEFT` |
| SDD17 | implementer status and stop-and-ask | SDD § The Task Loop, 2. Handle the report; implementer-prompt.md § Stop-and-Ask Triggers, § Report Format | R ~160; Seat ~215 | Std, Fold, VS; EX, BR | `Status: DONE | DONE_WITH_CONCERNS | BLOCKED | NEEDS_CONTEXT` |
| SDD18 | Decision Log and deviation audit | implementer-prompt.md § Binding vs Advisory: the Deviation License; SDD 3. Review the task (deviation-audit verdict) | R ~85; Seat ~210 | Std, Fold, VS; EX, BR | `Decision Log` section; deviation-audit verdicts |
| SDD19 | test-first with RED evidence | implementer-prompt.md § Tests: Test-First, Evidence Before Done | R ~30; Seat ~175 | Std, Fold, VS; EX, BR | RED output then GREEN output in reports; logged exceptions |
| SDD20 | weakened or deleted test rule | SDD 3. Review the task (**scope** verdict); templates' Scope / Testing passages | R ~40; Seat ~310 | All; EX, BR | Decision Log deletion justifications; scope findings |
| SDD21 | build-history ban | implementer-prompt.md § Code Organization; reviewers' Quality / What to Check / Scope | Seat ~210 (+ comment-convention lines ~135) | All; EX, BR | Findings citing "build history" |
| SDD22 | `Review: branch only` mark | writing-plans § Per-task structure — four fields, all required (**The review mark**); criterion in premise-and-questions § The arrangement questions | R ~757 across 5 skills; Ref ~300; Seat ~500 | Std, Fold; PP / SC grading, EX, BR, FIN | `Review: branch only — <reason>`; `Task <N>: complete (…, branch review only)`; `### Task Lines`; `[BRANCH_ONLY_TASKS]` |
| SDD23 | revert-and-replan with DRIFT | SDD § Revert-and-replan | R ~292 (SDD ~209 + CR 83); Seat ~50 | Std, Fold; EX, BR | `Task <N>: reverted — …; replanned as attempt <X>`; `DRIFT`; `-x<X>` report names |
| SDD24 | inline mode | SDD § Inline mode | R ~160; Ref ~60 (very-small-lane) | Std, Fold; EX; VS implementation | Controller-written `sdd/reports/task-<N>-report.md`; switch to dispatch on any loop finding |
| SDD25 | Finish record checks | SDD § Finish (step 1) | R 103 | Std, Fold, VS; FIN | "gaps" list in the close readout |
| SDD26 | close readout and answer | SDD § Finish (steps 2–3, restart rule); finishing § Overview (**After a close readout**) | R ~485 | Std, Fold, VS; FIN | Close readout message ending with a recommendation; wait for the answer |
| SDD27 | open-items routing | formats.md § Open items | R ~140; Ref ~450 | All; FIN, UL, UC | Ask where open items go and offer to record the answer; items written to the named home (this repo: `docs/backlog/`) |
| SDD28 | Finish suite run | SDD § Finish (step 5); requesting-code-review § The branch-review loop (**Finish's red suite.**) | R ~232 | Std, Fold, VS; FIN | Suite summary line shown before integration; a red run opens a branch wave |
| SDD29 | very-small lane execution | very-small-lane.md § The very-small lane | R ~146; Ref ~900 (read on entering the lane) | VS; EX, BR, FIN | Ledger `## Lane` section (`Lane:`, `Gates:`, `Implementation complete:`, `Departure:`, `Wave <n>:`); `sdd/reports/lane-report.md` |
| SDD30 | Lane Fit verdicts | code-reviewer.md § Binding Content (`[[when lane = very-small]]` passage) | Ref ~70; Seat ~150 | VS; BR | `### Lane Fit` with `EXCEEDS SHAPE` / `WITHIN SHAPE` and `GOAL MATCHES` / `GOAL DIFFERS` |
| SDD31 | upgrade hatch | very-small-lane.md (**The upgrade hatch.**) | Ref ~185 | VS; BR | `Hatch:` ledger line; ask "stay on the lane or move to standard" |
| SDD32 | goal check | premise-and-questions.md § The goal check | R ~10; Ref 186; Seat ~175 | All; SC, PP, BR (not the task reviewer, not the terminal pass) | `## Goal check` (seat) / `### Goal Check` (branch review) |
| SDD33 | seat Questions section | premise-and-questions.md § Questions | Ref 76; Seat ~110 | All seats | `## Questions` with `QUESTION s1-q1` or `Q1` lines |
| SDD34 | binding-item and unrecorded-choice findings | premise-and-questions.md § Binding items and unrecorded choices | Ref 88; Seat ~75 | SC, PP, BR, UC | Findings that a choice has no recording decision |
| SDD35 | seat git conduct | implementer-prompt.md § Where You Work | Seat ~260 (implementer ~100 + reviewers' read-only lines) | All; EX, BR | `git add <paths>` (never `-A`); no `-c user.*` |
| SDD36 | diff-as-files | task-reviewer-prompt.md § Diff Under Review; code-reviewer.md § Git Range to Review; re-review-prompt.md § The Fix | R ~155 (SDD adjudicator ~70 + HEAD~1 notes, CR 67); Seat ~320 | EX, BR | `git diff --stat --patch -U10 --output=<scratch>/range.diff`; `git cat-file -t`; `git merge-base --is-ancestor` |

### requesting-code-review (`SKILL.md` 2,755; `code-reviewer.md` 2,989 + card 449)

| ID | Name | Owner text | Resident cost | Reach | Observable signature |
|---|---|---|---|---|---|
| CR1 | branch reviewer seat | requesting-code-review § Dispatch the branch reviewer; code-reviewer.md | R ~415; Seat ~1,250 + card 449 | All (Std, Fold, VS; standalone); BR | `crucible:branch-reviewer`; `sdd/branch-review/pass-<k>.md`; "Ready to merge?" |
| CR2 | branch-review loop and 3-wave cap | requesting-code-review § The branch-review loop (steps 1–4) | R ~560 | Std, Fold, VS; BR | `Branch wave <n>/3 (…)`; `wave-<n>-fix.md`; successive `pass-<k>.md` |
| CR3 | ledger triage and ruling consistency | code-reviewer.md § Execution Trail; requesting-code-review § The branch-review loop (**Minors.**) | R ~163; Seat ~230 | Std, Fold, VS; BR | `### Ledger Triage` with `PROMOTE` / `FIX-IN-WAVE` / `LEAVE-PARKED`, `CONSISTENT` / `CONTRADICTED` |
| CR4 | cleanup wave | requesting-code-review § The branch-review loop (**The cleanup wave.**) | R 143 | Std, Fold, VS; BR | `Branch wave <n>/3 (cleanup, …)`; `Wave <n> (cleanup):` |
| CR5 | labelled changes | requesting-code-review § The branch-review loop (**Changes that ride a wave**) | R 110; Ref ~40; Seat ~30 | Std, Fold, VS; BR | `Change (improvement|ruling|requested): …`; `declined:` lines under `## Questions` |
| CR6 | rulings and requested work open waves | requesting-code-review § The branch-review loop (**Rulings and requested work.**) | R ~115 | Std, Fold, VS; BR, FIN | A wave opened after a close-readout answer |
| CR7 | standalone mode | requesting-code-review § Standalone mode | R ~190; Seat ~62 | Outside SDD | Report returned as the final message; `none` slots |

### writing-plans (`SKILL.md` 2,056)

| ID | Name | Owner text | Resident cost | Reach | Observable signature |
|---|---|---|---|---|---|
| WP1 | plan format | writing-plans § Plan header, § Per-task structure — four fields, all required, § What a plan never contains, § Binding vs advisory, § Task sizing | R ~620 | Std (Fold through BS22); plan writing | `plan.md` header sections and Why / Files / Contract / Acceptance per task |
| WP2 | spec pointer pin | writing-plans § Plan header (**Spec pointer**) | R ~235 (WP ~180 + SDD ~55); Ref ~90 | Std, Fold; PP onward | ``Spec: `…/design.md` @ `<rev>` ``; `Spec: this document` |
| WP3 | plan self-review | writing-plans § Self-review | R 137 | Std, Fold; plan writing | None |
| WP4 | decision-record attribution | writing-plans § Per-task structure — four fields, all required (**Files**, last sentence) | R ~55; Seat ~85 | Tasks that write decision records | `bases PASS|FAIL|n/a` in Task Lines; `brainstorm-decisions.md` named in a task's inputs |
| WP5 | acceptance-to-check mapping | writing-plans § Acceptance maps to checks | R ~270 (WP 163 + BS 54 + SDD 53); Ref ~40; Seat ~45 | All; BS, plan, EX | Acceptance mapping section; one-time checks with command, output and a failing pre-change run |

### finishing-a-development-branch (`SKILL.md` 1,917)

| ID | Name | Owner text | Resident cost | Reach | Observable signature |
|---|---|---|---|---|---|
| FIN1 | finishing guards | finishing § Step 2: Detect Environment, § Step 3: Determine Base Branch, § If your human partner asks to discard the work, § Step 6: Cleanup Workspace, branch-safety notes, § Common Rationalizations | R ~700 | All; FIN, UL | Three `git rev-parse` calls; "Type 'discard' to confirm."; `git branch -d` (never `-D`) |
| FIN2 | integration test verification | finishing § Step 1: Verify Tests; merged-result test in Option 1 | R ~200 | All; FIN | "Tests failing (<N> failures)"; test run after the local merge |
| FIN3 | records-in-PR question | finishing § Option 2: Push and Create PR (**Ask about the records.**) | R ~150 | All; FIN (PR option) | `git diff --name-only --diff-filter=A <base>...HEAD -- <feature-folder>`; the question to the operator |
| FIN4 | integration options menu | finishing § Step 4: Present Options; § Quick Reference | R ~215 | All; FIN, UL | "Implementation complete. What would you like to do?" |

### using-git-worktrees (`SKILL.md` 1,713)

| ID | Name | Owner text | Resident cost | Reach | Observable signature |
|---|---|---|---|---|---|
| WT1 | worktree isolation | using-git-worktrees § Step 0: Detect Existing Isolation, § Step 1: Create Isolated Workspace (1a, 1b, Directory Selection, Create the Worktree) | R ~1,060 | All; BS (spec write), EX setup | `git rev-parse --absolute-git-dir` / `--git-common-dir`; native worktree tool or `git worktree add <dir>/<branch> -b <branch> <base>` |
| WT2 | worktree-dir ignore check | using-git-worktrees #### Safety Verification (project-local directories only) | R ~264 | All; BS / EX setup | `git -C <root> check-ignore -q <dir>/` |
| WT3 | clean baseline | using-git-worktrees § Step 2: Project Setup, § Step 3: Verify Clean Baseline | R ~166 | All; EX setup | "Worktree ready at … Tests passing (<N> tests, 0 failures)" |

### receiving-review (`SKILL.md` 515)

| ID | Name | Owner text | Resident cost | Reach | Observable signature |
|---|---|---|---|---|---|
| RR1 | receiving-review discipline | receiving-review (whole body) | R ~480 | Outside crucible's loops: operator, PR, standalone review | Each item restated; pushback with evidence; ask to the operator |

### systematic-debugging (`SKILL.md` 1,491; technique files 1,931)

| ID | Name | Owner text | Resident cost | Reach | Observable signature |
|---|---|---|---|---|---|
| SD1 | root-cause-first discipline | systematic-debugging § The Iron Law, § The Four Phases (Phases 1–4, steps 1–3) | R ~1,100 (borderline core work) | All; any bug or unexpected behavior, implementers included | "I think X is the root cause because Y"; failing test before fix |
| SD2 | 3-fix architecture breaker | systematic-debugging § The Four Phases, Phase 4 steps 4–5; Red Flags line | R ~180 | All | "3+ fixes failed", a question about the architecture to the operator |

### writing-skills (`SKILL.md` 1,546)

| ID | Name | Owner text | Resident cost | Reach | Observable signature |
|---|---|---|---|---|---|
| WS1 | skill evaluation protocol | writing-skills § Evaluating a skill, ### Micro-test wording first, ### When the guidance isn't working | R ~469 | Text that instructs agents (implementers log the prose-only exception and leave evaluations to the controller) | Micro-test dispatches with a no-guidance control and ≥5 repetitions |

---

## Mechanism sections (3: restatements, 6: stated purpose, 7: consumers, 8: justification)

### using-crucible

**UC1 skill-check rule.**
- Restatements: none outside the router. The Skill Index restates every skill's description.
- Purpose: "work started without them usually has to be redone".
- Consumers: every skill's entry. If it goes, entry relies on host description-matching alone.
- Why: session-start-hook.md § The router (N, plus M for runs and one S). Basis tags: judgment; measured; "a single incident; measured, for the runs".

**UC2 trivial-edit waiver.**
- Restatements: Red Flags row "The skill is overkill"; routes.md.
- Purpose: an offered exit for "a typo, a comment, wording the operator dictated".
- Consumers: requesting-code-review's mandatory trigger relies on it ("an edit made under the trivial-edit waiver is already outside the process", branch-review.md).
- Why: routes.md § The waiver. N, explicitly unmeasured ("The waiver is unmeasured").

**UC3 evidence-before-claims.**
- Restatements: implementer-prompt.md § Tests: Test-First, Evidence Before Done (~95 words, "read that output … whatever a notification has promised"); systematic-debugging Phase 4 step 3; finishing § Step 1 ("a run on exactly the HEAD … counts").
- Purpose: "before saying work is complete, fixed or passing, run the check that shows it".
- Consumers: none mechanical.
- Why: evidence-and-findings.md § Evidence before claims. N for the router line (external, upstream); M for the implementer clause ("Twice an implementer acted on a suite outcome no tool had shown it").

**UC4 compaction re-read.**
- Restatements (Grep "after compaction", 16 lines): brainstorming 3, redteaming 6, SDD 4, requesting-code-review 1, finishing 1, using-crucible 1. Every "read … in full … re-read it after compaction; it binds as if written here" stub carries it.
- Purpose: a skill "whose text came back cut short" is re-invoked; references are re-read because the host re-attaches skills but no files read beside them.
- Consumers: every reference-loaded mechanism. Without it, references silently drop out after compaction.
- Why: authoring-crucible.md § References read on demand. N (external: Claude Code docs).

### brainstorming

**BS1 brainstorm-first gate.**
- Restatements: using-crucible § The Rule (**Brainstorm before planning**); SDD § Setup ("A plan crucible did not produce goes to `crucible:brainstorming`"); writing-plans § Overview (Input); finishing Option 2 and receiving-review ("new scope is a new feature").
- Purpose: "Simple features are where unexamined assumptions waste the most work."
- Consumers: everything downstream; BS5's route entry exists only because BS runs.
- Why: brainstorming-first.md § Brainstorm first. N (external, as surveyed; judgment).

**BS2 worktree before the spec.**
- Restatements: using-git-worktrees § Step 0 ("brainstorming closes its design presentation with one"), § Overview and 1a/1b ("brainstorming starts a feature inside another feature's worktree").
- Purpose: "the spec, the workspace and the records all live in the feature worktree".
- Consumers: BS16 workspace location; SDD § Setup's find-the-workspace step.
- Why: worktrees.md § Worktree first. N.

**BS3 arrangement presets.**
- Restatements: SDD intro ¶ and § The very-small lane ("the third route, alongside the standard and folded presets"); redteaming § The folded lane; very-small-lane.md intro; folded-lane.md.
- Purpose: "Each choice is made where its information exists"; combinations are unsupported "each for its reason".
- Consumers: BS5 route entry, RT38, SDD29, SDD22 (per-task review is the plan's choice).
- Why: routes.md § Separable choices. N for the form (preference and judgment); M for keeping folded ("about nineteen features used it").

**BS4 overturn selector (step 4).**
- Restatements: premise-and-questions § The arrangement questions (owner of the question; Grep "overturn": 2); redteaming SKILL 4, seat-prompt 3, terminal-pass 2, formats 3, very-small-lane 2, code-reviewer 1, flip-paths 1. Those are mostly RT23, RT24, RT29 and SDD30 uses of the same question.
- Purpose: a campaign "where overturning a major mechanism after code is reasonably expected".
- Consumers: BS5 (the proposal states the answer); SDD24 and SDD22 share the overdetermined test and the mark's criterion from the same section.
- Why: routes.md § The overturn question as the selector. N for adoption ("approved as a hypothesis"); M for the audit's corrections to its wording.

**BS5 preset confirmation and route entry.**
- Restatements: folded-lane.md (**Entry is not yours to declare.**); very-small-lane.md (**Entry is the operator's, and only at brainstorming.**); redteaming § The folded lane; SDD § The very-small lane; brainstorming § Handoff.
- Purpose: "a fold or a lane with no entry is one nobody downstream can see, and reads as unconfirmed".
- Consumers: RT38 (reads the confirmation before round 0), SDD29 (requires the entry), the terminal pass's RT30 (process entries are exempt).
- Why: routes.md § Separable choices and § The very-small lane. N.

**BS6 verification at writing.**
- Restatements: brainstorming § Spec self-review check 5; lane-note.md; writing-plans § Self-review check 4; RT14 record hygiene is the controller-side twin.
- Purpose: "an unenumerated consumer and an unchecked claim are the two largest measured finding classes".
- Consumers: RT2 round 0 and the seats' finding hygiene read the `UNVERIFIED` tags as declared input.
- Why: evidence-and-findings.md § Evidence on the author's side. M ("about 40% of findings corrected a false, mechanically checkable claim", ~1,620 findings).

**BS7 spec contract format.**
- Restatements: folded-lane-document.md ("The full six-section shape stays"); umbrellas.md #### Shape; every template's binding pointer names "Constraints & invariants" by name.
- Purpose: sections the reviewers "bind to". "No code beyond illustrative fragments in advisory sections."
- Consumers: BS8 (what binds is section-keyed), RT13, every template.
- Why: the-spec.md § Intent at the spec's altitude. M (Decisions sections grew 2.8–5.4× across four campaigns).

**BS8 binding-content model.**
- Restatements: SDD § The Task Loop (**Deviations.**, ~150 words); writing-plans § Plan header (Spec pointer) and § Binding vs advisory; dispatch-composition.md item 4; flip-paths.md intro. The Binding Content / What Was Requested / Requirements / Binding vs Advisory paragraphs of seat-prompt, terminal-pass-prompt, code-reviewer, implementer, task-reviewer and re-review restate it at ~150–230 words each. Grep "LOAD-BEARING" hits 14 files and "firm preference|firm decision" hits 17.
- Purpose: "binding text is never changed silently"; "a case its literal reading reaches that its author plainly did not consider [is] raised for a ruling, never applied literally".
- Consumers: RT39, RT40, SDD17 (BLOCKED with correction), SDD23 (drift from binding content reverts), every review verdict.
- Why: the-spec.md § Weights and flip paths (N, preference) and § The spec as a hypothesis (M: a sample, 3 of 29 marks and 9 of 36 Constraints items had any binding event).
- Note: the clause is copied into six templates although the clause itself says "a copy drifts against the artifact it copies". That copy is about the rule, not the spec.

**BS8b literal-reading finding.**
- Restatements: task-reviewer § What Was Requested; code-reviewer § Binding Content; re-review § Requirements; implementer § Binding vs Advisory; SDD § Disputes and adjudication (**Who rules.**); flip-paths § The containment test (rulings "pass this test whichever way it goes"). Grep: 15 lines over 9 files.
- Purpose: the case of "a controller applying a Constraint literally to an edge case its author plausibly never considered".
- Consumers: SDD13 (controller rules on it as a plan conflict), RT40.
- Why: task-loop.md § The implementer contract and adjudication.md § Who rules. M for the case (one case in the sample); N for the rule.

**BS9 `[LOAD-BEARING]` mark.**
- Restatements: every binding clause (see BS8); flip-paths § The containment test ("a mark names what builds on it").
- Purpose: binds "exactly the sentence or bullet it annotates … only where something beyond that sentence builds on the decision".
- Consumers: RT40 reads what the mark names; the binding clauses.
- Why: the-spec.md § The spec as a hypothesis. M (counts: 27 and 15 marks in the first two specs, 0–7 since; the operator: "load-bearing marks are used too liberally and result in bureaucracy").

**BS10 decision statuses.**
- Restatements: formats.md § Design digest format (status field) and **Later operator rulings…** ("delegated status"); terminal-pass-prompt mandate 2 (the delegated-call check); RT30.
- Purpose: `accepted` means "this until new evidence arrives"; `firm` only "on the operator's explicit word"; "your call" is never recorded as the operator's ruling.
- Consumers: RT28 (delegated check), RT30, RT41 (premise protects firm decisions), WP4 (attribution reads proposer and status), BS5 (the route entry confirms only when `accepted` or `firm`).
- Why: the-spec.md § The spec as a hypothesis; decision-records.md § Origin and strength. N (judgment; "your call" left to the agent).

**BS12 deferral chain.**
- Restatements (Grep "Deferred to implementation|deferred-to-implementation|routing table": 34 lines over 12 files):
  - redteaming § Merge and finding hygiene (**Deferral**, 231 words) and the fix-altitude marker;
  - readout deferred count;
  - plan-phase.md (rows appended by fix items); folded-lane.md (**Deferrals are kept per round.**);
  - SDD § Setup (**The deferred list**), step 1 reminder, step 3 routed-item check;
  - implementer § Binding vs Advisory (**Deferred to you**) and § Report Format;
  - task-reviewer Verdict 3 and report; code-reviewer § Execution Trail;
  - `[LEDGER_MINORS]` slot; self-review exemptions in brainstorming and writing-plans.
- Purpose: "they are the only record that the items were deferred rather than forgotten"; "Binding and cross-task content is never deferrable."
- Consumers: SDD1 ledger, SDD4 deviation audit, CR3 sweep ("an item omitted here is closed nowhere"), SDD22 (marked tasks shift the check to the gate and the branch reviewer).
- Why: the-spec.md § Intent at the spec's altitude (M: 60–90% of round-2+ findings introduced by fix waves, under a rule that forbade deferring BLOCKER/MAJOR findings); plans.md § A lean contract (N).

**BS13 spec self-review.**
- Restatements: brainstorming § Flow step 6; lane-note.md; umbrellas.md #### Review; writing-plans § Self-review is its plan sibling (WP3).
- Purpose: fix inline, "no re-review loop".
- Consumers: none mechanical.
- Why: brainstorming-first.md / upstream-skills-kept-close.md. N (external, upstream).

**BS14 consumer sweep.**
- Restatements: writing-plans § Per-task structure (**Files**: "by search, not from memory"); redteaming RT18 ("run `crucible:brainstorming` § Spec self-review's consumer sweep"); lane-note.md.
- Purpose: "A rule stated in more than one place … is such an interface."
- Consumers: RT18.
- Why: evidence-and-findings.md § Evidence on the author's side (M: ~29% of ~1,620 findings were unenumerated consumers or producers); the-spec.md § Restated rules (M).

**BS15 trace (routes × phases).**
- Restatements: redteaming RT18; code-reviewer.md § What to Check ("For each rule the branch ties to a trigger…").
- Purpose: "where X occurs and nothing reaches the rule, the design has a gap".
- Consumers: RT18, CR1.
- Why: the-spec.md § The trace. S (umbrella-specs feature, 2026-10-28).

**BS16 feature workspace.**
- Restatements (Grep "provisioning": 16 lines): brainstorming 5, formats 5, SDD 2 (§ Setup find-first, § Finish step 6), redteaming 1, umbrellas 1, folded doc 1; conserve.py 1.
- Purpose: one workspace per feature, "living until an end its Lifecycle names"; "No orphan workspaces".
- Consumers: everything that writes records (RT6, SDD1, BS17–BS19, RT43 scratch).
- Why: records-and-workspace.md § The workspace. M for the host facts (UTF-16LE `.gitignore`) and for dropping the config; otherwise external or preference.

**BS17 brainstorm decision record.**
- Restatements (Grep "brainstorm-decisions.md|brainstorm decision record|decision record": 52 lines over 20 files):
  - SDD outcomes ¶; redteaming § Round readout (post-close rulings); requesting-code-review cap step;
  - flip-paths intro; very-small-lane.md;
  - terminal-pass slot `{decision-record-path}`; writing-plans Files; implementer, task-reviewer, code-reviewer (WP4).
- Purpose: "This record is the digest's first derivation source"; every later operator ruling is entered "beside wherever its own phase records it".
- Consumers: BS19 digest, BS20 gate entry, RT30, RT34 launch, SDD29 entry check, WP4.
- Why: the-spec.md and records-and-workspace.md. N. The RT30 consumer: M (audit 4/10).

**BS18 request file.**
- Restatements (Grep: 23 lines over 12 files): formats.md (layout comment, appends); premise-and-questions § The goal check; redteaming § Round readout; SDD outcomes; requesting-code-review inputs and cap; flip-paths intro; very-small-lane.md (2); seat-prompt and code-reviewer; slot cards.
- Purpose: "evidence of what was asked, not the standard, and seats check the Intent against it".
- Consumers: SDD32 goal check; SDD30 GOAL verdict.
- Why: the-spec.md § The request. N (judgment). The move out of committed folders followed the privacy problem of published messages; no count is cited.

**BS19 design digest.**
- Restatements (Grep "digest": 35 lines): redteaming § Round readout item; § Exit; flip-paths (premise carried in `## Open judgments`); folded-lane.md ("no digest"); very-small-lane.md.
- Purpose: "crucible's default operator steers by decision asks rather than by reading specs or code".
- Consumers: BS20 gate; RT21 (digest-update item); RT41 carrying.
- Why: operator-steering.md § One gate for design and launch. N (preference).

**BS20 digest gate.**
- Restatements: redteaming § Panels (**Launch:** "proceed — no approval wait"); formats.md layout ("the gate entry included"); plan-phase.md and writing-plans § Exit ("the announcement is not an approval gate", stated as the contrast).
- Purpose: "approving the design approves the launch".
- Consumers: RT1 launch reads the gate entry; RT4's swap is named in it.
- Why: operator-steering.md § One gate for design and launch. N (preference: "I basically never adjusted the shape").

**BS21 lane note.**
- Restatements: very-small-lane.md (**The note is the lane's only artifact, and it is frozen.**); brainstorming § Proposing the arrangement (Very-small bullet); code-reviewer, implementer and re-review lane passages; slot cards.
- Purpose: "Intent, Acceptance and Out of scope are binding for the branch reviewer; the change list is advisory."
- Consumers: SDD29, SDD30, CR1 requirements.
- Why: routes.md § The very-small lane. N (judgment: one gate for the note and the proposal).

**BS22 folded document.**
- Restatements: writing-plans § Plan header (folded form); folded-lane.md; formats § Feature folder.
- Purpose: one combined document, keeping "Constraints & invariants least of all" out of folding away.
- Consumers: RT38, SDD (plan pointer names the combined document).
- Why: routes.md § One process for review, lighter documents. N for the fold; S for "the run".

**BS23 feature folder.**
- Restatements (Grep "birth step|resolve step": 10 lines over 9 files): brainstorming; writing-plans; flip-paths; umbrellas 2; folded doc; lane note; finishing; very-small-lane.
- Purpose: "a new feature never resolves into a finished feature's folder"; "a feature never has a second home".
- Consumers: WP2 pins, FIN3, RT39 successor names, SDD31 hatch.
- Why: records-and-workspace.md § The feature folder. N.

**UM1 umbrella file.**
- Restatements: brainstorming § The dialogue (scope-decomposition check), § Spec self-review check 3, § Proposing the arrangement stub; formats § Feature folder (`umbrella.md`).
- Purpose: "readable in its current state from one file".
- Consumers: UM4, UM5, UM8, the resume rule.
- Why: umbrellas.md § One file, read in its current state. M (by reading the documents of crucible's runs and one other project) plus preference.

**UM2 umbrella review choice.**
- Restatements: brainstorming § Handoff; redteaming § Exit; premise-and-questions (the overturn reading for an umbrella).
- Purpose: review "chosen by its content … it has no code of its own to review after".
- Consumers: BS20 (none for approval-only); RT1.
- Why: umbrellas.md § Review by content. N.

**UM3 umbrella landing.**
- Restatements: redteaming § Exit (umbrella bullet); flip-paths § Premise findings (carrying bullet 4); formats § Feature workspace (Lifecycle); finishing § Overview.
- Purpose: "children branch from a base that holds it and other sessions can read it".
- Consumers: UM5 (children's marks need the landed file), SDD27.
- Why: umbrellas.md § Work left open at the landing and § An open premise ask at the landing. N.

**UM4 umbrella line binding.**
- Restatements (Grep "Umbrella:|umbrella line|UMBRELLAS|umbrella-paths": 40 lines over 22 files):
  - dispatch-composition items 2 and 4;
  - writing-plans § Plan header; SDD § Setup (pre-flight), step 1 (receiving step), **Deviations.**, adjudicator inputs;
  - requesting-code-review inputs and the receiving-step ¶; very-small-lane.md;
  - all six templates and all six cards.
- Purpose: "Each seat reads them in its own worktree, never from a copied block."
- Consumers: SDD3, SDD4/CR1 findings, RT40 (umbrella content is never contained).
- Why: umbrellas.md § The line, and what binds. N.
- Note: this is the largest seat-side restatement after BS8. Nine sentences of near-identical text recur in six templates.

**UM5 umbrella marks.**
- Restatements: SDD § Finish step 4 (169 words, including the `git grep` / `git cat-file -e` detection of children born before their umbrella); umbrellas #### Landing step 5; code-reviewer § What Was Built, Against What.
- Purpose: closing "is read from the marks, nothing waits".
- Consumers: UM1 resume rule, UM8 trigger, the umbrella's #### Closing state.
- Why: umbrellas.md § Marks. N.

**UM6 umbrella binding-change protocol.**
- Restatements: SDD § Setup (pre-flight clause); every binding clause ("a change to those Constraints … is a finding"); flip-paths § Under an umbrella….
- Purpose: a binding change "is never made on a child's branch".
- Consumers: UM4 receiving step.
- Why: umbrellas.md § Binding changes off the child's branch. N.

**UM7 late split.**
- Restatements: redteaming § Flip paths stub; SDD § Plan changes mid-execution; formats § Lifecycle ("a late split's included").
- Purpose: a split found late "is an operator decision ask".
- Consumers: UM5 (`dropped` mark).
- Why: umbrellas.md. N.

**UM8 umbrella closing review.**
- Restatements: SDD § Finish step 2; finishing Option 1 (Grep "closing review|closing-": 8 lines over 5 files); premise-and-questions § Premise findings (lists closing seats); formats § Feature workspace and § Open items.
- Purpose: "nothing read across the children".
- Consumers: SDD27 open items.
- Why: umbrellas.md § The closing review. M (audit: 5 of 10 clusters).

### redteaming

**RT1 redteam panel.**
- Restatements: redteaming § Overview; seat-prompt.md (independence, full-scope lens); plan-phase.md (coherence seats); folded-lane.md; dispatching-parallel-agents (start all before waiting).
- Purpose: "Agents never see each other's reports"; a lens "only orders the search".
- Consumers: everything in SC.
- Why: spec-campaign.md § Panels and lenses. M (transcript study: 37 seat reports, ~360 findings; 60% of BLOCKERs found by ≥2 seats). The calibration is "thin, so it stays advisory".

**RT2 round-0 pre-pass and ordered-first hunt.**
- Restatements: formats § Round record format (Round-00 special record); folded-lane.md (**Round 0 always runs**); seat-prompt `[[when worksheet = ordered-first]]`; seat card selector; verifier-prompt ("round-0 treatment").
- Purpose: "a baseline claim table … plus a liveness check … and execution of regex/CLI claims".
- Consumers: round 1 seats ("the round-1 panel's full-scope read is the check on those fixes"); RT20b reuses its method.
- Why: spec-campaign.md § Round 0. M (14% of 141 classified findings; a liveness miss at round 16).

**RT3 right-sizing seat and over-subtraction guard.**
- Restatements: seat-prompt.md (5 lines); seat card (2); folded-lane.md (round-1 seat); formats field 8.
- Purpose: "judged by the scope-cut decisions it produces"; the guard: "cutting attested content requires a logged ruling".
- Consumers: fix waves consult `## Right-sized — do not cut`.
- Why: spec-campaign.md § Right-sizing. M (77% of rounds grew the artifact; a simplification lens "lost consistently") plus the maintainer's preference to keep the seat.

**RT3b wave line counts.**
- Restatements: formats.md field 8 Trace.
- Purpose: "Their net is the signal the right-sizing re-seat trigger judges."
- Consumers: RT3 re-seat judgment only.
- Why: spec-campaign.md § Right-sizing. M (the predecessor token-count trigger ran 116 times; one re-seat found 3 MAJORs).

**RT4 round-1 alternate-role swap.**
- Restatements: dispatch-composition § Models and effort (first trigger); brainstorming § Digest gate (shape names models); slot cards' Model lines.
- Purpose: "the seat you judge most architecture-heavy runs on the alternate role".
- Consumers: BS20 campaign shape.
- Why: model-roles-and-effort.md § The alternate role. N (preference).

**RT5 quorum, degraded rounds and top-up.**
- Restatements: formats field 3; plan-phase.md (**A degraded round is not a loop**); ST3.
- Purpose: "a crashed seat is never read as a clean pass"; "two consecutive degraded rounds = infrastructure escalation".
- Consumers: RT26 cap arithmetic, RT10 (degraded-round verdicts).
- Why: spec-campaign.md § Quorum and degraded rounds. N.

**RT6 round records, state line and rehydration.**
- Restatements: formats.md (Grep "state:|state line|rehydrat": formats 3, redteaming 3); plan-phase.md ("states running through `confirmed`").
- Purpose: "every judgment is computed from the records, never from conversation memory".
- Consumers: RT10, RT20 (fix list), RT23, RT26, RT27 inputs, rehydration.
- Why: `UNVERIFIED`. No decision record names the state line ("state line|rehydrat" matches nothing in docs/decisions/). The closest Why is task-loop.md § The spine's upstream ledger reason (controllers re-dispatching completed work after compaction; external).

**RT7 merged finding list and dispositions.**
- Restatements: formats.md field 5 (origins element, deferral); terminal-pass-prompt (finds seat findings through `origins:`).
- Purpose: "Silent discard is forbidden."
- Consumers: RT10, RT21 coverage, RT28.
- Why: fix-verification-and-merge.md § Dispositions and the sub-point check. M.

**RT8 seat index and merge from indexes.**
- Restatements: seat-prompt Report item 3; plan-phase.md (`## Index` in `seat-p0.md`).
- Purpose: "an advisory merge aid that nothing checks against the findings".
- Consumers: the controller's merge only.
- Why: fix-verification-and-merge.md § Merging from indexes. M (records were 23% of characters the controller read; "Nothing has held an index to its findings since … an accepted gap").

**RT9 sub-point check.**
- Restatements: none found.
- Purpose: "an unaddressed sub-point is added to the item or ruled in the entry".
- Consumers: RT16.
- Why: fix-verification-and-merge.md § Dispositions and the sub-point check. M (twice in one feature, then three more recorded cases; "the one control, at fix authoring, for a fix narrower than its finding").

**RT10 merge conservation.**
- Restatements (Grep "conserv": redteaming 6, formats 4, plan-phase 1, conserve.py 8).
- Purpose: "Every raw seat finding is accounted for."
- Consumers: RT6 quorum block.
- Why: fix-verification-and-merge.md § Conservation. M. The record reads, over 193 rounds: "at most one real catch of a dropped finding"; 7 exit-1s, 3–4 of them parser false positives; 9 exit-2s, each a format problem costing a repair cycle.

**RT11 question dispositions.**
- Restatements: formats field 5 (**Question dispositions**); readout item; terminal-pass mandate 2 (quote check); plan-phase.md and folded-lane.md (mark-proposal rule).
- Purpose: "A question that doubts the request, what the Intent asks for or a firm decision is always carried to readout."
- Consumers: RT21, RT28.
- Why: evidence-and-findings.md § Premise findings, the goal check and questions. M (questions answered 47, adopted 12, rejected 1, carried 0 across three features).

**RT12 finding hygiene.**
- Restatements: seat-prompt § Finding hygiene; terminal-pass report; task-reviewer § Finding Hygiene and Severity; code-reviewer § Calibration; re-review; implementer claim discipline; premise-and-questions § Location.
- Purpose: "a BLOCKER without reproduction/evidence is a question".
- Consumers: RT16 (no `UNVERIFIED` finding enters a fix list).
- Why: evidence-and-findings.md § Review that holds without a human reader. N (judgment; external FactReview study).

**RT13 finding scope.**
- Restatements: seat-prompt § Finding scope; terminal-pass mandate 1 (verbatim copy, ~170 words).
- Purpose: missing local detail "is not a finding at spec or plan stage".
- Consumers: BS12 (deferral is the point; "the detail is missing" is out of scope).
- Why: the-spec.md § Intent at the spec's altitude. M.

**RT14 record hygiene.**
- Restatements: formats § Round record format ("What the controller writes in them is under record hygiene").
- Purpose: an ask on an untagged false fact "is the measured channel by which author-supplied false facts reach ratified decisions".
- Consumers: RT28.
- Why: evidence-and-findings.md § Evidence on the author's side. M (15 of 16 overturning findings).

**RT15 operating stance.**
- Restatements: SDD § The fix loop (**Caught errors**); terminal-pass ("A discrepancy you find is a record correction, not a verdict on its author").
- Purpose: "disclosure against interest stays cheap — shading a record … is the only reportable failure".
- Consumers: RT31 (the stance names shading; the bias statement detects it).
- Why: spec-campaign.md § Operating stance. S (one session's retrospective, 2026-08-16).

**RT16 fix-list contract.**
- Restatements: formats field 6; plan-phase.md (contained-amendment item form); folded-lane.md.
- Purpose: "a fix that removes machinery outranks one that adds it"; the artifact "carries no finding citations".
- Consumers: RT20 (sole mandate input), RT17, RT18, RT19.
- Why: the-spec.md § Intent at the spec's altitude (M); fix-verification-and-merge.md.

**RT17 propagation sweep.**
- Restatements: formats field 6 (**Restating sites**).
- Purpose: "the measured dominant wave defect is the correct fix applied once while a sibling statement stands".
- Consumers: RT20 checks every named site.
- Why: the-spec.md § Restated rules. M (~1,620 findings classified).

**RT18 fix-item trace.**
- Restatements: none beyond formats field 6.
- Purpose: the sweep "does not follow the change to what consumes it".
- Consumers: RT20 via restating sites.
- Why: evidence-and-findings.md § Evidence on the author's side. M (6 of 10 audit clusters began in a fix wave). The record notes a cost "which word counts do not show".

**RT19 predicate is run, not read.**
- Restatements: plan-phase.md ("run it, don't read it"); lane-note.md (mechanical Acceptance run once); WP5 (failing pre-change run).
- Purpose: "that failure is the evidence it can fire".
- Consumers: RT20 checks only the landing.
- Why: evidence-and-findings.md § Evidence before claims. M ("twice recorded applied with nobody having run them").

**RT20 blind verifier.**
- Restatements: verifier-prompt.md; verifier card ("Blind by design"); formats field 7; plan-phase.md seat 3; dispatch-composition (alternate-role exclusion).
- Purpose: "early victory is the named verifier failure mode"; rationale withheld because a check shown the draft "tends to repeat the draft's errors".
- Consumers: RT6 `verified` state, RT23.
- Why: fix-verification-and-merge.md § Blind verification. M (study: 41 commits recording a fix-caused defect) plus external (CoVe, anchoring study).

**RT20b delta-claims check.**
- Restatements: verifier-prompt mandate 3; formats field 7.
- Purpose: "baseline verification doesn't end at round 0 when artifact growth doesn't".
- Consumers: the controller's own checks in the Verifier block.
- Why: fix-verification-and-merge.md § Blind verification. M (recount: half the later verifiers left delta claims unchecked; causation "an inference").

**RT21 round readout, trace and coverage check.**
- Restatements: formats field 8; SDD § Finish (the close readout is the analogue); terminal-pass inputs.
- Purpose: "no step requires reading spec, plan, code or diffs"; coverage: "nothing checks it after you".
- Consumers: BS19, RT27/RT28 via `Trace:`, RT3b, RT24.
- Why: fix-verification-and-merge.md § Readouts and the trace. M: the scripted coverage checks "ran 125 times … and never found a missing readout entry".

**RT22 decision-ask format.**
- Restatements: SDD § intro (**Continuous execution:**); requesting-code-review step 4; formats § Design digest format; flip-paths (repeated "analyst-language decision ask with a recommendation"); receiving-review § Who rules.
- Purpose: "Each ask lists every option the findings behind it propose, and states what its change withdraws."
- Consumers: RT28 checks fidelity.
- Why: operator-steering.md § Never required, never withheld. S (2026-10-08: the omitted middle option).

**RT23 stop rule (overturn question).**
- Restatements: premise-and-questions § The arrangement questions; formats field 8; flip-paths § Premise findings (the ruling's effect).
- Purpose: "Severity is not the trigger"; "A round whose own fix wave adds, removes or re-shapes a major mechanism is never the stop round."
- Consumers: RT27 (runs at the stop), RT29.
- Why: spec-campaign.md § Stop rule and cap. M (finding counts do not decay; 60–90% drift share; three stops by the question). Adopted "as a hypothesis with no demonstrated accuracy". Open: docs/backlog/campaign-early-stop-investigation.md.

**RT24 seat forecast lines.**
- Restatements: formats field 8 and trace; terminal-pass stop check; seat card (artifact kind gates the line).
- Purpose: "gives the stop a record the controller did not write".
- Consumers: RT21 overturn item, RT29.
- Why: spec-campaign.md § Stop rule and cap. S (2026-10-29 pilot: a round-2 stop flagged `CONCLUSION-CHANGING`).

**RT25 premise hold on the stop.**
- Restatements: flip-paths § Premise findings (**The ask.**); terminal-pass stop check.
- Purpose: the campaign "does not stop while the ask is pending".
- Consumers: RT29.
- Why: spec-campaign.md § Stop rule and cap. M (an audit finding about one sentence; judgment for the hold).

**RT26 campaign cap.**
- Restatements: formats (cap arithmetic, quorum block); plan-phase.md ("no round cap, no cap arithmetic"); flip-paths (the cap ask's supersede option).
- Purpose: "its guarantee that the campaign ends; the cap bounds rounds, not spend".
- Consumers: RT39 (the supersede option).
- Why: spec-campaign.md § Stop rule and cap. M, on thin data (cap fell from 6 to 4 on one feature's campaigns; a recount "supported neither raising nor lowering").

**RT27 terminal pass (artifact re-read).**
- Restatements (Grep "terminal pass|terminal-pass": 62 lines over 13 files; most mentions in redteaming SKILL 22, formats 14, plan-phase 7).
- Purpose: "A campaign never converges on unreviewed edits."
- Consumers: RT28–RT32; the second read.
- Why: terminal-pass.md § Why a pass at all. M (first read found a BLOCKER or MAJOR after the stop in 27 of 74 campaigns).

**RT28 decision-ask fidelity and `CONCLUSION-CHANGING`.**
- Restatements: redteaming § Overview ("why … the terminal pass checks each ask's fidelity"); formats (plan record: "A flagged correction is a decision ask").
- Purpose: "without a check it alone decides what the operator learns".
- Consumers: decision asks to the operator; RT31's escalation threshold.
- Why: terminal-pass.md § Fidelity of the asks. N for placement; M for samples and the audit-added checks.

**RT29 stop check.**
- Restatements: redteaming § Stop rule and terminal pass mandate 2; terminal card (spec inputs).
- Purpose: an unanswered forecast "is a mismatch, even where every seat of the stop round forecast `not reasonably expected`".
- Consumers: decision asks; the operator's extra round.
- Why: terminal-pass.md § Fidelity of the asks. M (probe: "one stop basis overstated").

**RT30 decision-record check.**
- Restatements: terminal card `{decision-record-path}`.
- Purpose: "An approval withdrawn with no such record is a correction flagged `CONCLUSION-CHANGING`."
- Consumers: decision asks.
- Why: terminal-pass.md § Fidelity of the asks. M (audit: approvals in no reviewer's inputs in 4/10 clusters; it "would have caught the first").

**RT31 directional-bias statement.**
- Restatements: terminal-pass-prompt (2 lines); redteaming SKILL (2).
- Purpose: "a set of individually immaterial corrections all leaning one way passes every one of them".
- Consumers: decision asks above the threshold; "Drift auditing across features is the operator's, mined from the terminal passes' reports".
- Why: terminal-pass.md § The bias statement. S for the observation (2026-08-15). The threshold came because the ask "had fired in nearly every campaign and never changed anything".

**RT32 terminal tail.**
- Restatements: formats (terminal-pass record, `second-read.md`); plan-phase.md (second read after repair); terminal card.
- Purpose: bounded to "at most one further fix wave + second read".
- Consumers: decision asks for anything still open.
- Why: terminal-pass.md § The tail. S ("One campaign ran a re-pass and then appended six re-checks").

**RT33 artifact freeze.**
- Restatements: none.
- Purpose: "fixes land between dispatches".
- Consumers: ST2 meaning.
- Why: shared-tree.md § Read windows. S (2026-08-07: a terminal pass saw a mid-read commit as a rogue agent).

**RT34 plan phase.**
- Restatements: writing-plans § Exit; redteaming § Overview, § Exit; formats (plan-phase record, `campaigns/plan/`).
- Purpose: "A plan is not campaigned"; "never loops".
- Consumers: SDD1 seeding (Close), RT40 (contained amendment lands in its wave).
- Why: plans.md § One round for the plan. M (late findings in the dual-runtime plan campaign were caused by its own edits; one plan terminal pass caught a last-wave MAJOR). The plan phase runs without approval: preference ("over 95% 'proceed'", "no count is recorded", operator-steering.md).

**RT35 plan arithmetic and post-wave re-run.**
- Restatements: writing-plans § Self-review check 2; folded-lane.md (two bullets); folded-lane-document.md ("the ownership census is the round-0 pre-pass's arithmetic input").
- Purpose: the census section "is arithmetic, and the plan phase runs it rather than reading it".
- Consumers: RT34 merge.
- Why: plans.md § One round for the plan. M.

**RT36 set census.**
- Restatements: seat card (3), plan-phase (2), folded-lane (1), seat-prompt (1).
- Purpose: "A place where the new member belongs that the plan's file census leaves out is a finding."
- Consumers: RT34 merge.
- Why: plans.md § One round for the plan. M (audit: 5 of 10 clusters). The record notes "It adds one table to every feature's plan phase, which word counts do not show".

**RT37 plan-phase repair paths.**
- Restatements: formats (plan-phase record; `second-read.md`); terminal-pass second-read passage.
- Purpose: "neither a loop".
- Consumers: RT34 `confirmed` state.
- Why: plans.md and terminal-pass.md § The tail. S for the tail's bound; N for the rest.

**RT38 folded-lane campaign rules.**
- Restatements: redteaming § The folded lane and § Exit (ledger seeding); brainstorming § Proposing the arrangement (Folded bullet); formats § Feature folder (unfold).
- Purpose: "The spec campaign … applies unchanged … only the artifact and the handoff differ."
- Consumers: SDD (direct handoff), BS12 per-round rows.
- Why: routes.md § Separable choices (M count of uses); § One process for review, lighter documents (N).

**RT39 flip paths.**
- Restatements (Grep "supersede|amendment marker|scoped amendment": 27 lines over 13 files): redteaming § Flip paths stub; SDD § Plan changes mid-execution; brainstorming § Spec contract; writing-plans; folded-lane (unfolding); formats § Feature folder (successor names); task-reviewer, re-review and cards (named amendment commits).
- Purpose: binding content "is never flipped by a fix wave".
- Consumers: SDD1 (predecessor links), SDD4/SDD11 scope verdicts (amendment commits).
- Why: the-spec.md § Weights and flip paths. N (preference). The move to one reference: authoring-crucible.md, M ("its two copies had drifted").

**RT40 containment test.**
- Restatements: SDD (BLOCKED ¶, **Who rules.**, **Outcomes.**, Setup seeding); plan-phase.md (**A contained amendment**); dispatch-composition item 4; writing-plans § Binding vs advisory and review mark; verifier-prompt (`Contained amendment:` items); the review cards' amendment-commit lists.
- Purpose: a contained change "is yours to confirm"; it "reaches the operator through readouts, never the design digest".
- Consumers: SDD1 `## Adjudication rulings`, SDD26 close readout, CR1 rulings input.
- Why: the-spec.md § The spec as a hypothesis. M (sample of 4 features, "order-of-magnitude only", report not committed) plus judgment.

**RT41 premise findings.**
- Restatements (Grep "premise": 78 lines over 20 files; premise-and-questions 10, redteaming 11, SDD 7, code-reviewer 7, flip-paths 6).
- Purpose: let a seat "say the spec, or the goal behind it, is wrong without costing a fix wave"; "it holds open no gate".
- Consumers: RT25, RT42-like carrying, BS19 `## Open judgments`, SDD26, UM3 (`open premise ask:`).
- Why: evidence-and-findings.md § Premise findings, the goal check and questions. M (escape analysis of 109 features: 2 premise-level MAJORs passed task reviews) plus preference for the aim.

**RT42 earlier-phase carriage.**
- Restatements: SDD § Setup (bullet 5); redteaming § Exit (folded bullet); umbrellas #### Landing step 3.
- Purpose: what earlier phases left open "had no carrier to Finish".
- Consumers: SDD26 close readout, SDD27.
- Why: records-and-workspace.md § Work left open. M (audit: 4/10 clusters lost when Finish deleted the ledger).

**RT43 focused checks and scratch.**
- Restatements (Grep "scratch": 33 lines over 9 files; every template).
- Purpose: "a focused check where a claim needs one, never a package-wide suite"; scratch keeps the tree check meaningful.
- Consumers: ST2.
- Why: spec-campaign.md § Focused checks (S: a 30-minute suite run beside other sessions); shared-tree.md (N for scratch).

**RT44 read scoping.**
- Restatements: 7 templates (1 line each in Grep, ~100 words each); requesting-code-review rationalization row.
- Purpose: "an unscoped grep is the measured way review exhaust reaches a seat that exists to be free of it".
- Consumers: RT20's blindness depends on it.
- Why: the-spec.md § Pointers, not copies. M ("all four recorded cases of a seat seeing what it should not were campaign exhaust").

**RT45 report-file contract.**
- Restatements (Grep "controller saved|with a mark": 6 lines over 5 files): every template's read-only line; SDD § Runtime identity (**Report files.**); claude-code-dispatch.md (**Report-name filter**).
- Purpose: "so whoever reads the workspace can tell the seat's text from text the controller transcribed".
- Consumers: SDD25, RT10 (reads seat reports on disk).
- Why: instruments.md § Report files. M (83 refusals, all on filter-matching names) plus S (the first refusal).

**RT46 instruments, slot cards and selectors.**
- Restatements: requesting-code-review § Dispatch the branch reviewer; every card's Dispatch section; every template's "Selected passages" ¶; both dispatch adapters.
- Purpose: "Read the card, not the template"; unselected passages are "dropped, not narrated".
- Consumers: all dispatches.
- Why: instruments.md § Instrument agents. M.

**RT47 seven-item dispatch composition.**
- Restatements: redteaming § Dispatch composition; SDD § Runtime identity in every dispatch; requesting-code-review; umbrellas #### Closing review; every template's Workspace / No delegation lines.
- Purpose: "Fill every slot; never trim one to shorten a dispatch."
- Consumers: all seats.
- Why: instruments.md § One composition and § No delegation. N.

**RT48 model roles and effort.**
- Restatements: SDD § Models; redteaming § Panels; requesting-code-review (dispatch and red flag); every card's Model line; host maps' Model roles entries.
- Purpose: "an omitted model silently inherits the session's"; "Effort is the operator's."
- Consumers: RT4, SDD9 escalation.
- Why: model-roles-and-effort.md. N (preference) for roles; M for effort (Codex default-effort measurement).

### Shared-tree rules

**ST1 no commit while a seat works.**
- Restatements: implementer § Where You Work (stage by name, no bare stash); using-git-worktrees (one hit, unrelated commit wording).
- Purpose: "the index is shared, so a bare commit sweeps in whatever that agent staged".
- Consumers: ST2.
- Why: shared-tree.md § Read windows. M ("three incidents in crucible's runs").

**ST2 tree check.**
- Restatements: formats (where readings go, 3 lines); plan-phase (1); requesting-code-review (1); "the tree check applies" in SDD steps 3 and adjudicator.
- Purpose: a changed tree voids "every report from it … until re-measured".
- Consumers: every review verdict's validity.
- Why: shared-tree.md § Read windows. N (judgment); the narrowing was declined because "no void it would have spared was on record".

**ST3 seat replacement gate.**
- Restatements: redteaming § Panels (top-up); every card's `-r<R>` path rule.
- Purpose: "this is where two agents quietly end up writing the same tree".
- Consumers: RT5, SDD1 BLOCKED lines.
- Why: shared-tree.md § Replacing a seat. N.

### subagent-driven-development

**SDD1 ledger.**
- Restatements: very-small-lane.md (**The lane ledger**); plan-phase.md (Close); flip-paths (supersede: successor ledger); requesting-code-review (wave lines); rationalization row.
- Purpose: "controllers that lost their place have re-dispatched whole completed task sequences, the most expensive failure observed".
- Consumers: SDD26 close readout ("It assembles from…"), CR1 inputs, resume.
- Why: task-loop.md § The spine. N (external: upstream's observed failure, not crucible's).

**SDD2 baseline line.**
- Restatements: using-git-worktrees § Step 3.
- Purpose: "A ledger that already carries that line means both ran: skip them on resume."
- Consumers: resume.
- Why: worktrees.md § Setup and baseline. N.

**SDD3 pre-flight plan-conflict scan.**
- Restatements: very-small-lane.md ("no pre-flight plan-conflict scan"); SDD § Finish close readout ("pre-flight and later plan conflicts").
- Purpose: rule on contradictions "before Task 1".
- Consumers: SDD13 (rulings), SDD26.
- Why: adjudication.md § Upstream's rule and the first port. N (external).

**SDD4 task review.**
- Restatements: task-reviewer-prompt.md; card; inline mode ("Review applies unchanged"); code-reviewer § Tasks With No Task Review (same four judgments).
- Purpose: "attempt to reject this task".
- Consumers: SDD6, SDD9, SDD13.
- Why: task-loop.md § Task review. N for keeping it (preference: "this shouldn't be here" mistakes with Sonnet-era implementers, no count); M for the role change (differential probe).

**SDD5 cannot-verify items.**
- Restatements: task-reviewer Verdict 1 and report.
- Purpose: "requirements living outside the diff".
- Consumers: SDD9 trigger.
- Why: `UNVERIFIED`: no Basis tag names it specifically. Part of the task-loop.md Decision.

**SDD6 loop wiring.**
- Restatements: task-reviewer § Finding Hygiene and Severity; code-reviewer § Tasks With No Task Review; requesting-code-review loop ¶ (branch-only tasks and confirmed leads count as BLOCKER/MAJOR).
- Purpose: "a failed one is a gap whatever label the reviewer staked".
- Consumers: SDD9.
- Why: task-loop.md § Loop wiring. N.

**SDD7 verification gates.**
- Restatements: writing-plans § Acceptance maps to checks; implementer § Tests.
- Purpose: "confirm the report shows each".
- Consumers: SDD22 (widened for marked tasks).
- Why: test-rules.md § Two kinds of check, and removals. M.

**SDD8 snapshot blessing.**
- Restatements: none (Grep "snapshot": SDD only).
- Purpose: "never autonomous".
- Consumers: operator ask.
- Why: task-loop.md § Snapshot blessing. N ("The mutation half went on 2026-10-12; this half stands").

**SDD9 fix ladder and 5-wave cap.**
- Restatements: implementer card (fix-only rules); dispatch adapters (resume operation).
- Purpose: "the cap, with the breaker, is the loop's termination guarantee"; "A loop that survives three resumes usually means the implementer cannot see its own problem."
- Consumers: SDD12.
- Why: task-loop.md § Fix waves and escalation. N (external). The maintainer questions the fresh-eyes reason (backlog/escalation-and-effort.md).

**SDD10 fix-report contract.**
- Restatements: implementer § After Review Findings; re-review § Tests; very-small-lane.md (inline fix reports); requesting-code-review fix dispatch.
- Purpose: confirm each defect "and names its cause before editing", and "checks the task's diff for sibling instances".
- Consumers: SDD11, SDD13.
- Why: task-loop.md and adjudication.md. N.

**SDD11 scoped re-review.**
- Restatements: re-review-prompt.md; card; requesting-code-review (fixed findings bullet); rationalization row.
- Purpose: "Unreviewed fixes are how regressions land."
- Consumers: SDD9 wave line; CR2 (scoped re-reviews verify waves, only a full-scope read clears the branch).
- Why: task-loop.md § The spine. N (external).

**SDD12 breaker.**
- Restatements: SDD § Finish (parked lines in the close readout); rationalization row.
- Purpose: "Parking a structural failure lets every dependent task build on it."
- Consumers: SDD26.
- Why: task-loop.md § Fix waves and escalation. N.

**SDD13 adjudication.**
- Restatements (Grep "adjudicat": SDD 22, requesting-code-review 6, very-small-lane 4, flip-paths 2, plus templates and cards).
- Purpose: "A finding is fixed or disputed, never dropped"; "on its own diff it would be grading itself".
- Consumers: SDD26 (every dismissed BLOCKER/MAJOR reaches the operator), CR3 (rulings checked against the code).
- Why: adjudication.md. N.

**SDD14 no controller fixes.**
- Restatements: requesting-code-review (**Fixes are never yours**; Red Flags); very-small-lane (the supersession); rationalization row.
- Purpose: "your context stays clean for coordination, and controller fixes skip review".
- Consumers: SDD24 conversion rule.
- Why: task-loop.md § Inline mode. N.

**SDD15 what a report voices.**
- Restatements: implementer § Report Format and § Code Organization; task-reviewer § The Implementer's Report; re-review § The Fix Report's Concerns; very-small-lane.md.
- Purpose: an implementer "that sees a fix elsewhere says so instead of making it".
- Consumers: SDD16, SDD4 rulings.
- Why: task-loop.md § The implementer contract. S (umbrella-specs feature) plus preference.

**SDD16 leads.**
- Restatements (Grep "lead \(|leads": 25 lines over 9 files).
- Purpose: carry what task reviewers and implementers voice "to the one seat that sees every task".
- Consumers: CR1 / CR3 rulings, CR4 cleanup wave.
- Why: branch-review.md § The last line of defence (S, for the forms) and § Leads keep the task review's guards (M, audit).

**SDD17 implementer status and stop-and-ask.**
- Restatements: implementer § Stop-and-Ask Triggers and § Report Format; SDD **Deviations.** (stop-and-ask list).
- Purpose: "Bad work is worse than no work."
- Consumers: SDD controller handling.
- Why: task-loop.md § The implementer contract. N (external; upstream's assurance restored).

**SDD18 Decision Log and deviation audit.**
- Restatements (Grep "Decision Log": 36 lines over 9 files).
- Purpose: "An unlogged deviation is indistinguishable from drift."
- Consumers: SDD4 deviation audit, SDD23 materiality bound, BS12 closure.
- Why: task-loop.md § The implementer contract. N.

**SDD19 test-first with RED evidence.**
- Restatements: task-reviewer Verdict 3; code-reviewer § Tasks With No Task Review; SDD steps 3 and 4.
- Purpose: "a failure from a typo or an import error proves nothing".
- Consumers: SDD4.
- Why: test-rules.md § Test-first. N (external).

**SDD20 weakened or deleted test rule.**
- Restatements: implementer, task-reviewer (4), re-review (1), code-reviewer (3).
- Purpose: "Weakening a test … is a scope finding whatever you log."
- Consumers: SDD4 scope verdict.
- Why: test-rules.md § Weakened and deleted tests. M (census).

**SDD21 build-history ban.**
- Restatements: 4 templates (Grep "build history" 1 line each).
- Purpose: build history "belongs in commit messages, the feature folder, and the project's decision records or changelog".
- Consumers: reviewer findings.
- Why: authoring-crucible.md § Build history and branch-review.md § The feature folder's files are not shipped history. N (preference; exemptions an agent's unruled call).

**SDD22 `Review: branch only` mark.**
- Restatements (Grep "Review: branch only|branch review only": 27 lines over 12 files): SDD 7, requesting-code-review 5, writing-plans 3, brainstorming 2, redteaming 2, flip-paths 2, folded-lane, plan-phase, formats, both cards, implementer.
- Purpose: "The branch review runs only after every later task, too late for a detail something else builds on."
- Consumers: CR1 Task Lines, SDD25, RT40 exclusion.
- Why: task-loop.md § Branch review only (preference; S umbrella-specs; M escape analysis) and plans.md § The review mark (M, audit). The branch-review-only path was "not yet exercised" per the project memory; that is `UNVERIFIED` from the tree.

**SDD23 revert-and-replan with DRIFT.**
- Restatements (Grep "DRIFT|Revert-and-replan": 15 lines over 7 files).
- Purpose: drift "is never patched forward".
- Consumers: CR2 (a DRIFT pass consumes a wave).
- Why: task-loop.md § Revert-and-replan. N.

**SDD24 inline mode.**
- Restatements: very-small-lane.md (implementation step); brainstorming § Proposing the arrangement; premise-and-questions (overdetermined).
- Purpose: inline only where "overdetermined … and fits your remaining context".
- Consumers: SDD29.
- Why: task-loop.md § Inline mode. N (external, preference) plus M (audit finding for the lane test).

**SDD25 Finish record checks.**
- Restatements: requesting-code-review § Tasks completed branch review only (record check reads the task line); umbrellas #### Landing step 1.
- Purpose: "List every gap explicitly; never paper over one."
- Consumers: SDD26.
- Why: records-and-workspace.md § Finish. N. The predecessor scripted record checks "never fired in the 125 runs after" (M, about the script).

**SDD26 close readout and answer.**
- Restatements: finishing § Overview; adjudication (rulings list); requesting-code-review (minors listed, declined changes).
- Purpose: "the decision point"; "integration stays the operator's decision".
- Consumers: FIN4 (skipped after an answer), SDD27, CR6.
- Why: records-and-workspace.md § Finish. N (preference: the flow "railroads towards the merge very hard").

**SDD27 open-items routing.**
- Restatements (Grep "open items|work left open": 16 lines; formats 7).
- Purpose: "No item left open stays only in the workspace."
- Consumers: BS16 deletion waits.
- Why: records-and-workspace.md § Work left open. M (audit 4/10) plus preference for the final form.

**SDD28 Finish suite run.**
- Restatements: finishing § Step 1 (exception); requesting-code-review (**Finish's red suite.**).
- Purpose: "a failure found afterwards has no ledger to land in".
- Consumers: CR2.
- Why: records-and-workspace.md § Finish. N (external, judgment; run times measured by the maintainer's report).

**SDD29 very-small lane execution.**
- Restatements: SDD § The very-small lane; requesting-code-review (lane differences); brainstorming § Handoff.
- Purpose: "for a change with nothing left to decide before code, the diff is the review object".
- Consumers: CR2 runs on it.
- Why: routes.md § The very-small lane. M (one cost comparison: ~36M against ~10.6M input-equivalent tokens; "no counterfactual").

**SDD30 Lane Fit verdicts.**
- Restatements: very-small-lane.md (3) and its hatch ¶; code-reviewer card selector.
- Purpose: checks the overturn question "now that it is coded", and whether the note's Intent matches the request.
- Consumers: SDD31.
- Why: routes.md § The very-small lane. N (preference for the goal half: "especially concerning for the very-small").

**SDD31 upgrade hatch.**
- Restatements: formats § Feature folder; umbrellas #### Children; flip-paths § Under an umbrella….
- Purpose: an exit from the lane when EXCEEDS SHAPE.
- Consumers: SDD1 predecessor link.
- Why: routes.md § The very-small lane. N.

**SDD32 goal check.**
- Restatements (Grep: 17 lines over 8 files): code-reviewer 8, seat-prompt 3, cards, formats, brainstorming.
- Purpose: "A mismatch you can stand behind is a premise finding; a vaguer one is a question."
- Consumers: RT41, SDD30.
- Why: evidence-and-findings.md § Premise findings, the goal check and questions. N (an agent's proposal accepted). The underlying escape analysis is M.

**SDD33 seat Questions section.**
- Restatements: seat-prompt, task-reviewer, code-reviewer, implementer report formats.
- Purpose: holds "anything material you could not stake as a finding"; "for doubts and misgivings, none is the normal case".
- Consumers: RT11, SDD16.
- Why: evidence-and-findings.md § Review that holds without a human reader. N (preference to reopen improvements).

**SDD34 binding-item and unrecorded-choice findings.**
- Restatements: seat-prompt, terminal-pass, code-reviewer (each points at the section).
- Purpose: a consequential choice "with no decision recording it … is a finding".
- Consumers: none specific.
- Why: evidence-and-findings.md § What the requirements leave unsaid. M (gap) plus external.

**SDD35 seat git conduct.**
- Restatements: reviewers' Where You Work (read-only on the checkout).
- Purpose: "the index is shared".
- Consumers: ST1.
- Why: git-steps.md § Seats' git conduct. M (three incidents) plus S (identity, 2026-08-23).

**SDD36 diff-as-files.**
- Restatements (Grep "--output|HEAD~1": 12 lines over 7 files).
- Purpose: "hosts cap inline tool output below a branch diff's size"; "never review an empty diff".
- Consumers: SDD4, SDD11, CR1, SDD13.
- Why: branch-review.md § Review seats build their own diff. M (script history) plus external (host cap).

### requesting-code-review

**CR1 branch reviewer seat.**
- Restatements: code-reviewer.md; card; SDD § Whole-Branch Review; rationalization rows.
- Purpose: "for what task-scoped gates cannot see — cross-task integration, drift accumulated across the branch".
- Consumers: CR2.
- Why: branch-review.md § The last line of defence. M (escape analysis: 6 of 11 branch-review BLOCKER/MAJORs premise-level or plan coverage) plus preference.

**CR2 branch-review loop and 3-wave cap.**
- Restatements: SDD § Whole-Branch Review, § Finish step 3; very-small-lane.md; implementer and re-review cards.
- Purpose: "scoped re-reviews verify waves, only a full-scope read clears the branch"; "Cap: 3 waves — the loop's termination guarantee".
- Consumers: SDD26.
- Why: branch-review.md § An iterative loop with a floor and a cap. N (external; intuition quoted).

**CR3 ledger triage and ruling consistency.**
- Restatements: code-reviewer § Execution Trail and § Ledger Triage; card `[LEDGER_MINORS]`, `[RULINGS]`; SDD § Whole-Branch Review; rationalization row.
- Purpose: "a roll-up nobody reads is a silent discard".
- Consumers: CR2 (PROMOTE, FIX-IN-WAVE).
- Why: branch-review.md § An iterative loop… (S: line-wrap waves, for minors not opening waves). Otherwise N.

**CR4 cleanup wave.**
- Restatements: very-small-lane.md (2); SDD § Finish (why a cleanup wave left items).
- Purpose: fix minors and leads "that you judge worth fixing" once.
- Consumers: CR2 cap.
- Why: branch-review.md § An iterative loop…. N (preference: "in practice, I approve them anyway").

**CR5 labelled changes.**
- Restatements: implementer and re-review cards; very-small-lane.md.
- Purpose: "With no defect to confirm, none is answered NOT CONFIRMED."
- Consumers: SDD11, SDD26 (declined items).
- Why: branch-review.md § Changes that ride a wave. M (audit finding, MINOR).

**CR6 rulings and requested work open waves.**
- Restatements: flip-paths § Premise findings (**The ruling.**); SDD § Finish step 3.
- Purpose: a premise ruling at the close readout "had no wave to land in".
- Consumers: CR2.
- Why: branch-review.md § Rulings in execution. M (audit).

**CR7 standalone mode.**
- Restatements: code-reviewer § Standalone Mode; card ("none"); receiving-review § Scope; finishing Option 2.
- Purpose: review "outside SDD", with "no wave loop and no cap".
- Consumers: RR1.
- Why: branch-review.md § One owner, and a standalone use. N.

### writing-plans

**WP1 plan format.**
- Restatements: folded-lane-document.md; plan-phase seats grade it; seat-prompt § Finding scope ("a plan task's required fields").
- Purpose: "the plan carries only what the spec does not: ownership, dependency order, seams".
- Consumers: SDD, RT34, RT35.
- Why: plans.md § A lean contract. N (external; judgment).

**WP2 spec pointer pin.**
- Restatements: dispatch-composition item 4; SDD § Setup (Read the plan once) and § Runtime identity; flip-paths step 2 (re-stamp); every template's Requirements.
- Purpose: "Point, never copy: … the copy and the spec drift and no reader knows which binds."
- Consumers: all EX and BR seats.
- Why: the-spec.md § Pointers, not copies. M (plan campaign findings caused by its own edits: 17→87%; 35 tests existed only to check copying).

**WP3 plan self-review.**
- Restatements: writing-plans notes "The plan phase's mechanical pre-pass stays the independent check".
- Purpose: "fix what turns up".
- Consumers: none.
- Why: plans.md § Self-review. N (external).

**WP4 decision-record attribution.**
- Restatements: implementer § Requirements; task-reviewer § What Was Requested; code-reviewer § Tasks With No Task Review and Task Lines (`bases`); requesting-code-review § Tasks completed branch review only; card.
- Purpose: the implementer "attributes, and its task reviewer … checks, each position's basis from its entry's proposer and status".
- Consumers: SDD4, CR1.
- Why: decision-records.md § Origin and strength. S (umbrella-specs: every position tagged "judgment, accepted by the maintainer").

**WP5 acceptance-to-check mapping.**
- Restatements (Grep "standing test|one-time check": 4 files): brainstorming § Spec contract (Acceptance); SDD § The Task Loop, 4. Verification gates; implementer § Tests; lane-note.md.
- Purpose: "An absence or removal criterion ("X is gone") is a one-time check unless…"
- Consumers: SDD7, RT35 (acceptance mapping), SDD4.
- Why: test-rules.md § Two kinds of check, and removals. M.

### finishing-a-development-branch

**FIN1 finishing guards.**
- Restatements: using-git-worktrees (single-invocation rule, branch safety).
- Purpose: "merging into the wrong base is expensive to undo"; "Only the typed word `discard` authorizes deletion."
- Consumers: SDD § Finish step 3 (discard confirmation before deletion).
- Why: git-steps.md § Finishing's guards. M (git's behaviour) plus judgment.

**FIN2 integration test verification.**
- Restatements: SDD § Finish step 5; UC3.
- Purpose: "A green run only proves the tree it ran on."
- Consumers: FIN4.
- Why: records-and-workspace.md § Finish. N.

**FIN3 records-in-PR question.**
- Restatements: SDD § Finish step 2 ("also ask that skill's question whether the feature folder's files go into it").
- Purpose: the PR "shows them under any merge strategy".
- Consumers: none.
- Why: records-and-workspace.md § What is committed / § The feature folder. N.

**FIN4 integration options menu.**
- Restatements: SDD § Finish (recommendation names one of its options).
- Purpose: "the integration decision is theirs".
- Consumers: none.
- Why: records-and-workspace.md § Finish. N (external).

### using-git-worktrees

**WT1 worktree isolation.**
- Restatements: brainstorming § Spec contract; SDD § Setup ("implementation on a main/master checkout needs the operator's explicit consent").
- Purpose: "Never fight the harness"; a native tool avoids "phantom state your harness can't see or manage".
- Consumers: BS16 (workspace per checkout).
- Why: worktrees.md. N (external, judgment).

**WT2 worktree-dir ignore check.**
- Restatements: none in skills.
- Purpose: "Prevents accidentally committing worktree contents to repository."
- Consumers: none.
- Why: worktrees.md § The fallback's checks. M.

**WT3 clean baseline.**
- Restatements: SDD2.
- Purpose: "A dirty baseline makes every later failure ambiguous."
- Consumers: SDD2.
- Why: worktrees.md § Setup and baseline. N.

### receiving-review

**RR1 receiving-review discipline.**
- Restatements: requesting-code-review § Standalone mode; finishing Option 2.
- Purpose: "Review feedback is a claim about the code. Check it before you act on it, whoever sent it."
- Consumers: none.
- Why: upstream-skills-kept-close.md § Receiving review, § The restate step. N.

### systematic-debugging

**SD1 root-cause-first discipline.**
- Restatements: implementer § Tests (follow it on unexpected failures); SDD10 ("confirms each defect and names its cause").
- Purpose: "NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST".
- Consumers: SDD10.
- Why: upstream-skills-kept-close.md § Generic craft stays upstream's. N (external).

**SD2 3-fix architecture breaker.**
- Restatements: Red Flags and rationalization rows in the same skill.
- Purpose: "3+ failures = architectural problem."
- Consumers: an operator discussion.
- Why: same record. N (external).

### writing-skills

**WS1 skill evaluation protocol.**
- Restatements: implementer § Tests (evaluations "are not yours … leave any evaluation the plan calls for to your controller").
- Purpose: "If the control doesn't show the failure, there is nothing to fix."
- Consumers: none.
- Why: authoring-crucible.md § writing-skills. M (upstream wording tests) plus external.

---

## Vocabulary

| Term | Kind | Owner text |
|---|---|---|
| `standard`, `folded`, `very-small` | preset (route) names | brainstorming § Proposing the arrangement (step 4) |
| route entry | decision-record entry | brainstorming § Proposing the arrangement (step 4) |
| `open`, `accepted`, `firm` | decision statuses | brainstorming § Workspace provisioning (brainstorm exit) |
| `accepted — proposed by the controller`, `accepted — delegated to the controller` | status forms with proposer | same |
| gate entry | decision-record entry (approved campaign shape) | brainstorming § Digest gate |
| `[LOAD-BEARING: <what builds on it>]` | mark | brainstorming § Spec contract |
| Constraints & invariants, Intent, Decisions, Interfaces & boundaries, Acceptance, Mechanism sketches | spec sections | brainstorming § Spec contract |
| binding / advisory / lightly held | content weights | brainstorming § Spec contract; writing-plans § Binding vs advisory |
| `Deferred to implementation: <what>` | marker | brainstorming § Spec contract (**Deferral device.**) |
| owner-pending | deferral state | same |
| `## Deferred-items routing table`, `T<N>` | plan section and owner form | writing-plans § Plan header |
| `UNVERIFIED` | claim tag | brainstorming § Spec contract; redteaming § Merge and finding hygiene |
| standing test / one-time check | acceptance check kinds | writing-plans § Acceptance maps to checks |
| `Spec: \`<path>\` @ \`<rev>\``, `Spec: this document` | pin forms | writing-plans § Plan header |
| `Review: branch only — <reason>` | task mark | writing-plans § Per-task structure — four fields, all required |
| task completed branch review only | task state | requesting-code-review § Tasks completed branch review only |
| `Umbrella: \`…/umbrella.md\`` | preamble line | umbrellas.md #### Children |
| `landed`, `umbrella`, `dropped` | umbrella entry marks | umbrellas.md #### Marks |
| `open premise ask: <the ask>` | umbrella entry note | umbrellas.md #### Landing |
| `Lane: very-small (operator-confirmed <date>)` | note and ledger line | lane-note.md; very-small-lane.md |
| `Gates:`, `Implementation complete:`, `Departure:`, `Wave <n>:`, `Wave <n> (cleanup):`, `Note re-pinned:`, `Hatch:` | lane ledger lines | very-small-lane.md (**The lane ledger**) |
| `EXCEEDS SHAPE` / `WITHIN SHAPE`; `GOAL MATCHES` / `GOAL DIFFERS` | Lane Fit verdicts | code-reviewer.md § Binding Content (lane passage) |
| design.md, folded.md, note.md, umbrella.md, plan.md, design-2.md, plan-2.md | role-named files | formats.md § Feature folder |
| birth step / resolve step | folder steps | formats.md § Feature folder |
| `.crucible/<slug>/`, `brainstorm-decisions.md`, `request.md`, `digest.md`, `campaigns/spec/`, `campaigns/plan/`, `sdd/`, `scratch/` | workspace layout | formats.md § Feature workspace root and layout |
| controller-saved mark | report first line | formats.md (**A report the controller saved carries a mark**) |
| `state:` `dispatched → returned → merged → fix-applied → verified → readout` (`→ confirmed`) | state vocabulary | formats.md § Round record format, field 2 |
| `degraded: yes \| no`, `topped-up` | quorum values | formats.md field 3 |
| `conservation: … clean` / `unaccounted:` | conservation line | formats.md field 3 |
| `origins: <seat-id>-<n>` | merged-entry element | formats.md field 5 |
| `applied`, `partly-applied`, `parked`, `rejected`, `deferred-to-implementation` | dispositions | formats.md field 5; redteaming § Merge and finding hygiene |
| `premise` (label) | finding label | premise-and-questions.md § Premise findings |
| `literal-reading` | finding label | task-reviewer / code-reviewer / re-review templates |
| `plan-mandated` | finding label | task-reviewer-prompt.md § Finding Hygiene and Severity |
| answered / carried to readout / rejected / adopted | question dispositions | formats.md field 5; redteaming § Merge and finding hygiene |
| `FINDING <seat-id>-<n> [SEV]`, `QUESTION <seat-id>-q<n>`, `## Index`, `## Worksheet`, `## Right-sized — do not cut`, `## Goal check`, `## Verdict` | seat report shape | seat-prompt.md (Report) |
| `Overturn after code: reasonably expected — …` / `… not reasonably expected` | forecast line | seat-prompt.md (Report item 1) |
| overturn question; major mechanism; overdetermined | defined tests | premise-and-questions.md § The arrangement questions |
| `BLOCKER` / `MAJOR` / `MINOR` | severity | redteaming § Merge and finding hygiene; all templates |
| `Trace:` | record-only readout part | formats.md field 8 |
| `## Rulings and corrections` | post-close record section | formats.md § Round record format |
| `Record corrections: <N>`, `CONCLUSION-CHANGING`, directional-bias line | terminal-pass outputs | terminal-pass-prompt.md |
| `Contained amendment:` | fix-list item opener | plan-phase.md |
| scoped amendment / supersede / amendment marker / contained | flip vocabulary | flip-paths.md |
| landed / not-landed / partial; TRUE / FALSE / not checked | verifier verdicts | verifier-prompt.md |
| `DONE`, `DONE_WITH_CONCERNS`, `BLOCKED`, `NEEDS_CONTEXT` | implementer status | implementer-prompt.md § Report Format |
| `fixed` / `NOT CONFIRMED` | fix answers | implementer-prompt.md § After Review Findings |
| `ADDRESSED` / `NOT ADDRESSED` | re-review verdicts | re-review-prompt.md § Report |
| `UPHELD` / `DISMISSED`; `pending operator` | adjudication outcomes | SDD § Disputes and adjudication |
| cannot-verify (⚠️) | review item | task-reviewer-prompt.md Verdict 1 |
| `lead (question\|proposal\|concern)` | ledger line | SDD § Setup |
| `CONFIRMED` / `RECOMMENDED` / `LEFT`; `PROMOTE` / `FIX-IN-WAVE` / `LEAVE-PARKED`; `CONSISTENT` / `CONTRADICTED`; `OPEN` | branch-review triage verdicts | code-reviewer.md § Execution Trail, § Ledger Triage |
| `DRIFT` | branch-review flag | code-reviewer.md § What to Check |
| `Change (improvement\|ruling\|requested): …` | labelled change | requesting-code-review § The branch-review loop |
| `# SDD ledger — plan: …`; `## Progress`, `## Adjudication rulings`, `## Deferred minors`, `## Questions`; `Baseline:`; `Task <N>: implementer …`, `… fix wave <W>/5 …`, `… complete (…)`, `… parked — …`, `… BLOCKED — …`, `… reverted — …`; `Branch wave <n>/3 (…)`; `Branch review pass <k>: …`; `<phase>: <item> — carried` | ledger forms | SDD § Setup, § The Task Loop; requesting-code-review; plan-phase.md |
| `Task <N>: intent PASS\|FAIL, scope …, deviation audit …, quality …, bases PASS\|FAIL\|n/a` | task line | code-reviewer.md § Output Format (Task Lines) |
| `-x<X>`, `-r<R>`, `-w<W>` | report-name suffixes | SDD § Revert-and-replan, § Disputes and adjudication; cards |
| `preserved` / `intent-visible` | snapshot verdicts | SDD § The Task Loop, 4. Verification gates |
| default / bounded / alternate role | model roles | dispatch-composition.md § Models and effort |
| instrument; slot card; selector; `[[when <selector> = <value>]]` | dispatch vocabulary | redteaming § Dispatch composition; templates |
| digest gate; decision ask; technical call; readout; close readout | operator interface | brainstorming § Digest gate; redteaming § Round readout; SDD § Finish |
| `discard` (typed) | confirmation word | finishing § If your human partner asks to discard the work |

## Totals per skill

Directory totals are from `tests/prose-budget.txt` (counted). Splits are estimates from the attributions above. "Unattributed" means core work, technique, wording, handoffs, frontmatter and host mechanics.

| Skill | Total | By mechanism (est.) | Unattributed (est.) | Notes |
|---|---|---|---|---|
| brainstorming | 6,651 | ~5,800 | ~850 (13%) | Unattributed: intro, context gathering, dialogue, handoff routing. All three references are mechanism text. |
| redteaming | 19,465 | ~18,800 | ~690 (3.5%) | Plus `conserve.py` (1,308 words of code, outside the budget). |
| subagent-driven-development | 19,548 | ~17,000 | ~2,500 (13%) | `writing-good-tests.md` (1,312) counted as core test craft; the rest is template core-work instructions and handoffs. |
| requesting-code-review | 6,193 | ~5,600 | ~570 (9%) | Generic What to Check lists, Critical Rules. |
| writing-plans | 2,056 | ~1,940 | ~120 (6%) | |
| finishing-a-development-branch | 1,917 | ~1,590 | ~330 (17%) | PR push and conventions, Option 3. |
| using-git-worktrees | 1,713 | ~1,490 | ~220 (13%) | |
| using-crucible | 2,032 | ~630 | ~1,400 (69%) | 1,235 of the unattributed words are the host adapters (host mechanics, outside the frame). |
| receiving-review | 515 | ~480 | ~35 | |
| systematic-debugging | 3,422 | ~1,280 | ~2,140 (63%) | Technique files unattributed; SD1 is borderline core work. |
| dispatching-parallel-agents | 920 | 0 | 920 | Technique; its "start all before waiting" is restated in RT1. |
| writing-skills | 1,546 | ~470 | ~1,080 (70%) | |
| **All** | **65,978** | **~55,100 (~84%)** | **~10,900 (~16%)** | |

Resident (`SKILL.md`) words, all skills: 31,136 (counted, frontmatter included: 3,764 + 920 + 1,917 + 515 + 6,374 + 2,755 + 7,288 + 1,491 + 797 + 1,713 + 2,056 + 1,546). Of these, ~25,000 are attributable to mechanisms (est.).

## Chains (mechanisms that exist mainly to check another mechanism)

1. **Fix-wave chain.** RT16 fix list → RT20 blind verifier → RT20b delta claims (controller re-checks the verifier's unchecked claims) → RT27 terminal pass re-read (backstops the last wave) → RT32 second read (checks the terminal pass's own follow-up wave). Side branches: RT9 sub-point check (fix narrower than its finding, which the verifier cannot see), RT17/RT18 (sites the verifier then checks), RT19 (checks that a check can fail).
2. **Readout-fidelity chain.** RT21 readout and RT22 asks → RT21 coverage self-check → RT28 fidelity check (with the RT11 carried-question quote check and the BS10 delegated-status check) → RT31 directional-bias statement (a check over the set of corrections) → escalation threshold. RT15 operating stance exists to keep the disclosure that RT31 audits cheap.
3. **Stop chain.** RT23 stop (controller judgment) → RT24 seat forecast lines (a record the controller did not write) → RT21 readout must answer each forecast → RT29 stop check. RT25 premise hold also feeds RT29.
4. **Approval chain.** BS17 decision record and BS10 statuses → RT30 decision-record check → `CONCLUSION-CHANGING` ask.
5. **Merge chain.** RT7 merge → RT10 conservation script (nothing re-runs it) → RT6 conservation line.
6. **Execution review chain.** SDD4 task review → SDD11 scoped re-review (checks a fix) → SDD13 adjudicator (checks disputes; controller rulings pass RT40) → CR1 branch review: SDD16 leads, CR3 triage with ruling-consistency check (checks rulings against code), Task Lines for SDD22 → CR2 full-scope pass after every wave → branch review's terminal full-scope pass.
7. **Concern-ruling chain.** SDD15 concerns → the review must rule on each ("missing verdict") → the controller refuses a review missing a verdict (SDD § The Task Loop, 3; requesting-code-review step 1). The same pattern holds for leads at CR1.
8. **Mark chain.** SDD22 mark → plan-phase and folded seats grade each mark → no-mark-in-last-wave rule (ensures a grading seat read it) → RT40 exclusion (a later mark goes to the operator) → controller gate at SDD step 2 → CR1 Task Lines → SDD25 record check reads the task line.
9. **Deferral chain.** BS12 marker → routing table → ledger seeding (RT34 Close / RT38 close check that "every marker has its rows and no row is owner-pending") → implementer Decision Log entry → SDD4 routed-item check → CR3 sweep.
10. **Arithmetic chain.** WP1 census → RT35 pre-pass arithmetic → RT35 controller post-wave re-run (checks the fix wave's effect on the arithmetic) → RT36 set census (checks the census against the repository).
11. **Author-side sweep chain.** BS14 / BS15 at self-review → RT18 on every fix item → CR1's trace question at branch review.
12. **Record-completeness chain.** RT45 report-file confirm → one resume → controller-saved mark. Separately: SDD25 record checks → gaps named in SDD26.
13. **Lane chain.** BS4 step-4 selector (operator-confirmed preset) → SDD30 Lane Fit (the same question asked of the diff) → SDD31 hatch.
14. **Goal chain.** BS18 request → SDD32 goal check at seats (a check on the brainstorm's Intent) → RT41 premise ask → RT28 fidelity of that ask.
15. **Measurement-validity guards.** ST2 tree check (voids reports from a moved tree) with RT33 freeze, ST1 and RT43 scratch, which exist so ST2's readings mean something.

---

## Did not fit the frame

- **A third cost bucket.** Templates and cards are neither `SKILL.md` nor references. They load into every dispatched seat, so their cost multiplies by the number of dispatches. Seat-side, the largest restated blocks are BS8, the binding-content clause (~900 words across 6 templates), and UM4, the umbrella-line clause (~720). Both repeat near-verbatim, although the clause itself says a copy drifts against the artifact it copies.
- **Always-loaded text.** `using-crucible` is injected at session start, so UC1–UC4 cost more than "resident on invoke" suggests.
- **Unseen costs.** Several decision records concede per-feature work "which word counts do not show": RT18 fix-item trace, RT36 set census, RT30 decision-record check, and the open-items commit in SDD27. Word counts understate them.
- **Scope mismatch.** WP4 decision-record attribution comes from crucible's own `docs/decisions` Basis convention (decision-records.md § Origin and strength). It ships in generic skill text as a rule for any project's "decision record".
- **Host adapters.** They carry mechanism-like steps that the brief classes as host mechanics, so they are excluded: the Claude Code report-name filter workaround (supports RT45), and the Codex rule to read `config.toml` effort before the first dispatch (supports RT48).
- **Repository tests.** `tests/` enforces text rules (prose budget, report filenames, instrument generation, claude-ism scanner). These are authoring mechanisms, not session mechanisms, and are not inventoried.
- **Borderline core work.** `writing-good-tests.md` (gate functions, mutation check) and systematic-debugging (SD1) are test and debug craft. Only SD1 and SD2 are inventoried.
- **"Measured" is broad.** It often means an audit count of findings about a predecessor rule, not a measurement of the current mechanism catching anything. Few records cite a catch rate for the mechanism as it now stands. Exceptions: RT10 (at most 1 real catch in 193 rounds), RT21's scripted predecessor (0 in 125), and RT27 (27 of 74).

Not verified (marked inline): the Why source for RT6 (state line) and SDD5 (cannot-verify); the statement that the branch-review-only path is unexercised (from project memory, not the tree). Every per-mechanism word split inside a paragraph is an estimate, as stated in the method.
