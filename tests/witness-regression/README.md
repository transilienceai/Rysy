# tests/witness-regression/

Drafts the witness should ship, rewrite, or flag. Used to verify the witness sub-agent retains calibration over time.

## Structure

```
tests/witness-regression/should-ship/
├── case-001/
│   ├── brief.md
│   ├── portrait.md
│   ├── draft.md
│   └── expected-verdict.md   # "ship" + reasoning
tests/witness-regression/should-rewrite/
├── case-001/
│   ├── brief.md
│   ├── portrait.md
│   ├── draft.md
│   └── expected-verdict.md   # "rewrite" + the specific issue
tests/witness-regression/should-flag/
├── case-001/
│   ├── brief.md
│   ├── portrait.md
│   ├── draft.md
│   └── expected-verdict.md   # "flag" + why it cannot be fixed by rewrite
```

## When to run

- Before any change to `.claude/agents/witness.md`
- After any change to the witness's standards (e.g., updates to `craft/cold-email/`)
- Periodically (monthly) to check for drift

## Pass criterion

The witness's verdict matches the expected verdict for at least 90% of cases. The 10% miss tolerance accounts for genuine edge cases where reasonable witnesses might disagree.

## Initial state

Empty. Add cases as the witness's behavior is observed and documented — every notable verdict becomes a candidate test case.
