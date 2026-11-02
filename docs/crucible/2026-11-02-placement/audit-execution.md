# Placement audit: execution reader

> Advisory input to `design.md`, read at `8332a00`. Where the spec decides otherwise (its Decisions and its corrections list), the spec governs; the questions below were answered in its brainstorm.

Tree: the repository at HEAD `8332a00`, `git status --short` empty before and after.
All locations are `file:line` as read on that tree. Paths shortened: `SDD` = `skills/subagent-driven-development/SKILL.md`, `VSL` = `skills/subagent-driven-development/references/very-small-lane.md`, `DC` = `skills/subagent-driven-development/references/dispatch-composition.md`, `RCR` = `skills/requesting-code-review/SKILL.md`, `FIN` = `skills/finishing-a-development-branch/SKILL.md`, `RR` = `skills/receiving-review/SKILL.md`, `ROUTER` = `skills/using-crucible/SKILL.md`, `CC` / `CCD` / `CX` / `CXD` = `skills/using-crucible/references/claude-code.md` / `claude-code-dispatch.md` / `codex.md` / `codex-dispatch.md`. Word counts are per line (`wc -w`), or my estimate of the clause where marked "~".

## 1. Restated rules

**R1. Never predict an agent's result (confirmed known item).**
Sites: CC:22-24 (~13 words of the rule), CX:26-28 (~13). No other site in `skills/`.
Owner: this is host-neutral, so it can't stay in the adapters (`docs/decisions/runtime-adapters.md:27-29` already lists it for moving). It belongs in ROUTER, beside "Evidence before claims" (ROUTER:24), because every session that dispatches reads that file. DC is the other candidate, but `crucible:dispatching-parallel-agents` never reads DC (see Q3).
Others: the adapters keep only the mechanic ("returns that agent's final report when it finishes, and you are notified" / "`wait_agent` … returns it").
Saved: ~13 words in the repo. Per session it's net zero, because the host map and ROUTER are in the same envelope.

**R2. Fan-out only for genuinely independent tasks (confirmed known item).**
Sites: CC:25-28 (~40), CX:29-32 (~40), `skills/dispatching-parallel-agents/SKILL.md:77` (~12: "Tasks that are not independent run one at a time, whatever the host permits"), plus its description and :40.
Owner: dispatching-parallel-agents:77, the skill whose reader acts on fan-out. It should take the adapters' fuller definition ("no shared state, no ordering, neither reading the other's output"; see D4).
Others: each adapter keeps one clause, e.g. "this host can run several dispatches concurrently" and "spawn each, then `wait_agent`".
Saved: ~55 words across both adapters, ~25 per session.

**R3. Effort only on the operator's request (confirmed known item).**
Sites:
- DC:81-84 (~45), the owner
- CCD:16-17 (~7: "used only on the operator's request")
- CXD:14-15 (~7)
- redteaming slot cards: `skills/redteaming/seat-prompt.slots.md:34`, `terminal-pass-prompt.slots.md:32`, `verifier-prompt.slots.md:21` ("an effort level only on the operator's request"). These belong to the templates reader.

The adapters keep the parameter name only. CXD keeps its host-specific config read (CXD:17-28).
Saved: ~14 words in the adapters.

**R4. Name the model on every dispatch.**
Sites: DC:64-65 (~12), CC:20-21 (~12), CX:24-25 (~4), CC:29 ("stated on the dispatch itself").
Owner: DC for crucible seats. But ad hoc dispatches through `crucible:dispatching-parallel-agents` (which says nothing about models; Grep `model|role` finds nothing) are covered only by the adapter copy. So the owner is either ROUTER or DC plus a pointer from dispatching-parallel-agents (Q3).
Saved: ~15 words.

**R5. Read the dispatch reference when the skill starts and after compaction.**
Sites: SDD:16 (26), RCR:10-13 (~35), `skills/redteaming/SKILL.md:20` (~35). The three paragraphs are near-identical.
Owner: DC. All three controllers already read DC before their first dispatch (SDD:48, redteaming:36; for RCR see D7). One line in DC would cover it.
Others: nothing.
Saved: ~95 words; DC grows by ~20.

**R6. Read the card, not the template; set every selector; dispatch through the instrument-dispatch operation.**
Sites: SDD:50 (~40 of 105), `skills/redteaming/SKILL.md:42` (~45), RCR:24 (~10), and each slot card's "Operation" line (e.g. `skills/requesting-code-review/code-reviewer.slots.md:28`).
Owner: DC, as a shared controller-side dispatch rule.
Others: SDD and redteaming keep only their list of instruments.
Saved: ~70 words.

**R7. Confirm the report file is on disk, and handle a missing one.**
Sites: DC:42-49 item 5 (owner), SDD:52 (51), `skills/redteaming/SKILL.md:39` (~50), `skills/redteaming/references/formats.md:118-129` (owns the mark for a report the controller saved), RCR:28 (~15; it points to SDD § Runtime identity, which itself points to DC).
Others: SDD:52 keeps the path-uniqueness clause ("at a path no earlier dispatch used") and points to item 5. RCR:28 should point to DC item 5 directly.
Saved: ~35 words.

**R8. What binds, and the umbrella change-is-a-finding clause.**
Sites:
- DC:20-33 item 4 (~150)
- SDD:87 (~110 of 269)
- RCR:26 (~70 of 293)
- VSL:13 (~90 of 227)
- `skills/writing-plans/SKILL.md:20` (plan-defect form)
- templates: `requesting-code-review/code-reviewer.md:78`, `subagent-driven-development/implementer-prompt.md:101`, `re-review-prompt.md:61`, `task-reviewer-prompt.md:64`
- source of the classification: `skills/brainstorming/references/umbrellas.md:59-71`

Owner: DC item 4 for the controller side, and the shared seat reference for the seat side (templates reader).
Others: SDD:87, RCR:26 and VSL:13 become one-line pointers.
Saved: ~250 words across SDD, RCR and VSL. See D1 for drift.

**R9. "The spec is a hypothesis … read for intent … literal reading raised for a ruling."**
Sites:
- `skills/redteaming/references/flip-paths.md:3` (~70), the owner on the controller side
- SDD:87 (~45)
- `skills/brainstorming/SKILL.md:86`, `skills/writing-plans/SKILL.md:52`
- templates: code-reviewer.md:82, task-reviewer-prompt.md:66, re-review-prompt.md:63, implementer-prompt.md:105, `redteaming/terminal-pass-prompt.md:82`, `redteaming/seat-prompt.md:58`

Owner: flip-paths:3, and the shared seat reference for seats.
Others: SDD:87 points to it.
Saved in SDD: ~40.

**R10. A scoped change passes § The containment test (confirm if contained, otherwise a decision ask).**
Sites: SDD:81 (~35), SDD:161 (~45), SDD:195 (~20), DC:39-41 (~15), and flip-paths § The containment test (owner).
Others: SDD:81 and :195 point to it; SDD:161 keeps its record-keeping only.
Saved: ~50.

**R11. Operator rulings enter the brainstorm decision record, and changes to the ask enter `request.md`.**
Owner: `formats.md:88-99`, which already says "(binding)".
Restated at: SDD:161 (~30), RCR:43 (~30), VSL:7 (~25), `redteaming/SKILL.md:134` (~25), flip-paths:3 (~25).
Others: drop them, or a three-word pointer.
Saved: ~110 across the five sites (~80 in my files).

**R12. What a decision ask is: analyst language, no reading of plan, code or diff, may quote lines.**
Sites: SDD:14 (~30), RCR:43 (~20), `redteaming/SKILL.md:126` (~40), flip-paths:3 and :56, RR:30 (~10).
Owner: one definition. SDD:14 is where an execution controller first meets it; redteaming:126 is the fuller copy. ROUTER would cover every skill. This needs a ruling (D2).
Saved: ~50.

**R13. Never `HEAD~1`; the reviewer builds the diff itself, so it never enters your context.**
Sites: SDD:93 (~30), RCR:22 (~25), `code-reviewer.slots.md:17`.
Owner: the slot cards' `[BASE_SHA]` slot (where the controller fills it), plus one "builds its own diff" line in DC.
Saved: ~40.

**R14. The controller never fixes findings: context stays clean, and controller fixes skip review.**
Sites:
- SDD:131 (42)
- SDD:191 ("controller fixes that skip review are the case this rule exists for")
- SDD:222 (rationalization)
- RCR:38 ("never you off the lane")
- RCR:63 (59)
- RCR:88 (red flag)
- VSL:16 (the lane exception)

Owner: SDD § Rules every route shares, since the rule spans both loops; SDD:131 sits inside task-loop step 5 today.
Others: RCR:63 becomes "on the lane you fix inline (VSL)"; RCR:38 is a pointer.
Saved: ~45.

**R15. The re-review: card fill and seat behaviour.**
Sites: SDD:126 (123), RCR:39 (91). Both restate the re-review card (`re-review-prompt.slots.md:8-13`) and the seat's verdicts (`re-review-prompt.md:120-177`).
Owner:
- the card, for what goes in the dispatch
- the template, for what the seat does
- the controller skills keep only what the controller does with the output: new BLOCKER/MAJOR joins the open findings, out-of-scope observations become deferred minors, an unruled concern is a missing verdict.

Saved: ~110. See D5.

**R16. Implementer and task-reviewer card fills restated in the skills.**
Sites: SDD:72 (~25), SDD:93 (~25), RCR:38 (~45), RCR:26 (~120 of input listing, against `code-reviewer.slots.md:8-17`).
Owner: the slot cards, which the controller is told to read instead of the template.
Saved: ~170.

**R17. Task-reviewer mandate and rubric restated in the controller skill.**
Sites: SDD:95 (71), SDD:100 (56), SDD:101 (66), against `task-reviewer-prompt.md:3-8, 160-200`.
Owner: the template. SDD keeps the four verdict names, "all required", the loop wiring (SDD:104) and the dispatch hygiene (SDD:106).
Saved: ~120.

**R18. Building the diff: git validation and writing the range into scratch files.**
Sites: SDD:155 (~85 of 295: `git cat-file -t`, `merge-base --is-ancestor`, `-U10`, `--output`, the scratch path, the error case), `task-reviewer-prompt.md:108-125`, `re-review-prompt.md:101-107`, `code-reviewer.md:197-203`.
Owner: the shared seat reference, as one "Diff under review" section (templates reader). SDD:155's adjudicator dispatch points to it, as do the three templates.
Saved in SDD: ~75.

**R19. Deferred minors and leads go to the branch reviewer, because "a roll-up nobody reads is a silent discard".**
Sites: SDD:199 (~45), RCR:26 (~70), RCR:80 (rationalization), SDD:151.
Owner: RCR:26, where the controller fills the inputs. SDD:199 becomes "run RCR; it owns the loop and its inputs."
Saved: ~70.

**R20. Red suite at Finish = a BLOCKER against the branch; "not the branch's" is a dispute.**
Sites: SDD:213 (140), RCR:61 (66), FIN:37 (28).
Owner: split. SDD:213 owns classification and dispute (where the controller acts). RCR:61 owns the wave mechanics (cap, FIX_BASE). FIN:37 stays as a pointer.
Saved: ~45. See D8.

**R21. Drift found in a completed task: how a repair or revert rides the branch review.**
Sites: SDD:184 (last sentence, ~20), SDD:185 (~50 on branch-review wave timing), RCR:59 (82).
Owner: SDD § Drift for the operator ask, revert and repair; RCR:59 for how a repair rides a wave and the resumed pass.
Saved: ~50.

**R22. Lane: drift from the note is a wave finding.**
Sites: VSL:13 (~15), SDD:187 (~10), RCR:59 (~10).
Owner: VSL.
Saved: ~20. See D3.

**R23. Umbrella receiving step before each pass and wave.**
Sites: RCR:34 (58), the owner on the branch side; SDD:70 (task side, owner there); SDD:195 (~35, restates both checkpoints); VSL:13 (~20).
Saved: ~55.

**R24. Lane fix waves inline: the controller writes `wave-<n>-fix.md`.**
Sites: VSL:16 (158), the owner, and RCR:63 (~35).
Also: VSL:16 restates the fix-report contract (fixed / NOT CONFIRMED, applied / declined), which is stated at SDD:124 and RCR:49 and in the implementer template. It could point there.
Saved: ~70.

**R25. Lane entry only by operator confirmation at brainstorming.**
Sites: VSL:5 (59), the owner, and SDD:203 (~20).
Saved: ~20.

**R26. Lost workspace: restart from the committed spec or plan; transcripts hold the lost records.**
Sites: SDD:42 (~30), `formats.md:144-146` (owner, near-verbatim).
Saved: ~25.

**R27. Ledger `## Questions` line forms.**
Sites: SDD:36 (~40), SDD:169, RCR:49, RCR:55 (owner: where the controller writes them).
Saved: ~30.

**R28. Disputes in the branch review: never park on your own ruling, never drop; dismissed ones go to the close readout.**
Sites: RCR:57 (~30), SDD:151 and SDD:161 (owner).
Saved: ~25.

**R29. Premise finding is a decision ask, not an open BLOCKER/MAJOR.**
Sites: SDD:143, RCR:36, RCR:87, flip-paths § Premise findings (owner).
Saved: ~25.

**R30. The replacement line.**
Sites: SDD:178 (owner), `redteaming/SKILL.md:75` (~25: "follows the replacement line execution uses", then restates it).
Saved: ~20, outside my files.

**R31. Record each agent's identity before relying on continuation (host-neutral, sits in an adapter).**
Sites: CXD:12-13 (~10), SDD:74 (owner for implementers), `redteaming/SKILL.md:75`.
Saved: ~10.

**R32. Resume fallback content: what a fresh fix dispatch carries.**
Sites: CCD:13-15 (~25: "dispatch fresh with the requirements, the report-file path and the open findings"), SDD:122 (the fresh-dispatch path), `implementer-prompt.slots.md:8` (the fix-only rules).
Owner: SDD:122 and the card.
Saved: ~20.

**R33. "Read X in full, re-read after compaction; it binds as if written here."**
Repeated as a formula at SDD:48, :195, :203 and in redteaming and brainstorming (~8 sites).
Owner: one ROUTER convention line, with each site saying "binding reference: X".
Saved: ~60 across `skills/`, ~25 in my files. This is a convention change, so low priority.

## 2. Drifted copies

**D1. The umbrella finding rule, narrower than its source (needs a ruling).**
Source: `umbrellas.md:69` defines a binding change as one "to the umbrella's Constraints & invariants or firm decisions, to what its Intent asks for, or any other change to a started child's entry".
Every restated copy says only "a change to those Constraints or firm decisions is a finding, and so is a change to the entry other than the feature's own mark or a clarification…". These are DC:29-33, SDD:87, RCR:26, VSL:13 and the four review/implementer templates. The copies miss two cases:
- a change to what the umbrella's Intent asks for;
- a change to another started child's entry.

So no seat flags either within a reviewed range. I can't tell whether reviewers are meant to see the narrower set, or whether these two cases were simply lost.

**D2. Decision-ask definition (needs a ruling).**
SDD:14 and RCR:43 have "analyst-language with a recommendation: never requires reading plan, code or a diff, and may quote the few lines it turns on". `redteaming/SKILL.md:126` adds "Each ask lists every option the findings behind it propose, and states what its change withdraws from an earlier operator approval."
Unclear whether the two extra obligations hold for execution-time asks. If they do, SDD and RCR are missing them.

**D3. Lane drift scope.**
VSL:13 says "Drift from the note's **binding parts** is a wave finding". SDD:187 and RCR:59 say "drift from the note". VSL:7 makes change-list departures ledger lines, not findings, so VSL's narrower version is the intended one.

**D4. Fan-out independence definition.**
CC:25-26 and CX:29-30 say "no shared state, no ordering, neither reading the other's output". dispatching-parallel-agents (description :3, :40, :77) says "without shared state or sequential dependencies" / "No shared state". It does not cover one agent reading another's output. The adapters' fuller version should move to the owner.

**D5. Controller copies of card fills miss the amendment commits.**
The cards require "each commit in BASE..HEAD [FIX_BASE..HEAD] that landed a scoped amendment or a plan-patching ruling, by hash, or 'no amendment commits'" (`task-reviewer-prompt.slots.md:8`, `re-review-prompt.slots.md:8`).
SDD:93 lists the task reviewer's inputs as "the plan pointer, the implementer's report, the range BASE..HEAD". SDD:126 says "the plan pointer". Both omit those commits; the cards are the intended version. A controller following the skill text instead of the card under-fills the slot. Deleting the restatement (R15/R16) fixes it.

**D6. Who owes a report-file check.**
SDD:52 says "Every review seat and the adjudicator writes its own report file … Confirm the file is on disk". DC item 5 (DC:43-49) covers any "seat that owes a report file", implementers included (`formats.md:118-121`: "the reports SDD's seats write under `sdd/`"). SDD's copy reads narrower; DC's is the intended version.

**D7. RCR never tells its controller to read DC.**
SDD:48 and `redteaming/SKILL.md:36` say to read DC before the first dispatch and again after compaction. RCR:24 says only that every seat "carries the seven items" of DC. In standalone mode, with no SDD run before it, nothing sends the reader to DC. The intended version is presumably SDD's. R5's consolidation should cover RCR as well.

**D8. Red-suite ruling persistence.**
SDD:213: "A failure ruled not the branch's, whoever ruled, is recorded with its ruling and not raised again while it fails the same way". RCR:61 restates the rest of the rule but not this. SDD is intended; the copy is incomplete rather than contradictory.

## 3. Wrong-level text

**W1. Host-neutral rules in the adapters (confirmed known items).** R1, R2 and R3 as above, plus:
- R4: the "an omitted model silently inherits" clause, CC:20-21
- R31: CXD:12-13
- R32: CCD:13-15

Destination: the owners named above. Saved: ~170 words in the adapters, ~90 per session envelope; ROUTER grows by ~15 if it takes R1.

**W2. Incident in SDD:32 (~20 words): "controllers that lost their place have re-dispatched whole completed task sequences, the most expensive failure observed."**
Already held at `docs/decisions/task-loop.md:169-170`. Delete it and keep the action ("track progress in the ledger"). Saved: ~20.

**W3. Explanatory evidence in CCD:18-24 (~30 of ~60 words).**
This is the quoted host message and "The host also advises subagents in prose … so an instrument can hand back its report without having written it." The action (handle a missing report) is DC item 5. The quote is already held in `docs/decisions/instruments.md` (Grep "return findings as text"). Keep the filter regex and a one-clause consequence; delete the rest. Saved: ~25.

**W4. Measurement provenance in the adapters.**
"(measured on codex-cli 0.162.1)" at CXD:21, already held at `docs/decisions/model-roles-and-effort.md:189`. Delete it. Saved: ~5.
The other version qualifiers (CX:18 "On codex-cli 0.162.1", CX:44 "Read on codex-cli 0.164.0") state what a reader needs to know, so they stay.

**W5. Accepted trade-off in SDD:177: "an edit inside one goes unseen, an accepted residual" (~8).**
Already held at `docs/decisions/shared-tree.md:19`. Delete it. Saved: ~8.

**W6. A seat's job specified in the controller skill.**
- SDD:155, the adjudicator: its inputs, mandate, git validation flags (`cat-file -t`, `--is-ancestor`, `-U10`, `--output`), scratch path and read/write limits, all inline in one 295-word paragraph. Only the inputs list is the controller's.
- SDD:95-102, the task reviewer's rubric (R17).

Destination for the git procedure: the shared seat reference (R18). The adjudicator's mandate and its read/write limits go either to a new adjudicator template beside the others, or stay inline as the one dispatch with no template (Q5).
Saved in SDD: ~75 (git procedure) + ~120 (rubric).

**W7. `ultra` in host-neutral DC:82 ("unless the operator asks for one, `ultra` included").**
`ultra` is named as a Codex reasoning level at CXD:15-17. The Claude Code effort setting at CCD:16 names no levels, so I can't tell whether it is host-neutral. If it is Codex-specific, it belongs in CXD (Q4).

**W8. Rationale clauses beyond one.**
- SDD:10 "Why subagents" (27): one sentence of why, acceptable.
- SDD:131 and RCR:63 both carry "your context stays clean for coordination, and controller fixes skip review", the same why twice (R14).
- RCR:26 "That is the execution phase's visibility surface: a roll-up nobody reads is a silent discard", plus "since this triage is the last stage that reads them and an item omitted here is closed nowhere": two whys for one input. Keep one. Saved: ~20.

No item in my files needs new text in `docs/`. Every wrong-level passage I found is already held by a record (W2-W5) or is a move inside `skills/` (W1, W6, W7).

## 4. Grain

**G1. Two "Step 6"s, plus collisions on steps 4 and 5, at one Finish (confirmed known item).**
SDD § Finish numbers its steps 1-7:
- step 4: open items and umbrella mark (SDD:212)
- step 5: the suite (SDD:213)
- step 6: workspace deletion, `.crucible/<slug>/` (SDD:214)
- step 7: invokes FIN.

FIN numbers its own:
- Step 4: Present Options (FIN:70)
- Step 5: Execute Choice (FIN:101)
- Step 6: Cleanup Workspace, the worktree (FIN:217)

Both sets are reached in one Finish. Cross-references use bare numbers on both sides:
- SDD:211 "skips steps 4 and 5 … before step 6" (SDD's)
- FIN:14 "Steps 1, 3 and 4 do not run" (FIN's)
- FIN:43, :58, :126, :211 "Step 6" (FIN's)

"Workspace" also means two things:
- FIN:14 "confirmed before the workspace was deleted" means SDD's feature workspace;
- FIN:43, :51, :217, :241 use "workspace" for the worktree.

Proposed trim, word-neutral:
- rename FIN § Step 6 to "Step 6: Remove the worktree" and say "worktree" at FIN:43, :51 and :241;
- name SDD's step 6 "Delete the feature workspace";
- have SDD:211 and FIN:14 cite steps by name with the file.

Saved: 0.

**G2. SDD:81 BLOCKED bullet (153 words) beside siblings of 5-15 words (SDD:78-80).**
It carries the binding-item correction routing, which § Deviations (SDD:87) and flip-paths also carry. Trim to "assess: context → re-dispatch; reasoning → tier bump, then the operator; oversized → split; defective plan or binding item → § Plan changes / flip-paths". Saved: ~90.

**G3. SDD:87 Deviations (269 words), one paragraph holding seven rules.**
These are advisory vs binding, what binds, the umbrella finding clause, the hypothesis rule, BLOCKED, deferred items, and the stop-and-ask triggers. After R8 and R9 it would be ~110 words. Its "Stop-and-ask triggers, for the implementer and for you" is also in the implementer template.

**G4. Long single paragraphs.**
- SDD:155 (295; one paragraph holds inputs, git procedure, mandate and limits).
- SDD:210 (325; Finish step 2).
- SDD:212 (239; Finish step 4). About 130 words of it are the procedure for telling whether a feature was born before its umbrella (`git grep`, `cat-file -e`, `log --diff-filter=A`), an edge case beside steps 6-7 of ~15 words. It could sit at `umbrellas.md:79`, which already states the concept ("A child that existed before its umbrella…"), with SDD step 4 pointing there. Net 0 in `skills/`.
- RCR:26 (293, one sentence).
- VSL:12 (190), VSL:13 (227).

**G5. The same why repeated.**
- "silently drops all but the last commit" (`HEAD~1`): SDD:93, RCR:22, `code-reviewer.slots.md:17` (R13).
- "a silent discard": SDD:151, SDD:199, RCR:26, RCR:80 (R19).
- "controller fixes skip review": SDD:131, :191, :222, RCR:63 (R14).

**G6. Rules restated within one file.**
- SDD, the "Questions items are leads" rule: SDD:95, :169, :172.
- SDD, "missing verdict": SDD:91, :126. RCR: RCR:36, :39.
- SDD, containment: SDD:81, :161, :195 (R10).
- RCR, model floor: RCR:24 and RCR:89 (red flag).
- RCR, controller fixes: RCR:38, :63, :88.
- RCR red flags RCR:86-89 restate the body, and RCR:78-79 restate RCR:8 and :22.
- FIN Common Rationalizations FIN:257-267 each restate a body rule (e.g. FIN:267 restates FIN:16-19). The Quick Reference table FIN:244-251 restates Step 5.
- SDD Common Rationalizations SDD:221-227 restate body rules.

`skills/writing-skills/SKILL.md:150` endorses rationalization tables, so whether they count as restatement needs a ruling (Q1). If they don't count, the only trims are RCR's Red Flags list, which duplicates both body and table (~25 words), and FIN's Quick Reference (~50).
One row carries a rule found nowhere else: FIN:268 "force-push only on your human partner's explicit request". Any trim of the table has to move that rule into Option 2 first.

**G7. Adapter entries at different grain.**
- CXD:14-28 "Select effort" is ~120 words, against ~30 for its siblings. The config.toml read is a procedure of its own, and could be a sibling bullet ("Seat effort default").
- CCD:18-29 "Report-name filter" and "Compaction" are host facts listed among operations ("Dispatch an instrument", "Resume", "Select effort"). A subheading such as "Host behaviours" would separate them. Saved: 0.

## 5. Shared seat reference

Skipped (templates reader). For that reader's table, my files contribute:
- R8 and R9 (binding clause and hypothesis rule, in four SDD/RCR templates);
- R18 (the diff-building procedure, which SDD:155 restates for the adjudicator; the adjudicator would point to it).

## 6. Totals

| File | Words now | Estimated removal by placement | Main items |
|---|---|---|---|
| SDD | 6,881 | ~800 | R5-R11, R13-R23, R26-R28, W2, W5, W6, G2 |
| RCR | 2,562 | ~525 | R5, R8, R11-R16, R19, R20, R23, R24, R28, R29, G6 |
| VSL | 1,308 | ~200 | R8, R11, R22-R25 |
| CC + CX | 708 | ~100 | R1, R2, R4 |
| CCD + CXD | 527 | ~70 | R3, R31, R32, W3, W4 |
| FIN | 1,920 | 0 (optional ~85 if Q1 allows trimming the table and Quick Reference) | G1 renames only |
| RR | 515 | ~10 (optional; "new scope is a new feature", RR:35, also at FIN:188-189 and RCR:51) | |
| ROUTER | 797 | +15 (takes R1, if Q3 chooses it) | |
| DC | 847 | +40 (takes R5, R6, the "builds its own diff" line) | |

Net: about **-1,650 words** from `skills/` in my files. Some of that relies on the shared seat reference absorbing R18, which the templates reader counts. Per session envelope: about -90 words (adapters).

Moving to `docs/`: nothing new. W2, W3, W4 and W5 are deletions whose text is already in `docs/decisions/task-loop.md:169-170`, `instruments.md`, `model-roles-and-effort.md:189` and `shared-tree.md:19`.

## 7. Questions

**Q1.** Do rationalization tables and red-flags lists count as restatement? writing-skills sanctions them (`skills/writing-skills/SKILL.md:150-157`). If they are exempt, G6's table items drop out. Either way, FIN:268's force-push rule exists only in a table row.

**Q2.** RCR:36 and RCR:39 say to treat a review missing a verdict "as § The Task Loop treats any review missing one". SDD:91 says only "never accept a report missing any verdict"; it states no action (resume the seat? re-dispatch?). The pointer's target lacks the action it points to. That is a rule gap, not a placement fault, but the rewrite will touch both sites.

**Q3.** Owner of the never-predict and name-the-model rules: ROUTER or DC? DC is read only by SDD, RCR and redteaming. `crucible:dispatching-parallel-agents` and ad hoc dispatches would lose the rule if it lived only in DC.

**Q4.** Is `ultra` (DC:82) a term both hosts share, or Codex-only? If Codex-only, it is a host term in host-neutral text and belongs in CXD. The claude-ism scanner does not catch it: no match in `tests/claudeism-allowlist.txt` or `tests/claudeism_scanner.py`.

**Q5.** The adjudicator is a controller-composed seat with no template. Is moving its seat-side text out of SDD:155 into a new adjudicator template within the rewrite's "move, merge, trim" remit? The alternative is a shared-reference pointer only (R18), which leaves the mandate inline.

**Q6.** D1 and D2 need rulings before the copies are merged, because merging picks one version.
