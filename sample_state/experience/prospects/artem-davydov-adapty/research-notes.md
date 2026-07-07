# Research notes — Artem Davydov

**Lead ID:** artem-davydov-adapty
**Company:** Adapty.io
**Research date:** 2026-04-30
**Tier:** A
**Playbooks run:** linkedin-deep-read, company-intelligence, trigger-event-detection, web-discovery, github-and-code-mining
**Podcast-and-talks result:** No public talks or podcast appearances found for Artem Davydov. He is not a public-facing operator. Section skipped per playbook protocol.

---

## Profile snapshot

**Title resolution — CRITICAL:**

Two LinkedIn URLs exist for Artem Davydov at Adapty:
- `linkedin.com/in/davyddd/` — LinkedIn title shows "Head of Engineering"
- `linkedin.com/in/artem-davydov-1087641bb` — Portuguese-locale LinkedIn page, also shows "Head of Engineering at Adapty Inc."

Both LinkedIn pages are stale relative to his self-described current role. His **GitHub bio** — which he controls and updates directly — reads: **"Infra Team Lead and Staff Engineer at Adapty Inc."** This is authoritative.

**ZoomInfo** confirms: "Infra Team Lead and Staff Engineer at Adapty." Multiple aggregators confirm that "Head of Engineering" was his *prior* title at Adapty, not his current one.

**Resolution:** Artem previously held the title Head of Engineering at Adapty. He is now Infra Team Lead and Staff Engineer. The LinkedIn pages have not been updated by him (stale LinkedIn is common in this persona). His GitHub is the ground truth. The title in the source CSV ("Infra Team Lead and Staff Engineer") is correct.

**Organizational picture:**
The open Infrastructure Team Lead job posting (careers.adapty.io, job ID 192221) explicitly states: "Gregory, Head of Engineering, is recruiting for this position." This confirms:
- Gregory Komissarov has the Head of Engineering title now (confirmed in the JD he authored and in multiple recent sources; ZoomInfo shows "Head of Development," which appears to be the same role with variant labeling)
- Artem reports to Gregory in his current Infra Team Lead and Staff Engineer role
- Artem's former "Head of Engineering" title was broad; Gregory now holds the top engineering management role
- The open Infra Team Lead job is an expansion hire — Adapty is hiring a *second* infrastructure team lead, not backfilling Artem (Artem is still in the role; he is being hired *around*, not replaced)

**Current title:** Infra Team Lead and Staff Engineer — Adapty.io
**LinkedIn handle:** `davyddd` (primary; `artem-davydov-1087641bb` appears to be an older or duplicate profile)
**GitHub:** github.com/davyddd
**Location:** Conflicting data across aggregators (ZoomInfo: Claymont, Delaware; LinkedIn: Warsaw; RocketReach: Tbilisi, Georgia). The company is fully remote; exact current location is not settled from public sources. Delaware likely reflects company incorporation address, not personal location.
**Email confirmed:** adavydov@adapty.io

**Tenure at Adapty:**
Artem joined Adapty via Poteha Labs (the pre-Adapty dev agency Vitaly Davydov ran). Exact start date at Adapty is not confirmed from public sources, but he was present in founding-era data (Poteha Labs → Adapty). He held the Head of Engineering title for a period and has since scoped into Infra Team Lead. Likely at Adapty since 2020–2021.

**Previous roles (confirmed from aggregators):**
1. Head of Engineering — Adapty (prior title, before Gregory Komissarov assumed the Head of Engineering role)
2. Backend/infra engineer — Poteha Labs (Vitaly Davydov's ML/NLP dev agency; confirmed via aggregators and Vitaly's research notes)
3. Backend developer — sibdev.pro (Krasnoyarsk-based Python web dev agency)
4. Developer — bro.agency

**Education:**
Siberian Federal University (SFU), Krasnoyarsk, Russia — Engineering Specialist Diploma, 2012–2018. Degree concentration: "Security of computer and information systems / information protection." Six-year integrated Engineering Specialist program (equivalent to Bachelor's + Master's).

**Significance of the education signal:** This is not a generic CS degree. His degree concentration was specifically in information security — offensive tools, application security standards, information protection systems. He has formal academic grounding in BurpSuite, nmap, sqlmap, wpscan, DirBuster, Metasploit, OWASP Testing Guide, and WASC Threat Classification. He is not a practitioner who picked up security awareness on the job. He studied it in structured academic context and then built a career on the infrastructure side. This is an unusual profile: security-trained engineer who became an infra operator.

---

## Activity scan (last 90 days)

**Browser session unavailable.** LinkedIn direct activity tab could not be accessed. Activity reconstructed from indexed public posts and aggregator data.

**Assessment:** Artem Davydov is a **sparse public presence**. He has no confirmed LinkedIn posts in the last 90 days indexed by search engines. His GitHub activity is the primary indicator of ongoing professional work (recent commits to dddesign, fastapi-stub, ddsql through February–March 2026). He does not appear to use LinkedIn as a publishing surface or as a commentary platform.

**Signal implication:** This is a low-public-output technical operator. The email strategy cannot rely on a specific post or comment he made; it must be anchored in what he *does* (the infrastructure he owns, the security education he has, the operational reality of the FunnelFox expansion) rather than something he said publicly.

**Gregory Komissarov's LinkedIn post (confirmed recent, within 12 months):**
Gregory posted recruiting content that included: "If you are looking for a fully remote job in an international product company and enjoy doing Backend/Python, Frontend/React, DevOps/self-hosted k8s for SaaS products, please let me know!" The phrase "self-hosted k8s" is significant — Adapty runs self-hosted Kubernetes, not managed (EKS/GKE), which implies their infra team owns more of the stack than a managed-k8s shop would.

Gregory also posted "I collect uptime nines" when recruiting for the Infra Team Lead role — a phrase that encapsulates the infrastructure team's primary identity at Adapty.

**Signal weight of Gregory's posts relative to Artem:** Low-medium. They reveal team culture and stack context, not Artem's personal perspective. They are still useful for framing because Gregory leads the team Artem is on.

---

## Article archive

**Result: None found.**

Artem Davydov has no public articles on LinkedIn, Medium, Substack, or any indexed blog platform. He has no confirmed conference talk slides on Speaker Deck or similar platforms. He has no podcast appearances.

**What exists in lieu of articles:** His GitHub repositories are his primary public intellectual output. They are technical documents in code form, and they reveal his architectural philosophy more clearly than any blog post would.

**GitHub as article substitute (high weight):**

His four public repositories constitute a coherent body of work:

1. **dddesign** — A Python DDD (Domain-Driven Design) library built on Pydantic. 15 stars, 21 releases, 213 commits. Actively maintained through March 2026 (latest release v1.1.11). This is not a toy project — it has 21 versioned releases and continuous CI/CD improvement. His README positions it as an implementation of Eric Evans' DDD and Martin Fowler's PEAA. The library's philosophy: "clear separation of responsibilities," domain logic "independent of storage implementations," "core application logic decoupled and modular."

   Signal weight: HIGH. He built an architectural framework to solve a real problem he encountered at Adapty (or while building for Poteha Labs). A Staff Engineer who builds and maintains an open-source DDD library is not just running infrastructure — he is thinking about how services should be structured to remain maintainable as they scale. This is architecture-minded infrastructure work.

2. **fastapi-stub** — A production-ready FastAPI application template implementing DDD. Stack: FastAPI, Dramatiq (async tasks via Redis), APScheduler, SQLModel/SQLAlchemy, PostgreSQL, ClickHouse, Kafka. Updated March 2026. This is essentially a blueprint for how Artem builds backend services — it mirrors Adapty's own production stack exactly (Redis, PostgreSQL, ClickHouse, Dramatiq).

   Signal weight: HIGH. The fastapi-stub is his mental model of what a well-structured service looks like. It shows his taste in tooling and his architectural instincts. The stack it codifies — Kafka for event streaming, ClickHouse for analytics, PostgreSQL for primary storage, Redis for task queuing — is the exact stack Adapty's Infrastructure Team Lead job description requires.

3. **ddsql** — A Python library for SQL query construction using Jinja2 template rendering, with adapters for PostgreSQL and ClickHouse. Released February 2026. Typed models for automatic result deserialization.

   Signal weight: MEDIUM. Confirms he is still hands-on with the database layer at the SQL level, not just at the ORM abstraction. A Team Lead who writes a SQL templating library is working close to the data tier.

4. **ddutils** — Python utility library; companion to dddesign. Minimal detail available.

**GitHub activity level:** Active in the last 6 months (commits through March 2026). He is an implementer, not just an architect. The personal repos are side-work; his primary contributions to Adapty production systems are through the @adaptyteam organization account (no public infra repos on that org).

**Confirmed technical stack (from LinkedIn skills and ZoomInfo):**
AWS ecosystem: ALB, ECS, EC2, RDS, S3, SES, SNS, Kinesis, Lambda. Kubernetes, Helm, Werf. Docker, gunicorn, Nginx. Python, Django, DRF, Celery/Dramatiq, Redis, PgBouncer, PostgreSQL, ClickHouse. Hexagonal architecture, DDD philosophy, GOF patterns (Strategy/DI, Abstract Factory, Factory Method), SOLID principles.

Security education tools (academic, from degree): BurpSuite, nmap, sqlmap, wpscan, DirBuster, Metasploit. Standards: OWASP Testing Guide, WASC Threat Classification.

---

## Engagement web

**Browser session unavailable.** Direct LinkedIn activity tab (comments on others' posts) could not be accessed.

**What can be reconstructed:**
- No indexed substantive comments from Artem on others' posts found in any search. He is not a commenter. He reads but does not engage publicly.
- His GitHub engagement is modest: 1 follower, 0 following, 6 starred repos. He uses GitHub for output (his own repos), not for social engagement.
- His GitHub's `wiki` repository suggests internal documentation habits, not public community engagement.

**Inferred peer reference group (low confidence):**
Given his technical stack (Python, DDD, Kafka, ClickHouse) and that he runs on self-hosted Kubernetes, his likely technical peer group is the Russian/post-Soviet Python engineering community and the DDD-in-Python community. Neither is a security-focused community. He did not arrive at Adapty through a security career path — he arrived through a Python/backend/infra career path with a security academic background.

**Topics likely to bring him out (inferred from GitHub):**
Architecture trade-offs (DDD vs. pragmatic patterns), Python backend infrastructure, Kubernetes operations, ClickHouse/PostgreSQL data architecture. Not: vendor announcements, marketing content, industry commentary.

**Signal implication:** The engagement web is sparse. He is a practitioner-introvert. Cold email to him must show direct domain fluency — not reference his public statements (there are none) but instead demonstrate understanding of the operational reality he lives in.

---

## External trail

### GitHub

**Account:** github.com/davyddd
**Organization:** @adaptyteam
**Bio (verbatim):** "Infra Team Lead and Staff Engineer at Adapty Inc."
**Activity level:** Active — commits through March 2026 on personal repos; organizational contributions presumably through @adaptyteam (no public infra repos on the org)
**Achievements:** Pull Shark (contributed PRs that were merged), Arctic Code Vault Contributor (code preserved in 2020 GitHub Archive Program)

**Pinned/notable repos:**
- dddesign (Python, 15 stars, MIT) — DDD framework library, actively maintained
- fastapi-stub (Python, 2 stars, MIT) — production FastAPI + DDD application template
- ddsql (Python, MIT) — SQL query builder for PostgreSQL/ClickHouse
- ddutils (Python, MIT) — DDD utility helpers
- wiki (no language) — documentation (likely internal Adapty infra docs)

**Cross-reference (GitHub vs. LinkedIn role):**
His personal GitHub output is entirely about making Python services more structurally sound — DDD, clean architecture, typed data layers. This is the thinking of a senior engineer who has lived through the consequences of bad architecture at scale. His fastapi-stub uses Dramatiq (which Adapty uses in production, confirmed in ZoomInfo tech stack), ClickHouse, and Kafka. He is not building toy projects — he is open-sourcing the patterns he uses at work.

The alignment between his personal library work and the production stack he maintains is tight. His GitHub is the window into how he thinks about the infra/backend layer at Adapty.

**GitHub as signal for outreach:** He is still an active implementer as of March 2026. He is not a pure-manager who delegated all hands-on work. The combination of Infra Team Lead title + active personal GitHub output in DDD/Python/infrastructure suggests he is playing a "player-coach" role — which is exactly what the open Infra Team Lead job description asks for ("Lead a distributed team in a playing coach capacity").

### Conference talks and podcasts

**Result: None found after thorough search.**
Zero podcast appearances, zero conference talks, zero Speaker Deck presentations attributed to Artem Davydov at Adapty. His profile is consistent with a practitioner who does not seek external visibility.

### Press and external mentions

**Result: Minimal.**
No press coverage, no journalist quotes, no blog posts. He does not appear in any Adapty press materials. The public Adapty narrative (TechCrunch, Business of Apps, etc.) is carried by Vitaly Davydov and Kirill Potekhin. Artem is entirely absent from the public-facing narrative.

### Verbatim quotes

**No public verbatim quotes found.** No posts, no talks, no press quotes exist in public record. The only candidate "voice" artifacts are his GitHub repository names, README text, and his bio.

From his GitHub bio (verbatim, self-described):
> "Infra Team Lead and Staff Engineer at Adapty Inc."

From the dddesign README (authored by him, architectural philosophy in code form):
> "if an Application uses more than one Repository, this indicates a design issue"
— README, dddesign library

This constraint statement is worth noting: it reveals an engineer with strong opinions about clean boundaries. A person who writes "this indicates a design issue" into a library's documentation is someone who cares about preventing structural drift. The equivalent in infrastructure is: accumulated cloud state that diverges from declared state is "a design issue."

---

## Company snapshot

For full Adapty company context, see `experience/prospects/kirill-potekhin-adapty/research-notes.md`. Key additions specific to Artem's position:

**Adapty's infra stack (confirmed from job posting + ZoomInfo + Gregory's posts):**
Self-hosted Kubernetes (not managed EKS/GKE). Python backend. PostgreSQL primary. ClickHouse for analytics. Kafka for event streaming. Redis for task queuing. AWS for supplemental services (ALB, S3, SES, SNS, Kinesis). Grafana for monitoring (8 global checkpoints, 15-second ping cadence). Multi-cloud + on-premise hybrid (per Kirill's October 2025 blog post).

**What this means for Artem's operational reality:**
Running self-hosted Kubernetes for a payments-adjacent SaaS at 99.99% SLA is a non-trivial operational commitment. Self-hosted k8s means the infra team owns the control plane — etcd backups, API server hardening, RBAC configurations, network policy management. These are things a managed Kubernetes service abstracts away. Artem's team owns this layer.

**FunnelFox PSP expansion impact on Artem:**
The May 2025 FunnelFox web paywall launch added Stripe, PayPal, Paddle, Braintree, Adyen, and Solidgate to the infrastructure Artem's team maintains. Each PSP integration is a new network boundary, a new set of webhooks, a new set of credentials, and a new set of outbound connections. From an infrastructure posture standpoint, this is a meaningful surface expansion.

**The "20-person team monitoring 24/7" claim:**
Adapty states on their infra page that a 24/7 dedicated team monitors infrastructure. This is likely the total monitoring/on-call pool across the engineering team, not 20 dedicated SREs — a company of 120 people does not have 20 dedicated SREs. Artem likely manages or contributes to the on-call rotation for the infrastructure layer specifically.

**The open Infra Team Lead job (infrastructure expansion, not backfill):**
The job posting asks for "8+ years building solutions with Kubernetes, Python, PostgreSQL, ClickHouse, and Kafka." This is a senior IC-plus-leadership role. The "playing coach" language is identical to Artem's current role description from the outside. Two interpretations:
- **Expansion:** Adapty is growing the infra team with a second senior lead. Given "200 employees growing 3x year-over-year" (from the job description — notably claiming 200 employees, larger than other sources), the infra team capacity is the constraint on growth.
- **Promotion signal:** If Artem is being elevated to a more architectural or strategic role (Staff Engineer as a stepping stone to Principal/Distinguished), the day-to-day team lead ops role would need filling. His dual title "Infra Team Lead and Staff Engineer" already contains both the management layer and the technical excellence layer — the open role may be bringing in someone to take the team-lead people-management work while Artem focuses on architecture.

Either interpretation leaves Artem in the infrastructure ownership role. He is not leaving; he is being hired around.

**Operational moment:**
Same as Kirill's research notes: Adapty is in post-launch scale mode for FunnelFox. The company is profitable, growing 3x YoY per their own hiring materials, and has just expanded from Apple/Google receipt validation (read-only, upstream-trusted) into web PSP payment processing (write-path, self-owned). Artem's team is the one that makes this expansion work. The compliance and security surface of the FunnelFox PSP integrations lives in his layer — webhook validation, credential management, network policies on the self-hosted Kubernetes cluster, the ClickHouse analytics pipeline that now includes web payment transaction data.

---

## Trigger event

**Primary trigger: FunnelFox web paywall launch (May 2025) + self-hosted Kubernetes surface expansion + security-educated infra owner**

The trigger for Artem is distinct from both Kirill's trigger (reliability-philosophy / payment trust) and Vitaly's trigger (enterprise sales / compliance questionnaires). Artem's trigger is operational:

When Adapty launched FunnelFox and integrated six PSPs into their infrastructure in May 2025, Artem's team acquired a materially larger and more complex attack surface to maintain:
- Six new PSP webhook endpoints (Stripe, PayPal, Paddle, Braintree, Adyen, Solidgate) — each a potential misconfiguration surface
- New outbound network policies required on the self-hosted Kubernetes cluster
- New secrets management requirements (PSP API keys, webhook signing secrets)
- ClickHouse analytics now ingesting web payment transaction data, not just Apple/Google receipt events
- A 99.99% SLA commitment now covering a more complex multi-PSP payment processing layer

Artem has a degree specifically in "Security of computer and information systems / information protection" and hands-on academic training in OWASP testing methodology. He knows what a cloud posture drift problem looks like — he studied it academically and now owns the infrastructure that is increasingly susceptible to it.

**Why the IaC drift angle is specific to Artem:**
The campaign brief names "operational-drift: IaC declared state vs effective cloud state" as the angle for this persona. This is calibrated correctly for Artem:

His dddesign library's core philosophy — "if an Application uses more than one Repository, this indicates a design issue" — translates directly to infrastructure: if your effective cloud state diverges from your declared IaC state, that indicates a design issue. He has built his intellectual identity around preventing architectural drift in code. The adjacent problem is preventing configuration drift in the cloud state his Terraform/Helm configs declare. His own programming philosophy predicts he would find this argument resonant.

The FunnelFox PSP expansion is a specific, recent, documentable reason why the gap between declared state and effective state is likely wider now than before the launch: six new integrations, rapid deployment timeline (FunnelFox was 12 days from Apple ruling to launch), self-hosted Kubernetes absorbing new webhook services. Rapid expansion in self-hosted k8s is precisely where IaC drift accumulates fastest.

**Secondary trigger:** The open Infra Team Lead hiring (Gregory's post + careers.adapty.io listing). Adapty is actively investing in the infrastructure function. They are growing the team, not cutting it. This is a moment of infrastructure investment, not belt-tightening. Outreach that arrives during infrastructure investment mode is more likely to receive attention than outreach during a cost-consolidation moment.

**Trigger strength ranking:**
1. FunnelFox PSP expansion (strongest — directly operational, specific, recent, in Artem's domain)
2. Infrastructure hiring investment (medium — signals active infra focus, but is company-level not Artem-specific)
3. No prospect-specific public statement available (limitation — no recent post or comment from Artem to anchor a warm-observational opener)

**Trigger-less fallback note:** Because Artem has no recent public statements, the dry-precise register (which requires the least prospect-specific voice signal) may be more appropriate than warm-observational. However, the combination of his security-educated background + DDD architecture philosophy + FunnelFox surface expansion provides enough operational-specific signal to anchor a diagnostic-pattern opener without needing a verbatim quote.

---

## Vitaly Davydov / family relationship

**The shared surname Davydov:**
Public record does not confirm a biological family relationship. The pattern (same uncommon-context surname + shared pre-Adapty employer + Artem brought into Vitaly's orbit via Poteha Labs) is consistent with a sibling, cousin, or close family connection. However, Vitaly studied at MIPT in Moscow; Artem studied at Siberian Federal University in Krasnoyarsk — approximately 4,000 km apart. They could be brothers with different universities, or unrelated colleagues from different cities.

**Geographic divergence:**
Krasnoyarsk (Artem's university) is 4,000 km from Moscow (Vitaly's university). However, Vitaly was born and raised in Russia; "Davydov" is a common Russian surname. Siberian Federal University draws from across Russia; Vitaly could have family in Siberia. This does not resolve the question.

**Operational significance:**
Whether they are family or not, Artem entered Adapty through Vitaly's network (Poteha Labs). They have a close professional relationship with multiple years of shared history. The multi-thread outreach sequencing note in Vitaly's research notes stands: do not contact Vitaly and Artem in the same week without a strategy for note-comparison. Artem would be aware quickly if Vitaly received an outreach.

**Conclusion:** Low-confidence inference that they may be related; no public confirmation. The professional relationship (Poteha Labs → Adapty) is confirmed. The family relationship is unconfirmed and should not be referenced or assumed in any email.

---

## Disqualify check

**Result: CLEAR — no disqualify signals found.**

- No "Open to Work" status. His GitHub bio and ZoomInfo both show active employment at Adapty.
- No layoff or company restructuring signals. Adapty is growing (3x YoY per their own JD materials), profitable, and actively hiring 20 open positions.
- No personal crisis, grief, illness, or family issue signals in any public source.
- No PTO, sabbatical, or extended leave signals.
- His GitHub shows commits as recently as March 2026. He is actively working.
- No "not taking inbound" signal.
- The open Infra Team Lead hiring is an expansion signal, not a backfill for Artem — he is still in role.

**Potential routing note (not a disqualify, but worth flagging):** If Artem was previously Head of Engineering and is now Infra Team Lead, there may be some sensitivity about role scope. This is not a demotion signal per public evidence (the company is growing, the infrastructure function is expanding), but it could mean he has processed a title change that he has not fully updated on LinkedIn. A cold email that references his "Head of Engineering" title would be using stale data; using "Infra Team Lead" or simply referencing his operational ownership without a title is safer.

---

## Open questions

1. **Why the title change from Head of Engineering to Infra Team Lead?** The most likely explanation: as Adapty scaled from ~50 to 120+ employees, the "Head of Engineering" scope became too broad for one person, and Gregory Komissarov was brought in or elevated to run the overall engineering function (he has 17 years of engineering leadership experience). Artem may have self-selected to go narrower and deeper on infrastructure rather than manage a broader engineering organization. This is a common pattern for technically-deep engineers when companies scale. Alternatively, Gregory joining Adapty (from SOAX / Tango Me) is what created the organizational realignment. The exact sequence is not confirmed. Confirming this would help the profiler assess whether Artem is satisfied with his current scope or feels constrained by it.

2. **When did Artem join Adapty and what was his exact Poteha Labs role?** Duration at Poteha Labs and what he built there would clarify the depth of the Vitaly/Artem professional relationship and whether Artem was a junior developer brought along or a peer contributor. This matters for sequencing multi-thread outreach.

3. **Artem's current location — Warsaw, Delaware, or Tbilisi?** Conflicting aggregator data. This affects email personalization around local regulatory context (GDPR if Warsaw/EU, different if US). Not critical for the email but worth resolving before reference to any geographic context.

4. **Is the open Infra Team Lead job a backfill or expansion?** Best current evidence is expansion (Adapty claims 200 employees, 3x growth; the JD language suggests scaling the infra team, not replacing someone). But if Artem has been quietly elevated to a Principal/Distinguished Engineer or architectural track, the day-to-day Team Lead role would need filling. The profiler could weight these two interpretations differently for angle calibration.

5. **What is Artem's actual relationship to Vitaly Davydov — colleague or family?** Unresolved from public sources. Multi-thread sequencing should treat them as closely connected professionals regardless.

6. **Has Artem made any LinkedIn posts in the last 90 days that are not indexed?** Browser session unavailable prevented direct activity tab access. The last confirmed LinkedIn post from him found via web search is stale. He may have sparse activity that is not indexed. Direct profile visit would confirm.

7. **Does Artem's security academic background have any visible operational expression at Adapty?** His degree was in information security with OWASP / penetration testing focus. His current role is Infra Team Lead. Whether he applies any of that background to cloud posture / network security policy at Adapty — or whether he treats it as a dead academic credential — affects how to pitch the angle. His fastapi-stub project does not contain security-specific patterns (no auth hardening layers, no secrets rotation examples); this may suggest his security education has not been operationalized into his current infrastructure work. This is an interesting gap.

8. **Does Artem have any GitHub contributions to the @adaptyteam organization repos?** The adaptyteam org has no public infra repositories; his contributions are through private repos. Checking if he appears in commit histories on any public SDK repos would confirm whether he crosses into the product engineering layer or stays strictly in infra.
