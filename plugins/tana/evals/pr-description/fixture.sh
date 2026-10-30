#!/bin/bash
set -euo pipefail
c() { git -c user.email=e@x -c user.name=e commit -qm "$1"; }
git checkout -q -B main
mkdir -p tests
touch tests/__init__.py
cat > money.py <<'EOF'
def _fmt(cents: int) -> str:
    return f"${cents // 100}.{cents % 100:02d}"
EOF
for m in cart receipt refund statement; do
cat > $m.py <<EOF
from money import _fmt


def show_$m(cents: int) -> str:
    return "$m: " + _fmt(cents)
EOF
done
cat > invoices.py <<'EOF'
INVOICES = [{"id": 1, "cents": 1250}, {"id": 2, "cents": 399}]
EOF
cat > tests/test_money.py <<'EOF'
import unittest
from cart import show_cart

class MoneyTest(unittest.TestCase):
    def test_cart(self):
        self.assertEqual(show_cart(1250), "cart: $12.50")
EOF
git add -A; c "money formatting"
git checkout -q -b feat/invoice-csv
cat >> invoices.py <<'EOF'


def invoices_csv() -> str:
    rows = ["id,amount_cents"] + [f"{i['id']},{i['cents']}" for i in INVOICES]
    return "\n".join(rows) + "\n"
EOF
cat > tests/test_invoices.py <<'EOF'
import unittest
from invoices import invoices_csv

class InvoicesTest(unittest.TestCase):
    def test_csv(self):
        self.assertEqual(invoices_csv(), "id,amount_cents\n1,1250\n2,399\n")
EOF
git add -A; c "feat: export invoices as CSV for the finance team"
for f in money.py cart.py receipt.py refund.py statement.py; do sed -i.bak 's/_fmt/format_money/g' $f && rm $f.bak; done
git add -A; c "refactor: rename _fmt to format_money"
