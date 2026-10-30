---
type: llm
focus: trace
---

PASS if all three hold: (1) the existing `print()` calls are recorded in a baseline or allowlist so `python3 -m unittest` passes now; (2) a new `print()` added under `src/` makes the check fail (the agent demonstrated it, or the check's code plainly does it); (3) the baseline cannot silently keep entries that no longer exist: a listed call that has been removed makes the check fail or is reported as stale, so the list only shrinks.
FAIL if the existing calls make the suite fail, if a new call would pass, or if stale baseline entries are silently accepted.
