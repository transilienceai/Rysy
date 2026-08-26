---
playbook: company-intelligence
applies_to_tiers: [A, B, C]
applies_to_personas: [all]
version: 0.1
last_updated: 2026-04-27
---

# Company intelligence

Most cold-email writers either over-research the company (turning the email into a press-release recap) or under-research it (missing the operational context that explains the prospect's week). This playbook covers the middle path — the company-side research that genuinely informs the email without overwhelming it.

## Why this playbook runs at all tiers

Even C-tier (lightweight) prospects need basic company context. A 5-minute pass on the company is the floor; A-tier extends this to 20-30 minutes.

## Stage 1 — The company snapshot

Capture from the company's site, LinkedIn page, and public records:
- Stage (private, public, recent IPO, acquired)
- Headcount range and trajectory (growing, flat, recently shrunk)
- Funding history (latest round, valuation if public, investor names)
- Sector and sub-sector (be specific — *fintech* is not specific enough; *B2B payments infrastructure* is)
- Geographic footprint (HQ + major offices)
- Public position on key topics (their own marketing claims, what they are *trying* to be known for)

Write this into a *Company snapshot* section of `research-notes.md`.

## Stage 2 — Recent events (last 90 days)

Search patterns:
- `"{company}" news`
- `"{company}" announcement OR launched OR raised`
- `site:techcrunch.com OR site:thelogger.com OR site:axios.com "{company}"` (for press)
- `"{company}" 8-K` (for public companies — disclosure events)
- `"{company}" earnings` (for public companies — quarterly context)
- `"{company}" hiring` (often signals priorities)

For each event found:
- Date
- Type (funding, launch, hire, acquisition, layoff, regulatory event, partnership)
- Operational implications for the prospect's role specifically

Operational implications matter most. A hire announcement is not just news; it is a signal about where they are investing. A layoff is not just news; it is a signal about budget posture. An IPO is not just news; it is a multi-quarter shift in how the prospect spends their week.

## Stage 3 — Hiring signals

The company's open job listings are some of the highest-signal data about *what they care about right now*. Search:
- The company's careers page
- LinkedIn jobs filter by company
- Job aggregators

For roles in the prospect's domain:
- What roles are open?
- What level (IC vs. management)?
- What does the description emphasize? (tools, frameworks, experience markers)
- How long has the role been open?

A persistent open senior role with a specific tool requirement signals an active investment direction. A wave of mid-level roles in a specific area signals a build-out.

## Stage 4 — Public content from the company

The company's own content (blog, social, talks):
- What are they publishing about?
- Which executives are publicly speaking, and on what topics?
- What is the messaging emphasis right now? (tech depth vs. customer wins vs. category narrative)

This catches whether the prospect's company is in *story-telling mode*, *building mode*, or *customer-acquisition mode* — different modes call for different outreach angles.

## Stage 5 — Synthesis: the operational moment

The synthesis question after Stages 1-4: *what is the operational moment this company is in, and how does that shape the prospect's week*?

Examples of operational moments:
- Just-IPO: every executive's calendar is full of investor meetings; budget posture is conservative
- Just-funded: hiring rapidly; tooling decisions are easier; ambition is high
- Post-layoff: budget tight; trust in vendors low; consolidation priority
- Pre-IPO regulatory prep: compliance and risk topics dominate; CISO/legal in pole position
- Mid-migration: platform team is overcommitted; non-migration tooling decisions get deferred

Write the operational moment as one paragraph in `research-notes.md` under *Operational moment*.

## What the operational moment unlocks

The operational moment shapes:
- Which trigger events are credible
- Which value propositions are likely to land *this quarter*
- Whether to lead with risk framing or growth framing
- Whether the prospect's calendar is open or chaotic right now (which affects ask weight)

A great cold email is partly about the prospect, partly about the moment they are in. Without the moment, the prospect-side research is half the picture.

## Anti-patterns

- Reciting the company's mission statement back to them
- Praising the company's recent funding round
- Listing logos of their customers (this is for the writer's company, not Rysy's)
- Quoting their CEO's recent statement to them (they have read it; you have not added value)
- Confusing what they say they care about (marketing) with what they actually invest in (hiring, headcount, talks)

## Time budget

- C-tier: 5-10 minutes (Stages 1 and 2 only)
- B-tier: 15-25 minutes (Stages 1-3)
- A-tier: 30-45 minutes (all five stages)
