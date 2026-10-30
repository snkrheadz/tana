---
type: llm
focus: trace
---

PASS if the agent moved or copied the R-7 rule (user-facing strings go through `t()`) out of REVIEW.md into a CLAUDE.md file (repo root `CLAUDE.md` or `.claude/CLAUDE.md`) or into a `.claude/rules/*.md` file, AND its reply says why: `/code-review` is told to check conventions from CLAUDE.md files, and a rule that lives only in REVIEW.md is not reliably applied.
FAIL if R-7 stays only in REVIEW.md, or the agent assumes `/code-review` reads REVIEW.md as its instructions.
