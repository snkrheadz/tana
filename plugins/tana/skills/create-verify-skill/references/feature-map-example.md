# Feature map example

A tiny notes app. Two files live under `features/`.

## features/README.md

    # Notes feature map
    Setup once: start with `NOTES_DATA_DIR=$(mktemp -d)`, seed two notes, run
    `verify-notes doctor` and read the URL and build id before any drive.
    Conventions: use roles and labels, not CSS. Reset data after changes.
    - [Search notes](./search.md)
    - [Create a note](./create-note.md)

## features/search.md

    # Search notes
    Typing in the search box narrows the list to matching titles.

    ## Sub-features
    - S1 match: matching titles stay. S2 empty: "No results" shows. S3 clear: full list returns.

    ## How to get to it (user POV)
    - Click the search box in the toolbar. Press `/`. Run `notes find <text>`.

    ## Driving it with the browser
    Preconditions: two seeded notes.
    - S1: fill the box with "plan"; expect one row, "Quarterly plan"; save a screenshot.
    - S2: fill "zzz"; expect the text "No results".
    - S3: clear the box; expect two rows.

    ## Gotchas
    - Results are debounced; wait for the row count, not a fixed delay.
