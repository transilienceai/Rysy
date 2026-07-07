"""
ai_tells.py

The canonical hard-block list of AI tells. Used by the
pre-write-tell-detector hook to deterministically reject drafts that
contain the most-recognizable template phrases.

This list is intentionally *exclusive* — every entry has been observed in
the wild as a high-frequency tell. The probabilistic witness sub-agent
catches the broader, fuzzier set; this list is the floor below the floor.

Adding entries: a phrase joins this list only after it has been recognized
across multiple campaigns as a genuine giveaway. The list is human-approved.
The list intentionally does NOT enumerate every awkward phrase — that
would be the witness's job.

See craft/cold-email/ai-tells-graveyard.md for the full discussion of why
each entry is here and how the broader probabilistic set differs.
"""

HARD_BLOCKS = [
    # Generic openers — universal AI cold email signature
    "i came across your profile",
    "i came across your work",
    "came across your profile",
    "i hope this email finds you well",
    "i hope this finds you well",
    "hope this email finds you well",
    "hope you're having a great week",
    "hope you're doing well",

    # Filler intentions
    "just wanted to reach out",
    "just wanted to share",
    "just checking in",
    "just touching base",
    "i wanted to reach out because",
    "i'm reaching out because",
    "wanted to introduce myself",

    # Subject line graveyard (when used in body openers)
    "quick question",

    # Filler praise
    "loved your post",
    "loved your talk",
    "loved your thread",
    "fascinating insights",

    # Generic value claims (also in subject lines)
    "industry-leading",
    "best-in-class",
    "cutting-edge",
    "game-changing",
    "synergy",
    "synergies",

    # Filler closes
    "looking forward to hearing from you",
    "looking forward to your reply",
    "awaiting your response",
    "let me know if you'd like to chat",
    "would love to connect",
    "would love to learn more about",
    "happy to hop on a quick call",

    # Manufactured urgency
    "limited time",
    "before it's too late",
    "last chance",

    # The hostile follow-up tell
    "i'll follow up next week if i don't hear back",
    "i'll follow up if i don't hear",
]


def normalize(text: str) -> str:
    """Lowercase + collapse whitespace, for matching."""
    return " ".join(text.lower().split())


def find_hits(text: str):
    """
    Return list of (phrase, position) for each hard-block phrase found in text.
    Position is the index in the original (lowercased) text.
    """
    text_l = text.lower()
    hits = []
    for phrase in HARD_BLOCKS:
        pos = text_l.find(phrase)
        if pos != -1:
            hits.append((phrase, pos))
    return hits


if __name__ == "__main__":
    # Quick smoke test
    sample = "I came across your profile and I'm reaching out because we have synergy."
    hits = find_hits(sample)
    print(f"Found {len(hits)} hits in sample text:")
    for phrase, pos in hits:
        print(f"  - '{phrase}' at position {pos}")
