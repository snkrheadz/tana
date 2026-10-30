#!/bin/bash
set -euo pipefail
c() { git -c user.email=e@x -c user.name=e commit -qm "$1"; }
mkdir -p .github/workflows src .claude
cat > CLAUDE.md <<'EOF'
# catalog-api

TypeScript service. `bun test` runs the tests.

- Keep HTTP handlers in `src/api/`; pure rules in `src/lib/`.
- When a review finding comes back a second time, turn it into a test or lint rule.
EOF
cat > .github/workflows/review.yml <<'EOF'
name: review
on: pull_request
jobs:
  review:
    runs-on: ubuntu-latest
    permissions: { pull-requests: write }
    steps:
      - uses: actions/checkout@v4
        with: { fetch-depth: 0 }
      - run: npm i -g @anthropic-ai/claude-code
      # Writes review.json: { "findings": [ { "file", "line", "category", "verdict", "rule", "summary" } ] }
      - run: claude -p "/code-review high origin/main...HEAD" --output-format json > review.json
      - uses: actions/upload-artifact@v4
        with: { name: review, path: review.json, retention-days: 14 }
      # One sticky comment per PR, overwritten on every push.
      - run: node scripts/post-sticky-comment.js review.json
EOF
cat > .claude/settings.json <<'EOF'
{ "hooks": {} }
EOF
cat > NOTES.md <<'EOF'
# Team notes

- 2026-09: we opened `harness-improvement` issues for repeated review findings. Twelve are open; nobody has looked at them since.
- The reviewer has flagged "handler calls the database directly" on PR #41, #57 and #63. Each time the author fixed that one handler.
EOF
echo 'export const ok = true;' > src/index.ts
git add -A; c "catalog-api"
