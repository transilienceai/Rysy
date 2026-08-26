# Filter criteria — separating trend from noise

The filter is the single most important judgment in this skill. A topic that passes the filter shapes how Rysy frames every email this quarter. A topic that should have been dropped but wasn't pollutes her thinking.

## The four criteria

### 1. Independent sources (≥3 unaffiliated)

A "source" is independent only if it has its own editorial voice and audience. Three vendor blogs syndicating the same press release counts as ONE source. Three different newsletters from different authors covering the same event counts as three.

How to verify:
- Check whether sources cite each other (cascading citation = same source)
- Check whether sources are owned by the same parent company (TechCrunch + The Information are independent; both being cited by the same author is one source)
- Check whether the language is independently formulated or echoed

### 2. Behavioral signal (not just opinion)

Real trends produce behavior. Opinion-only "trends" are commentary. Behavioral signals include:
- Hiring (companies posting roles tagged to the trend)
- Building (open-source projects gaining contributors and stars)
- Presenting (conference agendas reflecting the topic)
- Complying (regulatory deadlines forcing action)
- Buying (RFPs, vendor evaluation activity)

If the topic is purely "people are talking about X" without anyone DOING anything about X, it has not yet earned trend status.

### 3. Time depth (≥2 weeks)

Topics that flare for one news cycle and disappear are not trends. Verify:
- The topic has appeared in at least one source from each of the last 2 weeks
- The topic's volume has not collapsed to zero in the most recent week
- The topic was not seeded by a single PR push that has since faded

### 4. Practitioner voice (≥1)

The most-abused trends in the cold-email industry are the ones where vendors and analysts are the only voices. A real trend has at least one practitioner — a CISO, CTO, VP Eng, VP Security, or comparable operator — engaging substantively. "Substantively" means a thoughtful comment, post, talk, or quote that shows operational reality, not a one-line reaction.

## Edge cases

**Major incident in the last 48 hours.** Time depth criterion is the bottleneck. Surface as a candidate but not yet a confirmed trend. Note in the run report.

**Regulation with a future-dated deadline.** Behavioral signal may be slow to materialize but the deadline is real. Treat as trend if practitioners are *preparing* (compliance hires, talks on prep) even if compliance behavior isn't visible yet.

**A trend that was active and is now declining.** Drop from current.md but keep in archive. The disappearance is itself a useful signal for next refresh.

**Vendor-driven topics.** The "AI-powered everything" cycle of any given year is the canonical example. If the only voices are vendors and the analysts they fund, drop, regardless of volume.

## What to log when dropping

For every dropped topic, log:
- Topic name
- Failure criterion(ia)
- One-line evidence summary
- Whether to revisit next refresh

This audit trail is what makes the skill defensible. A trends file with no dropped-topic log is unfalsifiable.
