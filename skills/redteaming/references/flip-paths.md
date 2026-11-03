## Flip paths — scoped amendment and supersede

You own both paths, in whichever skill context you are operating.

What binds, and how binding text is read: `skills/subagent-driven-development/references/review-terms.md` § What binds in a spec.

These paths govern that content and binding-by-construction contract content, `skills/brainstorming/references/umbrella-children.md` § Under an umbrella a change the umbrella content itself needs, and § Premise findings a premise finding at any phase, the spec campaign included. The bar on flipping binding content by a fix wave holds from the spec campaign's close onward: during a spec's own campaign the spec is the artifact under review, and its fix waves correct binding content like any other text, with the terminal pass as the check. From that close on, binding content that a finding shows wrong cannot be flipped by a fix wave; it forces one of these paths, and so does defective or superseded plan text found mid-execution. The supersede path applies wherever a supersede is called for, inside a campaign included — the cap ask's supersede option, an unfold. **Both start as a decision ask to the operator**, except a change § The containment test finds contained, which you confirm; choose by blast radius, your judgment, logged. An operator's ruling on any ask here also enters `brainstorm-decisions.md`.

**Scoped amendment** (the default, for a correction inside a mechanism that stands), confirmed by you where the change is contained (§ The containment test), otherwise by the operator:

1. amend the spec **in place with an amendment marker** at the changed content;
2. patch the plan to match — where spec and plan are separate documents, the same patch re-stamps the plan header's spec pointer to the amended revision; a folded document keeps its `Spec: this document` header;
3. **point in-flight seats at the patch** — seats read the plan live, so later dispatches read it; an implementer resumed in an open task's fix wave is told to re-read its task section; and **each amendment commit is named** in the dispatch of every task-loop review, re-review and adjudication whose range holds it, and, for a task completed branch review only, to the branch reviewer beside that task's range (`crucible:requesting-code-review`): any other change to the plan, a folded document or the spec in that range is a finding;
4. continue — **no new spec campaign or plan phase**.

A ruling that patches the plan mid-execution, an adjudicator's or yours, passes § The containment test like any change to binding content: a contained one is handled by steps 3 and 4, its commit named as an amendment commit is; any other goes to the operator as a decision ask.

**Supersede** (structural blast radius): draft a successor spec and header-mark the old one superseded. Predecessors stay in place as the forensic record; successors go into the feature's existing feature folder, which its resolve step finds, under the successor names it gives, an unfold's included — both in the Feature folder section of `skills/redteaming/references/formats.md`. Where the predecessor's preamble carries an umbrella line, the successor spec's preamble carries the same line. If execution is in flight, halt it and derive a successor plan. The successor ledger takes the identity and predecessor-link lines of the Setup section of `skills/subagent-driven-development/SKILL.md`, which also says how a resume follows that link and recovers when the predecessor records are gone; the successor plan's header records which completed tasks carry over and which are invalidated. A successor spec gets its own spec campaign and a successor plan its own plan phase; **the round counter does not carry over**.

### The containment test

From the spec campaign's close, every change to binding content, a ruling that patches the plan included, is either contained, and yours to confirm, or put to the operator as a decision ask, whatever finding, report or ruling raised it. A change is **contained** when everything that builds on or consumes the changed item lies inside this feature, as you judge it, and it is none of these:

- a change to umbrella content, this feature's own entry included;
- a change to a decision the spec or an umbrella records as the operator's firm preference;
- a change after which the same work, unchanged, passes a verification gate or an acceptance check it failed;
- a structural change, one that redefines a mechanism rather than correcting content inside one that stands: it takes a supersede.

Any other change keeps the operator's decision ask, as does a plan conflict that is a design judgment.

A ruling on a case a binding item's literal reading reaches, or on a BLOCKED report about a binding item, passes this test whichever way it goes. One that leaves the text standing goes to the operator as a decision ask where applying it as written changes behaviour something outside this feature builds on or consumes, and is otherwise recorded as your ruling.

A contained change to the spec is a scoped amendment you confirm with no decision ask, and one in every other respect — marker, plan patch, re-pin, named commit — so every rule naming a scoped amendment covers it. Record each contained change as one of your rulings under the ledger's `## Adjudication rulings` — the item, what changed and why, why it is contained, the commit — so the branch review receives it and the close readout lists it; in the plan phase it lands as `skills/redteaming/references/plan-phase.md` states. It reaches the operator through readouts. Reversing one is a scoped amendment the operator confirms, made before the branch lands.

### Premise findings

A premise finding claims that the request, what the Intent asks for (for a child, its umbrella's too; on the very-small lane, the lane note's), or a firm decision is wrong, and carries the label `premise`. Your side, at any phase, the spec campaign included:

**A mislabel.** You correct a finding's label by the definition above, in either direction, your reason recorded with it: a finding labelled `premise` that the definition classes as ordinary — against a lightly held decision, say — is merged or routed as an ordinary finding, and an unlabelled finding against the request, what the Intent asks for or a firm decision takes the label and this section's route.

**The ask.** Every premise finding goes to the operator as a decision ask, carrying the severity its seat staked for the operator's weighing — never a change you confirm, whatever § The containment test would find. It is an open decision ask, not an open BLOCKER or MAJOR: by itself it holds open no gate keyed on one — the cap escalation, the branch review's end condition, task completion — opens no fix wave and consumes no wave cap. The readouts carry it until it is ruled, and while it is open, work goes on.

**The ruling.** What the operator's ruling brings takes the route any change of its kind takes: in a spec campaign, the next fix list, where a change that re-shapes a major mechanism makes overturning one after code reasonably expected again, and its round no stop round (`crucible:redteaming` § Stop rule and terminal pass); from that campaign's close, the paths above, the ruling standing as the operator's confirmation. In execution, a ruling given during the task loop lands as a plan change at the next task boundary (`crucible:subagent-driven-development` § Plan changes mid-execution), the affected tasks not yet dispatched waiting for it; one given later, at the branch review or its close readout, lands in a branch-review wave, counted against its cap like any, and Finish restarts after it (`crucible:subagent-driven-development` § Finish). A ruling that keeps the decision opens no wave.

**Precedence.** A finding that is both a premise finding and a binding item found wrong — a firm decision, a lane note's Intent — takes this section's route. Any other binding item found wrong keeps its own: in its spec's own campaign the fix list, from that campaign's close § The containment test, and from an implementer a BLOCKED report with a proposed correction.

**Carrying an open ask.** Until the ledger exists, an open premise ask stays in the records and close readouts of the phase it is open in, and SDD's Setup seeds it into the ledger as open (`skills/subagent-driven-development/references/setup.md`); once the ledger exists, write it under its `## Adjudication rulings` directly and tell the operator of it in a one-line message, not waiting for the close readout; one still open when an umbrella lands goes as `skills/brainstorming/references/umbrellas.md` § Landing and `skills/brainstorming/references/umbrella-children.md` § Children state.
