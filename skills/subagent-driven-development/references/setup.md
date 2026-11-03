## Setup

**A plan crucible did not produce** goes to `crucible:brainstorming` as its input before any Setup step creates anything.

**Find the feature workspace first** — `.crucible/<feature-slug>/`, before the worktree step and before provisioning:

- **In this checkout:** proceed.
- **In another checkout** (`git worktree list`): continue there, working from that checkout's path; create no worktree and provision no empty workspace here. Where your host cannot work from another path, stop and tell the operator where the workspace is.
- **Nowhere:** create the isolated worktree with `crucible:using-git-worktrees`, and provision the workspace in the checkout that step leaves you in.

In the checkout you work from, run the provisioning step (`skills/redteaming/references/formats.md` § Feature workspace root and layout) — re-running it changes nothing, so run it rather than assume. Then run `crucible:using-git-worktrees` Steps 2–3 there, the project setup and the clean baseline — unless that skill just ran them, creating the worktree above — and record the result in the ledger (`crucible:subagent-driven-development § Setup`) under `## Progress` as `Baseline: <result> at <sha7>`. A ledger that already carries that line means both ran: skip them on resume.

**Read the plan once** — its spec pointer included: the header line naming the spec at its pinned revision and what the pin makes binding — and create a todo per task.

**Seed the ledger** before the first dispatch, from the records of the phases that ran before execution — the plan record (`campaigns/plan/round-01/record.md`), the spec campaign's records and the brainstorm decision record — each item once: on resume, only what the ledger lacks.

- **Seed each `Contained amendment:` item of the plan record's `## Fix list` under `## Adjudication rulings`** as one of your own rulings, in that item's form with the reason and why it is contained from its merged entry's ruling beside it: the item alone carries neither, and the branch review and the close readout find it only in the ledger.
- **Seed each open premise ask there as open** — those open in the plan record and any the spec campaign's close carried (`skills/redteaming/references/flip-paths.md` § Premise findings).
- **Seed each `deferred-minor` entry** of the spec campaign's records and the plan record under `## Deferred minors`, as `<source>: minor (deferred): <one-liner>`, `<source>` being `Spec` for the spec campaign's and `Plan` for the plan record's, for the branch review's triage.
- **What earlier phases left open:** seed under `## Questions`, one line each as `<phase>: <item> — carried`, `<phase>` being `brainstorm`, `spec` or `plan`, what the brainstorm and every phase since left open: dispositions that send work to a follow-up outside the feature (not `deferred-to-implementation`, which the plan's tasks own, nor `deferred-minor`, seeded under `## Deferred minors` above), parked entries the operator has not ruled on, the unaddressed part of partly-applied ones, and carried questions the operator left unanswered.
