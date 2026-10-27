---
name: writing-skills
description: Use when creating or editing a skill or other text that instructs agents, such as a prompt or a dispatch template, or when checking whether such text works.
---

# Writing Skills

A skill is guidance an agent loads when its description matches the
situation: a technique, a pattern of thought, or reference material. It is
not the story of how one problem was solved once. Prompts and templates are
the same kind of text: another agent acts on them. Project conventions go
in the instruction file the host reads at session start (`CLAUDE.md` on
Claude Code, `AGENTS.md` on Codex), and a constraint a check can enforce
goes in the check.

## Start with the host's own tooling

Each host has a skill creator that scaffolds a skill and runs evaluations
of it; use it for both. This skill covers what those leave out.

- **Codex:** `skill-creator` is built in, under `~/.codex/skills/.system/`.
  Personal skills go in `$HOME/.agents/skills`. Guidance:
  <https://learn.chatgpt.com/docs/build-skills>
- **Claude Code:** the official plugin marketplace's `skill-creator`
  plugin. Personal skills go in `~/.claude/skills/<skill-name>/SKILL.md`.
  Guidance: <https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices>
  and <https://code.claude.com/docs/en/skills>

Crucible's own skills live in this plugin's `skills/` directory, one tree
for both hosts.

## Descriptions and names

The host matches the description against the task to decide whether to
load the skill. Give concrete, discriminating triggers that cover the
situations where it applies: symptoms, contexts, the words a user or agent
would use. It may say what the skill is for. It never lists the
procedure's steps: upstream (superpowers) found an agent following a
description's workflow summary in place of the body, so a description
saying "code review between tasks" got one review where the skill's
flowchart required two. Too narrow a description under-triggers
(Anthropic's guidance); a catchall over-triggers (Codex's). Write it in
the third person.

Frontmatter needs `name` and `description`. The name is at most 64
characters of lowercase letters, numbers and hyphens, matches the skill's
directory, and says what you do (`condition-based-waiting`, not
`async-test-helpers`). The description is at most 1,024 characters.

## Match the form to the failure

Before writing guidance, classify the failure it is for. The form that
fixes one failure type measurably backfires on another.

| Failure | Right form | Wrong form |
|---|---|---|
| Skips or breaks a rule it knows (knows better, does it anyway) | Prohibition, rationalization table and red flags (The discipline toolkit, below) | Soft guidance ("prefer...", "consider...") |
| Complies, but the output has the wrong shape (bloated prompt, buried verdict, restated spec) | Positive recipe or contract: state what the output IS, its parts, in order | Prohibition list ("don't restate", "never narrate") |
| Omits a required element from something it already produces | Structural: a REQUIRED field or slot in the template it fills in | Prose reminders near the template |
| Behavior should depend on a condition | Conditional keyed to an observable predicate ("if the brief exists, reference it") | Unconditional rule plus exemption clauses |

**Why prohibitions backfire on shaping problems:** under a competing
incentive ("make the prompt self-contained"), agents negotiate with "don't
X". In upstream's head-to-head wording tests on dispatch-prompt guidance,
the prohibition arm produced clearly more of the unwanted content than the
recipe arm (fully separated distributions), and trended worse than even
the no-guidance control. Micro-test your own case rather than assuming,
but never reach for the prohibition by default. A recipe leaves nothing to
negotiate: the output matches the stated shape or it doesn't.

**Rules for whichever form you pick:**
- **No nuance clauses.** "Don't X unless it matters" reopens the
  negotiation: in the same upstream tests, appending a single nuance clause
  to a winning recipe degraded it from consistent to noisy. Express a real
  exception as its own conditional on an observable predicate.
- **Exemption clauses don't scope.** "This limit doesn't apply to code
  blocks" still suppresses code blocks. If part of the output must be
  exempt, restructure so the rule can't reach it.

## Evaluating a skill

Tell the evaluated agent nothing false: no claim that the run is real work,
no invented stakes or pressure. A dilemma scenario, one built to set the
guidance against something else, is disclosed as an evaluation. A
realistic task, run the way the hosts' skill creators run it (Claude
Code's with and without the skill, Codex's with it), needs no
announcement. An agent that asks or escalates, or argues the skill is
wrong, has produced an outcome to examine, never a failure by definition:
it may have made the right call, or found a defect in the skill.

**Baseline.** Know the failure before writing for it: a recorded incident,
or a run without the guidance. A skipped baseline is recorded with its
reason.

**By skill type:**
- **Discipline** (a rule the agent knows and might skip): a realistic task
  where skipping is tempting, or a disclosed dilemma. Record what it did
  and the reasons it gave.
- **Technique:** apply it to a new case and to variations; look for gaps
  in the instructions.
- **Pattern:** does it recognize when the pattern applies, and when not?
- **Reference:** does it find the right information and use it correctly;
  are the common cases covered?

### Micro-test wording first

Full scenario runs are slow and costly per iteration. Check the wording
itself first:

1. **One fresh agent per sample:** a raw API call, or a single-shot
   subagent. Its context is the realistic context the guidance will live in
   (the whole skill or template, not the guidance alone); its task is one
   that invites the failure.
2. **Always include a no-guidance control.** If the control doesn't show
   the failure, there is nothing to fix: stop, don't write the guidance.
3. **Five or more repetitions per variant.** Single samples lie.
4. **Read every flagged match by hand.** Score programmatically if you
   like, but template echoes and quoted counter-examples pass for hits;
   automated counts alone overstate both failure and success.
5. **Variance is a signal.** When guidance lands, repetitions converge on
   one shape. Five interpretations in five runs means the wording isn't
   binding: tighten the form before adding words.

Micro-tests check wording; a discipline skill still needs its scenario
evaluation.

### When the guidance isn't working

When an agent read the skill and went another way, ask it, as the
evaluator: how could the skill have been written to make the expected
choice clear? The answers sort three ways:

1. **"It was clear; I chose otherwise."** Not a wording problem. Weigh its
   reasons: the rule may be wrong, or it may need its reason stated, or a
   rationalization-table row.
2. **"It should have said X."** A wording problem. Try its wording, and
   micro-test it.
3. **"I didn't see section Y."** An organization problem. Move it earlier
   or make it more prominent.

## The discipline toolkit

For an agent that knows a rule and breaks it. For wrong-shaped output or a
missing element, prohibitions backfire: use the forms above.

- **State the reason.** An agent that knows why a rule exists can apply it
  to a case no list anticipates.
- **Close the loopholes you saw.** Name the specific workarounds the
  baseline produced, not just the rule.
- **Rationalization table.** Every excuse from the baseline, verbatim,
  beside why it doesn't hold:

  | Excuse | Reality |
  |---|---|
  | "Too simple to test" | Simple code breaks. The test takes thirty seconds. |
  | "I'll test after" | A test that passes at once proves nothing. |

- **Red-flags list.** The thoughts that come just before the violation
  ("this case is different because..."), so the agent can catch itself.
- **Trigger on the moment before.** The description can name the point
  where the violation happens ("before writing implementation code").

## Structure

- **Files.** `SKILL.md` alone, unless there is heavy reference material
  (a hundred lines or more) or a reusable tool; principles and short code
  stay inline. Cite every supporting file from `SKILL.md` and say when to
  read it.
- **Cross-references.** Name the skill (`crucible:systematic-debugging`)
  or the file's path, and say whether it is required. Never force-load
  one: an `@path` import loads the file at once, before it is needed.
- **Flowcharts** only for a non-obvious decision, a loop an agent might
  leave too early, or an A-versus-B choice; never for reference material
  (use a table), code (use a code block) or linear steps (use a numbered
  list). Style: `skills/writing-skills/graphviz-conventions.dot`.
- **Examples.** One excellent example beats many mediocre ones: complete,
  from a real case, commented with why. Not five languages, not a
  fill-in-the-blank template.
- **Portability.** Write forward slashes in paths, examples included, and
  run scripts only with an interpreter your users' hosts have, naming it
  in the invocation (`bash <script>`, `python <script>`), never a bare
  path: packagers can strip executable bits.
- **Size and placement.** Always-loaded text (descriptions, anything a
  host injects at session start) is budgeted by its host. Everything else
  is as short as its job allows. State each rule once, where its reader
  acts on it, and point to it from elsewhere. Give the action, its
  observable signal and at most one clause of why: how the rule was
  learned belongs in the project's decision records. Write siblings in one
  list or section at the same grain, and move detail to a supporting file
  or a tool's `--help`.
