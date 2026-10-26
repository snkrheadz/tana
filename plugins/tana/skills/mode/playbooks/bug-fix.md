# Bug fix

Every line you ship traces to something you observed. A change that "might help" is a
hypothesis. It does not ship.

1. **Reproduce it yourself.** Use the surface the user saw the bug on. Read
   `pillars/sounding.md` and get a failing reading before any edit. Ask the user to
   reproduce only when you have driven every surface you can reach and can name what
   blocks you.
2. **Narrow the cause.** List the candidate causes. Pick the observation that rules out
   the most of them, take it, and repeat until one cause survives. When state is
   unclear, add logging and read it while the code runs. `git log -S` and `git blame`
   on the failing lines tell you whether this is a regression and what changed.
3. **Fix at the first wrong step.** Follow the bad value back to where the system first
   went wrong and fix it there, not where the symptom surfaced.
4. **Take the same reading again.** The reproduction from step 1 now passes. Run the
   nearest existing tests too, so the fix did not move the bug somewhere else.
5. **Keep the reproduction.** If the repository has tests of this kind, commit the
   failing test before the fix, so history shows the bug and its cure.

Reply with what was broken, the cause, the fix, and the failing-then-passing output
pasted as it was printed.
