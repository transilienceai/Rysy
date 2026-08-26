# proposed-character-diffs/

Pending changes to `self/character.md` awaiting human approval.

## Workflow

1. Rysy or the `introspecter` sub-agent writes a proposed diff file here
2. A human reviews the diff
3. If approved, the human sets `approved_by` and `approved_at` in the file's frontmatter
4. The human invokes `/apply-diff <path-to-this-file>`
5. The `apply-approved-diff` skill applies the diff to `self/character.md`, archives the diff to `experience/journal/applied-character-diffs/`, and logs the change

## Why this exists

The `pre-write-self-protect.py` hook blocks every direct write to `self/`. The only path for Rysy's constitution to change is through this directory, with a human in the loop. This is the architectural enforcement of the constitution-versus-memory dialectic.

## What does *not* belong here

- Notes about Rysy's recent work (those go in `experience/journal/adhoc/` or `experience/journal/monthly/`)
- Pattern proposals (those go through `promote-pattern` to `craft/patterns/`)
- Open questions (those go in `craft/open-questions.md`)

This directory is exclusively for proposed changes to `self/character.md`. Other reflective writing has its own home.

## Format

See `experience/journal/README.md` for the proposed-diff file format.
