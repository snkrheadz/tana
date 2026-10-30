---
description: review-loop. Round 3 of review finds two more ways around a guard that matches command text; rounds 1 and 2 each patched one. The agent should see the loop is not converging and change the mechanism or narrow the claim, not add a third patch.
max_turns: 40
timeout_seconds: 900
runs: 3
allowed_tools: [Read, Glob, Grep, Skill, Edit, Write, Bash]
---

Work the tana way. Round 3 of review on my branch found more ways around the delete guard (`review-findings.md`). Address the findings and tell me whether the branch is ready.
