#!/bin/bash
set -euo pipefail
c() { git -c user.email=e@x -c user.name=e commit -qm "$1"; }
mkdir -p src tests docs
cat > CLAUDE.md <<'EOF'
# ledger

- **No `print()` in `src/`.** Use `log()` from `src/logutil.py`; print output is lost when the service runs under the job runner.
- Run the tests with `python3 -m unittest -q`.
EOF
cat > REVIEW.md <<'EOF'
# Review checklist

- No `print()` in `src/`; use `log()`.
- New behavior has a test.
EOF
cat > docs/contributing.md <<'EOF'
# Contributing

Never call `print()` in `src/`. Use `log()` from `src/logutil.py` instead.
EOF
touch src/__init__.py tests/__init__.py
cat > src/logutil.py <<'EOF'
import sys


def log(msg: str) -> None:
    sys.stderr.write(f"[ledger] {msg}\n")
EOF
cat > src/orders.py <<'EOF'
def place(order_id: int, qty: int) -> int:
    print("placing", order_id)
    total = qty * 100
    print("total", total)
    return total
EOF
cat > src/billing.py <<'EOF'
def charge(cents: int) -> bool:
    print(f"charging {cents}")
    ok = cents > 0
    print("ok" if ok else "declined")
    return ok
EOF
cat > src/report.py <<'EOF'
HELP = "Shows totals. For quick debugging you may be tempted to use print() here; use log() instead."


def summarize(totals: list[int]) -> str:
    print("summarizing", len(totals))
    return f"{len(totals)} orders, {sum(totals)} cents"
EOF
cat > src/cli.py <<'EOF'
"""Command-line entry point. Prints the report to stdout so shell pipes can read it."""
from src.report import summarize


def main() -> None:
    print(summarize([100, 250]))


if __name__ == "__main__":
    main()
EOF
cat > tests/test_orders.py <<'EOF'
import unittest
from src.orders import place

class OrdersTest(unittest.TestCase):
    def test_place(self):
        self.assertEqual(place(1, 3), 300)
EOF
git add -A; c "feat: orders, billing, report"
git commit -q --allow-empty -m "fix: review finding on PR #12 - print() in src/orders.py broke the no-print rule (removed one call)"
git commit -q --allow-empty -m "fix: review finding on PR #19 - print() in src/billing.py again (no-print rule)"
