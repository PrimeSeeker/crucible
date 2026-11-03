export const meta = {
  name: 'compaction-reverify',
  description: 'Blind re-check of each compacted final against its inventory and open QA items; one repair; blind re-check and QA re-ask',
  phases: [
    { title: 'Check' },
    { title: 'Repair' },
    { title: 'Recheck' },
  ],
}

const W = args.root  // the repository root (absolute)
const WS = `${W}/.crucible/prose-compaction`
const CHECK = `python ${WS}/tools/check_variant.py`
const COMMON = `Read ${WS}/brief-common.md first: it is your shared brief and binds you.`
const slug = p => p.replace(/^skills\//, '').replace(/\//g, '__').replace(/\.md$/, '')
const udir = p => `${WS}/units/${slug(p)}`

const PROBLEMS = {
  type: 'object',
  properties: {
    problems: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string' },
          verdict: { type: 'string', enum: ['weakened', 'missing'] },
          detail: { type: 'string', description: 'what the rewrite lost or changed, and the case where a reader would now act differently' },
        },
        required: ['id', 'verdict', 'detail'],
      },
    },
    added: { type: 'array', items: { type: 'string' }, description: 'only statements that would make a reader act differently from the inventory' },
    checked: { type: 'integer', description: 'how many core/edge items you checked' },
  },
  required: ['problems', 'added', 'checked'],
}

const REPAIRED = { type: 'object', properties: { restored: { type: 'array', items: { type: 'string' } }, accepted_losses: { type: 'array', items: { type: 'object', properties: { item: { type: 'string' }, says: { type: 'string' }, reason: { type: 'string' }, severity: { type: 'string', enum: ['minor', 'significant'] } }, required: ['item', 'says', 'reason', 'severity'] } }, words: { type: 'integer' } }, required: ['restored', 'accepted_losses', 'words'] }

const ANS = { type: 'object', properties: { answers: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, a: { type: 'string' } }, required: ['id', 'a'] } } }, required: ['answers'] }
const GRADE = { type: 'object', properties: { grades: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, grade: { type: 'string', enum: ['match', 'partial', 'diverge'] }, cause: { type: 'string' } }, required: ['id', 'grade'] } } }, required: ['grades'] }

const checkPrompt = u => `${COMMON}

You are a blind checker of \`${udir(u.path)}/final.md\`, a compacted rewrite of \`${u.path}\`. Do NOT open the original at its repo path. Read \`${udir(u.path)}/inventory.json\` (the original's rule items: id, says, quote, criticality), the unit brief \`${u.brief}\` (it may retire items on purpose) and \`${udir(u.path)}/accepted.json\` (losses already accepted: do not report those again). Read the rewrite whole; you may open other repo files it points to, since a rule stated where a pointer leads counts as present.

Check every item whose criticality is core or edge (skip support items). Report under problems only the items the rewrite states weaker (a condition, case, exception or force lost) or not at all, and not retired or accepted. Under added, list only what the rewrite says that would make a reader act differently from the inventory: a new obligation, a changed meaning, an ambiguity that changes the action. Never report wording, order, placement or brevity.`

const repairPrompt = (u, problems) => `${COMMON}

You repair \`${udir(u.path)}/final.md\`, a compacted rewrite of \`${u.path}\` (read the original at its repo path for wording; its rule items are in \`${udir(u.path)}/inventory.json\`). Checks found these problems:

${problems}

For each: restore what the original says where a reader acting under the rewrite would now act differently (a lost condition, case, exception, force or obligation, or a real new ambiguity), in the fewest words that keep it, in the place its reader needs it. Leave it only where the unit brief \`${u.brief}\` retires it, where \`${udir(u.path)}/accepted.json\` already accepts it with a reason that still holds, or where the loss is minor, the case rare and the words not worth it: list each such with your reason. Change nothing else. Then run \`${CHECK} ${u.path} ${udir(u.path)}/final.md\` until no violations remain. Return what you restored and what you accepted as lost.`

const fmt = c => [...c.problems.map(p => `- ${p.id} (${p.verdict}): ${p.detail}`), ...c.added.map(a => `- ADDED/CHANGED: ${a}`)].join('\n')

const results = await pipeline(
  args.units,
  async u => {
    const c = await agent(checkPrompt(u), { label: `rv-check:${slug(u.path)}`, phase: 'Check', schema: PROBLEMS, effort: 'high' })
    if (!c) throw new Error('check failed')
    return { c }
  },
  async ({ c }, u) => {
    const parts = []
    if (c.problems.length || c.added.length) parts.push(`From a blind check against the inventory:\n${fmt(c)}`)
    if (u.qa) parts.push(`From behavioural QA (a blind reader answered scenario questions under the rewrite; the file \`${udir(u.path)}/qa-open.md\` holds each scenario, the original's answer and what the rewrite lost). Read it and treat each as a problem.`)
    if (!parts.length) return { c, r: null }
    const r = await agent(repairPrompt(u, parts.join('\n\n')), { label: `rv-repair:${slug(u.path)}`, phase: 'Repair', schema: REPAIRED })
    return { c, r }
  },
  async ({ c, r }, u) => {
    if (!r) return { c, r, c2: null, gr: null }
    const c2 = await agent(checkPrompt(u), { label: `rv-recheck:${slug(u.path)}`, phase: 'Recheck', schema: PROBLEMS, effort: 'high' })
    let gr = null
    if (u.qa) {
      const ans = await agent(`${COMMON}

Read \`${udir(u.path)}/final.md\` whole: it is the text you act under (a rewrite of \`${u.path}\`). Do NOT open that original, and in the folder \`${udir(u.path)}/\` open only final.md and qa-questions.md. You may read other repo files the rewrite points to. \`${udir(u.path)}/qa-questions.md\` holds scenario questions, each under a "### <id>" heading. Answer each as a reader acting under the rewrite would, briefly. Where the text does not settle a question, say "not settled" and what you would do.`, { label: `rv-qans:${slug(u.path)}`, phase: 'Recheck', schema: ANS, effort: 'high' })
      if (ans) {
        gr = await agent(`Read \`${udir(u.path)}/qa-open.md\`: each "### <id>" entry holds a scenario and the original's answer. Grade the answers below against the original's answers. For each: match (same action/outcome), partial (right action, a condition or detail lost), diverge (different action or outcome, or not settled where the expected answer is definite). For partial and diverge, name what the rewrite lost or changed. Judge substance, not wording.

${ans.answers.map(a => `${a.id}: ${a.a}`).join('\n\n')}`, { label: `rv-qgrade:${slug(u.path)}`, phase: 'Recheck', schema: GRADE, effort: 'medium' })
      }
    }
    return { c, r, c2, gr }
  },
)

const summary = results.map((x, i) => {
  const u = args.units[i]
  if (!x) return { path: u.path, failed: true }
  return {
    path: u.path,
    first: { problems: x.c.problems.length, added: x.c.added.length },
    repaired: !!x.r,
    words: x.r ? x.r.words : null,
    accepted: x.r ? x.r.accepted_losses.length : 0,
    significant: x.r ? x.r.accepted_losses.filter(l => l.severity === 'significant').map(l => `${l.item}: ${l.reason}`) : [],
    left: x.c2 ? { problems: x.c2.problems.map(p => `${p.id} ${p.verdict}: ${p.detail}`), added: x.c2.added } : null,
    qa: x.gr ? x.gr.grades.reduce((a, g) => (a[g.grade] = (a[g.grade] || 0) + 1, a), {}) : null,
    qa_left: x.gr ? x.gr.grades.filter(g => g.grade !== 'match').map(g => `${g.id} ${g.grade}: ${g.cause || ''}`) : [],
  }
})
return { summary }
