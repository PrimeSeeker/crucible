# Authoring crucible

## Decision

**Where text goes.** `crucible:writing-skills § Reader cost` holds the
general rules: state each rule once, where its reader acts on it, and
point to it from elsewhere, stating one sentence itself where its reader
would not otherwise load the target; give the action, its observable
signal and at most one clause of why, how the rule was learned going to
the project's decision records; write siblings at one grain, detail
moving to a supporting file or a tool's `--help`. Its § Structure keeps
a `SKILL.md` that a host cuts after compaction under the cut, long step
bodies going to supporting files. `AGENTS.md` ("Where text goes")
names crucible's homes: how a rule was learned (incidents, measurements,
accepted trade-offs) in the decision records, `docs/decisions/`; host
mechanics in the adapter pair; text about crucible's own text in `docs/`;
what a seat does and produces in its template, and the rules seats share
in the shared seat reference,
`skills/subagent-driven-development/references/seat-rules.md`, or, for the sections controllers also read, in `skills/subagent-driven-development/references/review-terms.md`, each
template taking by splice the sections its seat follows
(`docs/decisions/instruments.md`).
`skills/redteaming/references/formats.md` and, for the round directories and the round record, `skills/redteaming/references/round-record.md` hold the shapes of what
controllers and seats write and point at the skills for process rules;
`docs/authoring.md` holds the rules for crucible's authors (anchor
stability, the reference convention, the paired texts).

**Where each shared rule lives.** A controller skill keeps the steps its
controller takes and the inputs it fills; a seat's rubric and verdicts
live in its template and a card's inputs on its card. The rules every
dispatching controller shares (reading the card rather than the
template, confirming the report file, the shared-tree rules, effort only
on request) live in
`skills/subagent-driven-development/references/dispatch-composition.md`,
and each skill that dispatches carries one line sending its controller
there and to its host's dispatch reference when the skill starts and
after compaction. Rules every session needs, ad hoc dispatches included
(never predicting an agent's result, naming the model, the form of a
decision ask), live in the router. A rule stated more than once has one
owner text and pointers; three rules are stated on purpose for both
controllers and seats, and `docs/authoring.md` § Paired texts lists
them. Skills stay hand-written: only the seat templates are rendered.

**A `SKILL.md` stays under the compaction line; route procedures and
long step bodies live in references.** Every `SKILL.md` body, the text
after its frontmatter, stays at or under 18,000 characters, held by
`tests/test_skill_size.py`: after compaction Claude Code re-attaches an
invoked skill cut at about 20,000 characters, and a cut copy loses the
steps past the cut (§ Why). A procedure that applies only on some routes
sits in a reference read on demand: redteaming's `plan-phase.md` and
`folded-lane.md`, SDD's `very-small-lane.md`, brainstorming's
`folded-lane-document.md` and `lane-note.md`, and
`skills/redteaming/references/flip-paths.md`, which redteaming and SDD
share. So does a long step body where the line needs it, as in SDD,
redteaming and brainstorming. The skill keeps its spine: the overview
and the steps in order, each with its trigger; the resume and
rehydration rules; the loop bounds; the flow gates; its rationalization
and red-flag tables, where it has them, without rows that only restate
its body (§ Why); and every rule that binds beyond the step whose
section holds it, at every dispatch, resume or fix application. A moved
section keeps its heading with a stub, one paragraph naming the
reference and when to read it in full, so citations of the heading
resolve unchanged and every trigger stays in the re-attached text. What
a stub means is stated once near the top of each skill that has stubs:
"A reference a section names to read in full binds as if written here. Read it when its step comes, unless read since your last compaction; after compaction, re-read the step in progress's reference first." The flip-paths stubs,
the trigger beside each for `skills/brainstorming/references/umbrella-children.md` § Under an umbrella,
redteaming's premise-findings stub and brainstorming's two umbrella stubs keep their own line sending a controller
back after compaction. `tests/skill_corpus.py` reads a skill together
with the references its stubs name, so a test follows text that moved.

**The prose budget.** `tests/prose-budget.txt` holds each skill
directory's word count of hand-edited text: every `*.md` in it but the
templates `tools/instrument_agents.py` renders from their sources, which
the sources already count. `tests/test_prose_budget.py` fails when a
count is above its number or more than 50 words below it. A commit that
grows a skill raises the number and says in its body what the words buy
or what went in exchange; one that shrinks a skill lowers it. Restored
upstream text counts like any other.

**No build history in shipped text.** The implementer, task-reviewer,
re-reviewer and branch-reviewer templates keep build history out of
everything a change ships, code, comments, docs and prompts: plan task
numbers, spec section numbers, feature decision ids, pointers to a
feature's spec or plan, rulings carrying names or dates, wave names, what
was retired when. It belongs in commit messages, the feature folder, and
the project's decision records or changelog, which exist to hold it. That
rule is unconditional; the rest of the templates' comment policy (the
current invariant or hazard, symbols rather than `file:line`, a pointer
to the owning document) is a default under the project's conventions.

**Terminology.** The human is "the operator", defined once in the router
as the person the agent works with, whom inherited upstream text calls
"your human partner"; that text keeps the phrase. A round is a review
pass and a wave a fix plus its verification, so SDD says "fix wave". The
closing pass is the terminal pass everywhere, qualified by phase, and its
follow-up the second read. A campaign is the spec's multi-round review
only; the plan has its plan phase, and slot cards say `{phase}` and
`{phase-dir}`. The folded lane's document is `folded.md`. There is no
glossary file; the reader's glossary is `README.md` § Glossary.

**Descriptions.** A skill's description gives concrete, discriminating
triggers, may say what the skill is for, and never lists the procedure's
steps (`crucible:writing-skills § Descriptions and names`); the router's
Skill Index lines follow it. Codex's `agents/openai.yaml` short
descriptions are presentation, outside the rule.

**writing-skills.** `skills/writing-skills/` holds `SKILL.md`,
`compacting.md`, `graphviz-conventions.dot` and `agents/openai.yaml`. It covers text agents act on (skills, instruction files, rules, prompts and templates, hook-injected text), organized around reader cost: a text's tokens times its reads, for each reader, measured on the written text. A fix revises the sentence that owns the case and keeps the finding's reasons, its failure scenario and what a pointer defines out of the text; a review counts excess as a finding. `compacting.md`, read only when compacting, holds the inventory, one-writer and blind-check procedure and the cut patterns. It sends an author to
each host's own skill creator for scaffolding and evaluations, says where
each host keeps personal skills and which instruction file it reads, and
links each vendor's authoring guidance rather than copying it. It keeps
upstream's "Match the form to the failure", its micro-test method and its
question for an agent that went another way, their measurements
attributed to upstream's wording tests, named in the skill as
superpowers'. Its evaluation tells the
evaluated agent nothing false; a dilemma scenario is disclosed as an
evaluation; asking, escalating or arguing the skill is wrong are outcomes
to examine, never failures by definition. It sets no word targets. The
implementer template points its seat at it when a task changes text that
instructs agents; the skill's evaluations stay the controller's.

**How records cite.** Records and `docs/upstream.md` cite crucible's
files by plugin-root path and each other by `docs/decisions/<slug>.md`.
They cite a skill heading as `crucible:<skill> § <heading>`, any heading,
as the skills do; `docs/authoring.md` § Anchor stability lists no skill
heading, and the reference scanner is the guard. In them a bare
`README.md § <heading>` means the root `README.md`; in `skills/` and
`hooks/` it means `hooks/README.md`. An upstream path carries the prefix
`superpowers/` (`superpowers/skills/executing-plans/`), and the upstream
name followed by a colon, its namespace form, is never written: the
retired-namespace check bans it. The reference scanner (`tests/test_references.py`) checks records and
the map as it checks the skills: every crucible path resolves and every
citation's text after `§` begins with a heading of the cited file, while
prefixed upstream paths and URLs are skipped.
`docs/authoring.md` § Reference convention states these rules.

**Line endings.** Every text file is LF: `.gitattributes` sets
`* text=auto eol=lf` and keeps its explicit pins for `*.sh` and
`hooks/session-start`.

**One line per paragraph.** Text under `skills/`, which agents read, holds each paragraph and list item on one line, never hard-wrapped; the rendered templates and agents follow their sources.

## Why

### Where text goes

Redteaming, SDD and requesting-code-review grew from 16.3k words on
2026-08-07 to 41.2k on 2026-10-05, and rewrites cut them to 31.4k by
2026-10-13. Per-commit deltas put most of the growth in new mechanisms,
not in wording, and a detail-level audit of all shipped skill prose on
2026-10-16 found about 11% of it at the wrong level or restated,
restatement the largest category. A rule stated twice drifts: the two
copies of the flip-path procedure had. (Basis: measured.) The placement
rules and their homes in crucible were an agent's proposal the
maintainer agreed to on 2026-10-16. (Basis: judgment, accepted by the
maintainer.)

A read-only placement audit of the tree on 2026-11-02, by four
default-role readers, estimated about 8,000 of the skills' 63,732 words
removable by placement and found about 25 rules whose copies differed
in substance, the statement of what binds the largest restatement,
copied into six seat templates and about eight other sites. (Basis:
measured.) The placement that followed gave each such rule one owner
text: the seat-side clauses one shared reference spliced into the
templates (`docs/decisions/instruments.md` § The splice); the rules every
dispatching controller shares `dispatch-composition.md`, since the
redteaming and execution controllers both act on them and neither reads
the other's skill; the host-neutral dispatch rules and the decision
ask's form the router, which every session loads
(`docs/decisions/runtime-adapters.md`). Where copies disagreed, the text
took the evidently intended version; for the four whose intended
version was not evident, an agent proposed one and the maintainer
accepted it. A reference read on demand is not re-attached after
compaction, so only the skill's own line sends a controller back to it.
The three paired
texts stay paired because controllers and seats act on them at
different sites, and a seat reads no controller's file. An agent's
design, which the maintainer accepted. (Basis: judgment, accepted by the
maintainer.)

Skills are not generated as the templates are. A controller loads
several skills into one context and can follow a pointer; splicing a
shared rule into each skill would put it before the controller once per
skill and grow the `SKILL.md` files that have to fit the compaction
line. An agent's recommendation on the maintainer's question, which the
maintainer accepted. (Basis: judgment, accepted by the maintainer.)

`formats.md` was split by reader on 2026-10-09: a controller acts on the
shapes, a script's rules are read when it refuses, and author rules only
by crucible's authors. On 2026-10-13 eight passages in it that restated a
redteaming rule became pointers, each rule still stated in the skill.
(Basis: judgment, accepted by the maintainer.)

On 2026-11-03 its § Round record format and the per-round directory listing moved into `skills/redteaming/references/round-record.md`, which the redteaming controller reads when its skill starts. Brainstorm read the whole of `formats.md` on every route for the workspace and the feature folder, and about half of its 3,124 words were the round record, which only the spec campaign and the plan phase write: the very-small lane and an approval-only umbrella loaded it for nothing, and every later read of `formats.md` (SDD Setup's provisioning, Finish's open items, a plan's folder resolve) carried it. On a route that runs a spec campaign, the load only moves from brainstorm to the campaign's start. The new file's `##` headings are frozen interfaces like those of `formats.md` (`docs/authoring.md` § Anchor stability). An agent's proposal, on which the maintainer left the call to the agent. (Basis: measured, for the words; judgment, accepted by the maintainer.)

The same day the umbrellas reference split by reader. A child's brainstorm loaded all of it, 2,302 words, though a child acts on its § Children, § Edits, § Marks and § Resuming alone, and a child's execution read `skills/redteaming/references/flip-paths.md` for the step that takes in a binding change at each boundary, a 263-word section. Those four sections and flip-paths' § Under an umbrella moved into `skills/brainstorming/references/umbrella-children.md`, which a stub of its own sends a child's controller to: 1,218 words at the split and 1,333 after its § Marks took in, from SDD's finish, the procedure for a feature with no umbrella line; `skills/brainstorming/references/umbrellas.md`, then 1,381 words, keeps what the umbrella's own controller and the landing that completes it act on. The umbrella's own controller reads both, its load rising by the moved flip-paths section. An agent's proposal, on which the maintainer left the call to the agent. (Basis: measured, for the words; judgment, accepted by the maintainer.)

Then flip-paths' § Premise findings moved into `skills/redteaming/references/premise-asks.md`, then 499 words, with a stub of its own in redteaming that takes the premise trigger the flip-paths stub had carried. Seats raise premise findings at every phase, and a controller handling one loaded all of flip-paths, 1,413 words after the umbrella move, for that section; a flip then read 918; the per-file compaction the same day cut all four files further. The citers of the section, in the skills and the records, point at the new file. An agent's proposal, on which the maintainer left the call to the agent. (Basis: measured, for the words; judgment, accepted by the maintainer.)

### References read on demand

Measured on 2026-10-01 over one project's sessions since 2026-08-25, in
input-equivalent tokens: skill prose resident in controllers was about
5% of their spend (41M of 848M), in
subagents 0.2%, and no skill was loaded twice within a compaction epoch,
so the lever is what a session loads. A route's procedure loaded only on
that route pays whenever the route does not run, and the cheapest lanes
took 14 of 26 features from 2026-09-28 to 2026-10-11. (Basis: measured.)
Claude Code re-attaches an invoked skill after compaction, within a
token budget ("Extend Claude with skills", read 2026-10-20), and names no
file read beside it; hence the re-read. (Basis: external.)

The split was kept on 2026-10-12, with no failure from it on record; the
maintainer left the call to an agent ("Your call"). The flip-path
procedure moved to a shared reference on 2026-10-13: its two copies had
drifted, its triggers stay in both skills' always-loaded stubs, so
noticing one is unchanged, and the two sections fell from 681 words to
197. (Basis: judgment, accepted by the maintainer.)

### The compaction line

The host's documentation ("Extend Claude with skills", read 2026-11-03)
says that after compaction the "first 5,000 tokens" of each invoked
skill are kept, within a "combined budget of 25,000 tokens" filled from
the most recently invoked skill. In a maintainer session that day the
re-attached copies of SDD and redteaming, both at 0.13.0, were cut at
exactly 19,902 characters of header line
(`Base directory for this skill: <path>`) and body without frontmatter,
before a 98-character truncation notice, while their sizes in bytes
differed (20,046 and 20,040); by the tokenizer the two cuts held 6,775
and 6,620 tokens. Upstream's issue #2481 (obra/superpowers) records the
same cut publicly, each copy "cut to exactly 20,000 characters" ending
in the notice, whose 98 characters bring 19,902 to 20,000. The
documented 5,000 tokens are therefore an estimate at four characters a
token, and the cut is about 20,000 characters, counted in characters,
neither bytes nor tokenizer tokens. Three bodies were over it then, as
the test counts them: SDD at 37,482 characters, redteaming at 33,182 and
brainstorming at 20,958. A cut copy of SDD ended inside its disputes
section, before drift, inline mode and Finish; one of redteaming inside
its fix application, before its readout, stop rule and exit. Upstream
met the same failure, a session that lost its fix loop's cap running 18
rounds, and moved always-run sections into references read at their
step. (Basis: measured; external, for the documentation and upstream's
issue.)

The test holds each body at or under 18,000 characters. The margin
covers the header line, which carries the install path, and small
edits; the line holds under bytes too, a body's bytes exceeding its
characters by under 1%. At the measured 2.66 to 3.18 bytes a token the
documented 5,000 tokens would be about 14,500 characters; the measured
cut governs, being what the host does, and a host that moved to the
documented figure would cut copies that the router's line on a skill
that came back cut short still catches. The line and its test were an
agent's proposal, which the maintainer accepted; the reasoning on the
unit was added during the spec's review, on the agent's call. (Basis:
measured; judgment, accepted by the maintainer, for the line and its
test; judgment, an agent's call the maintainer has not ruled on, for
the reasoning on the unit.)

Long step bodies move into references, as route procedures did, rather
than into skills of their own: a new skill adds to the always-loaded
skill index, spreads the combined re-attach budget over more skills, and
turns a step into a skill invoked by name mid-flow. The spine stays
because upstream's incident was a lost cap, and because a controller
acts on gates and tables before it knows which reference applies. An
agent's proposal, which the maintainer accepted; the list of what the
spine keeps was reworked during the spec's review, on the agent's
calls. (Basis: judgment, accepted by the maintainer, for the move and
the spine; judgment, an agent's call the maintainer has not ruled on,
for the rework of the spine's list.)

The placement of 2026-11-02 kept the rationalization tables whole, as a form writing-skills endorses, cutting only exact duplicates. On 2026-11-03, under the maintainer's mandate to cut prose as far as reasonably achievable, 18 of the 31 rows in finishing, using-git-worktrees, SDD and requesting-code-review went, each restating a rule its skill's body states, with no recorded catch; destructive-action guards and rows resting on recorded evidence stayed (`docs/decisions/worktrees.md`), and the router's Red Flags stayed whole (`docs/decisions/session-start-hook.md`). The loss is minor: a second phrasing of rules the body keeps, none recorded as changing behaviour. An agent's proposal, on which the maintainer left the call to the agent. (Basis: judgment, accepted by the maintainer.)

Stating once per skill what a stub means keeps each stub to its
reference and trigger; the route stubs had restated it, at 29 to 72
words each. After compaction only the reference of the step in progress
is re-read before acting, the others when their step next comes, rather
than all at once. A reference is read when its step first comes, not
before every round as upstream reads its fix loop: it stays in context
until compaction. The flip-paths stubs, the premise-findings stub, which
took over their premise trigger, the umbrella-children trigger beside each flip-paths stub, which took over their umbrella triggers, and brainstorming's umbrella stubs
keep their own line because a flip, a premise ask or a split or binding-change ask in flight belongs to no step, and an
umbrella's rules span a child's whole brainstorm, which has no
rehydration rule. An agent changed the convention during the spec's
review, on a reviewer's question, from the per-stub re-read the
maintainer had accepted, and put it to the maintainer, who left the call
to the agent ("Your call"). (Basis: judgment, accepted by the
maintainer.)

The convention's own text said nothing of a recurring step until 2026-11-03, so a stub whose trigger recurs, such as merging each round's seat reports, read literally sent a controller back to its reference every round; it now says a reference read since the last compaction is not read again. An agent's proposal, on which the maintainer left the call to the agent. (Basis: judgment, accepted by the maintainer.)

On 2026-11-03 SDD's ledger line forms for leads and `## Questions` moved from its § Setup into `skills/subagent-driven-development/references/setup.md`, read at Setup, though leads and questions are written past that step, at every task and branch-review pass: the texts where they are written restate their forms or lead to that file by citation, so a controller after compaction still finds a form, and the forms no longer ride every re-attach. An agent's proposal, on which the maintainer left the call to the agent. (Basis: judgment, accepted by the maintainer.)

### Resident tokens per route

Resident tokens were counted on 2026-11-03 at `a3db87f`, before the
skill text rewrite, at `d78398c`, before the compaction fit, and at
`4026f6b`, after it. For each route a manifest lists every file a Claude
Code controller loads, by phase, each once, and each file's text went
alone to Anthropic's token-counting endpoint
(`docs/crucible/2026-11-03-compaction-fit/resident-tokens.md`, with the
manifests and the script beside it). Totals, every run, and in brackets
with the files loaded only on an event added (a dispute, drift, inline
work, a flip path, a child of an umbrella):

| Route | `a3db87f` | `d78398c` | `4026f6b` |
|---|---|---|---|
| standard | 79,145 (87,453) | 72,172 (80,383) | 70,761 (81,158) |
| folded | 81,079 (89,387) | 73,542 (81,753) | 72,131 (82,528) |
| very-small | 59,043 (68,511) | 54,708 (63,986) | 50,295 (61,408) |
| umbrella campaign | 53,425 (57,211) | 51,916 (55,521) | 52,168 (55,773) |

Across the rewrite the every-run load fell by 11% on the standard and
folded routes, 15% on the very-small lane and 2% on an umbrella's own
campaign. The compaction fit lowered it by 1,411 tokens on the standard
and folded routes, disputes, drift and inline mode now loading only when
they occur, and by 4,413 on the very-small lane, which no longer loads
the task loop and loads disputes and drift only when they occur; it
raised an umbrella campaign's by 252, and the load with every event's
file by 775 on the standard and folded routes, through the stubs and the headings the
references repeat. The manifests are Claude Code's and say nothing about
Codex, whose host files and tokenizer differ. These figures are the
baseline a later measurement compares with: the skill text rewrite's
re-audit (`docs/backlog/skill-rewrite-reaudit.md`) re-counts the
manifests. The
measurement was an agent's proposal, which the maintainer accepted.
(Basis: measured; judgment, accepted by the maintainer.)

When a full rewrite of the controller skills was declined on
2026-10-01, a re-open trigger was set: skill prose above about 10% of
controller spend in a later measurement, or a rule change that had to
land in a trimmed router or adapter with no headroom left. The rewrite
it would have reopened ran as the skill text rewrite
(`docs/crucible/2026-11-01-skill-text-rewrite/umbrella.md`), and the
trigger was retired on 2026-11-03: growth is held word by word by the
prose budget, per skill by `tests/test_skill_size.py`, and in the router
and host maps by the session-start budget (`tests/test_session_start.py`,
10,000 characters), which covers the trigger's second clause. An agent's
proposal, which the maintainer accepted. (Basis: judgment, accepted by
the maintainer.)

### The prose budget

From 2026-10-07 a rewrite was to be net-negative in shipped skill prose,
and a feature that added prose named what it removed in exchange or why
nothing could go, citing its diffstat. That governed each change's net and showed no skill's total: one feature
estimated +130 to +200 words and measured +745. A count per skill
directory makes the total visible in every commit. The maintainer, on
2026-10-16: "OK, let's try the ratchet (though I expect it to result in
a series of raises)". (Basis: measured; judgment, accepted by the
maintainer.)

Until 2026-11-02 every `*.md` under a skill directory was hand-edited,
so counting them all counted what an author maintains. From then the
seat templates are rendered from sources beside them with shared
sections spliced in, and counting a rendered template beside its source
would count its text twice, spliced sections once per template that
takes them, and say nothing about what an author maintains. The count
takes each hand-edited file and no rendered template; what a seat
carries at dispatch, the rendered size, is a different measure, reported
beside it where a feature measures it. An agent's proposal, which the
maintainer accepted on a decision ask, reading the skill text rewrite's
"no rule changes, but one" as not covering this authoring check.
(Basis: judgment, accepted by the maintainer.)

### Build history

On 2026-08-29 the maintainer directed that code comments carry no
execution narrative: comments state current invariants and hazards, and
task and wave history goes to commit messages. On 2026-10-07 the rule
widened to everything a change ships. A feature's spec and plan are
frozen build records, so a comment pointing at one points at history;
decision records and changelogs are exempt because history is their job,
which a branch review found the first wording would have flagged. No
test bans the patterns: a regex list catches shapes, not the habit, and
the rule has to hold in every project crucible runs on, not in
crucible's repository alone. (Basis: the maintainer's preference, for
the 2026-08-29 rule; judgment, accepted by the maintainer, for the
widening and the absent test.)

### Terminology

Agents read terms literally, so one thing gets one name. Converting
"your human partner" in upstream's text would add differences to files
that are otherwise upstream's (`docs/decisions/upstream-skills-kept-close.md`).
The terms date from 2026-10-07 and 2026-10-09; the reader's glossary went
into the README on 2026-10-19. (Basis: judgment, accepted by the
maintainer.)

### Descriptions

Upstream found that "when a description summarizes the skill's workflow,
an agent may follow the description instead of reading the full skill
content": a description saying "code review between tasks" got one
review where the skill's flowchart showed two
(`superpowers/skills/writing-skills/SKILL.md` at v6.2.0). Six
descriptions were cut to their triggers on 2026-10-07. On 2026-10-14 the
rule was relaxed to let a description say what the skill is for:
Anthropic's "Skill authoring best practices" asks for both what a skill
does and when to use it (read 2026-10-20), and the procedure's steps stay
out. (Basis: external, for upstream's finding and Anthropic's guidance;
judgment, accepted by the maintainer.)

### writing-skills

On 2026-10-14 the directory was the largest skill crucible shipped:
14,971 words of markdown, most of it upstream's or a verbatim vendor
copy. Upstream's testing guide told the evaluator to "Make agent believe
it's real work, not a quiz", listed invented pressures, and counted an
agent that "argues skill is wrong" as not bulletproof
(`superpowers/skills/writing-skills/testing-skills-with-subagents.md` at
v6.2.0). Its Iron Law, "NO SKILL WITHOUT A FAILING TEST FIRST", went
unfollowed as written: of three recorded sessions that loaded the skill,
two edited with no baseline run, and the third ran a micro-test with a
no-guidance control, a section the shrink keeps. Its word targets ("Other
skills: <500 words") were exceeded by most of crucible's skills,
redteaming's `SKILL.md` by about ten times. (Basis: measured; external,
for upstream's text.)

An agent recommended shrinking the skill rather than removing it or
rewriting it whole, and the maintainer agreed: "OK, agree with the
recommendation". Of two evaluation rules the agent offered, the
maintainer chose the narrower, disclosing dilemma scenarios only ("I
guess 1"). In SDD's task loop implementer seats write the skill text,
and before 2026-10-14 no template named the skill, so the pointer is in
the implementer's template. (Basis: judgment, accepted by the maintainer.)

On 2026-11-03 the skill was rewritten around reader cost. The prose compaction (`docs/crucible/2026-11-03-prose-compaction/effort.md`) had found crucible's skill text regrown within weeks of each rewrite, with 67 raises and 27 lowers of the prose budget since 0.2.0 and none refused, and ranked new mechanisms, review that counts omissions but never excess, and restatement as its main causes. The maintainer asked whether a light version of that effort's per-file pipeline should become the default, and for the skill to cover all reused prompt-class text. An agent argued against running it on every edit: it works on phrasing, not on the mechanisms behind most growth; it would cost a share of the effort's spend, about 850k tokens a file, mostly cached reads, on every edit; and per-file passes miss rules two files each drop on the strength of the other. It proposed the general rules for writing-skills and left the project-side controls, a measured trigger among them, to `docs/backlog/prose-creep-containment.md`. The maintainer accepted, adding that token costs are reliably underestimated before implementation, so a control measures the written text. (Basis: measured, for the budget history; the maintainer's preference, for the estimate; judgment, accepted by the maintainer.)

A micro-test chose the fix rule (`docs/crucible/2026-11-03-writing-skills-reader-cost/microtest/`): fresh agents applied two of the prose compaction's own review findings to the files as they stood before the fix, five runs per arm. Under the skill as it then stood, every run revised the sentence that owned the case, so "replace before adding" had nothing to fix and was not written; the added words were the finding's reasons and a term its pointer already defined, copied into the rule. The recipe that keeps those out took the `setup.md` case from a median of 11 added words (5 to 14) to 5 in all five runs, and the `umbrella-children.md` case from 33 (26 to 36) to 22 (14 to 22); the fixes on record had added 5 and 10. With the rewritten skill as the guidance (at its final text), the `umbrella-children.md` case came to a median of 17 (13 to 22), no run restating the defined term; earlier runs of that arm on the intermediate texts gave medians of 21, 17 and 12, so a five-run median moves by about five words between runs. Two cases, one model, five runs per arm. (Basis: measured.)

The rewrite re-derived `SKILL.md` from a rule inventory of the 1,576-word file, 150 items after a completeness critic's additions: a writer that never read the original worked from the inventory and a brief of the new rules. A blind check against the inventory led to one repair, and a second blind check to a few wording fixes the controller made; the branch review read those, and its findings led to four waves: a fix wave, a cleanup wave, a third fix wave and, on the maintainer's answer past the cap, a fourth. A blind check of the text the last wave left, against the inventory and the rulings, found no item missing or weakened and sixteen dropped by ruling: three retired and thirteen support items. The rulings on items: support items go where the text works without them; three items retire: crucible's own skills directory, which every user paid for, the opening's three kinds of skill, which the four evaluated kinds replace, and the toolkit's claim that prohibitions backfire on a missing element, which nothing supported: the form table names prose reminders as the wrong form there, and upstream's tests covered wrong-shaped output only; and the supporting-file rule, restated in reader-cost terms (a long passage that serves one step or one reader), retires its 100-line threshold, which a file written one paragraph per line no longer measures. `SKILL.md` was capped at its pre-change 3,366 tokens (Anthropic's token count) and came to 3,208; the cap bound this rewrite only. The rewrite reverses the 2026-10-14 rejection of a whole rewrite, whose reason, a 14,971-word skill that was mostly upstream's, no longer held at 1,576 words of crucible's own. (Basis: measured, for the sizes and the checks; judgment, accepted by the maintainer, for the restructure, the cap and the reversal; judgment, an agent's call the maintainer has not ruled on, for the rulings on items.)

### How records cite

A record cites by path and heading so that the scanner can fail a
dangling citation. Records point at skill sections more than the skills
point at each other, and a record is edited with the change it records,
so any heading may be cited and the scanner checks that the cited text
begins with one, a limit `docs/authoring.md` § Reference convention states
(words appended to a real heading pass). The skills
had the same freedom only for headings `docs/authoring.md` listed as
frozen, one in all, while they cited 42 others (as counted on
2026-10-27); since the
scanner fails a citation whose heading is gone whether listed or not,
and placement moved enough text that a hand-kept list would lag, the
restriction was retired on 2026-11-02. An agent's proposal, which the
maintainer accepted with the placement design. (Basis: measured, for
the count; judgment, accepted by the maintainer.) Writing
upstream paths with a prefix lets the scanner tell them from crucible's
own paths while it still fails a dangling crucible reference. (Basis:
judgment, accepted by the maintainer, 2026-10-20.)

### Line endings

The SessionStart hook is a bash script, and bash fails on a script with
CRLF line endings. `AGENTS.md` said line endings are LF, but only `*.sh`
and the hook were pinned; upstream also pins `*.md`, `*.json` and other
text types (its `.gitattributes` at v6.2.0), which the port dropped with
no recorded reason. Setting LF for every text file on 2026-10-17 changed
one committed file, in bytes only. (Basis: judgment, accepted by the
maintainer.)

### One line per paragraph

Counted with Anthropic's token-counting endpoint on 2026-11-03, joining the hard wraps of three files cut their tokens by 4 to 5% as raw text (`seat-rules.md` 4,725 to 4,533, `formats.md` 7,684 to 7,316, the implementer agent 6,172 to 5,901) and by 12 to 13% as Claude Code's file reader returns them, each line numbered (5,737 to 5,020, 8,995 to 7,943, 7,361 to 6,406). Every agent read pays it, and a wrap carries nothing a reader needs. An agent's proposal, on which the maintainer left the call to the agent. (Basis: measured; judgment, accepted by the maintainer.)

## Rejected

- **A full rewrite of the controller skills** (2026-10-01): about three
  times the saving of the references at several times the cost, and it
  would reword rules that each came from an incident. The rewrite later
  ran as the skill text rewrite, and its re-open trigger is retired
  (§ Why).
- **Folding the route references back in**: they pay whenever a route
  does not run (§ Why).
- **A total or reduction target** for skills or a rewrite, in bytes or
  words: declined on 2026-10-07; the budget is a ratchet, not a target,
  and writing-skills sets none. The 18,000-character line is no such
  target: it is a per-skill ceiling the host's cut imposes (§ Decision).
  The cap on writing-skills' `SKILL.md` at its 2026-11-03 token count
  bound that one rewrite (§ Why).
- **A per-feature prose diffstat**: replaced by the budget file's diff.
- **A standing ban test, or a contributor rules file, for build
  history** (§ Why).
- **A test pinning description wording**: it would pin prose
  (`docs/decisions/crucible-suite.md`).
- **Removing writing-skills** (§ Why).
- **A compaction pass on every edit** (2026-11-03): it works on phrasing, not on the mechanisms behind most growth, at a share of a whole compaction's cost each time (§ Why).
- **Generating skill text** as the seat templates are generated: a
  shared rule spliced into each skill would reach a controller once per
  skill it loads (§ Why).
- **Evaluation that tells the agent anything false**, and with it
  upstream's pressure fixtures; also **announcing every evaluation run**,
  the wider option the maintainer did not take.
- **Copying vendor guidance** into the skill: linked instead.

## What a project may change

The comment policy beyond the build-history rule yields to a project's
own conventions. A project's instruction files outrank every skill rule,
the build-history rule included (`skills/using-crucible/SKILL.md`).

## Changes

- 2026-11-03: writing-skills covers text agents act on and is organized around reader cost, with a micro-tested fix rule, excess as a review finding and `compacting.md` for compaction; its supporting-file rule is stated in reader-cost terms; a compaction pass on every edit is rejected; it was rewritten whole from a rule inventory, reversing the 2026-10-14 rejection of a whole rewrite, its `SKILL.md` capped at its prior token count for that rewrite only; because the maintainer asked it to carry what the prose compaction learned about creep and to cover all reused prompt-class text.
- 2026-11-03: the split files' word counts are dated to the moves, since the per-file compaction cut those files further.
- 2026-11-03: text under `skills/` holds each paragraph and list item on one line, because a hard wrap cost 4 to 5% of a file's tokens raw and 12 to 13% with the line numbers a file reader adds.
- 2026-11-03: a skill's rationalization table drops rows that only restate its body, the router's Red Flags kept whole, revisiting the placement's whole-table keep: a minor loss under the maintainer's compaction mandate, each row cut having restated a body rule with no recorded catch.
- 2026-11-03: SDD's ledger line forms for leads and `## Questions` sit in its setup reference, an exception to the spine's rules that bind beyond their step; because the texts where leads and questions are written restate the forms or cite that file, and the forms no longer ride every re-attach.
- 2026-11-03: the flip-paths stubs in redteaming and SDD send a feature's controller to `skills/brainstorming/references/umbrella-children.md` § Under an umbrella before it raises a late split or a binding change and before its first boundary check for a landed one, and back after compaction; because the umbrella split left that section cited there without the read and re-read that flip-paths' stub had given it. The umbrella split's word count for `umbrella-children.md` also states its size after § Marks took in the no-line procedure.
- 2026-11-03: the premise-finding route has a reference of its own, `skills/redteaming/references/premise-asks.md`, with a redteaming stub that keeps the re-read line the flip-paths stub gave it; because a controller handling a premise finding loaded all of flip-paths for one section.
- 2026-11-03: brainstorming has two umbrella stubs, `skills/brainstorming/references/umbrellas.md` for the umbrella's own controller and `skills/brainstorming/references/umbrella-children.md` for a child's, which also holds flip-paths' raising and receiving steps; because a child loaded the whole umbrellas reference, and flip-paths for one section, to act on the children's side alone.
- 2026-11-03: the round record's shapes have a home of their own, `skills/redteaming/references/round-record.md`, its `##` headings frozen as `formats.md`'s are; because every route loaded all of `formats.md` at brainstorm for the workspace and the feature folder, about half of it a round record only the spec campaign and the plan phase write.
- 2026-11-03: the rules seats share have a second home, `skills/subagent-driven-development/references/review-terms.md`, for the sections controllers also read; because § The arrangement questions, § Finding scope and § Suite bound moved there from the shared seat reference (`docs/decisions/instruments.md`).
- 2026-11-03: the stub convention's statement shortened, and it says a reference read since the last compaction is not read again when its step recurs: what this record's reasoning already held, now in the text a controller reads.
- 2026-11-03: resident tokens re-counted after the compaction fit's
  branch-review fixes, which lowered SDD's every-run load by 4 tokens.
- 2026-11-03: the compaction fit's basis tags name the agent's calls the
  maintainer has not ruled on, and the very-small lane's token saving is
  attributed to the files it no longer loads, both misstated when added.
- 2026-11-03: resident tokens per route counted before the skill text
  rewrite, before the compaction fit and after it, as the baseline a
  later measurement compares with; the full-rewrite re-open trigger
  retired, since the rewrite ran as the skill text rewrite and growth is
  held by the prose budget, the size test and the session-start budget.
- 2026-11-03: every `SKILL.md` body at or under 18,000 characters, held
  by a test, since the host re-attaches a skill cut at about 20,000
  characters after compaction; long step bodies move into references as
  route procedures do, the spine staying; what a stub means stated once
  per skill, and after compaction only the reference of the step in
  progress re-read before acting; the byte-or-word-target rejection
  narrowed to totals and reductions.
- 2026-11-03: the cross-skill citation count is dated as counted, not as
  filed: the filing date is not known.
- 2026-11-03: placement of shared rules, so that each rule has one owner
  and its copies stop drifting: seat rules in the shared seat reference,
  spliced into the templates; controller-shared dispatch rules in
  `dispatch-composition.md`; host-neutral dispatch rules and the
  decision ask in the router; the paired texts listed in
  `docs/authoring.md`; skill text not generated; any skill heading
  citable from a skill, the frozen list having lagged the citations.
- 2026-11-02: the prose budget counts hand-edited text, every `*.md` of
  a skill but the templates the generator renders, since a rendered
  template beside its source would count its text twice.
- 2026-10-20: records cite skill headings as
  `crucible:<skill> § <heading>`, a bare `README.md` citation as the
  root README, and upstream paths with the `superpowers/` prefix; the
  reference scanner checks records and the map.
- 2026-10-20: one owner text per rule, where its reader acts; how a rule
  was learned in the decision records; `formats.md` for shapes,
  `docs/authoring.md` for author rules, one shared seat reference once
  one exists.
- 2026-10-19: one name per thing: the operator, round and wave, the
  terminal pass and second read, campaign and plan phase; the glossary
  in the README.
- 2026-10-17: LF for every text file.
- 2026-10-16: a word-count budget per skill directory, raised with a
  reason in the commit that grows it, in place of the per-feature
  diffstat.
- 2026-10-14: descriptions give triggers, may say what the skill is for,
  and never list the procedure.
- 2026-10-14: writing-skills shrunk to the hosts' tooling, upstream's
  form-to-failure and micro-test sections and honest evaluation, with an
  implementer pointer.
- 2026-10-13: route-conditional procedures in references read on demand
  behind always-loaded stubs, the flip paths in one shared reference.
- 2026-10-07: no build history in anything a change ships; comments
  state invariants and cite symbols, under the project's conventions.
