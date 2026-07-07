# Padlet — campaign company summary

**ICP fit:** A — primary. 78 employees, edtech (K-12 + higher-ed heavy), founder-led (Nitesh Goel since 2008), no CISO. FERPA / COPPA / 50-state student-data-privacy patchwork surface. SOC 2 Type 1 (since Jan 2023, no Type 2). Stack of certifying-body relationships: 1EdTech, Common Sense Privacy Seal, ST4S, EU-U.S. DPF re-cert.

**Live trigger:** Padlet Arcade launched early 2026 at arcade.padlet.com — free public beta AI learning games platform that runs without student login. Existing district DPA library covers padlet.com but does not list Arcade as a covered product. This is the operational gap the four emails approach from four different angles.

## Four routings, four distinct angles, four distinct vocabularies

| Lead | Role | Subject | Angle | Product-sentence verb | CTA opener |
|---|---|---|---|---|---|
| Nitesh Goel | Founder & CEO | Arcade and existing district DPAs | DPA-addendum-by-addendum vs continuous evidence (architectural choice) | "Transilience handles..." | Where |
| Audrey Leong | Operations Lead (Compliance + Support) | When Arcade DPA questions land | Inbound queue / documentation-lag (operational laborer) | "Transilience generates..." | Are |
| Linh Nhat | Engineering Manager | Arcade moderation without accounts | Incident-trace reconstruction without accounts (engineering execution) | "Transilience treats..." | What |
| Collin Palmer | Senior PM (AI/Education) | Arcade safety documentation cadence | Documentation-cadence vs iteration-cadence (product-level) | "Transilience keeps..." | How |

## Witness pass/rewrite history

| Lead | Versions | Final verdict |
|---|---|---|
| Audrey | v1 | ship |
| Nitesh | v1 → v2 → v3 | ship |
| Linh | v1 → v2 | ship |
| Collin | v1 → v2 → v3 | ship |

10 drafts written. 4 shipped. 6 witness-driven rewrites.

## What the witness caught (specific to Padlet)

Round 1:
- "Each new product surface" verbatim in Nitesh + Audrey
- Em-dash binary CTA shape ("[question] — [option A], or [option B]?") in all four drafts
- Wh-cleft "Transilience" pattern in Nitesh and Collin (echo of the Coalesce-mirror habit flagged previously)
- "The gap" as a recurring diagnostic move across three of four drafts

Round 2 introduced new fingerprints during fixes:
- "Right now?" terminal echo in Nitesh and Linh CTAs
- Collin v2 "attestation surface / product surface" abstract parallel — densest line of the set

Round 3 cleared all flags. The full four-draft set ships.

## Lessons reinforced (already in feedback memory from Coalesce)

- Cross-email diff is the doer's job, not the witness sub-agent's. Drafted with cross-draft awareness from the start this round; still got caught by witness on phrase-level echoes ("Each new product surface" verbatim, "right now" terminal echo). Cross-draft awareness is necessary but not sufficient — phrase-level repetition emerges in unexpected places.
- The em-dash binary CTA pattern ("X — A, or B?") is *Vendy's* habit, not the campaign's. Worth watching for.
- "The gap" as an opener phrase is a Vendy habit too. Diagnostic-pattern register tempts it.

## Sequencing guidance

Four contacts at one 78-person company. Recommended cadence: one per 2–3 weeks, in this order:
1. **Nitesh first** — the architectural decision is his to make; the email surfaces a real gap and asks a real question.
2. **Linh second (3 weeks later)** — engineering-execution angle is independent; Linh and Nitesh can both reply without crossing wires.
3. **Collin third (3 weeks later)** — product-level documentation is downstream of the architectural decision; Collin's email lands cleanly after Nitesh has had time to think.
4. **Audrey fourth (3 weeks later)** — the inbound-queue angle is the operational reality if nothing changes; if Nitesh has not engaged after three touches, Audrey's email reframes the trigger as a workload question and may surface internally.

## Artifacts

Per-lead final emails: `experience/prospects/{lead-id}/final.md`
Per-lead deeper artifacts (research, portrait, all drafts): `experience/prospects/{lead-id}/`
Per-lead campaign JSONs (this directory): `{lead-id}.json`
Cross-draft witness review: `_witness-cross-draft-review.md`
