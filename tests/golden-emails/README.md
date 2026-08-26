# tests/golden-emails/

Hand-curated reference drafts for known prospects. These are emails Rysy *should* produce when given a known input — anchors against regression.

## Structure

Each test case is a folder:

```
tests/golden-emails/{case-slug}/
├── input.json           # campaign + lead JSON Rysy receives
├── expected-draft.md    # the draft Rysy should produce (or close to it)
├── notes.md             # why this is the expected output; what to compare on
```

## Calibration

Golden emails are not exact-string-match tests. Rysy's drafts will vary slightly across runs; the comparison is on:
- The register chosen (must match)
- The opener architecture (must match)
- The CTA weight (must match)
- The presence of any hard-blocked AI tells (must be zero)
- The witness verdict (must be ship or rewrite-but-not-flag)
- The general posture and length

Drift on any of these without an explanation in `notes.md` is a signal to investigate.

## Initial state

Empty. Add cases as Rysy ships drafts that exemplify high quality — those become the goldens for regression.
