# Authoring crucible

## Decision

**Where text goes.** writing-skills' Size and placement bullet holds the
general rules: state each rule once, where its reader acts on it, and
point to it from elsewhere; give the action, its observable signal and at
most one clause of why, how the rule was learned going to the project's
decision records; write siblings at one grain, detail moving to a
supporting file or a tool's `--help`. `AGENTS.md` ("Where text goes")
names crucible's homes: how a rule was learned (incidents, measurements,
accepted trade-offs) in the decision records, `docs/decisions/`; host
mechanics in the adapter pair; text about crucible's own text in `docs/`;
what a seat does and produces in its template, and rules every seat
follows in one shared reference, once one exists.
`skills/redteaming/references/formats.md` holds the shapes of what
controllers and seats write and points at the skills for process rules;
`docs/authoring.md` holds the rules for crucible's authors (anchor
stability, the reference convention). Bringing the existing skills into
line is `docs/backlog/skill-text-rewrite.md`.

**Route-conditional procedures live in references.** A procedure that
applies only on some routes sits in a reference read on demand:
redteaming's `plan-phase.md` and `folded-lane.md`, SDD's
`very-small-lane.md`, brainstorming's `folded-lane-document.md` and
`lane-note.md`, and `skills/redteaming/references/flip-paths.md`, which
redteaming and SDD share. The skill keeps the section's heading with a
stub that names the reference and when to read it in full, says it binds
as if written there and is re-read after compaction; the stubs keep every
trigger in the always-loaded text. `tests/skill_corpus.py` reads a skill
together with the references its stubs name, so a test follows text that
moved.

**The prose budget.** `tests/prose-budget.txt` holds each skill
directory's word count, and `tests/test_prose_budget.py` fails when a
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
`graphviz-conventions.dot` and `agents/openai.yaml`. It sends an author to
each host's own skill creator for scaffolding and evaluations, says where
each host keeps personal skills and which instruction file it reads, and
links each vendor's authoring guidance rather than copying it. It keeps
upstream's "Match the form to the failure", its micro-test method and its
question for an agent that went another way, their measurements
attributed to upstream's wording tests. Its evaluation tells the
evaluated agent nothing false; a dilemma scenario is disclosed as an
evaluation; asking, escalating or arguing the skill is wrong are outcomes
to examine, never failures by definition. It sets no word targets. The
implementer template points its seat at it when a task changes text that
instructs agents; the skill's evaluations stay the controller's.

**How records cite.** Records and `docs/upstream.md` cite crucible's
files by plugin-root path and each other by `docs/decisions/<slug>.md`.
They cite a skill heading as `crucible:<skill> § <heading>`, any heading,
whether or not `docs/authoring.md` lists it as frozen. In them a bare
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

`formats.md` was split by reader on 2026-10-09: a controller acts on the
shapes, a script's rules are read when it refuses, and author rules only
by crucible's authors. On 2026-10-13 eight passages in it that restated a
redteaming rule became pointers, each rule still stated in the skill.
(Basis: judgment, accepted by the maintainer.)

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

### The prose budget

From 2026-10-07 a rewrite was to be net-negative in shipped skill prose,
and a feature that added prose named what it removed in exchange or why
nothing could go, citing its diffstat. That governed each change's net and showed no skill's total: one feature
estimated +130 to +200 words and measured +745. A count per skill
directory makes the total visible in every commit. The maintainer, on
2026-10-16: "OK, let's try the ratchet (though I expect it to result in
a series of raises)". (Basis: measured; judgment, accepted by the
maintainer.)

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

### How records cite

A record cites by path and heading so that the scanner can fail a
dangling citation. Records point at skill sections more than the skills
point at each other, and a record is edited with the change it records,
so any heading may be cited and the scanner checks it exists. Writing
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

## Rejected

- **A full rewrite of the controller skills** (2026-10-01): about three
  times the saving of the references at several times the cost, and it
  would reword rules that each came from an incident. Its re-open
  trigger is in `docs/backlog/skill-text-rewrite.md`.
- **Folding the route references back in**: they pay whenever a route
  does not run (§ Why).
- **A byte or word target** for skills or a rewrite: declined on
  2026-10-07; the budget is a ratchet, not a target, and writing-skills
  sets none.
- **A per-feature prose diffstat**: replaced by the budget file's diff.
- **A standing ban test, or a contributor rules file, for build
  history** (§ Why).
- **A test pinning description wording**: it would pin prose
  (`docs/decisions/crucible-suite.md`).
- **Removing writing-skills, or rewriting it whole** (§ Why).
- **Evaluation that tells the agent anything false**, and with it
  upstream's pressure fixtures; also **announcing every evaluation run**,
  the wider option the maintainer did not take.
- **Copying vendor guidance** into the skill: linked instead.

## What a project may change

The comment policy beyond the build-history rule yields to a project's
own conventions. A project's instruction files outrank every skill rule,
the build-history rule included (`skills/using-crucible/SKILL.md`).

## Changes

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
