# One rod

You fish best with one rod you are watching. Every handoff to another agent loses
detail: the subagent sees only its brief, and you see only its summary. Keep the work
in this conversation unless one of the three reasons below holds.

## The three reasons to spawn

1. **Context flood.** The step produces output you will not read again: a sweep
   over many files, a long log, a web crawl. The subagent reads it and returns a
   short result.
2. **Parallel pieces.** Several pieces of work are independent, each returns a
   compact result, and none writes what another reads.
3. **Fresh eyes.** The check needs a reader that did not write the code, such as a
   review of the diff against the request.

Name the reason in the spawn prompt. If you cannot, do the work yourself.

Do not delegate a handful of tool calls, a lookup whose answer you already know where
to find, or a chain of small edits that depend on each other. The handoff costs more
than the work.

## Split by context, not by role

Give each subagent work that needs little from the rest of the conversation and
returns something small. Independent research paths, separate modules with clear
interfaces, and black-box verification split well. "Planner", "implementer", and
"tester" that all need the same facts do not. They become a game of telephone.

## Write the brief like a handoff to a colleague

The brief is all the subagent knows. Include:

- the goal and why it matters;
- the paths and facts it needs, and what you already ruled out;
- the scope, including what not to touch;
- the shape of the result: paths changed, a short summary, and the check it ran
  with its output. Not file dumps.

You own the result. Read the diff yourself before you report it. A subagent saying
"done" is a claim, not evidence.

## Pick the model for the job

Set `model` on every spawn unless the agent definition already sets one.

| Work | Model |
| :- | :- |
| Search, listing, collecting logs | `haiku` |
| Summarizing, cross-checking, mechanical edits, implementation from a complete spec | `sonnet` |
| Design judgment, review, anything ambiguous | `opus` |

## Parallel work that writes

Separate before you parallelize. Two agents that write the same file or branch will
collide. Give each its own worktree (`isolation: "worktree"`) or its own files. If
the pieces cannot be separated, run them one after another.

For many similar pieces (a migration across dozens of call sites, an audit of every
module), use a Workflow with a verify step per piece instead of spawning agents by
hand each turn.

Requests to the same web host go one at a time. Parallel fetches trip rate limits and
bot detection, and the job ends up slower.

## Continue or start fresh

Start a fresh subagent for new work, with a brief that carries everything decided so
far. Continue an existing one with `SendMessage` only when the work depends on
something that agent holds and you cannot cheaply recreate, such as a running dev
server or edits it has not committed yet.
