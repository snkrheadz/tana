#!/bin/bash
# Regenerate plugins/tana/FILES, the list a cloud setup script downloads.
# Usage: scripts/update-files.sh [--check]   (--check exits 1 if FILES is stale)
set -euo pipefail
cd "$(dirname "$0")/.."
list=$(git ls-files plugins/tana | grep -v '/evals/' | grep -v '^plugins/tana/FILES$' | sed 's|^plugins/tana/||' | sort)
if [[ "${1:-}" == "--check" ]]; then
    diff <(printf '%s\n' "$list") plugins/tana/FILES >/dev/null || { echo "plugins/tana/FILES is stale: run scripts/update-files.sh" >&2; exit 1; }
    exit 0
fi
printf '%s\n' "$list" > plugins/tana/FILES
