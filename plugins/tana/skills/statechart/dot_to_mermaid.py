"""Turn a TLC `-dump dot,actionlabels` file into a Mermaid stateDiagram.

Usage: python3 -I dot_to_mermaid.py graph.dot > chart.mmd
"""
import re
import sys

NODE = re.compile(r'^\s*(-?\d+)\s*\[label="((?:[^"\\]|\\.)*)"(.*?)\]\s*;?\s*$')
EDGE = re.compile(r'^\s*(-?\d+)\s*->\s*(-?\d+)\s*(?:\[label="((?:[^"\\]|\\.)*)".*\])?\s*;?\s*$')


def clean(text):
    text = text.replace("\\n", ", ").replace("\\\\", "\\").replace('\\"', "'")
    return text.replace("/\\ ", "").strip(", ")


def convert(lines):
    names, starts, edges = {}, [], []
    for line in lines:
        m = EDGE.match(line)
        if m:
            edges.append((m.group(1), m.group(2), m.group(3) or ""))
            continue
        m = NODE.match(line)
        if m:
            names[m.group(1)] = clean(m.group(2))
            if "filled" in m.group(3):
                starts.append(m.group(1))
    ids = {n: "s%d" % i for i, n in enumerate(names)}
    out = ["stateDiagram-v2"]
    out += ['    state "%s" as %s' % (names[n].replace('"', "'"), ids[n]) for n in names]
    out += ["    [*] --> " + ids[n] for n in starts if n in ids]
    for a, b, label in edges:
        if a in ids and b in ids:
            out.append("    %s --> %s%s" % (ids[a], ids[b], ": " + clean(label) if label else ""))
    return "\n".join(out)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    with open(sys.argv[1], encoding="utf-8") as f:
        print(convert(f))
