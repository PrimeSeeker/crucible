# Round record reference

The round directories under the feature workspace's `campaigns/` and the record each holds. Field lists are binding where their section does not say otherwise, and file and directory names are fixed: consumers depend on them.

Per-round directory contents:

```
round-NN/                     # NN zero-padded, sequential; round 0 = round-00
  record.md                   # the round record — format below
  seat-<id>.md                # one per seat report, raw, workspace-only (the
                              #   plan phase's pre-pass report is seat-p0.md)
  verifier.md                 # blind verifier report
  terminal-pass.md            # plan round-01 ONLY: its terminal pass's report
  second-read.md              # plan round-01 ONLY: its terminal pass's second read
terminal-pass/
  record.md
  pass.md                     # the terminal pass's report
  second-read.md              # the pass's second read, if one runs: the spec
                              #   campaign's last report
```

## Round record format

`record.md` in each round directory, one per round. All bookkeeping —
stop-rule inputs, cap arithmetic, parked and deferred minors,
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

**Where dispatch items go.** A run predicate's command and output go under
its item in `Fix list`. A plan-half or pre-pass re-run (the plan record, the folded lane) goes in the
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

4. **Panel roster** (`## Panel roster`) — per seat: seat id, model, assigned
   lens and its `seat-<id>.md` file.

5. **Merged finding list** (`## Merged finding list`) — entries only: one
   list item per finding, opening `- <id> <SEVERITY>` (BLOCKER, MAJOR or
   MINOR, the only vocabulary), its continuation lines indented:
   originating seat(s), an `origins:` element (below), one-line
   substance, the `UNVERIFIED` tag where staked without evidence, and one
   `disposition: <value>` element — `applied` | `partly-applied` |
   `parked` | `rejected` | `deferred-to-implementation` | `deferred-minor`
   — plus the ruling a partly-applied, parked or rejected entry owes and
   an `UNVERIFIED` entry's verification outcome (`crucible:redteaming` § Merge and finding hygiene).
   An entry closing a repeat of an earlier round's `deferred-minor` takes
   `deferred-minor` too and names that round and entry; SDD's Setup seeds
   the two once.
   An entry merged from a premise finding carries the label `premise`
   after its severity, `- F4 MAJOR premise`; its route is
   `skills/redteaming/references/flip-paths.md` § Premise findings.

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

   **Deferral:** which findings take `deferred-to-implementation` or
   `deferred-minor` is ruled in `crucible:redteaming` § Merge and finding
   hygiene, and what a deferral's fix items land in `crucible:redteaming`
   § Fix application and blind verification; a deferred entry keeps its
   row.

   **Question dispositions** (`## Question dispositions`, after the merged
   finding list): every question a seat report raises, by its id
   `<seat-id>-q<n>`, is answered (with the answer), carried to readout (the
   question goes to the operator in this round's readout, quoted
   verbatim), rejected (with a ruling) or adopted (an improvement riding
   this round's fix wave, with the fix item that carries it); which
   questions are always carried, and where a question is never adopted,
   is in `crucible:redteaming` § Merge and finding hygiene.

6. **Fix list** (`## Fix list`) — enumerated fix items, each naming the
   finding id(s) it resolves, or the question id `<seat-id>-q<n>` of an
   adopted improvement it carries: the blind verifier's sole mandate input (fix
   list + diff, never rationale). Which findings and items a fix list takes
   is ruled in `crucible:redteaming` § Fix application and blind
   verification. **Restating sites** (binding): each item
   also names every other artifact site restating the content it changes,
   found by the propagation sweep run before the list freezes, and for an
   item that adds or changes a rule each site its trace finds
   (`crucible:redteaming` § Fix application and blind verification), or its
   one site where the content is stated once.

7. **Verifier block** (`## Verifier block`) — pointer to `verifier.md`;
   landed/not-landed verdict per fix item; the nothing-outside-the-list-moved
   verdict; a verdict per delta claim (each new "the code does X" claim the
   wave introduced): TRUE or FALSE with evidence, or not checked with the
   reason, and for each claim not checked, the controller's own check and
   its outcome.

8. **Round readout** (`## Round readout`) — the readout as delivered to the
   operator, compact, with the items and in the form `crucible:redteaming`
   § Round readout defines.

   **Trace** (record only, never delivered): the field ends with a part
   opened by a line `Trace:`, after the readout, holding the bookkeeping
   other readers need —
   - in a numbered round record and the plan record, each decision ask's
     merged-list ids, the entries it turns on, which the terminal pass
     reads;
   - in a numbered spec-campaign round record only, beside each mechanism
     the overturn item answers, the ids of the seats whose forecasts named
     it as reasonably expected to be overturned.

**Special records** — field sets and reachable states (a state outside a
record's subset is skipped by definition):

- **Round-00:** fields 1, 2, 6 and 8 plus `## Claim table` (claims about the
  code, or with no code baseline about the inputs, → TRUE/FALSE with
  evidence). Its findings and the fixes applied before
  round 1 are in its fix list, each finding the list does not take
  named after its items with its disposition. It has no merge and so no question
  dispositions: the round-0 agent's questions are answered in its readout,
  under the panel's rule for which are always carried.
  States: `dispatched → returned → fix-applied → readout`.
- **Terminal pass** (`terminal-pass/record.md`): fields 1, 2, 6 and 8, with
  a pointer to `pass.md` in its preamble, and `## Deferred minors`, the
  pass's `deferred-minor` findings, a second read's included, each with
  its disposition. Field 6 is present only
  when the pass's findings trigger the at-most-one further fix wave; no
  second wave is recordable. Field 8, the close, is recorded before any
  second read and delivered after it, its corrections added. States:
  `dispatched → returned → readout`, with the wave
  `dispatched → returned → fix-applied → verified → readout`, or with a
  record-only read `dispatched → returned → verified → readout`;
  `verified` means `second-read.md` is on disk.
- **Plan-phase record** (`campaigns/plan/round-01/record.md`): the plan
  phase's only record, with fields 1–8 and `## Terminal pass` — the pass's
  `Record corrections: <N>` outcome, any sanctioned repair, the close
  delivered after the pass, any second read, the pass's `deferred-minor`
  findings, and the final check before `confirmed`. The quorum block is kept for lost
  seats; no cap arithmetic applies. States: the
  full sequence through `confirmed`, a sanctioned repair re-advancing the
  record through `fix-applied → verified` before `confirmed` is written
  last. The round directory also holds the pre-pass's `seat-p0.md` (a seat
  report for every purpose), `terminal-pass.md` and any `second-read.md`. A
  flagged correction is a decision ask to the operator.
