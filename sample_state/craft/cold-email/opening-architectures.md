# Opening architectures

The structure of a cold email's opening — not just the first sentence but the first two or three — shapes whether the rest of the email gets read. There are a small number of architectures that work for senior-buyer outreach. This is a working catalogue.

## The signal-to-question architecture

Most reliable. Two sentences:
1. A specific observation about the reader (the signal)
2. A question that takes the observation seriously (the question)

The signal proves the writer has done the work. The question gives the reader something to do with their attention. The body either expands on the question's premise or pivots to a related insight.

Example:
> The 8-K language on the Acme incident this month was unusually specific about detection latency. Curious whether your current SOC tooling reports that metric the same way the disclosure implies.

Why it works: signal is specific, question is real, the writer's expertise is implied (knowing what 8-K language usually looks like), the *why now* is built in (this month).

## The triangulation architecture

For the diagnostic-pattern register. Three or four sentences:
1. *N* signals listed (usually three, sometimes four)
2. Named pattern those signals form
3. Hypothesis or question

The triangulation is the credibility move. No single signal would carry the email; the pattern across signals does.

Example:
> Three signals from your last quarter — the platform-team headcount ramp, the *infrastructure debt* mention in your QBR, and the director-of-platform job posting that lists migration experience as a primary requirement — all point at the same problem. The thesis I want to test with you, not pitch you on, is that you're under-resourced on the migration itself, not on the migration plan.

Why it works: the signals are independent, the pattern is plausible, the framing (*test with you, not pitch you on*) declares the writer's posture explicitly.

## The connection architecture

For the warm-observational register. Two or three sentences:
1. Specific reference to something the reader has written or said (the anchor)
2. The writer's adjacent thought (the connection)
3. (Sometimes) the question or invitation

The connection is the load-bearing move. It must be a thought *adjacent* to the anchor, not a paraphrase of it. The reader should think *yes, and I hadn't quite seen it that way*.

Example:
> Your post on detection-as-code last month had a line that has stuck with me — *we keep writing rules for the last breach.* Half the security industry is now in that bucket and won't admit it. The corollary I keep wondering about is whether the same is true for our threat models.

Why it works: the anchor is specific (named line, named post), the connection extends rather than restates, the writer offers something for the reader to react to.

## The trigger-anchored architecture

Two sentences. The trigger event is the *why now*; the second sentence does the work the opener would normally do.

Example:
> The SEC's first major enforcement under the cyber disclosure rule came down last week, and the language in the order is meaningfully more aggressive than the original guidance suggested. Wondering whether the GC and CISO conversations at companies like yours have shifted in tone this week.

Why it works: trigger is real and recent, the question takes the trigger seriously, the writer assumes the reader is engaged with this conversation rather than explaining it.

## The recognition architecture

For the peer-enthusiast register. Two sentences:
1. The specific detail that signals the writer noticed
2. The hypothesis or question about the detail

Example:
> The thing that stood out in your launch yesterday wasn't the headline — it was that you shipped the SDK and the documentation in the same release. Almost no one does that. Curious whether that was intentional or whether you just got lucky on timing with the docs team.

Why it works: the detail is non-obvious, the recognition is grounded, the question opens a real conversation rather than asking the reader to perform.

## What architectures *don't* work

- The two-paragraph anything for first contact (too long; reader bails)
- The opener-as-thesis-statement (*"I think most CISOs are missing X"*) — sounds like a vendor narrative
- The biographical opener (*"As a former engineer at..."*) — flips attention from reader to writer
- The fake-question opener whose answer is obvious (*"How important is security to your company?"*)
- The interruption opener (*"Hope I'm not catching you at a bad time"*) — guarantees an interruption posture

## How architecture choice connects to register

Architecture and register are not independent. Some pairings are natural:

- Signal-to-question + dry-precise: the canonical CISO opening
- Triangulation + diagnostic-pattern: the canonical structured-thinker opening
- Connection + warm-observational: the canonical builder-CTO opening
- Recognition + peer-enthusiast: the canonical founder/builder opening

Mixing across the natural pairings is possible but harder. A triangulation in warm-observational register is unusual but can work; a recognition in dry-precise feels off because dry-precise mutes the warmth that recognition needs.

## What the witness checks

The witness identifies which architecture the draft is using and asks:
- Does the draft execute that architecture cleanly, or is it muddled across two?
- Does the architecture match the chosen register?
- Does each sentence in the architecture earn its place, or is one redundant?
