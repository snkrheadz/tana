---
type: llm
focus: trace
---

Judge the final state of `discount.py` and `checkout.py` as the agent left them.
PASS if a checkout without a coupon no longer raises (handled either in `checkout_total` or in `apply_discount`; both are fine), AND `apply_discount` returns an `int` number of cents computed without letting a float through (integer arithmetic, or explicit rounding to int, such that 1000 with 7 percent off gives 930 and 1000 with 10 percent off gives 900).
FAIL if a checkout without a coupon still raises, if `apply_discount` can return a float for an integer percentage, or if it truncates so that 1000 with 7 percent off gives 929.
