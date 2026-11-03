"""Extract a workflow journal into {label: result}. Usage: python journal.py <journal.jsonl> <out.json>"""
import json
import sys

labels, out = {}, {}
for line in open(sys.argv[1], encoding="utf-8"):
    d = json.loads(line)
    if d.get("type") == "started":
        labels[d["key"]] = d["label"]
    elif d.get("type") == "result":
        out[labels.get(d["key"], d["key"])] = d.get("result")
json.dump(out, open(sys.argv[2], "w", encoding="utf-8"), indent=1)
print(len(out), "results")
