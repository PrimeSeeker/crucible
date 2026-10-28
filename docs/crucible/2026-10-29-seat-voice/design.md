# Seat voice: premise findings, questions and the request

Umbrella: `docs/crucible/2026-10-28-hypothesis-specs/umbrella.md`

## Intent

**The request.** The umbrella carries no request block of its own, so
the effort's opening message (2026-10-28) is quoted here, as evidence of
what was asked for, not as the standard:

> 3) I think the reviewer agents have a narrower mandate (they're still
> evolved from normal code review, after all) than the redteaming ones,
> and we should extend it to parity. I don't expect broad corrections to
> trigger often, but that's the last line of defense (maybe only
> full-branch, rather than task reviews?). Especially concerning for the
> very-small, where we don't have independent review of the premises, but
> it doesn't seem worth to introduce a redteam round
>
> 4) It feels to me that redteaming operates with too much human
> deference and/or narrow mandate as well. I'm not aiming precisely for
> the "wrong problem using the wrong methods based on a wrong model of the
> world", but it'd be directionally useful (maybe something something
> assume incomplete goal factoring?). Generally, I wonder if we could get
> agents to cast "it doesn't smell right" of various kinds in calibrated
> manner
>
> 5) Probably more proactivity throughout the process? I believe we
> disallowed improvement suggestions, for example.

and, from the same dialogue, the message that changed point 4:

> 4: Calibration is not the key point here (probably I'm consuming too
> much rationalism), the idea is - can we have the process to detect that
> things aren't right when there is no specific issue to point to, in a
> sensible manner? Say, something like "your intents don't mean what you
> seem to think they do" is not a finding in a normal sense, but
> potentially useful

This feature's own entry in the umbrella states what it must deliver.

**Problem.** A seat that doubts the premise of what it reviews has no
form to put it in. The branch reviewer cites `file:line` for every
finding and has no section for questions
(`skills/requesting-code-review/code-reviewer.md` § Calibration, § Output
Format); the task reviewer likewise (`task-reviewer-prompt.md` § Finding
Hygiene and Severity). Redteam seats have `## Questions`, scoped to what
they "could not stake as a finding" (`skills/redteaming/seat-prompt.md`).
No reviewer counts an improvement as a finding, and none has anywhere else
to put one (`docs/backlog/review-improvements.md`). No seat sees the
request, so none can check the Intent against it. An implementer's
concerns are read by the controller and, unless they bear on correctness
or scope, "noted" (`skills/subagent-driven-development/SKILL.md` § The
Task Loop, step 2): on crucible's umbrella-specs feature (2026-10-27) the
implementers' concerns named the problems that mattered and the task
reviews approved with minors (`docs/backlog/review-catch-and-implementers.md`).

**The probes** (one-off, run in this feature's context gathering,
2026-10-28; the entry's two):

- *Escape analysis*, over git history and 109 first full-scope branch
  reviews on crucible and on a second project (Python, Claude models):
  task reviews let through 12 real defects; 10 were minor wording,
  consistency or comment slips, and the 2 MAJORs were premise-level and
  needed other tasks' knowledge, both caught by the branch review. The
  largest path behind later fixes (13 items) was a task reviewer raising
  the problem as a MINOR and approving, the branch review fixing it. Of 11
  branch-review BLOCKER/MAJORs on planned routes, 6 were premise-level or
  plan-coverage gaps. Branch reviews staked a BLOCKER or MAJOR on 24% of
  planned routes and 41% of very-small lanes. On the second project
  alone: 65 first passes, 21 with a BLOCKER or MAJOR, no defect found to
  have escaped its feature.
- *Differential probe*: 10 past task reviews that approved (5 crucible, 5
  on the second project), each re-read by one fresh default-role seat
  with no rubric, given a snapshot at the reviewed head, the diff and the
  plan task. Where the original reviewer ran on the bounded role (3
  crucible samples), the seat found every later branch-review catch the
  original missed, the umbrella-specs receiving trigger and the
  binding-and-marks literal-reading gap among them. Where the original ran
  on the default role over code (4 samples), both saw the same defects;
  where a later fix exists, the original had staked it MINOR, the ledger
  carried it, and the branch review or a later commit fixed it. On records and design prose, the seat raised what the
  rubric does not ask for: an unruled decision recorded as settled, a
  policy reversal filed as a stale fact, controller proposals listed as
  operator rulings, caveats dropped from a measurement. Three defects it
  found still stood on master (D9). Model and rubric are confounded in the
  first group; the samples are small.

**Goals.**

- **G1.** A seat can stake a claim that the premise is wrong, and it
  reaches the operator without costing a fix wave.
- **G2.** A seat can voice a doubt, a misgiving or an improvement with
  nothing specific to stake, and nothing it voices is silently dropped.
- **G3.** Every seat that grades the Intent can check it against the
  request, the very-small lane's branch reviewer included.
- **G4.** An implementer's concern is ruled on, not noted.
- **G5.** Task review runs at a tier that sees what the probe found.

**Non-goals.**

- A premise-finding mandate for task reviewers: the probes found the
  rubric hiding nothing on code; their premise doubts go to `Questions`
  (D1, D3).
- Moving the re-reviewer's tier: the probes did not look at it.
- Changing which arrangement a feature takes (`arrangements`).
- Retrofitting a request block into the umbrella.

## Decisions

All lightly held unless stated.

- **D1. Premise findings.** A finding labelled `premise` claims, with
  evidence, that the goal, the Intent or the chosen approach is wrong, or
  that the request itself looks mistaken. Redteam seats, the branch
  reviewer and implementers may raise one; a task reviewer puts a premise
  doubt in `Questions` (D3). It carries a staked severity, opens no fix
  wave and consumes no cap. The controller routes it to the operator as a
  decision ask with a recommendation; while the ask is open, work goes on
  unless later work builds on the challenged premise. It sits beside the
  two labels that exist: `literal-reading` (binding text applied where its
  author plainly did not intend, a plan conflict for the controller) and a
  binding item found wrong (the containment test, `flip-paths.md`). It
  differs from both in that it always reaches the operator: it questions
  what was asked for. Basis: the entry; the form is the controller's
  proposal, accepted by the operator.
- **D2. The goal check.** Before reading the Intent, a redteam seat and
  the branch reviewer restate the goal in one sentence from the request
  block, then compare; a mismatch it can stand behind is a premise
  finding, a vaguer one a question. On the very-small lane the branch
  reviewer's Lane Fit gains this check beside its shape check, so the
  lane's goal premise gets the independent check the umbrella's G1 asks
  for. Basis: the controller's proposal, accepted.
- **D3. `Questions`, widened.** The section holds anything material a
  seat could not stake as a finding: a question, a doubt, a misgiving or
  a suggested improvement, a few at most per seat, none being the normal
  case. Redteam seats keep their section, its ids and its dispositions;
  the task reviewer and the branch reviewer gain it, and so does the
  implementer's report. A task reviewer's or an implementer's items reach
  the branch reviewer as leads; the branch reviewer's reach the operator
  in the close readout, each carried or ruled by the controller.
  Improvements stay out of findings, and that rule now points here. The
  controller may act on an improvement itself, as a lightly held change it
  names in the readout. Basis: the entry (U4 channel, improvements
  ruling); the single section is the controller's proposal, accepted.
- **D4. Location.** Every finding keeps its evidence. Its location is
  `file:line`, or, for a premise finding, the passage of the spec, plan
  or request it contradicts. Basis: the entry (format barriers).
- **D5. The request block.** A `Request` block opens the Intent of every
  spec, folded document, lane note and umbrella: the message that asked
  for the work, and any later message that changed what was asked,
  verbatim; a message the controller is unsure about is included. A part
  the no-local-context rule keeps out of a public repository is replaced
  by `[redacted: <kind>]`. A child points to its umbrella's block and
  quotes only what was asked of it. The request is evidence, not the
  standard: a seat may find it wrong. Basis: the entry; placement and form
  the controller's proposal, accepted.
- **D6. The task reviewer on the default role**, every task. The row read
  "the bounded role or better", carried from an unmeasured 2026-08-07
  proposal ("mid-tier or better"); controllers took the floor. Basis: the
  differential probe, and the operator's ruling (2026-10-29).
- **D7. Implementers' standing.** The task reviewer rules on every concern
  the implementer reports, in its deviation audit: confirmed as a finding
  at a staked severity, or dismissed with a one-line reason. A concern is
  about the task's own work; what reaches beyond it goes to `Questions`.
  An implementer may raise a premise finding (D1) and use `Questions`
  (D3). A
  fix outside its task is proposed in its report, naming the site and the
  change, never made; the controller routes it to the owning task, to the
  branch review as a deferred minor, or, where it touches binding content,
  to the operator. Basis: the entry; the form is the controller's
  proposal, accepted.
- **D8. The trace check.** For a rule tied to a trigger ("at each X, do
  Y"), brainstorming's self-review check 5 names each route and phase that
  must reach it and the moment X occurs there; the branch reviewer asks
  the same of the shipped text. No campaign seat gains a duty. Basis: the
  entry; placement the controller's proposal, accepted.
- **D9. Three defects the probe found**, fixed here:
  - `docs/decisions/umbrellas.md` says a child's mark is "the one edit to
    its entry" it may make; a clarification its spec states is the other.
  - The same record's "Recursion and flat folders" paragraph carries one
    basis, the maintainer's preference, for a quoted preference and an
    agent's reasoning together.
  - A plan-phase `Contained amendment:` fix-list item carries its reason,
    which the blind verifier must never see, and lands in the spec, outside
    the verifier's diff and read scope (`skills/redteaming/references/plan-phase.md`,
    `skills/redteaming/verifier-prompt.md`). The item carries the binding
    item and the change; the reason goes to the record's ruling; the
    verifier skips the item.

  Basis: the operator's ruling (2026-10-29).

## Constraints & invariants

- **C1.** A premise finding, a question and a lead never open a fix wave
  and never consume a wave cap.
- **C2.** Nothing a seat or an implementer voices under D1, D3 or D7 is
  dropped unrecorded: each item ends with a disposition, a ruling, a
  ledger line or a line in a readout.
- **C3.** An implementer never edits outside its task.
- **C4.** The seat-side rules of D1–D4 are stated once, in the shared
  reference (Interfaces), and the controller-side routing of D1 once, in
  `flip-paths.md`; every other site points to its home.

## Interfaces & boundaries

- **The shared reference**,
  `skills/subagent-driven-development/references/findings-and-questions.md`,
  new: what a premise finding is and its location (D1, D4), the goal check
  (D2), and what `Questions` holds (D3). Read by the redteam seat, the
  task reviewer, the branch reviewer and the implementer, each template
  pointing to it under the plugin root its dispatch names.
- **Premise routing**, in `skills/redteaming/references/flip-paths.md`:
  the controller's handling of D1, read by the redteaming controller
  (merge and readout) and by SDD and `requesting-code-review` (task loop
  and branch-review loop).
- **Leads.** A task reviewer's and an implementer's `Questions` items, and
  an implementer's out-of-task proposals, ride the ledger's
  `## Deferred minors` to the branch reviewer, which triages them as it
  triages minors. No new dispatch slot.
- **The close readout** lists the branch reviewer's `Questions` with the
  controller's disposition, and the premise findings with their rulings.
- **Owners of the other sites**: the redteam seat template and its
  merge/readout text; the branch-reviewer template, its slot card and
  `requesting-code-review`; the task-reviewer and implementer templates,
  SDD's § Models and task loop, `very-small-lane.md`; brainstorming's spec
  contract, check 5, `lane-note.md`, `folded-lane-document.md` and
  `umbrellas.md` § Shape; the decision records whose position changes
  (`evidence-and-findings`, `model-roles-and-effort`, `the-spec`,
  `task-loop`, `branch-review`, `spec-campaign`, `routes`, `umbrellas`),
  `docs/upstream.md`'s Recommendations row, and the two backlog items.
- `agents/` is regenerated from the templates.

## Acceptance

- **A1.** The shared reference exists, and the four seat templates point
  to it; none restates its rules. One-time: a search for the reference's
  key phrases over `skills/` finds them only in the reference.
- **A2.** `flip-paths.md` states premise routing; the redteaming, SDD and
  `requesting-code-review` sites point to it. One-time search.
- **A3.** A redteam seat report with widened `Questions` still passes
  `conserve.py`. Standing: the existing conservation tests, unchanged,
  pass.
- **A4.** The task reviewer's model row and slot card name the default
  role, and no text still puts it on the bounded role. One-time search for
  "bounded role or better".
- **A5.** The request block is defined in the spec contract and in the
  lane-note, folded-document and umbrella shapes. One-time search.
- **A6.** Lane Fit carries the goal check; the branch-reviewer template
  carries the trace question; check 5 carries the trace. One-time search.
- **A7.** The task reviewer's deviation audit has a line per implementer
  concern, and SDD's `DONE_WITH_CONCERNS` handling no longer "notes" one.
  One-time search.
- **A8.** D9's three defects are gone. One-time check per item.
- **A9.** `docs/backlog/review-improvements.md` is deleted;
  `review-catch-and-implementers.md` keeps only the per-task-review
  follow-up; each edited decision record carries a Changes line. Standing:
  the decision-records test; one-time for the backlog.
- **A10.** The suite passes and the generated agents match their
  templates. Standing.
- **A11.** The landing states the skills' net word change from
  `tests/prose-budget.txt` and what was removed (umbrella U5). Why
  neither: a report, read by the operator.

## Mechanism sketches (advisory)

- The goal restatement is one line in the seat's report, before its
  findings; in Lane Fit, a second verdict beside WITHIN/EXCEEDS SHAPE.
- In a campaign, a premise finding's merged entry is `parked` with the
  ruling "decision ask to the operator", and the readout carries the ask.
- The task reviewer's concern line sits beside its routed-items line:
  one entry per concern, CONFIRMED (with the finding) or DISMISSED (with
  the reason).
- Deferred to implementation: the wording and placement of each pointer,
  and the ledger line form for a lead.
