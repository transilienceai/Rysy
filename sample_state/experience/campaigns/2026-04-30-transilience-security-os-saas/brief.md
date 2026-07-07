# Campaign brief — Transilience Security OS / SaaS Cold List

- **Campaign-id**: 2026-04-30-transilience-security-os-saas
- **Date opened**: 2026-04-30
- **Sender**: Transilience
- **Service line**: Transilience Security OS — Full Stack Security OS for the Cloud (Declare → Detect → Decide → Deliver loop; closes the gap between detection and remediation that the point-tool sprawl created)
- **Goal**: Single conversation per shortlisted prospect — book a 15-minute call
- **CTA**: Fifteen minutes, framed as comparing notes / testing a thesis, not a demo

## ICP fit ranking (used to set lead priority)

**A** — primary ICP, 30–150 emp cloud-native handling sensitive data with capacity-constrained security ownership:
Coalesce.io (130), Padlet (78), Adapty.io (120), InEvent (79), Mango Voice (78), Netlify (150–180)

**B** — Series A/B adjacent, 150–400 emp, clear security trigger or under-resourced security function:
beehiiv (240), QA Wolf (270), RevenueWell (180), Route (260), Canopy (300), Karbon (390), NexHealth (230), Replit (340), Domino Data Lab (310)

**C** — out of ICP on size but real security wounds; lower probability but worth a tested email:
Filevine (600), Hugging Face (680), Vercel (880), Blackbaud (2600), Fivetran (1600)

## Routing logic across the 4 picks per company

Where possible, the four picks split across distinct angles so we are not sending four variants of the same pitch into one org:
1. **Primary security buyer** (CISO / Head of Security / Director Security) — operational angle: detection→remediation loop
2. **Technical authority** (CTO / Co-founder) — architecture angle: build-vs-buy honesty about the integration layer
3. **Engineering execution** (VP/Director Engineering / Infra / DevOps) — capacity angle: data-laborer pattern
4. **Compliance / GRC / Operations** (Director Compliance, Head of Ops, BISO) — compliance-as-byproduct angle: live cloud state vs screenshot evidence

When a company lacks one of these, the slot is filled by the next most plausible buyer or influencer. When a company has *no security title at all* (Karbon, Coalesce.io, Padlet — all sub-150 emp), that absence is itself the signal — and the framing for those companies leans into the capacity-gap pitch.

## Value-prop anchors

- **Closes the loop.** LLMs commoditized security knowledge; the unsolved last mile is doing the work continuously, tailored to your environment. Transilience is the substrate that turns knowledge into action.
- **Declare → Detect → Decide → Deliver.** Baseline posture, drift detection, prioritized intelligence, remediation with human-in-the-loop. The full stack, not a tool you bolt onto five others.
- **Compliance is a peripheral, not a deliverable.** SOC 2 / HIPAA / GDPR posture is a property of how the system runs, not a quarterly screenshot drill.
- **Outcome ownership stays with the customer.** Tools, correlation, evidence — Transilience handles. Risk tolerance, business context, accountability — irreducibly the customer's. The closed loop is human + agent, not agent alone.

## Voice constraints (apply universally)

- Dry-precise primary; warm-observational only when the prospect has a public publishing footprint that earns it; diagnostic-pattern when triangulation is honest
- 4–6 sentences body, 30–50 char subject
- No *AI-powered*, no *full-stack* as a slogan, no *seamless*, no *transformative*, no *unleash*, no *empower*, no *game-changing*, no *journey*
- One product-positioning sentence maximum, and only when the inquiry has earned it
- Never: fear-based opener, vendor-consolidation pitch as opener, founder-cosplay, *quick question*, manufactured urgency, first-name padding

## Output structure (per user request)

Per-company folder under this campaign directory containing one JSON per shortlisted lead. Master `output.json` rolls up all results. The per-prospect deeper artifacts (research-notes, portrait, drafts, witness-feedback) live in `experience/prospects/{lead-id}/` per the standard schema.

## Scale note

79 leads across 20 companies. Processed in waves by ICP priority (A → B → C). Each lead receives: a research-summary based on public role/company signal, a witness-reviewed draft, and explicit `ready_to_send` / `human_review_required` flags. Where signal is thin and a credible specific hook can't be earned, the draft is flagged for human review rather than shipped on a generic.
