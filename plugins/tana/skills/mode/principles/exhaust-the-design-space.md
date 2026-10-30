# Exhaust the design space
Open when: a UI interaction or architecture choice has no precedent in the codebase and the right answer depends on feel.

Do not pick the first idea. Build two or three rough, throwaway versions and compare them side by side. Reading a description of a design rarely shows what using it is like, and a sketch costs far less than rewriting shipped code.

1. Name what differs between the options and what you will judge on.
2. Make each version just real enough to try (a static page, a stub, a spike branch). Parallel sketches can each get a worktree.
3. Look at them together, pick one, and say why. Delete the others.

Under `../pillars/keep-moving.md` this is the cheap way to settle a "which looks better" question without asking the user.
