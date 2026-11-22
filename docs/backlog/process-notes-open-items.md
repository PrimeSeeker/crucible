# Process notes: what its build left open

## Observation

- The seats a controller composes itself, with no template (a spec
  campaign's mechanical pre-pass, the adjudicator, the snapshot-blessing
  agent, a fresh look, an umbrella closing review's seats), take no
  sentence asking what was off in their instructions or tools. Whether
  they should was asked of the maintainer at the feature's close and not
  answered. The feature's lane note excludes three of them by name
  (`docs/crucible/2026-11-21-process-notes/note.md`, Out of scope); the
  record names five among others (`docs/decisions/operator-steering.md`
  § Process notes).
- The router's "With no notes made, say so only at a feature's close"
  sits outside "unless the operator's instructions say otherwise", and
  Finish step 2 names "or that no notes were made" as an alternative of
  its own (`skills/using-crucible/SKILL.md`, the Process notes paragraph;
  `skills/subagent-driven-development/references/finish.md`). Read
  literally, an operator whose instructions ask for no process notes
  still sees that line at each close with none. The branch review's last
  full read raised it, after the last fix wave it could ride.
- The same sentence reads as a limit more than an obligation. Finish
  step 2 is the one site that carries the obligation: a feature dropped
  before execution, and an umbrella's landing, say nothing when no notes
  were made.
- A seat's template tells it to write its report file "even where your
  host advises returning findings as text"
  (`skills/subagent-driven-development/references/seat-rules.md` § Report
  file required) and gives no reason. On the feature's own build, where
  seats were asked what was off, two reported that clash, each following
  the template. Once the seat sentence is installed, every seat may
  report it on every run, which would crowd out other remarks. The
  maintainer's view: the template should say why, so a seat reads it as a
  reasoned exception to the host's advice.

## Follow-up

- Put the first question to the maintainer again. If the answer is yes,
  state the duty once in the dispatch composition's return contract
  (`skills/subagent-driven-development/references/dispatch-composition.md`,
  item 5), about 15 words, in place of a list of exceptions.
- On the maintainer's word, since it narrows their ruling, bring the
  no-notes line under the same exception as the one line, for example
  "... an offer of the rest, or, with none made and only at a feature's
  close, that there are none", and drop Finish step 2's own alternative.
  Say there whether a close outside Finish carries the line.
- Give § Report file required its reason (the controller reads the file,
  not the reply, so its context stays small and the report survives
  compaction), then read in later runs whether seats still report the
  clash. Whether a reason also reduces seats ending without the write is
  untested (`docs/backlog/review-seat-report-write.md`).
