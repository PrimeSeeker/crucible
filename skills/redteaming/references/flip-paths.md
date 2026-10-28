## Flip paths — scoped amendment and supersede

You own both paths, in whichever skill context you are operating. What binds in a spec is its Constraints & invariants, its [LOAD-BEARING] marks, the preamble conventions it declares binding, the decisions it records as the operator's firm preference, and the umbrella content its umbrella line brings in, an umbrella's firm decisions included; these paths govern that content and binding-by-construction contract content, § Under an umbrella a change the umbrella content itself needs, and § Premise findings a premise finding at any phase, the spec campaign included. The spec is a hypothesis, probably subtly wrong and certainly locally imperfect: binding means never changed silently, not never changed without the operator. Binding text is read for its intent: a case its literal reading reaches that its author plainly did not consider is raised for a ruling, never applied literally. The bar on flipping binding content by a fix wave holds from the spec campaign's close onward: during a spec's own campaign the spec is the artifact under review, and its fix waves correct binding content like any other text, with the terminal pass as the check. From that close on, binding content that a finding shows wrong cannot be flipped by a fix wave; it forces one of these paths, and so does defective or superseded plan text found mid-execution. The supersede path applies wherever a supersede is called for, inside a campaign included — the cap ask's supersede option, an unfold. **Both start as an analyst-language decision ask to the operator with a recommendation**, except a change § The containment test finds contained, which you confirm; choose by blast radius, your judgment, logged. An operator's ruling on any ask here also enters the brainstorm decision record (`skills/redteaming/references/formats.md` § Feature workspace root and layout).

**Scoped amendment** (the default, for a correction inside a mechanism that stands), confirmed by you where the change is contained (§ The containment test), otherwise by the operator:

1. amend the spec **in place with an amendment marker** at the changed content;
2. patch the plan to match — where spec and plan are separate documents, the same patch re-stamps the plan header's spec pointer to the amended revision; a folded document keeps its `Spec: this document` header;
3. **point in-flight seats at the patch** — seats read the plan live, so later dispatches read it; an implementer resumed in an open task's fix wave is told to re-read its task section; and **each amendment commit is named** in the dispatch of every task-loop review, re-review and adjudication whose range holds it: any other change to the plan, a folded document or the spec in that range is a scope finding;
4. continue — **no new spec campaign or plan phase**.

A ruling that patches the plan mid-execution, an adjudicator's or yours, passes § The containment test like any change to binding content: a contained one is handled by steps 3 and 4, its commit named as an amendment commit is; any other goes to the operator as a decision ask.

**Supersede** (structural blast radius): draft a successor spec and header-mark the old one superseded. Predecessors stay in place as the forensic record; successors go into the feature's existing feature folder, which its resolve step finds, under the successor names it gives, an unfold's included — both in the Feature folder section of `skills/redteaming/references/formats.md`. Where the predecessor's preamble carries an umbrella line, the successor spec's preamble carries the same line. If execution is in flight, halt it and derive a successor plan. The successor ledger takes the identity and predecessor-link lines of the Setup section of `skills/subagent-driven-development/SKILL.md`, which also says how a resume follows that link and recovers when the predecessor records are gone; the successor plan's header records which completed tasks carry over and which are invalidated. A successor spec gets its own spec campaign and a successor plan its own plan phase; **the round counter does not carry over**.

### The containment test

From the spec campaign's close, every change to binding content, a ruling that patches the plan included, is either contained, and yours to confirm, or put to the operator as a decision ask, whatever finding, report or ruling raised it. A change is **contained** when everything that builds on or consumes the changed item lies inside this feature — a mark names what builds on it; for any other item, or a mark that names nothing, you judge what does — and it is none of these:

- a change to umbrella content, this feature's own entry included;
- a change to a decision the spec or an umbrella records as the operator's firm preference;
- a change after which the same work, unchanged, passes a verification gate or an acceptance check it failed;
- a structural change, one that redefines a mechanism rather than correcting content inside one that stands: it takes a supersede.

Any other change keeps the operator's decision ask, as does a plan conflict that is a design judgment.

A ruling on a case a binding item's literal reading reaches, or on a BLOCKED report about a binding item, passes this test whichever way it goes. One that leaves the text standing goes to the operator as a decision ask where applying it as written changes behaviour something outside this feature builds on or consumes, and is otherwise recorded as your ruling.

A contained change to the spec is a scoped amendment you confirm with no decision ask, and one in every other respect — marker, plan patch, re-pin, named commit — so every rule naming a scoped amendment covers it. Record each contained change as one of your rulings under the ledger's `## Adjudication rulings` — the item, what changed and why, why it is contained, the commit — so the branch review receives it and the close readout lists it; in the plan phase it lands as `skills/redteaming/references/plan-phase.md` states. It reaches the operator through readouts, never the design digest, which records decision asks. Reversing one is a scoped amendment the operator confirms, made before the branch lands.

### Premise findings

What a premise finding is, and its label `premise`, is in `skills/subagent-driven-development/references/findings-and-questions.md` § Premise findings. Your side, at any phase, the spec campaign included:

**The ask.** Every premise finding goes to the operator as an analyst-language decision ask with your recommendation, carrying the severity its seat staked for the operator's weighing — never a change you confirm, whatever § The containment test would find. It is an open decision ask, not an open BLOCKER or MAJOR: by itself it holds open no gate keyed on one — the stop trigger and the cap escalation, the branch review's end condition and its merge red flag, task completion — opens no fix wave and consumes no wave cap. The readouts carry it until it is ruled. While it is open, work goes on, except work that builds on the premise it challenges, which waits for the ruling.

**The ruling.** What the operator's ruling brings takes the route any change of its kind takes: in a spec campaign, the next fix list, where a change that re-shapes a mechanism makes its round structural; from that campaign's close, the paths above, the ruling standing as the operator's confirmation; in execution, a fix wave, counted against its cap like any.

**Precedence.** A finding that is both a premise finding and a binding item found wrong — a firm decision, a lane note's Intent — takes this section's route. Any other binding item found wrong keeps its own: in its spec's own campaign the fix list, from that campaign's close § The containment test, and from an implementer a BLOCKED report with a proposed correction.

**Carrying an open ask.** Until it is ruled, an open premise ask is kept with the records of the phase it is open in, and passes on at each close:

- raised by a plan-phase seat: in the plan record, until the plan phase's close seeds it into the ledger's `## Adjudication rulings` as open;
- open when a spec campaign closes: in the digest's `## Open judgments`, or the close readout of a minor design, which has no digest; the plan phase's close seeds it into the ledger as open, or on the folded lane the campaign's close;
- raised once the ledger exists: written under its `## Adjudication rulings` directly, from where SDD's close readout carries it;
- still open when an umbrella lands, with no ledger to hold it: put to the operator with the landing ask; unruled, it enters the first child's brainstorm decision record as open, and that child's dialogue takes it up. No landing waits on it.

### Under an umbrella: binding changes and late splits

What an umbrella is, which of its edits is a binding change, and what follows the operator's ruling are in `skills/brainstorming/references/umbrellas.md`. Your side, as a feature's controller:

**Raising.** Two findings, yours or a seat's, go to the operator as an analyst-language decision ask with a recommendation: that the feature needs splitting after its spec campaign closes or once its lane note is committed, and that its umbrella needs an edit the reference's § Edits classes as a binding change. Neither is a scoped amendment or a supersede, and **neither is made as an edit to an umbrella on the feature's branch**.

**Receiving.** For a feature whose preamble carries an umbrella line, at each task or round boundary and before each full-scope pass and fix wave of its branch review (`crucible:requesting-code-review`) — before you record the task's BASE, the revision the round reviews, the pass's range or the wave's FIX_BASE — check whether a binding change to an umbrella in its chain has landed on the base since the branch last took the base in (`git diff HEAD...<base> -- <umbrella paths>` shows what changed there). If one has, and the operator has not ruled the feature unaffected, merge the base into the feature's branch — never rebase it, which would rewrite the revisions your records name. Where the change contradicts the feature's spec, folded document or lane note, amend it: a spec or folded document by the scoped amendment above; a lane note by an operator-approved change to its binding parts, re-pinned in the ledger as `skills/subagent-driven-development/references/very-small-lane.md` states, or by that lane's upgrade hatch.
