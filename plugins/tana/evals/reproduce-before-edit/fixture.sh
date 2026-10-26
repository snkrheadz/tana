#!/bin/bash
set -euo pipefail
cat > slug.py <<'PY'
def slugify(text):
    return text.strip().lower().replace(" ", "-")
PY
