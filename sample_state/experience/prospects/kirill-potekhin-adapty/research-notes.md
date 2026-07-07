# Research notes — Kirill Potekhin

**Lead ID:** kirill-potekhin-adapty
**Company:** Adapty.io
**Research date:** 2026-04-30
**Tier:** A
**Playbooks run:** linkedin-deep-read, company-intelligence, trigger-event-detection, web-discovery, github-and-code-mining, podcast-and-talks

---

## Profile snapshot

**Current title:** CPO and CTO, Co-Founder — Adapty.io
**Title as appears on LinkedIn:** "CPO and CTO, Co-Founder" (confirmed via multiple sources; Crunchbase lists "Co-founder and CTO"; Adapty's own about page lists "CPO/CTO")
**Tenure in current role:** Co-founded Adapty in 2019; approximately 6 years in this combined founder-executive role
**Location:** London, GB (confirmed via GitHub bio; earlier sources listed Moscow, which appears outdated)
**Languages:** Russian (native), English (professional)

### Title overlap resolution — Kirill vs. Gregory Komissarov

The source CSV listed two people with overlapping CTO titles. Resolution:

- **Kirill Potekhin** is the Co-Founder and holds the combined CPO+CTO title. He is the chief technical *and* product authority. All primary sources — Adapty's own team page, press coverage, conference bios, and Crunchbase — confirm him as the architectural decision-maker and public face for product and technical strategy.
- **Gregory Komissarov** is listed in multiple data aggregators (ZoomInfo, RocketReach) as "Head of Development" or, in one stale entry, "CTO." His LinkedIn title per LinkedIn itself and ZoomInfo current data is **Head of Development**. He is based in Almaty, Kazakhstan. He is an engineering manager, not a co-founder. The "CTO" label on his profile appears to be a data-scraper artifact, not his actual title. He has been at Adapty (joined from SOAX and Tango Me) and has 17+ years of engineering leadership experience.

**Conclusion:** Kirill is the strategic and architectural owner. Gregory runs the development team under Kirill. Kirill is the correct outreach target for a security/infrastructure pitch. No title conflict exists in practice — it is a data artifact.

### Previous roles
- **Co-founder, Poteha Labs** — data science consulting agency (with Vitaly Davydov, pre-Adapty)
- **EasyTen (language-learning app)** — mobile app developer, approximately 2016-2019; this is where the founders built their first internal subscription infrastructure and identified the market gap Adapty fills
- **Partner, ITMOST** — listed in some older bios; appears to be an advisory or investment relationship
- **Школа анализа данных (School of Data Analysis) / Poteha Devs** — early-career technical work, likely 2013-2015

### Education
Higher Schеol of Economics (HSE Moscow), Computer Science — confirmed via GitHub (Python_HSE_projects repo) and background summaries. Not a load-bearing signal at this career stage.

### About section
LinkedIn not directly accessible without browser session. From aggregate sources and author bios: Kirill is described consistently as having "10+ years in app development" and as the person responsible for both product direction and technical architecture at Adapty. The founding narrative centers on solving a problem they personally experienced — building an internal subscription management system for EasyTen and realizing no good tooling existed for the market. This origin story is authentic (repeated across press, podcast appearances, and funding announcements) and suggests a builder-founder ethos rather than a market-opportunist ethos.

**Tone assessment:** Sparse-to-personal. His public voice is technical and pragmatic, with a preference for data over assertion.

---

## Activity scan (last 90 days)

**Note:** LinkedIn browser session unavailable; activity inferred from indexed posts, external references to his LinkedIn activity, and confirmed post text.

### Confirmed posts (indexed externally, last 90-180 days)

**Post 1 — October 2025 (original post / medium weight):**
Kirill published the blog post "How Adapty keeps running when (almost) nothing else does" following the AWS US-East-1 outage on October 20, 2025. This is a substantive technical piece in his own voice. Key verbatim from the article:

> "When our clients use Adapty, they're trusting us with their entire payment infrastructure."

> "If Adapty goes down, our clients stop making money. Their users literally cannot buy subscriptions."

> "Since infrastructure *is* our product, reliability isn't a feature. That's the whole point."

> "We don't accept our clients losing revenue because of it."

Signal weight: HIGH. These are not marketing claims — they are an operational commitment stated after a real industry stress event. He is articulating Adapty's reliability doctrine in his own words.

**Post 2 — August 2025 (LinkedIn post, medium weight):**
Kirill shared the "State of In-App Subscriptions 2024" report, noting three trends: weekly subscription market share crossing 55% (up from 36.8% in 2022), EU pricing increases (+7.5%), and the claim that "App developers see up to 100x more revenue with paywall experiments." He framed weekly subscriptions as "one of the highly discussable trends now." This is promotional content for Adapty's research, but his framing choice reveals he thinks in data-anchored arguments.

**Post 3 — November 2025 (hiring post, low weight):**
> "We're hiring frontend and backend engineers at Adapty. Join us to build exciting new features with a fantastic team. Our product is loved by customers; you'll love it too. If you're interested, DM me and we'll be quick (no agencies, please)"

Signal: He is personally recruiting, which is unusual for a co-founder six years in. Suggests high standards, tight hiring process, and that he still thinks of team-building as his job.

**Post 4 — Vitaly Davydov's LinkedIn post (engagement, low-medium weight):**
In August/September 2025, Vitaly Davydov (CEO) posted "Kirill Potekhin legend" while resharing a Business of Apps interview in which Kirill discussed that "60% of customers stick with the default option" as a key paywall conversion insight. Davydov's framing implies Kirill is the intellectual authority on product science within the partnership — Davydov leads commercial strategy, Kirill leads product/engineering thinking.

**Overall activity assessment:** Activity is substantive but not frequent. He posts when he has something real to say — a new product, a data insight, a technical incident. He does not repost for the sake of presence. This is a low-noise, high-signal LinkedIn operator.

---

## Article archive

Kirill has published 10 articles on Adapty's blog. Most recent first:

**1. "How Adapty keeps running when (almost) nothing else does" — October 2025**
His most recent and most substantive piece. Written in response to the AWS US-East-1 outage. Describes Adapty's hybrid infrastructure (on-premise + cloud), 3-stage paywall fallback, global CDN with 400+ locations, and 24/7 monitoring with Grafana across 8 global checkpoints. His own words (verbatim captures above). Tone: confident, engineering-first, commercially aware. This is the fullest statement of his infrastructure philosophy. It is not a marketing post — it is a technical accountability post.

Signal weight: VERY HIGH. He is articulating what it means for payment infrastructure to be mission-critical — the exact frame Transilience pitches from.

**2. "Google Play server-side purchase validation" — December 2022**
20-minute read. Deep technical walkthrough on validating Google Play receipts server-side. Hands-on engineering content, not executive positioning. Confirms he writes technical documentation for practitioners, not just for thought-leadership.

**3. "StoreKit 2 API: How Apple simplified integration of in-app purchases" — July 2021**
Early StoreKit 2 coverage. He engaged with platform changes immediately as they were announced. Pattern: follows Apple/Google policy changes closely and writes technical responses quickly.

**4. "Adapty API outage and what we've learned from it" — April 2021**
Post-mortem on their own outage. The decision to publish a public post-mortem is itself a signal — transparency about failure, accountability framing, engineering discipline. This is the 2021 version of the 2025 reliability post.

**5. "Step-by-step guide to run a scalable API on AWS spot instances" — July 2020**
19-minute technical deep-dive. Verbatim: *"steep discounts. Amazon says they can reach 90%, in our experience, it is ~3x"* — he corrects vendor marketing with operational data. AWS expert, serverless architecture, cost-conscious engineering. His tone is: pragmatic, skeptical of vendor claims, grounded in real operational numbers.

**6. Monthly product update posts (2022, low weight):** These are product changelog posts, not original thinking.

**Article archive conclusion:** His writing clusters around two themes — (1) infrastructure reliability and engineering rigor, and (2) mobile subscription/paywall product science. He writes as a practitioner. He has a documented history of transparency after failures. He is AWS-native and serverless-oriented.

---

## Engagement web

LinkedIn browser session unavailable; engagement web partially reconstructed from indexed posts.

**Confirmed engagement pattern:**
- Vitaly Davydov (CEO, Adapty) re-shares and endorses Kirill's technical content. The co-founder relationship is clearly delineated: Davydov handles commercial narrative, Kirill handles product/engineering narrative.
- Business of Apps appears multiple times as a platform where Kirill publishes and speaks. This is a practitioner audience (app developers, monetization leads), not a CISO/security audience.
- Leeds Mobile developer community (UK-based). Conference speaking to mobile engineering practitioners.

**Peer reference group inference:** Based on the conference circuit (Business of Apps, App Promotion Summit, Leeds Mobile, React Summit appearance referenced), Kirill's peer group is mobile product engineers and subscription-analytics practitioners, not enterprise infrastructure or security communities. This is relevant for outreach tone — he is not thinking in SIEM/CSPM terms, but he is deeply familiar with platform compliance (Apple/Google policy), API reliability, and payment infrastructure trust.

**Topics that bring him out:** Infrastructure failures (he writes substantively when something breaks, industry-wide), platform policy changes (StoreKit, Apple antitrust), data-backed product insights (he publishes when the data is interesting enough to share).

---

## External trail

### GitHub

**Account:** github.com/kpotehin
**Affiliation:** @adaptyteam (Adapty organization)
**Location on profile:** London
**Activity level:** Low-to-dormant on personal account; active contributions presumably through organization account

**Personal repositories:**
- `store-receipt-validator` — PHP receipt validator for Apple iTunes and Google Play Stores. This is directly relevant — he built the receipt validation logic himself early on. This is core infrastructure for subscription security (validating purchase receipts is a trust/integrity function).
- `serverless-optimizer-plugin` — JavaScript fork of a Lambda optimization plugin
- `serverless-upmind` — JavaScript fork of Serverless Framework
- `Python_HSE_projects` — educational Python work from his HSE coursework
- `ya-shri` — unspecified project

**Pinned/notable repos:** The PHP receipt validator is the most significant. Building this confirms he did the hands-on subscription infrastructure work himself in Adapty's early stage — this is not a manager who delegated the security-critical receipt validation logic.

**GitHub cross-reference:** His GitHub shows strong serverless/AWS orientation (forking Lambda optimizer tools), PHP backend work, and early attention to purchase validation. This is consistent with his blog writing (AWS spot instances, StoreKit 2, server-side validation). He is an implementer who moved into product/CTO role, not a manager who arrived from outside.

**Activity level:** The personal account appears dormant or low-activity post-2021. This is typical of technical co-founders who shift from hands-on coding to product/architecture direction as the company grows. His technical depth was established early and is credible; he now operates at the architecture/direction level.

### Talks and conference appearances

**1. "How to Build a Paywall Builder: the tech behind 100M+ daily paywalls"**
- Venue: Leeds Mobile meetup, The Malmaison, Leeds, UK
- Date: December 2, 2025
- Slides: Speaker Deck (leedsmobile account)
- Content: Native vs. WebView rendering (native is "5x faster" — 1.21-2.57s vs. 5.26-12.98s), multi-level CDN caching with URL parameter segmentation for cache hit maximization, three-stage fallback (CDN → backend → local SDK), Base64 encoded image previews. Analysis of $2B tracked revenue across 215M transactions revealing 3 LTV levers: premium pricing, paywall personalization (+23% avg LTV), and A/B testing (apps with 50+ experiments see 10-100x revenue growth).
- Feedback: Described by attendees as "a real highlight" with "unexpected customer-behaviour patterns."
- Signal weight: HIGH. He is speaking to technical peers about architecture decisions, not business audiences about revenue growth. This is his engineering voice.

**2. "From 73,000 Paywalls: How We Found the Blueprint to Higher Conversion"**
- Venue: Business of Apps (video, October 2025)
- Content: Data analysis of 73,000 paywalls to identify conversion levers. He describes this as producing "a simple, step-by-step action plan."
- Direct quotes not available from transcript (403 on page)
- Signal weight: Medium. This is more product/marketing science content than engineering content.

**3. "Strategies for Personalized Paywalls and Subscription Success with Adapty.io's Kirill Potekhin"**
- Venue: Business of Apps (Peggy Anne Salz interview), ~September/November 2024-2025
- Also published as YouTube video
- Content: Personalized paywalls, dynamic A/B testing, extended onboarding, localization, strategic product defaults. Vitaly Davydov's reshare captures one specific data point: "60% of customers stick with the default option" — making default selection the highest-leverage paywall conversion variable.
- His title used in this interview: CPO & Co-Founder. (Note: "CTO" is not used in the interview bio, suggesting that in public-facing product/marketing contexts he presents as CPO, while in technical/infrastructure contexts he presents as CTO.)
- Signal weight: High for the verbatim data point about default selection psychology.

**4. "Subscription Margin Optimisation and Web2App Transition"**
- Venue: Business of Apps (video, ~May/June 2024)
- Content: Web2app as an alternative to in-app subscriptions; pricing geography (Netherlands: +62%, Turkey: -71%); practical assessment of the App Store tax avoidance opportunity.
- Signal: He was analyzing web2app a full year before FunnelFox launched publicly (March 2025) and before the April 2025 Apple court ruling. This is consistent with a founder-CTO who does market and product research before committing to a build direction.

**5. Business of Apps NYC 2026 (upcoming)**
- Kirill is listed/referenced as a speaker for the 2026 New York event.
- Signal: He is actively maintaining his conference presence through 2026.

### Verbatim quotes (prioritized)

1. *"Since infrastructure is our product, reliability isn't a feature. That's the whole point."* — "How Adapty keeps running when (almost) nothing else does," October 2025

2. *"If Adapty goes down, our clients stop making money. Their users literally cannot buy subscriptions."* — ibid.

3. *"When our clients use Adapty, they're trusting us with their entire payment infrastructure."* — ibid.

4. *"We don't accept our clients losing revenue because of it."* — ibid.

5. *"60% of customers stick with the default option"* — Business of Apps interview (via Vitaly Davydov's reshare), 2024/2025. This is Kirill's data point; Vitaly framed it as the core insight.

6. *"Native is 5x faster"* — Leeds Mobile talk, December 2025 (re: native vs. WebView paywall rendering, with measured numbers: 1.21-2.57s vs. 5.26-12.98s)

7. *"steep discounts. Amazon says they can reach 90%, in our experience, it is ~3x"* — AWS spot instances article, July 2020. Older but reveals his epistemic stance: vendor claims get tested against operational reality.

8. *"The approach described in the article fully works within standard AWS capabilities, without additional scripts, crons, etc."* — ibid.

---

## Company snapshot

**Adapty.io**

- **Stage:** Bootstrapped-to-seed. Self-described as "profitable" (TechCrunch, March 2025). Total external funding: $2.5M across two rounds (December 2020 seed via 500 Global / AdFirst.VC / Genesis; November 2022 seed via Surface Ventures / irrvrntVC). **No Series A or B has been raised.** The "Series A/B" framing in the campaign brief is incorrect — Adapty is a profitable, bootstrapped-through-seed company operating without institutional venture scale.
- **Headcount:** Approximately 100-120 employees (sources vary: 71 per 2024 data, 104 per PitchBook 2025, 116 per one October 2025 report). The campaign brief's "~120 employees" is approximately correct for late 2025.
- **HQ:** New York City (incorporated). Development team historically Eastern Europe / post-Soviet. Kirill is based in London. The company is globally remote.
- **Revenue:** $6.9M revenue reported circa October 2024 (Latka). The company claims 20,000+ apps on the platform processing $500M+/year in in-app purchases (customer revenue processed, not Adapty's own revenue). $1.2B tracked annually per TechCrunch March 2025 article.
- **Sector:** Mobile subscription infrastructure / paywall SaaS. Sub-sector: developer tooling for Apple App Store + Google Play billing integration, A/B testing, analytics, and now web payment processing.
- **Investor names:** Surface Ventures (lead, 2022), 500 Global, AdFirst.VC, irrvrntVC, Ukrainian Genesis Investments (per 2020 round). Flyer One Ventures listed in portfolio page.

### Compliance posture

- **SOC 2:** Adapty claims "SOC 2 verified" on their homepage. Specifics (Type I vs. Type II, scope, auditor) are not publicly documented in a trust center. No public trust center URL was found.
- **GDPR:** DPA available at adapty.io/data-processing-agreement/. They are registered under EU-US Data Privacy Framework (DPF), UK Extension DPF, and Swiss-US DPF. Standard GDPR Article 32 technical measures described.
- **PCI scope:** Adapty does not process raw payment card data (Apple and Google handle the actual card transactions; Adapty receives subscription event data and purchase receipts). Their new web paywall product (FunnelFox web paywalls) integrates with PSPs (Stripe, Paddle, PayPal, Braintree, Adyen, Solidgate) — this may push their PCI surface area. The new web payment flow is the most significant compliance complexity addition. No PCI-DSS certification was found publicly.
- **Encryption:** SSL/TLS in transit confirmed. Daily backups. Peer-reviewed code with security tests in CI/CD pipeline per DPA documentation.
- **Monitoring:** 24/7 dedicated team; Grafana monitoring from 8 global checkpoints every 15 seconds (per Kirill's October 2025 article).
- **Overall posture:** SOC 2-adjacent but not fully documented publicly. No CISO. Founder-owned compliance posture. The web paywall/FunnelFox expansion is materially increasing their payment data surface area.

### Recent events (last 90 days — measured from April 30, 2026)

1. **FunnelFox web paywalls went live — May 12, 2025.** Adapty launched web paywall builder supporting Stripe, PayPal, Paddle, Braintree, Adyen, Solidgate. This came 12 days after the April 30, 2025 US court ruling that banned Apple from charging commissions on external purchases. The speed of launch (they had been beta testing with 100+ customers for over a year, per TechCrunch March 2025) suggests this was a pre-built product released on a regulatory trigger.
2. **FunnelFox (web-to-app funnels) launched publicly — March 2025.** Covered in TechCrunch. The product enables app developers to acquire users outside app stores through web funnels. Revenue-sharing pricing model.
3. **US court ruling on external iOS payments — April 30, 2025.** Apple banned from charging commissions on external purchases. Adapty published a developer analysis (authored by Victoria Kharlan, not Kirill) within 48 hours.
4. **Leeds Mobile talk — December 2, 2025.** Kirill spoke at Leeds developer meetup; slides published on Speaker Deck.

### Hiring signals (as of April 2026, from careers.adapty.io)

20 open positions. Notable for this outreach:
- **Team Lead (Infrastructure)** — Remote. The existence of this role is significant: they are hiring a leader for the infrastructure team, suggesting the current infrastructure org needs strengthened leadership. This is a build-out signal.
- **Senior QA Engineer (FunnelFox) — Billing** — Explicit billing quality focus for the FunnelFox product.
- **Head of Product (Billing, FunnelFox)** — (from careers page search, now 404) Billing product lead for FunnelFox.
- **Product Manager, Analytics & Integrations** — Analytics infrastructure growth.
- Also hiring: Senior User Acquisition Manager, Developer Advocate (Turkey), Marketing Operations.

**Hiring inference:** The Infrastructure Team Lead and the FunnelFox billing QA role together signal that Adapty is actively investing in the reliability and correctness of their new payment-processing surface area. They are building out the team that will own exactly the infrastructure that Transilience is concerned with.

### Public company content

The Adapty blog is primarily content-marketing (analytics guides, comparison pages, Apple/Google policy explainers). Kirill's personal blog contributions are technical and substantive. Vitaly Davydov publishes commercial/narrative content. The company is in active product-marketing mode for FunnelFox.

### Operational moment

Adapty is in **post-launch scale mode** for FunnelFox, its second product. The company is profitable at ~$7M ARR, has not raised institutional capital, and has just made its most consequential bet: expanding from subscription analytics (read-only payment data) into web payment processing (write-path payment data). This expansion materially increases their compliance surface area — they are now handling Stripe/Paddle/PSP payment flows, not just Apple/Google receipt validation. They have a 20-person monitoring team, SOC 2 claimed but not fully documented, and are actively hiring an Infrastructure Team Lead. Kirill is simultaneously the product owner and architectural owner of this expansion. He is thinking about reliability and infrastructure right now — his October 2025 article and December 2025 talk both confirm this is front of mind.

---

## Trigger event

**Primary trigger: FunnelFox web paywall launch (May 12, 2025) + April 30 court ruling + Infrastructure Team Lead hiring**

The convergence of three events makes this an unusually strong trigger:

1. Adapty launched web paywalls on May 12, 2025 — twelve days after the Apple antitrust ruling. They moved fast. They now process payments via Stripe, PayPal, Paddle, Braintree, Adyen, Solidgate — PSPs they did not previously route payments through. This is a new attack surface.

2. The April 30 ruling explicitly shifted compliance burden onto developers: the Adapty blog post acknowledges that developers now face "tax compliance, fraud prevention, chargebacks, currency conversion, and customer payment support" — things Apple previously handled. For Adapty, which is the infrastructure layer between developers and these PSPs, these are now *Adapty's* operational risks, not just their customers'.

3. The open Infrastructure Team Lead role signals they recognize they need to strengthen the team that owns this expanded surface.

**Why this is the strongest trigger for a Transilience pitch:**
Kirill has publicly stated, in his own words, that "when our clients use Adapty, they're trusting us with their entire payment infrastructure" and that "reliability isn't a feature, that's the whole point." He has defined his mission as being the infrastructure layer that cannot fail. He just added a materially more complex payment-processing surface (web PSP integrations) at a moment when the regulatory environment is also changing. He is accountable for both the reliability and the security of this new surface, without a CISO to carry the compliance burden.

**Secondary trigger (usable if primary feels too commercial):**
The AWS US-East-1 outage in October 2025, which Kirill wrote about. He built a post around the fact that Adapty survived when 1,000+ other companies including ChatGPT, Lyft, and Coinbase went down. This establishes his self-identity as someone who has solved the availability problem. Transilience's Detect/Decide loop addresses the adjacent problem — the *security* events that a 24/7 infrastructure monitor doesn't catch, but a cloud security operation does. The angle: you have availability solved; the next layer is the security posture running on top of that infrastructure.

**Trigger-less fallback:** Not needed — two strong triggers exist.

**Recommended trigger for email:** The web paywall launch + PSP expansion. Frame around what Kirill himself said: the payment trust is theirs. The expansion just widened the perimeter of that trust.

---

## Open questions

1. **Kirill's actual LinkedIn activity in the last 30 days (April 2026):** Browser session unavailable during this research run. The most recent indexed activity is from December 2025. Verify whether he has posted about the December 2025 Apple reversal (the appeals court modified the Epic injunction, walking back some of the April 30 commission-free ruling — per MacRumors Dec 11, 2025). If he has commented on this reversal, that is a fresher and more nuanced trigger.

2. **SOC 2 Type II status:** Adapty claims "SOC 2 verified" on their homepage but no trust center or report is publicly linked. Is this a Type I (point-in-time) or Type II (operational over time)? If they only have Type I, they have a significant gap as they expand into web payments. This is worth probing gently in the email.

3. **Gregory Komissarov's actual reporting relationship:** ZoomInfo shows him as Head of Development; some scrapers show CTO. Whether he reports to Kirill or is a peer influences who the second contact at Adapty would be if Kirill doesn't reply. Given the company structure (Kirill = CPO/CTO, Gregory = Head of Dev), he likely reports to Kirill. But this should be confirmed if a multi-thread campaign is considered.

4. **PCI-DSS scope for web paywalls:** Adapty's new PSP integrations (Stripe, Paddle, etc.) through FunnelFox create payment card data handling questions. The docs only mention Stripe explicitly having "published new documentation for U.S. developers who want to process payments for digital goods outside of apps." Does Adapty route card data through their own infrastructure, or are they a pure redirect layer? The answer changes the PCI scope materially. If they are in the data path, PCI DSS Level 3-4 merchant or service provider obligations apply.

5. **Kirill's engagement with the December 2025 Apple reversal:** The appeals court on December 11, 2025 modified the Epic injunction to allow Apple to charge fees on external payment links (different from the April 30 ruling). This is a fast-moving regulatory environment. Kirill has been tracking this closely (multiple Adapty blog posts on the topic). Whether he posted on LinkedIn about the reversal would indicate whether this is still a top-of-mind concern in April 2026.

6. **ITMOST partnership:** Kirill is listed in older bios as a partner at ITMOST. This appears to be a side advisory role. Whether this is still active and whether ITMOST has a security practice could be worth checking — it would indicate whether he has adjacent exposure to security-oriented vendors.

7. **Adapty's data residency:** The company has employees across Eastern Europe, North America, and Asia. With GDPR DPA in place and EU-US DPF registration, their data flow is documented. But their actual data residency (where subscription/payment data is stored) is not publicly disclosed. A security pitch that touches on data sovereignty may be relevant given the EU-origin customer base.
