# Placement audit: the templates reader

> Advisory input to `design.md`, read at `8332a00`. Where the spec decides otherwise (its Decisions and its corrections list), the spec governs; the questions below were answered in its brainstorm.

Tree: the repository at `8332a00`, `git status --short` empty before and after; nothing in the repository was written. Word counts come from a script over the line ranges cited. "Saved" figures are estimates, net of any pointer left behind.

Short names: S = `skills/redteaming/seat-prompt.md`, V = `verifier-prompt.md`, T = `terminal-pass-prompt.md` (both in `skills/redteaming/`), B = `skills/requesting-code-review/code-reviewer.md`, I = `skills/subagent-driven-development/implementer-prompt.md`, R = `.../task-reviewer-prompt.md`, X = `.../re-review-prompt.md`, PQ = `.../references/premise-and-questions.md`, DC = `.../references/dispatch-composition.md`, WGT = `.../writing-good-tests.md`, SDD = `skills/subagent-driven-development/SKILL.md`, RCR = `skills/requesting-code-review/SKILL.md`, RT = `skills/redteaming/SKILL.md`. "Shared ref" = the proposed shared seat reference (§5).

## 1. Restated rules

Each item gives the sites (with approximate words), the owner, what the other sites become, and the words saved.

1. **What binds (pointer, umbrella chain, change-is-a-finding, "the spec is a hypothesis", read for intent).** S:38-61 (265), T:64-85 (239), B:66-92 (309), I:90-109 (213), R:53-73 (246), X:51-68 (209), DC:20-41 (243), plus outside my files SDD:87, RCR:26, very-small-lane.md:13, writing-plans/SKILL.md:20 and :52, brainstorming/SKILL.md:86, flip-paths.md:3, umbrellas.md:53 (the umbrella rule's own owner). Owner for seats: shared ref § What binds, written in two forms: *an artifact calling for* a change (S, T) and *within the range you review* (B, I, R, X). Each template keeps one line pointing there plus its own route for a literal-reading case (finding / labeled finding to the controller / BLOCKED). DC item 4 keeps the pointer and the mandate line and drops the seat-side finding rule (DC:29-33). Saved: about 950 in the templates and 70 in DC.
2. **Seat conduct: the workspace, never another checkout, no delegation.** S:22-27, V:20-24, T:31-36, B:30-34 and :48, I:70-75 and :85-86, R:26-30 and :40-41, X:23-27 and :37. That is 433 words over 7 templates, and DC items 6-7 (DC:50-53) state the same on the controller side. Owner: shared ref § Seat conduct (about 50 words). Each template keeps a pointer plus its seat-specific lines: I's git identity, staging and branch rules (I:76-84), and B's throwaway-worktree rule (B:35-40). Saved: about 280.
3. **Read-only discipline, the scratch subdirectory and the suite bound.** S:114-127 (143), V:67-79 (140) and T:195-207 (140) are verbatim with each other. B:35-47 (120), R:31-39 (83) and X:28-36 (83) are a variant of the same rule. RT:47 restates the "scratch line" and the "suite bound" for round 0. Owner: shared ref § Read-only seats (about 110 words, one example path). Saved: about 550.
4. **Read scoping, general part** (read only what is enumerated, scope every search to it, never read `campaigns/`, of `sdd/` only the named paths). S:63-71, V:26-35, T:57-62, B:107-123, I:56-66, R:77-87, X:79-86 (737 in total, mostly per-seat lists). Owner: shared ref § Seat conduct for the general sentence. Each template keeps its own enumeration. Saved: about 240.
5. **Finding hygiene** (BLOCKER/MAJOR/MINOR; a BLOCKER without evidence is a question; improvements are not findings; formatting that no tool enforces is not a finding). S:129-139 (94), B:283-291 (91), R:236-249 (117), X:135-137 (formatting, about 20), T:241-242 ("seat-report hygiene applies"). Also restated by RT:91 (controller), SDD:95, and PQ:74-76 (the owner of "improvements go to Questions"). Owner: shared ref § Findings, which absorbs PQ § Location. Saved: about 180.
6. **Finding scope at spec and plan stage** (advisory register, local versus non-local mechanism). S:141-156 (134) and T:103-120 (159) are verbatim apart from the last bullet; RT:93 is a shorter controller copy (about 95). T cannot point into S, because S is not among T's inputs. Owner: shared ref § Finding scope. RT:93 keeps "you enforce it at merge" plus a pointer. Saved: about 125 in the templates and about 70 in RT.
7. **Building the diff as files** (cat-file and is-ancestor checks, `git log/diff --output`, an empty diff is reported). B:195-209 (121), R:110-127 (155), X:99-114 (123), and SDD:155 for the adjudicator (about 80). Owner: shared ref § Building the diff, with `<base>` as a parameter. Each template names its range and keeps any seat-specific line (R:122-124 "context lines ARE the changed files"; B:211-213 read beyond the diff). Saved: about 190, plus about 70 in SDD.
8. **Build history in shipped text.** B:238-243 (65), I:204-209 (56), R:220-224 (54), X:130-133 (48). Owner: shared ref § What shipped work carries. Saved: about 130 (but see drift D2).
9. **Comment rule.** B:248-252 (47), I:210-214 (46), R:225-229 (49), X:133-135 (29, a fragment). Owner: the same shared section. Saved: about 85; X gains the full rule through the pointer (D1).
10. **Weakened and deleted tests: the four justifications.** B:267-273 (54), I:160-167 (80), R:169-179 (117), X:140-147 (94), SDD:100. The core list is about 45 words. The angle differs by reader, as intended (`docs/decisions/test-rules.md:30-44`): I logs it, R checks the Decision Log, X checks the fix report, B judges from the code. Owner: WGT, beside § Warning Signs, which all four seats already read and which the list cites; the shared ref is the alternative. Each template keeps its one-line angle. Saved: about 180.
11. **Test-first exceptions and a removal's failing step.** I:146-155 (owner; the seat acts there), R:199-205 (74), B:186-188, SDD:101 and :112. Owner: shared ref § Tests in review, or keep I as owner, with R and B pointing to the shared copy (R and B do not read I). Saved: about 50.
12. **Silence is not permission.** B:224-227 (48), R:231-234 (50). Owner: shared ref § What shipped work carries. Saved: about 45.
13. **Reviewer test-running bound and truncated evidence** ("do not re-run the suite", "re-read at its stated path"). R:103-106 and :139-146, X:156-161; SDD:106 is the controller counterpart. Owner: shared ref § Read-only seats. Saved: about 70.
14. **Concerns ruling, and what the controller routes instead** (premise findings, Questions, proposals outside the task). R:98-101 and :193-198, X:118-124, SDD:126 and :167-172. Owner: shared ref § Concerns, with SDD § What a report voices as the controller side. Saved: about 50.
15. **Report-file contract** (begin directly with no preamble; the file is required; on a refused write, the full report goes in the reply). B:295-301 (86), R:267-273 (77), X:165-172 (86), S:117-119, V:69-71 and :89-91, T:197-199, I:282-284; DC item 5 is the controller side. Owner: shared ref § Report file. Saved: about 150.
16. **Selected passages.** The paragraph is identical at S:8-12, T:17-21, B:10-14, I:5-9 and X:7-11 (46 each, 230 in total). Recommended owner: none moved. It tells the seat how to read the template itself, so it must come before anything else (Question Q1). Saved: 0, or about 180 if the generator renders it from one source.
17. **Slot-card Operation line** ("each slot's rule replaced by its value, each selector line cut ... through your adapter's instrument-dispatch operation"). On all 7 cards (about 38 each, 266 in total); RT:41 and SDD:50 restate how to fill a card. Owner: DC, a new short § Filling a card. Each card keeps "instrument `X`, card filled". Saved: about 175.
18. **Card Model lines restate DC § Models and effort.** The three redteam cards ("explicit model, effort only on the operator's request", about 15 words each) versus the four SDD/branch cards ("REQUIRED ... Effort: per DC"). Owner: DC. Each card keeps only its role. Saved: about 45 (see grain G7).
19. **Seat mandates restated in controller skills.** The task reviewer's mandate is at SDD:95-104 (about 250; R:3-8 and R:148-260 own it). The verifier's mandate and its blindness are at RT:117 (about 95) and RT:38 (about 30). The re-reviewer's mandate is at SDD:126 (about 30). Owner: the template, since the seat acts there; the controller keeps only what it acts on (loop wiring, card inputs). Saved: about 250, in other readers' files, so flagged only.

## 2. Drifted copies

- **D1, confirmed: the comment rule fragment.** X:133-135 has only "absent project comment conventions, a `file:line` citation in a comment". I:210-214, R:225-229 and B:248-252 also carry "states the current invariant, hazard, or local reason a line looks wrong but isn't", "points to the owning reference doc or decision record", and they cover docstrings. Intended version: the full rule. `docs/decisions/authoring-crucible.md:41-50` names the re-reviewer among the templates carrying the comment policy, and the umbrella's `placement` entry (`docs/crucible/2026-11-01-skill-text-rewrite/umbrella.md:310`) already rules that the re-review seat takes the full rule through the shared reference.
- **D2: what the build-history rule exempts.** B:241-243 exempts "Decision records, changelogs, the feature folder's files and the open items the controller's finish wrote". R:223-224 and X:132-133 exempt only "decision records and changelogs". I:207-209 says the history "belongs in commit messages, the feature folder, and the project's decision records or changelog". `docs/decisions/branch-review.md:270-280` widened the exemption for the branch reviewer only. My reading: the feature folder is meant to be exempt everywhere (a scoped amendment commit inside a task range edits it), while the open-items part is branch-only. **Needs a ruling.**
- **D3: "the report file is required even where your host advises returning findings as text"** appears only at V:89-90 and X:169-170. It is missing from S, T, B, R and I. `skills/using-crucible/references/claude-code-dispatch.md:22-24` describes that advice as host-wide. Intended: every report-writing seat.
- **D4: the suite bound.** R:141-143 says "never a package-wide suite, race detector run, or repeated/high-count loop; recommend heavy validation". S:125-127, V:77-79 and T:205-207 have no race/loop clause. X:159-161 has neither that clause nor the heavy-validation recommendation. Intended: probably R's superset everywhere. A low-stakes ruling.
- **D5: the terminal pass's findings carry no location.** T:237-242 requires substance and evidence. T:28-29 does not send it to PQ § Location, which S, B and I read. `docs/decisions/evidence-and-findings.md:12-15` says every finding carries evidence and a location. Intended: a location applies. **Needs a ruling** on whether that omission is deliberate.
- **D6: the `literal-reading` label.** PQ:28-30, which redteam seats read (S:19-20, T:28-29), says "a `literal-reading` finding keeps its own label". Yet S:56-59 and T:83-85 define no such label ("is a finding, naming the item and the case"); only B, R and X apply it. **Needs a ruling:** does a redteam seat label it (it matters in the plan phase, where the spec is binding)? If not, PQ:28-30 should be scoped to execution seats.
- Not drift, though the wording differs: the umbrella-entry clause at S:48-52, T:74-78 and writing-plans:20 omits "the feature's own mark" and "taken in from the base by a merge". That fits readers that review an artifact rather than a range. The checkout ban differs too: S, V and T ban reading; I and DC:50-51 do not, but I's Read Scoping (I:56-60) excludes other checkouts anyway.

## 3. Wrong-level text

| Site | Words | Kind | Destination | Saved |
|---|---|---|---|---|
| S:69-71, T:60-62, I:65-66 "an unscoped grep is the measured way ..." | 45 | measurement | delete; `docs/decisions/the-spec.md:281` holds the four cases | 45 |
| S:52-55, T:78-80 "deliberately not copied ... a copy drifts"; B:79-81; I:35-36, R:65-66, X:62 "none is copied into this prompt" | 95 | template explaining its design | delete; `the-spec.md` § Pointers, not copies holds it | 95 |
| V:8-14 blindness design ("its absence is the design, not an omission") | 100 | design note | keep about 20 words; rationale in `fix-verification-and-merge.md` § Blind verification and RT:38 | 80 |
| V:64-65 "Artifact growth doesn't stop at round 0 ..." | 14 | why | delete (RT:117 holds it) | 14 |
| V:71, T:199 "the controller saves it with a mark saying so" | 18 | controller routing | delete; DC item 5 owns | 18 |
| T:187-189 and :251-252 (flagged correction "is itself a decision ask"; "which makes it a decision ask") | 45 | controller routing | delete; RT:147 owns | 45 |
| T:191-193 "a record correction, not a verdict on its author: ... baseline error rate" | 33 | stance/rationale | delete; RT § Operating stance and `terminal-pass.md:120-125` hold it | 30 |
| T:181-186 "timing-free in both directions ... by construction" | about 75 | long why | compress to one clause; rationale to `docs/decisions/terminal-pass.md` (not there now) | 45 |
| R:256-260 "How your verdicts are consumed" | 55 | controller loop wiring (SDD:104) | one clause ("a failed verdict opens a wave whatever its label: stake honestly") | 35 |
| B:86-87, R:70-71, X:67-68 "it goes to the controller as a plan conflict"; B:160 "on which the controller opens a fix wave ..."; B:222-223; X:194-195 | about 55 | controller routing | delete; SDD:153 and RCR's loop own it | 50 |
| I:270-273 claim-discipline rationale ("The report feeds your reviewer, the ledger ...") | 45 | long why | `docs/decisions/evidence-and-findings.md` | 40 |
| B:150-151 "a roll-up nobody reads is a silent discard" | 14 | why, told 3 times (also SDD:199, RCR:26) | keep one copy, in RCR | 14 |
| DC:29-33 the seat-side finding rule inside a controller list | about 70 | seat rule at the controller level | shared ref § What binds (counted in item 1) | — |

No host-neutral rules in the adapters fall in my files.

## 4. Grain

- **G1, V's mandate.** "Every item" is stated four times: V:37-39 (the mandate line repeats the three verdicts), V:50 header "never stop at first pass", V:52-55 "early victory", and V:54-55 "a report that does not verdict every item individually is a failed verification". Keep the header and "early victory". Saved: about 45.
- **G2, B:350-363 Critical Rules DO/DON'T** (60, upstream). This restates § Calibration and § Output Format ("Give a clear verdict" and "Avoid giving a clear verdict" are both there). Delete it. Saved: about 55.
- **G3, B:211-213 "you may read beyond the diff"** restates B:112-114. Saved: about 25.
- **G4, R: the "requirement living outside the diff" rule** is stated three times (R:80-81, R:129-135, R:160-163). Keep it at Verdict 1. Saved: about 30.
- **G5, I: "binding item wrong → BLOCKED"** is stated three times (I:105-109, I:129-130, I:288-289). Saved: about 20.
- **G6, WGT.** The Quick Reference table at WGT:171-184 (165) restates every rule of Principles 1 and 2. The gate functions at WGT:65-79 and :135-148 (146) restate them again. § Tests Ship With the Implementation at WGT:150-155 (46) repeats WGT:50-52 and :60-63. Delete the table and trim the section to its one new clause; the gates are upstream form, so trimming them is optional. Saved: about 195.
- **G7, slot cards.** Sibling cards state the model at different grains: the redteam cards say "see SKILL.md § Panels" with no Effort line, while the SDD and branch cards have "REQUIRED: ..." plus an Effort line. Placeholder syntax also differs (`{x}` against `[X]`). Recommend one form. The words are counted in item 18.
- **G8.** The `-r<R>` replacement path is restated on four cards (B slots:16, I slots:12, R slots:11, X slots:12) beside SDD:159 and :178. Keep it on the cards, since that is where paths are filled; it is not worth moving.

## 5. Shared seat reference

### Copied clauses

| Clause | S | V | T | B | I | R | X | Move? |
|---|---|---|---|---|---|---|---|---|
| Selected passages | 46 | — | 46 | 46 | 46 | — | 46 | no (Q1) |
| Runtime: host tools, no router | ~25 | 26 | ~25 | ~25 | ~25 | ~25 | ~25 | no; keep one line naming the shared ref |
| Workspace / other checkouts | 36 | 36 | 36 | 53 | 56 | 53 | 53 | yes (I and B keep their git lines) |
| No delegation | 23 | 13 | 22 | 11 | 16 | 18 | 7 | yes |
| Read scoping, general sentence | ~30 | ~30 | ~30 | ~40 | ~40 | ~35 | ~35 | yes; per-seat lists stay |
| What binds and the umbrella chain | 265 | — | 239 | 309 | 213 | 246 | 209 | yes; literal-reading route stays |
| Read-only, scratch, suite bound | 143 | 140 | 140 | 120 | — | 83 | 83 | yes |
| Report file required / refused write / no preamble | ~35 | ~45 | ~35 | 86 | ~30 | 77 | 86 | yes |
| Finding hygiene | 94 | — | ~20 | 91 | — | 117 | ~20 | yes |
| Finding scope (spec and plan stage) | 134 | — | 159 | — | — | — | — | yes |
| Building the diff | — | — | — | 121 | — | 155 | 123 | yes |
| Build history | — | — | — | 65 | 56 | 54 | 48 | yes |
| Comment rule | — | — | — | 47 | 46 | 49 | 29 | yes (fixes D1) |
| Silence is not permission | — | — | — | 48 | — | 50 | — | yes |
| Weakened and deleted tests | — | — | — | 54 | 80 | 117 | 94 | core list to WGT or the shared ref; angle line stays |
| Test-first exceptions | — | — | — | ~25 | 112 | 74 | — | yes |
| Truncated evidence, no suite re-run | — | — | — | — | — | ~70 | ~60 | yes |
| Concerns ruling and controller-routed items | — | — | — | — | — | ~70 | ~80 | yes |
| Mandate in one line | 18 | 29 | 23 | 18 | — | 18 | 18 | no (per seat) |
| Local context in shipped text | — | — | — | ~30 | — | — | — | no (branch only; moving it would extend a rule) |

### Proposed outline

The proposal grows PQ and renames it. Any new name must avoid the Write filter `^(REPORT|SUMMARY|FINDINGS|ANALYSIS).*\.md$`, for example `seat-rules.md`. The umbrella asks for a rename; PQ is cited at about 12 skill sites plus records.

0. **Which sections you read.** A table of seat against sections, replacing each template's list. The alternative is to keep each template naming its sections, at about 15 words each.
1. **Seat conduct** (all seven): work from the worktree; never read, edit, write or run git against another checkout, nor cd into one; create no agents; use the host's tools and never re-run the router; read only what the dispatch enumerates and scope every search to it; for execution seats, never `campaigns/`, and of `sdd/` only the named paths.
2. **Read-only seats** (all but the implementer): edit nothing, and leave the working tree, index and HEAD untouched. Your writes are the report and a scratch subdirectory: the report path less `.md`, under `scratch/`, with one example. Run focused checks only (no package-wide suite, race run or high-count loop) and recommend heavy validation instead. Never re-run a suite a report evidences. Re-read truncated evidence at its stated path.
3. **Report file** (all seven): the file is the deliverable, even where the host advises text. If the write is refused, put the full report in the reply and say so. Begin directly, with no preamble or narration.
4. **What binds** (all but the verifier): the pointer and what the pin makes binding; the umbrella chain; the finding rule in its artifact form and its range form; "a hypothesis, probably subtly wrong ... read for intent". Each template keeps its literal-reading route.
5. **Findings:** the severities, a BLOCKER without evidence being a question, code-shaped claims carrying evidence or `UNVERIFIED` (where the template says so), improvements and style going to § Questions, formatting no tool enforces, and the current § Location.
6. **Finding scope at spec and plan stage** (S, T).
7. **What shipped work carries** (I, R, X, B): build history and its exemption (after the D2 ruling), the comment rule, and silence is not permission.
8. **Tests in review** (I, R, X, B): weakened tests, the deleted-test justification list (or a pointer to WGT), test-first exceptions, and a removal's failing step.
9. **Building the diff** (R, X, B, and the adjudicator through SDD:155).
10. **Concerns** (R, X): CONFIRMED or DISMISSED; an unruled concern is a missing verdict; premise findings, Questions and proposals are the controller's to route.
11. The existing sections: § Premise findings, § Binding items and unrecorded choices, § The goal check, § Questions, § The arrangement questions. Controllers also read the last one.

### How templates point to it

Each template's Runtime paragraph becomes: "You are running on {runtime} ... Before anything else read, under the plugin root your dispatch names, `skills/.../seat-rules.md` § Seat conduct, § ..., which bind as if written here." Each moved block leaves at most a one-line "per the shared reference § X" where the seat acts. Two catches:

- **V has no plugin-root slot,** and RT:36 lists its inputs as "nothing else". Pointing V at the shared ref changes its inputs, which needs a ruling (Q2). Without that ruling, V keeps its conduct inline and saves only its trims.
- **X does not read PQ today** (X:17-19). It gains the read, as the umbrella already intends.

## 6. Totals

These are net estimates, after the owner text is added to the shared ref.

| File | Words now | Est. removed |
|---|---|---|
| S | 1,770 | ~610 |
| V | 813 | ~310 (≈150 without the Q2 ruling) |
| T | 2,241 | ~630 |
| B | 2,732 | ~700 |
| I | 2,415 | ~450 |
| R | 2,365 | ~870 |
| X | 1,553 | ~560 |
| 7 slot cards | 2,536 | ~220 |
| WGT | 1,312 | ~150 (−195, +45 if it takes the deleted-test list) |
| DC | 847 | ~30 (−70 seat rule, +40 § Filling a card) |
| PQ / shared ref | 1,017 | **+~1,050** |
| **Net in my files** | 19,601 | **~3,500** (range 3,000–4,000) |

In other readers' files, from my searches: SDD (~400: :87, :95-104, :126, :155), RT (~200: :38, :93, :117), RCR:26, very-small-lane.md:13 and writing-plans:20/:52. Those are their calls.

Moves to `docs/`: about 85 words of new record text (the claim-discipline rationale to `evidence-and-findings.md`; the terminal pass's timing-free rationale to `terminal-pass.md`). Everything else on the wrong level is already held by a record and is deleted.

## 7. Questions

- **Q1.** Should the Selected-passages paragraph stay in each template (my recommendation, since it governs reading the template), or should `tools/instrument_agents.py` render it from one source?
- **Q2.** May the blind verifier read the shared ref (a new plugin-root slot and a new input against RT:36)? Its sections carry no review content, but it is still an input change.
- **Q3.** Rulings are needed on D2 (the build-history exemption), D5 (terminal-pass location) and D6 (literal-reading label for redteam seats).
- **Q4.** Owner of the deleted-test justification list: WGT (all four seats read it, and the list cites its Warning Signs) or the shared ref?
- **Q5.** Moving conduct rules out of the generated agent body (the system prompt on Claude Code) into a file read at runtime depends on the seat doing the read. PQ works this way today, but I know of no measurement of the skip rate.
- **Q6.** PQ:38 says "two findings a reviewer raises", but R and X do not read that section. Is it scoped to S, T and B by design? Inventory row SDD34 suggests yes; the text does not say.
- **Q7.** Which card form becomes standard for the Model and Effort lines and for placeholder syntax (G7)?
