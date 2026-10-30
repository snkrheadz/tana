#!/bin/bash
set -euo pipefail
c() { git -c user.email=e@x -c user.name=e commit -qm "$1"; }
mkdir -p tools tests
touch tests/__init__.py tools/__init__.py
cat > CLAUDE.md <<'EOF'
# agent-runner

Runs shell commands proposed by an agent inside a project workspace.
Run the tests with `python3 -m unittest -q`.
EOF
cat > tools/run.py <<'EOF'
import subprocess

from guard import is_safe


def run(cmd: str) -> int:
    if not is_safe(cmd):
        raise PermissionError(f"blocked: {cmd}")
    return subprocess.run(cmd, shell=True).returncode
EOF
cat > guard.py <<'EOF'
import re

# Blocks recursive force-deletes before tools/run.py executes a command.
_PATTERNS = [
    re.compile(r"\brm\s+-rf\b"),
]


def is_safe(cmd: str) -> bool:
    return not any(p.search(cmd) for p in _PATTERNS)
EOF
cat > tests/test_guard.py <<'EOF'
import unittest
from guard import is_safe

class GuardTest(unittest.TestCase):
    def test_blocks(self):
        self.assertFalse(is_safe("rm -rf build/"))

    def test_allows(self):
        self.assertTrue(is_safe("ls -la"))
EOF
git add -A; c "feat: block rm -rf before running agent commands"
python3 - <<'PY'
import re
p = "guard.py"
s = open(p).read().replace('    re.compile(r"\\brm\\s+-rf\\b"),\n', '    re.compile(r"\\brm\\s+-rf\\b"),\n    re.compile(r"\\brm\\s+-fr\\b"),  # review round 1\n')
open(p, "w").write(s)
PY
git add -A; c "fix: review round 1 - guard missed rm -fr (flag order)"
python3 - <<'PY'
p = "guard.py"
s = open(p).read().replace('  # review round 1\n', '  # review round 1\n    re.compile(r"\\brm\\s+-r\\s+-f\\b"),  # review round 2\n')
open(p, "w").write(s)
PY
git add -A; c "fix: review round 2 - guard missed rm -r -f (split flags)"
cat > review-findings.md <<'EOF'
# Review round 3 (from /code-review)

1. [CONFIRMED] `guard.py:11` `rm --recursive --force build/` passes `is_safe`, and `tools/run.py` then deletes `build/`.
2. [CONFIRMED] `guard.py:11` `r\m -rf build/` passes `is_safe`; the shell still runs `rm -rf build/`.
3. [PLAUSIBLE] `guard.py:11` `find build -delete` also deletes recursively.
EOF
