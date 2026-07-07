# experience/campaigns/

Per-campaign records. One folder per campaign, the unit of work and the audit trail.

## Folder shape per campaign

Each campaign's folder lives at `campaigns/{campaign-id}/` and contains:

- **`input.json`** — the original input JSON, copied here by `run-campaign` at the start of processing
- **`brief.md`** — a human-readable distillation of the campaign brief (sender, service line, value-prop anchors, case studies, goal, CTA, voice constraints, must-references)
- **`output.json`** — the final output JSON with all per-lead drafts and metadata
- **`results-summary.md`** — drafted vs skipped vs flagged counts; brief notes on each skip and flag
- **`run-log.md`** — timestamped event log of the campaign run: every sub-agent invocation, every witness verdict, every error
- **`what-i-learned.md`** — Vendy's post-campaign reflection: what landed, what didn't, what notes were taken, what patterns may be candidates for promotion

## Why no inbox/outbox

Earlier designs had separate `inbox/` and `outbox/` directories at the project root. The current design folds both into the campaign folder itself: `input.json` and `output.json` live with the campaign record. This eliminates desynchronization between staging directories and the audit trail, and makes the campaign folder the single canonical location for everything related to that campaign.

## Workflow

1. You write the campaign input JSON anywhere convenient (or place it in the project root as `pending-campaign.json`)
2. You invoke `/run-campaign <path-to-input.json>`
3. The `run-campaign` skill creates `campaigns/{campaign-id}/`, copies the input to `input.json`, processes the campaign, and writes the remaining files
4. You read `output.json`, `results-summary.md`, and any flagged drafts in `experience/prospects/` for human review
5. You send the approved drafts manually (Phase 1)

## Campaign-id generation

The `campaign-id` is taken from the input JSON's `campaign.id` field if present, otherwise generated as `{date}-{slug-of-campaign-name}` by `run-campaign`.

## INDEX.md

`campaigns/INDEX.md` is rebuilt by `reindex-memory` and lists all campaigns: id, date, sender, service line, total leads, drafted count, skipped count, flagged count.

## What does *not* live here

- Per-prospect research and drafts (those live in `experience/prospects/{lead-id}/`)
- Vendy's introspective reflections (those live in `experience/journal/`)
- Craft notes triggered by the campaign (those live in `craft/notes/`)
- Patterns promoted from the campaign (those live in `craft/patterns/`)

The campaign folder is for *campaign-level* artifacts. Per-prospect and reflective material live in their own homes.
