export const meta = {
  name: 'compaction-branch-review',
  description: 'Whole-branch review of the prose compaction: loss lenses per skill family, cross-file consistency, records, route walkthroughs; adversarial verification of each finding',
  phases: [
    { title: 'Review' },
    { title: 'Verify' },
  ],
}

const W = args.root  // the repository root (absolute)
const WS = `${W}/.crucible/prose-compaction`
const BASE = args.base || '0deefcf'
const OUT = `${WS}/review-${args.round || 1}`

const COMMON = `Repository: \`${W}\` (branch prose-compaction). Its base is master \`${BASE}\`; \`git diff ${BASE}..HEAD\` is the branch. The branch compacts crucible's skill text for tokens (the operator's mandate: cut prose as far as reasonably achievable, restructuring allowed, minor losses acceptable where the cut justifies them, no significant functionality loss). Rulings the controller made, with the losses it accepted on purpose: \`${WS}/decisions.md\` (cluster texts in \`${WS}/decisions-draft.md\`), and per file \`${WS}/briefs/<slug>.md\` and \`${WS}/units/<slug>/accepted.json\` (slug = path without \`skills/\` and \`.md\`, \`/\` as \`__\`). Read \`AGENTS.md\` for the repo's rules.

Constraints: read-only. Edit no tracked file, run no git command that changes anything, commit nothing, start no agents, publish nothing, call no model API. Write only your report file. Run \`git status --short\` at your start and end; both must match.

Findings: report only what makes an agent acting under the branch's text act worse than under \`${BASE}\`'s in a case that arises — a lost rule, condition, exception, format or ordering; a contradiction; a pointer that no longer leads to the rule; a new ambiguity that changes the action — or a defect the branch introduced. Severity: BLOCKER (breaks a route or a seat's output), MAJOR (a wrong action in a common case), MINOR (a wrong action in a rare case, or a dangling pointer the reader can recover from). For each: file and line at HEAD; the scenario (who reads it, when, what they now do); what \`${BASE}\` said, quoted (\`git show ${BASE}:<path>\`); whether a ruling or accepted loss already covers it (then say which and whether its stated reason holds); the smallest fix. Never report wording, style, brevity or a loss the rulings accepted with a reason that holds. Never propose adding a rule \`${BASE}\` did not have, except to fix a contradiction.`

const FIND = {
  type: 'object',
  properties: {
    findings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string' },
          severity: { type: 'string', enum: ['BLOCKER', 'MAJOR', 'MINOR'] },
          file: { type: 'string' },
          line: { type: 'integer' },
          what: { type: 'string' },
          scenario: { type: 'string' },
          base_said: { type: 'string' },
          ruling: { type: 'string', description: 'the ruling or accepted loss that covers it, or none' },
          fix: { type: 'string' },
        },
        required: ['id', 'severity', 'file', 'what', 'scenario', 'base_said', 'ruling', 'fix'],
      },
    },
    report: { type: 'string', description: 'path of your report file' },
    status_start: { type: 'string' },
    status_end: { type: 'string' },
  },
  required: ['findings', 'report', 'status_start', 'status_end'],
}

const VERDICT = {
  type: 'object',
  properties: {
    verdict: { type: 'string', enum: ['confirmed', 'refuted', 'accepted-loss'] },
    severity: { type: 'string', enum: ['BLOCKER', 'MAJOR', 'MINOR', 'none'] },
    reason: { type: 'string' },
    fix: { type: 'string', description: 'the smallest fix, if confirmed' },
  },
  required: ['verdict', 'severity', 'reason', 'fix'],
}

const FAMILIES = [
  ['entry', 'skills/using-crucible/ (router, host maps, dispatch references), skills/brainstorming/, skills/using-git-worktrees/, skills/writing-plans/'],
  ['redteam-controller', 'skills/redteaming/SKILL.md and skills/redteaming/references/'],
  ['redteam-seats', 'skills/redteaming/*.source.md, *.slots.md and the rendered templates beside them (seat, verifier, terminal pass), with the sections they splice from skills/subagent-driven-development/references/seat-rules.md and review-terms.md'],
  ['sdd-controller', 'skills/subagent-driven-development/SKILL.md and skills/subagent-driven-development/references/'],
  ['sdd-seats', 'skills/subagent-driven-development/*.source.md, *.slots.md and the rendered templates (implementer, task reviewer, re-reviewer), with their spliced sections, and skills/subagent-driven-development/writing-good-tests.md'],
  ['review-finish', 'skills/requesting-code-review/ (SKILL.md, code-reviewer source, slots and rendered, very-small-lane-review.md), skills/finishing-a-development-branch/, skills/systematic-debugging/, skills/dispatching-parallel-agents/'],
]

const LENSES = [
  ...FAMILIES.map(([k, scope]) => ({ key: `loss-${k}`, prompt: `${COMMON}

Your lens: functional loss in ${scope}. Read each file at HEAD whole and compare it with ${BASE} (\`git diff ${BASE}..HEAD -- <path>\`; a file new on the branch took text from another file, so follow the move). Text that moved is not lost where its new home is read at the step its reader needs it: check that the reader is sent there. Write your report to \`${OUT}/loss-${k}.md\`.` })),
  { key: 'consistency', prompt: `${COMMON}

Your lens: cross-file consistency of the skill tree at HEAD. (1) The paired texts listed in \`docs/authoring.md\` § Paired texts: each pair still says the same thing. (2) Every \`§\` citation and file pointer in \`skills/\` leads to a heading or file that holds what the citing sentence says it holds (the suite checks that headings exist, not what they hold). (3) A rule stated in two files states the same rule in both; where one file now points to another for a rule, the other states it. (4) The generated templates and \`agents/\` match their sources (\`python tools/instrument_agents.py check\`). Write your report to \`${OUT}/consistency.md\`.` },
  { key: 'records', prompt: `${COMMON}

Your lens: the repository's own records against the tree. \`docs/decisions/\`, \`docs/backlog/\`, \`docs/authoring.md\`, \`AGENTS.md\` and \`README.md\`: find statements about skill text that are false at HEAD (a quoted rule, a § named, a file said to hold something, a count), a record whose position the branch changed with no \`## Changes\` line dated 2026-11-03, and committed text breaking AGENTS.md § No local context. History sections describing the past are not findings. Write your report to \`${OUT}/records.md\`.` },
  ...[
    ['walk-standard', 'a feature on the standard route: brainstorm with a spec campaign, the plan and its plan phase, SDD execution of three tasks (one with a fix wave, one disputed finding, one task marked branch review only), the branch review with one fix wave, Finish and the merge'],
    ['walk-small', 'first a feature on the very-small lane (lane note, inline implementation, the lane review with one inline fix wave, Finish); then a feature on the folded lane (combined spec and plan document, its campaign, execution)'],
    ['walk-umbrella', 'an umbrella effort: proposing and writing the umbrella, its review and landing, then its first child (brainstorm, binding changes under the umbrella, a premise finding raised in the child\'s campaign and carried to the ledger), and the umbrella\'s closing'],
  ].map(([k, route]) => ({ key: k, prompt: `${COMMON}

Your lens: a behavioural walkthrough. You are a controller agent on this host (Claude Code) with crucible installed from this tree; the SessionStart envelope is \`skills/using-crucible/SKILL.md\` plus \`skills/using-crucible/references/claude-code.md\`. Walk ${route}. Read only what the text in front of you tells you to read, when it tells you to, as a controller would; at each step write down what you do next and which sentence told you. Wherever the HEAD text leaves the next action unsettled, contradicts itself, or sends you to a file or section that does not hold what you need, check \`${BASE}\`'s text for the same step: a finding is a place where ${BASE} settled it and HEAD does not. Note also each seat you would dispatch and check its card and template give the seat what it needs. Write your report to \`${OUT}/${k}.md\`.` })),
]

const RUN = LENSES.filter(l => !(args.skip || []).includes(l.key) && (!args.only || args.only.includes(l.key)))
const results = await pipeline(
  RUN,
  l => agent(l.prompt, { label: `review:${l.key}`, phase: 'Review', schema: FIND, effort: 'xhigh' }),
  (r, l) => {
    if (!r) return null
    const keep = r.findings.filter(f => f.severity !== 'MINOR' || args.verifyMinor)
    return parallel(keep.map(f => () => agent(`${COMMON}

You verify one finding from a reviewer of this branch, adversarially: try to refute it. Read the cited file at HEAD and at ${BASE}, and what it points to. Verdicts: confirmed (an agent under HEAD acts worse than under ${BASE} in a case that arises, as claimed, or worse), refuted (HEAD settles it, maybe elsewhere, or ${BASE} did not say it), accepted-loss (a ruling or accepted loss covers it, with a reason that holds). Give the severity you judge and the smallest fix. Write no file.

Finding ${f.id} (${f.severity}) — ${f.file}:${f.line || ''}
What: ${f.what}
Scenario: ${f.scenario}
${BASE} said: ${f.base_said}
Reviewer's ruling note: ${f.ruling}
Proposed fix: ${f.fix}`, { label: `verify:${l.key}:${f.id}`, phase: 'Verify', schema: VERDICT, effort: 'high' }).then(v => ({ lens: l.key, ...f, v }))))
      .then(vs => ({ lens: l.key, report: r.report, status: [r.status_start, r.status_end], findings: r.findings, verified: vs.filter(Boolean) }))
  },
)
return { results: results.filter(Boolean) }
