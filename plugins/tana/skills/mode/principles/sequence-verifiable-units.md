# Sequence verifiable units
Open when: doing a sweep, migration, or any run of similar edits, or deciding how to order commits.

Work in small steps that each end in a checkable state, and do not start the next until the current check is green. A break found at the step that caused it is cheap to locate; found after a batch, it is buried under later work.

- Per step: known-good state, one change, run the check, move on. Start from a clean trunk so checks measure the true baseline. Cheap checks from a script (`build-the-lever.md`) still get run.
- Per delivery: order commits so they argue the case. Failing test, then the fix. Removal, then reshape. Baseline capture, then the change. Scaffold, then feature.

Baseline thinking is in `../pillars/sounding.md`; the failing-test-then-fix order is in `../playbooks/bug-fix.md`.
