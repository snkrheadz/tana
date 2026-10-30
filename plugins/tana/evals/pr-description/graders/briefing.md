---
type: llm
focus: { source: file, path: PR.md }
---

PASS if `PR.md` reads as a short briefing for a reviewer who has the diff: under about 40 lines, says why the change exists, what it covers and what it leaves out, what it could break, and how it was verified by naming a command and its result. No file-by-file walkthrough and no restating of the diff.
FAIL if it is longer than about 40 lines, walks through files one by one, or has no verification with a concrete command and result.
