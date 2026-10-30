# Lessons

Corrections from the user, with the pattern and the reason. Newest first.

## 2026-10-30: never name or credit outside reference material

- **Pattern:** when ideas from another project's skills or docs are used, tana's files,
  commit messages, PR titles, and PR bodies must not name that project or link to it.
- **Why:** the user does not want tana to point at other projects. Naming one in a
  README section and in commit messages had to be removed from public history with a
  force push, which cannot be undone and still leaves the old commits on the PR pages.
- **How to apply:** write every borrowed idea in tana's own words (no copied sentences;
  keep 8-word overlap with the source under 5%), and say nothing about the source.
  `scripts/check-terms.py` fails CI on the banned names, so add a hash there when a new
  name must stay out.
