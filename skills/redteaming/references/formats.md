# Crucible formats reference

What a controller or seat writes and reads, defined once so writers and
readers are built against one text: the feature workspace, the round record,
the feature folder and the design digest. Provisioning the workspace and
finding the feature folder are steps stated here;
`skills/redteaming/scripts/conserve.py` checks a round's merge, and its
`--help` is its contract.

Field lists are binding where their section does not say otherwise, and file
and directory names are fixed: consumers depend on them. Content marked *advisory* may be refined by its implementer
with a logged decision.

## Feature workspace root and layout

**Root convention:** one workspace per feature at

```
<repo>/.crucible/<feature-slug>/
```

where `<repo>` is the root of the checkout the controller session works in
(typically the feature worktree) and `<feature-slug>` matches
`[a-z0-9]+(-[a-z0-9]+)*`; the slug also names the feature folder (§ Feature
folder).

**Self-ignition:** whoever creates `.crucible/` first also writes
`.crucible/.gitignore` containing exactly `*`. No host
`.gitignore` is ever edited: host gitignores are operator-owned.

**Provisioning (binding):** the step that creates a feature's workspace.
Re-running it on an existing workspace changes nothing.

1. Create `.crucible/<feature-slug>/` at the root of the checkout
   (`git rev-parse --show-toplevel`).
2. If `.crucible/.gitignore` is absent, write it holding the single line
   `*`, as UTF-8, with your file-writing tool and never a shell redirect:
   Windows PowerShell 5.1's `>` writes UTF-16LE, which git does not read.
   An existing one is never overwritten, whatever it holds.
3. From the checkout's root, run
   `git check-ignore -q .crucible/<feature-slug>/probe` (the path need
   not exist). Exit 0 confirms the workspace is ignored; report any other
   result to the operator. Check a file path, never the directory: against
   a UTF-16LE `.gitignore` the directory form, `.crucible/<feature-slug>/`,
   still exits 0.

Gitignored files do not propagate across worktrees, so the workspace lives in
one checkout: dispatch prompts pass its absolute path, and anything agents in
*other* checkouts must read — the spec, the plan — is committed to the repo,
never workspace-only. Nothing in the workspace is committed by any step of
crucible's flow.

**Layout** (the spec campaign, the plan phase and SDD share one
workspace):

```
<repo>/.crucible/
  .gitignore                  # exactly "*" — self-ignition
  <feature-slug>/             # the feature workspace
    brainstorm-decisions.md   # brainstorm decision record, the gate entry
                              #   included (crucible:brainstorming)
    digest.md                 # design digest (format below)
    campaigns/
      spec/                   # the spec campaign
        round-00/             # round 0 mechanical pre-pass (consumes no cap round)
        round-01/ ... round-NN/
        terminal-pass/        # terminal pass (consumes no cap round)
      plan/                   # the plan phase: round-01 only, no round-00 and
                              #   no terminal-pass/ — its pass reports into round-01/
    sdd/                      # SDD execution records (internal shape advisory)
      ledger.md
      reports/
      branch-review/          # pass-<k>.md per full-scope pass, pass-<k>-r<R>.md
                              #   for a replacement seat's
    scratch/                  # what read-only agents build or run to check
                              #   claims, one subdirectory per report;
                              #   deleted with the workspace
```

The other report names under `sdd/` — review, re-review, fix and adjudication
reports — are fixed in `crucible:subagent-driven-development` § Finish.

**Later operator rulings enter the decision record (binding).** Every
operator ruling on a decision ask after the brainstorm — in a campaign, the
plan phase or execution — is also entered in `brainstorm-decisions.md`, in
that record's entry form (`crucible:brainstorming` § Workspace provisioning
(brainstorm exit)) and with its status, beside wherever its own phase
records it.

Per-round directory contents:

```
round-NN/                     # NN zero-padded, sequential; round 0 = round-00
  record.md                   # the round record — format below
  seat-<id>.md                # one per seat report, raw, workspace-only (the
                              #   plan phase's pre-pass report is seat-p0.md)
  verifier.md                 # blind verifier report
  terminal-pass.md            # plan round-01 ONLY: its terminal pass's report
  second-read.md              # plan round-01 ONLY, after a sanctioned repair
terminal-pass/
  record.md
  pass.md                     # the terminal pass's report
  second-read.md              # only after the one further fix wave: the spec
                              #   campaign's last report
```

**A report the controller saved carries a mark (binding).** Every report
file an instrument or seat owes — a round's `seat-<id>.md`, `verifier.md`,
`terminal-pass.md`, `pass.md` and `second-read.md`, and the reports SDD's
seats write under `sdd/` — is written by its author. The controller writes
one itself in two cases only: the host refused the write and the seat
returned the report as text; or the seat returned it as text without writing
it or reporting a refusal, and one resume left no file. It then writes the
returned text unchanged under a first line saying the controller saved it
and why, so whoever reads the workspace can tell the seat's text from text
the controller transcribed. The `sdd/` files the controller writes by rule —
the very-small lane's `wave-<n>-fix.md`, inline mode's report — are its own
and carry no mark.

**Lifecycle** (binding): provisioned at brainstorm exit; lives until one of
three ends — SDD Finish, an umbrella's landing (an umbrella never reaches
SDD), or feature abandonment. At each, the controller deletes
`.crucible/<feature-slug>/` and nothing else (at Finish, after SDD Finish's
record checks; at an umbrella's landing, before it lands, in the order
`skills/brainstorming/references/umbrellas.md` § Landing gives) and reports
to the operator anything it could not delete. No orphan workspaces. Workspace lost mid-feature: the in-flight phase restarts
from the committed spec or plan and `git log`; the session transcripts hold
the lost records if they are needed.

## Round record format

`record.md` in each round directory, one per round. All bookkeeping —
stop-rule inputs, cap arithmetic, merge conservation, parked minors,
quorum status — is computed from these records. What the controller writes
in them is under record hygiene (`crucible:redteaming` § Merge and finding
hygiene).

**Sections.** The record is written for the agents that read it — the
controller rehydrating, the stop rule, the blind verifier, the terminal
pass: its field layout and section titles are guidance, and the process
rules its fields state bind. Fields 1–2 are the preamble, before the first
`##` heading; every later field is a `##` section under the title its field
names. Any record may also carry
`## Rulings and corrections`: dated entries added after the round closed —
operator rulings on its decision asks, corrections to the record.

**Where dispatch items go.** A dispatch's tree-check readings go in its own
section: `Panel roster` for seats, `Verifier block` for the verifier,
`Terminal pass` for the plan record's pass, the terminal-pass record's
preamble for its pass, round 0's preamble for its pre-pass. A run
predicate's command and output go under its item in `Fix list`. A plan-half
or pre-pass re-run (the plan record, the folded lane) goes in the
`Verifier block` of the record whose wave it follows, or under its
`Fix list` where that record has no verifier block (round 0, the
terminal-pass record); one after a sanctioned plan-phase repair goes under
the plan record's `Terminal pass`, with the repair.

Fields, in order:

1. **Header** — phase (`spec` | `plan`), round number, feature slug, date,
   and the artifact reviewed, written `<path> @ <rev>` (a commit hash or a
   stated revision marker; backticks optional around either part): the one
   revision every seat in the round reads.

2. **State line** (binding) — a single line `state: <value>`, where
   `<value>` is exactly one token from the vocabulary, which is, verbatim:

   `dispatched → returned → merged → fix-applied → verified → readout`

   The plan record alone appends one further token,
   `… → readout → confirmed`, written after the plan phase's terminal pass
   has graded the recorded readout; no other record carries it.

   States advance strictly in order, each written only after its phase's
   outputs are on disk. Numbered rounds (`round-01..NN`) skip none; the
   special records advance through their reachable subsets (below), a state
   outside a record's subset skipped by definition, never a gap. Meanings:
   - `dispatched` — seats launched; roster recorded.
   - `returned` — every dispatched seat's report on disk, or its loss
     recorded and resolved (field 3).
   - `merged` — merged finding list with dispositions written.
   - `fix-applied` — the recorded fix list has landed in the artifact.
   - `verified` — blind-verifier report on disk, every item confirmed landed.
   - `readout` — round readout recorded; the round closes once it is
     delivered (`crucible:redteaming` § Round readout).
   - `confirmed` (plan record only) — the terminal pass's report, and any
     second read, on disk and the phase's final check done; written last,
     after any sanctioned repair has re-advanced the record through
     `fix-applied → verified`.

   Rehydration resumes from this line, by the rule in `crucible:redteaming`
   § Inputs and state.

3. **Quorum block** (`## Quorum block`) — seats dispatched, seats returned,
   and *every* lost or crashed seat by id with what happened and its
   resolution: `topped-up` (re-dispatched, report present) or the round
   marked degraded, on one line (binding; the cap arithmetic reads it):

   ```
   degraded: yes | no
   ```

   A round that lost any dispatched seat and was not topped back up is
   `degraded: yes`.

   **Conservation line** (binding; every numbered panel round, at merge
   time): the reconciliation of raw seat findings against the merged list,
   on its own line in this block —

   ```
   conservation: <raw seat findings> → <merged entries>; <what accounts for the rest>; <verdict>
   ```

   — the three-part arithmetic, then `<verdict>`, the latest result of the
   conservation check (`crucible:redteaming` § Merge and finding hygiene):
   `clean` where it exits 0, or on exit 1 its printed `unaccounted:` line
   verbatim. **A recorded `unaccounted:` element is written on a single line**
   (binding): the check reads it line by line, so an id wrapped onto the
   next line would count as accounted. Conservation is a per-round step
   recorded here, never as a bullet in the merged finding list.

4. **Panel roster** (`## Panel roster`) — per seat: seat id, model, assigned
   lens and its `seat-<id>.md` file; and the seats' tree-check readings.

5. **Merged finding list** (`## Merged finding list`) — entries only: one
   list item per finding, opening `- <id> <SEVERITY>` (BLOCKER, MAJOR or
   MINOR, the only vocabulary), its continuation lines indented:
   originating seat(s), an `origins:` element (below), one-line
   substance, the `UNVERIFIED` tag where staked without evidence, and one
   `disposition: <value>` element — `applied` | `partly-applied` |
   `parked` | `rejected` | `deferred-to-implementation` — plus the ruling a
   partly-applied, parked or rejected entry owes and an `UNVERIFIED` entry's
   verification outcome (`crucible:redteaming` § Merge and finding hygiene).
   An entry merged from a premise finding carries the label `premise`
   after its severity, `- F4 MAJOR premise`: the stop rule reads it as a
   decision ask, not by its severity.

   **Origins element** (binding): every entry names the per-seat finding
   ids it accounts for —

   ```
   origins: <seat-id>-<n>, <seat-id>-<n>
   ```

   — one id per raw seat finding it absorbs, merged into it or closed
   against it as a duplicate; the terminal pass finds seat findings through
   it. A seat finding's id is the one its seat report's finding header
   carries (`skills/redteaming/seat-prompt.md`): `<seat-id>` is the seat's
   `seat-<id>.md` identity (`p0` for the plan phase's pre-pass) and `<n>`
   numbers its findings from 1. An entry with its elements on one line:

   ```
   - F3 MAJOR (seat-s2, seat-s3) — origins: s2-4, s3-1 — the cap arithmetic
     is never derived from the records — disposition: applied
   ```

   **Deferral:** which findings take `deferred-to-implementation` is ruled
   in `crucible:redteaming` § Merge and finding hygiene, and what their fix
   items land in `crucible:redteaming` § Fix application and blind
   verification; a deferred entry keeps its row.

   **Question dispositions** (`## Question dispositions`, after the merged
   finding list): every question a seat report raises, by its id
   `<seat-id>-q<n>`, is answered (with the answer), carried to readout (the
   question goes to the operator in this round's readout), rejected (with
   a ruling) or adopted (an improvement riding this round's fix wave, with
   the fix item that carries it; `crucible:redteaming` § Merge and finding
   hygiene).

6. **Fix list** (`## Fix list`) — enumerated fix items, each naming the
   finding id(s) it resolves, or the question id `<seat-id>-q<n>` of an
   adopted improvement it carries: the blind verifier's sole mandate input (fix
   list + diff, never rationale). **Restating sites** (binding): each item
   also names every other artifact site restating the content it changes,
   found by the propagation sweep run before the list freezes
   (`crucible:redteaming` § Fix application and blind verification), or its
   one site where the content is stated once.

7. **Verifier block** (`## Verifier block`) — pointer to `verifier.md`;
   landed/not-landed verdict per fix item; the nothing-outside-the-list-moved
   verdict; a verdict per delta claim (each new "the code does X" claim the
   wave introduced): TRUE or FALSE with evidence, or not checked with the
   reason, and for each claim not checked, the controller's own check and
   its outcome; and the verifier's tree-check readings.

8. **Round readout** (`## Round readout`) — the readout as delivered to the
   operator, compact, with the items `crucible:redteaming` § Round readout
   defines: key findings, every rejected, parked or partly-applied
   BLOCKER/MAJOR named with its ruling; technical calls; decision asks; the
   round's `deferred-to-implementation` count; the digest-update note; and,
   in a numbered spec-campaign round with no BLOCKER other than a premise
   finding, whether the round
   drove structural change and on what basis. The delivered readout carries
   no internal id — merged-list, seat-finding or question id — and no line
   counts.

   **Trace** (record only, never delivered): the field ends with a part
   opened by a line `Trace:`, after the readout, holding the bookkeeping
   other readers need —
   - in a numbered round record and the plan record, each decision ask's
     merged-list ids, the entries it turns on, which the terminal pass
     reads;
   - in a numbered spec-campaign round record only, the wave's line counts:
     the lines it added to the artifact and the lines it removed, as git
     counts them between `<base-rev>`, the revision the round reviewed
     (field 1), and `<head-rev>`, the revision the wave landed at —

     ```
     git diff --numstat <base-rev> <head-rev> -- <artifact-path>
     ```

     — two numbers, added then removed, with no justification prose. Their
     net is the signal the right-sizing re-seat trigger judges
     (`crucible:redteaming` § Panels); where the wave was not committed, the
     trace records the counts as not taken.

**Special records** — field sets and reachable states (a state outside a
record's subset is skipped by definition):

- **Round-00:** fields 1, 2, 6 and 8 plus `## Claim table` (baseline claims
  → TRUE/FALSE with evidence). Its findings and the fixes applied before
  round 1 are in its fix list. It has no merge and so no question
  dispositions: the round-0 agent's questions are answered in its readout.
  States: `dispatched → returned → fix-applied → readout`.
- **Terminal pass** (`terminal-pass/record.md`): fields 1, 2, 6 and 8, with
  a pointer to `pass.md` in its preamble. Field 6 is present only when the
  pass's artifact findings trigger the at-most-one further fix wave, whose
  second read lands as `second-read.md`; no second wave is recordable.
  States: `dispatched → returned → readout`, or with the wave
  `dispatched → returned → fix-applied → verified → readout`, `verified`
  meaning the second read is on disk.
- **Plan-phase record** (`campaigns/plan/round-01/record.md`): the plan
  phase's only record, with fields 1–8 and `## Terminal pass` — the pass's
  `Record corrections: <N>` outcome, any sanctioned repair and second read,
  and the final check before `confirmed`. The quorum block is kept for lost
  seats; no cap arithmetic applies, since the phase never loops. States: the
  full sequence through `confirmed`, a sanctioned repair re-advancing the
  record through `fix-applied → verified` before `confirmed` is written
  last. The round directory also holds the pre-pass's `seat-p0.md` (a seat
  report for every purpose), `terminal-pass.md` and any `second-read.md`. A
  flagged correction is a decision ask to the operator.

## Feature folder

This section is the binding definition of where a feature's committed
documents live — its spec and its plan — and skill prose points here rather
than restating it.

**Feature folder (binding):** each feature's committed documents live
together in one tracked directory of the target repo, the feature's
*feature folder*:

```
<root>/<YYYY-MM-DD>-<feature-slug>/
```

`<root>` is `docs/crucible` by default; a root the project's instruction
files name overrides this default. The date is the day brainstorming first
writes the spec, before provisioning; `<feature-slug>` is the workspace slug
(§ Feature workspace root and layout).

**Files named by role (binding):** the folder carries the slug and the date,
so a filename carries only its role.

- Exactly one *current* spec, named by its kind: `design.md` (standard
  route), `folded.md` (the folded spec+plan), `note.md` (the very-small lane)
  or `umbrella.md` (an umbrella, `skills/brainstorming/references/umbrellas.md`).
- `plan.md`, on the standard route only.
- A route that replaces a spec keeps the predecessor in place as the
  forensic record and writes the successor into the same folder: a supersede
  successor takes a numeric suffix (`design-2.md`, `plan-2.md`, …); an
  unfold leaves `folded.md` beside its `design.md` and `plan.md` successors,
  and the very-small lane's upgrade hatch leaves `note.md` beside them.
- Other feature-scoped documents may live in the folder under descriptive
  names.

**Birth and resolve; a slug names one feature (binding):** two steps find
a feature's folder, and both match a directory under `<root>` named
exactly `YYYY-MM-DD-<feature-slug>`: a date of that shape, then the whole
slug, so slug `diet` never matches `2026-09-27-cost-diet`. A
`*-<feature-slug>` glob is not that match: it also matches
`2026-10-11-bar-<feature-slug>`.

- **Birth** — brainstorming, when it first writes the spec. List
  `<root>`. Where no directory there is named exactly
  `YYYY-MM-DD-<feature-slug>`, create `<root>/<today>-<feature-slug>/` (local
  date). Where one is, refuse and tell the operator: a new feature
  never resolves into a finished feature's folder, so it takes a new slug.
- **Resolve** — every other consumer: a resumed brainstorm, the plan, a
  successor spec, dispatches. Find the one directory under `<root>`
  named exactly `YYYY-MM-DD-<feature-slug>`, creating nothing. None, or more
  than one, is reported to the operator.
- Nothing but the birth creates a feature folder, so a feature never has a
  second home.

## Design digest format

`digest.md` at the feature-workspace root. Operator-facing collation for
major designs. Audience: the operator as tech analyst — analyst language,
decision asks with recommendations; no step requires reading spec, plan,
code or diffs, and a decision ask may quote the few lines it turns on.

**Derivation rule (binding):** derived, never independently authored.
Exactly three source classes, and every entry cites its source record:

1. the brainstorm dialogue's decision record;
2. round readouts and their decision asks;
3. scoped-amendment decision-ask records (so the digest legally tracks
   mid-execution flips).

Material spec internals reach the digest by being included in a readout —
never by side-authoring against the spec.

Sections:

- `## Decisions` — each: the decision, the trade-off it resolves, status,
  source pointer (which readout or record). The status is `open`,
  `accepted` or `firm`: `accepted` is the default for any approval, a
  "+", an "OK" or a "your call" included, and means "this until new
  evidence arrives"; `firm` is recorded only on the operator's explicit
  word, never inferred from an approval.
- `## Positions flipped` — what flipped, why, and where (source pointer).
- `## Open judgments` — pending decision asks, each with its recommendation.

Updated at round closes (the round readout names the digest update).
