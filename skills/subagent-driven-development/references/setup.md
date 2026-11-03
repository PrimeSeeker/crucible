## Setup

A plan crucible did not produce goes to `crucible:brainstorming` as input before Setup creates anything.

First find the feature workspace `.crucible/<feature-slug>/`:

- In this checkout: proceed.
- In another checkout (`git worktree list`): work from that checkout's path; create no worktree or empty workspace here. Where your host cannot work from another path, stop and tell the operator where the workspace is.
- Nowhere: create the isolated worktree with `crucible:using-git-worktrees` and work from the checkout it leaves you in.

In the checkout you work from, always run the provisioning step (`skills/redteaming/references/formats.md` § Feature workspace root and layout); re-running it changes nothing.

Then run the project setup and the clean baseline there, unless `crucible:using-git-worktrees` just ran them, its Steps 2–3; either way, record the result in the ledger under `## Progress` as `Baseline: <result> at <sha7>`. A ledger already carrying that line means both ran: skip them.

- Run the project's dependency setup, where it has one.
- For the baseline, run the project's own test command. If tests fail, report the failures and ask whether to proceed or investigate.

Read the plan once, its spec pointer included (the header line naming the pinned spec and what the pin makes binding), and create a todo per task.

Then, before any task, seed the ledger from the records of the phases that ran: the plan record (`campaigns/plan/round-01/record.md`), the spec campaign's records and the brainstorm decision record. Seed each item once; on resume, only what the ledger lacks.

- Each `Contained amendment:` item of the plan record's `## Fix list`: under `## Adjudication rulings`, as one of your rulings in the item's form, with the reason and why it is contained, from its merged entry's ruling, beside it.
- Each premise ask open in the plan record or the brainstorm decision record, or carried by the spec campaign's close (`skills/redteaming/references/premise-asks.md`): there too, as open.
- Each `deferred-minor` entry of the spec campaign's records and the plan record: under `## Deferred minors`, as `<source>: minor (deferred): <one-liner>`, `<source>` being `Spec` or `Plan`.
- **What earlier phases left open**: under `## Questions`, one line each, as `<phase>: <item> — carried`, `<phase>` being `brainstorm`, `spec` or `plan`. It covers dispositions sending work to a follow-up outside the feature, parked entries the operator has not ruled on, the unaddressed part of a partly applied entry, and carried questions the operator left unanswered; not `deferred-to-implementation` (the plan's tasks own it) nor `deferred-minor` (above).

**Leads** are `## Deferred minors` lines the branch reviewer rules on rather than triages: `<source>: lead: <one-liner>`, `<source>` being `Task <N>`, or `Lane` on the very-small lane; the branch review's own lead sources and `## Questions` forms: `crucible:requesting-code-review § The branch-review loop`. No seat reads `## Questions`; the close readout lists it.
