---
description: Apply a human-approved character diff from experience/journal/proposed-character-diffs/ to self/character.md. The only sanctioned path for self/ to change.
argument-hint: <path-to-proposed-diff-file>
---

Invoke the `apply-approved-diff` skill on the proposed-diff file at the path I'm about to give you.

Path: $ARGUMENTS

The skill's instructions are in `.claude/skills/apply-approved-diff/SKILL.md`.

Validate that the diff has been human-approved (frontmatter `approved_by` is non-null, `approved_at` is set). If validation fails, stop and report — do NOT apply the diff. If valid, apply it to `self/character.md`, archive the diff to `experience/journal/applied-character-diffs/`, write a journal entry recording the change, and trigger reindex-memory.

Report the sections of `character.md` that changed.
