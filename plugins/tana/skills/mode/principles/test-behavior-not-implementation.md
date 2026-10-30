# Test behavior, not implementation
Open when: writing or reviewing a test, or a refactor broke tests that should not have broken.

A test is a claim about what users of the code can observe: return values, errors, readable state, effects on outside systems (a request sent, a row written). Private helpers and call order are not observable.

Judge each test with two imagined edits:
- Break the behavior (wrong value, skipped effect, effect twice). If it still passes, it proves nothing. Usual causes: loose assertion, expected value computed by the code under test, a copied constant, data the test built itself.
- Change the internals, keeping results the same. If it fails, it is pinned to implementation.

Keep tests that fail on the first edit and survive the second; rewrite or delete the rest. Drive code through its public interface with a concrete input, and derive the expected value from the requirement. A "nothing happens" test needs a twin where it does happen, so it shows it can see the call. An invariant (a key present in two tables) can be the behavior. Reading before change: `../pillars/sounding.md`.
