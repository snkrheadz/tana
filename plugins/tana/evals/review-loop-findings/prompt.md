---
description: review-loop. Two confirmed findings (one repeats a rule already broken and fixed in PR 41) and two plausible ones. The agent should fix the confirmed ones, triage the rest, turn the repeat into a check, and review its own fix before calling the branch ready.
max_turns: 40
timeout_seconds: 900
runs: 3
allowed_tools: [Read, Glob, Grep, Skill, Edit, Write, Bash]
---

Work the tana way. The reviewer left findings on my branch in `review-findings.md`. Address them and tell me whether the branch is ready to push.
