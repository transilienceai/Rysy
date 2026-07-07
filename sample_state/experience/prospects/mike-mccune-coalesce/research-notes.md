# Research notes — Mike McCune

**Lead ID:** mike-mccune-coalesce
**Research date:** 2026-04-30
**Tier:** A
**Disqualify check:** Clear — no signals of unemployment, active crisis, extended leave, or stated aversion to inbound. Profile says "CURRENTLY LEADING ENGINEERING AT COALESCE.IO" on personal site (mccune.io). Most recent activity 1 week ago. Active and in role.

---

## Profile snapshot

**Current role:** VP of Engineering, Coalesce.io
**Tenure in current role:** April 2024 – present (~13 months as of research date)
**Location:** Portland, Oregon, United States
**LinkedIn followers:** 1,979
**LinkedIn connections:** 500+
**Premium member:** Yes
**Pronouns:** He/Him

**About section:** No substantive About section visible on LinkedIn. The profile renders primarily as an activity feed without a bio description in the standard LinkedIn position.

**Personal site tagline (mccune.io):**
> "Engineering leader who builds teams that ship."
> "Two decades scaling product engineering, Red Hat, Logixboard, now Coalesce. I build remote-first teams that move fast, hold the line on quality, and stay aligned with product, design, and GTM."

Tone: Spare, operator-confident. Three-word punch: "teams that ship." No fluff, no vision language — the site is built to attract inbound for senior-leader hiring, advising, or conversation. Anti-brand-building energy; explicitly functional.

**Career progression (3 prior roles):**

1. **Coalesce.io — VP of Engineering** (April 2024 – present, ~13 months)
   - Personal site: "Leading an AI forward, fully remote global engineering organization that builds and supports Coalesce's core data transformation platform. AI features, platform scale, and developer ergonomics in tight coordination with product and design."

2. **Logixboard — VP of Engineering** (July 2022 – 2023, ~18 months)
   - Personal site: "Scaled a 45-person globally distributed team. Drove platform observability and feature delivery that produced 75% revenue growth and 50% infra cost reduction."
   - Key signal: The personal site explicitly lists **SOC 2** among Logixboard deliverables: "revenue growth through delivery, observability investments, and SOC2."
   - Logixboard is a freight/logistics SaaS platform — regulated-adjacent industry (international trade compliance, freight forwarder data).

3. **Red Hat — Director of Engineering** (2004 – July 2022, 18+ years)
   - Personal site: "IC to Director. Owned product lines that produced top-5 revenue with consistent 35% YoY growth."
   - Departure post (July 2022, verbatim): *"Well, after 18+ years I'm on my way out of Red Hat with my last day in the 'office' today. My official end date is July 15th with some PTO next week before I start my new gig. I'm heading to a small startup in the Seattle area and am absolutely stoked to start something new, wake up at a normal time and ride a bit of the chaos of the startup life again. My time at Red Hat with all of you has been monumental to me and I have the fondest memories of all the ups and downs (mostly ups!) over the years. I've been saying it over and over the last few weeks that the people are what kept me here so long and it is hard to walk away from all of you."*

**Career archetype reading:** Mike is the classic "long-tenured company IC-to-manager who then leaps to smaller, faster-moving orgs" archetype. 18 years at Red Hat (a large, open-source-native enterprise) gave him a deep grounding in platform engineering, Kubernetes-era infrastructure, and process rigor. He moved to a 45-person startup (Logixboard), scaled it, and then moved to Coalesce — a 140-person company mid-growth sprint with two acquisitions in 12 months. His personal site metrics — "130+ engineers led, 11 time zones, 20+ years leading eng" — show he thinks of himself as an org-scale operator, not an IC contributor.

**Builder vs. operator signal:** Operator, tilting back toward builder. In his Coalesce joining post (April 2024), he wrote: *"The time away from full time work was beyond invaluable as I finally had the time to get back into technology directly. I spent time learning by building small applications, realizing SO much has changed when I stepped away from hands-on coding work."* This reveals a manager who had drifted from code and actively worked to reconnect. GitHub shows 18 contributions in 2026 YTD — sporadic but present. His most recently forked repos are AI tools (personalagentkit, slacrawl, Keycard-related), not enterprise infrastructure. He experiments on the side; he manages at work.

---

## Activity scan (last 90 days)

**Summary:** No original posts in last 90 days (LinkedIn Posts tab returns "Nothing to see for now"). All visible activity is reposts and comments. Comments tab shows 19 items across the last ~60 days. This is a sparse-original-post profile; his signal is in his comments and reposts.

---

### Highest-signal items (weighted most to least)

**1. Comment on Claude Code PR review pricing — HIGH WEIGHT (1 month ago)**

Post: Sam Keen (ex-AWS, Lululemon, Nike; AI Research & Educator) posted about Anthropic's Claude Code Review costing $15-25 per pull request compared to a human code review.

Mike's verbatim comment:
> "we run at a rate of roughly 40 PRs/week for my team and were averaging about $55/review putting it at $110k+/year. Perhaps worthwhile but Cursor's bugbot at $40/seat with unlimited PR reviews is a better price point with amazing value that we have been getting from it."

**Weight: Highest single signal in the dataset.** This comment reveals:
- Team is active: 40 PRs/week is a real engineering cadence at Coalesce
- He tracks tooling costs per developer hour closely — cost-per-output thinking, not just capability thinking
- He's already using Cursor's bugbot for automated PR review — meaning he has an active AI-assisted engineering workflow in place
- He evaluated Claude Code's PR review and found a cheaper alternative that met his needs — he does his own math, doesn't accept vendor pricing without benchmarking
- This is a VP who still owns tooling decisions at the workflow level — operator but with hands in the tools

**2. Repost of Jamie D. (Google Cloud) — AI + Domain Knowledge story — MEDIUM-HIGH WEIGHT (2 months ago)**

Jamie D. posted a story about a 100-year-old company with monolithic C code in a heavily regulated industry. A senior architect, with domain expertise, used AI to complete in 3 days a project that was scheduled for 30 weeks. Mike reposted this without comment.

The post's thesis: AI without domain knowledge is noise; AI multiplied by domain knowledge is transformational.

**Weight: Medium-high.** Mike reposted without original commentary, which reduces weight relative to a substantive original comment. However, the selection of this specific post — not generic "AI is amazing" content but a specific story about domain expertise + AI in a regulated, legacy-code environment — signals what he finds credible. This is consistent with the Keycard repost (see below) and the Claude Code review comment: Mike is drawn to *specific, operationally grounded* AI content, not hype.

**3. Comment on SYNQ acquisition post — MEDIUM WEIGHT (1 month ago)**

Coalesce.io corporate post announcing SYNQ acquisition.

Mike's verbatim comment:
> "excited to bring more depth to our stack and team!"

**Weight: Medium, low verbosity but genuine.** Brief, positive, enthusiastic. No hesitation language. He publicly endorsed the integration direction. This is not a mandatory "say something nice" comment; it's brief but not perfunctory given the enthusiasm marker "excited." Consistent with someone who is driving the integration work, not just watching it happen.

**4. Repost of Keycard (AI agent identity/credentials) — MEDIUM WEIGHT (~7 months ago)**

Matthew Creager posted about Keycard — a startup building "credentials that carry task, intent, and full lineage. Runtime-scoped" for AI agents. The post described the problem: legacy auth tells you WHO accessed, but not WHY they needed it, WHAT TASK they were completing, or HOW that permission came to exist.

Mike reposted this. No original commentary.

**Weight: Medium.** This repost is 7 months old (past the 30-day high-weight window) but notable because: (1) it is explicitly about access control and security for AI agents, (2) the specific language in the post — "credentials that carry task, intent, and full lineage" — is precisely the security-provenance problem that is escalating as Coalesce adds AI features (Copilot) on top of a data platform. A VP of Engineering reposting an access-control/identity startup's announcement signals awareness of the identity problem in agentic systems. Combined with the Claude Code and AI domain knowledge reposts, a consistent pattern emerges.

**5. Comment on Brent Midwood (Tanium) joining post — LOW WEIGHT (1 month ago)**

Brent Midwood announced starting a new role as Sr. Director, PM and Portfolio Lead at Tanium (endpoint security company).

Mike's verbatim comment: *"oh damn, welcome to the other side! congrats"*

**Weight: Low.** Congratulatory. However: he has a connection at Tanium now. "Welcome to the other side" suggests Midwood crossed over from a non-security-native role into a security company — and Mike recognizes the transition as meaningful. The word choice "other side" implies Mike sees the security world as distinct from his own current operating environment.

**6. Comment on "ditching microk8s for k3s in CI" (Chris Alfonso, Kubernetes rewrite) — LOW WEIGHT (1 week ago)**

Chris Alfonso (Director, OpenShift & Kubernetes Engineering) posted about rewriting Kubernetes in Rust.

Mike's verbatim comment: *"Chris Alfonso we just ditched microk8s for our CI for k3s .. perhaps we should just jump straight to ... c10o?"*

**Weight: Low-medium as a portrait signal, but confirms hands-in-infrastructure.** Mike knows the internal CI/CD stack well enough to make a specific joke about switching Kubernetes distributions. He's not the all-business operator who doesn't know what CI tooling runs; he's still close to the platform.

**7. Aggregate reactions/reposts (~12 visible items in the 90-day window)**

Primarily reposts of: Coalesce company posts (SYNQ, Armon 4-year post), Snowflake product team updates (Josh Klahr on Open Semantic Interchange), a Python engineer job posting for a mental health startup, Red Hat intern posting at Katie Riker.

Pattern: He reposts Coalesce content (loyalty/brand signal), amplifies hiring posts for peers and his network (connector behavior), and engages with infrastructure/AI content from the Kubernetes/cloud-native community (identity signal from prior Red Hat tenure).

---

## Article archive

**LinkedIn Articles:** None. The Articles tab is empty.

**mccune.io:** No blog section. The personal site is a positioning page (About, Experience, Work, Contact) only — no longform writing.

**No external longform writing found** under his name at Coalesce. Mike McCune does not write publicly. He is not a content creator or thought leader by publication; his public voice is entirely via reposts and comments.

*Note for profiler: The absence of writing is itself signal. He is not building a personal brand. He is doing the work.*

---

## Engagement web

From visible comments activity (last 90 days):

| Person | Role | Topic | Comment weight |
|---|---|---|---|
| Sam Keen | AI Research & Educator, ex-AWS/Lululemon | Claude Code PR review pricing | High (substantive, specific data) |
| Chris Alfonso | Director, OpenShift/Kubernetes Engineering, Red Hat | Kubernetes Rust rewrite | Low-medium (infrastructure joke) |
| Brent Midwood | Sr. Director PM, Tanium | Job announcement | Low (congrats) |
| Steven Rostedt | Open Source Developer (Red Hat alumni) | Red Hat 2006 interview list | Low (congrats/nostalgia) |
| Kevin Smith | Engineering Leader & Distributed Systems Nerd | CLI tool for novelists | Low (bug report: "404 on the GH link") |
| Jamie D. | App & Infra Transformation, Google Cloud | AI + domain knowledge story | Medium (repost only) |
| Armon Petrossian | CEO/Co-Founder, Coalesce | 4-year Coalesce anniversary | Low (repost only) |
| Josh Klahr | Product, Snowflake | Open Semantic Interchange update | Low (repost only) |
| Matthew Creager | — (Keycard) | AI agent identity/credentials | Medium (repost only) |
| Austin Banta | — (Coalesce) | Coalesce hiring post | Low (repost) |

**Engagement web pattern:** Mike engages substantively only with tooling/cost/productivity content. His recent engagement with Sam Keen on Claude Code pricing is the only comment where he shared internal data. He engages lightly with his Red Hat-era network (Kubernetes/cloud-native people). He reposts Coalesce company content consistently (loyalty). He does not engage with security leaders, compliance content, or CISO-level conversation — security is not a topic he publicly engages with on LinkedIn.

**Topics that bring him out:** Developer tooling cost, AI productivity ROI, infrastructure decisions (CI/CD, Kubernetes distributions).

**Reference group signal:** His peer group includes Red Hat/Kubernetes-era cloud-native engineers, engineering leaders at early/mid-stage startups, and data platform ecosystem people. No visible engagement with security practitioners.

---

## External trail

### Personal website (mccune.io)

Active personal site, updated as of 2026 (copyright "© 2026 Mike McCune"). Three-column career story:

**Key verbatim from mccune.io:**
> "Building teams that push past their own ceiling."
> "Two decades of scaling engineering orgs has taught me one thing: the best work happens when the system around the team (clarity, trust, tools, ritual) is as well-designed as the product itself."

The site lists four work pillars:
- **Vision:** "Engineering, product, design, and GTM aligned around a single, observable bet."
- **Velocity:** "Tight feedback loops, ruthless prioritization, and ship cadence the org can rely on."
- **Talent:** "Diverse senior ICs and managers who scale themselves out of..."
- (fourth not fully captured)

**Logixboard entry (highly relevant):**
> "Scaled a 45-person globally distributed team. Drove platform observability and feature delivery that produced 75% revenue growth and 50% infra cost reduction."
> Explicitly lists: "75% REVENUE GROWTH" — and separately calls out **"observability investments, and SOC2"** as deliverables in the context of Logixboard revenue growth.

This is the only place Mike has mentioned SOC 2 publicly. The framing is telling: SOC 2 is listed alongside revenue growth and observability investments — it was an infrastructure-level enabling work, not a standalone compliance initiative.

### GitHub (mccun934)

- **Account:** https://github.com/mccun934
- **Repositories:** 122 public (mostly forks)
- **Stars:** 68
- **Followers:** 22, Following: 1
- **Activity level:** Sporadic — 26 contributions in last year; 18 contributions YTD in 2026
- **Contribution graph:** Low-density, scattered. Not a daily committer.

**Recently updated forks (most recent activity):**
- `slacrawl` — CLI terminal app for Slack with SQLite backend (Go) — forked from vincentkoc
- `personalagentkit` — "A seed for growing your own bespoke AI agent — autonomous, self-naming, and built to learn over time using Claude Code" — forked from gbelinsky
- `exa-lead-gen-agent` — Lead generation agent (forked)
- `chartli` — CLI that turns numbers into terminal charts (forked)
- `KIRA` — Krafton Intelligence Rookie Agent (Python) (forked)
- `retirement-planner` — Retirement account calculator (TypeScript) (forked)
- `manager-resources` — Engineering manager resources (forked from dmleong)
- `motia` — Multi-Language Backend Framework with AI agents, observability, queues (TypeScript)
- `kimi-writer` — AI writing agent

**Recently starred (most recently starred first):**
- `slacrawl` (Go — Slack CLI)
- `andrej-karpathy-skills` — "A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls"
- `skills` — based on The Minimalist Entrepreneur
- `autoresearch` — "Claude Autoresearch Skill — Autonomous goal-directed iteration for Claude Code"
- `chartli`
- Keycard AI agent (starred around 6-7 months ago)
- `instructlab` (InstructLab Core — Red Hat's fine-tuning workflow)
- `Verba` (Weaviate RAG chatbot)

**Cross-reference observation:** GitHub activity is completely consistent with the LinkedIn portrait — Mike is actively experimenting with Claude Code tooling, AI agents, and productivity tools. He starred `andrej-karpathy-skills` (a CLAUDE.md file for Claude Code) and `autoresearch` (autonomous Claude Code iteration). He is clearly a hands-on user of Claude Code both personally (starred tooling) and at work (reported $110k+/year spend at Coalesce). His GitHub is not "professional" work — it is personal experimentation and curiosity tracking. The personal/work split is clean: he manages at work, experiments at home.

**Architecture vs. implementer:** His own repos (`fakerpmrepo-generator`, `grinder`) are old Python/shell tools from the Pulp (Red Hat content management) era. His recent activity is forks-and-stars, not original contributions. He is a consumer and experimenter with AI tools, not a contributor to them. Consistent with the Coalesce joining post: he's re-engaging with code after years of management, doing it on the side with AI assistance.

### GitHub: Logixboard SOC 2 signal

No GitHub repos related to SOC 2 or compliance tooling. The SOC 2 work at Logixboard (per his personal site) appears to have been an organizational/vendor initiative he owned, not a hands-on implementation. This is expected for a VP of Engineering.

### Podcasts and talks

**No podcast appearances found under Mike McCune's name.** No conference talks found for the management-track Mike McCune. His Red Hat era appears to have been primarily internal management (Director of Engineering), not external-facing technical speaking. The conference talks found under "Michael McCune" from Red Hat (OpenStack Summit Boston 2017, Strata EU 2019, KubeCon SIG Cloud Provider talks) are attributable to a different Michael McCune (GitHub: elmiko) who was an individual contributor and Kubernetes SIG Cloud Provider co-chair.

**Zero podcast/talk external trail for our prospect.** He is not a public speaker and has not given talks in his current role. The email cannot reference a specific talk or podcast.

### Press and announcements

No press quotes found for Mike McCune at Coalesce. He is not quoted in the SYNQ acquisition press release (Armon is) or the CastorDoc acquisition press release (Armon and Satish are). His name does not appear in Coalesce's external communications.

**Pattern:** He is entirely internal-facing. He leads the engineering organization that builds the product; he does not represent Coalesce externally.

---

## Company intelligence

*Cross-referenced from Satish's research notes; only Mike-specific additions noted here.*

### Coalesce's operational moment (Mike-specific lens)

Coalesce made two acquisitions in 13 months: CastorDoc (March 2025, now Coalesce Catalog) and SYNQ (March 2026, now Coalesce Quality). Both acquisitions required engineering integration work — new codebases, new teams, new platform surface area. Mike joined Coalesce in April 2024, eleven months before the first acquisition (CastorDoc, March 2025) and two years before the second (SYNQ, March 2026).

**Operational implication for Mike specifically:**
- He is 13 months into the role, having gone through the CastorDoc integration and now in the early stages of the SYNQ integration
- His comment on the SYNQ announcement ("excited to bring more depth to our stack and team!") uses the words "stack" and "team" — both acquisitions brought new engineering teams and new codebases to integrate
- His personal site describes his four pillars as Vision, Velocity, Talent, and a fourth (presumably Culture or Execution). Post-acquisition, all four of those pillars are stressed: vision alignment across merged teams, velocity with more surface area, talent integration of acquired-company engineers

### Hiring signals (engineering-specific)

Only 2 open roles at Coalesce as of April 2026:
1. Senior DevOps Engineer — EMEA (Infrastructure & SRE)
2. Sales Director — France

**The DevOps job description is highly signal-rich:**
- Stack: ArgoCD, Terraform, GitHub Actions, DataDog, PagerDuty, Tailscale, Kubernetes on all 3 major clouds
- Required: *"Experience adhering to security frameworks (SOC2) and working with security teams to triage vulnerabilities or other findings."*
- Bonus: CISM, CISSP, or other security certifications; Kubernetes security certification (CKS, KCSA)

**Operational inference:** The one engineering hire they are making explicitly requires SOC 2 adherence experience and security vulnerability triage. This is the Infrastructure & SRE team — Mike's org. The fact that this role lists SOC 2 as required experience, while Coalesce has no dedicated security title and no CISO, means the SOC 2 work currently sits inside the engineering org under Mike. He owns it, or his team does.

---

## Trigger event

**Chosen trigger:** SYNQ acquisition and Coalesce Quality launch (March 10, 2026, 51 days ago at research date) + the active SOC 2 burden signal in the open DevOps role.

**Two-part trigger:**
1. **Acquisition integration burden:** Two acquisitions in 13 months. The second one (SYNQ, now Coalesce Quality) closed 51 days ago. Mike's comment — "excited to bring more depth to our stack and team!" — signals he owns the integration work. VP of Engineering at a company that just closed its second acquisition in a year is deep in integration labor: new codebase surface area, new team dynamics, new security/compliance perimeter to maintain.

2. **SOC 2 as open hiring requirement (not a solved problem):** The only engineering hire they are making at Coalesce explicitly requires SOC 2 adherence experience. This means: (a) the current team does not have dedicated SOC 2 capacity, and (b) they recognize the gap enough to require it in a new hire. For a tool like Transilience (continuous compliance evidence), this is the precise operational moment when a VP of Engineering might be receptive: active integration work creating new compliance surface area, no dedicated security owner, and they're trying to staff into it.

**Why this is the strongest trigger for this campaign:**
- It is specific and recent (SYNQ acquisition 51 days ago, within the 60-day threshold)
- It connects directly to Mike's immediate operational reality (he is in post-acquisition integration mode)
- The SOC 2 signal is not inferred — it's explicit in his open job posting
- The trigger does not require Mike to admit a problem publicly; the problem is already public through the job listing
- Unlike Satish (who owns the architectural vision for the platform), Mike owns the engineering capacity cost. Continuous compliance evidence as an engineering capacity problem — not just a security problem — is the right frame for this persona

**Alternative trigger candidate (weaker):** Claude Code review tooling discussion (1 month ago). Mike explicitly said his team runs 40 PRs/week and was spending $55/review ($110k+/year) on Claude Code before switching to Cursor. This reveals a VP who thinks about engineering costs per-unit. However, this is not a security angle — it is a general engineering productivity angle. It works for establishing credibility and persona fit, but it's not the campaign trigger.

**How the email uses the trigger:**
- Lead with the acquisition context — specifically the expanded compliance surface (two acquisitions = two codebases, two engineering teams, two sets of vendor relationships to audit)
- Bridge to the SOC 2 work: at 140 people with no CISO, continuous compliance evidence is engineering work. His own job posting says so.
- The ask is not "do you have a security problem" but "you've just expanded the surface area twice in 13 months while your engineering team has been doing the actual integration work — what's your plan for keeping the compliance picture current without it becoming another sprint item?"

---

## Open questions

1. **Who is Mike's SOC 2 point person?** His personal site lists SOC 2 as a Logixboard deliverable. At Coalesce, the DevOps job posting requires SOC 2 adherence experience. But no one on the visible Coalesce team has a security or compliance title. Is Mike personally managing the SOC 2 renewal program, or is it currently owned by a specific engineer (possibly DevOps lead)? The answer changes how the email frames the ask — "you're doing this yourself" vs. "your team is stretched managing this."

2. **Red Hat heritage and process rigor:** 18 years at Red Hat means Mike grew up in open-source governance culture, where security reviews, CVE triage, and responsible disclosure are normal engineering overhead. Does he view compliance work as a natural cost of doing business (Red Hat frame), or does he view it as organizational overhead that competes with velocity (startup-mode frame)? The Logixboard experience (startup, SOC 2 as a growth enabler) suggests he can hold both, but it is unknown which frame dominates at Coalesce.

3. **Tension between post-acquisition integration work and sprint velocity:** Mike's personal site emphasizes "velocity" and "tight feedback loops" as core to how he leads. But post-acquisition integration is inherently slow, non-sprint, coordination-heavy work. Is he experiencing velocity pressure right now, or is the integration phase being managed as a separate track from the core product cadence? His 40 PRs/week team cadence suggests the core product team is still shipping — but the integration work may be pulling bandwidth from a subset of engineers.

4. **How close is Mike to the compliance renewal cycle?** Coalesce achieved SOC 2 Type 2 in July 2022. Annual renewal means there have been 3+ subsequent audits, likely scheduled around July each year. If they maintain an annual cadence, the next audit window is ~July 2026 — approximately 10 weeks from the research date. This creates a credible budget-cycle and calendar pressure window for the outreach.

5. **Mike's connection to Tanium (via Brent Midwood):** He congratulated Brent Midwood on joining Tanium's security PM team. Does Mike have a pre-existing relationship with Tanium's ecosystem, or was this a passing comment? Tanium does endpoint security and compliance reporting — adjacent to Transilience's space. Not an actionable signal yet, but worth noting if the email references peer companies doing continuous compliance work.

6. **The "domain knowledge + AI" frame:** Mike's repost of the Jamie D. story (domain expertise x AI = 30 weeks → 3 days) signals what he finds credible in AI productivity narratives. This is relevant to how a Transilience pitch should be framed to Mike: not "AI-powered compliance automation" (too hype-adjacent) but "your team already has the compliance domain knowledge; Transilience makes that knowledge continuously active across your expanded platform surface area." The domain-expertise multiplier frame may resonate more than the automation frame for this persona.
