---
playbook: web-discovery
applies_to_tiers: [A, B]
applies_to_personas: [all]
version: 0.1
last_updated: 2026-04-27
---

# Web discovery — beyond LinkedIn

For senior prospects, LinkedIn is necessary but not sufficient. The strongest research signals often come from the web outside LinkedIn — talks, podcasts, blog posts, press, GitHub, public records. This playbook covers the search patterns that find what LinkedIn misses.

## Search query patterns

Use these queries (substitute the prospect's name and company):

**Talks and presentations**
- `"{name}" site:youtube.com`
- `"{name}" keynote OR "talk"`
- `"{name}" "presented" OR "spoke at"`
- `"{name}" "{conference name}"` (for known conferences in their domain)

**Podcasts**
- `"{name}" podcast`
- `"{name}" "interviewed"`
- `"{name}" site:overcast.fm OR site:apple.com/podcasts`

**Writing**
- `"{name}" blog`
- `"{name}" site:medium.com OR site:substack.com`
- `"{name}" "published" OR "wrote"`

**Press and quotes**
- `"{name}" "{company}" "said"`
- `"{name}" "{company}" "told"` (catches journalist quotes)
- `"{name}" press release`

**Aggregators and bio sources**
- Crunchbase profile (often has investor or board context)
- AngelList (for startup-adjacent prospects)
- Sched, Lanyrd-archive (conference history)

**Cross-references**
- `"{name}" "{prior company}"` — captures their writing/talks about their prior role
- `"{name}" + "{specific topic from LinkedIn}"` — confirms whether a topic they posted about has external depth

## What to look for

For each external item found:

- **Date** (recency matters — old talks are less relevant unless they reference foundational thinking)
- **Format** (talk, podcast, blog post, quote in press, paper, etc.)
- **Substance** (what claim or argument did they make?)
- **A quotable sentence** (verbatim — these are the most useful for warm-observational openers)

Write these into the *External trail* section of `research-notes.md`.

## Hierarchy of signal value

External signals weighted highest to lowest:

1. **Their own longform writing** (Substack, personal blog, technical posts) — direct insight into their thinking
2. **Conference talks with available video/transcript** — they thought about this, prepared, presented; high signal
3. **Podcast appearances** — they thought out loud, often more candid than written content
4. **Quoted comments in journalism** — short but verified
5. **Mentions in others' content** — useful for context, not for direct read of their thinking
6. **Press releases mentioning them** — generally low signal (PR-shaped)

## The 2-hour limit

For A-tier research, web discovery should not exceed 60 minutes. For B-tier, 20 minutes. The diminishing returns curve flattens quickly — after the first hour of search you are scraping for marginal signal.

If a prospect has very thin web presence (no talks, no writing, no quotes), that *itself* is information — they are not a public-facing operator. Note this and shift research weight to company intelligence and engagement-web inferences.

## Anti-patterns

- Following every link found regardless of relevance (do triage)
- Reading whole talks when transcripts/summaries suffice
- Citing aggregator content (Crunchbase summary, Wikipedia) as primary signal
- Treating Twitter/X content as equivalent to longform — Twitter is fast and thin, useful for trigger events but rarely for deep portrait
- Forgetting to capture verbatim quotes — paraphrases lose the prospect's voice, which is what the warm-observational register needs

## Output integration

External trail findings go into the *External trail* section of `research-notes.md`. Quotable sentences go in a sub-section *Verbatim quotes* with date and source. Trigger candidates from external trail get noted in the cross-stage *Trigger event* synthesis.
