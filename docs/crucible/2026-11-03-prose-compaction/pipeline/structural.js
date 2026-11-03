export const meta = {
  name: 'compaction-structural',
  description: 'Sequential structural steps of the prose compaction: implement, review, fix, each on the shared worktree',
  phases: [{ title: 'Structural' }],
}

const W = args.root  // the repository root (absolute)
const WS = `${W}/.crucible/prose-compaction`
const COMMON = `Read ${WS}/brief-common.md first: it is your shared brief and binds you.`
const TRAILER = `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_01JwnxpWhDazk3WroirNqi7o`

const IMPL = {
  type: 'object',
  properties: {
    base: { type: 'string', description: 'git rev-parse HEAD before your first edit' },
    head: { type: 'string', description: 'git rev-parse HEAD after your last commit' },
    commits: { type: 'array', items: { type: 'string' } },
    suite: { type: 'string', description: 'the pytest summary line, quoted from your last run' },
    suite_green: { type: 'boolean' },
    changes: { type: 'string', description: 'per cluster: what moved where, what was rewritten or deleted' },
    deviations: { type: 'array', items: { type: 'string' } },
    defects: { type: 'array', items: { type: 'string' } },
  },
  required: ['base', 'head', 'commits', 'suite', 'suite_green', 'changes', 'deviations', 'defects'],
}
const REVIEW = {
  type: 'object',
  properties: {
    findings: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, severity: { type: 'string', enum: ['BLOCKER', 'MAJOR', 'MINOR'] }, claim: { type: 'string' }, evidence: { type: 'string' }, fix: { type: 'string' } }, required: ['id', 'severity', 'claim', 'evidence', 'fix'] } },
    suite: { type: 'string' },
    generator_check: { type: 'string' },
    verdict: { type: 'string' },
  },
  required: ['findings', 'suite', 'generator_check', 'verdict'],
}

const implRules = `EXCEPTION to the brief's read-only constraint: you are an implementer. You edit files in the worktree ${W} and commit on its branch \`prose-compaction\`. Never touch another checkout, never push, never check out or commit to master, never use git stash, never rewrite history (no amend, rebase or reset of existing commits). Start no agents.

Rules:
- Move text verbatim where a ruling moves it; rewrite only where a ruling rewrites (a dedupe, a narrowing, a definition, a pointer). Do not line-edit other text: a per-file compaction pass follows. Text you write new: one paragraph or list item per line, no hard wraps.
- Add no rule. Defects you notice go in your report, unfixed.
- Keep the suite green: \`python -m pytest tests/ -q\` from the worktree root. After editing any *.source.md or the shared seat reference(s), run \`python tools/instrument_agents.py write\`. Change a test only where the ruling changes what code reads (e.g. EXPECTED stub pairs, the generator's shared-reference list), each assertion keeping its comment naming the reader.
- tests/prose-budget.txt: set each changed skill directory's line to its new count.
- Decision records: where a ruling changes what a record in docs/decisions/ states, edit the record in place and add a \`## Changes\` line \`2026-11-03: <what changed, and why>\`; docs/authoring.md likewise. Shipped feature folders under docs/crucible/ and docs/backlog/ items are not yours to edit, except a backlog item the ruling names.
- No local context in committed text (AGENTS.md). LF line endings (Edit/Write tools, or Python with newline='\\n').
- Commit the step (one commit per logical change), subject \`prose-compaction: <what>\`, body saying what changed and why with the cluster ids, ending with these two lines:
${TRAILER}`

const steps = args.steps
const out = []
phase('Structural')
for (const s of steps) {
  const impl = await agent(`${COMMON}

${implRules}

Your step: ${s.title}. The rulings: read ${WS}/decisions.md, and in ${WS}/decisions-draft.md the clusters ${s.clusters.join(', ')} (each § C<n>: what, saving, risk and dependencies). Implement exactly those clusters as ruled, nothing else. ${s.extra || ''}

Your final output is the structured result; quote the suite summary line from your own last run.`, { label: `impl:${s.key}`, phase: 'Structural', schema: IMPL })
  if (!impl) { out.push({ step: s.key, failed: 'implementer returned nothing' }); break }
  const rev = await agent(`${COMMON} You are read-only: no edits, no git commands that change anything.

You review one structural step of the prose compaction: the commits ${impl.base}..${impl.head} on branch prose-compaction in ${W} (use git log, git show, git diff, read-only). The step implemented clusters ${s.clusters.join(', ')} of ${WS}/decisions-draft.md as ruled in ${WS}/decisions.md. ${s.extra ? 'The controller added: ' + s.extra : ''}

Check, reading the diff in full and the files it touches:
1. Every ruling in scope is implemented, and nothing outside scope changed.
2. No rule was lost: moved text arrives in its new home (verbatim unless the ruling rewrites it); deleted text is exactly what a ruling deletes; every reader that needs a moved rule can still reach it at the moment it acts (pointer, stub trigger, splice).
3. No rule was added, and no meaning changed, beyond what the ruling asks.
4. Every citation and pointer the step touches resolves to what it means, not merely to a heading that exists.
5. Decision records and docs/authoring.md were updated where the step changes what they state, each with a Changes line.
6. Run \`python -m pytest tests/ -q\` and \`python tools/instrument_agents.py check\` and quote their summary output.
Report each finding with severity (BLOCKER/MAJOR/MINOR), the evidence (file:line or diff hunk) and the fix you propose. Your final output is the structured result.`, { label: `review:${s.key}`, phase: 'Structural', schema: REVIEW, effort: 'high' })
  let fix = null
  const serious = rev ? rev.findings.filter(f => f.severity !== 'MINOR') : []
  const minors = rev ? rev.findings.filter(f => f.severity === 'MINOR') : []
  if (serious.length || minors.length) {
    fix = await agent(`${COMMON}

${implRules}

A reviewer checked the structural step "${s.title}" (commits ${impl.base}..${impl.head}; clusters ${s.clusters.join(', ')} of ${WS}/decisions-draft.md as ruled in ${WS}/decisions.md). Fix every BLOCKER and MAJOR finding below, and each MINOR one that is a real defect cheap to fix; for a finding you judge wrong, say why and leave it. Commit the fixes as a new commit (subject \`prose-compaction: review fixes for <step>\`).

Findings:
${JSON.stringify(rev.findings, null, 1)}

Your final output is the structured result (base = HEAD before your fixes).`, { label: `fix:${s.key}`, phase: 'Structural', schema: IMPL })
  }
  const green = fix ? fix.suite_green : impl.suite_green
  out.push({ step: s.key, impl, rev, fix })
  log(`${s.key}: impl ${impl.commits.length} commits, review ${rev ? rev.findings.length : 'none'} findings (${serious.length} serious), fix ${fix ? fix.commits.length : 0}, green ${green}`)
  if (!green) { log(`stopping: suite not green after ${s.key}`); break }
}
return out.map(o => ({ step: o.step, failed: o.failed, commits: o.impl && o.impl.commits, suite: (o.fix || o.impl || {}).suite, review: o.rev && o.rev.findings.map(f => `${f.severity} ${f.claim}`.slice(0, 200)), fixed: o.fix && o.fix.commits, deviations: o.impl && o.impl.deviations, defects: [...((o.impl && o.impl.defects) || []), ...((o.fix && o.fix.defects) || [])] }))
