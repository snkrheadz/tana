# Attack the premise
Open when: two or more fixes built on the same belief have failed the same check.

Stop fixing and question the belief. Every failed fix is a vote against what it assumed, so a third attempt on that assumption digs where the evidence already says nothing is buried.

1. Write the shared assumption as one sentence.
2. Find an observation that would look different if it were false, and take it before touching code. Look at where the failures cluster, not only how big they are.
3. If the assumption is false, hunt for what the failures share. If it holds, ask why once more: the earlier fixes may have patched a consequence.
4. Prefer removing the condition that causes the loss over adding cleanup that compensates for it.

This is not a redesign (see `redesign-from-first-principles.md`). It tests a fact, it does not change a requirement. Pair with `../pillars/sounding.md` for the observation.
