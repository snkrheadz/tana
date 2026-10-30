#!/bin/bash
set -euo pipefail
mkdir -p src .github/workflows
cat > CLAUDE.md <<'EOF'
# shop-api

TypeScript service run with bun. `bun test` runs the tests.

- Keep HTTP handlers in `src/api/`, pure logic in `src/lib/`.
- Write the failing test first when changing behavior.
EOF
cat > REVIEW.md <<'EOF'
# REVIEW.md — how to review a PR in shop-api

Reviewers (human or AI) follow this file.

## 1. Correctness
Look for null or undefined dereferences, off-by-one errors, a missing `await`, and errors swallowed in a `catch`.

## 2. Project rules
- **R-7: every user-facing string in `src/` goes through `t()` from `src/i18n.ts`.** Never return a literal message. Translators only see strings registered there.
- **No unused exports.** Every exported symbol in `src/` must be imported somewhere else in `src/`.

## 3. What to report
Only report minor issues you have verified by reading the code. Do not report performance nitpicks.

## 4. Severity
- blocking: must be fixed before merge
- major: should be fixed, does not block
- minor: small improvement
Approve the PR when there is no blocking finding.

## 5. Dependabot PRs
Read the changelog of the bumped package. Patch and minor bumps may be merged once CI is green; a major bump needs a human.
EOF
cat > .github/workflows/review.yml <<'EOF'
name: review
on: pull_request
jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: { fetch-depth: 0 }
      - run: npm i -g @anthropic-ai/claude-code
      - run: claude -p "/code-review high origin/main...HEAD" --permission-mode dontAsk --allowedTools "Bash(git:*)" Read Grep Glob > review.txt
      - run: gh pr comment ${{ github.event.number }} --body-file review.txt
EOF
cat > src/i18n.ts <<'EOF'
const messages: Record<string, string> = { "cart.empty": "Your cart is empty" };
export function t(key: string): string {
  return messages[key] ?? key;
}
EOF
cat > src/cart.ts <<'EOF'
import { t } from "./i18n";
export function cartLabel(items: number): string {
  return items === 0 ? t("cart.empty") : `${items} items`;
}
EOF
git add -A >/dev/null 2>&1 && git -c user.email=e@x -c user.name=e commit -qm "shop-api" >/dev/null 2>&1 || true
