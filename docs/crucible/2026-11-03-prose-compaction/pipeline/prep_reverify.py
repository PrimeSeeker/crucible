"""Write per-unit inventory, accepted losses and open QA items from a compaction journal.

Usage: python prep_reverify.py <journal-extract.json> <args.json> <out-args.json>
Writes units/<slug>/inventory.json, accepted.json, qa-open.md (when QA left partial/diverge),
and an args file for reverify.js.
"""
import json
import sys
from pathlib import Path

WS = Path(__file__).resolve().parent.parent
d = json.load(open(sys.argv[1], encoding="utf-8"))
units = json.load(open(sys.argv[2], encoding="utf-8"))["units"]
out = []
for u in units:
    s = u["path"].removeprefix("skills/").removesuffix(".md").replace("/", "__")
    ud = WS / "units" / s
    inv = d[f"inv:{s}"]
    by = {i["id"]: i for i in inv["items"]}
    crit = d.get(f"crit:{s}")
    if crit:
        for i in crit["items"]:
            by[i["id"]] = i
    items = list(by.values())
    json.dump({"items": items}, open(ud / "inventory.json", "w", encoding="utf-8", newline="\n"), indent=1)
    acc = list(d.get(f"synth:{s}", {}).get("accepted_losses", []))
    for k in ("repair0", "repair1", "qarepair"):
        r = d.get(f"{k}:{s}")
        if r:
            acc += r.get("accepted_losses", [])
    json.dump(acc, open(ud / "accepted.json", "w", encoding="utf-8", newline="\n"), indent=1)
    qa, qq = [], []
    qs, gr = d.get(f"qgen:{s}"), d.get(f"qgrade:{s}")
    if qs and gr:
        for g in gr["grades"]:
            if g["grade"] != "match":
                q = next(x for x in qs["questions"] if x["id"] == g["id"])
                qa.append(f"### {q['id']} ({g['grade']})\nScenario: {q['q']}\nThe original's answer: {q['expected']}\nWhat the rewrite lost: {g.get('cause') or ''}\n")
                qq.append(f"### {q['id']}\n{q['q']}\n")
    for name, body in (("qa-open.md", qa), ("qa-questions.md", qq)):
        qp = ud / name
        if body:
            open(qp, "w", encoding="utf-8", newline="\n").write("\n".join(body))
        elif qp.exists():
            qp.unlink()
    out.append({"path": u["path"], "brief": u["brief"], "qa": len(qa), "core_edge": sum(i["criticality"] != "support" for i in items)})
json.dump({"units": out}, open(sys.argv[3], "w", encoding="utf-8"), indent=1)
print(len(out), "units;", sum(1 for x in out if x["qa"]), "with open QA items")
