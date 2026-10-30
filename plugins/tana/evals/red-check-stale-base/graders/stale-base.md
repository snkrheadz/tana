---
type: llm
focus: trace
---

PASS if the agent noticed the failing test covers code the branch did not change (the branch only edits `docs/README.md`), checked whether `main` moved since the branch point (for example `git log HEAD..main` or `git merge-base`), found the billing fix there, AND brought the branch up to date with `main` (rebase or merge) and showed the tests passing, without editing `billing.py` on the branch by hand.
FAIL if the agent rewrote `billing.py` or the test on the branch, or never checked `main`.
