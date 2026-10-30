# Red check

A red check on a PR is a reading to classify before it is a thing to fix.

1. **Read the failure, not the badge.** Open the log and find the step or test that
   failed and the line it failed on.
2. **Classify it before you run it again.**
   - Infrastructure or a flaky test: one fresh run, never more. The same failure twice
     is not flaky. Read it as a real failure.
   - A failure in code the branch did not change: suspect a stale base. Check whether
     the target branch moved (`git log HEAD..origin/main`, `git merge-base`). If the fix
     or the cause is there, bring the branch up to date instead of patching that code
     here.
   - A failure in the branch's own code: fix it with a failing-then-passing reading
     (`playbooks/bug-fix.md`).
3. **Batch the fixes.** Push every fix for one round in one push, so the next run, and
   the next paid review, sees them together.
4. **Stop at the owner's line.** Green checks are not permission to merge. Merges,
   deploys, and force pushes to shared branches stay with the person who owns them
   (`pillars/keep-moving.md`).
