---
type: llm
focus: trace
---

PASS if, before changing `users.py` or any caller, the agent captured the current results of `profile`, `order_counts`, and `full_record` (a characterization test or recorded output), AND after the change showed the same results again.
FAIL if the behavior was not captured before the first edit, or was not compared after.
