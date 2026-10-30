# Laziness protocol
Open when: sizing a diff, or tempted to add an abstraction, layer, or extra parameter threading.

Mostly covered by `../pillars/light-tackle.md`: delete first, smallest change, no one-caller helpers. Added nuance:

- Make each decision in one place. If the same choice is encoded in several files, move it behind a single source and pass the outcome as a plain value.
- Fewer lines beat elegant scaffolding, even when the scaffolding looks tidy.
- When a problem keeps recurring, remove what creates the condition instead of building something that cleans up after it.
