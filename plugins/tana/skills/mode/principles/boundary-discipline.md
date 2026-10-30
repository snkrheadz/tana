# Boundary discipline
Open when: adding validation, error handling, or glue between your logic and a framework or outside system.

Guard the edges and trust the inside. Check input once where it enters (arguments, files, network, other services), turn it into your own types there, and let the core code assume those types hold.

- Scattered re-checks add noise and a false sense of safety, and they hide real bugs.
- Keep decisions in plain functions that take data and return data. The framework layer stays thin and only calls them, so tests do not need the framework.
- Do not leak transport, storage, or wire types past the edge. Expose domain terms.

Ask of any check: is data crossing a boundary right now? If not, delete it. Short form in `../pillars/light-tackle.md` (shape the data, validate at the edge). Typing details are in `type-system-discipline.md`.
