# Witness cross-draft review -- Adapty (4 leads)

**Date:** 2026-04-30
**Reviewer posture:** Stranger. No knowledge of the writer. No investment in the outcome.

---

## Draft 1 -- Kirill Potekhin (CPO/CTO Co-Founder)

**Subject:** Reliability of the PSP control plane

**Verdict: ship**

### What works

The opener earns its existence. "Twelve days from the antitrust ruling to FunnelFox shipping with six PSPs integrated" is a verifiable fact that proves the writer did the work, and "the kind of execution that makes the infrastructure-as-product frame more than a slogan" paraphrases Kirill's published doctrine without quoting it back at him. The distinction matters: it operates near his language rather than echoing it. The second sentence -- connecting the PSP control plane to the product reliability surface rather than treating it as a separate operational concern -- is a genuine synthesis, not a restatement. A CPO/CTO who wrote "since infrastructure is our product, reliability isn't a feature" would recognize this as someone who read his work and extended it one step, not someone who Googled his name. The Transilience sentence is one sentence, appropriately restrained. The CTA ("What instrumentation does the PSP control plane have today?") is a real engineering question that a builder-founder can answer in two sentences if he chooses to.

### What fails

"Frame more than a slogan" carries a faint whiff of judgment -- it implies the infrastructure-as-product idea could be a slogan, which is not how Kirill would hear his own published position. A builder-founder six years in does not worry about whether his operational philosophy is a slogan; he has the uptime numbers to prove it is not. The phrase is clever rather than honest. It is a minor blemish, not a structural problem.

### Per-draft question: Does "infrastructure-as-product" land as observation or echo?

It lands as observation. The writer does not quote the article; the writer extends its logic to the new PSP surface. That is the right move for a sparse poster who publishes deliberately -- the email demonstrates comprehension, not surveillance.

---

## Draft 2 -- Gregory Komissarov (Head of Development)

**Subject:** PSP credential state on self-hosted k8s

**Verdict: ship**

### What works

The angle is genuinely distinct from Draft 1. Where Kirill's email is about architectural-philosophical coherence (reliability surface = product surface), Gregory's is about the operational layer beneath it: credential state accreting faster than anyone baselines against. This maps to the portrait's central finding -- Gregory built oack.io because monitoring tools "stopped at the HTTP layer," so the email positions Transilience at a layer his own tool explicitly does not cover (secret-scoping-and-rotation vs. request/response). The parenthetical "(which oack and the rest of the observability stack already cover)" is the strongest move in any of the four drafts. It names his tool, acknowledges it covers its layer, and draws a clean boundary rather than claiming overlap. A builder who shipped his own monitoring product would notice that distinction immediately and respect it. "Rotation week" is appropriate engineer vocabulary -- it is the shorthand infrastructure teams actually use for the periodic pain of credential rotation across multiple providers. The CTA ("How is credential state currently tracked at the cluster level?") is the right question for someone who thinks in operational terms, not buying terms.

### What fails

"Accretes faster than anyone declares a baseline against" is a dense clause that requires re-reading. Gregory would parse it -- he is technical enough -- but the sentence carries more syntactic weight than necessary for its meaning. A plainer construction would land faster with someone whose inbox time is measured in seconds.

### Per-draft question: Does naming oack.io land as build-vs-buy honesty or keyword-stuffing?

Honesty. The email does not praise oack.io or describe it; it names it in a parenthetical that draws a scope boundary. This is the correct posture toward a builder's side project: acknowledge its existence and its competence at its layer, then identify the adjacent layer it does not cover. If the email had opened with oack.io or made it the subject, it would read as surveillance. In a parenthetical, it reads as homework.

---

## Draft 3 -- Vitaly Davydov (CEO Co-Founder)

**Subject:** 4th variable beyond price/convert/change

**Verdict: rewrite** (prior round) -> see v2 review below

### What works (v1 review, retained for record)

The foreword reference is the right anchor. Vitaly's "price, convert, change" framing from the 2026 State of In-App Subscriptions is recent, public, in his own voice, and commercial rather than technical -- which matches his current identity. The "fourth member" concept is a real insight: enterprise security questionnaires do become a deal-cycle variable when product surface expands. This is the kind of thing a CEO approaching enterprise sales would encounter and not yet have a frame for.

### What fails (v1 review, retained for record)

Two problems. First, "at enterprise altitude" is decorative language that does not appear anywhere in Vitaly's vocabulary. The portrait describes him as a storyteller-founder, not as someone who talks in altitude metaphors. The phrase tries to elevate the sentence and instead creates distance. Second -- and this is the structural problem -- the email's second sentence assumes too much about Vitaly's deal-cycle reality: "The deals that stall here aren't about whether SOC 2 exists -- they're about the speed at which a buyer-side security review can match..." This is projection. The research shows Vitaly is hiring a VP of Sales and a Head of Growth; the enterprise deal-cycle friction is plausible but not evidenced. The email declares his problem to him rather than asking whether the problem exists. This is the most dangerous failure mode the witness role exists to catch.

### If rewrite -- specific direction (v1, retained for record)

Remove "at enterprise altitude" -- it is not his register. Rewrite the second sentence to probe rather than declare: the email should ask whether deal-cycle security questionnaires have become a variable, not assert that they have. The first sentence (foreword reference + fourth member) is strong enough to carry the email if the second sentence earns its place through inquiry rather than projection.

---

## Draft 4 -- Artem Davydov (Infra Team Lead and Staff Engineer)

**Subject:** Reconciliation between IaC and cluster state

**Verdict: ship**

### What works

The email correctly assumes security-vocabulary fluency throughout. "IAM roles, new secret stores, new network policies, all declared in IaC and all subject to drift the moment the next iteration ships" -- a person with a six-year formal security education and a DDD library built around declared-vs-actual alignment would read this as someone speaking his language. The email never explains what IaC drift is; it describes the specific failure mode (static IaC checks running on a different cadence than the cluster's actual change rate) and trusts the reader to fill in the operational context. This is the right level for a practitioner-introvert. The Transilience sentence names three specific domains (IAM, secrets, network policy) rather than making a general claim. The CTA ("Has declared-vs-effective checking been pulled into the deploy pipeline, or is it still incident-driven?") is a real engineering question with a binary shape that invites a substantive answer. It is the strongest CTA of the four drafts.

### What fails

The opener -- "The FunnelFox launch absorbed six PSP integrations into a self-hosted Kubernetes cluster in twelve days" -- is factually identical to information already carried in Drafts 1 and 2. While Artem would not see those drafts, if anyone at Adapty forwards or discusses these emails internally, the shared opener fact creates a templating signal. This is a minor risk given the four emails go to different people, but it is worth noting under the cross-draft section below.

### Per-draft question: Does "Has X been pulled into the deploy pipeline, or is it still incident-driven?" land as a real engineering question?

Yes. This is the operational question that an infrastructure team lead running self-hosted k8s would have a specific answer to. It is not a trick question or a leading question; it names a real architectural decision point. The binary framing (pipeline vs. incident-driven) is how engineers actually categorize this choice. It invites a response because the answer reveals something about their operational maturity, and practitioners enjoy demonstrating operational maturity.

---

## V2 review round -- 2026-04-30 (appended)

**Context:** Three drafts were rewritten to address prior-round flags. Artem v1 already shipped and is included only for cross-comparison. This review verifies the three specific fixes, evaluates each v2 draft independently, and scans for new cross-draft fingerprints.

---

### Kirill v2 -- fix verification

**Fix applied:** Dropped "continuous" from product sentence.

**Prior v1 product sentence (reconstructed):** "Transilience extends that reliability surface to control-plane state, continuous, human-in-the-loop on remediation."

**Current v2 product sentence:** "Transilience extends that reliability surface to control-plane state, with humans in the loop on remediation."

**Verdict on fix:** Clean. "Continuous" is gone. The sentence is tighter without it -- "extends that reliability surface" is inherently an ongoing operation; the word was redundant. The remaining clause ("with humans in the loop on remediation") does more work for a CPO/CTO's decision calculus than "continuous" ever did, because a builder-founder cares about whether automation is autonomous or supervised. Substance carries the meaning without the word.

**Per-draft verdict: ship**

No new problems introduced. The draft that was clean enough to ship in v1 is marginally better in v2. The "frame more than a slogan" blemish noted in v1 remains, but it was non-blocking then and is non-blocking now.

---

### Gregory v2 -- fix verification

**Fixes applied:** (1) Replaced "in twelve days" with "after the FunnelFox launch." (2) Replaced "continuously baselined" with "baselined live."

**Fix 1 -- "twelve days" removal:**

Prior v1 opener: "Six PSPs absorbed into a self-hosted k8s cluster in twelve days is the kind of integration where..."

Current v2 opener: "Six PSPs absorbed into a self-hosted k8s cluster after the FunnelFox launch is the kind of integration where..."

The temporal anchor is replaced with the event anchor. "After the FunnelFox launch" does different work: it ties the integration to a specific, named trigger rather than emphasizing speed. For Gregory -- a Head of Development who would have lived through the FunnelFox integration as an operational event, not as a speed metric -- the event anchor is actually a better fit. The prior round recommended this exact change ("preferably Draft 2, where it is least load-bearing"), and it was the right call. Cross-draft "twelve days" count drops from 3/4 to 2/4. Clean.

**Fix 2 -- "baselined live" swap:**

Prior v1: "continuously baselined"

Current v2: "baselined live"

"Baselined live" is more precise engineering vocabulary. In infrastructure contexts, "live" means against running state (as opposed to against a snapshot or a declaration). This communicates that the baseline is computed from live cluster state, not from a static artifact. A Head of Development running self-hosted k8s would parse this immediately. Clean swap. No ambiguity introduced. Cross-draft "continuously" count drops from 4/4 to 2/4.

**Full v2 text review:**

The dense opener clause ("accretes faster than anyone declares a baseline against") remains from v1. It was flagged as the weakest link then -- syntactically heavy for its meaning. It is still the weakest link now. But it was non-blocking for a reader with Gregory's technical fluency, and it remains non-blocking. The oack.io parenthetical is still the strongest move across all four drafts. "Additive to whatever observability already runs" is a clean, non-decorative phrase that positions correctly.

**Per-draft verdict: ship**

Both fixes land cleanly. No new problems introduced. The dense opener clause is a known blemish, not a structural failure.

---

### Vitaly v2 -- fix verification and full re-evaluation

**Fixes applied:** (1) Dropped "at enterprise altitude." (2) Reshaped sentence 2 from assertion to conditional probe.

**Fix 1 -- "at enterprise altitude" removal:**

The phrase is gone. No trace of altitude metaphors anywhere in v2. Clean.

**Fix 2 -- conditional probe:**

Prior v1 sentence 2 (from review): "The deals that stall here aren't about whether SOC 2 exists -- they're about the speed at which a buyer-side security review can match..."

Current v2 sentence 2: "If those questions are slowing the cycle -- or pulling engineering out of roadmap to assemble answers -- the issue is usually less SOC-2-existence and more match-speed between procurement and platform reality."

The structural change is the "If" conditional. The v1 version declared Vitaly's reality to him ("The deals that stall here..."). The v2 version proposes a hypothesis: *if* this is happening, *then* the issue is usually X. The "usually" adds epistemic humility -- the writer is describing a common pattern among companies entering enterprise, not diagnosing Adapty specifically.

Does this land as inquiry or still as projection? It lands as inquiry-adjacent. The conditional frame does not assert that questionnaires are slowing Vitaly's deals -- it invites him to recognize whether the pattern applies. The "or" construction ("slowing the cycle -- or pulling engineering out of roadmap") gives him two entry points to self-identify, rather than a single declaration to accept or reject. This is materially better than v1.

One residual concern: "pulling engineering out of roadmap to assemble answers" is still specific about an internal dynamic. The research showed Vitaly hiring a VP of Sales and Head of Growth, which makes enterprise motion plausible but doesn't evidence engineering-pull specifically. However, the conditional frame converts this from assertion to hypothesis. For a 120-person company with no dedicated security hire, the scenario that engineering handles security questionnaires is near-universal -- it is less projection and more structural inevitability at this company size. The conditional softens it enough. Acceptable.

**Full v2 text review:**

Sentence 1 is unchanged and remains strong. "The price/convert/change frame from your foreword has a fourth member that lands in close-cycle: the security questionnaire" -- this is the right anchor for a CEO who published that framing recently. It demonstrates reading, not Googling.

Sentence 3: "With Transilience handling that layer continuously, the answer comes from platform state rather than artifacts assembled for the deal." The word "continuously" remains (2/4 cross-draft, now acceptable). "Artifacts assembled for the deal" is precise commercial language -- it names the specific pain of manually composing security documentation per-deal, which is real friction for a company entering enterprise without a security team. This sentence earns its place.

CTA: "Where does that loop sit between sales and engineering today?" Open question, distinct from the other three CTAs. "That loop" refers back to the security-questionnaire/deal-cycle dynamic without re-explaining it. The word "today" is a temporal anchor that makes the question current without being pushy. The CTA is proportional to what the email has earned.

**Mood and posture:** Warm-observational, commercially framed. Advisor-adjacent posture. The v2 holds this consistently -- the conditional probe in sentence 2 actually strengthens the advisor posture because advisors hypothesize rather than diagnose. The mood fits a storyteller-founder who thinks in commercial frames.

**Per-draft verdict: ship**

The two fixes resolve both prior-round failures. "At enterprise altitude" is gone. The projection is converted to a conditional probe that earns the right to suggest without asserting. The email now earns its existence: it brings a genuinely new frame (the fourth variable in Vitaly's own published model), it demonstrates reading rather than Googling, and it asks a proportional question. A CEO receiving this email would recognize that the writer read the foreword and extended its logic. That is worth fifteen seconds.

---

### Cross-draft fingerprint verification (v2 round)

**1. "Twelve days" distribution:**

| Draft | Present? |
|-------|----------|
| Kirill v2 | Yes -- "Twelve days from the antitrust ruling..." |
| Gregory v2 | No -- replaced with "after the FunnelFox launch" |
| Vitaly v2 | No -- was never present |
| Artem v1 (shipped) | Yes -- "in twelve days" |

2/4 drafts. Acceptable. Two separate recipients receiving the same factual anchor is normal research overlap, not a campaign signal. Prior-round flag resolved.

**2. "Continuously" / "continuous" distribution:**

| Draft | Present? | Form |
|-------|----------|------|
| Kirill v2 | No -- dropped from product sentence | -- |
| Gregory v2 | No -- swapped to "baselined live" | -- |
| Vitaly v2 | Yes | "handling that layer continuously" |
| Artem v1 (shipped) | Yes | "reconciles...continuously" |

2/4 drafts. Down from 4/4. Prior-round flag resolved. 2/4 is acceptable density for a word that describes the product's actual operating mode.

**3. "Six PSPs" / "six PSP integrations" distribution:**

| Draft | Present? |
|-------|----------|
| Kirill v2 | Yes -- "six PSPs integrated" |
| Gregory v2 | Yes -- "Six PSPs absorbed" |
| Vitaly v2 | No -- references "FunnelFox, Adapty Mail, and the upscale tier" instead |
| Artem v1 (shipped) | Yes -- "six PSP integrations" |

3/4 drafts. Unchanged from prior round. This was assessed as acceptable previously -- the PSP count is the operational fact that makes the trigger concrete, and each draft uses it for a different analytical purpose. Remains acceptable.

**4. "FunnelFox" distribution:**

| Draft | Present? |
|-------|----------|
| Kirill v2 | Yes |
| Gregory v2 | Yes (newly added -- "after the FunnelFox launch") |
| Vitaly v2 | Yes |
| Artem v1 (shipped) | Yes |

4/4 drafts. This is the company trigger -- the event that makes all four emails timely. 4/4 is expected and acceptable; it would be suspicious if any draft did not mention it. Not a fingerprint.

**5. New phrasal echo -- "is the kind of":**

Kirill v2: "is the kind of execution that makes..."
Gregory v2: "is the kind of integration where..."

This construction appears in 2/4 drafts, both in the opening sentence. It existed in v1 and was not flagged. Now that other fingerprints have been cleaned up, it becomes more visible as a residual seam. However, 2/4 is below the threshold that would register as coordinated. The phrases serve different analytical functions (execution vs. integration) and would only be noticed if someone placed the two emails side by side and read the first sentences together. Mild risk. Non-blocking.

**6. Terminal time-words in CTAs:**

| Draft | CTA terminal phrase |
|-------|-------------------|
| Kirill v2 | "...have today?" |
| Gregory v2 | "...at the cluster level?" |
| Vitaly v2 | "...and engineering today?" |
| Artem v1 (shipped) | "...or is it still incident-driven?" |

"Today" appears in 2/4 CTA endings (Kirill, Vitaly). "Currently" appeared in Gregory v1 but is now gone from his CTA. This is a mild echo, unchanged from prior round (which noted "currently"/"today" as near-synonym terminals). 2/4 is below the coordinated-campaign threshold. Non-blocking.

**7. Structural pattern -- 4-sentence shape:**

All four drafts follow: opener -> analysis -> product sentence -> question CTA. This is a genre convention for cold emails to senior technical buyers, not a templating artifact. Noted in prior round; unchanged. Non-blocking.

**8. No new fingerprints detected.** The three fixes were surgical -- they resolved the flagged problems without introducing new cross-draft echoes. "Baselined live" is unique to Gregory. "After the FunnelFox launch" is unique to Gregory (others use "FunnelFox" differently). "With humans in the loop on remediation" is unique to Kirill. The conditional "If those questions are slowing the cycle" is unique to Vitaly.

---

### Updated cross-draft mood and posture table

| Draft | Mood | Posture | Fit | Change from v1 |
|-------|------|---------|-----|----------------|
| Kirill v2 | Warm-precise, respectful of builder doctrine | Peer-who-did-the-reading | Correct | Product sentence tighter without "continuous" |
| Gregory v2 | Dry-precise, operationally grounded | Practitioner-to-practitioner | Correct | "Baselined live" more precise; "after FunnelFox launch" better event anchor |
| Vitaly v2 | Warm-observational, commercially framed | Advisor-adjacent | Correct | Conditional probe fixes the projection; advisor posture is now consistent |
| Artem v1 | Dry-precise, architecturally specific | Engineer-to-engineer | Correct | Shipped; no change |

---

## Updated summary verdicts (v2 round)

| Lead | Prior verdict | Current verdict | Key change |
|------|--------------|-----------------|------------|
| Kirill Potekhin | **ship** | **ship** | "Continuous" dropped; product sentence tighter. "Frame more than a slogan" blemish remains, non-blocking. |
| Gregory Komissarov | **ship** | **ship** | "Twelve days" replaced with event anchor; "baselined live" cleaner than "continuously baselined." Dense opener clause persists, non-blocking. |
| Vitaly Davydov | **rewrite** | **ship** | Both prior-round failures resolved. "Enterprise altitude" gone. Projection converted to conditional probe. Email now earns its existence. |
| Artem Davydov | **ship** (shipped) | **ship** (shipped) | No change. Included for cross-comparison only. |

### Cross-draft resolution summary

All three prior-round cross-draft flags are resolved:

1. **"Twelve days" x3 -> x2.** Gregory's swap to "after the FunnelFox launch" reduced the count to acceptable levels. The remaining two instances (Kirill, Artem) serve different analytical functions and would not register as coordinated.
2. **"Continuously" x4 -> x2.** Kirill dropped it; Gregory swapped to "baselined live." The remaining two instances (Vitaly, Artem) are acceptable density for a word that describes the product's actual operating mode.
3. **Vitaly projection -> conditional probe.** The structural failure that triggered the rewrite verdict is resolved. The email no longer declares Vitaly's reality to him.

**Residual non-blocking observations:**
- "Is the kind of" appears in Kirill and Gregory openers (2/4). Mild seam. Would only surface if someone placed the two emails side by side.
- "Today" appears in 2/4 CTA endings. Mild echo. Below coordinated-campaign threshold.
- Dense syntax in Gregory's opener clause persists. Non-blocking for this reader's technical fluency.

**Overall assessment:** The four-draft set is clean enough to ship. The fixes were surgical and effective. No new fingerprints were introduced. The residual seams are at a level that would not register to individual recipients, and would require deliberate side-by-side comparison to detect even within the company. The set reads as four independently motivated emails from someone who did the work on each recipient, not as four outputs of a campaign template.
