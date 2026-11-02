# Placement audit: upstream-derived skills

> Advisory input to `design.md`, read at `8332a00`. Where the spec decides otherwise (its Decisions and its corrections list), the spec governs; the questions below were answered in its brainstorm.

Reader: upstream-derived. Tree: the repository, HEAD `8332a00`, clean
before and after (checked with `git status --short`). Files: `skills/systematic-debugging/`
(`SKILL.md` 1,491 words, `root-cause-tracing.md` 911, `defense-in-depth.md` 494,
`condition-based-waiting.md` 526), `skills/dispatching-parallel-agents/SKILL.md` 920,
`skills/using-git-worktrees/SKILL.md` 1,713, `skills/writing-skills/SKILL.md` 1,546.
Word counts are `wc -w` over the cited line ranges; savings are estimates.

## 0. A premise to settle before any of this is used

**Two of the four skills are upstream's text by a standing decision.**
`docs/decisions/upstream-skills-kept-close.md:5-12` says systematic-debugging and
dispatching-parallel-agents "keep superpowers' text ... and change it only where" a
listed reason applies (host mechanics, a folded skill, a secret, a platform limit, a
defect, a check from a folded skill). Its Why (`:67-75`): "each line crucible changes
in upstream's text is a difference to carry past later upstream releases". The record
lists the exact lines changed (`:14-41`).

The umbrella's `placement` child (`docs/crucible/2026-11-01-skill-text-rewrite/umbrella.md:306`,
"upstream-derived supporting files brought to crucible's grain") and the backlog
(`docs/backlog/skill-text-rewrite.md:28-32`) plan to rewrite those same files, and
neither mentions the record (searched the umbrella folder for "kept close" and
"upstream's text": no hit in `umbrella.md`). Bringing them to crucible's grain changes
no *process* rule, but it reverses a recorded *decision*. The child says "No rule
changes". So this part needs the operator's ruling and an edit to
`upstream-skills-kept-close.md` (Decision plus a `## Changes` line). It would also
change how `docs/upstream.md` § Upkeep works for these files: each upstream release
is reviewed as a diff, and that diff would no longer apply to rewritten text.

Everything below for systematic-debugging and dispatching-parallel-agents depends on
that ruling. using-git-worktrees (crucible's rewrite, `docs/decisions/worktrees.md`,
`docs/decisions/git-steps.md`) and writing-skills (shrunk by crucible,
`docs/decisions/authoring-crucible.md` § writing-skills) are not covered by the
kept-close record. One exception in writing-skills is in § 3 below.

## 1. Restated rules (cross-skill)

1. **Single-invocation rule for Git steps.**
   Sites: `skills/using-git-worktrees/SKILL.md:16-19` (49 w), the same skill's
   rationalization row `:191` (~35 w), `skills/finishing-a-development-branch/SKILL.md:14-17`
   (~45 w, almost the same words).
   Owner: each skill for its own commands. The two skills load separately, and the
   reader acts in each one. Keep both statements; cut the worktree table row `:191`.
   The rationale is already in `docs/decisions/git-steps.md` § Single invocations.
   Saved: ~35.
2. **Fan-out only for independent tasks, otherwise one at a time.**
   Sites: `skills/dispatching-parallel-agents/SKILL.md:77` (~20 of 33 w; the
   independence criteria are also at `:36-45`), `skills/using-crucible/references/claude-code.md:25-28`
   (~40 w), `skills/using-crucible/references/codex.md:29-32` (~38 w),
   `skills/redteaming/SKILL.md:69` (~25 w, the "start every seat ... before waiting"
   clause, which already points to dispatching-parallel-agents).
   Owner: dispatching-parallel-agents, where the fan-out is decided. The adapters
   would keep only the host mechanic ("this host can run several concurrently" /
   "spawn each, then `wait_agent`"). Redteaming's clause is the controller's own act
   for its seats and stays. Saved: ~45 in the adapters; that is the adapter reader's
   call. The backlog lists "fan-out independence" among host-neutral rules in the
   adapters (`docs/backlog/skill-text-rewrite.md:33-34`).
3. **Native worktree tool first, Git invocations otherwise.**
   Sites: `skills/using-git-worktrees/SKILL.md:10,63-69` (owner),
   `skills/using-crucible/references/claude-code.md:33-35` (~25 w).
   The adapter line is partly a host fact (this host exposes one) and partly
   restatement. Cut it to the host fact plus a pointer. Saved: ~10.
4. **The worktree for a feature started inside another feature's worktree.**
   Sites: `skills/brainstorming/SKILL.md:88` (~70 w: "create this feature's own
   whatever Step 0 concludes, with Step 1b, from the repo's base branch or a base the
   operator names, in the main checkout's worktree directory"), and
   `skills/using-git-worktrees/SKILL.md:10,69,73,77,119`.
   Owner: using-git-worktrees for where and from what base; brainstorming for when.
   brainstorming:88 keeps "create this feature's own with Step 1b" and points to it.
   Saved: ~25 (brainstorming reader's file).
5. **Consent to create a worktree is the approved design message.**
   Sites: `skills/using-git-worktrees/SKILL.md:57` (~75 w), `:65` ("The user has asked
   for an isolated workspace (Step 0 consent)", ~10 w), `skills/brainstorming/SKILL.md:42`
   (last sentence, ~30 w).
   Owner: using-git-worktrees `:57`. Brainstorming states its own act (naming the
   worktree in the message), and that stays. Cut the clause at `:65`. Saved: ~10.
6. **Evidence before claims.**
   Sites: `skills/using-crucible/SKILL.md:24` (owner, always loaded, ~25 w),
   `skills/systematic-debugging/SKILL.md:189` (~25 w), the implementer prompt's
   evidence paragraph (`skills/subagent-driven-development/implementer-prompt.md`,
   § Tests, seat-specific).
   The copies are consistent. The SD line is one of the four lines the kept-close
   record names, so leave it. Saved: 0.
7. **Root cause before any fix.**
   Sites: systematic-debugging (owner), `skills/subagent-driven-development/implementer-prompt.md:186-190,227-229`.
   These are pointers with one clause and are correctly placed. No action.

## 2. Drifted copies

1. **Test-first exception (systematic-debugging).** Unconditional copies:
   `skills/systematic-debugging/SKILL.md:176` "MUST have before fixing", `:251`
   "Untested fixes don't stick. Test first proves it.", and the red flag at `:220`
   "Skip the test, I'll manually verify". The conditional copy at `:177`: "Write the
   failing test before the fix; where no test or script can reproduce the bug, say
   why."
   Intended: `:177`, as recorded (`docs/decisions/upstream-skills-kept-close.md:90-97`,
   Changes 2026-10-15). Deleting `:176`'s bullet resolves it. That edit is another
   change to upstream's text, so it falls under § 0.
2. **Step 0 forbids what Step 1b requires (using-git-worktrees).**
   `skills/using-git-worktrees/SKILL.md:49` reads "You are already in a linked
   worktree. Skip to Step 2 (Project Setup). Do NOT create another worktree."
   Quick Reference row `:166` matches it. But the overview at `:10` and Steps 1a/1b at
   `:69,73` send "brainstorming starts a feature inside another feature's worktree" to
   the fallback, and `skills/brainstorming/SKILL.md:88` says "create this feature's
   own whatever Step 0 concludes".
   Intended: create one (`docs/decisions/worktrees.md:17-25`). Step 0 is missing that
   case. A reader who follows the worktree skill alone stops at `:49`.
3. **Directory priority in the Quick Reference.** Rows `:170-173` use an existing
   `.worktrees/` or `worktrees/` as-is and consult the instruction file only when
   "Neither exists". The body checks the instruction file first (`:79` "Explicit user
   preference always beats observed filesystem state", `:81`; row `:190`).
   Intended: the body.
4. **Ignore-check failure in the Quick Reference.** Row `:175` says "add it to
   .gitignore + commit, re-check". It drops the case at `:99`: "From another feature's
   worktree, commit nothing: report the result to the operator" (also
   `docs/decisions/worktrees.md:23-25`). Intended: the body.
5. **Setup skip in the Quick Reference.** Row `:179` reads "No package.json/Cargo.toml
   → Skip dependency install". The body's table at `:136-144` has five markers
   (requirements.txt, pyproject.toml and go.mod as well). Intended: the body.

Example, not a rule (listed for the rewrite; not counted): the empty-projectDir
incident's two tellings disagree. `skills/systematic-debugging/root-cause-tracing.md:142-144`
reads "Layer 1: Project.create() validates directory", "Layer 3: NODE_ENV guard". The
other telling, `skills/systematic-debugging/defense-in-depth.md:107-109`, reads
"validates not empty/exists/writable", "Layer 3: `WorktreeManager` refuses". Its Layer
1 code (`:26-37`) checks existence and is-a-directory, not writability. The call
chains also differ: WorktreeManager/Session (`root-cause-tracing.md:54-57`) against
Project/WorkspaceManager (`defense-in-depth.md:101-104`). Telling the incident once
removes the disagreement.

## 3. Wrong-level text

| Site | Words | What it is | Where it goes | Saved in skills |
|---|---|---|---|---|
| `skills/systematic-debugging/root-cause-tracing.md:183-189` | 32 | "Real-World Impact", a dated session's measurements (2025-10-03, 1847 tests) | Delete. It is upstream's text, still at upstream; no crucible record holds it (§ 0) | 32 |
| `skills/systematic-debugging/condition-based-waiting.md:113-119` | 31 | Same kind (pass rate 60%→100%, 40% faster) | Delete (§ 0) | 31 |
| `skills/systematic-debugging/defense-in-depth.md:96-112` | 79 | "Example from Session", the incident retold | One clause plus a pointer to root-cause-tracing's example (§ 4) | ~65 |
| `skills/dispatching-parallel-agents/SKILL.md:136-159` | 109 | "Real Example from Session", a narrative of one run | Delete. The example prompt `:94-113` already carries the case (§ 0) | ~100 |
| `skills/using-git-worktrees/SKILL.md:44-47` | 44 | Git internals: why the submodule probe is needed | `docs/decisions/worktrees.md` § The fallback's checks. No record holds it (grep "submodule" over `docs/decisions/`: no hit) | ~40 |
| `skills/using-git-worktrees/SKILL.md:101-113` | 113 | Why the wrong directory or a missing slash defeats the check, down to how Git matches `.gitignore` | Already in `docs/decisions/worktrees.md:105-115`. Keep one line: "Check the directory you selected, with its trailing slash: without it Git reports an ignored directory as not ignored." | ~85 |
| `skills/writing-skills/SKILL.md:37-41` | ~45 | Upstream's incident (a description saying "code review between tasks" got one review where the flowchart required two) | Already in `docs/decisions/authoring-crucible.md:178-182`. Keep one clause: "an agent may follow a summary in place of the body" | ~35 |
| `skills/writing-skills/SKILL.md:62-69`, `:72-75` (part) | ~100 | Measurements from upstream's wording tests ("fully separated distributions", "consistent to noisy") | `docs/decisions/authoring-crucible.md` § writing-skills. That record's Decision (`:73-75`) says the skill *keeps* "their measurements attributed to upstream's wording tests", so moving them needs a ruling (§ 7) | ~70 if ruled |
| `skills/systematic-debugging/condition-based-waiting.md:84-86` (last clause) | ~10 | "so it carries no platform requirement": a maintainer's reason (the record holds it, `upstream-skills-kept-close.md:104-109`) | Keep "It is not a runnable script"; drop the reason | ~8 |
| `skills/systematic-debugging/root-cause-tracing.md:123-124` | ~10 | "nothing in this workflow waits on it": maintainer rationale, held at `docs/upstream.md` (find-polluter row) and `upstream-skills-kept-close.md:104-109` | Delete | ~10 |

I found no seat-routing or host-neutral adapter text in my files. The adapter
restatements are in § 1 items 2 and 3.

## 4. Grain (within each file), and what crucible's grain makes of each

### `skills/systematic-debugging/SKILL.md` (1,491 → ~1,220; all subject to § 0)
- **Root-cause-first said four times:** `:10` core principle, the Iron Law
  `:16-20`, `:50` "BEFORE attempting ANY fix", `:170`. Keep the Iron Law and its
  one-line consequence. ~15.
- **"Don't skip when" `:39-42` (~30 w) repeats rationalization rows `:248-249`**
  (simple issue, emergency). Keep the table. ~30.
- **Phase 1 step 5 "Quick version" `:114-118`** summarises root-cause-tracing.md right
  after pointing to it. Keep the pointer and "fix at source, not at symptom". ~25.
- **One change at a time said four times:** `:152-155`, `:181-183`, red flag `:219`,
  row `:252`. Keep Phase 3 step 2 and the table row. ~15.
- **Three-fix breaker said five times:** step 4 `:191-196`, step 5 `:198-212`, red
  flags `:226-227` and `:231`, row `:255`. Merge steps 4 and 5 into one (the
  condition, the pattern signs, ask your human partner). Drop `:226-227` and `:231`.
  ~60.
- **Red flags against the rationalization table:** six red flags restate rows
  (`:217`/`:250`, `:219`/`:252`, `:220`/`:251`, `:221`/`:254`, `:223`/`:253`,
  `:226`/`:255`). Keep the table. Keep the flags that have no row: `:218`, `:222`,
  `:224`, `:225`. ~40.
- **Quick Reference `:257-264` (71 w)** restates the four phases' headings. Delete. ~70.
- **Drift fix `:176`** (§ 2.1). ~4.
- Crucible's grain: Iron Law; When to Use as one list; the four phases with their
  steps (the Phase 1 example kept, since it is the file's one example); one breaker
  step; the "your human partner" signals (the record keeps them,
  `upstream-skills-kept-close.md:111-115`); one rationalization table; "No Root Cause"
  (its heading is cited at `root-cause-tracing.md:31`); the supporting-file index
  `:277-283`, which writing-skills § Structure requires.

### `skills/systematic-debugging/root-cause-tracing.md` (911 → ~620)
- **The empty-projectDir incident told three times in this file:** the Tracing
  Process `:39-71` (118 w), the Real Example `:126-145` (103 w), Real-World Impact
  `:183-189`. defense-in-depth.md `:96-112` tells it a fourth time. Keep the Tracing
  Process. Fold in the Real Example's root cause and fix (`:137-139`, ~25 w) and point
  to defense-in-depth for the layers. ~75, plus the § 3 row.
- **The dead-end loop drawn twice and said once more:** digraph `:11-27` (96 w),
  digraph `:149-172` (142 w), prose `:29-31`. Keep the second digraph (it has the
  whole loop and the fix-at-source end), with the prose sentence under it, and turn
  "Use when" `:33-37` into its lead. ~100.
- **Instrumentation said twice:** Adding Stack Traces `:73-102` and Stack Trace Tips
  `:176-181`. `console.error` appears at `:92` and `:178`; `new Error().stack` appears
  in the code and at `:181`. Fold the one new tip ("log before the dangerous
  operation") into `:75`. ~30.
- **`:174`** "NEVER fix just where the error appears" restates `:7`. ~12.
- **Windows note `:119-124` (74 w)** says POSIX-only twice ("POSIX/Bash-only.
  Consequence on Windows: the script is a Bash program ... does not run natively
  there"). Cut to: "Bash-only: run it from WSL or Git Bash, or bisect by hand, running
  the candidate test files one at a time and checking after each whether the polluter
  appeared." ~35.

### `skills/systematic-debugging/defense-in-depth.md` (494 → ~330)
- **Validate-at-every-layer said four times:** `:7`, `:11-12`, `:122`, plus Key
  Insight `:116`. Keep `:7`. ~20.
- **The four layers listed five times:** `:15-18`, the four headings `:20-85`, `:93`,
  `:107-110`, `:117-120`. Keep the headings with their purpose lines. Drop "Why
  Multiple Layers" `:9-18`, except one clause ("each catches what the others miss:
  other code paths, mocks, platform edge cases"), which replaces Key Insight
  `:114-122`. ~75.
- **Layer 4 code `:75-84`** repeats root-cause-tracing's instrumentation `:78-90`.
  Point to it. ~25.
- **Example `:96-112`** (§ 3).

### `skills/systematic-debugging/condition-based-waiting.md` (526 → ~420)
- **The decision shown twice:** the digraph `:11-22` (48 w) and Use/Don't use
  `:24-32`. The digraph draws a single yes/no, which writing-skills § Structure would
  not draw. Delete it. ~45.
- **"Document WHY" said three times:** `:15`, `:32`, `:105`/`:111`. Keep the
  requirements list `:108-111`. ~10.
- **`:82-86`:** merge the pointer and the copy-it note into one sentence. ~15, plus
  the § 3 rows.

### `skills/dispatching-parallel-agents/SKILL.md` (920 → ~540; subject to § 0)
- **One example told four times:** domains `:51-56`, dispatch block `:70-75`, the
  example prompt `:94-113`, and the Real Example `:136-159`, whose dispatch block
  `:148-152` repeats `:70-75` nearly word for word. Keep `:51-56`, `:70-75` and
  `:94-113`. Delete `:136-159` (§ 3).
- **Use/Don't use said twice:** `:36-45` and "When NOT to Use" `:129-134` (43 w). Only
  "Exploratory debugging" `:133` is new. Move it into `:42-45` and delete the section.
  ~35.
- **Digraph `:18-34` (85 w)** draws two yes/no questions already listed in `:36-45`.
  Delete it (writing-skills § Structure). ~85.
- **Prompt contents said three times:** "Each agent gets" `:60-64`, "Good agent prompts
  are" `:89-92`, and Common Mistakes `:115-127` (80 w), whose four ❌/✅ pairs are the
  same four bullets. Keep `:60-64` and add "paste the error messages and test names"
  from `:121`. ~100.
- **The review steps said twice:** step 4 `:79-85` and Verification `:161-167`. Merge,
  keeping "spot check: agents make systematic errors" from `:167`. ~40.
- **Overview `:12`** restates the When to Use triggers. ~15.

### `skills/using-git-worktrees/SKILL.md` (1,713 → ~1,190)
- **The fallback's three conditions listed three times:** `:10`, `:69`, `:73`; rows
  `:168`, `:186` refer back to them. State them once, at `:69` with its clause of why,
  and make `:73` "Only where Step 1a sends you here". In the overview, keep "prefer
  native tools; fall back to Git (Step 1b)". ~70.
- **"Phantom state" said twice:** `:67` and `:186`. ~15.
- **Selected directory and trailing slash said four times:** `:87-89`, `:101-113`,
  row `:174`, rows `:188-189`. Keep `:87` ("whatever you selected is `<worktree-dir>`")
  and one line at the check (§ 3). ~40, beyond § 3.
- **Directory priority said three times:** `:79` lead, list `:81-85`, rows
  `:170-173`, `:190`. Keep the list. Dropping the Quick Reference covers the rest.
- **"Prevents committing the worktree" said three times:** `:107-108`, `:115`, row
  `:187`. Keep `:115`. ~10.
- **Quick Reference `:162-179` (187 w)** restates the body, and three of its rows
  drifted (§ 2.3-2.5). Delete it. ~185.
- **Rationalization table `:181-192` (263 w):** each row restates a body rule with its
  reason. Keep the rows with an evidenced failure behind them: `:185` (skipping
  detection), `:186` (bypassing the native tool; upstream's tests;
  `docs/decisions/worktrees.md:27-31` keeps `EnterWorktree` there), `:187`, `:192`.
  Drop `:188-191`, whose content stays in the body. ~110.
- **Submodule internals `:44-47`** (§ 3).
- **Drift fix `:49`** (§ 2.2): adds about 15 words.
- Interfaces to keep: the step numbers "Steps 0–1" and "Steps 2–3" (cited at
  `skills/brainstorming/SKILL.md:88` and `skills/subagent-driven-development/SKILL.md:28`),
  and the headings `§ Step 0: Detect Existing Isolation` and `§ 1b. Git Worktree
  Fallback` (cited at `docs/decisions/worktrees.md:15,40`).

### `skills/writing-skills/SKILL.md` (1,546 → ~1,430)
Most of this file is already at crucible's grain. Remaining:
- **"Prohibitions backfire on shaping problems" said three times:** table row `:58`,
  `:62-69`, and the toolkit's lead `:143-144`. Keep the table. The toolkit's lead
  becomes "For an agent that knows a rule and breaks it (the table's first row)". ~15.
- The measurement paragraphs (§ 3) are the larger lever, if ruled.
- `:29-30` (~15 w) describes crucible's own tree to its authors; `AGENTS.md` already
  says it. It is minor, and it is where an author editing crucible acts, so I'd leave it.
- Heading `§ Descriptions and names` is cited at `docs/decisions/authoring-crucible.md:64`. Keep it.

## 5. Shared seat reference

Skipped (templates reader only).

## 6. Totals

| File | Now | Est. saved | Gated by § 0 / § 7 |
|---|---|---|---|
| `skills/systematic-debugging/SKILL.md` | 1,491 | ~270 | § 0 |
| `skills/systematic-debugging/root-cause-tracing.md` | 911 | ~290 | § 0 |
| `skills/systematic-debugging/defense-in-depth.md` | 494 | ~165 | § 0 |
| `skills/systematic-debugging/condition-based-waiting.md` | 526 | ~110 | § 0 |
| `skills/dispatching-parallel-agents/SKILL.md` | 920 | ~375 | § 0 |
| `skills/using-git-worktrees/SKILL.md` | 1,713 | ~510 (net of +15 for § 2.2) | no |
| `skills/writing-skills/SKILL.md` | 1,546 | ~50, or ~120 with the ruling | ~70 by § 7 Q2 |
| Other skills' copies (§ 1: adapters ~55, brainstorming ~25) | — | ~80 | other readers' files |

**Total in my files: about 1,770 words** (≈1,210 of it gated by the kept-close
ruling, ≈70 by the writing-skills ruling, ≈490 free to take now). Add ~80 in other
readers' files.

Moves to `docs/`: the submodule-probe reason (~40 w) to `docs/decisions/worktrees.md`.
If ruled, the upstream wording-test measurements (~70 w) go to
`docs/decisions/authoring-crucible.md` § writing-skills. Everything else is deletion of
text a record already holds or of upstream's own history. If § 0 is ruled a reversal,
`docs/decisions/upstream-skills-kept-close.md` needs its Decision rewritten and a
Changes line, and `docs/upstream.md` § Upkeep should say these two skills no longer
track upstream's text line by line.

## 7. Questions

1. **Kept-close (§ 0).** Does the operator reverse
   `docs/decisions/upstream-skills-kept-close.md` for systematic-debugging and
   dispatching-parallel-agents? Without that, the umbrella's "upstream-derived files
   brought to crucible's grain" contradicts a standing decision, and "No rule
   changes" doesn't cover it. A middle option: trim only the tellings of history
   (Real-World Impact ×2, the Real Example in DPA) and the drift fix, and leave
   upstream's structure. That is about 270 words.
2. **writing-skills' measurements.** `docs/decisions/authoring-crucible.md:73-75`
   decides that the skill keeps upstream's wording-test measurements. The placement
   rule sends measurements to records. Which wins? An argument for keeping one clause:
   the measurement is what makes a counter-intuitive rule credible to the agent
   ("State the reason", `skills/writing-skills/SKILL.md:146-147`).
3. **Rationalization rows.** writing-skills says a table's rows are "every excuse from
   the baseline, verbatim" (`:150-151`). I can't tell which of using-git-worktrees'
   rows `:188-191` came from an observed run and which were written to restate a rule.
   Dropping them is my judgment.
4. **§ 2.2 is a fix with words attached.** Adding the brainstorming case to Step 0
   `:49` adds text. It is the one place this audit suggests growing a file. The other
   choice is to rely on brainstorming:88's "whatever Step 0 concludes" and say nothing
   in the worktree skill. I'd add it, because the skill is invoked on its own too.
