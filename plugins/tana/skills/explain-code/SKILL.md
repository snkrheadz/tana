---
name: explain-code
description: Explain how a piece of code works, where things live, and which layer owns what. Use for /tana:explain-code or "how does X work", "walk me through this", "where should this live".
disable-model-invocation: true
---

# Explain code

The deliverable is an explanation a new teammate could build on. It follows
`../mode/playbooks/investigation.md`: answer first, evidence with `path:line`, no code change.
For the reason a thing is shaped this way, use `/tana:trace-why` instead.

1. **Size the question.** If the scope is vague, state your reading in one line and go on.
   - Narrow (one module, one function): read it yourself and write the answer. No subagents.
   - Broad (a subsystem, a flow across services): go to step 2.
2. **Split a broad question into 2 to 4 slices.** One slice is one part of the flow, for
   example "request entry and auth" or "how results are stored". Launch one `Explore`
   subagent per slice in a single message, `model: "haiku"`. Hand each the brief in
   `references/slice-brief.md`. Follow `../mode/pillars/one-rod.md` before you fan out.
3. **Reconcile.** Merge the slices. Where two reports disagree, open the code and settle it
   yourself. Do not pass a contradiction on to the reader.
4. **Write the explanation** with the layout in `references/layout.md`. Drop sections that
   do not apply.
5. **Check the claims you are least sure of.** Re-open the file for any function name or
   call order you took from a subagent. Mark what you read, what you inferred, and what
   you could not trace.

For a placement question ("which package owns this?"), name the owner you would pick, the
two facts that point there, and the nearest alternative with the reason you passed on it.
