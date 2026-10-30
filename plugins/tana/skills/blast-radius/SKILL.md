---
name: blast-radius
description: Find what a change could break outside its diff, and prove the one fact that makes it safe by running real code. Use for /tana:blast-radius or "what could this break", "blast radius of X", or a small diff you do not trust.
disable-model-invocation: true
---

# Blast radius

Find what a change breaks elsewhere, before it ships. A list of callers is easy and not the point. The point is breakage that search will not show.

A fluent writeup proves nothing. So do not hand one back. Find the one or two facts the change is safe because of, and run code to test them.

## How sure are you

For each safety fact, go as far down as is cheap and say where you stopped.

1. Asserted. Worth nothing alone.
2. Pointed at: a real `file:line`, or the library's source.
3. Walked: you traced the failure step by step and it does not arrive.
4. Ran it: a script or test calls the real code and fails loudly if you are wrong.
5. Seen live in the running app.

Level 4 is usually a short script that imports the library the app ships and calls the exact function in doubt (`../mode/pillars/sounding.md`).

## Steps

1. Read the change. Symbols added, changed, deleted, and behavior that differs without the diff showing it. `/tana:trace-why` helps pull the history.
2. Find the one fact. Most scary changes are safe for one reason, such as "this call only drops entries that are already dead." If that holds, many risks go away at once. Spend time here, not on a pile of maybes.
3. Look past where search stops: the library source and its pinned version, local patches, ordering of async work and teardown, data crossing a boundary (API JSON, a DB column, a wire format, another language reading the same bytes), feature flags, code three calls away.
4. Rate each risk with a real chance and a real cost. Cite `file:line`. An empty search is a valid answer. Never invent a caller or an API. Keep confirmed risks apart from those you checked and cleared.
5. Prove the fact. Write the script or test, run it, paste the output.
6. For a wide change, ask several independent subagents the same question with `/tana:compete` and merge. Name the reason when you spawn (`../mode/pillars/one-rod.md`).

## Hand back

- **What it does**, including the part the diff hides.
- **The safety fact**, the level you reached, and the proof. Write "unproven" if you could not.
- **Risks**: how each breaks, where, odds and cost, how to check, proof for those that matter.
- **Cleared**: what you checked and why it is fine.
- **Before merge**: the cheapest test that would catch the real bug, with your script.

Remove anything private before this goes into a public place.
