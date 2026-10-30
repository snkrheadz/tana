# Design red flags

Check every candidate sketch against these. A hit means revise or reject.

- **Shallow module.** Callers must call several methods in order to finish one job, or options expose internal stages. A good module hides a lot behind a small surface. A long call chain is not depth; it only spreads understanding over layers.
- **Leaked decision.** One internal choice (a format, a policy, a protocol detail) shows up in more than one module. Do not re-export wire or storage types. Parse them into domain types at the edge.
- **Split by time.** Modules named load, validate, transform, save that each repeat the same representation. Group by the knowledge a module owns instead.
- **Pass-through.** A method that hands its arguments on unchanged. Remove it, unless the layer adds policy or adapts a type.
- **Two writers.** Two modules change the same state or keep their own copy. Give each piece of state one owner; others read or ask.
- **Two ways in.** The design allows two routes to one task. Contributors copy whichever they see first, so both grow. Keep one, move callers, delete the other in the same change.
- **Reachable internals.** Anything outside the module can import its guts. Make that a build failure.
- **Hand-kept list.** The same items are listed in two places by hand. Derive one from the other, or fail the build when they differ.
