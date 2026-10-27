# Skill text rewrite: placement, then mechanisms

## Observation

- **The rule to apply.** writing-skills' Size and placement bullet: one
  owner text per rule, where its reader acts; the action, its observable
  signal and at most one clause of why, with how the rule was learned
  going to decision records; siblings at one grain. `AGENTS.md`'s Where
  text goes rule names their homes in crucible. Existing text has not been
  brought into line.
- **Placement is worth about 11%.** A detail-level audit of all shipped
  skill prose (three readers, read-only) judged about 5,500 of 48,700
  words wrong-level or restated: redteaming ~12%, SDD ~12%, the other
  skills ~10%. Restatement is the largest category, mostly seat templates
  copying shared rules (the deleted-test list, build history, the comment
  rule, diff-as-files, read scoping, the workspace and scratch rules); the
  copies have started to drift.
- **Where it is uneven.** Upstream-derived supporting files are written at
  a finer grain than crucible's own: systematic-debugging's supporting
  files and dispatching-parallel-agents tell one incident or example two
  or three times; using-git-worktrees explains its safety check down to
  git internals and restates its rules three or four times. The host
  adapters restate host-neutral process rules (the never-predict rule,
  fan-out independence, effort-on-request). Redteaming's lens
  roster gives right-sizing its trigger mechanics and the other lenses a
  line each. SDD specifies the adjudicator inline to git flags and the
  snapshot-blessing agent in two sentences. Templates explain their own design to maintainers, and
  the terminal-pass template carries the controller's escalation routing.
- **Size follows mechanisms.** The three execution and review skills
  (redteaming, SDD, requesting-code-review) grew from 16.3k words to 41.2k
  over two months: records and evidence machinery about 12k, two-host
  dispatch about 4.8k, cost-diet and cost-levers about 4.7k, review fix
  waves about 2.5k net. Later rewrites cut 9.8k, mostly by deleting
  mechanisms, not by rewording. Placement alone will not halve the text.
- **Resident cost.** A measurement on one project's very large features
  put skill prose resident in controllers at about 5% of their spend
  (subagents 0.2%), and a full rewrite of the controller skills was
  declined then, with a re-open trigger: skill prose above about 10% of
  controller spend in a later measurement, or a rule change that has to
  land in a trimmed router or adapter with no headroom left. On a small
  project a redteam controller loaded the redteaming skill plus
  `formats.md`, about 27K tokens, before any work, so the trigger likely
  trips there. Cost was measured in tokens, not duties or adherence.
- **Umbrellas added about 4,200 words** across six skills
  (brainstorming +53%, most of it in a reference loaded on demand). The
  largest single part is the clause on what binds, stated in full at
  thirteen statements in eleven files, about 90 to 110 words each, as
  the umbrella spec required; a one-line clause with the finding rule
  stated once would save roughly 600 to 700 words.
- **A minor defect the audit found, unfixed:** the re-review template's
  comment rule is a fragment of the implementer's and task reviewer's.
  Copying the whole rule in would add one more restatement; the shared
  seat reference is its fix.
- **"Load-bearing" means two things in SDD:** the spec's `[LOAD-BEARING]`
  mark, and the fix loop's breaker, where a "real and load-bearing"
  finding is one a later task builds on or one that reveals a plan
  defect. A reader can take the breaker's STOP as tied to the mark.

## Follow-up

- Re-audit at the current tree, then bring the skills into line with the
  placement rule: one owner text per rule; a shared seat reference the
  templates point to, once a release has shown seats reading plugin files
  through `[PLUGIN_ROOT]`; history and long rationale to the decision
  records; host-neutral rules out of the adapters.
- For each mechanism, weigh what it costs in always-loaded text against
  what it has caught; retiring the ones that don't pay is the larger
  lever, and each retirement is the operator's ruling. Part of it: restate
  the resident-cost re-open trigger above as resident tokens per route, or
  retire it.
- Fix the minor defect above on the way, and give the breaker's sense of
  "load-bearing" a word of its own.
