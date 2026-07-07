# Adapty.io — campaign company summary

**ICP fit:** A — primary. 120 employees, Series A/B, mobile subscription analytics + paywall SaaS for iOS/Android (newly expanding to web via FunnelFox). No CISO. PCI-adjacent surface (subscription event metadata, six PSP integrations as of May 2025). GDPR scope. Apple App Store + Google Play policy compliance.

**Live trigger:** FunnelFox web paywall launched May 12, 2025 — twelve days after the Apple antitrust ruling — integrating six PSPs (Stripe, PayPal, Paddle, Braintree, Adyen, Solidgate). Plus Adapty Mail AI agent + upscale enterprise tier. Three-front expansion adding payment-security and data-handling surface that didn't exist a year ago. Active hiring of Infrastructure Team Lead (April 2025) signals capacity strain.

## Title resolutions (research-driven corrections to source CSV)

- **Kirill Potekhin** — confirmed CPO/CTO Co-Founder.
- **Gregory Komissarov** — Head of Development, NOT CTO. Source CSV had a data-scraper artifact. Important for routing — Gregory leads Engineering operationally under Kirill (CPO/CTO).
- **Vitaly Davydov** — confirmed CEO Co-Founder. LinkedIn URL corrected to https://www.linkedin.com/in/iwitaly/ from Sales Navigator URL.
- **Artem Davydov** — Infra Team Lead and Staff Engineer (per his own GitHub bio; LinkedIn shows stale "Head of Engineering" — that scope is now Gregory's). The active Infra Team Lead hire is EXPANSION, not backfill.

## Vitaly ↔ Artem relationship note

Shared surname + shared pre-Adapty employer (Poteha Labs). Family or close professional connection plausible, unconfirmed. Sequence sends with awareness they may compare notes.

## Four routings, four distinct angles

| Lead | Subject | Angle | Product-verb | CTA opener |
|---|---|---|---|---|
| Kirill (CPO/CTO Co-Founder) | Reliability of the PSP control plane | Infrastructure-as-product extended to control-plane state | "Transilience extends..." | What |
| Gregory (Head of Development) | PSP credential state on self-hosted k8s | Build-vs-buy honesty: oack covers HTTP layer; Transilience covers secret-scoping-and-rotation | "Transilience does that part..." | How |
| Vitaly (CEO Co-Founder) | 4th variable beyond price/convert/change | Commercial trust gap / deal-cycle (4th variable beyond his foreword's three) | "With Transilience handling..." (preposition-fronted) | Where |
| Artem (Infra Team Lead) | Reconciliation between IaC and cluster state | Operational drift between IaC declared and effective cluster state, post-FunnelFox | "Transilience reconciles..." | Has |

## Witness pass/rewrite history

| Lead | Versions | Final verdict |
|---|---|---|
| Artem | v1 | ship |
| Kirill | v1 → v2 | ship |
| Gregory | v1 → v2 | ship |
| Vitaly | v1 → v2 | ship |

7 drafts written. 4 shipped. 3 witness-driven rewrites — all cross-draft cleanup (the v1s were individually clean but had cross-draft phrase repetition).

## Cross-draft fingerprints caught

Round 1:
- "Twelve days" appeared in 3/4 Adapty drafts (factual anchor used identically) — flagged as detectable; reduced to 2/4 in v2.
- "Continuously" / "continuous" appeared in 4/4 — flagged; varied in two drafts (Kirill: dropped entirely; Gregory: "baselined live"). Now 2/4.
- Vitaly's sentence 2 declared his deal-cycle problem as fact — reshaped to conditional probe ("If those questions are slowing the cycle...") in v2.
- "At enterprise altitude" was decorative — dropped in v2.

Round 2:
- "Is the kind of" opener in Kirill + Gregory (2/4) — flagged as residual seam, non-blocking, would only surface in deliberate side-by-side comparison.

## Lessons reinforced (cross-campaign feedback memory already captured)

The most important lesson surfaced again here: **cross-email diff is the doer's job, not the witness sub-agent's.** Drafted with cross-draft awareness from the start (per Coalesce/Padlet learning), and still got caught on phrase-level echoes the witness flagged. Cross-draft awareness is necessary but not sufficient — phrase-level repetition emerges in unexpected places (factual anchors, frequency adverbs, opener cadence) that only a side-by-side comparison surfaces.

## Sequencing guidance

Four contacts at one 120-person founder-led co with possible Davydov family connection. Recommended cadence: one per 2–3 weeks, in this order:

1. **Artem first** — operational angle is the most immediate / least strategic; lowest risk if it doesn't land
2. **Gregory second (3 weeks later)** — engineering execution layer, separate from architectural conversation
3. **Kirill third (3 weeks later)** — the architectural conversation lands cleanly after the operational pattern has surfaced
4. **Vitaly last (3 weeks later)** — commercial trust gap is the highest-strategic angle; lands best after the technical conversation has had time to accumulate

If any sub-cycle of this order produces a positive reply, halt the rest and let the conversation expand from the reply rather than continuing to push outbound into the same org.

## Artifacts

Per-lead final emails: `experience/prospects/{lead-id}/final.md`
Per-lead deeper artifacts (research, portrait, drafts): `experience/prospects/{lead-id}/`
Per-lead campaign JSONs (this directory): `{lead-id}.json`
Cross-draft witness review: `_witness-cross-draft-review.md`
