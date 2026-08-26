# Persuasion frameworks — overview

The persuasion frameworks Rysy uses are not deployed as tactics; they are baked into the default posture of how she writes. This overview file maps the relevant frameworks to the specific moves Rysy makes and to where each is operationalized.

## The frameworks in scope

**Cialdini's principles** (reciprocity, commitment/consistency, social proof, authority, liking, scarcity, unity). Documented in `craft/canon/cialdini.md`. Applied per-persona in the persona-specific files in this directory.

**Loss aversion** (Kahneman, Tversky). People weight losses more heavily than equivalent gains. Documented in `loss-aversion-for-ciso.md` because it is the framework most reliably useful for security-side personas, where the buyer's mental model is *risk-first*.

**Peer proof** (a refinement of Cialdini's social proof). What matters is not that *anyone* is doing the thing, but that *peers* are — same stage, same sector, same problem. Documented in `peer-proof-for-cto.md` because the CTO archetype most reliably engages with peer-stage references.

**Time-to-value** (a pragmatic framework for engineering buyers). The buyer's mental model is *how long until this becomes useful*, and the time horizon is short. Documented in `time-to-value-for-vp-eng.md`.

**Pre-suasion** (Cialdini, 2016). The state the reader is in *before* they read the persuasive move shapes the move's effectiveness. Embedded throughout — the trigger event in research, the subject line, the temperature of the opener — all are pre-suasion moves.

## Why frameworks live in `craft/`, not `self/`

Frameworks are *learned tools*, not constitutional. They evolve as Rysy's understanding evolves. They can be revised by evidence, extended by application, and corrected by counter-cases. This is why they live in `craft/psychology/` rather than embedded in `self/character.md`.

Rysy's character does not contain the names of the frameworks. It contains the *posture* that makes the frameworks work — respect for the reader, honesty about what is being offered, the discipline of not letting wanting corrupt the work. The frameworks describe how persuasion functions; the character describes how to use that knowledge ethically.

## Application discipline

The frameworks should not appear *named* in any draft. *I want to apply social proof here* is not a useful drafting thought; *what would a thoughtful peer cite as evidence* is. The framework is a way of understanding what works; the doing is craft.

The witness does not check drafts against frameworks by name. It evaluates whether the draft earns its claim on the reader's attention — and frameworks are useful primarily as diagnostic tools after-the-fact (*this opener landed because it anchored on commitment-consistency*), not as construction templates.

## How frameworks are extended

When Rysy reads a piece of canon (Cialdini, a paper, a practitioner thinker) that introduces a new framework or refines an existing one, she takes a craft note. If the framework recurs in three or more notes with operational utility, it can be promoted to its own psychology file via the standard promotion path.

## Persona-specific files in this directory

- `loss-aversion-for-ciso.md` — risk-first framing for security-side personas
- `peer-proof-for-cto.md` — credible peer references for technical leaders
- `time-to-value-for-vp-eng.md` — short-horizon ROI framing for operational engineering leaders
