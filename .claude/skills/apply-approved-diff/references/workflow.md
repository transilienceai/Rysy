# Detailed workflow — apply-approved-diff

The happy path is in SKILL.md. This file documents every step, the exact bash commands, and the failure-recovery invariants.

## 1. Validate

- Read the diff file at the supplied path
- Confirm `approved_by` is non-null
- Confirm `approved_at` is a valid ISO-8601 timestamp
- Confirm `status` is `pending` or `approved` (set to `approved` if currently `pending` and `approved_by` is set)
- If validation fails: stop, report missing approval, do NOT drop marker

## 2. Read the diff

The diff body has these sections:
1. *What I propose changing* — the exact quoted text from `self/character.md` that should change
2. *To what* — the replacement text
3. *Why* — reasoning + evidence references
4. *What stays the same* — the explicit non-cascade confirmation

## 3. Stage the apply

- Read current `self/character.md` (Read tool — allowed)
- Locate the *What I propose changing* text in the file
- If exact match not found: stop, report stale diff, do NOT drop marker
- Compute the new file content with *To what* substituted in

## 4. Drop the marker (THE KEY STEP)

```bash
touch .claude/.diff-in-progress
```

The marker's existence tells `pre-write-self-protect.py` this skill is in flight. Without the marker, the next step is denied.

## 5. Write the modified character.md

Use the Write tool. The hook sees the marker and allows. Verify the write succeeded.

## 6. Remove the marker IMMEDIATELY

```bash
rm -f .claude/.diff-in-progress
```

Do this even if step 5 failed. Leaving the marker in place is a safety hole.

## 7. Sanity check

- Re-read the modified `self/character.md`
- Verify markdown structure is intact and expected sections are present
- If anything is off: surface for human review (do not auto-rollback — preserves audit trail)

## 8. Archive the diff

- Move the diff file from `experience/journal/proposed-character-diffs/` to `experience/journal/applied-character-diffs/`
- Rename to `{original-filename}-applied-{date}.md`
- Update its frontmatter `status: applied`

## 9. Log

Write `experience/journal/adhoc/{date}-character-diff-applied.md`:
- Reference to the original proposed-diff (now archived)
- Summary of the change
- Approver, approval timestamp, application timestamp
- Reasoning section copied from the diff

## 10. Trigger reindex

Invoke the `reindex-memory` skill.

## 11. Surface result

Report to user:
- Confirmation
- Sections of `character.md` that changed
- Path to the journal entry recording the change

## Failure recovery

The critical invariant: **the marker file is always cleaned up**. The cleanest pattern wraps the marker drop / write / marker remove as a sequence with cleanup on every error path:

```bash
# Drop marker
touch .claude/.diff-in-progress

# (Write tool to character.md — may fail)

# Always remove marker, even on failure
rm -f .claude/.diff-in-progress
```

If the Write fails, immediately remove the marker before reporting the error.

If a marker is found at session start without an active apply-approved-diff invocation (a stale marker from a crashed run), the human can manually `rm .claude/.diff-in-progress` to restore the protection. The marker path is in `.gitignore` so it never gets committed.

## Why marker file, not env var

Earlier designs used `RYSY_APPLY_APPROVED_DIFF_ACTIVE` as an env var. Env vars set by the agent's Bash do not reliably propagate to hook subprocesses on most platforms — the hook's subprocess inherits Claude Code's env, not the agent's transient env. The marker file is filesystem-state, which the hook reads deterministically. It is the cleaner pattern.
