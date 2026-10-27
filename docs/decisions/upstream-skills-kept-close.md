# Upstream skills kept close

## Decision

Two craft skills keep superpowers' text (v6.2.0) and change it only
where it names one host's mechanics or crucible's own machinery, points
at an upstream skill crucible folded, or prints a secret, where a
shipped script or example needs its platform limit stated, where
upstream's text is defective, and where a later upstream release
improves it. A third,
receiving-review, rewrites upstream's skill for feedback from outside
crucible's loops, keeping its core.

**dispatching-parallel-agents** is upstream's text except step 3: start
every independent agent before waiting for any of them, through the
host's parallel fan-out operation, starting the rest as capacity frees;
tasks that are not independent run one at a time, whatever the host
permits; and its review steps, where each agent's diff is checked, not
only its summary, from upstream's later verification-before-completion.
It carries none of crucible's seat machinery. Redteaming starts
its seats and leaves the rest of the fan-out mechanics to it
(`crucible:redteaming § Panels`).

**systematic-debugging** is upstream's text except four lines of its
`SKILL.md`, a note in each of two references, and root-cause-tracing's
script invocation and dead-end edges. Test-first reads "Write
the failing test before the fix; where no test or script can reproduce
the bug, say why", with a pointer to
`skills/subagent-driven-development/writing-good-tests.md`; the verify
step asks for evidence before done without naming an upstream skill; and
the example's two lines that printed a secret's value test only for its
presence. `skills/systematic-debugging/root-cause-tracing.md` says
`find-polluter.sh` is POSIX/Bash-only and what to do on Windows instead,
runs it through `bash` by its path from the plugin root (upstream's `./`
form resolved against the user's project), and sends a trace that
dead-ends to instrumentation and then to `SKILL.md`'s "No Root Cause"
section, where upstream's two diagrams disagree (one fixes at the symptom
point, the other forbids it);
`skills/systematic-debugging/condition-based-waiting.md` says its example
is a pattern to copy, not a runnable script. The framing and the "your
human partner" sections stay.

**receiving-review** takes the place of upstream's receiving-code-review,
for review feedback from outside crucible's own loops: the operator, a
pull request's reviewers and bots, the findings
`crucible:requesting-code-review`'s standalone mode hands back, any other
reviewer. Task review, the branch-review loop and redteam campaigns keep
their own rules. It keeps upstream's core: read every item first and
restate each in your own words, an item you cannot restate counting as
unclear, and ask about every unclear item before implementing any; verify
each item against the codebase; say when one cannot be verified; the
YAGNI check on "do it properly"; push back with evidence, naming the
tension where pushback is uncomfortable; correct a wrong pushback in one
line; reply in the comment's own thread; implement one item at a time,
testing each. It departs from upstream in three ways: the operator's
feedback is checked like anyone's, and the operator rules after the
pushback; an outside reviewer never rules, so a disagreement that
survives the evidence, or an item that conflicts with an earlier operator
decision, becomes a decision ask; and feedback that is new scope goes to
`crucible:brainstorming` (`crucible:receiving-review § Who rules`). It
drops upstream's anti-gratitude rules and its role-play examples. Where
pull-request feedback is handled after a branch finishes:
`docs/decisions/records-and-workspace.md`.

## Why

### Generic craft stays upstream's

Fanning out agents and finding a root cause are craft any project uses,
not crucible's process, and each line crucible changes in upstream's
text is a difference to carry past later upstream releases. So on
2026-10-08 both skills went back to upstream's text, changed only where
a line could not serve crucible's two hosts as written, named a folded
skill, or printed a secret. (Basis: judgment, accepted by the
maintainer.)

Upstream's step 3 reads "Issue all three subagent dispatches in the same
response — they run in parallel" and "Multiple dispatch calls in one
response = parallel execution"
(`superpowers/skills/dispatching-parallel-agents/SKILL.md` at v6.2.0):
one host's mechanics, while Codex starts agents differently. The
claude-ism scanner flags that phrasing in shipped text
(`docs/decisions/crucible-suite.md`). The same change removed what
crucible had added: a pointer to the dispatch reference, a requirement
that every fan-out carry the dispatch composition, which was built for
crucible's own seats, an instrument sentence, a line about crucible's
own repository, and two anti-patterns drawn from a single run. (Basis:
external, for upstream's text; judgment, accepted by the maintainer.)

Upstream's systematic-debugging sends test-first and verification to its
test-driven-development and verification-before-completion skills, which
crucible folded into its seats' rules (`docs/upstream.md`). Outside
subagent-driven development there is no Decision Log to record a skipped
test in, so the line became "if you skip it, say why" (2026-10-08); on
2026-10-15 the skip was narrowed to an observable condition, a bug no
test or script can reproduce, which the maintainer confirmed. (Basis:
judgment, accepted by the maintainer.)

The example's `env | grep IDENTITY` printed the variable's value, and so
did `${IDENTITY:+SET}${IDENTITY:-UNSET}`, whose second expansion yields
the value whenever it is set: with `IDENTITY=secret`, bash prints
`SETsecret`. A branch review found the second. (Basis: measured.)

The two reference notes date from 2026-08-15, when each script the
skills ship was sorted by whether a workflow step waits on it: a
diagnostic the operator runs by hand may stay in its own language if its
platform limit is stated where it is invoked, and the TypeScript file is
an example to copy, not a script to run. (Basis: judgment, accepted by
the maintainer.)

The "your human partner" sections stay: a session's human partner is the
operator (`skills/using-crucible/SKILL.md`), and the implementer, which
has none, reports BLOCKED wherever the skill sends it to one
(`skills/subagent-driven-development/implementer-prompt.md`). (Basis:
judgment, accepted by the maintainer.)

### Receiving review

The first design dropped upstream's receiving-code-review: "No human code
review in this philosophy" (2026-08-06). That reason never covered the
pull requests finishing still opens, whose reviewers and bots send
feedback, so on 2026-10-08 the skill returned for feedback from outside
crucible's loops. (Basis: judgment, accepted by the maintainer.)

Upstream trusts the human partner's feedback ("Trusted - implement after
understanding", `superpowers/skills/receiving-code-review/SKILL.md` at
v6.2.0). Crucible checks it like anyone's: the operator steers without
reading code (`docs/decisions/operator-steering.md`), so a wrong premise
about the code is caught only where the agent checks the feedback against
it. The authority stays the operator's: the operator rules after the
pushback, and an outside reviewer, who answers to no one in the session,
never rules. Replies carry content, what changed or the evidence behind a
disagreement, in place of upstream's list of phrases never to write.
(Basis: judgment, accepted by the maintainer, 2026-10-08.)

### The restate step

Upstream's response pattern has an UNDERSTAND step, "Restate requirement
in own words (or ask)" (`superpowers/skills/receiving-code-review/SKILL.md`
at v6.2.0). Crucible's 2026-10-08 rewrite left it out with no recorded
reason, and it returned on 2026-10-20: asking catches only what the agent
knows it did not understand, and restating also catches what it misread.
An agent's call, which the maintainer left to it ("Unsure how would it
play out, your call"); its effect is unmeasured. (Basis: judgment,
accepted by the maintainer.)

## Rejected

- **Crucible's seat machinery in dispatching-parallel-agents**: the
  skills that start crucible's seats carry the dispatch composition
  themselves; generic fan-out does not need it.
- **Upstream's one-response dispatch wording**: one host's mechanics
  (§ Why).
- **Implementing the operator's feedback unchecked**: a wrong premise
  about the code would go uncaught (§ Why).
- **A list of phrases never to write in replies**: replies carry content
  instead.

## Changes

- 2026-10-27: dispatching-parallel-agents checks each agent's diff,
  not only its summary, taken from a later upstream release; the
  Decision allows such an improvement.
- 2026-10-27: root-cause-tracing runs `find-polluter.sh` through `bash`
  from the plugin root, and the script is committed executable: its `./`
  form failed on every POSIX host. A dead-end trace goes to
  instrumentation, then to "No Root Cause", resolving upstream's two
  contradicting diagrams (still contradicting at v7.0.1).
- 2026-10-20: receiving-review restates each item in the agent's own
  words before implementing, an item it cannot restate counting as
  unclear: upstream's step, restored.
- 2026-10-15: systematic-debugging upstream's but for four `SKILL.md`
  lines (test-first skipped only for a bug no test or script can
  reproduce, the verify step naming no upstream skill, two secret lines
  as presence checks) and the platform notes in two references.
- 2026-10-08: dispatching-parallel-agents upstream's again but for step
  3, every independent agent started before waiting, through the host's
  fan-out operation.
- 2026-10-08: receiving-review for feedback from outside crucible's
  loops, upstream's core kept, the operator's feedback checked like
  anyone's, the operator ruling and an outside reviewer never.
