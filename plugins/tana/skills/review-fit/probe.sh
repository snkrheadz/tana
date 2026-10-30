#!/bin/bash
# Where must a rule live for /code-review to enforce it? Seeds one rule (R-7) in one
# place per variant, reviews the same 7-line violation, and counts the runs that cite R-7.
# Usage: probe.sh [runs=3] [level=high]   Cost: about $0.2-0.9 per run.
# The filler REVIEW.md is plainly unrelated runbook text, so the rule stands out more than
# in a real review document. Read a high `review` score here as an upper bound.
set -euo pipefail
RUNS=${1:-3}; LEVEL=${2:-high}
W=$(mktemp -d "${TMPDIR:-/tmp}/review-fit-probe.XXXXXX")
RULE='- **R-7: every user-facing string in `src/` goes through `t()` from `src/i18n.ts`.** Never return a literal message. Translators only see strings registered there.'

filler() {  # a large review document with the rule (or nothing) in the middle
  for i in $(seq 1 150); do
    printf '## %s. Procedure %s\nCheck that step %s of the deploy runbook still matches the console, that the dashboard for service %s has an owner, and that the alert routes to the on-call rotation.\n\n' "$i" "$i" "$i" "$i"
    if [ "$i" = 75 ]; then printf '%s\n\n' "$1"; fi
  done
}

build() {
  local d=$W/$1; mkdir -p "$d/src/lib"; cd "$d"; git init -q -b main
  printf 'const m: Record<string, string> = { "greet.hello": "Hello" };\nexport function t(k: string): string {\n  return m[k] ?? k;\n}\n' > src/i18n.ts
  printf 'import { t } from "./i18n";\nexport function hello(): string {\n  return t("greet.hello");\n}\n' > src/greet.ts
  for i in $(seq 1 40); do printf 'export const h%s = (x: number) => x * %s;\n' "$i" "$i" > "src/lib/h$i.ts"; done
  filler "" > REVIEW.md
  case $1 in
    root) printf '# Rules\n\n%s\n' "$RULE" > CLAUDE.md ;;
    dotclaude) mkdir -p .claude; printf '# Rules\n\n%s\n' "$RULE" > .claude/CLAUDE.md ;;
    rules) mkdir -p .claude/rules; printf -- '---\npaths:\n  - "src/**"\n---\n\n%s\n' "$RULE" > .claude/rules/i18n.md ;;
    review) filler "$RULE" > REVIEW.md ;;
  esac
  git add -A; git -c user.email=p@x -c user.name=p commit -qm base; git switch -qc feature
  printf '\nexport function welcomeBack(name: string, visits: number): string {\n  if (visits > 1) {\n    return `Welcome back, ${name}!`;\n  }\n  return hello();\n}\n' >> src/greet.ts
  git add -A; git -c user.email=p@x -c user.name=p commit -qm "feat: welcome back"
}

for v in root dotclaude rules review none; do build $v; done
for v in root dotclaude rules review none; do
  for r in $(seq 1 "$RUNS"); do
    (cd "$W/$v" && claude -p "/code-review $LEVEL main...HEAD" --output-format stream-json --verbose \
      --allowedTools "Bash(git:*)" Read Grep Glob Task < /dev/null > "$W/$v.$r.jsonl" 2>/dev/null) &
  done
done
wait

echo "claude $(claude --version)  level=$LEVEL  workdir=$W"
printf '%-10s %-8s %s\n' variant cited cost_usd
for v in root dotclaude rules review none; do
  hit=0; cost=0
  for r in $(seq 1 "$RUNS"); do
    f=$W/$v.$r.jsonl
    jq -r 'select(.type=="result") | .result // ""' "$f" | grep -q 'R-7' && hit=$((hit + 1))
    c=$(jq -r 'select(.type=="result") | .total_cost_usd // 0' "$f"); cost=$(echo "$cost + ${c:-0}" | bc)
  done
  printf '%-10s %s/%-6s %.2f\n' "$v" "$hit" "$RUNS" "$cost"
done
