# Review loop

A recall-first reviewer such as `/code-review high` returns findings on any real diff, so
zero findings is not the finish line. Done is: the confirmed defects are fixed, and your
fix has been reviewed like any other new code.

1. **Sort the findings.** Fix the confirmed defects. A plausible finding with no failure
   you can name, or a cost claim with no numbers, gets a written reason instead of a code
   change.
2. **Check for a repeat.** If the reviewer said the same thing before (search `git log`
   and past review notes), handle it with `pillars/log-the-catch.md`.
3. **Review your fix before you call it ready.** The fix is new code nobody has reviewed.
   Run `git diff` over everything since the reviewed commit and read it as the reviewer
   would: new branches, new guards and how they can be passed around, the callers of what
   you changed. Then run the tests. In one repository, every major finding across six
   review rounds of one PR landed on code that the previous round's fix had added.
4. **Call it.** Ready or not, with every finding you did not act on and why.
