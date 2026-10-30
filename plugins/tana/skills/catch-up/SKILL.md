---
name: catch-up
description: Summarize what happened in this session after the user's last message, then list each decision that is theirs, with enough detail to make it from the reply alone. Use for /tana:catch-up or "what did I miss", "where are we".
disable-model-invocation: true
---

# Catch up

Treat the user's last message as the cutoff: they know it and nothing later. Task
notifications and subagent reports do not count as their messages. Keep this turn read-only: change no code, start
no job, post nothing.

Voice: follow `../plain-words/SKILL.md`. Report outcomes, not process.
Write "the tests pass" rather than naming the CI system. Drop hashes, paths, commands, and
counts unless the reader must act on them. Refer to a PR, branch, or agent by the name
the user would use.

1. **Collect.** Gather what you did since that message, subagent reports, and anything
   others posted. Check live state of each PR, check run, and background task this chat
   touched (`gh pr view`, `gh pr checks`, task output). Re-verify any number you will show.
2. **Find the calls that wait on them.** A call is something only the user can do: a
   product choice, an approval, an irreversible step, access you lack. Include old ones
   still open. Work you can do yourself is not a call. Do not invent a call to fill space;
   `../mode/pillars/keep-moving.md` says what counts.
3. **Write the reply.**
   - One opening sentence: what waits on them, or that nothing does.
   - What happened, under 100 words, one line per thing they asked for, each saying
     done, running, failed, or not checked. Each line must stand alone. Name any bug
     found and fixed on the way. Never mark done what still needs them.
   - Then the calls. For each: the decision, your pick, the user-visible effect, the
     evidence behind your pick, and the risk (say "low" when it is). When several items
     share one call, state it once and give each item a bullet, riskiest first, with its
     link. For a choice between options, give each option's gain and cost. The reply must
     be enough to decide; a link only adds depth. Never trim items to hit a word count.
4. **Pictures only when they help.** Embed a screenshot if the change is visible. Use a
   Mermaid diagram for a PR stack or a flow, at most six boxes. No diagram of a status
   list. Do not mock up a screen you never captured. For a visible change with no capture,
   describe it in words and say that no screenshot exists.

## Optional: video

Only if the environment already has the tools (for example `ffmpeg` and a way to render
slides, checked with `command -v`), offer a short subtitled slide video in place of the
pictures. Keep it to 10 slides or fewer, one point each, one short subtitle per slide, held
long enough to read. Render to a temp folder outside the repo, then extract a frame per
slide and look at it. If any tool is missing or the render fails, skip it and say so in one
line. The calls stay as text either way.
