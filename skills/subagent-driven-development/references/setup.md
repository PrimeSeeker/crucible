## Setup

**A plan crucible did not produce** goes to `crucible:brainstorming` as its input before any Setup step creates anything.

**Find the feature workspace first** — `.crucible/<feature-slug>/`, before the worktree step and before provisioning:

- **In this checkout:** proceed.
- **In another checkout** (`git worktree list`): continue there, working from that checkout's path; create no worktree and provision no empty workspace here. Where your host cannot work from another path, stop and tell the operator where the workspace is.
- **Nowhere:** create the isolated worktree with `crucible:using-git-worktrees`, and provision the workspace in the checkout that step leaves you in.

In the checkout you work from, run the provisioning step (`skills/redteaming/references/formats.md` § Feature workspace root and layout) — re-running it changes nothing, so run it rather than assume. Then run `crucible:using-git-worktrees` Steps 2–3 there, the project setup and the clean baseline — unless that skill just ran them, creating the worktree above — and record the result in the ledger (`crucible:subagent-driven-development § Setup`) under `## Progress` as `Baseline: <result> at <sha7>`. A ledger that already carries that line means both ran: skip them on resume.

**Read the plan once** — its spec pointer included: the header line naming the spec at its pinned revision and what the pin makes binding — and create a todo per task.
