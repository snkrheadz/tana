# Lessons

Corrections from the user, with the pattern and the reason. Newest first.

## 2026-11-16: a parser in a skill script needs probes of real shapes, not only my own fixture

- **Pattern:** `system_map.py` shipped with 17 passing tests and still misread common
  Terraform: a local written as a multi-line map, keys inside a `jsonencode` call, a
  trailing comment that shifted later offsets, an escaped interpolation, a list over
  several lines, a number with a leading zero (a crash), and `*.tfvars` files that
  Terraform never loads. A review found them by running small probe folders.
- **Why:** the fixture held only the shapes I had in mind while writing the parser, and it
  read lines with regexes and kept a name stack on the side. Each miss gave a false tie
  or dropped a real one, which is the one thing the `draw` check exists to prevent.
- **How to apply:** for a script that reads a nested format, walk the brackets and keep
  real offsets. Do not match line by line. Before shipping, write one probe per shape the
  format allows (nested map, call argument, comment at line end, escape, multi-line
  value, odd literal), as `EdgeCaseTest` in `tests/system_map_test.py` now does, and
  compare the reading of a real repo before and after each parser change.

## 2026-11-16: after changing a command in a skill, reread the lines that describe its output

- **Pattern:** adding `-continue` to the TLC command in `statechart` left "TLC prints the
  shortest trace to the first broken rule" in the next section. With the flag, TLC prints
  one trace for each state that breaks a rule.
- **Why:** I checked the flag against the claim it fixed and did not rerun the other
  claims in the file that depend on the same command.
- **How to apply:** when a command in a skill changes, search the skill for every
  sentence about that command's output and run a case that exercises each one.

## 2026-11-02: README.md is English only

- **Pattern:** write README.md entirely in English, with no Japanese, even when the
  conversation is in Japanese.
- **Why:** the user asked for the README in English after an update kept its Japanese text.
- **How to apply:** when editing README.md, write new text in English and translate any
  Japanese you touch; check with `grep -P '[\p{Hiragana}\p{Katakana}\p{Han}]' README.md`.

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
