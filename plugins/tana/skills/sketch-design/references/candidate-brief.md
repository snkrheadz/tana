# Candidate brief for design sketches

Give this to each candidate along with the task, the grounding notes, and the directory it may write to.

You are making one independent candidate design. Deliver types, signatures, a module map, and a rationale shaped by `rationale-template.md`.

Work in this order and these rules:

1. Write the caller's usage and a few call sites. Derive types from them.
2. Choose data structures first. Trace the main access paths. If the answer is "add an index later", the structure is wrong.
3. Prefer a small public surface over a thin implementation. Keep wire types off it.
4. If two actors may write the same state, give each its own copy and merge on read.
5. Make flow readable from signatures: `not implemented` bodies, pseudocode for tricky parts, comments that state intent and invariants.
6. Put invariants in types before runtime checks, and checks before comments.
7. Validate at the edges, trust types inside, keep logic pure and the outer shell thin.
8. One source of truth per fact. Derive, do not sync.
9. Ask what happens if an operation runs twice or dies halfway.
10. If tracing a flow takes more than three files, flatten.

Do not hedge toward what other candidates might do. The gaps between candidates are what the chooser uses.
