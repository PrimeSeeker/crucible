---
name: writing-skills
description: Use when creating, editing or compacting text that instructs agents (a skill, an instruction file, rules, a prompt or dispatch template, hook-injected text), or checking whether it works.
---

# Writing Skills

This skill covers text agents act on: skills, instruction files, rules, prompts and templates, hook-injected text. Each is as short as its job allows; a one-off prompt takes that and § Match the form to the failure, the rest paying only with reuse. A skill is guidance an agent loads when its description matches the situation, not the story of one problem solved once. Project conventions go in the host's session-start instruction file (`CLAUDE.md` on Claude Code, `AGENTS.md` on Codex), not a skill; a constraint a check can enforce goes in the check.

## Reader cost

A text costs its tokens times its reads, for each reader: an orchestrating agent every run, each dispatched agent every dispatch, each session at start.

- Measure what each reader loads and how often, in tokens, not words; a character-based estimate is close enough to compare two versions.
- Judge cost by counting the written text, never by a design-time estimate: those run low.
- Always-loaded text (descriptions, session-start injections) is budgeted by its host.
- Load each rule where its reader acts on it: text every session or dispatch loads holds only what each reader needs; a long step body goes in a file read at that step.
- State each rule once and point to it from elsewhere. For one sentence in a file its reader would not otherwise load, state the sentence: a pointer pays only where its reader already loads the target. Never a pointer longer than its rule.
- Split by reader a file one of its readers mostly skips.
- Retire a rule whose reason has lapsed (its incident fixed elsewhere, its mechanism removed): every load pays for it until it goes.
- A rule gives the action, its observable signal and at most one clause of why.
- How a rule was learned goes in the project's decision records, or its docs where it keeps none.
- Write siblings in one list or section at the same grain; detail that breaks the grain goes to a supporting file or a tool's `--help`.
- A fix revises the sentence that owns the case; its added words are the rule's new condition or action, stated as the sentence states its others, while the finding's reasons, its failure scenario and what a pointer already defines stay out of the text.
- A review counts excess as a finding, as it counts an omission: text no reader acts on, a restatement of what its reader already loads, a pointer longer than its rule, a second clause of why.
- Before compacting a text, **read `skills/writing-skills/compacting.md` in full**.

## Match the form to the failure

Before writing guidance, classify its failure:

| The agent | Use | Not |
|---|---|---|
| Knows a rule and breaks it | Prohibition, rationalization table, red flags (§ The discipline toolkit) | Soft guidance ("prefer...") |
| Complies, with wrong-shaped output | A positive recipe or contract: what the output IS, its parts, in order | A prohibition list ("don't restate") |
| Omits a required element of its output | A REQUIRED field or slot in the template it fills in | Prose reminders near the template |
| Should act on a condition | A conditional keyed to an observable predicate | An unconditional rule plus exemption clauses |

For wrong-shaped output, never reach for a prohibition by default: under a competing incentive agents negotiate with "don't X", and in the wording tests that superpowers, the project crucible derives from, ran on dispatch-prompt guidance, a prohibition produced more of the unwanted content than a recipe and trended worse even than no guidance. Whatever the form:

- No nuance clauses ("Don't X unless it matters"): in those tests one turned a winning recipe noisy. Express a real exception as its own conditional on an observable predicate.
- Exemption clauses don't scope ("This limit doesn't apply to code blocks" still suppresses them): restructure so the rule can't reach what must be exempt.

## Evaluating agent-read text

Tell the evaluated agent nothing false: no claim the run is real work, no invented stakes or pressure. A dilemma scenario, built to set the guidance against something else, is disclosed as an evaluation; a realistic task run as the hosts' skill creators run it (Claude Code's with and without the skill, Codex's with it) needs no announcement. Asking, escalating or arguing the guidance is wrong is an outcome to examine, never a failure by definition.

**Baseline.** Know the failure before writing for it: a recorded incident or a run without the guidance; record a skipped baseline with its reason.

By skill type:

- Discipline: a realistic task where skipping is tempting, or a dilemma; record what the agent did and its reasons.
- Technique: a new case and variations; look for gaps in the instructions.
- Pattern: does it recognize when the pattern applies and when not?
- Reference: does it find the right information and use it correctly; are the common cases covered?

### Micro-test wording first

Micro-test the wording before full scenario runs:

1. One fresh agent per sample (a raw API call or a single-shot subagent), given the whole skill or template the guidance will live in and a task that invites the failure.
2. Always include a no-guidance control; if it doesn't show the failure, don't write the guidance.
3. Five or more repetitions per variant.
4. Read every flagged match by hand, since template echoes and quoted counter-examples pass for hits; score programmatically if you like.
5. Variance is a signal: guidance that lands makes repetitions converge on one shape. If they diverge, the wording doesn't bind; tighten the form before adding words.

Micro-tests check wording only; a discipline skill still needs a scenario evaluation.

### When the guidance isn't working

If an agent read the guidance and went another way, ask it how the guidance could have made the expected choice clear:

- "It was clear; I chose otherwise": not a wording problem. Weigh its reasons; the rule may be wrong, or need its reason stated or a rationalization-table row.
- "It should have said X": micro-test that wording.
- "I didn't see section Y": put the section where the agent is when it acts, or make it more prominent.

## The discipline toolkit

For an agent that knows a rule and breaks it; other failures take the table's forms.

- **State the reason**, in one clause.
- **Close the loopholes you saw:** name the workarounds the baseline produced, not just the rule.
- **Rationalization table:** each excuse from the baseline, verbatim, beside why it doesn't hold, in one clause.
- **Red flags:** the thoughts just before the violation, so the agent can catch itself.
- **Trigger on the moment before:** the description can name where the violation happens ("before writing implementation code").

## The host's own tooling

Scaffold and evaluate with each host's skill creator; this skill covers what those leave out.

- **Codex:** `skill-creator` is built in, under `~/.codex/skills/.system/`. Personal skills go in `$HOME/.agents/skills`. Guidance: <https://learn.chatgpt.com/docs/build-skills>.
- **Claude Code:** the official plugin marketplace's `skill-creator` plugin. Personal skills go in `~/.claude/skills/<skill-name>/SKILL.md`. Guidance: <https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices>, <https://code.claude.com/docs/en/skills>.

## Descriptions and names

Give concrete, discriminating triggers (symptoms, contexts, the words a user or agent would use) covering every situation the skill serves: too narrow a description under-triggers (Anthropic's guidance), a catch-all over-triggers (Codex's). The description may say what the skill is for, never the procedure's steps, which an agent may follow in place of the body; third person, at most 1,024 characters.

Frontmatter needs `name` and `description`. The name, at most 64 characters of lowercase letters, numbers and hyphens, matches the skill's directory and says what you do (`condition-based-waiting`, not `async-test-helpers`).

## Structure

- **Files.** `SKILL.md` alone, unless a long passage serves only one step or one reader, or there is heavy reference material or a reusable tool; principles and short code stay inline. Cite every supporting file from `SKILL.md`, saying when to read it.
- **Compaction cut.** Where a host re-attaches skills cut at a fixed size after compaction, `SKILL.md` stays under the cut: long step bodies go to files read at their step; it keeps the steps with their triggers, resume rules, loop bounds, gates, rationalization tables, red-flags lists and rules binding beyond one step.
- **Cross-references** name the skill (`crucible:systematic-debugging`) or the file's path and say whether it is required; never force-load one, as an `@path` import does.
- **Flowcharts** only for a non-obvious decision, a loop an agent might leave too early, or an A-versus-B choice; reference material takes a table, code a code block, linear steps a numbered list. Style: `skills/writing-skills/graphviz-conventions.dot`.
- **Examples.** One excellent example, not many mediocre ones: complete, from a real case, commented with why; not five languages, not a fill-in-the-blank template.
- **Portability.** Forward slashes in paths, examples included. Run scripts only with an interpreter your users' hosts have, named in the invocation (`bash <script>`, `python <script>`), never a bare path.
