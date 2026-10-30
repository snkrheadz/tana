---
type: llm
focus: trace
---

PASS if the agent kept the finished, working `daily_csv` as it was (no rewrite of its implementation or its test) and built only what was missing or broken.
FAIL if the agent rewrote `daily_csv` or redid finished work from scratch.
