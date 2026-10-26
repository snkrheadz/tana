# Decisions

Each entry records a change that was measured with `claude plugin eval`, the result,
and what was kept. Runs are per arm (with tana / without tana). Model: Opus 5.5.

## 2026-10-26: pillar 1 and the closing rules

| Case | Check | with | without |
| :- | :- | :- | :- |
| reproduce-before-edit | ran the code before the first edit | 7/7 (+1 run whose trace was lost) | 8/8 |
| reproduce-before-edit | reply shows the fixed output | 8/8 | 4/8 |
| refactor-keeps-output | ran `report.py` before the first edit | 3/3 | 3/3 |
| refactor-keeps-output | reply shows a before/after comparison | 2/3 | 0/3 |

The model already takes a before reading on its own. What tana adds is that the
observation reaches the reply as evidence. Kept. tana runs take about twice the turns
(7 to 12 against 4 to 8), the cost of reading the mode and pillar files.

## 2026-10-26: `ripple` (blast radius) skill. Not shipped

| Case | with | without |
| :- | :- | :- |
| ripple-persisted-data (old key in a data file inside the repo) | 3/3 | 3/3 |
| ripple-data-outside-repo (old key in `~/.scoreboard/records.json`) | 3/3 | 3/3 |

Without the skill the model still checked the stored data, ran the app, and reported
the KeyError in every run. The skill added two to three turns and no correct answers.
Removed. Revisit with a harder case or a weaker model.
