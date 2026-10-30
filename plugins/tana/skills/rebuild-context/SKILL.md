---
name: rebuild-context
description: Rebuild your recent working context from past Claude Code sessions, git and GitHub state, and the shared record, and hand back a short brief of where things stand. Use for /tana:rebuild-context or "where did I leave off", "what was I working on", "catch me up on X".
disable-model-invocation: true
---

# Rebuild context

An investigation (`../mode/playbooks/investigation.md`) into your own recent work. Read
only what the in-scope threads need, then stop.

Two records matter. Past sessions hold what was done and decided. The shared record holds
what happened around the same code under other names: user reports, fixes that shipped
and were reverted, errors still firing. Use both.

1. **Route.** One named prior session to continue is a plain resume, not this. If the user
   gave a full state note (branch, paths, change), use it and skip the digging.
2. **Lock the scope.** Window (default last 7 days), topic if named, project (default the
   current one; never read another project's sessions unasked). Say the scope back.
3. **Read past sessions.** They are JSONL files in `~/.claude/projects/<project>/`, where
   `<project>` is the working directory path with `/` turned into `-`. Order by modified
   time (`ls -t`), not by name. Run `grep -l` on the topic first, then read only the
   matching sessions and only the relevant lines (`jq` helps). Skip this session and
   obvious noise such as subagent runs. For many sessions, launch `Explore` subagents on
   `model: "haiku"`, each with a slice, so raw transcripts stay out of this context. Ask
   each for: topic, goal, decisions, open threads, corrections, and artifacts (PR numbers,
   branches), with the session file name.
4. **Sweep the shared record** when the topic names a feature, file, or bug. Follow
   `/tana:trace-why`, but ask "what is the state now, what was tried and did not hold, what
   are users still reporting". Skip for pure activity recall.
5. **Check live state.** Verify every PR, branch, and ticket you found with `git` and `gh`.
   If the answer depends on what a session actually did, read the raw lines, not a summary.
6. **Write the brief.** Cite sessions by file name and the shared record by PR, ticket, or
   link. Strip private detail before anything public. Filter the prose through
   `../cut-ai-tells/SKILL.md`.

## Brief

- **Capsule:** at most 5 bullets: what the work is and where it stands.
- **Threads:** one line each, starting with one tag: `[merged #N]`, `[open PR #N]`,
  `[in flight <branch>]`, `[verified, uncommitted]`, `[reverted #N]`, `[planned]`.
  An untagged thread is unfinished, so tag it.
- **Problems:** at most 5 recurring ones, including fixes that were reverted.
- **Next move:** one concrete action.

Leave out adjacent work unless it blocks this. If it runs long, cut detail before threads.
