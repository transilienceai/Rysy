# Campaign input JSON schema

The campaign input has three top-level blocks: `campaign`, `sender`, `leads[]`.

## Top level

```json
{
  "campaign": { ... },
  "sender": { ... },
  "leads": [ ... ]
}
```

## campaign

```json
{
  "id": "string",                         // optional; generated if absent
  "name": "string",
  "service_line": "string",                // what we're pitching
  "value_prop_anchors": ["string"],        // 1-3 short proof points
  "case_studies": [
    {"company": "string", "sector": "string", "outcome": "string"}
  ],
  "campaign_goal": "book-call|reply|share-doc|intro",
  "desired_cta": "string",                 // suggested wording; Rysy may improve
  "avoid_topics": ["string"],
  "must_reference": ["string"],
  "tone_shift": "default|formal|casual",
  "max_email_length_sentences": 6
}
```

## sender

```json
{
  "name": "string",
  "title": "string",
  "company": "string",
  "company_one_liner": "string",
  "email_signature": "string",
  "voice_notes": "string",                 // free-form; how this human writes
  "credible_claims": ["string"]            // things this human can actually say
}
```

## leads[]

Each lead:

```json
{
  "id": "string",
  "priority": "A|B|C",
  "person": {
    "name": "string",
    "linkedin_url": "string",
    "email": "string|null",
    "title": "string|null",
    "location": "string|null"
  },
  "company": {
    "name": "string",
    "domain": "string|null",
    "linkedin_url": "string|null",
    "industry": "string|null",
    "stage": "string|null",
    "size_range": "string|null"
  },
  "context": {
    "prior_touches": [
      {"date": "string", "channel": "string", "outcome": "string", "summary": "string"}
    ],
    "mutual_connections": ["string"],
    "pre_attached_intel": "string",
    "trigger_event": "string|null",
    "disqualify_signals_check": ["string"]
  }
}
```

## Validation rules

- `campaign.service_line`, `campaign.campaign_goal`, `sender.name`, `sender.company` are required
- Each lead must have `id` (or one is generated), `priority`, `person.name`, and `person.linkedin_url`
- `priority` must be one of `A`, `B`, `C`
- `campaign_goal` must be one of `book-call`, `reply`, `share-doc`, `intro`
- `leads[]` may be empty (the skill exits early with a no-op summary)

If any required field is missing, stop with a structured error report and do not process any leads.
