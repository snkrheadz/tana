---
description: review-loop. Round 2 brings back a finding already declined twice (round 1 and PR 31), next to a real bug and a security-shaped finding. The agent should not churn code, should record the repeated dismissal where the reviewer will see it next time, and should not turn the security finding into a skip.
max_turns: 40
timeout_seconds: 900
runs: 3
allowed_tools: [Read, Glob, Grep, Skill, Edit, Write, Bash]
---

Work the tana way. Round 2 of review on my branch is in `review-findings.md`. Handle it and tell me whether the branch is ready.
