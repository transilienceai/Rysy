# tests/tell-detector/

Test cases for the deterministic AI-tell detector at `.claude/hooks/pre-write-tell-detector.py`.

## Structure

```
tests/tell-detector/should-block/
├── case-001.md   # contains a hard-blocked phrase; expected: blocked
tests/tell-detector/should-pass/
├── case-001.md   # clean; expected: passes through
```

## When to run

- Before adding entries to `HARD_BLOCKS` in `.claude/lib/ai_tells.py`
- After any change to the detector logic
- Occasionally to confirm regex patterns still catch what they should

## Pass criterion

100%. The detector is deterministic — every case must produce the expected outcome. Misses indicate a bug; the detector is the floor below the floor and must be reliable.

## Initial state

Empty. Seed with the first 10-20 examples from `craft/cold-email/ai-tells-graveyard.md` as Vendy comes online.
