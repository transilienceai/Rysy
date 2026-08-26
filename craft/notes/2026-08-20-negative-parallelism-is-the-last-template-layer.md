---
date: 2026-08-20T00:00:00Z
campaign_id: 2026-07-23-transilience-insurtech-health-payments
lead_id: (set-level — all ten)
tags: [ai-tells, wikipedia-signs, negative-parallelism, recency, anchors, humanize]
status: hypothesis
---

# What I noticed

After two full de-templating rounds (see [[2026-08-13-batch-convergence-survives-synonym-rotation]]), the human reviewer still read the set as AI-ish and pointed at Wikipedia's "Signs of AI writing" page. Auditing against that list found the residue precisely: **negative parallelism** — "It's not X, it's Y" / "not just X" / "X, not Y" — appeared roughly fifteen times across ten emails, at least once in every email, even though vocabulary, em-dashes, sentence counts, and product-sentence architecture were all already clean. The contrast frame is the deepest tell because it *feels* like rhetoric rather than template — every instance individually reads as craft; the density across a set reads as machine.

The fix that held: a **budget, not a ban**. Four instances survived, each thesis-critical (mPulse's "The certs aren't the problem; the seam is"; Pulse's "show the state, not the certificate"; REPAY's workflow/state and finding/changing pair). Everything else was recast as direct positive assertion ("Call it what it is: a sales tax" instead of "That's not a compliance gap; it's a sales tax") — and the witness confirmed the recasts kept their snap. Rule-of-three lists went to zero the same way (pairs or asymmetric enumeration).

The second half of the round: **recency is the humanity signal that can't be faked by style.** Three researcher sweeps re-verified all ten prospects in-role and produced dated July–August anchors for seven emails (a ten-day-old earnings call detail, a three-week-old CMS report with its own quotable phrase, a company podcast quote, a trade-conference booking, a pricing page). The set-level witness's verdict on the human test: the research specificity was "too varied in kind to read as automated." Style removes suspicion; fresh, woven, correctly-attributed specifics create belief.

One boundary held on principle: an unconfirmed ransomware claim against a prospect's parent company (posted by the threat actor, under law-firm investigation, unacknowledged by the company) was found and **excluded**. Unverified incidents are never anchors — referencing one is fear-mongering plus potential amplification of a false claim, and a 25-year ISO would smell the ambulance-chase instantly.

## Evidence

- Wikipedia lint before/after: negative parallelism ~15 → 4 budgeted; triples 3 → 0; AI vocab 0 → 0 (already clean); audit scripts in session log 2026-08-20
- set-review-v6.md (ship-with-flags; human-test verdict), witness-fivepack-v6-A/-B.md, witness-v7-bloom-spoton.md
- Per-lead recency files: experience/prospects/*/recency-2026-08-13.md

## Hypothesis

(1) De-templating proceeds in layers — vocabulary → phrase → architecture → *rhetorical figure* — and negative parallelism is the last layer; lint for it explicitly with a budget of one instance per ~3 emails, thesis-critical only. (2) A recency sweep (personal shares + company news + role confirmation, ≤1 month old) should precede every wave as a standing step; an email whose anchor is a month stale reads researched, an email whose anchor is a week old reads *attended to*. (3) Proposed for human approval: add the unambiguous Wikipedia vocabulary ("delve", "tapestry", "underscores", "showcasing", "fostering", "moreover", "furthermore", "stands as a testament", etc.) to `ai_tells.py` HARD_BLOCKS — per that file's own contract, additions are human-approved, so this is a proposal, not an edit.
