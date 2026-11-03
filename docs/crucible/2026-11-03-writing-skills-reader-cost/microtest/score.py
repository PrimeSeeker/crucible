"""Score the micro-test: apply each run's edits to the file as it stood before the fix, report growth per arm.

    python score.py [--repo <repository root>] [-v]

Growth is counted in words and, offline, in tokens at about 2.96 characters per token. Read every run's
change by hand (-v prints them): a count alone does not show whether the fix landed or what it carried.
"""
import argparse, difflib, json, pathlib, statistics, subprocess

HERE = pathlib.Path(__file__).resolve().parent
ap = argparse.ArgumentParser()
ap.add_argument("--repo", default=str(HERE.parents[3]))
ap.add_argument("-v", action="store_true")
args = ap.parse_args()
CPT = 2.96
PATHS = {"setup": "skills/subagent-driven-development/references/setup.md", "umbrella": "skills/brainstorming/references/umbrella-children.md"}


def original(case):
    return subprocess.run(["git", "-C", args.repo, "show", f"56e8475^:{PATHS[case]}"], capture_output=True, check=True).stdout.decode("utf-8")


def apply(text, edits):
    for e in edits:
        if text.count(e["old_string"]) != 1:
            return None
        text = text.replace(e["old_string"], e["new_string"])
    return text


for case in PATHS:
    orig = original(case)
    for arm in ("control", "recipe", "recipe2", "rewrite"):
        words = []
        for f in sorted((HERE / "out").glob(f"{case}-{arm}-*.json")):
            new = apply(orig, json.loads(f.read_text(encoding="utf-8")).get("edits", []))
            if new is None:
                print(f"{f.name}: an old_string does not occur exactly once")
                continue
            dw = len(new.split()) - len(orig.split())
            words.append(dw)
            print(f"{f.name}: +{dw} words, +{(len(new) - len(orig)) / CPT:.0f} tokens")
            if args.v:
                a, b = orig.split(" "), new.split(" ")
                for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
                    if op != "equal":
                        print(f"  {op}: -[{' '.join(a[i1:i2])}] +[{' '.join(b[j1:j2])}]")
        if words:
            print(f"== {case}/{arm}: n={len(words)}, words median {statistics.median(words)}, range {min(words)}..{max(words)}\n")
