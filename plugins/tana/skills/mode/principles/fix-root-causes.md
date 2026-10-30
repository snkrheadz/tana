# Fix root causes
Open when: debugging, and the obvious change would be a guard, retry, or catch near where it blew up.

The crash site is where bad state became visible, not where it began. Fix the first wrong decision, or the first state the code failed to handle.

1. Reproduce it. See `../playbooks/bug-fix.md`.
2. Ask why repeatedly until the answer is a decision in code, not a result of an earlier one. Stuck: add instrumentation and read real values.
3. Decide if the triggering state is legitimate. If the system may be in it, handling it there is the fix. If it should never exist, a check at the crash site buries the bug, so find what produced it.
4. Failing only after a restart points at persisted state: caches, lock files, configs.
5. Search for the same fault elsewhere and fix every copy.

If the workaround needs a long comment to defend it, the code is wrong. If the cause was hard to find, propose a cheap permanent signal that would reveal it next time.
