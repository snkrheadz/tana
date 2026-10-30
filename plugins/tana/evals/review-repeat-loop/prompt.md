---
description: review-fit. Findings come back across PRs and nobody notices. The agent should design a record that outlives the PR, a repeat signal where the next agent session will see it, and a number that shows whether the loop improves.
max_turns: 40
timeout_seconds: 900
runs: 3
allowed_tools: [Read, Glob, Grep, Skill, Edit, Write, Bash]
---

The same review findings keep coming back on new PRs, and nobody notices until the reviewer says it again (see NOTES.md). Propose how to set this repo up so that a repeated finding gets noticed and turned into a fix that sticks, and how we would know it is working. Keep it to the design and the files you would change; you do not need to implement it.
