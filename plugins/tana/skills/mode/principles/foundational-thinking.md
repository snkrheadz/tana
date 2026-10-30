# Foundational thinking
Open when: choosing core types or data structures, ordering scaffold against feature work, or letting concurrent actors share something.

Settle the shape of the data before the logic; the code that follows gets obvious. Name the core types, list how they are accessed, and pick structures that fit the common paths.

- Deduplicate structure, not every line. Three similar statements beat a premature abstraction.
- Do first whatever helps every later step: CI, lint, test setup, shared types. Tests before fixes, setup before features. Keep commits small and single-purpose.
- Each step should land or deepen one abstraction, not smear a new capability across callers as special cases.
- Before sharing state, ask what happens if another actor changes it mid-use; see `separate-before-serializing-shared-state.md`.
- Subtract first, then lay foundations (`../pillars/light-tackle.md`).
