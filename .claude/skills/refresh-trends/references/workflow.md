# Detailed workflow — refresh-trends

Five phases. Phases 1-2 are mechanical; phase 3 (filter) is the judgment-heavy step.

## Phase 1 — Collection

For each configured source in `sources.yaml`:
- Fetch the last 7-14 days of content (RSS, web page, API as appropriate)
- Dump items into a working buffer with provenance: source, item title, link, date, raw excerpt

Goal: over-collect. The filter is the next phase.

## Phase 2 — Topic clustering

Group items by topic, not by source. The same story will appear in multiple sources if it is real.

For each item, tag with one or more topic slugs (e.g., `sec-cyber-disclosure`, `mcp-security`, `ai-red-teaming`, `post-quantum-migration`). A topic with only one source contribution is candidate noise; a topic with many is candidate signal.

## Phase 3 — Filter

For each candidate topic, apply the four criteria from `filter-criteria.md`:
1. Independent sources (≥3 unaffiliated)
2. Behavioral signal
3. Time depth (≥2 weeks)
4. Practitioner voice (≥1)

A topic must meet ALL FOUR to survive. Topics that fail any criterion are dropped. Log each drop with the failed criterion and a one-line reason.

## Phase 4 — Synthesis

For each surviving trend:
- **Title** — one short phrase
- **Summary** — 4-5 sentences: what it is, why it is hot now
- **Strongest evidence** — 3-5 source links with one-line context each
- **Personas affected** — tags from {CISO, CTO, VP-Eng, VP-Security, Head-of-ProdSec}
- **Conversational hook** — one suggested phrasing for how Rysy might mention this in an email when the prospect's context fits

## Phase 5 — Write and archive

- Move existing `craft/trends/current.md` to `craft/trends/archive/{old-timestamp}.md`
- Write new `craft/trends/current.md` per the schema in `references/output-format.md`
- Write run report to `craft/trends/runs/{timestamp}.md` with full audit (which topics dropped, why)
- Update `craft/INDEX.md` last-trends-refresh date

## Anti-patterns

- Reporting topics with only one source (single-source = noise by default)
- Including vendor announcements as if they were industry trends
- Writing trend summaries from search engine snippets without reading the underlying material
- Failing to log dropped candidates (the audit is what makes the skill defensible)
- Refreshing on a calendar regardless of real change — better to skip a refresh than to write one from no real change
