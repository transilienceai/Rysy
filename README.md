# Rysy

<div align="center">

[![Built by Transilience](https://img.shields.io/badge/Built%20by-Transilience.ai-4A90D9)](https://www.transilience.ai)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GitHub stars](https://img.shields.io/github/stars/transilienceai/Rysy)](https://github.com/transilienceai/Rysy/stargazers)
[![Claude AI](https://img.shields.io/badge/Powered%20by-Claude%20AI-blue)](https://claude.ai)

**An open-source Claude Code agent that does the homework before you reach out to anyone — researches people, builds psychological portraits, and crafts approaches calibrated to the person and your intent — from the team at [Transilience.ai](https://www.transilience.ai)**

[Quick Start](#-quick-start) | [Personas](#-who-its-for) | [Architecture](#-architecture) | [Customization](#-customization) | [Website](https://www.transilience.ai)

</div>

---

## Overview

**Rysy** is a Claude Code agent that researches people using browser automation (LinkedIn, the web), builds psychological portraits from public signals, and helps you craft an approach calibrated to the person and your intent — whether you're pitching an investor, applying to a job, preparing for a podcast interview, or reaching out to a customer.

The core pipeline: **research** → **profile** → **strategize** → **witness review**.

Same engine, different outputs — the intent is the variable.

### Why Rysy?

- **Deep research, not templates** — drives Claude in Chrome through your logged-in LinkedIn and the web to read real signals
- **Psychological portraits** — synthesizes research into how someone thinks, what they care about, and what would earn their attention
- **Intent-driven output** — the same pipeline produces investor cold notes, interview questions, networking briefs, or outreach drafts depending on your goal
- **Built-in quality control** — every draft is reviewed by an independent witness agent that doesn't know it's reviewing your work
- **Accumulating craft** — learns from every campaign through notes, patterns, and trend tracking
- **Fully customizable** — rewrite the constitution, research playbooks, and voice palette for your domain

---

## 🎯 Who it's for

| Persona | Scenario | What Rysy produces | Why it beats doing it manually |
|---|---|---|---|
| **Founder raising a round** | Researching investors before cold outreach | Investor profile (thesis, recent bets, stated vs. revealed preferences), tailored angle, warm-intro path analysis, draft cold note | Reads the investor's actual activity — reposts, comments, arguments — and finds the gap between their marketed thesis and their revealed one |
| **Job seeker** | Understanding a hiring manager before applying or interviewing | Hiring manager portrait, team context (recent hires, departures, open problems), interview angle, cover letter draft | Turns "why I'm a fit" into "here's the problem you're solving and why my background maps to it" |
| **Sales or BD rep** | Customer outreach to senior buyers | Prospect portrait, objection map, approach strategy (angle, tone, timing, CTA), draft outreach with witness review | Deep research → personalized outreach instead of templating at volume |
| **Journalist or podcaster** | Prepping for a guest interview | Guest dossier (career arc, positions, intellectual evolution), prior interview digest, question bank ranked by novelty | Surfaces the thread nobody has asked them to pull on yet — the question that makes them lean forward |
| **VC or angel investor** | Evaluating a founder before or after a pitch | Founder profile (builder evidence, leadership signals), narrative consistency check, reference-call prep questions | Catches what a LinkedIn skim misses — commit history vs. "technical founder" claims, team churn the deck omits |
| **Conference attendee** | Prepping for an event with a speaker or attendee list | Priority-ranked briefs, conversation hooks per person, connection graph, personalized follow-up templates | Fifteen people researched overnight instead of five minutes of panic-Googling between sessions |
| **Recruiter** | Sourcing and reaching out to senior candidates | Candidate portrait (trajectory, motivational signals, move-readiness), role-fit mapping, outreach draft | Produces outreach that reads like someone who actually looked — because the agent actually did |

---

## 🚀 Quick Start

### 1. Clone and open

```bash
git clone https://github.com/transilienceai/Rysy.git
cd Rysy
claude    # Launch Claude Code
```

### 2. Install Claude in Chrome

Install [Claude in Chrome](https://chromewebstore.google.com/detail/claude-in-chrome/) for browser-driven research. Without it, the researcher falls back to WebFetch and WebSearch for publicly available information.

### 3. Populate market context

```
/refresh-trends
```

### 4. Run your first campaign

```
/run-campaign path/to/your-campaign.json
```

> **First time setting up?** See [`LOCAL_SETUP.md`](LOCAL_SETUP.md) for the full walkthrough — installing Claude Code, trusting the hooks, granting permissions, and connecting Claude in Chrome.

---

## ⚙️ How It Works

You give Rysy a list of people (with LinkedIn URLs) and an intent. Rysy runs four sub-agents:

| Agent | Role |
|-------|------|
| **Researcher** | Drives Claude in Chrome through your logged-in LinkedIn session and the broader web. Loads playbooks from `craft/research-methodology/`. Writes structured research notes. |
| **Profiler** | Reads the research notes in a separate context (so the synthesis isn't colored by the main agent's voice) and writes a psychological portrait. |
| **Rysy** | Reads the portrait and crafts an approach strategy + draft output calibrated to the person and your stated intent. |
| **Witness** | Reviews each draft from a stranger's perspective. Returns `ship \| rewrite \| flag` with prose. The witness does not know it is reviewing your work — that isolation is the point. |

---

## 📥 Input

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

### Supported Intents

The `intent` field shapes the entire pipeline — what the researcher prioritizes, what the profiler emphasizes, and what the output looks like.

| Intent | What it researches |
|--------|-------------------|
| `investor-outreach` | Thesis, portfolio, recent bets, stated vs. revealed preferences |
| `job-application` | Hiring manager, team trajectory, open problems, culture signals |
| `customer-outreach` | Pain points, decision-making style, competitive landscape |
| `interview-prep` | Prior appearances, intellectual positions, unexplored topics |
| `founder-diligence` | Builder credibility, team signals, narrative consistency |
| `event-networking` | Batch-research attendees, connection paths, conversation hooks |
| `candidate-outreach` | Career trajectory, motivational signals, move readiness |
| `custom` | Define your own research priorities and output format |

---

## 📤 Output

After running, you'll find:

| File | Contents |
|------|----------|
| `experience/campaigns/{id}/output.json` | Structured output with drafts, witness verdicts, and review flags |
| `experience/campaigns/{id}/results-summary.md` | Drafted vs. skipped vs. flagged counts |
| `experience/campaigns/{id}/run-log.md` | Timestamped event log |
| `experience/campaigns/{id}/what-i-learned.md` | Rysy's post-campaign reflection |
| `experience/prospects/{lead-id}/` | Full per-prospect working folder (research notes, portrait, drafts) |

Drafts marked `ready_to_send: true` passed both the deterministic quality detector and the witness review. Drafts marked `human_review_required: true` need your eyes.

---

## 🏗️ Architecture

### Three Memory Layers

| Layer | Purpose | Mutability |
|-------|---------|------------|
| **`self/`** | Constitution and voice palette | Slow-moving. Human-approved changes only via `/apply-diff` |
| **`craft/`** | Canon, exemplars, personas, psychology, research playbooks, notes, patterns, trends | Accumulates freely through use |
| **`experience/`** | Journal, prospects (gitignored), campaigns | Written every campaign |

### Skills

| Skill | Purpose |
|-------|---------|
| `run-campaign` | Top-level orchestration |
| `take-craft-note` | Atomic dated observation |
| `promote-pattern` | Promote note clusters to patterns with evidence |
| `refresh-trends` | Pull and filter current market narratives |
| `apply-approved-diff` | The only path to change `self/character.md` |
| `reindex-memory` | Rebuild INDEX files across the library |

### Hooks

Six hooks enforce guardrails automatically — self-protection, quality detection, witness triggers, and session lifecycle management.

---

## 🔧 Customization

Rysy is designed to be adapted to your domain. Key extension points:

| Extension Point | What to customize |
|-----------------|-------------------|
| **`self/character.md`** | The constitution — who the agent *is*, not what it does |
| **`self/voice-palette/`** | Register modes (dry-precise, warm-observational, diagnostic, etc.) for different people |
| **`craft/personas/`** | Persona templates for the types of people you interact with |
| **`craft/research-methodology/`** | Research playbooks — what to look for, where to look, how to weigh signals |
| **`craft/exemplars/`** | 5-10 examples of great output for your use case |
| **`craft/canon/`** | The intellectual lineage your agent draws from |

---

## 🔒 Privacy

`experience/prospects/` contains personal data about real people and is gitignored. Treat it accordingly.

Research is conducted through your own logged-in browser session — Rysy sees what you can see. No scraping APIs, no data brokers, no dark patterns. The line between attention and intrusion is part of the constitution.

---

## 🗺️ Roadmap

- **Phase 1 (now)** — research → portrait → strategy → draft → witness review; output for human review
- **Phase 2** — memory across campaigns; promoted patterns inform future work; cross-campaign retrieval
- **Phase 3** — fuller autonomy: target identification → research → outreach → reply handling → follow-up with guardrails

---

## Project Stats

| Category | Count |
|----------|-------|
| **Sub-agents** | 4 (researcher, profiler, witness, introspecter) |
| **Skills** | 6 |
| **Hooks** | 6 |
| **Supported Intents** | 8 |
| **Research Playbooks** | 7 |
| **Voice Registers** | 4 |

---

## Community & Support

- [GitHub Issues](https://github.com/transilienceai/Rysy/issues) — Report bugs, request features
- [Transilience.ai](https://www.transilience.ai) — See what else we're building
- [LinkedIn](https://linkedin.com/company/transilienceai) — Follow our work
- [Email](mailto:contact@transilience.ai) — Get in touch

---

## License

MIT License — Copyright (c) 2026 Transilience AI. See [LICENSE](LICENSE) for details.

---

## Contributors

<a href="https://github.com/transilienceai/Rysy/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=transilienceai/Rysy" />
</a>

---

<div align="center">

**Built by [Transilience AI](https://www.transilience.ai)**

We build AI-driven cloud security and compliance automation. Rysy is how we think about people research — if you're curious about what else we're building, [take a look](https://www.transilience.ai).

[![Star this repository](https://img.shields.io/badge/Star%20this%20repo-yellow?style=for-the-badge)](https://github.com/transilienceai/Rysy)

[Website](https://www.transilience.ai) | [Issues](https://github.com/transilienceai/Rysy/issues)

`claude-code` `ai-agent` `people-research` `outreach` `linkedin` `browser-automation` `psychological-profiling` `investor-outreach` `job-search` `sales` `recruiting` `multi-agent`

</div>
