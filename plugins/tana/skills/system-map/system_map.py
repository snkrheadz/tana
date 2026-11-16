"""Read Terraform files, list what they declare, and draw a checked Mermaid flowchart.

Usage:
  python3 -I system_map.py scan DIR...          what each Terraform folder declares, by type
  python3 -I system_map.py show PATTERN DIR...  one resource: file, line, plain values, uses, used by
  python3 -I system_map.py draw MAP.json DIR... check the map against the files, print the chart

PATTERN is a glob over `folder:type.name`. Without a colon it matches in every folder.
`draw` exits 1 and prints no chart when a box or an arrow has nothing behind it.
"""
import fnmatch
import json
import os
import re
import sys
from collections import Counter

SKIP_DIRS = {".terraform", ".git", "node_modules"}
HEADER = re.compile(r'(resource|data|module|variable|locals)((?:[ \t]+"[^"\n]*")*)[ \t]*\{')
USE = re.compile(r"(?<![\w.])(data\.[a-z0-9_]+\.[\w-]+|module\.[\w-]+|local\.[\w-]+|var\.[\w-]+|[a-z][a-z0-9]*_[a-z0-9_]+\.[A-Za-z_][\w-]*)")
ATTR = re.compile(r'^\s*([A-Za-z_][\w-]*)\s*=(?!=)\s*(.*?)\s*$')
OPENER = re.compile(r'^\s*(?:(dynamic)\s+"([^"]+)"|([A-Za-z_][\w-]*)(?:\s+"[^"]*")*|([A-Za-z_][\w-]*)\s*=)\s*\{\s*$')
PLAIN = re.compile(r'"[^"$%\\]*"|true|false|-?\d+(?:\.\d+)?')
PLAIN_LIST = re.compile(r'\[\s*(?:"[^"$%\\]*"\s*,?\s*)*\]')
HEREDOC = re.compile(r"<<-?([A-Za-z_]\w*)[ \t]*\n")
EVIDENCE = re.compile(r"^(.+):(\d+)$")
NODE_ID = re.compile(r"^[A-Za-z0-9_]+$")


def code_view(text):
    """Return text of the same length with comments and string contents blanked.

    Code inside `${...}` stays, so a reference in a string or a heredoc is still found.
    """
    out = list(text)
    n = len(text)

    def blank(a, b):
        for k in range(a, b):
            if out[k] != "\n":
                out[k] = " "

    def template(i):
        depth = 1
        while i < n and depth:
            c = text[i]
            if c == '"':
                i = quoted(i)
                continue
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    blank(i, i + 1)
            i += 1
        return i

    def quoted(i):
        i += 1
        while i < n and text[i] not in '"\n':
            if text[i] == "\\":
                blank(i, i + 2)
                i += 2
            elif text.startswith("${", i):
                blank(i, i + 2)
                i = template(i + 2)
            else:
                blank(i, i + 1)
                i += 1
        return i + 1

    def heredoc(i, m):
        end = re.compile(r"^[ \t]*" + re.escape(m.group(1)) + r"[ \t]*$", re.M).search(text, m.end())
        stop = end.end() if end else n
        blank(i, m.end())
        j = m.end()
        while j < stop:
            if text.startswith("${", j) and (j == 0 or text[j - 1] != "$"):
                blank(j, j + 2)
                j = template(j + 2)
            else:
                blank(j, j + 1)
                j += 1
        return stop

    i = 0
    while i < n:
        c = text[i]
        if c == "#" or text.startswith("//", i):
            j = text.find("\n", i)
            j = n if j < 0 else j
            blank(i, j)
            i = j
        elif text.startswith("/*", i):
            j = text.find("*/", i)
            j = n if j < 0 else j + 2
            blank(i, j)
            i = j
        elif c == '"':
            i = quoted(i)
        elif text.startswith("<<", i) and (m := HEREDOC.match(text, i)):
            i = heredoc(i, m)
        else:
            i += 1
    return "".join(out)


def block_end(code, start):
    depth = 0
    for i in range(start, len(code)):
        if code[i] == "{":
            depth += 1
        elif code[i] == "}":
            depth -= 1
            if depth == 0:
                return i
    return len(code) - 1


def plain_value(raw):
    if PLAIN_LIST.fullmatch(raw):
        return re.findall(r'"([^"]*)"', raw)
    if PLAIN.fullmatch(raw):
        return raw[1:-1] if raw.startswith('"') else json.loads(raw)
    return None


def attributes(text, code, start, end, first_line):
    """Yield (path, raw value, line, offset) for each `key = value` line in a block body."""
    stack = []
    line_no = first_line
    pos = start
    for line, cline in zip(text[start:end].split("\n"), code[start:end].split("\n")):
        if cline.strip():
            line = line[: len(cline.rstrip())]
            indent = len(line) - len(line.lstrip())
            opener = OPENER.match(line) if cline.rstrip().endswith("{") else None
            attr = ATTR.match(line) if not opener and cline[indent : indent + 1].strip() else None
            if attr:
                yield ".".join([s for s in stack if s] + [attr.group(1)]), attr.group(2), line_no, pos
            net = cline.count("{") - cline.count("}")
            if net > 0:
                name = ""
                if opener:
                    name = opener.group(2) or opener.group(3) or opener.group(4)
                    if name == "content" and stack and stack[-1].startswith("dynamic:"):
                        name = ""
                    elif opener.group(1):
                        name = "dynamic:" + name
                stack += [name] + [""] * (net - 1)
            elif net < 0:
                del stack[net:]
        line_no += 1
        pos += len(line) + 1


def uses_in(code, start, end, line_of):
    found = {}
    for m in USE.finditer(code, start, end):
        found.setdefault(m.group(1), line_of(m.start()))
    return found


def scan_folder(folder, label):
    """Return the resources, data sources, and module calls that one folder's .tf files declare."""
    resources, local_uses, variables = {}, {}, {}
    names = sorted(os.listdir(folder))
    for name in names:
        path = os.path.join(folder, name)
        if not os.path.isfile(path) or not name.endswith((".tf", ".tfvars")):
            continue
        with open(path, encoding="utf-8") as f:
            text = f.read()
        code = code_view(text)
        starts = [0] + [i + 1 for i, c in enumerate(text) if c == "\n"]

        def line_of(pos, starts=starts):
            lo, hi = 0, len(starts) - 1
            while lo < hi:
                mid = (lo + hi + 1) // 2
                lo, hi = (mid, hi) if starts[mid] <= pos else (lo, mid - 1)
            return lo + 1

        if name.endswith(".tfvars"):
            for key, raw, _, _ in attributes(text, code, 0, len(text), 1):
                if "." not in key and plain_value(raw) is not None:
                    variables[key] = plain_value(raw)
            continue
        pos = 0
        while pos < len(text):
            at_line_start = pos == 0 or text[pos - 1] == "\n"
            m = HEADER.match(text, pos) if at_line_start and code[pos : pos + 1].strip() else None
            if not m:
                nl = text.find("\n", pos)
                pos = len(text) if nl < 0 else nl + 1
                continue
            kind = m.group(1)
            labels = re.findall(r'"([^"]*)"', m.group(2))
            end = block_end(code, m.end() - 1)
            body = (m.end(), end)
            first = line_of(m.start())
            attrs = list(attributes(text, code, body[0], body[1], line_of(body[0])))
            if kind == "locals":
                tops = [(key, at) for key, _, _, at in attrs if "." not in key]
                for (key, at), nxt in zip(tops, [at for _, at in tops[1:]] + [end]):
                    local_uses.setdefault(key, {}).update(uses_in(code, at, nxt, line_of))
            elif kind == "variable" and labels:
                for key, raw, _, _ in attrs:
                    if key == "default" and plain_value(raw) is not None:
                        variables.setdefault("default:" + labels[0], plain_value(raw))
            elif (kind == "module" and len(labels) == 1) or (kind in ("resource", "data") and len(labels) == 2):
                short = {"resource": "", "data": "data.", "module": "module."}[kind] + ".".join(labels)
                values = {}
                for key, raw, _, _ in attrs:
                    value = plain_value(raw)
                    if value is not None:
                        key = key.replace("dynamic:", "")
                        values.setdefault(key, [])
                        values[key] += [v for v in (value if isinstance(value, list) else [value]) if v not in values[key]]
                resources[label + ":" + short] = {
                    "folder": label, "short": short, "file": os.path.relpath(path), "line": first,
                    "values": values, "raw_uses": uses_in(code, body[0], body[1], line_of),
                }
            pos = end + 1
    for name in [k for k in variables if k.startswith("default:")]:
        variables.setdefault(name[len("default:"):], variables.pop(name))

    def through_locals(found, seen):
        out = {}
        for ref, line in found.items():
            if ref.startswith("local."):
                key = ref[len("local."):]
                if key not in seen:
                    for inner in through_locals(local_uses.get(key, {}), seen | {key}):
                        out.setdefault(inner, line)
            else:
                out.setdefault(ref, line)
        return out

    for res in resources.values():
        found = through_locals(res.pop("raw_uses"), frozenset())
        res["uses"] = {label + ":" + r: ln for r, ln in found.items() if label + ":" + r in resources and r != res["short"]}
        res["vars"] = {r[4:]: variables.get(r[4:]) for r in found if r.startswith("var.")}
    return resources


def scan(dirs):
    """Return every resource, data source, and module call under dirs, keyed by `folder:type.name`."""
    inventory = {}
    for top in dirs:
        if not os.path.isdir(top):
            sys.exit("not a folder: %s" % top)
        for folder, subdirs, files in os.walk(top):
            subdirs[:] = sorted(d for d in subdirs if d not in SKIP_DIRS)
            if any(f.endswith(".tf") for f in files):
                inventory.update(scan_folder(folder, os.path.relpath(folder)))
    return inventory


def match(inventory, pattern):
    key = (lambda a: a) if ":" in pattern else (lambda a: inventory[a]["short"])
    return [a for a in inventory if fnmatch.fnmatchcase(key(a), pattern)]


def used_by(inventory):
    back = {a: {} for a in inventory}
    for a, res in inventory.items():
        for b, line in res["uses"].items():
            back[b][a] = line
    return back


def where(res, line=None):
    return "%s:%d" % (res["file"], line or res["line"])


def cmd_scan(inventory):
    lines = []
    for folder in sorted({r["folder"] for r in inventory.values()}):
        types = Counter(r["short"].rsplit(".", 1)[0] for r in inventory.values() if r["folder"] == folder)
        lines.append("%s  (%d declared)" % (folder, sum(types.values())))
        lines += ["  %4d  %s" % (count, name) for name, count in sorted(types.items(), key=lambda t: (-t[1], t[0]))]
    return lines or ["no .tf files found"]


def cmd_show(inventory, pattern):
    hits = match(inventory, pattern)
    if len(hits) > 3:
        return ["%s  %s" % (a, where(inventory[a])) for a in hits]
    back = used_by(inventory)
    lines = []
    for a in hits:
        res = inventory[a]
        lines.append("%s  %s" % (a, where(res)))
        lines += ["  %s = %s" % (k, json.dumps(v[0] if len(v) == 1 else v, ensure_ascii=False)) for k, v in res["values"].items()]
        lines += ["  var.%s = %s" % (k, json.dumps(v, ensure_ascii=False)) for k, v in res["vars"].items()]
        lines += ["  uses     %s  %s" % (inventory[b]["short"], where(res, ln)) for b, ln in res["uses"].items()]
        lines += ["  used by  %s  %s" % (inventory[b]["short"], where(inventory[b], ln)) for b, ln in back[a].items()]
    return lines or ["nothing matches %s" % pattern]


def evidence_problem(text):
    m = EVIDENCE.match(text or "")
    if not m:
        return "evidence must be path:line, got %r" % text
    path, line = m.group(1), int(m.group(2))
    if not os.path.isfile(path):
        return "evidence file not found: %s" % path
    with open(path, encoding="utf-8", errors="replace") as f:
        rows = f.read().split("\n")
    if not 1 <= line <= len(rows) or not rows[line - 1].strip():
        return "evidence line is missing or blank: %s" % text
    return None


def links(inventory, owner):
    """Map (box, box) to the place in the files that ties the two boxes together.

    Two boxes are tied when one uses the other, directly or through resources that sit in no box,
    or when a resource outside every box uses those two boxes and no third, as an access grant does.
    """
    found = {}

    def note(a, b, place):
        if a != b:
            found.setdefault((a, b), place)
            found.setdefault((b, a), place)

    for start, res in sorted(inventory.items(), key=lambda item: item[0] not in owner):
        box = owner.get(start)
        if box is None:
            direct = sorted({owner[b] for b in res["uses"] if b in owner})
            if len(direct) == 2:
                note(direct[0], direct[1], "%s at %s uses both" % (res["short"], where(res)))
            continue
        frontier, seen = list(res["uses"].items()), {start}
        while frontier:
            target, line = frontier.pop()
            if target in seen:
                continue
            seen.add(target)
            if target in owner:
                note(box, owner[target], "%s at %s" % (res["short"], where(res, line)))
            else:
                frontier += [(b, line) for b in inventory[target]["uses"]]
    return found


def label_text(text):
    return str(text).replace('"', "#quot;").replace("\n", "<br/>")


def draw(inventory, spec):
    """Return (chart, errors, report). The chart is None when there are errors."""
    errors, report = [], []
    nodes, edges = spec.get("nodes", {}), spec.get("edges", [])
    owner = {}
    for key, node in nodes.items():
        if not NODE_ID.match(key):
            errors.append("box %r: use only letters, digits, and _ in a box name" % key)
        patterns = node.get("is", [])
        patterns = [patterns] if isinstance(patterns, str) else patterns
        if not patterns:
            problem = evidence_problem(node.get("evidence"))
            if problem:
                errors.append("box %r names nothing in the Terraform files, so it needs evidence: %s" % (key, problem))
        elif node.get("evidence") and evidence_problem(node["evidence"]):
            errors.append("box %r: %s" % (key, evidence_problem(node["evidence"])))
        for pattern in patterns:
            hits = match(inventory, pattern)
            if not hits:
                errors.append("box %r: nothing in the Terraform files matches %r" % (key, pattern))
            for a in hits:
                if owner.setdefault(a, key) != key:
                    errors.append("%s is in two boxes: %r and %r" % (a, owner[a], key))
    tied = links(inventory, owner)
    drawn, from_files = set(), 0
    for edge in edges:
        a, b = edge.get("from"), edge.get("to")
        if a not in nodes or b not in nodes:
            errors.append("arrow %r -> %r: no such box" % (a, b))
            continue
        drawn.add((a, b))
        drawn.add((b, a))
        if edge.get("evidence"):
            problem = evidence_problem(edge["evidence"])
            if problem:
                errors.append("arrow %s -> %s: %s" % (a, b, problem))
        elif (a, b) in tied:
            from_files += 1
        else:
            errors.append("arrow %s -> %s: no reference in the Terraform files ties these boxes. Add evidence (path:line) or remove the arrow" % (a, b))
    if errors:
        return None, errors, report
    report.append("OK %d boxes, %d arrows (%d backed by a Terraform reference, %d by evidence)" % (len(nodes), len(edges), from_files, len(edges) - from_files))
    missing = sorted((a, b) for (a, b) in tied if a < b and (a, b) not in drawn)
    if missing:
        report.append("Tied in the files but not drawn (%d):" % len(missing))
        report += ["  %s -- %s  (%s)" % (a, b, tied[(a, b)]) for a, b in missing]
    rest = Counter(r["short"].rsplit(".", 1)[0] for a, r in inventory.items() if a not in owner)
    if rest:
        top = ", ".join("%s %d" % t for t in rest.most_common(8))
        report.append("Left out: %d of %d declared (%s%s)" % (sum(rest.values()), len(inventory), top, ", ..." if len(rest) > 8 else ""))

    out = []
    if spec.get("title"):
        out += ["---", "title: " + json.dumps(str(spec["title"]), ensure_ascii=False), "---"]
    out.append("flowchart " + spec.get("direction", "LR"))
    groups = {}
    for key, node in nodes.items():
        groups.setdefault(node.get("group"), []).append(key)
    outside = [k for k, node in nodes.items() if not node.get("is")]

    def box(key, indent):
        text = label_text(nodes[key].get("label", key))
        shape = '[("%s")]' if nodes[key].get("shape") == "store" else '(["%s"])' if key in outside else '["%s"]'
        return "%sn_%s%s" % (indent, key, shape % text)

    for i, (group, keys) in enumerate(groups.items()):
        if group is None:
            out += [box(k, "    ") for k in keys]
        else:
            out.append('    subgraph g%d["%s"]' % (i, label_text(group)))
            out += [box(k, "        ") for k in keys]
            out.append("    end")
    for edge in edges:
        text = '|"%s"|' % label_text(edge["label"]) if edge.get("label") else ""
        out.append("    n_%s -->%s n_%s" % (edge["from"], text, edge["to"]))
    if outside:
        out.append("    classDef outside stroke-dasharray: 4 3")
        out.append("    class %s outside" % ",".join("n_" + k for k in outside))
    return "\n".join(out), errors, report


def main(argv):
    if not argv or argv[0] not in ("scan", "show", "draw") or len(argv) < (2 if argv[0] == "scan" else 3):
        sys.exit(__doc__)
    if argv[0] == "scan":
        print("\n".join(cmd_scan(scan(argv[1:]))))
        return 0
    inventory = scan(argv[2:])
    if argv[0] == "show":
        print("\n".join(cmd_show(inventory, argv[1])))
        return 0
    with open(argv[1], encoding="utf-8") as f:
        chart, errors, report = draw(inventory, json.load(f))
    print("\n".join(errors + report), file=sys.stderr)
    if errors:
        return 1
    print(chart)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
