# Review loop

A recall-first reviewer such as `/code-review high` returns findings on any real diff, so
zero findings is not the finish line. Done is: the confirmed defects are fixed, and your
fix has been reviewed like any other new code.

1. **Sort the findings.** Fix the confirmed defects. A plausible finding with no failure
   you can name, or a cost claim with no numbers, gets a reply with the concrete reason
   instead of a code change. Never change code only to quiet the reviewer. Findings about
   security, auth, billing, user data, or migrations are fixed or taken to the owner,
   never waved through.
2. **Check for a repeat.** Search `git log` and past review notes. A real finding the
   reviewer made before goes to `pillars/log-the-catch.md`. A finding you declined before
   that came back goes into the project's shared triage list, a file the reviewer is
   given: when it may be skipped, when it must not be, an example, and where the decision
   came from. Mark it a candidate until it holds on more PRs, and keep security, auth,
   billing, data, and migration findings off the list. Make the list change its own
   change.
3. **Review your fix before you call it ready.** The fix is new code nobody has reviewed.
   Run `git diff` over everything since the reviewed commit and read it as the reviewer
   would: new branches, new guards and how they can be passed around, the callers of what
   you changed. Then run the tests. In one repository, every major finding across six
   review rounds of one PR landed on code that the previous round's fix had added.
4. **Call it.** Ready or not, with every finding you did not act on and why.
