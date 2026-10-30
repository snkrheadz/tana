# Outcome-oriented execution
Open when: carrying out a planned rewrite or migration with explicit phases.

Aim at the verified end state, not at keeping every midpoint working. Holding each step fully stable usually means temporary compatibility code that outlives the migration.

- Allow breakage in the middle only when it is planned, limited in scope, and reversible. Write down where it is allowed.
- Keep quick, sharp checks on the areas you are touching as you go.
- Require the full static and runtime verification when the plan ends, not before.

This does not license sloppiness in ordinary work. See `sequence-verifiable-units.md` for the per-step discipline when each step must stay green.
