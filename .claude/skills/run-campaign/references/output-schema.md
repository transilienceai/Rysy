# Campaign output schema and folder layout

## Per-prospect folder

```
experience/prospects/{lead-id}/
├── brief.md                  # distilled lead context
├── research-notes.md         # researcher sub-agent output
├── psychological-portrait.md # profiler sub-agent output
├── drafts/
│   ├── v1.md                 # first draft
│   └── v2.md                 # rewrite if witness rejected v1
├── witness-feedback.md       # witness verdict and prose
├── final.md                  # final draft after witness ship
└── disqualify-check.md       # only present if a disqualify signal fired
```

## Per-campaign folder

```
experience/campaigns/{campaign-id}/
├── input.json                # original input copied here
├── brief.md                  # human-readable distillation of campaign block
├── output.json               # final structured output
├── results-summary.md        # drafted/skipped/flagged counts
├── run-log.md                # timestamped event log
└── what-i-learned.md         # post-campaign reflection
```

## output.json structure

```json
{
  "campaign_id": "string",
  "generated_at": "ISO-8601",
  "agent": "rysy",
  "results": [
    {
      "lead_id": "string",
      "status": "drafted|skipped|flag",
      "skip_reason": "string|null",
      "research_summary": {
        "linkedin_signal_strength": "high|med|low|none",
        "trigger_event": "string",
        "fallback_used": "individual|company|industry|none"
      },
      "draft": {
        "subject_line": "string",
        "body": "string",
        "voice_register_used": "string",
        "length_sentences": "number"
      },
      "witness": {
        "verdict": "ship|rewrite|flag",
        "what_works": "string",
        "what_fails": "string"
      },
      "ready_to_send": "boolean",
      "human_review_required": "boolean",
      "review_flags": ["string"]
    }
  ],
  "summary": {
    "total_leads": "number",
    "drafted": "number",
    "skipped": "number",
    "flagged": "number",
    "notes_added": "number",
    "patterns_promoted": "number"
  }
}
```

## ready_to_send and human_review_required

- `ready_to_send: true` requires: witness verdict = `ship` AND no review flags AND tell-detector did not block
- `human_review_required: true` is set when: witness verdict = `flag` OR rewrite cycle exhausted OR research insufficient OR a disqualify pre-check passed but research turned up a softer disqualify signal worth human eyes

These flags are the human reviewer's primary triage signal.
