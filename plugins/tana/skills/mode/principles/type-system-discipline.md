# Type system discipline
Open when: defining types, handling outside data, or seeing impossible states and mixed-up primitives.

Make the compiler refuse what should never happen. Design errors and special cases out of existence before adding handlers.

- Give same-shaped but different-meaning primitives distinct types (a user id is not an order id): brand or newtype them, validate once on creation, trust after.
- Outside data (JSON, RPC, CLI args, env vars, config, DB rows) is untyped until a parse function at the edge produces the typed model; see `boundary-discipline.md`.
- Derive types from the file that owns a shape (protobuf, OpenAPI, GraphQL, migrations, token files) instead of hand-writing a parallel copy that can drift.
- Unhandled variants should be compile errors via exhaustive matching.
