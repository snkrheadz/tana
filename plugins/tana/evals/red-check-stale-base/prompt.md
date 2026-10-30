---
description: PR loop. CI is red twice with the same failure, in code the branch never touched, and main already fixed it. The agent should call it not-flaky, find the stale base, and update from main instead of patching the code on the branch.
max_turns: 30
timeout_seconds: 600
runs: 3
allowed_tools: [Read, Glob, Grep, Skill, Edit, Write, Bash]
---

Work the tana way. CI is red on my branch (logs are in `ci-logs/`). I already re-ran it once. Get it green.
