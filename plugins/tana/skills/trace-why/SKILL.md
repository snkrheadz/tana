---
name: trace-why
description: Find out why code, a design, or a number ended up the way it is, using every evidence source that is connected, and report how sure each claim is. Use for /tana:trace-why or "why do we do it this way", "why did we pick X", "where did this threshold come from".
disable-model-invocation: true
---

# Trace why

An investigation (`../mode/playbooks/investigation.md`) into intent. Code shows what it
does; the reason lives in history that is partial and sometimes wrong. Report what the
record says and how strong it is. For runtime behavior use `/tana:explain-code`.

1. **Pin the target and the question.** A file and line range, a symbol, a flag, or a
   number. If the referent is vague, take it from open files and recent talk, say your
   reading in one line, and go on. Treat any guess in the question ("I assume it is for
   speed") as one candidate, not a conclusion.
2. **Build the anchor yourself, inline.** Run `git blame -L`, `git log --follow -p -- <file>`,
   and `git log -1 --format=%B <sha>`. Collect the commits, PR numbers (`(#123)` in subjects),
   and ticket IDs. Read the PR bodies and review threads with `gh pr view` and
   `gh api`. Do this before any fan-out. Often it answers the question.
3. **Find what else is connected.** List the MCP servers and CLIs this session has. Sort
   each into a source kind: issue tracker, long-form docs, team chat, incident notes,
   observability, error tracker, data warehouse. Read `references/sources.md` for what each
   kind is good at and how to search it.
4. **Search each connected kind, one `general-purpose` subagent per kind** when more than
   two are in play (`model: "sonnet"`, they are mechanical). Give each the anchor, the
   question, and the matching section of `references/sources.md`. They must not write
   anything. Search one kind at a time per host to avoid rate limits. With one or two
   sources, search them yourself.
5. **Record empty results.** A null is a finding. Note what was searched and with which
   keywords. Note any kind you skipped and why (not connected, or clearly irrelevant).
6. **Write the answer** with the tiers and phrasing in `references/confidence.md`.

## Output

1. The answer in one or two sentences, with its tier.
2. **Found:** direct and supported claims, each with a link or `path:line`.
3. **Inferred:** your reading, with the chain shown.
4. **Competing readings and conflicts:** both sources side by side, not a tidied story.
5. **Not known:** what you searched and found nothing for. Name who could answer.
6. **Sources:** one line per source kind, including empty and skipped ones.

If the user is about to change this code, end with Keep / Change / Avoid / Risk lines.

Traps: trusting the latest commit (the shape is many decisions stacked); reading the code
as proof of its own intent; calling "nobody mentioned it" proof of "it did not matter".
