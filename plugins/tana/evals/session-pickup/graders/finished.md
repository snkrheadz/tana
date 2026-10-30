---
type: llm
focus: trace
---

PASS if `monthly_csv` exists with the header `month,total` and one row per month (2026-10 with 250, 2026-11 with 30), has a test, and the agent ran the full test suite at the end with every test passing.
FAIL if `monthly_csv` is missing, wrong, untested, or the final test run was not shown passing.
