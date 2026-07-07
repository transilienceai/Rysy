# Vendy

A Claude Code-based cold-outreach agent for senior technical buyers — CISOs, CTOs, VPs of Engineering, VPs of Security, Heads of Product Security.

Vendy is built as a digital salesperson with a constitution, a voice palette, an accumulating library of craft, and a record of her own work. She uses Claude in Chrome to research prospects through their actual logged-in LinkedIn session and the broader web, the way a thoughtful human SDR would — but faster.

This is **Phase 1**: she takes campaign input as JSON, processes leads end-to-end (research → profile → draft → witness review), and produces output JSON of drafts for human review and send. Phase 2 will add memory across campaigns; Phase 3 will move toward fuller autonomy.

## How to run

Open this folder in Claude Code. The session-start hook will print Vendy's welcome banner and inject her character, latest journal entry, and current trends into context.

To run a campaign:

```
/run-campaign path/to/your-campaign-input.json
```

To trigger introspection:

```
/introspect
```

To refresh the trends file:

```
/refresh-trends
```

To promote pattern candidates from accumulated notes:

```
/promote-patterns
```

To apply a human-approved character diff:

```
/apply-diff experience/journal/proposed-character-diffs/2026-04-27-some-diff.md
```

## Input JSON shape

A campaign input has three blocks: `campaign`, `sender`, `leads[]`.

```json
{
  "campaign": {
    "id": "q2-2026-fintech-ciso",
    "name": "Q2 fintech CISO campaign",
    "service_line": "detection-as-code observability for SOC tier-1",
    "value_prop_anchors": [
      "cuts alert triage time on lateral movement detections",
      "integrates as a SIEM-side reader, no replace"
    ],
    "case_studies": [
      {"company": "Acme Bank", "sector": "fintech", "outcome": "MTTD on lateral-movement signal cut from 22m to 6m"}
    ],
    "campaign_goal": "book-call",
    "desired_cta": "fifteen minutes next week to compare notes on detection-debt economics",
    "avoid_topics": ["AI buzzwords without specifics"],
    "must_reference": [],
    "tone_shift": "default",
    "max_email_length_sentences": 6
  },
  "sender": {
    "name": "Your Name",
    "title": "Founder",
    "company": "Your Company",
    "company_one_liner": "we run a detection-engineering platform that sits alongside your SIEM",
    "email_signature": "Best,\nYour Name\nFounder, Your Company",
    "voice_notes": "I write short, hate exclamation marks, sign with first name only",
    "credible_claims": ["ex-detection-engineer at Stripe", "based in NYC next week"]
  },
  "leads": [
    {
      "id": "jane-doe-acme-fintech",
      "priority": "A",
      "person": {
        "name": "Jane Doe",
        "linkedin_url": "https://linkedin.com/in/jane-doe-ciso",
        "email": null,
        "title": "CISO",
        "location": null
      },
      "company": {
        "name": "Acme Bank",
        "domain": "acmebank.com",
        "linkedin_url": "https://linkedin.com/company/acme-bank",
        "industry": "fintech",
        "stage": "post-IPO",
        "size_range": "5000-10000"
      },
      "context": {
        "prior_touches": [],
        "mutual_connections": [],
        "pre_attached_intel": "",
        "trigger_event": null,
        "disqualify_signals_check": ["recent layoff", "active breach disclosure", "PTO indicator"]
      }
    }
  ]
}
```

## Output

After running, you'll find:

- `experience/campaigns/{campaign-id}/output.json` — the structured output with drafts, witness verdicts, ready-to-send flags, and human-review flags
- `experience/campaigns/{campaign-id}/results-summary.md` — drafted vs skipped vs flagged counts
- `experience/campaigns/{campaign-id}/run-log.md` — timestamped event log
- `experience/campaigns/{campaign-id}/what-i-learned.md` — Vendy's post-campaign reflection
- `experience/prospects/{lead-id}/` — full per-prospect working folder for each lead processed

Drafts marked `ready_to_send: true` passed both the deterministic AI-tell detector and the witness sub-agent's probabilistic review. Drafts marked `human_review_required: true` need your eyes — the witness flagged them or they failed the rewrite cycle.

## Architecture

Three memory layers:

- **`self/`** — Vendy's constitution and voice palette. Slow-moving. Human-approved changes only.
- **`craft/`** — accumulating library: canon, exemplars, anti-canon, personas, psychology, research-methodology, cold-email knowledge, notes, patterns, trends, open questions.
- **`experience/`** — episodic memory: journal, prospects, campaigns.

Four sub-agents:

- **`researcher`** — drives Claude in Chrome through LinkedIn + web
- **`profiler`** — synthesizes research into a psychological portrait
- **`witness`** — reviews drafts from a stranger's perspective; returns ship/rewrite/flag
- **`introspecter`** — periodic check on whether character still matches practice

Six skills:

- `run-campaign`, `take-craft-note`, `promote-pattern`, `refresh-trends`, `apply-approved-diff`, `reindex-memory`

Six hooks:

- `session-start-load-self.sh` (welcome banner + context injection)
- `pre-write-self-protect.py` (blocks unauthorized writes to `self/`)
- `pre-write-tell-detector.py` (blocks drafts containing hard-blocked AI tells)
- `post-draft-trigger-witness.sh` (cues the witness on draft writes)
- `subagent-stop-log.sh` (logs sub-agent returns to campaign run-log)
- `session-end-reflect.sh` (triggers reindex; suggests pattern promotion)

Plus five slash commands and a Python lib for shared utilities.

## Repo layout: clean root + sample_state

- The **repo root** is a clean, ready-to-use Vendy — full framework and craft library, with the `experience/` output directories reset to empty scaffolding. This is what you open in Claude Code and run.
- **`sample_state/`** is a frozen snapshot of a real, evolving instance after it has processed campaigns — kept as a reference for what a populated Vendy looks like. See [`sample_state/README.md`](sample_state/README.md).

## Privacy

In the live root instance, `experience/prospects/` contains personal data about real people and is gitignored (anchored to the root). Treat it accordingly.

`sample_state/` **deliberately retains real prospect data** — names, work emails, LinkedIn URLs, and psychological profiles — as a demonstration snapshot. This is the reason this repository must stay **private**. Do not make it public without scrubbing that PII first.

## Required setup

- Claude Code installed
- Claude in Chrome MCP server available for the researcher to drive your logged-in browser. Until installed, the researcher falls back to WebFetch and WebSearch for what's publicly fetchable.
- Run `/refresh-trends` before the first campaign to populate `craft/trends/current.md`.
- Optionally seed `craft/exemplars/` with 5-10 of your team's best past cold emails (or curated public exemplars) before processing your first real campaign.

## Phase roadmap

- **Phase 1 (now)** — research → portrait → draft → witness; output JSON for human review and send
- **Phase 2** — memory across campaigns; promoted patterns inform future drafts; cross-campaign retrieval
- **Phase 3** — full autonomy: ICP → candidate sourcing → outreach → reply handling → follow-up cadence with guardrails

## The reference PDF

`vendy.pdf` is a designed reference of the whole project, laid out in the Transilience
design system (see `transilience/sales-doc`). Its source is `vendy.html` (self-contained
except Google Fonts and `assets/logo.png`). To regenerate after editing the HTML, print it
with headless Chrome:

```
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --disable-gpu --no-pdf-header-footer --virtual-time-budget=15000 \
  --print-to-pdf=vendy.pdf "file://$PWD/vendy.html"
```
