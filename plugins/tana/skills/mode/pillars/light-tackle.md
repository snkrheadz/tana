# Light tackle

Heavy tackle catches nothing the fish can see. Every line you add is a line someone
must read, test, and later delete. Aim for the smallest change that the evidence
justifies, then check whether it can be smaller.

## Before you add, subtract

- Look for dead code, unused flags, and stale branches in the area you are about to
  touch. Removing them first often makes the change itself small.
- If a new requirement does not fit the current design, redesign the area as if the
  requirement had been there from the start. Bolting a special case onto a shape that
  never expected it is how code grows branches nobody can follow.

## Things that do not earn their place

| Temptation | Why it fails | Instead |
| :- | :- | :- |
| A helper, wrapper, or interface with one caller | One more hop for every reader, no reuse | Inline it until a second caller exists |
| An option or parameter "for later" | Untested paths, unclear defaults | Add it when a caller needs it |
| A guard for a state that cannot happen | Hides the real bug when the impossible happens | Let it fail loudly, or make the state unrepresentable in the types |
| Keeping the old API "just in case" | Two ways to do one thing, forever | Move every caller to the new one and delete the old one in the same change |
| A comment that repeats the code | Drifts out of date, adds noise | Keep only the why that the code cannot show |
| Formatting or renaming nearby code you were not asked to touch | Buries the real change in the diff | Leave it, and mention it if it matters |

## Shape the data, not the branches

When the same flags are checked in several places, or one function grows a long
if/else ladder, the data model is missing something. Name the states and their
transitions, or use a lookup table, a typed record, or a state machine. Then the
branches mostly disappear.

Validate and convert outside data (user input, files, network responses) once, at the
edge of the system. Inside, trust the types you converted to.

## Read your own diff

Before you call the work done, read the whole diff as a reviewer would. Remove what
the request does not need. Clean up only what your change orphaned (an import, a
variable, a helper that lost its last caller). Dead code that was there before is the
user's call. Mention it, do not delete it.
