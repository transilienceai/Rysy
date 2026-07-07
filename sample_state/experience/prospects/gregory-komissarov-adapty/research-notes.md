# Research notes — Gregory Komissarov

**Lead ID:** gregory-komissarov-adapty
**Company:** Adapty.io
**Research date:** 2026-04-30
**Tier:** A
**Playbooks run:** linkedin-deep-read, company-intelligence (cross-ref kirill-potekhin-adapty), trigger-event-detection, web-discovery, github-and-code-mining, podcast-and-talks

---

## Profile snapshot

**Current title:** Head of Development — Adapty.io
**Title resolution:** "CTO" label on some aggregator sources (ZoomInfo stale entry) is a data-scraper artifact. LinkedIn itself and current ZoomInfo confirm "Head of Development." The actual CTO is Kirill Potekhin (CPO/CTO, Co-Founder). Gregory is the engineering execution owner under Kirill. No title conflict; confirmed in kirill-potekhin-adapty research notes.
**Tenure at Adapty:** Joined post-SOAX; aggregator data places arrival circa 2023. Exact start month not confirmed. As of April 2026, approximately 2-3 years at Adapty.
**Location:** Almaty, Kazakhstan (confirmed via LinkedIn and ZoomInfo; GitHub bio previously listed Saint-Petersburg — city may have changed during career transitions)
**Languages:** Russian (native/bilingual), English (full professional)
**LinkedIn connections:** 500+ connections; ~1,000 followers

### Career progression (reconstructed from aggregator cross-reference)

Approximate timeline, most recent first:

1. **Head of Development, Adapty.io** — ~2023–present (~2–3 years)
   Engineering execution lead for Adapty's development team. Scope: backend Python, frontend React, DevOps/self-hosted Kubernetes for SaaS products.

2. **VP Supply + CTO, SOAX** — ~2022–2023 (~1 year)
   Proxy infrastructure company. Launched a new data collection product ("a small team of three professionals" per his own LinkedIn post). Dual-hatted VP Supply + CTO role. SOAX grew 64% in 2023 during his tenure. He personally posted a hiring announcement for the data collection product — indicating he was still hands-on recruiting at VP/CTO level.

3. **VP Infrastructure, Tango Me** — ~2021–2022 (~1 year)
   Video calling app (not Tango.ai — the social video platform). VP-level infrastructure ownership.

4. **Head of Infrastructure, Wrike** — dates unknown, estimated ~2017–2021 (pre-Tango)
   Led and motivated a team of **70+ employees** across data engineering, SysOps, DevOps, and Global Office IT. Oversaw product migration to Kubernetes and data engineering migration to a public cloud provider. Established the DevOps department. This is the largest team he has led — 70 people across multiple infrastructure functions.

5. **Performance Testing Engineer, Yandex** — pre-Wrike, estimated ~2013–2016
   Identified bottlenecks in services. Built tools for load testing using Python, Linux, and web technologies. Delivered quality monitoring metrics. Built firebat — a console load-testing tool integrated with the Yandex Tank / Phantom ecosystem (27 stars on GitHub). Spoke at EPAM IT Meetup on April 4, 2015, presenting Yandex Tank.

6. **Team Leader, Operations & Load Testing, Novardis** — pre-Yandex
7. **Build System Administrator & Deployment Engineer & Tester, CSBI Group** — early career

**Education:** Bonch-Bruevich State University of Telecommunications, Saint Petersburg, 2004–2009. Engineer's degree, multichannel telecommunication systems. Started working as an engineer from his second year of study.

**Certifications (LinkedIn-listed, from Coursera):**
- Programming with Google Go Specialization — January 2021 (signal: actively learning Go while at Wrike/Tango-era transition)
- Write Professional Emails in English — June 2019
- Strategic Planning and Execution — May 2019

**About section (truncated on public profile):** "With progressively responsible experience in technical leadership and management roles…"

**Tone assessment:** Sparse public presence on LinkedIn. Posts infrequently, and only when hiring or announcing something operational. Not a thought-leadership poster. His public voice is found more in GitHub artifacts, his personal monitoring project, and the 2015 conference talk than in LinkedIn content.

---

## Activity scan (last 90 days)

**Note:** LinkedIn browser session not available. Activity reconstructed from indexed posts and aggregator data. LinkedIn activity is sparse — two public posts found in the entire accessible record, both hiring-focused.

### Confirmed posts

**Post 1 — approximately April 2025 (hiring post, medium weight):**
Verbatim: *"If you are looking for a fully remote job 🌎 in an international product company and enjoy doing Backend/Python, Frontend/React, DevOps/self-hosted k8s for SaaS products, please let me know! 💪 Strong and involved colleagues, high pace, minimum bureaucracy! All our positions are listed here:"* [link to adapty.io/careers]

Signal weight: MEDIUM. This is the hiring post indexed as "1 year ago" (approximately April 2025). The tech stack he calls out — Backend/Python, Frontend/React, DevOps/self-hosted k8s — is Gregory's own vocabulary for what his team builds. "Self-hosted k8s" is a deliberate choice: Adapty runs its own Kubernetes rather than delegating to managed cloud K8s (EKS/GKE). This is an infrastructure philosophy signal — he favors operational control over vendor convenience, consistent with his Wrike background where he ran a 70-person infra org.

"High pace, minimum bureaucracy" — this is his characterization of working at Adapty. Whether it reflects satisfaction or the strain of post-launch scale is an open question.

**Post 2 — approximately January 2023 (SOAX hiring post, context only):**
*"Hi folks! I'm glad to announce that we(SOAX) are kick-starting work on a new product in the data collection market. It would be a small team of three professionals."*

Signal weight: LOW for current outreach (3+ years old). But reveals: at SOAX he was running a startup-within-a-startup. At CTO level he was still personally posting to recruit three engineers. Consistent with a hands-on manager who stays close to the team, not a delegating executive.

**Overall activity assessment:** Gregory is a sparse LinkedIn operator. Two public posts in at least 3 years. He does not use LinkedIn for thought leadership, opinion, or technical narrative. His public voice is almost entirely operational — hiring or announcing. **This shifts research weight significantly toward his external trail (oack.io, GitHub) and toward company-level inference.**

---

## Article archive

**No articles found on LinkedIn.** Gregory has not published longform content on LinkedIn.

**No Habr (Хабр) presence found.** Despite his Saint-Petersburg/Russian engineering background and the site being a natural outlet for post-Soviet technical leaders, no articles by Gregory Komissarov were found on habrahabr.ru / habr.com. His Yandex-era peers often published there; his absence may indicate a preference for shipping over writing, or a language/audience shift as he moved to international companies.

**GitHub as the primary written record:** His open-source output from the Yandex era is the closest thing to a public technical voice. See External trail > GitHub.

---

## Engagement web

**Cannot be reconstructed from public data.** LinkedIn activity is too sparse to map an engagement web. No substantive comments on peers' posts were found. No repeated engagement patterns visible.

**Inference from network shape:** His 500+ connections and ~1,000 followers at the Head of Development level is modest. He is not building a public persona. His peer reference group is not inferable from LinkedIn engagement.

**What the sparse engagement web tells us:** Gregory is an operator, not a broadcaster. The email cannot open with "I saw your recent post on X" because there are no recent posts with substance. The warm-observational register must be anchored in his external trail — specifically oack.io — rather than LinkedIn activity.

---

## External trail

### GitHub — github.com/greggyNapalm

**Account metrics:** 26 repositories, 29 followers, 27 following, 409 starred repos
**Languages:** Python, Go, Vim Script
**Activity level:** Personal account appears low-to-dormant post-2021 (consistent with senior ICs who move into management and contribute via organizational accounts rather than personal accounts)

**Pinned / notable repositories:**

1. **firebat-console** (Python, 27 stars) — "Console helper for Phantom load tool." A load testing management CLI that integrates with Phantom (the C++ IO engine behind Yandex Tank). 138 commits; published to PyPI. This is the most substantive artifact of his engineering voice — he was not just a user of load testing tools, he built tooling for load testing tooling. Signal: systems-level engineering orientation, Python as primary tool, attention to developer experience (building the console layer on top of a complex underlying engine).

2. **proxychick** (Go, 11 stars) — Proxy checking tool. Written in Go (consistent with his 2021 Go Specialization cert). Connects to his SOAX work (proxy infrastructure). The Go cert + a Go repo is a credible upskill signal.

3. **ammo** (Python, 5 stars) — "Generators for input data for load testing." Another Yandex Tank ecosystem tool.

4. **phantom_doc** — Documentation for Phantom load tool. He was not just a contributor; he wrote the docs.

5. **shell-tools** (Vim Script) — Personal Unix/Vim environment configuration. A signal of a developer who has strong opinions about their tooling setup.

**GitHub cross-reference:** The Yandex-era tools (firebat, ammo, phantom_doc) show an engineer who builds tools for other engineers — metacognitive about the tooling layer, not just the product layer. This is the same instinct that produced oack.io. His GitHub has been quiet since ~2021, which is expected for someone who moved into Head of Infrastructure at Wrike (where he would contribute through organizational accounts) and then into management at Tango, SOAX, and Adapty. The technical depth is established and credible; he now operates at the architectural/people-management layer.

**Website linked from GitHub:** https://oack.io — his personal monitoring/incident-response SaaS (see below).

### oack.io — Personal SaaS project

**What it is:** Oack is a monitoring, incidents, and status pages platform that Gregory built as a side project and now runs commercially. Pricing: Free tier, Pro ($14/mo), Business ($69/mo), Enterprise (custom). Product is actively being developed — changelog shows active feature shipping through April 2026 (just 3 weeks ago).

**His own words on why he built it (verbatim from oack.io/about):**

> *"For over 10 years I've relied on web monitoring services to keep production systems healthy."*

> *"I've used just about every tool out there, from the big enterprise platforms to scrappy open-source setups, and each time I ran into the same gaps: missing features, clunky workflows, or telemetry that stopped at the HTTP layer."*

> *"I wanted deep TCP-level telemetry, instant multi-channel alerting, and an incident workflow that didn't fight me at 3 AM."*

> *"Oack started as a side project to scratch my own itch."*

> *"Over time it grew into a full platform that I now use to monitor my own infrastructure every day."*

> *"I built Oack for engineers and entrepreneurs who are building their businesses and need monitoring they can trust without spending hours configuring it."*

> *"If you've ever wished your monitoring tool just worked the way you expected, that's exactly what I'm aiming for."*

**Signal weight: VERY HIGH.** These are the clearest statements of Gregory's engineering philosophy in his own voice found anywhere on the web. Key themes:

- *Frustration with complexity and clunky workflows* — "enterprise platforms" with "clunky workflows" is how he frames bad tooling. He is biased toward clean, purposeful interfaces over feature-bloat.
- *Depth over surface monitoring* — he specifically calls out "telemetry that stopped at the HTTP layer" as the gap. He wanted TCP-level telemetry. This is an engineer who thinks about the stack below the obvious layer.
- *3 AM as the test case* — "an incident workflow that didn't fight me at 3 AM" is an operationally honest framing. He thinks about systems from the perspective of the on-call engineer at the worst moment, not the demo environment.
- *Builder instinct even at executive level* — he is running a full commercial SaaS as a side project while working as Head of Development at Adapty. He did not stop building when he became a manager. This is the same pattern as his Yandex-era open-source work.

**Recent oack.io changelog (last 4 weeks as of April 30, 2026):**
- MCP server with 53 read-only tools
- PagerDuty sync and external alert ingestion
- Postmortem editor with AI analysis
- On-call schedules with rotation shifts and escalation policies
- Cloudflare log enrichment integration
- Interactive checker world map with geolocation

The MCP server with 53 tools is a notable signal — he has integrated oack.io into the AI coding assistant ecosystem (Claude, Copilot, Cursor can query oack.io via MCP). He is tracking AI tooling trends and building for the developer workflow. This is recent (within the last 30 days).

### 2015 EPAM IT Meetup presentation

**Title:** "Yandex tank: примеры и нюансы использования" (Yandex Tank: Examples and Usage Nuances)
**Venue:** EPAM IT Meetup, Saint Petersburg, April 4, 2015
**Format:** Technical talk (Google Slides, publicly accessible)
**Content:** Yandex Tank load testing internals — Phantom's C++ IO engine, async non-blocking sockets, stateless protocol limitation, data format specifications.

Signal weight: LOW for current trigger (11 years old). High for character understanding — this is his earliest public technical voice, and it is consistent with every subsequent artifact: he goes deep into the machinery, documents what he finds, and builds tools for other engineers.

**No more recent conference talks found.** Unlike Kirill (who speaks at mobile dev conferences), Gregory has no public talks post-2015. He is not a conference circuit engineer. His public voice is GitHub and oack.io.

### Verbatim quotes (prioritized by signal weight and recency)

1. *"I wanted deep TCP-level telemetry, instant multi-channel alerting, and an incident workflow that didn't fight me at 3 AM."* — oack.io/about (undated, current/live)

2. *"Oack started as a side project to scratch my own itch."* — oack.io/about

3. *"I've used just about every tool out there, from the big enterprise platforms to scrappy open-source setups, and each time I ran into the same gaps: missing features, clunky workflows, or telemetry that stopped at the HTTP layer."* — oack.io/about

4. *"Over time it grew into a full platform that I now use to monitor my own infrastructure every day."* — oack.io/about

5. *"I built Oack for engineers and entrepreneurs who are building their businesses and need monitoring they can trust without spending hours configuring it."* — oack.io/about

6. *"If you are looking for a fully remote job 🌎 in an international product company and enjoy doing Backend/Python, Frontend/React, DevOps/self-hosted k8s for SaaS products, please let me know! 💪 Strong and involved colleagues, high pace, minimum bureaucracy!"* — LinkedIn post, ~April 2025

7. *"Hi folks! I'm glad to announce that we(SOAX) are kick-starting work on a new product in the data collection market. It would be a small team of three professionals."* — LinkedIn post, ~January 2023 (SOAX era, included for character reference)

---

## Company snapshot (cross-reference)

Full company context documented in `experience/prospects/kirill-potekhin-adapty/research-notes.md`. Summarized here for Gregory's operational context:

- **Stage:** Profitable, bootstrapped-through-seed (~$7M ARR per 2024 data). No Series A/B. The "Series A/B" framing in the campaign brief is incorrect.
- **Headcount:** Careers page now describes "200+ talented people" — up from ~120 in late 2025. The company is growing.
- **Gregory's team scope (inferred):** The April 2025 hiring post cites Backend/Python, Frontend/React, DevOps/self-hosted k8s as his team's domain. The careers page (April 2026) shows open roles for Engineering Team Lead (Product), Team Lead (Infrastructure), Backend Developer (Python), and Senior QA Engineer (FunnelFox, Billing). These are roles within or adjacent to his org. Estimated team size: 30-50 engineers across backend, frontend, mobile, devops. The infrastructure function (Artem Davydov as Infra Team Lead) appears to be a sub-team within Gregory's broader development org.
- **Operational moment:** Post-launch scale mode for FunnelFox / web paywalls. The company shipped web payment processing (Stripe, Paddle, PayPal, Braintree, Adyen, Solidgate) in May 2025 — 12 days after the Apple court ruling. Gregory's team built and maintains this. They are now actively hiring an Infrastructure Team Lead and an Engineering Team Lead (Product), suggesting the current structure is feeling the strain of scale.
- **Key engineering challenge right now (inferred from hiring + changelog):** The team is scaling across SDK surface area (Capacitor, KMP, React Native, Flutter, iOS, Android, web), a new payment-processing product (FunnelFox), and an AI-augmented product roadmap (Autopilot, CLI). Gregory is running a bigger, more complex team than he had 18 months ago.

---

## Trigger event

**Primary trigger: The May 2025 web paywall launch — his team's delivery, his operational problem to own**

The FunnelFox web paywall launch (May 12, 2025) was the most consequential engineering execution event at Adapty in the past year. Six PSPs integrated. Shipped 12 days after the Apple court ruling. The Kirill research notes established this as a pre-built product held in beta and released on a regulatory trigger — meaning the engineering work happened *before* May 12. Gregory's team did the build.

The operational consequence for Gregory is distinct from the consequence for Kirill:
- Kirill's frame: *this expanded our product surface area and our infrastructure trust commitment*
- Gregory's frame: *this expanded what my team has to keep running, keep secure, and keep scaling*

His oack.io About page says it explicitly: he built his monitoring tool because enterprise tools had "clunky workflows" and "telemetry that stopped at the HTTP layer." He thinks about the stack below the obvious layer. Adapty just added six PSP integrations on top of a payment-processing flow that, prior to May 2025, did not exist in their stack. Gregory is now responsible for an engineering surface area that has materially widened in 12 months.

**Secondary trigger: Active hiring strain signals his team is undersized for current scope**

Two engineering leadership roles are simultaneously open (Engineering Team Lead Product, Team Lead Infrastructure). This is unusual — hiring two leads at once suggests the current structure is stretched. Gregory is operating a growing team that is hiring mid-management, which is a classic "growing faster than the org chart can support" signal.

**Tertiary trigger: oack.io as a mirror signal**

He built oack.io because existing monitoring tools failed him "at 3 AM." He is personally aware of monitoring/observability gaps at the enterprise end. The most recent oack.io changelog shows active MCP integration (last 3 weeks). He is not intellectually dormant — he is building in his discretionary time. An outreach that speaks to his tool-building instinct and his specific frustration with "telemetry that stopped at the HTTP layer" will land differently than generic security/ops outreach.

**Strongest trigger for email:** The web paywall expansion as Gregory's engineering execution responsibility — framed through his own language about "telemetry" and "incident workflows" — not through the business/product framing Kirill would receive.

---

## Disqualify check

**Result: CLEAR — no disqualify signals found.**

- No layoff or "Open to Work" signal found on LinkedIn or any aggregator
- No personal crisis, grief, or health issue signals found in any public content
- Active hiring (Gregory posted ~April 2025 and Adapty's careers page is active) — he is expanding the team, not contracting
- No sabbatical or PTO signals
- No anti-inbound signals (no "not taking outreach" statements found)
- Adapty company: no layoffs found in any tracker; careers page lists 20 open roles

---

## Open questions

1. **Exact Adapty start date:** Aggregators place Gregory's arrival at Adapty as post-SOAX (2023), but the precise month and whether he joined before or after the FunnelFox web paywall build began is unconfirmed. If he joined in late 2023 or early 2024, he owned the FunnelFox engineering execution from early in the project. If earlier, even more so. Confirm via LinkedIn if browser session becomes available.

2. **Relationship to Kirill — direct report or peer?** All available data indicates Gregory reports to Kirill (Kirill is CPO/CTO co-founder; Gregory is Head of Development). However, at a company with 200+ employees that has never had a formal CTO-minus-Gregory structure, the operational reality may be more collegial. Worth observing whether Gregory uses Kirill's blog posts/framing in his own communications — it would indicate intellectual alignment or distance.

3. **oack.io as commercial reality or side experiment:** The pricing page and active changelog suggest oack.io is a real commercial product, not just a weekend project. But is Gregory actively marketing it, or is it running quietly? The "Founding member" pricing (locked for 365 days) suggests early-stage growth mode. Whether Gregory is actively trying to grow oack.io as a business or just maintaining it for personal use is unclear. If he is trying to grow it, that is a lifestyle signal (he wants to build something of his own) that could inform outreach angle.

4. **His view of the post-launch engineering challenge:** The May 2025 web paywall launch happened 12 months ago. By April 2026, the engineering team has had time to feel the operational reality of maintaining six PSP integrations. Whether Gregory has publicly commented on the challenges of that integration (Habr, technical Telegram channels, internal Adapty posts not indexed) is unknown.

5. **Technical Telegram channels:** Post-Soviet senior engineers often use Telegram for technical community. Gregory's lack of public presence on X/Twitter and Habr suggests Telegram may be a primary professional community channel. No Telegram handle was found. This is a gap.

6. **Python backend depth:** His April 2025 hiring post calls out "Backend/Python" as the primary stack. His GitHub shows Python as primary language. His Yandex era was Python-heavy. Whether Adapty's backend is primarily Python (consistent with the 2025 post) or has diversified is worth checking — the Backend Developer (Python) open role on the careers page as of April 2026 confirms Python is still the primary backend language.

7. **The "self-hosted k8s" signal:** He specifically says "self-hosted k8s" rather than EKS/GKE. This is Kirill's reliability doctrine made operational: they control their own Kubernetes to maximize availability. What the security posture of self-hosted k8s at Adapty's scale looks like is unknown — self-hosted k8s is notably harder to keep patched and audited than managed offerings. This may be a technically specific angle for Transilience if the product offering touches Kubernetes security posture.
