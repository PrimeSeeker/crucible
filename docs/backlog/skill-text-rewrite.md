# Skill text rewrite: placement, then mechanisms

## Observation

- **The rule to apply.** writing-skills' Size and placement bullet: one
  owner text per rule, where its reader acts; the action, its observable
  signal and at most one clause of why, with how the rule was learned
  going to decision records; siblings at one grain. `AGENTS.md`'s Where
  text goes rule names their homes in crucible. Existing text has not been
  brought into line.
- **Size as of `dd6897d`.** The twelve skills hold 62,069 words
  (`tests/prose-budget.txt`): subagent-driven-development 18,724,
  redteaming 17,871, brainstorming 5,994, requesting-code-review 5,581,
  the other eight 13,899 together.
- **Growth since `dd6897d`.** At `a709dbc` they hold 65,636 words,
  +3,567: redteaming +1,324, subagent-driven-development +761,
  brainstorming +672, requesting-code-review +573,
  finishing-a-development-branch +206, writing-plans +31, the other six
  unchanged. All of it is the audit-corrections feature's, whose spec
  estimated about +1,500 and set no target.
- **Placement is worth about 11%.** A detail-level audit of all shipped
  skill prose (three readers, read-only), when it came to 48,700 words,
  judged about 5,500 of them wrong-level or restated: redteaming ~12%,
  SDD ~12%, the other skills ~10%. Restatement is the largest category, mostly seat templates
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
  over two months (42.2k as of `dd6897d`): records and evidence
  machinery about 12k, two-host dispatch about 4.8k, cost-diet and cost-levers about 4.7k, review fix
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
- **Design-level findings of the umbrella audit.** An audit of the
  hypothesis-specs umbrella's three features (2026-10-29), by five
  readers blind to the review records and two tracing each finding back
  through them, found design-level problems that the effort's reviews had
  mostly seen and deferred to this item, which no commit of the effort
  updated. Its correctness findings went to a feature of their own
  (audit-corrections, 2026-10-30); these were left here:
  - growth (the size figures above);
  - separability of review before code and plan form: the route presets
    treat them as separate choices, while a feature's spec is always
    campaigned and a note never is;
  - signal and vocabulary sprawl: the labels, statuses and marks a
    reader must know;
  - the check on a check: each seat forecasts the overturn answer, the
    round readout answers the forecasts, and the terminal pass checks
    the stop against both;
  - the binding clause restated at many sites (the umbrellas bullet
    above);
  - the containment test's incident rules: exclusions in
    `skills/redteaming/references/flip-paths.md` § The containment test,
    each added after one incident.
- **Two findings that predate the effort**, found by the same audit:
  the folded lane gives "the fold requires a code baseline" as the reason
  round 0 always runs, but nothing in the fold's entry requires one, and
  `crucible:redteaming` § Round 0 gives a greenfield artifact no round-0
  agent; and the very-small
  lane's upgrade hatch moves the work to the standard route without
  naming the skill that runs next.
- **A minor defect the placement audit found, unfixed:** the re-review
  template's comment rule is a fragment of the implementer's and task reviewer's.
  Copying the whole rule in would add one more restatement; the shared
  seat reference is its fix.
- **Two numbering and naming slips:**
  - two "Step 6"s that mean different steps, both reached at one Finish:
    `crucible:finishing-a-development-branch` § Step 6: Cleanup
    Workspace removes the worktree, and step 6 of
    `crucible:subagent-driven-development` § Finish deletes the feature
    workspace, `.crucible/<feature-slug>/`;
  - `skills/redteaming/references/formats.md`'s paragraph on later
    operator rulings in the decision record enters an answer that
    leaves the call to the controller "with the delegated status that
    section defines", which reads as a fourth status; the section it
    points to, `crucible:brainstorming` § Workspace provisioning
    (brainstorm exit), defines no status but a form of `accepted`,
    `accepted — delegated to the controller`, written in the proposer's
    place.
- **Brainstorming's open-items reader points nowhere.** Its context
  gathering reads "open items in the home the project's instructions
  name for them" (`skills/brainstorming/SKILL.md` § Context gathering)
  without pointing to `skills/redteaming/references/formats.md`
  § Open items, which counts a user-level file's line naming the project
  as such a home; a strict reader may skip a home kept only there.
- **"Load-bearing" means two things in SDD:** the spec's `[LOAD-BEARING]`
  mark, and the fix loop's breaker, where a "real and load-bearing"
  finding is one a later task builds on or one that reveals a plan
  defect. A reader can take the breaker's STOP as tied to the mark.

## Follow-up

- Re-audit at the current tree, then bring the skills into line with the
  placement rule: one owner text per rule; a shared seat reference the
  templates point to, which released seats can read, as they read
  `premise-and-questions.md` through `[PLUGIN_ROOT]`; history and long
  rationale to the decision
  records; host-neutral rules out of the adapters.
- For each mechanism, weigh what it costs in always-loaded text against
  what it has caught (one data point: in one subagent-driven run, the
  tree checks around eight review seats changed nothing); retiring the ones that don't pay is the larger
  lever, and each retirement is the operator's ruling. Part of it: restate
  the resident-cost re-open trigger above as resident tokens per route, or
  retire it.
- Take the umbrella audit's design-level findings above as design
  targets of the rewrite, and fix its two predating findings on the way.
- Consider moving the right-sizing lens, with its over-subtraction guard
  and re-seat trigger, from the spec campaign to the branch review.
- Restructure how a tension a review finds gets closed, today by adding
  a distinction. For a fix-list clause asking whether a removing or
  merging resolution exists, the maintainer agreed it looked weak and
  deferred the restructuring ("probably later").
- Fix the minor defect and the two slips above on the way, and give the
  breaker's sense of "load-bearing" a word of its own.
