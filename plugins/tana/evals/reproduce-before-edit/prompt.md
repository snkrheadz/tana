---
description: Pillar 1. The agent should observe the failure before editing and observe the fix after.
max_turns: 25
runs: 2
allowed_tools: [Read, Glob, Grep, Skill, Edit, Bash]
---

Work the tana way. In this directory, `slugify("Hello  World")` in `slug.py` returns `hello--world`. It should return `hello-world`. Please fix it.
