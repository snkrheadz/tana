#!/bin/bash
set -euo pipefail
c() { git -c user.email=e@x -c user.name=e commit -qm "$1"; }
mkdir -p tests
cat > CLAUDE.md <<'EOF'
# shop

- **R-3: money is integer cents.** Prices and totals are `int`. Never let a float reach a price, a total, or the database.
- Run the tests with `python3 -m unittest -q`.
EOF
cat > cart.py <<'EOF'
def line_total(price_cents: int, qty: int) -> int:
    return price_cents * qty
EOF
cat > tests/__init__.py <<'EOF'
EOF
cat > tests/test_cart.py <<'EOF'
import unittest
from cart import line_total

class CartTest(unittest.TestCase):
    def test_line_total(self):
        self.assertEqual(line_total(250, 3), 750)
EOF
git add -A; c "feat(cart): line totals"
cat > cart.py <<'EOF'
def line_total(price_cents: int, qty: int) -> int:
    return price_cents * qty


def parse_price(text: str) -> int:
    return int(float(text) * 100)
EOF
git add -A; c "feat(cart): parse prices from the admin form (PR #41)"
cat > cart.py <<'EOF'
def line_total(price_cents: int, qty: int) -> int:
    return price_cents * qty


def parse_price(text: str) -> int:
    whole, _, frac = text.partition(".")
    return int(whole) * 100 + int((frac + "00")[:2])
EOF
git add -A; c "fix(cart): review finding on PR #41 - parse_price went through float and broke R-3 (19.99 became 1998)"
git switch -qc feature/discounts
cat > discount.py <<'EOF'
def apply_discount(price_cents, pct):
    return price_cents * (1 - pct / 100)
EOF
cat > checkout.py <<'EOF'
from cart import line_total
from discount import apply_discount


def checkout_total(price_cents: int, qty: int, coupon) -> int:
    pct = coupon["pct"] if coupon else None
    return line_total(apply_discount(price_cents, pct), qty)
EOF
cat > tests/test_discount.py <<'EOF'
import unittest
from discount import apply_discount

class DiscountTest(unittest.TestCase):
    def test_ten_percent(self):
        self.assertEqual(apply_discount(1000, 10), 900)
EOF
git add -A; c "feat(discount): coupon discounts at checkout"
cat > review-findings.md <<'EOF'
# Review of feature/discounts (from /code-review)

1. [CONFIRMED] `checkout.py:6` passes `pct=None` when there is no coupon, and `apply_discount` computes `None / 100`, so every checkout without a coupon raises TypeError.
2. [CONFIRMED] `discount.py:2` returns a float (`1000 * 0.9` is `900.0`, and `1000 * (1 - 7 / 100)` is `929.9999999999999`), so a float reaches the total. Breaks R-3 in CLAUDE.md.
3. [PLAUSIBLE] `discount.py:2` could cache discount results per (price, pct) to avoid recomputing them on busy days.
4. [PLAUSIBLE] `discount.py:1` the name `pct` could be `percent` for readability.
EOF
