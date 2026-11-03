# Cut patterns for this corpus

Read this before each unit. The patterns are ordered by estimated share of the text. Every "before" is corpus text; `…` marks an omission. Apply the decision list first: these patterns tighten text and never retire a rule.

## Patterns

**1. Clause-stacked conditionals.** Rule: three or more cases in one sentence become condition → action fragments, a list or a table. (Share: about 10–15% of controller text; samples cut 27–42%.)
Before (subagent-driven-development SKILL.md): "Executing defective or superseded plan text produces reviewable-but-wrong work, so such text found mid-execution — a BLOCKED escalation of a defective plan, an operator's answer that changes plan text, an adjudication or a ruling of yours that patches the plan, an operator's ruling on a premise finding given during the task loop — takes a flip path, …"
After: "Defective or superseded plan text found mid-execution (a BLOCKED escalation; an answer, adjudication or ruling that patches the plan; a premise ruling during the task loop) takes a flip path."

**2. Citation weight.** Rule: use the shortest citation the convention allows. Headings carry no subtitles. Never cite what the reader already holds. (Share: 6.3% of characters; a path is one word but 10–17 tokens.)
Before (task-loop.md): "take the receiving step of `skills/brainstorming/references/umbrella-children.md` § Under an umbrella: binding changes and late splits first, so a binding change it takes in falls before BASE"
After: "first take the receiving step of `skills/brainstorming/references/umbrella-children.md` § Under an umbrella, so a binding change it takes in falls before BASE" (the heading's subtitle dropped; C7(4), bare basenames, is rejected: a cross-skill reference keeps its full path, and a file's second mention of the same reference may say "that file" or the basename where unambiguous in context).

**3. Point or state, never both; never a pointer longer than the rule.** (Share: about 3–5%.)
Before (very-small-lane.md): "the operator's answer is recorded where `skills/redteaming/references/formats.md` § Feature workspace root and layout sends it."
After: "the answer is entered in `brainstorm-decisions.md`."

**4. Restating beside a splice.** Rule: a template never restates a section it splices. It states only this seat's consequence: the label it gets, or the verdict it fails. (Share: about 3–5% of rendered seat text, paid on every dispatch.)
Before (implementer-prompt.source.md): "- What the change ships follows § What shipped work carries." directly above "[[include What shipped work carries]]"
After: the include line alone.

**5. Why-text and anti-loophole clauses.** Rule: give the rule, with at most one clause of why. Never argue against a misreading no record shows. The reasons go in docs/decisions. (Share: about 1.5–4%.)
Before (terminal-pass-prompt.source.md): "The test is materiality, and it is timing-free in both directions: a correction never flags merely because a close decision happens to be pending (this pass runs at the phase's close by construction), and never fails to flag merely because the operator has not yet ruled, or ruled the same way afterwards on the corrected record."
After: "Materiality is the whole test: a pending close never flags by itself, and a ruling, made or not, never unflags."

**6. Controller text restating a card or template.** Rule: check the instrument's card and template before writing inputs, models or seat rules into skill text. Point where they already carry it. (Share: about 3% of controller text.)
Before (redteaming SKILL.md): "the blind verifier runs on the bounded role and never lower — checking a fix list against a diff is a bounded task, and its mandate is unchanged by the tier."
After: "Seat models: each card's Model line."

**7. Re-defining a defined term.** Rule: one definition per term, and every other site names it. This covers what binds and the umbrella chain. (Share: about 2.5%.)
Before (dispatch-composition.md): "plus one line naming what the pin makes binding: its Constraints & invariants, any preamble convention it declares binding and the decisions it records as the operator's firm preference; and, where its preamble carries an `Umbrella:` line, … up the chain, each read in the seat's worktree at the revision its review reads."
After: "plus one line naming what binds there (§ What binds)."

**8. Rationalization rows that restate the body.** Rule: keep only the rows the decision list keeps (C16), each with a one-clause Reality. (Share: about 2%.)
Before (finishing SKILL.md): "| \"`branch -d` refused — I'll use -D\" | `-d` refuses because the commits never reached the base. `-D` throws them away. Find out why the merge did not take. |"
After: "| \"`branch -d` refused — I'll use -D\" | The merge did not take; `-D` throws the commits away. |"

**9. Case lists and riders under a quantifier.** Rule: state the rule over its whole class and name a member only where it is an exception. Give a scope rider once, where the rule is defined. (Share: about 1.5–2%.)
Before (fix-application.md): "That holds for every fix list — round 0's, a numbered round's, the plan phase's, the spec terminal pass's follow-up wave's — and for a plan-phase repair."
After: "It holds for every fix list and plan-phase repair."

**10. Formatting overhead.** Rule: bold only a defined term or a read trigger, never a whole sentence. No alignment padding. Write every paragraph and every list item on one line, never hard-wrapped (C8: measured 4–5% of tokens raw, 12–13% where the Read tool numbers each line). (Share: about 1.4% of tokens.)
Before (redteaming SKILL.md): "**Before you size, staff or dispatch any panel round or plan-phase seat, and whenever a dispatched seat is lost, read `skills/redteaming/references/panels.md` in full.**"
After: the same words, bolding only "**read `skills/redteaming/references/panels.md` in full**".

**11. Upstream anecdotes and duplicate sections.** Rule: one procedure, one example. Session statistics and retold incidents go. Only where C22 is ruled in. (Share: about 1% of the corpus.)
Before (root-cause-tracing.md): "## Real-World Impact / From debugging session (2025-10-03): … - 1847 tests passed, zero pollution"
After: (cut)

**12. Saying one thing several ways.** (Share: about 0.5–1%.)
Before (seat-prompt.source.md): "The lens is a **search-ordering hint — not a scope limit**. Your mandate is **full-scope**: read the whole artifact, and report any finding you hit regardless of whether it matches your lens. Order your hunt by the lens; bound nothing by it."
After: "Read the whole artifact and report every finding; the lens only orders the search." Likewise, "goes to the operator as a decision ask" becomes "is a decision ask".

**13. Meta-text about the text.** Rule: a sentence that describes the document goes to docs/. (Share: about 0.7%.)
Before (formats.md): "What a controller or seat writes and reads, defined once so writers and readers are built against one text: the feature workspace, the round record and the feature folder."
After: "Field lists and file names are binding unless marked *advisory*."

**14. Rare-path variants at every site.** Rule: state the variant once, where its rare event is handled. Other sites name only the common path. (Share: about 0.6% of words, more of tokens.)
Before (re-review-prompt.slots.md): "A replacement seat adds `-r<R>` before `.md`, as in `sdd/reports/task-<N>-re-review-w<W>-r<R>.md`."
After: (dropped; dispatch-composition.md § Shared-tree rules states it)

**15. Text for other readers inside a shared section.** Rule: a spliced section holds only rules every taker follows. Rosters go in the preamble or in controller text; one seat's variant goes in its own template. (Share: about 0.5%, paid on every dispatch.)
Before (seat-rules.md): "Redteam seats, the terminal pass, the branch reviewer, an umbrella's closing-review seats and implementers raise premise findings; a task reviewer raises none."
After: (moved to the unspliced preamble)

## What not to cut

- **Frozen anchors and test-read text.**
  - The anchors: formats.md's `##` headings, hooks/README.md § Hook registration per runtime, and docs/authoring.md's `##` headings.
  - A heading may be shortened only to a prefix of its old text.
  - Literals the tests read (constraints.json), among them:
    - the router's `<SUBAGENT-STOP>` and its index entries, each with at least 10 characters of trigger;
    - card grammar;
    - include and passage lines;
    - the stub sentence "read `skills/…` in full".
- **The claudeism scanner.** No "dispatch all seats in one message", and no model or host words. Joined lines can create a hit.
- **Rows and rules with recorded evidence:**
  - the worktrees native-tool row and red flag;
  - the destructive-git rows (`-D`, `--force`, typed `discard`, `worktree remove`);
  - the single-invocation rule;
  - the UTF-16LE and `*-<slug>` warnings;
  - the tree check, seat replacement, the report-file mark and procedure, and the implementer's git identity;
  - the read-the-output rule;
  - the blind verifier's "never rationale";
  - the second read after a wave.
- **Recorded operator preferences:** umbrella recursion, round 1's alternate-role swap, `Review: branch only`, and the shared-tree status check.
- **A reason the rule needs to be read right**, where it is counterintuitive or a record cites an incident behind it. One clause.
- **A SKILL.md's spine:** every step trigger, loop bound, flow gate, resume rule, and every rule that binds beyond its step. Compaction re-attaches only SKILL.md.
- **Paired texts** (docs/authoring.md): edit both sides in one commit.
- **writing-good-tests' Warning Signs:** § Tests in review cites them.
- **Off-list cuts.** If a cut removes a rule rather than words and is not on the decision list, don't make it: raise it.
