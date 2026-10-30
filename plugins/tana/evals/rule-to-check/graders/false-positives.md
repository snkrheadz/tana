---
type: llm
focus: trace
---

PASS if the agent looked at what the detection matches across all of `src/` before settling the check, AND handled both look-alikes: the intentional output in `src/cli.py` (its docstring says it prints for shell pipes) is treated as a permanent, stated exception rather than as debt in the baseline, AND the help text in `src/report.py` that merely mentions `print()` inside a string is not counted (for example by parsing calls with `ast` instead of matching text).
FAIL if `src/cli.py` is listed as ordinary debt without a note, or if the string in `src/report.py` is counted as a violation.
