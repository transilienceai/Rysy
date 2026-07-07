---
name: run-campaign
description: Orchestrate a cold-outreach campaign end-to-end — read input JSON, iterate leads through researcher → profiler → drafting → witness, write output JSON. Use when the user invokes /run-campaign, asks Vendy to process a campaign, or hands you a path to a campaign input file. Do NOT use for one-off single-prospect drafts.
---

# run-campaign

The canonical workflow for processing a cold-outreach campaign end-to-end.

## When to invoke

- User runs `/run-campaign <path-to-input.json>`
- User asks Vendy to process a campaign and provides input data
- User pastes a campaign brief and lead list together

## Inputs

A campaign input JSON with three top-level blocks: `campaign`, `sender`, `leads[]`.

The full schema is in `references/input-schema.md`. Read it before validating input.

## Outputs

For the campaign as a whole, files are written under `experience/campaigns/{campaign-id}/`. For each lead, files are written under `experience/prospects/{lead-id}/`. The full output layout — including the per-lead folder shape, the campaign folder shape, and the structured `output.json` — is in `references/output-schema.md`.

## Happy path (one paragraph)

Validate input. Set up `experience/campaigns/{campaign-id}/`. If `craft/trends/current.md` is older than 14 days, invoke `refresh-trends` first. For each lead: create the prospect folder, run a disqualify pre-check, invoke the `researcher` sub-agent, invoke the `profiler` sub-agent, draft in your main thread (consulting voice palette + persona + craft as needed), let the witness review the draft, rewrite once if rejected, finalize or flag. After each lead, invoke `take-craft-note` if you noticed something worth recording. When the campaign closes, write `output.json`, `results-summary.md`, `run-log.md`, and `what-i-learned.md`, then trigger `reindex-memory`.

## Detailed workflow

The full step-by-step workflow with edge cases, retry logic, and failure modes is in `references/workflow.md`. Read it before processing your first lead.

## Hard rules

1. Never skip the witness on any draft.
2. Never draft for a prospect whose disqualify check fired.
3. Never loop more than one rewrite attempt on a witness rejection — escalate to human flag.
4. Never write to `self/` from this skill (that path is reserved for `apply-approved-diff`).
5. Never exceed `max_email_length_sentences` from the campaign brief.

## Failure modes

Documented in `references/workflow.md` under *Failure modes*.
