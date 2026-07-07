---
name: apply-approved-diff
description: Apply a human-approved character diff from experience/journal/proposed-character-diffs/ to self/character.md. The ONLY sanctioned path for self/ to change. Use when the user invokes /apply-diff with a path to an approved diff file. Do NOT invoke autonomously — diff application requires explicit human approval.
---

# apply-approved-diff

The only sanctioned path for `self/character.md` to change.

## When to invoke

- User runs `/apply-diff <path-to-proposed-diff-file>`
- The proposed diff file at the supplied path has `approved_by` and `approved_at` set in its frontmatter

This skill MUST NOT be invoked autonomously. The diff requires human approval as part of the constitution-versus-memory dialectic.

## Inputs

- `diff_path` — path to the proposed-diff file (under `experience/journal/proposed-character-diffs/`)

## Happy path

Validate the diff has been human-approved. Read the current character.md. Compute the new content. Drop the marker file `.claude/.diff-in-progress`. Write the modified character.md. Remove the marker. Sanity-check. Archive the diff. Log the change. Trigger reindex.

## The marker-file contract

The `pre-write-self-protect.py` hook blocks every write to `self/` *unless* `.claude/.diff-in-progress` exists. This skill is the only thing allowed to create that marker, and it MUST remove the marker immediately after the write — even on failure paths.

The full step-by-step procedure, with the exact bash commands and failure recovery, is in `references/workflow.md`.

## Hard rules

1. Never bypass the marker contract — always create the marker before writing, always remove it after (success or failure).
2. Never apply a diff that lacks `approved_by` or `approved_at` in frontmatter.
3. Never apply a diff whose *What I propose changing* text does not match current `character.md` exactly — surface as stale.
4. Never delete the proposed-diff file — archive it to `applied-character-diffs/` so the audit trail survives.
5. Never invoke this skill autonomously. Only on explicit `/apply-diff` invocation.

## Failure modes

Documented in `references/workflow.md` under *Failure recovery*. The critical invariant: the marker file is always cleaned up.
