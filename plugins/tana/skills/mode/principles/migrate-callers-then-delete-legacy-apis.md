# Migrate callers, then delete the old API
Open when: you introduce a new internal API while the old one still has callers.

Move every caller to the new API and remove the old one in the same change. A compatibility layer left behind means two ways to do one thing, and it rarely gets removed.

- Applies when nobody outside the repo depends on the old shape and the team can take a coordinated breaking change.
- Rewrite tests to assert the new contract. Delete tests that only guarded old internals.
- Search for all references (code, docs, examples) so nothing points at the removed API.
- If outside users exist, this does not apply; deprecate with a date instead.

See the "keeping the old API" row in `../pillars/light-tackle.md`.
