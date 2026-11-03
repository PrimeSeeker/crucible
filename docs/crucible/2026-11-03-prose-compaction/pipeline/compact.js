export const meta = {
  name: 'compaction-units',
  description: 'Per-file compaction: inventory, three framed rewrites, blind checks, judge-synthesis, final check, behavioural QA',
  phases: [
    { title: 'Inventory' },
    { title: 'Write' },
    { title: 'Check' },
    { title: 'Synthesize' },
    { title: 'Verify' },
    { title: 'QA' },
  ],
}

const W = args.root  // the repository root (absolute)
const WS = `${W}/.crucible/prose-compaction`
const CHECK = `python ${WS}/tools/check_variant.py`
const COMMON = `Read ${WS}/brief-common.md first: it is your shared brief and binds you. ${args.extraCommon || ''}`
const STYLE = args.style || `${WS}/style.md`
const slug = p => p.replace(/^skills\//, '').replace(/\//g, '__').replace(/\.md$/, '')
const udir = p => `${WS}/units/${slug(p)}`

const INV = {
  type: 'object',
  properties: {
    items: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string' },
          kind: { type: 'string', enum: ['obligation', 'prohibition', 'permission', 'condition', 'definition', 'format', 'step', 'ordering', 'pointer', 'rationale', 'example'] },
          says: { type: 'string', description: 'precise paraphrase: enough for a checker to tell whether a rewrite still says it' },
          quote: { type: 'string', description: 'short verbatim anchor, <= 12 words' },
          criticality: { type: 'string', enum: ['core', 'edge', 'support'] },
        },
        required: ['id', 'kind', 'says', 'quote', 'criticality'],
      },
    },
    defects: { type: 'array', items: { type: 'string' }, description: 'contradictions, gaps or unclear rules noticed in the file' },
  },
  required: ['items', 'defects'],
}

const WROTE = {
  type: 'object',
  properties: {
    path: { type: 'string' },
    words: { type: 'integer' },
    violations_left: { type: 'integer' },
    dropped: { type: 'array', items: { type: 'object', properties: { item: { type: 'string' }, reason: { type: 'string' } }, required: ['item', 'reason'] } },
    defects: { type: 'array', items: { type: 'string' } },
    notes: { type: 'string', description: 'what you cut and how; which techniques gave the most' },
  },
  required: ['path', 'words', 'violations_left', 'dropped', 'defects', 'notes'],
}

const VERDICTS = {
  type: 'object',
  properties: {
    items: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string' },
          verdict: { type: 'string', enum: ['present', 'weakened', 'missing', 'retired'] },
          detail: { type: 'string' },
        },
        required: ['id', 'verdict'],
      },
    },
    added: { type: 'array', items: { type: 'string' }, description: 'obligations, meanings or ambiguities the rewrite adds or changes' },
  },
  required: ['items', 'added'],
}

const SYNTH = {
  type: 'object',
  properties: {
    path: { type: 'string' },
    words: { type: 'integer' },
    base: { type: 'string', enum: ['A', 'B', 'C'] },
    picks: { type: 'string', description: 'per section: which variant it came from, and grafts' },
    framing_ranking: { type: 'string', description: 'A/B/C ranked, with why: tokens saved, losses, readability' },
    accepted_losses: { type: 'array', items: { type: 'object', properties: { item: { type: 'string' }, says: { type: 'string' }, reason: { type: 'string' }, severity: { type: 'string', enum: ['minor', 'significant'] } }, required: ['item', 'says', 'reason', 'severity'] } },
    defects: { type: 'array', items: { type: 'string' } },
    techniques: { type: 'string', description: 'which cut techniques produced the savings here' },
    violations_left: { type: 'integer' },
  },
  required: ['path', 'words', 'base', 'picks', 'framing_ranking', 'accepted_losses', 'defects', 'techniques', 'violations_left'],
}

const QS = {
  type: 'object',
  properties: {
    questions: {
      type: 'array',
      items: {
        type: 'object',
        properties: { id: { type: 'string' }, q: { type: 'string' }, expected: { type: 'string' }, items: { type: 'array', items: { type: 'string' } } },
        required: ['id', 'q', 'expected', 'items'],
      },
    },
  },
  required: ['questions'],
}
const ANS = { type: 'object', properties: { answers: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, a: { type: 'string' } }, required: ['id', 'a'] } } }, required: ['answers'] }
const GRADE = {
  type: 'object',
  properties: {
    grades: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, grade: { type: 'string', enum: ['match', 'partial', 'diverge'] }, cause: { type: 'string', description: 'for partial/diverge: what the rewrite lost or changed, naming inventory items' } }, required: ['id', 'grade'] } },
  },
  required: ['grades'],
}

const invText = inv => inv.items.map(i => `${i.id} [${i.kind}/${i.criticality}] ${i.says} — "${i.quote}"`).join('\n')

const FRAMES = {
  A: { model: undefined, text: `FRAMING A — LINE EDITOR. Keep the file's structure: its sections in their order, its anchors. Cut sentence by sentence: tighter phrasing; drop restatements, hedges, doubled qualifiers, and pointers that add nothing. Change no rule.` },
  B: { model: undefined, text: `FRAMING B — RE-DERIVER. Do NOT open the original file at its repo path: write the file fresh from the inventory below, the unit brief and the original's heading list, as the shortest text a capable agent acting at that step could follow correctly. Reorder and merge items freely within the cited-heading skeleton. You may read other repo files for context (what a term means, where a rule lives), just not the original of this file.` },
  C: { model: 'fable', text: `FRAMING C — RESTRUCTURER. Rewrite for the reader at the moment they act: regroup where order or grouping costs words (merge sections that repeat a frame, turn parallel cases into a table or list, put the common path first and edge cases after), keeping cited headings; then cut as tightly as you can.` },
}

const writerPrompt = (u, inv, heads, X) => `${COMMON}

You are writer ${X} of several for one file: \`${u.path}\` (several writers rewrite it independently under different framings; a judge compares them).

Read: the unit brief \`${u.brief}\` (binding decisions for this file: retirements, where duplicated rules live, structural notes); the style notes \`${STYLE}\` (cut patterns found in this corpus).

${FRAMES[X].text}

Every writer:
- Keeps every inventory item of criticality core or edge unless the brief retires it. You may drop one you judge not worth its words: list it under "dropped" with your reason. Support items (rationale, examples, emphasis, pointers) go wherever the text works without them; at most one clause of why per rule.
- Adds nothing: no new rule, obligation or clarification. A rule you find unclear, contradictory or wrong goes under "defects", unchanged in the text.
- Keeps what code reads: cited headings, a SKILL.md's frontmatter name and description verbatim, stub sentences (\`read \`skills/.../references/<file>.md\` in full\`), \`[[...]]\` lines, protected strings. The checker tells you.
- Writes for a capable agent acting at that step: imperative, plain, no hedges. Tokens are the target, words a proxy: long repo paths are token-heavy, so name a file once in full and refer back briefly where the reference convention allows (docs/authoring.md § Reference convention; stubs keep full paths).

Write your whole rewrite of the file to \`${udir(u.path)}/v-${X}.md\` (LF line endings). Then run \`${CHECK} ${u.path} ${udir(u.path)}/v-${X}.md\` and fix every violation; judge each warning. Repeat until no violations remain. Write no other file.

The original's headings, in order:
${heads}

The inventory (id [kind/criticality] paraphrase — "quote"):
${invText(inv)}

Your final output is the structured result: path, words, violations_left, dropped, defects, notes.`

const checkPrompt = (u, inv, file) => `${COMMON}

You are a blind checker. Below is the rule inventory of the original \`${u.path}\` (its items with short verbatim quotes). The unit brief \`${u.brief}\` lists items retired on purpose. Do NOT open the original at its repo path. Read the rewrite \`${file}\` whole. For each inventory item, give a verdict: present (the rewrite still says it — in other words, or by an accurate pointer to where it lives), weakened (says less: a condition, a case, an exception, or its force lost), missing, or retired (the brief retires it). Then list under "added" anything the rewrite says that the inventory does not: new obligations, changed meanings, new ambiguities. Judge meaning only, never style or length.

Inventory:
${invText(inv)}`

const synthPrompt = (u, inv, wrote, checks) => `${COMMON}

You are the judge and synthesizer for \`${u.path}\`. Read the original (at its repo path), the unit brief \`${u.brief}\`, the style notes \`${STYLE}\`, and the rewrites in \`${udir(u.path)}/\`: ${Object.keys(wrote).sort().map(k => ({A: 'v-A.md (line edit)', B: 'v-B.md (re-derived from the inventory)', C: 'v-C.md (restructured; another model)'})[k]).join(', ')}. Their writers' notes and blind checks are below.

Produce the final version at \`${udir(u.path)}/final.md\`:
1. Pick the base: the rewrite with the best combination of fewest words and fewest missing or weakened items, readable at the step its reader acts.
2. Graft: where another rewrite says a section more briefly without loss, or keeps an item the base lost, take it.
3. Restore each item the checks found missing or weakened, unless the brief retires it or you accept the loss: accept one only where the case is rare and the saving real, never a core item for a few words. List each accepted loss (item id, what it said, why, minor or significant). The operator allows minor losses where the cut justifies them.
4. Add nothing beyond the inventory: no new rules, no clarifications (record a defect instead).
5. Run \`${CHECK} ${u.path} ${udir(u.path)}/final.md\` until no violations remain.

Inventory:
${invText(inv)}

Writers' reports:
${JSON.stringify(wrote, null, 1)}

Blind checks (per variant):
${JSON.stringify(checks, null, 1)}

Your final output is the structured result. In framing_ranking and techniques, be specific: this run is also an experiment in which framing and which cut techniques work.`

const repairPrompt = (u, inv, problems) => `${COMMON}

You repair \`${udir(u.path)}/final.md\`, a compacted rewrite of \`${u.path}\` (read the original at its repo path for wording). A blind check found these inventory items missing, weakened or changed in it:
${problems}

For each: restore what the original says only where a reader acting under the rewrite would now act differently (a lost condition, case, exception, force or obligation, or a real new ambiguity); ignore pure wording differences and lost support (pointers, rationale) the reader does not need there. Otherwise in the fewest words that keep it, in the place its reader needs it — unless it is retired by the unit brief \`${u.brief}\`, or the loss is minor and you judge the words not worth it, which you list with your reason. Change nothing else. Then run \`${CHECK} ${u.path} ${udir(u.path)}/final.md\` until no violations remain. Return what you restored and what you accepted as lost.`

const REPAIRED = { type: 'object', properties: { restored: { type: 'array', items: { type: 'string' } }, accepted_losses: { type: 'array', items: { type: 'object', properties: { item: { type: 'string' }, says: { type: 'string' }, reason: { type: 'string' }, severity: { type: 'string', enum: ['minor', 'significant'] } }, required: ['item', 'says', 'reason', 'severity'] } }, words: { type: 'integer' } }, required: ['restored', 'accepted_losses', 'words'] }

const units = args.units
const results = await pipeline(
  units,
  // 1. inventory + critic
  async (u) => {
    const inv = await agent(`${COMMON}

You are the inventory extractor for one file: \`${u.path}\`. Read it whole, and the unit brief \`${u.brief}\`. Extract its rule inventory: every normative statement — an obligation, prohibition, permission, condition, definition, format, procedure step, ordering, a pointer telling the reader where a rule lives — and each rationale and example, as atomic items. One item is one thing a reader must do, may do, must not do or must know, or one reason or example. Keep a condition attached to the rule it conditions. A rule restated within the file is one item. Criticality: core (a reader acting without it would act wrongly in a case that commonly arises), edge (the same, in a rare case), support (rationale, example, emphasis, or a pointer to a rule stated elsewhere). Record contradictions, gaps or unclear rules you notice as defects. Write no file.`,
      { label: `inv:${slug(u.path)}`, phase: 'Inventory', schema: INV, effort: 'high' })
    if (!inv) throw new Error('inventory failed')
    if (u.small) return { inv }
    const crit = await agent(`${COMMON}

You are the completeness critic for a rule inventory of \`${u.path}\`. Read the file whole. Below is the inventory another agent extracted. Find every normative statement, condition, exception, format detail or ordering the file carries that no item captures, or that an item states imprecisely (lost condition, wrong force). Return only the additions and corrections as items (new ids continue from N1; a correction reuses the item's id). Write no file.

Inventory:
${invText(inv)}`, { label: `crit:${slug(u.path)}`, phase: 'Inventory', schema: INV, effort: 'high' })
    if (crit) {
      const byId = new Map(inv.items.map(i => [i.id, i]))
      for (const i of crit.items) byId.set(i.id, i)
      inv.items = [...byId.values()]
      inv.defects = [...inv.defects, ...crit.defects]
    }
    return { inv }
  },
  // 2. writers, 3. checks
  async ({ inv }, u) => {
    const heads = '(read them from the corpus map entry for this file: ' + `${WS}/corpus-map.json` + ')'
    const frames = u.frames || ['A', 'B', 'C']
    const wrote = {}, checks = {}
    await parallel(frames.map(X => async () => {
      const w = await agent(writerPrompt(u, inv, heads, X), { label: `write-${X}:${slug(u.path)}`, phase: 'Write', schema: WROTE, ...(FRAMES[X].model ? { model: FRAMES[X].model } : {}) })
      if (!w) return
      wrote[X] = w
      const c = await agent(checkPrompt(u, inv, `${udir(u.path)}/v-${X}.md`), { label: `check-${X}:${slug(u.path)}`, phase: 'Check', schema: VERDICTS, effort: 'high' })
      if (c) checks[X] = { missing_or_weakened: c.items.filter(i => i.verdict === 'missing' || i.verdict === 'weakened'), added: c.added }
    }))
    return { inv, wrote, checks }
  },
  // 4. synthesis, 5. final check + repair
  async ({ inv, wrote, checks }, u) => {
    if (!Object.keys(wrote).length) throw new Error('no variants')
    const s = await agent(synthPrompt(u, inv, wrote, checks), { label: `synth:${slug(u.path)}`, phase: 'Synthesize', schema: SYNTH })
    if (!s) throw new Error('synthesis failed')
    let repairs = []
    let fin = null
    for (let k = 0; k < 2; k++) {
      fin = await agent(checkPrompt(u, inv, `${udir(u.path)}/final.md`), { label: `verify${k}:${slug(u.path)}`, phase: 'Verify', schema: VERDICTS, effort: 'high' })
      if (!fin) break
      const bad = fin.items.filter(i => i.verdict === 'missing' || i.verdict === 'weakened')
      const accepted = new Set([...s.accepted_losses.map(l => l.item), ...repairs.flatMap(r => r.accepted_losses.map(l => l.item))])
      const crit = id => ((inv.items.find(x => x.id === id) || {}).criticality || 'core')
      const open = bad.filter(i => !accepted.has(i.id) && crit(i.id) !== 'support')
      if (!open.length && !fin.added.length) break
      const problems = [...open.map(i => `${i.id} (${i.verdict}): ${(inv.items.find(x => x.id === i.id) || {}).says || ''} — ${i.detail || ''}`), ...fin.added.map(a => `ADDED/CHANGED: ${a}`)].join('\n')
      const r = await agent(repairPrompt(u, inv, problems), { label: `repair${k}:${slug(u.path)}`, phase: 'Verify', schema: REPAIRED })
      if (r) repairs.push(r)
    }
    return { inv, wrote, checks, s, fin, repairs }
  },
  // 6. behavioural QA
  async (prev, u) => {
    if (u.small) return prev
    const n = Math.max(4, Math.min(14, Math.round((u.words || 800) / 120)))
    const qs = await agent(`${COMMON}

Read \`${u.path}\` whole (the original, at its repo path). Write ${n} scenario questions a reader acting under this file would face, each answerable from this file alone, chosen to exercise its core and edge items — conditions, exceptions, orderings, formats — what a compressed rewrite most likely loses, spread across the file. Never ask about a support item (an anecdote, an example's details, a rationale): a rewrite may drop those on purpose. For each, the answer the original gives (cite its words briefly), and the ids of the inventory items it tests. Write no file.

Inventory:
${invText({ items: prev.inv.items.filter(i => i.criticality !== 'support') })}`, { label: `qgen:${slug(u.path)}`, phase: 'QA', schema: QS, effort: 'high' })
    if (!qs) return prev
    const ans = await agent(`${COMMON}

Read \`${udir(u.path)}/final.md\` whole: it is the text you act under (a rewrite of \`${u.path}\`; do NOT open that original). You may read other repo files it points to. Answer each question as a reader acting under that text would, briefly. Where the text does not settle a question, say "not settled" and what you would do.

${qs.questions.map(q => `${q.id}: ${q.q}`).join('\n')}`, { label: `qans:${slug(u.path)}`, phase: 'QA', schema: ANS, effort: 'high' })
    if (!ans) return { ...prev, qs }
    const gr = await agent(`Grade answers against expected answers. For each question: match (same action/outcome), partial (right action, a condition or detail lost), diverge (different action or outcome, or not settled where the expected answer is definite). For partial and diverge, name what the rewrite lost or changed. Judge substance, not wording.

${qs.questions.map(q => `${q.id}: ${q.q}\nEXPECTED: ${q.expected}\nGOT: ${(ans.answers.find(a => a.id === q.id) || {}).a || '(none)'}`).join('\n\n')}`, { label: `qgrade:${slug(u.path)}`, phase: 'QA', schema: GRADE, effort: 'medium' })
    let qaRepair = null
    const bad = gr ? gr.grades.filter(g => g.grade === 'diverge') : []
    if (bad.length) {
      const problems = bad.map(g => { const q = qs.questions.find(x => x.id === g.id); return `Scenario: ${q.q}\nThe original's answer: ${q.expected}\nUnder the rewrite: ${g.cause || ''} (items ${q.items.join(', ')})` }).join('\n\n')
      qaRepair = await agent(repairPrompt(prev.u || u, prev.inv, problems), { label: `qarepair:${slug(u.path)}`, phase: 'QA', schema: REPAIRED })
    }
    return { ...prev, qs, ans, gr, qaRepair }
  },
)

const summary = results.map((r, i) => {
  const u = units[i]
  if (!r) return { path: u.path, failed: true }
  const lastWords = r.qaRepair ? r.qaRepair.words : (r.repairs && r.repairs.length ? r.repairs[r.repairs.length - 1].words : (r.s ? r.s.words : null))
  return {
    path: u.path,
    words_orig: u.words,
    variants: Object.fromEntries(Object.entries(r.wrote || {}).map(([k, v]) => [k, v.words])),
    variant_misses: Object.fromEntries(Object.entries(r.checks || {}).map(([k, v]) => [k, v.missing_or_weakened.length])),
    base: r.s && r.s.base,
    final_words: lastWords,
    accepted_losses: [...((r.s && r.s.accepted_losses) || []), ...((r.repairs || []).flatMap(x => x.accepted_losses)), ...((r.qaRepair && r.qaRepair.accepted_losses) || [])].length,
    qa: r.gr ? r.gr.grades.reduce((a, g) => (a[g.grade] = (a[g.grade] || 0) + 1, a), {}) : null,
  }
})
return { summary, spent: budget.spent() }
