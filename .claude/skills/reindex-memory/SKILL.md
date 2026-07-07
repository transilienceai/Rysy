---
name: reindex-memory
description: Rebuilds INDEX.md files across craft/ and experience/. Run after note-taking, pattern-promotion, character-diff application, or by the session-end hook for safety.
---

# reindex-memory

Walks the markdown library and rebuilds index files. Light-touch, fast, deterministic. No vector indexing — just markdown link tables.

## When to invoke

- Triggered by `take-craft-note` skill after each note write
- Triggered by `promote-pattern` skill after each promotion run
- Triggered by `apply-approved-diff` skill after each character change
- Auto-fired by the `session-end-reflect.sh` hook at session end (safety reindex)
- Manually invokable for debugging

## What it builds

### craft/INDEX.md

Top-level navigation across the library plus a brief recent-activity summary.

### craft/notes/INDEX.md

Table of all notes with date, slug, tags, status. Promoted notes get a `promoted-to:` column linking to the pattern.

### craft/patterns/INDEX.md

Table of all patterns with slug, promoted date, confidence, status, last-reaffirmed timestamp.

### craft/canon/INDEX.md

Table of all canon entries with slug and one-line description from each file's first paragraph.

### craft/exemplars/INDEX.md

Table with slug, persona-targeted, rhetorical-move, source. Used by drafter to query exemplars by persona+move.

### craft/anti-canon/INDEX.md

Table with slug, primary-failure, persona-targeted. Used by witness for anti-canon lookups.

### experience/prospects/INDEX.md

Table with lead-id, persona, industry, campaign, register-used, witness-verdict, outcome (when known), date.

### experience/campaigns/INDEX.md

Table with campaign-id, date, sender, service-line, total leads, drafted count, skipped count, flagged count.

## Workflow

### 1. Walk craft/

For each subdirectory, read frontmatter from each markdown file. Build the appropriate index table from the frontmatter fields.

### 2. Walk experience/

For each prospect folder and campaign folder, read the relevant frontmatter (from `final.md`, `output.json`, `witness-feedback.md`, `brief.md`).

### 3. Write index files

Each INDEX.md is replaced wholesale (not appended). The schema for each index is documented in the relevant directory's README.

### 4. Update craft/INDEX.md last-reindex timestamp

The top-level INDEX file's *Recent activity* section gets updated with current counts and the reindex timestamp.

### 5. Surface

Report to the user (or the calling skill):
- How many files were indexed across each subdirectory
- Any anomalies detected (files missing required frontmatter, broken links, orphaned references)

## Anomaly handling

If a file lacks required frontmatter, log it but do not fail the reindex. Continue and report the anomaly so the human can repair it. The reindex itself should be robust — a broken file in one corner of the library should not prevent the rest of the library from being indexed.

## What this skill does *not* do

- It does not edit content files. Only index files are written.
- It does not delete files. If a referenced file no longer exists, the index entry is omitted, but the original file is left alone.
- It does not perform any semantic operation (no clustering, no summarization, no inference). Indexing is purely structural.

## Performance

The library is small (hundreds of files at most in Phase 1). The reindex should complete in under 5 seconds. If it is slower, investigate — the operation is fundamentally fast.

## Why no vector indexing

Phase 1 deliberately avoids embeddings. Markdown indexes plus Grep/Glob over the file system are faster, more interpretable, and more debuggable than vector search at this scale. If retrieval becomes the bottleneck (it will not in Phase 1 with hundreds of files), Phase 2 can revisit.
