# Rysy

A Claude Code agent that does the homework before you reach out to anyone.

Rysy researches people using browser automation (LinkedIn, the web), builds psychological portraits from public signals, and helps you craft an approach calibrated to the person and your intent — whether you're pitching an investor, applying to a job, preparing for a podcast interview, or writing a cold email.

The core pipeline: **research** → **profile** → **strategize** → **witness review**.

Same engine, different outputs — the intent is the variable.

## Who it's for

| Persona | Scenario | What Rysy produces | Why it beats doing it manually |
|---|---|---|---|
| **Founder raising a round** | Researching investors before cold outreach | Investor profile (thesis, recent bets, stated vs. revealed preferences), tailored angle, warm-intro path analysis, draft cold note | Reads the investor's actual activity — reposts, comments, arguments — and finds the gap between their marketed thesis and their revealed one |
| **Job seeker** | Understanding a hiring manager before applying or interviewing | Hiring manager portrait, team context (recent hires, departures, open problems), interview angle, cover letter draft | Turns "why I'm a fit" into "here's the problem you're solving and why my background maps to it" |
| **Sales or BD rep** | Customer outreach to senior buyers | Prospect portrait, objection map, approach strategy (angle, tone, timing, CTA), draft outreach with witness review | The original Rysy use case — deep research → personalized outreach instead of templating at volume |
| **Journalist or podcaster** | Prepping for a guest interview | Guest dossier (career arc, positions, intellectual evolution), prior interview digest, question bank ranked by novelty | Surfaces the thread nobody has asked them to pull on yet — the question that makes them lean forward |
| **VC or angel investor** | Evaluating a founder before or after a pitch | Founder profile (builder evidence, leadership signals), narrative consistency check, reference-call prep questions | Catches what a LinkedIn skim misses — commit history vs. "technical founder" claims, team churn the deck omits |
| **Conference attendee** | Prepping for an event with a speaker or attendee list | Priority-ranked briefs, conversation hooks per person, connection graph, personalized follow-up templates | Fifteen people researched overnight instead of five minutes of panic-Googling between sessions |
| **Recruiter** | Sourcing and reaching out to senior candidates | Candidate portrait (trajectory, motivational signals, move-readiness), role-fit mapping, outreach draft | Produces outreach that reads like someone who actually looked — because the agent actually did |

## How it works

You give Rysy a list of people (with LinkedIn URLs) and an intent. Rysy runs four sub-agents:

1. **Researcher** — drives Claude in Chrome through your logged-in LinkedIn session and the broader web. Loads playbooks from `craft/research-methodology/`. Writes structured research notes.
2. **Profiler** — reads the research notes in a separate context (so the synthesis isn't colored by the main agent's voice) and writes a psychological portrait.
3. **Rysy (you)** — reads the portrait and crafts an approach strategy + draft output calibrated to the person and your stated intent.
4. **Witness** — reviews each draft from a stranger's perspective. Returns `ship | rewrite | flag` with prose. The witness does not know it is reviewing your work — that isolation is the point.

## Quick start

1. Install [Claude Code](https://docs.anthropic.com/en/docs/claude-code)
2. Clone this repo and open it in Claude Code
3. Install [Claude in Chrome](https://chromewebstore.google.com/detail/claude-in-chrome/) for browser-driven research (falls back to WebFetch/WebSearch without it)
4. Run `/refresh-trends` to populate market context
5. Run your first campaign:

```
/run-campaign path/to/your-campaign.json
```

> **First time setting up?** See [`LOCAL_SETUP.md`](LOCAL_SETUP.md) for the full walkthrough — installing Claude Code, trusting the hooks, granting permissions, and connecting Claude in Chrome.

## Input

A campaign input has three blocks: `campaign` (your intent and constraints), `sender` (who you are), and `leads[]` (the people to research).

```json
{
  "campaign": {
    "id": "2026-08-series-a-investors",
    "name": "Series A investor outreach",
    "intent": "investor-outreach",
    "context": "We're raising a Series A for our developer tools platform. $2M ARR, 40% MoM growth.",
    "desired_outcome": "Get a first meeting to walk through our metrics and product roadmap",
    "output_format": "cold-note",
    "constraints": {
      "tone": "founder-to-investor, direct, no pitch-deck language",
      "max_length_sentences": 5,
      "avoid": ["buzzwords", "flattery", "asking for money in the first email"]
    }
  },
  "sender": {
    "name": "Your Name",
    "title": "Co-founder & CEO",
    "company": "Your Company",
    "company_one_liner": "developer tools platform that cuts CI/CD pipeline time by 60%",
    "credible_claims": ["ex-infra at Stripe", "YC W24", "open-source project with 2k GitHub stars"]
  },
  "leads": [
    {
      "id": "sarah-chen-first-round",
      "person": {
        "name": "Sarah Chen",
        "linkedin_url": "https://linkedin.com/in/sarah-chen-vc",
        "title": "Partner",
        "location": "San Francisco"
      },
      "company": {
        "name": "First Round Capital",
        "domain": "firstround.com",
        "industry": "venture capital",
        "stage": "established"
      },
      "context": {
        "pre_attached_intel": "Led the Series A for DevToolsCo last year. Writes about developer experience on her blog.",
        "disqualify_signals_check": ["fund currently closed", "competitive portfolio conflict"]
      }
    }
  ]
}
```

The `intent` field shapes the entire pipeline — what the researcher prioritizes, what the profiler emphasizes, and what the output looks like. Supported intents:

- `investor-outreach` — research their thesis, portfolio, recent bets
- `job-application` — research the hiring manager, team, and company trajectory
- `customer-outreach` — research pain points, decision-making style, competitive landscape
- `interview-prep` — research prior appearances, intellectual positions, unexplored topics
- `founder-diligence` — research builder credibility, team signals, narrative consistency
- `event-networking` — batch-research attendees, find connection paths
- `candidate-outreach` — research career trajectory, motivational signals, move readiness
- `custom` — define your own research priorities and output format

## Output

After running, you'll find:

- `experience/campaigns/{campaign-id}/output.json` — structured output with drafts, witness verdicts, and review flags
- `experience/campaigns/{campaign-id}/results-summary.md` — drafted vs. skipped vs. flagged counts
- `experience/campaigns/{campaign-id}/run-log.md` — timestamped event log
- `experience/campaigns/{campaign-id}/what-i-learned.md` — Rysy's post-campaign reflection
- `experience/prospects/{lead-id}/` — full per-prospect working folder (research notes, portrait, drafts)

Drafts marked `ready_to_send: true` passed both the deterministic quality detector and the witness review. Drafts marked `human_review_required: true` need your eyes.

## Architecture

Three memory layers:

- **`self/`** — Rysy's constitution and voice palette. Slow-moving. Human-approved changes only via `/apply-diff`.
- **`craft/`** — accumulating library: canon (the lineage), exemplars, anti-canon, personas, psychology, research-methodology playbooks, notes (atomic observations), patterns (promoted from notes with evidence), trends (rolling market context), open questions.
- **`experience/`** — episodic memory: journal (introspective), prospects (per-lead working memory), campaigns (per-campaign records).

Four sub-agents:

- **`researcher`** — drives Claude in Chrome through LinkedIn + web
- **`profiler`** — synthesizes research into a psychological portrait
- **`witness`** — reviews output from a stranger's perspective; returns ship/rewrite/flag
- **`introspecter`** — periodic check on whether character still matches practice

Six skills:

- `run-campaign` — top-level orchestration
- `take-craft-note` — atomic dated observation
- `promote-pattern` — promote note clusters to patterns with evidence
- `refresh-trends` — pull and filter current market narratives
- `apply-approved-diff` — the only path to change `self/character.md`
- `reindex-memory` — rebuild INDEX files across the library

Six hooks enforce guardrails automatically — self-protection, quality detection, witness triggers, and session lifecycle management.

## Customization

Rysy is designed to be adapted to your domain. Key extension points:

- **`self/character.md`** — rewrite the constitution to match your values and voice. This is who the agent *is*, not what it does.
- **`self/voice-palette/`** — define register modes (dry-precise, warm-observational, diagnostic, etc.) for different prospect types.
- **`craft/personas/`** — add persona templates for the types of people you interact with (investors, hiring managers, enterprise buyers, etc.).
- **`craft/research-methodology/`** — customize research playbooks for your domain (what to look for, where to look, how to weigh signals).
- **`craft/exemplars/`** — seed with 5-10 examples of great output for your use case.
- **`craft/canon/`** — the intellectual lineage your agent draws from. Add books, thinkers, and frameworks relevant to your domain.

## Repo layout

- The **repo root** is a clean, ready-to-use Rysy — full framework and craft library, with `experience/` reset to empty scaffolding.
- **`sample_state/`** is a frozen snapshot of a real instance after processing campaigns — kept as reference for what a populated Rysy looks like. See [`sample_state/README.md`](sample_state/README.md).

## Privacy

`experience/prospects/` contains personal data about real people and is gitignored. Treat it accordingly.

Research is conducted through your own logged-in browser session — Rysy sees what you can see. No scraping APIs, no data brokers, no dark patterns. The line between attention and intrusion is part of the constitution.

## Required setup

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed
- [Claude in Chrome](https://chromewebstore.google.com/detail/claude-in-chrome/) MCP server for browser-driven research. Without it, the researcher falls back to WebFetch and WebSearch for publicly available information.
- Run `/refresh-trends` before the first campaign to populate `craft/trends/current.md`
- Optionally seed `craft/exemplars/` with examples of great output for your use case

## Roadmap

- **Phase 1 (now)** — research → portrait → strategy → draft → witness review; output for human review
- **Phase 2** — memory across campaigns; promoted patterns inform future work; cross-campaign retrieval
- **Phase 3** — fuller autonomy: target identification → research → outreach → reply handling → follow-up with guardrails

## Built with

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) — the agent runtime
- [Claude in Chrome](https://chromewebstore.google.com/detail/claude-in-chrome/) — browser automation for research
- [Transilience](https://transilience.ai) — where Rysy was born
