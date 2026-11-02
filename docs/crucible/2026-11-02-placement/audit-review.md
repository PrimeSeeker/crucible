# Placement review: review-before-code reader

> Advisory input to `design.md`, read at `8332a00`. Where the spec decides otherwise (its Decisions and its corrections list), the spec governs; the questions below were answered in its brainstorm.

Tree: the repository at HEAD `8332a00`, clean before and after (`git status --short` empty both times). All locations are `file:line` as read on this tree, and every path is under `skills/`. Word counts are `awk NF` per line: whole-line counts are exact, clause counts are estimates.

Files covered: `redteaming/SKILL.md` (6,098 words), `redteaming/references/{formats,flip-paths,plan-phase,folded-lane}.md`, `brainstorming/SKILL.md` (3,517), `brainstorming/references/{umbrellas,lane-note,folded-lane-document}.md`, `writing-plans/SKILL.md` (1,897). I opened the templates only to find restatement sites.

## 1. Restated rules

**R1. No `Review: branch only` mark is added once the plan's review has closed** (known item, confirmed at four sites):
- `writing-plans/SKILL.md:42`, last sentence (~17 words): "A mark is added only before the plan's review closes; after that, the task keeps its review."
- `redteaming/references/plan-phase.md:14`, last sentence (~7 words); the whole **Marks** paragraph is 39 words.
- `redteaming/references/folded-lane.md:13`, last sentence (~7 words); the whole **Marks** paragraph is 43 words.
- `subagent-driven-development/SKILL.md:83`, last sentence (~13 words).
- Proposed owner: writing-plans § Per-task structure, which defines the mark and is the page every other site already points to for its form.
- The plan-phase and folded-lane **Marks** paragraphs can go entirely. Their other clause, that the close readout lists the marked tasks, is owned by `redteaming/SKILL.md:130` (see R2).
- SDD:83's sentence becomes nothing: it already points to writing-plans in its first clause.
- Saves about 95 words.

**R2. The close readout lists the marked tasks:**
- `redteaming/SKILL.md:130` (59 words): this is the owner, since the controller writes the readout there.
- `formats.md:301-303` (~20)
- `plan-phase.md:14` (~15)
- `folded-lane.md:13` (~15)
- `brainstorming/SKILL.md:60` ("reported at the close of the phase that reviews the plan", ~10; keep, it tells the proposer why marks aren't confirmed at step 4).
- Saves about 50 words, counted with R1 and R14.

**R3. Spec-marker naming: the plan names each spec marker, by its site, in the Contract of each task that owns it** (known item, confirmed):
- Stated twice in writing-plans: `writing-plans/SKILL.md:31` ("Name each of the spec's markers, by its site, in the Contract of each task that owns it…", ~30 words) and `:39` ("the spec's deferral markers it owns, named by their sites (§ Deferring detail)", ~12).
- Also stated at:
  - `brainstorming/SKILL.md:92` ("The plan names each marker, by its site, in the Contract of each task that owns it, and a mechanical pre-pass checks that each has one", ~28)
  - `redteaming/SKILL.md:85` (~25)
  - `redteaming/SKILL.md:107` ("for a spec marker each owning Contract naming it", ~8)
  - `folded-lane.md:15` (~20)
  - `folded-lane-document.md:9` (~12)
  - `redteaming/seat-prompt.md:100-103`, the pre-pass check, which is the seat's own rule.
- Proposed owner: writing-plans § Deferring detail, where the plan author acts. Proposed changes:
  - `:39` keeps "the spec's deferral markers it owns (§ Deferring detail)".
  - brainstorming:92 keeps a one-clause pointer.
  - redteaming:85 keeps "named in its owning task's Contract (writing-plans § Deferring detail)".
- Saves about 45 words.

**R4. Shared-tree rules restated in redteaming** (known item, confirmed):
- `redteaming/SKILL.md:32` is 151 words. Most of it restates `subagent-driven-development/SKILL.md:176-177`: the no-commit rule and why ("the index is shared, so a bare commit sweeps in whatever that agent staged; queue the commit"), and the whole status-check mechanics (`git rev-parse HEAD`, `git status --porcelain --untracked-files=all`, `tree-check.txt`, the voiding rule, untracked paths tolerated). It does this right beside its own pointer to SDD § Shared-tree rules.
- Local content to keep: the list of redteaming windows (panel batches, round-0 pre-pass, blind verifier, terminal pass, plan-phase pre-pass and coherence seats), "dispatch with your fixes committed", and "your fix apply lands between windows".
- Model to copy: `requesting-code-review/SKILL.md:28`, which binds its seats to SDD § Shared-tree rules by pointer alone.
- Owner: SDD § Shared-tree rules. Saves about 95 words.

**R5. Replacing a lost seat** (never start a replacement until the host confirms the first has stopped; an unconfirmable state is a stop-and-ask):
- `redteaming/SKILL.md:75` (~35 words) restates `subagent-driven-development/SKILL.md:178`.
- Keep redteaming's local difference: a fresh seat id, not `-r<R>`.
- Owner: SDD:178. Saves about 30 words.

**R6. Operator rulings also enter `brainstorm-decisions.md`, and changes to the ask enter `request.md`.** Owner: `formats.md:88-99` (~110 words), which is binding and covers every phase. It is restated, each with a pointer back, at:
- `redteaming/SKILL.md:134` (~30)
- `flip-paths.md:3`, last sentence (~35)
- `brainstorming/SKILL.md:116` last sentence and `:118` last sentence (~12 and ~16)
- `requesting-code-review/SKILL.md:43` (~30)
- `subagent-driven-development/SKILL.md:161` (~30)
- `subagent-driven-development/references/very-small-lane.md:7` (~30)

Each phase site can shrink to "(also entered per `formats.md` § Feature workspace root and layout)". Saves about 15 per site, about 100 in total, about 55 of it in my files.

**R7. An answer that leaves the call to the controller is recorded as delegated, never as the operator's ruling:**
- `brainstorming/SKILL.md:116` (~30 words) is the owner: it defines the entry form.
- `formats.md:93-95` (~25) restates it, with drifted wording (D1). Its earlier clause, "in that record's entry form … and with its status", already covers the rule.
- Saves about 25 words.

**R8. Deferral boundaries** (binding or cross-task content is never deferrable; a misplaced deferral is a defect; "the detail is missing" is no defect):
- `writing-plans/SKILL.md:33` (65 words) is the owner for the plan author.
- `redteaming/SKILL.md:85`'s last two sentences, "Two findings *against* a deferral … unsafe … misplaced … 'The detail is missing' is neither", ~65 words, restate it nearly verbatim.
- `brainstorming/SKILL.md:92` restates "Binding and cross-task content is never deferrable" (~6).
- The seat-side form lives in `seat-prompt.md:143-157` (finding scope).
- redteaming:85 can keep the disposition rule and point to writing-plans § Deferring detail for unsafe or misplaced. Saves about 50 words.

**R9. Finding scope:**
- `redteaming/SKILL.md:93` (108 words) restates `redteaming/seat-prompt.md:141-157`, the seat's binding finding scope, nearly verbatim.
- The controller's own act is the last sentence: a finding outside scope is merged and `rejected` with that ruling.
- Owner: seat-prompt for the rule; redteaming keeps the enforcement sentence and a pointer. Saves about 70 words.
- `redteaming/SKILL.md:91`, finding hygiene, has the same pattern on a smaller scale. It states the seat's staking and evidence rules, and the controller's own act is "`UNVERIFIED` findings never enter a fix list". Saves about 20 words.

**R10. Consumer sweep:**
- `brainstorming/SKILL.md:110` (check 5, ~60 words of sweep) is the owner. `redteaming/SKILL.md:113` already points to it.
- `writing-plans/SKILL.md:38` restates it in the Files field (~40): "Enumerate the existing consumers … mechanically, by search, not from memory … A rule stated in more than one place — docs, prompts, templates — is such an interface".
- writing-plans:38 can point to brainstorming § Spec self-review's consumer sweep and keep "each lands in this list or in the census". Saves about 30 words.

**R11. Kinds of acceptance check** (standing test vs one-time check; absence criteria are one-time):
- `brainstorming/SKILL.md:83` (~54 words)
- `writing-plans/SKILL.md:60-65` (~165 words, the fuller copy)
- Proposed owner: writing-plans § Acceptance maps to checks. brainstorming:83 keeps "maps to a standing test or a one-time check (`crucible:writing-plans` § Acceptance maps to checks), or states why neither". Saves about 30 words. See Q4.

**R12. A failing check is the evidence that it can fire:**
- `writing-plans/SKILL.md:63` (~25)
- `redteaming/SKILL.md:115` (~25)
- `brainstorming/references/lane-note.md:10` (~30)

Each reader (plan author, fix-list author, lane-note author) acts at its own site and the copies agree. I note it but propose no change.

**R13. What binds in a spec, and "the spec is a hypothesis; binding text is read for its intent":**
- `flip-paths.md:3`, its opening sentences (~90 words): the cited owner, since `redteaming/SKILL.md:105` and `:170` point to "what flip-paths.md opens by stating binds".
- `brainstorming/SKILL.md:86` (89)
- `writing-plans/SKILL.md:20` (binding list, ~60) and `:52` (hypothesis plus BLOCKED, ~70)
- `subagent-driven-development/SKILL.md:87` (~100)
- `subagent-driven-development/references/dispatch-composition.md:20-33`
- the templates (seat, terminal-pass, implementer, task-reviewer, re-review, code-reviewer; the templates reader has those).

Proposals:
- brainstorming:86 becomes a pointer ("binding from the campaign's close as `flip-paths.md` states; changed only by its paths"), saving about 60.
- writing-plans:20's binding list points to dispatch-composition item 4 or flip-paths, saving about 60.
- writing-plans:52's implementer clauses, see W3.

**R14. A plan is not campaigned; the plan phase is one round with no loop and no cap:**
- `redteaming/SKILL.md:12` (~40)
- `redteaming/SKILL.md:149`, last sentence (~15)
- `redteaming/SKILL.md:153`, first sentence (~25)
- `plan-phase.md:3` (~35, the owner)
- `plan-phase.md:28` (~10)
- `formats.md:345-346` (~10)
- `writing-plans/SKILL.md:86` (~8)

redteaming:153 keeps only the read instruction (saves 25), and plan-phase:28's "cap arithmetic does not apply" goes (saves 5). Saves about 30 words.

**R15. The folded preset: what it is, and where its entry comes from:**
- `redteaming/SKILL.md:12` (~12)
- `redteaming/SKILL.md:157` (78)
- `folded-lane.md:3` (57) and `:5` (54)
- `brainstorming/SKILL.md:51,66`
- `folded-lane-document.md:3`
- `writing-plans/SKILL.md:20` ("where the folded preset has folded the plan into the spec — one combined spec+plan document and no separate plan file", ~22)

Owner: `folded-lane.md` for the campaign side, brainstorming § Proposing the arrangement for the entry. Proposals:
- redteaming:157 keeps the trigger and the read instruction (saves about 30).
- folded-lane:5 becomes "the route entry in the brainstorm decision record confirms it (`crucible:brainstorming` § Proposing the arrangement)" (saves about 40).
- writing-plans:20's description becomes a pointer (saves about 15).

`subagent-driven-development/references/very-small-lane.md:5` is the very-small twin of folded-lane:5.

**R16. Ledger seeding at the folded close:**
- `redteaming/SKILL.md:164` (90 words): it says which items, and how, "as plan-phase.md states".
- `folded-lane.md:21` (~25 of 57; it points back to redteaming § Exit)
- `plan-phase.md:34` ("and at the other closes that seed the ledger (the folded campaign's…)")

Owner: `plan-phase.md:32-34` for the seeding form; redteaming § Exit for "the folded close seeds". redteaming:164 keeps "names SDD, not the plan skill, and its close seeds the ledger as `plan-phase.md` § Close states for the plan phase", and folded-lane:21 goes to its first clause. Saves about 60 words.

**R17. An open premise ask at an umbrella's landing:**
- `umbrellas.md:36` (step 2, 69 words): the owner.
- `umbrellas.md:47` (~30)
- `flip-paths.md:48` (44)
- `redteaming/SKILL.md:165` (82 words, which also restates umbrellas § Landing step 3 and "an umbrella takes no plan phase and no SDD")

The flip-paths bullet should keep only "put to the operator with the landing ask (`umbrellas.md` § Landing step 2)", and redteaming:165 only "names the umbrella's landing (`umbrellas.md` § Landing), not the plan skill". Saves about 70 words.

**R18. A premise ask opens no wave, holds no cap and is never an open finding:**
- `flip-paths.md:37` (the owner)
- `redteaming/SKILL.md:138` last sentence (~25), `:140` ("premise findings aside"), `:149` ("An open premise finding is its own ask and joins neither cap ask", ~12)
- `formats.md:236-237` (~15)

redteaming:138 keeps "a premise finding is a decision ask (`flip-paths.md` § Premise findings)". Saves about 30 words.

**R19. Round readout contents:**
- `redteaming/SKILL.md:123-132` (~420 words): the owner.
- `formats.md:292-316`, field 8 (~200 words), restates the whole item list and the trace, with drift (D4).

Field 8 becomes "the readout as delivered, with the items `crucible:redteaming` § Round readout defines; then a part opened by `Trace:`, holding [the two trace items]". Saves about 110 words.

**R20. Question and finding dispositions:**
- `redteaming/SKILL.md:79` lists the six finding dispositions, and `formats.md:228-229` lists them too.
- `redteaming/SKILL.md:89` defines the four question dispositions, and `formats.md:264-271` defines them too (~50 words).

Formats owns the vocabulary and redteaming the rules for choosing among them. Each could keep its half. Saves about 40 words.

**R21. Where a plan-half re-run or arithmetic re-run is recorded:**
- `formats.md:165-170` (the owner)
- `folded-lane.md:10` ("record it in that record's `Verifier block`, or under its `Fix list` where it has none", ~15)
- `plan-phase.md:20` ("record it in the `Verifier block`", ~6)

Saves about 18 words.

**R22. Announce the plan phase's shape and proceed; it is no approval gate:**
- `plan-phase.md:12` (the owner)
- `writing-plans/SKILL.md:86` (~22)

Also "the handoff is the controller's explicit move, stated in the close readout", at `writing-plans/SKILL.md:87` (~12) and `redteaming/SKILL.md:161` (the owner). writing-plans' Exit becomes two pointers. Saves about 34 words.

**R23. The terminal pass's two mandates:**
- `redteaming/SKILL.md:144-145` (96 words) restates `redteaming/terminal-pass-prompt.md:91-163`, despite saying they "are stated in full" there.

The controller needs the names and the inputs (`:142`), not the contents. Saves about 70 words.

**R24. Umbrella binding scope** (own entry, plus the umbrella's Constraints & invariants and firm decisions, up the chain; a change to the entry other than its own mark or a clarification is a finding):
- `umbrellas.md:53` (the owner, 189 words)
- `subagent-driven-development/references/dispatch-composition.md:25-33` (the dispatch owner)
- `writing-plans/SKILL.md:20` (~70)
- `subagent-driven-development/SKILL.md:87` (~70)
- the templates

writing-plans:20 and SDD:87 point to umbrellas § Children. Saves about 60 in writing-plans and about 60 in SDD.

**R25. Feature-folder birth and resolve, and committing what agents must read:**
- The owners are `formats.md:386-403` and `:45-48`.
- `brainstorming/SKILL.md:88` restates the birth refusal and "which creates nothing" (~25)
- `brainstorming/SKILL.md:90` ("worktree agents can't read gitignored files")
- `writing-plans/SKILL.md:14` (resolve, suffix naming, gitignored reason, ~30)
- `lane-note.md:16` and `folded-lane-document.md:11` (identical persistence sentences, ~20 each)

Saves about 70 words.

**R26. Feature-worktree mechanics:**
- `brainstorming/SKILL.md:88` (~100 of 222 words) restates `using-git-worktrees/SKILL.md:10,69,73,77`: another feature's linked worktree, Step 1b, the base branch, the main checkout's worktree directory.

Owner: using-git-worktrees. brainstorming keeps "establish this feature's worktree with `crucible:using-git-worktrees` before the first write; the spec, workspace and records live there". Saves about 50 words.

**R27. Brainstorming's terminal state and its two exceptions:**
- `brainstorming/SKILL.md:8` (the owner of the summary)
- `:23`, `:25`, `:26` (flow steps 6, 8, 9)
- `:128`, `:130`, `:132`
- `umbrellas.md:27,29`
- `folded-lane-document.md:5,11`

The approval-only umbrella path alone appears 6 times. See G4.

**R28. The very-small lane note: drafted and self-reviewed at step 4, written as approved at step 5:**
- `brainstorming/SKILL.md:23`, `:67`, `:100`
- `lane-note.md:3`, `:10`

Owner: lane-note.md, with step 4's line in brainstorming:67. Saves about 25 words.
- `lane-note.md:10,12` (SDD side: departures as ledger lines, re-pin) and `subagent-driven-development/references/very-small-lane.md:7` (binding and advisory parts) restate each other in both directions, about 25 and 40 words.
- Owner split: lane-note for the parts and freezing, the SDD reference for re-pin and departures.

**R29. The decision-ask form** (analyst language, with a recommendation; never requires reading the artifacts; may quote the lines it turns on):
- `redteaming/SKILL.md:126`
- `subagent-driven-development/SKILL.md:14`
- `requesting-code-review/SKILL.md:43`
- `flip-paths.md:3,37,56`
- `receiving-review/SKILL.md:30`

The copies have drifted (D2). A single owner, with every other site pointing to it, needs D2 ruled first.

## 2. Drifted copies

**D1. "The delegated status"** (known item, confirmed):
- `formats.md:93-95` reads: "An answer that leaves the call to the controller is entered with the delegated status that section defines".
- `brainstorming/SKILL.md:116` defines only three statuses (`open`, `accepted`, `firm`). Delegation fills the proposer's place: "recorded `accepted — delegated to the controller`, in the proposer's place".
- `redteaming/terminal-pass-prompt.md:138` gets it right.
- Intended: brainstorming's version. The formats sentence can be dropped (R7).

**D2. What a decision ask must contain:**
- `redteaming/SKILL.md:126` adds "Each ask lists every option the findings behind it propose, and states what its change withdraws from an earlier operator approval".
- `subagent-driven-development/SKILL.md:14` and `requesting-code-review/SKILL.md:43` lack both clauses. They also say "plan, code or a diff", where redteaming says "spec, plan, code or diffs".

I cannot tell whether the options and withdrawal clauses are meant for execution and branch-review asks. **Needs a ruling.**

**D3. What is never deferrable:**
- `brainstorming/SKILL.md:92`: "Binding and cross-task content is never deferrable."
- `writing-plans/SKILL.md:31`: "binding or crosses tasks".
- `redteaming/SKILL.md:85`: "Non-local mechanism — cross-task or cross-component contracts, shared formats, orderings or state, consumers outside the change's own files — is never deferred". The seat prompt (`seat-prompt.md:147-150`) carries this same list.

The spec and plan copies miss cross-component contracts and consumers outside the change's files. Intended: the fuller redteaming and seat list, which the shorter copies paraphrase.

**D4. Where the trace carries decision-ask ids:**
- `redteaming/SKILL.md:132`: the trace holds "each decision ask's merged-list ids", for any readout.
- `formats.md:311-313`: "in a numbered round record and the plan record".

Round 0's and the terminal-pass record's readouts have no merged list, so the formats copy is the coherent one. Intended: formats' scope.

**D5. Round-1 lenses on the folded lane:**
- `folded-lane.md:11`: "**The round-1 seat carries the right-sizing and outside-the-frame lenses** alongside general". This is singular, and puts both lenses on one seat.
- `folded-lane.md:3`, same file: "the lens roster … applies unchanged".
- `redteaming/SKILL.md:59,61`: right-sizing is seated in round 1; outside-the-frame is one seat of round 1, beside general only in a one-seat round 1.

For a multi-seat folded round 1 the copies differ. If the line assumes a one-seat round 1, it is a pure restatement and can go (about 12 words). **Needs a ruling** if it is meant as a folded-lane rule.

## 3. Wrong-level text

- **W1.** `redteaming/SKILL.md:111`, "the measured dominant wave defect is the correct fix applied once while a sibling statement stands" (~17). The measurement is held at `docs/decisions/evidence-and-findings.md:320` and `docs/decisions/the-spec.md:306`. Delete.
- **W2.** `redteaming/SKILL.md:95`, last sentence, "an operator ratification obtained on one is the measured channel by which author-supplied false facts reach ratified decisions" (~20). Held at `evidence-and-findings.md:325`. Delete the "measured channel" clause, keeping "is a defect in the ask".
- **W3.** `writing-plans/SKILL.md:52`, second half (~70), and `:54` (~15): an implementer's BLOCKED escalation, the containment test, and logging deviations in the Decision Log. The plan author does not act on these; the implementer and the SDD controller do (`subagent-driven-development/SKILL.md:81,87`, the implementer template). Same for `writing-plans/SKILL.md:31`, "The call is the owning implementer's, logged in its Decision Log…" (~15). Reduce to the binding/advisory definition the plan author needs. Saves about 90 words.
- **W4.** `writing-plans/SKILL.md:44`, "There is no per-task constraints field … a per-task restatement would be a second copy to keep true" (38). This explains why the template omits something. Move to `docs/decisions/plans.md` if not already there; check before deleting. Saves 38 words.
- **W5.** `brainstorming/SKILL.md:110`, last sentence, "An unenumerated consumer and an unchecked claim are the two largest measured finding classes; both are cheaper…" (~25). Held at `evidence-and-findings.md:~320-328`. Delete.
- **W6.** `folded-lane-document.md:3`, "every binding-content pointer in the seat, terminal-pass, implementer and task-reviewer prompts names that section by name, so a folded document missing it aims all of them at nothing" (~30). This explains other files' design to maintainers. Shorten to "None folds away, Constraints & invariants least of all: every seat's binding pointer names it" (saves about 15), or move the full reason to `docs/decisions/routes.md`.
- **W7.** `folded-lane-document.md:5`, "don't restate them here" (~4), and `formats.md:3-6`, `:354-356`, `:407-408` ("defined once so writers and readers are built against one text", "skill prose points here rather than restating it", ~30 words in all). Text about crucible's own text; belongs in `docs/authoring.md`.
- **W8.** Small measurement asides:
  - `redteaming/SKILL.md:51`, "(advisory; derived from thin local data)" (5; held at `spec-campaign.md:187`)
  - `redteaming/SKILL.md:138`, "(counts stay flat deep into long campaigns)" (7; held at `spec-campaign.md:387`)
  - `redteaming/SKILL.md:117`, "(early victory is the named verifier failure mode)" and "because baseline verification doesn't end at round 0 when artifact growth doesn't" (~20)

  Delete; about 30 words.
- **W9.** `formats.md:35-36,41-43` (PowerShell 5.1 and UTF-16LE, ~35 words). Each is one clause of why, so within the rule, but it is incident-derived and platform-specific; held at `records-and-workspace.md:189-193`. Borderline; keep or trim to the actions.
- **W10.** `umbrellas.md:91`, "The fixed `closing-` prefix keeps every name clear of a host's report-name rules (…dispatch.md)" (~17). This is design rationale tied to host mechanics. Keep the prefix as an action and drop the reason, or move it to `docs/decisions/umbrellas.md`.

## 4. Grain

- **G1. Lens roster** (known item, confirmed). `redteaming/SKILL.md:59`, right-sizing, is 111 words; its siblings at `:55-58,60` run 14-17 words, and outside-the-frame `:61` 44. The bullet carries:
  - the seat's attestation obligation, which `seat-prompt.md:88-96` already holds;
  - the controller's cut rule ("consult those attestations before applying any cut — cutting attested content requires a logged ruling").

  Trim it to "(cost-benefit scope-cutting) — round 1 and periodically after; its seat carries the over-subtraction guard". Move the cut rule, about 45 words including "a proposed cut that would remove binding content … is a finding against the cut", to § Fix application, where cuts are applied. Saves about 45 net. See Q1.
- **G2. writing-plans' spec-pointer bullet.** `writing-plans/SKILL.md:20` is 246 words; its siblings at `:21-25` run 9-45. It carries:
  - the pin form;
  - the binding list (R13);
  - the umbrella chain (R24);
  - a plan-defect rule;
  - the folded form;
  - "point, never copy".

  Keep the pin form, the folded form and a pointer for what binds. Saves about 120 words, counted in R13 and R24.
- **G3. "Point, never copy spec text"** is stated 6 times within writing-plans (`:10`, `:20`, `:39`, `:44`, `:48`, plus `brainstorming/SKILL.md:81`). Keep it in § What a plan never contains (`:48`), with one clause of why. Saves about 50 words.
- **G4. Brainstorming's exceptions are restated within the file** (R27). Flow steps 6, 8 and 9 (`:23,25,26`) each repeat the very-small and approval-only-umbrella exceptions, which `:8` and § Handoff (`:128-132`) also state. Steps 6, 8 and 9 can name the step and point to § Handoff. Saves about 40 words.
- **G5. Instrument-dispatch boilerplate.** "Dispatch it as instrument X with its filled slot card (§ Dispatch composition)" appears at `redteaming/SKILL.md:69,117,142,147`. `:41` already states the rule for all three instruments. Saves about 25 words.
- **G6. The blind verifier's input.** "Fix list plus diff, never rationale" is stated at:
  - `redteaming/SKILL.md:38`, `:105`, `:117`
  - `formats.md:274-276`
  - `plan-phase.md:9` ("unchanged input contract") and `plan-phase.md:18` ("the fix list is the blind verifier's input")

  Keep `:38`, the departure that dispatch-composition requires, and `:117`. Saves about 20 words.
- **G7. `flip-paths.md:3`** is one 300-word paragraph. It mixes what binds, the hypothesis reading, the campaign-close bar, where supersede applies, the decision-ask form and the record-entry rule (R6). Its siblings run 28-150 words. Splitting it costs nothing, and dropping R6's clause saves 35 words.
- **G8. `redteaming/SKILL.md:170`** (233 words) is a trigger paragraph for reading `flip-paths.md`. It restates that reference's rules:
  - the bar from the campaign's close;
  - containment confirms;
  - supersede applies inside the campaign;
  - splitting before close returns to brainstorming (restates `umbrellas.md:55`).

  The trigger list plus the read instruction would do. Saves about 120 words. `subagent-driven-development/SKILL.md:195` is its execution twin; the SDD reader has it.

## 6. Totals (estimates, words removable from skills/)

| File | Estimated saving | Main sources |
|---|---|---|
| `redteaming/SKILL.md` | ~800 | R4 95, R5 30, R8 50, R9 90, R14 25, R15 30, R16 50, R17 45, R18 30, R23 70, R6 20, G1 45, G5 25, G6 15, G8 120, W1/W2/W8 65 |
| `writing-plans/SKILL.md` | ~430 | G2 (with R13/R24) 120, G3 50, W3 90, W4 38, R3 6, R10 30, R22 34, R25 25, mark-dispatch clause at `:42` 20 |
| `brainstorming/SKILL.md` | ~310 | R13 60, R26 50, R25 25, R3 20, R11 30, W5 25, G4 40, R28 25, R6 10, R8 6 |
| `redteaming/references/formats.md` | ~215 | R19 110, R7 25, R20 35, R18 15, W7 30 |
| `redteaming/references/folded-lane.md` | ~125 | R1/R2 43, R15 40, R16 15, R21 15, D5 12 |
| `redteaming/references/flip-paths.md` | ~60 | R6 35, R17 25 |
| `redteaming/references/plan-phase.md` | ~50 | R1/R2 39, R21 6, R14 5 |
| `brainstorming/references/folded-lane-document.md` | ~40 | W6 15, W7 4, R25 20 |
| `brainstorming/references/lane-note.md` | ~40 | R25 20, R28 20 |
| `brainstorming/references/umbrellas.md` | ~20 | W10 17 |
| **My files, total** | **~2,090** | |
| Sites outside my files | ~200 | SDD:83 13, SDD:87 60, SDD:161 15, very-small-lane:7 40, requesting-code-review:43 15, others |

What would move to `docs/`:
- W4, the per-task-constraints design reason, to `docs/decisions/plans.md` (check first);
- W6's full reason to `docs/decisions/routes.md`;
- W7's text-about-text lines to `docs/authoring.md`;
- W10's reason to `docs/decisions/umbrellas.md`.

Everything else in § 3 is deletion: the decision records already hold it, as cited.

## 7. Questions

- **Q1.** "A proposed cut that would remove binding content, or a declared mechanism's only producer or consumer, is a finding against the cut" appears only in the controller's skill (`redteaming/SKILL.md:59`). Neither `seat-prompt.md` nor its slot card carries it, so seats never see the rule that turns a cut into a finding. This is a placement question, possibly a gap: should it live in the seat prompt's right-sizing passage?
- **Q2.** D2 (whether execution and branch-review decision asks must list every option and state what they withdraw) and D5 (the folded round-1 lens line) need rulings before a merge.
- **Q3.** R1's owner. I propose writing-plans, which defines the mark. The other defensible owner is SDD § The Task Loop, step 2, where a post-close plan edit would happen. Either works if the other three sites go.
- **Q4.** R11, the kinds of acceptance check. I chose writing-plans because it is the fuller copy. The spec contract classifies acceptance first, so brainstorming could own the two definitions instead, with writing-plans adding the mapping and the fail-before clause. Your call.
- **Q5.** R16 and R17: redteaming § Exit, plan-phase § Close and folded-lane § Exit form a pointer loop for the folded close's seeding. Folded-lane points to redteaming § Exit, which points to plan-phase for the form. Whichever owner is chosen, the loop should run one way.
