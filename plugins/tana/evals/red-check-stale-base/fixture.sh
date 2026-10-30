#!/bin/bash
set -euo pipefail
c() { git -c user.email=e@x -c user.name=e commit -qm "$1"; }
git checkout -q -B main
mkdir -p tests docs ci-logs
touch tests/__init__.py
cat > billing.py <<'EOF'
def round_cents(amount: float) -> int:
    return round(amount * 100)
EOF
cat > tests/test_billing.py <<'EOF'
import unittest
from billing import round_cents

class BillingTest(unittest.TestCase):
    def test_rounding_half_up(self):
        self.assertEqual(round_cents(0.125), 13)
EOF
echo "# Billing" > docs/README.md
git add -A; c "billing: round to cents"
git checkout -q -b docs/fix-typo
printf '# Billing\n\nAmounts are stored in integer cents.\n' > docs/README.md
git add -A; c "docs: explain cents"
git checkout -q main
cat > billing.py <<'EOF'
from decimal import ROUND_HALF_UP, Decimal


def round_cents(amount: float) -> int:
    return int((Decimal(str(amount)) * 100).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
EOF
git add -A; c "fix(billing): round half up (round() is banker's rounding)"
git checkout -q docs/fix-typo
for n in 1 2; do
cat > ci-logs/run-$n.txt <<'EOF'
$ python3 -m unittest -v
test_rounding_half_up (tests.test_billing.BillingTest.test_rounding_half_up) ... FAIL

======================================================================
FAIL: test_rounding_half_up (tests.test_billing.BillingTest.test_rounding_half_up)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "tests/test_billing.py", line 6, in test_rounding_half_up
    self.assertEqual(round_cents(0.125), 13)
AssertionError: 12 != 13

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
EOF
done
sed -i.bak '1i\
# CI run #2 (re-run of #1 on the same commit)
' ci-logs/run-2.txt && rm ci-logs/run-2.txt.bak
sed -i.bak '1i\
# CI run #1
' ci-logs/run-1.txt && rm ci-logs/run-1.txt.bak
