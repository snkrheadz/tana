# Opening a PR

1. **One change per PR.** If the branch mixes unrelated changes (a feature and a rename,
   a fix and a cleanup), split them into separate PRs before you write anything.
2. **Run the check you will cite.** Run the tests or the reproduction on the branch now
   and keep the output.
3. **Write a briefing, not a log.** The reader has the diff. Title:
   `type(scope): imperative subject`. Body in short sections, dropping any that are
   empty:
   - Why: the problem and the approach, in one to three sentences.
   - Scope: what it covers and what it leaves out.
   - Risk: who or what it touches, and why that is safe.
   - Verification: the command you ran and what it printed.

   Keep it under about 40 lines. No file-by-file tour, and no restating the diff.
