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
- **Umbrella landings.** Whether a clause-sized binding change to an
  umbrella entry needs a landing of its own on the base branch first:
  one feature needed two such landings for one-clause edits.
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
  - three wording points: "decision asks stand apart" reaches the
    campaign gate, the umbrella landing and the closing review only
    through a redteaming reference, and could join the router's
    § Decision asks; `references/finish.md` asks both for the decision
    asks in a final block and to end with the recommendation; "proposing
    no preset" after a hatch is stated only in the lane reference.

- **Left by `prose-compaction`** (2026-11-03): `skills/redteaming/references/round-record.md` makes "the phase's final check" a condition of `confirmed` without saying what that check is (the wording dates from 0.2.0).

## Follow-up

- Weigh the separability point and the tension-closing restructuring as
  design targets of a later rewrite.
- The umbrella-landing question: weigh it when the umbrella procedure is
  next edited.
- `placement`'s open items: give composed seats their report form;
  state the plugin-root exception in § Seat conduct if a development
  install needs it.
- `compaction-fit`'s open item: let the terminal pass read the files a
  claim it checks cites, or say what it does with a claim it cannot
  check within its inputs.
- The closing review's items: correct the trigger's stated ground or
  restate the trigger; settle the three wording points.
- `prose-compaction`'s defect: name the plan phase's final check, or drop the condition.
