# Skill text rewrite: what stays open

## Observation

- **Separability of review before code and plan form.** An audit of the
  hypothesis-specs umbrella's three features (2026-10-29) found that the
  route presets treat review before code and the plan's form as separate
  choices, while a feature's spec is always campaigned and a note never
  is.
- **How a tension gets closed.** A tension a review finds is closed
  today by adding a distinction. For a fix-list clause asking whether a
  removing or merging resolution exists, the maintainer agreed it looked
  weak and deferred the restructuring ("probably later").
- **A rule gap:** when the operator answers the after-three-waves ask
  with another approach by a plan change rather than a revert, nothing
  says what happens to the task's open findings: its latest line stays
  `fix wave 3/3`, and the resume rule sends it to an ask already
  answered.
- **Umbrella landings.** Whether a clause-sized binding change to an
  umbrella entry needs a landing of its own on the base branch first:
  one feature needed two such landings for one-clause edits.
- **A review missing a verdict.** `crucible:subagent-driven-development`
  § The Task Loop says never to accept a review report missing any
  verdict, and `crucible:requesting-code-review` sends its two cases (a
  pass leaving a lead it was handed unruled, a re-review leaving a
  fix-report concern unruled) there for the action; neither says what
  the controller then does: resume the seat for the verdict, dispatch a
  fresh one, or rule itself.
- **Left open by `placement`** (2026-11-03):
  - an umbrella's closing-review seats are composed with no template,
    yet the shared sections copied into their prompts
    (`skills/subagent-driven-development/references/seat-rules.md`
    § Premise findings, § Questions) send them to "your report format",
    and `skills/brainstorming/references/umbrellas.md`
    § Closing review gives them no report form;
  - `seat-rules.md` § Seat conduct bans every seat from reading another
    checkout; the plugin files are reached only through each template's
    read list, which could conflict where the plugin root is itself a
    checkout of the repository under review (a development install).
- **Left open by `compaction-fit`** (2026-11-03): both of its spec
  campaign's terminal passes read files outside their enumerated inputs
  to run the checks the template asks for, since checking a spec's
  factual claims needs the cited files; the terminal-pass template's
  read scoping conflicts with its instruction to run a check where a
  claim needs one.
- **Left by the umbrella's closing review** (2026-11-03, range
  `8c14505..902bded`):
  - `docs/decisions/authoring-crucible.md` retires the resident-cost
    re-open trigger on the ground that growth is "held word by word by
    the prose budget"; a commit that grows a skill raises its number,
    rendered seat templates are no longer counted, and the umbrella's
    own Problem shows about 3,900 words of growth under that budget;
  - the goal check, the outside-the-frame lens and the alternate-role
    swap are tied to round 1 by its number, so a round 1 recorded
    degraded instead of topped up drops all three for that campaign;
  - a task waiting on an operator ask after an implementer's BLOCKED
    report gets no ledger line, so after compaction the resume rule
    reads it as not done and resumable; the `Task <N>: BLOCKED` wait
    covers only the answer after the third fix wave;
  - on the very-small lane nothing reachable says what to do when the
    lane's implementer reports NEEDS_CONTEXT, or BLOCKED for context or
    reasoning: that handling lives in `references/task-loop.md`, which
    the lane neither applies nor loads;
  - an umbrella's closing-review seats are dispatched with no named
    status-check window, so the tree-check guard does not cover them;
  - three wording points: "decision asks stand apart" reaches the
    campaign gate, the umbrella landing and the closing review only
    through a redteaming reference, and could join the router's
    § Decision asks; `references/finish.md` asks both for the decision
    asks in a final block and to end with the recommendation; "proposing
    no preset" after a hatch is stated only in the lane reference.

## Follow-up

- Weigh the separability point and the tension-closing restructuring as
  design targets of a later rewrite.
- Fill the rule gap and state the action on a review missing a
  verdict, each in the skill that owns the step.
- The umbrella-landing question: weigh it when the umbrella procedure is
  next edited.
- `placement`'s open items: give composed seats their report form;
  state the plugin-root exception in § Seat conduct if a development
  install needs it.
- `compaction-fit`'s open item: let the terminal pass read the files a
  claim it checks cites, or say what it does with a claim it cannot
  check within its inputs.
- The closing review's items: correct the trigger's stated ground or
  restate the trigger; fill the four rule gaps, each in the skill that
  owns the step; settle the three wording points.
