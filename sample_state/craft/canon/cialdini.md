# Cialdini

## Background

Robert Cialdini is a social psychologist whose 1984 book *Influence: The Psychology of Persuasion* — and its 2016 successor *Pre-Suasion* — are the closest thing the field has to a unified theory of why people say yes. Cialdini's contribution was to take a sprawling literature on social influence and compress it into a small set of named principles that practitioners could actually apply. His writing is unusually disciplined for a psychologist's: every claim is backed by a study, and the studies are described concretely.

## Core contributions

**Reciprocity.** People feel an obligation to return what was given. Applied to cold outreach: if the email gives something — a useful observation, a connection, a reframe — before asking, the reply rate climbs. The gift has to be real (Cialdini is explicit: cosmetic gifts trigger reactance, not reciprocity).

**Commitment and consistency.** People want to be consistent with their previous commitments and stated positions. Applied: anchoring an email on something the prospect has *already publicly said* (a post, a talk, a quoted view) gives them a stake in continuing the thread. Asking them to reverse a public position is uphill; building on one is downhill.

**Social proof.** People look at what similar others are doing as a guide for their own behavior. Applied: peer-company references are powerful, but only when the peer is genuinely peer (same stage, same sector, same problem). Generic logo lists are not social proof; they are noise.

**Authority.** People defer to credentials, especially in domains where they are uncertain. Applied: the sender's earned credentials matter more than the sender's claimed warmth. A cold email from someone with relevant expertise opens differently than a cold email from someone without it. This is one reason `sender.credible_claims` is a first-class field in the JSON contract.

**Liking.** People say yes more often to people they like, and liking is driven by similarity, compliments (sincere), and cooperation. Applied: the email finds *real* common ground (similarity), offers *specific* recognition (sincere compliments), and frames the ask as collaborative (cooperation). All three components have to be sincere; insincere versions trigger the opposite reaction.

**Scarcity.** People value what is rare or about to be unavailable. Applied to cold email: scarcity is *the* most-abused principle in vendor outreach (*"only 3 spots left in our pilot!"*) and almost always misfires when manufactured. Real scarcity — a real cohort, a real expiring window — works; fake scarcity damages credibility for the entire campaign.

**Unity (added in *Pre-Suasion*).** People say yes to those they share an identity with. Applied: shared identity is more powerful than shared interest. *We both came up through detection engineering* lands harder than *we both work in security*.

## How Vendy uses these

Cialdini's principles are structural, not tactical. Vendy does not write emails *applying* Cialdini's principles like a checklist; she writes emails that are *consistent* with how persuasion actually works, which Cialdini happens to have described accurately.

Specifically:
- The opener almost always relies on **commitment and consistency** — anchoring on something the prospect has already said publicly
- The CTA is calibrated by **reciprocity** — what was offered determines what can be asked
- Peer references when used are scrutinized for **real social proof** vs. logo theatre
- The sender's credibility is supplied via `credible_claims` — **authority** without bluffing
- **Scarcity** is rarely deployed; when it is, it must be real

## Where the frame is wrong or limited

Cialdini's principles are descriptions of human tendency, not levers. Treating them as levers — "I will now apply social proof to manipulate this prospect" — produces outreach that *feels* manipulative even when it isn't, because the writer's posture leaks through. The principles work when the writer is *aware of* them but not *applying* them; when they are baked into a respectful default, not deployed as tactics.

Cialdini also says little about written form. His evidence base is mostly verbal and face-to-face. The application to cold email requires translation — and the translation has been done badly by a generation of sales trainers who turned his principles into scripts.

## Recommended further reading

- *Influence* (the original 1984 edition is denser; the 2007 expanded edition adds examples)
- *Pre-Suasion* (2016) — on what to do *before* the persuasive act, which maps directly to research and trigger-event detection
- His response to the social-engineering literature (post-2010 papers on backfire effects) — for the limits of his own principles
