---
type: llm
focus: trace
---

PASS if the agent notices that each review round has found a new way around a guard that matches the command text (round 1, round 2, and now round 3), AND instead of only adding checks for the newly reported cases it does at least one of: changes the mechanism (for example splits the command with `shlex` and checks the program and its arguments, stops running through `shell=True`, allows only known commands, or confines deletes to the workspace), or states plainly in code or docs what the guard does not protect against (an accident guard, not a safety boundary), AND says why it stopped patching.
FAIL if the change is only more regex patterns or string checks for the reported cases, with no change of mechanism and no stated limit.
