# AI tells graveyard

Phrases, constructions, and rhythms that mark a cold email as machine-produced or template-driven. The deterministic tell-detector at `.claude/lib/ai_tells.py` enforces a subset of these as hard blocks. The witness flags the rest probabilistically.

## Hard-blocked phrases

These trigger the `pre-write-tell-detector.py` hook and prevent a draft from being written. They are listed in `.claude/lib/ai_tells.py` and any draft containing them is rejected before the witness even sees it.

- *I came across your profile*
- *I came across your work*
- *I hope this email finds you well*
- *I hope this finds you well*
- *Just wanted to reach out*
- *Just wanted to share*
- *Just checking in*
- *Quick question*
- *I wanted to reach out because*
- *I'm reaching out because*
- *Hope you're having a great week*
- *Hope you're doing well*
- *I noticed you* (when followed by a generic observation)
- *Saw that you* (same caveat)
- *Congrats on* (when not followed by something specific)
- *Hope this is helpful*
- *Looking forward to hearing from you*
- *Let me know if you'd like to chat*
- *Would love to connect*
- *Would love to learn more about*

## Probabilistic tells (witness-flagged)

These don't trigger automatic blocks but degrade quality. The witness flags emails containing patterns of them.

**Filler openers that aren't quite phrases:**
- Any sentence starting with *I* if it can be reworded to start with the subject
- Any opener whose first six words are about the writer
- *As a* clauses for credentialing the writer at the start

**The praise-without-specifics pattern:**
- *Loved your post* / *Loved your talk* / *Loved your thread* (without a specific reference)
- *Fascinating insights*
- *Great content*
- *Thought leadership* (this phrase, in any context)

**Filler bridges:**
- *That said*
- *With that in mind*
- *Curious to hear your thoughts*
- *Would love to get your perspective*
- *Wanted to pick your brain*

**Generic value claims:**
- *Help you scale*
- *Help you grow*
- *Increase your productivity*
- *Reduce your costs*
- *Drive results*
- *Unlock value*
- *Synergy* (in any form)
- *Game-changing*
- *Cutting-edge*
- *Best-in-class*
- *Industry-leading*

**Manufactured urgency:**
- *Limited time*
- *Quick turnaround*
- *Time-sensitive*
- *Before it's too late*
- *Last chance*

**The CTA flailing patterns:**
- *Are you the right person to talk to about this?*
- *If not you, who would be?*
- *Worth a quick chat?* (the *quick* is the tell)
- *Got 15 minutes?*
- *Open to a brief call?*

**Sign-offs that imply continuation:**
- *Looking forward to your reply*
- *Awaiting your response*
- *I'll follow up next week if I don't hear back* (this in particular is a hostile move)

## Constructions to avoid

Beyond specific phrases, certain constructions read as machine-generated:

- **Three-part lists in any sentence.** *We help you increase X, decrease Y, and optimize Z.* Real prose rarely has the symmetry of generated lists.
- **Sentences that begin with the same word in adjacent paragraphs.** Hallmark of templated structure.
- **First-name overuse.** *Hi {name}, I noticed {company}'s recent... I think {name}, you would find...* — using the prospect's name more than once in five sentences.
- **The em-dash overuse.** AI-generated text often over-uses em-dashes for rhythm. Two em-dashes in five sentences is the upper limit.
- **The double-question opener.** *How are you handling X? And what's your perspective on Y?* Reads as stalling.
- **Clauses about *helping*.** *I'd love to help you with...* / *We help companies like yours...* — the word *help* in this construction reads as vendor-coded.

## Why these matter

Each individual tell is a small thing. A draft might survive any one of them. But the *combination* of two or three is unmistakable to a reader who has seen ten thousand cold emails — which describes most of the prospects Vendy is writing to. The deterministic block on the worst phrases prevents the most-recognizable tells; the witness's probabilistic review catches the more subtle accumulation.

The goal is not to write differently from a machine; the goal is to write specifically and honestly enough that the question never arises.

## How this list grows

When a new tell becomes recognizable enough to flag (a phrase that has been picked up across the cold-email industry, a construction that has become a giveaway), Vendy proposes adding it via a craft note. Promotion to the hard-block list (the Python file) is human-approved; promotion to the probabilistic list is autonomous after evidence.
