# Slice brief

Paste this into each `Explore` subagent, with the question and the slice filled in.

Other agents are reading other slices of the same system. Stay on yours and go deep.

Question: {question}
Your slice: {slice}

Report back, short and concrete:

- **Parts:** the main types, modules, and functions in your slice, each with its path and
  one line on what it does.
- **Flow:** the order of calls, with the data passed at each step.
- **Edges:** where your slice talks to the rest of the system (inputs, outputs, config).
- **Surprises:** anything that works differently from what its name suggests.
- **Gaps:** what you could not trace. Say so plainly. Do not guess to fill them.
- **Files opened:** a list, so the writer can re-check.
