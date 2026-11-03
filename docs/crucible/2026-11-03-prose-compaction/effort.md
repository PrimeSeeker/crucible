# Prose compaction (2026-11-03)

The operator asked for crucible's skill prose to be cut as far as reasonably achievable, the target being tokens (words a proxy), restructuring in scope, minor losses acceptable where the cut justifies them, no significant loss of function. A bespoke process ran instead of a crucible route, on the operator's word; a separate aim was to learn what contains prose creep. writing-skills' guidance was left untouched.

## Results

Measured with Anthropic's token-counting endpoint (no inference) on the head of the branch against master `0deefcf`; the route manifest is `resident-tokens.json` here, the compaction-fit manifest with the new references added.

| Route (controller, every run) | before | after |
|---|---|---|
| standard | 70,761 | 50,781 (−28%) |
| folded | 72,131 | 50,131 (−31%) |
| very-small | 50,295 | 32,248 (−36%) |
| umbrella campaign | 52,168 | 36,906 (−29%) |

Loaded only when their condition arises, the standard route's conditional files fell from 10,397 to 6,952 tokens. Across the corpus, hand-edited skill text fell from 127,236 to 94,539 tokens (−26%) and 57,177 to 43,079 words (−25%); the rendered seat templates, what each dispatched seat reads, from 36,413 to 26,742 tokens (−27%). Joining hard wraps (one paragraph per line) is part of the token figure: it saves 4–5% of a file's tokens, 12–13% where the Read tool numbers lines.

## Process

The whole effort spent over 70M subagent tokens, most of them cached reads; the per-file rewrite took 44M of them for 52 files, its re-verification 9M.

1. **Mining.** Nine fresh agents, each with one framing (duplicates, retirements twice, architecture, density, seat reads, a route walk, creep history, the constraints tests and tools put on the text), plus one Codex seat, proposed cuts. A clustering agent merged them into 49 clusters with saving, loss and risk each; the controller ruled on every cluster. Rejected: deliberate recent keeps, blindness controls, and behaviour changes with little token payoff.
2. **Structural steps.** Moves and splits (new references `review-terms.md`, `round-record.md`, `premise-asks.md`, `umbrella-children.md`, `git-fallback.md`; Codex seats reading their template by path) ran as a chain, each step an implementer, a reviewer and a fixer, the suite green between steps.
3. **Per-file rewrite** (`pipeline/compact.js`), one unit per file, each with a brief carrying the rulings that touch it:
   - a rule inventory (every obligation, condition, format, ordering, pointer, rationale and example as an atomic item, rated core, edge or support) and, for files over 400 words, a completeness critic;
   - two or three writers with different framings: A, a line editor; B, a re-deriver writing from the inventory without reading the original; C, a restructurer on another model (files of 1,200 words or more);
   - a blind check of each variant against the inventory;
   - a judge-synthesizer picking a base and grafting the best sections of the others, restoring what the checks found lost or listing it as an accepted loss;
   - blind verification with up to two repairs, then behavioural QA (scenario questions from the original, answered blind under the rewrite, graded);
   - `pipeline/check_variant.py` after every write: the body cap, frontmatter, cited headings, stub sentences, splice markers and the text tests read.
4. **Re-verification** (`pipeline/reverify.js`): a blind check of core and edge items after the last repair, the QA partials as problems, one repair, a blind re-check and the QA questions asked again.
5. **Integration** per skill family, the generator, prose budget and suite run after each; then one mechanical reflow (one paragraph or list item per line).
6. **Review**: six loss lenses (one per skill family), cross-file consistency, records, three route walkthroughs, one Codex seat; each BLOCKER or MAJOR finding verified adversarially.

The review found no BLOCKER or MAJOR. Codex reported nothing beyond the accepted losses. The Claude lenses raised twelve MINOR findings, fixed in one commit: among them a rule two per-file units each dropped because each relied on the other file keeping it (the terminal pass's and blind verifier's search bound), and one retirement whose premise did not hold (round 1's cross-host swap rule, which an operator-instructed seat on another host needs), reverted. A second round over the records and cross-file consistency, every finding verified, confirmed six more MINOR findings, mostly records citing where a rule lived before the moves; fixed.

## What worked, and what did not

- **No single framing won; the synthesis did.** Over 52 files the synthesizer took A as its base 33 times and B 19 times, C never (17 files). Mean variant length against the original: A 0.83, B 0.80, C 0.84; mean blind misses A 1.6, B 2.5, C 1.9. The finals came to 0.79, below every single framing. In an earlier batch of eight files, mostly the two upstream-derived skills (tutorial text, anecdotes), B was the base six times and the batch fell 40%: re-derivation suits accreted text, line editing dense rule text.
- **The verification layers catch different things.** Inventory checks catch dropped conditions; QA caught meaning shifts the inventory check passed (a mandate reminder "naming" the binding output instead of being it); the suite caught what both missed (a template left uncited, a bare file name that the sibling-file test rejects). A blind checker's "added" list is never empty, so a loop keyed on it always repairs; verification has to follow the last repair.
- **QA is noisy.** Most partial grades after repair were the answerer missing text that was present, or rules retired on purpose. Grade only against core and edge items, and read the partials by hand.
- **Per-file units can each drop a rule on the strength of the other.** One unit cut a shared sentence because a template kept the rule; the template's unit cut its own copy because the shared sentence kept it. Only a whole-branch read caught it. A per-file pass needs a ledger of "stated elsewhere" drops, checked at integration.
- **Review adds words even on a cutting branch.** Every structural step's review raised findings, and every fix that changed skill text added words; no reviewer proposed a cut.

## Creep: what grows the text, and what could contain it

Growth, from git history: hand-edited skill words went 38k → 71.3k → 47.7k → 57.2k in three months, each rewrite regrown within two to three weeks; since 0.2.0 the prose budget saw 67 raises and 27 lowers, none refused. The mechanisms, in order of weight:

1. new mechanisms, each needing a clause at every hand-off of every route;
2. review pushing one way: an omission is a finding, an excess is not;
3. restatement for a second reader, every reader getting its own copy;
4. recovery checks layered on rules;
5. mechanisms outliving their evidence;
6. a budget that counts words per directory at commit time, not tokens per load, after the campaign has already grown the spec.

Containment ideas, by expected effect over cost (none adopted here):

- **Bill reader cost in the suite**: a standing test of each route's every-run tokens (offline, about 2.96 characters per token) against an operator-owned cap; raising it takes an operator ruling.
- **Replace before adding**: a fix first revises the rule that owns the case; a new paragraph only where that rule cannot carry it.
- **Section takers checked by the generator**: each shared section declares its takers.
- **A compaction trigger**: when a route's every-run load passes this effort's baseline by 10%, the next feature is a compaction.
- **A token allowance in a skill-changing spec**, net zero by default, graded by its seats.
- **Re-derive rather than line-edit**: a periodic rewrite of a file from its rule inventory sheds accreted phrasing a line edit keeps.

## Accepted losses

Each file's losses were accepted as minor by its synthesizer or repairer, against the brief's rulings; none was rated significant. By class:

- **Retired by ruling:** seat ids no longer described as never reused (a replacement takes a fresh id); the overturn Trace's seat-id bullet; plan-phase's dispatch arithmetic; the controller's own re-run of the pre-pass arithmetic after a wave or a repair, so a wave breaking ownership or overlap arithmetic surfaces as a task review's scope finding instead; deferral rules kept in one home; the worktree setup table, so the agent picks the dependency command; rationalization-table rows restating a body rule with no recorded catch (destructive-action guards and evidence-backed rows kept; the router's table kept whole); duplicates and anecdotes in the two upstream-derived skills.
- **Per file:** rationale clauses, restatements now stated once with a pointer, and pointers a reader recovers nearby; request.md's "evidence of what was asked, not the standard"; the finishing skill's detached-HEAD menu described rather than spelled out.

## Files

`pipeline/` holds the scripts as run (workflow scripts take the repository root as `args.root`; the Python tools expect to sit in `<root>/.crucible/prose-compaction/tools/`); `style.md` the cut patterns and what not to cut; `brief-common.md` and `briefs-task.md` the writers' and brief-writers' shared briefs; `resident-tokens.json` the per-route manifest of this measurement and `resident-tokens.md` its figures, per phase and per file.
