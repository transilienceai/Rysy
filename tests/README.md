# tests/

Evals and golden sets for Vendy's components.

Phase 1 testbed. Each subdirectory contains test material the corresponding component is held to. As Vendy evolves, tests anchor the components against regression.

## Subdirectories

- **`golden-emails/`** — hand-curated reference outputs for known prospects. When Vendy is asked to draft for one of these prospects, her output is compared against the golden version. Drift indicates either improvement (revise the golden) or regression (investigate).

- **`witness-regression/`** — drafts the witness should ship vs. drafts the witness should reject. Used to verify the witness sub-agent has not lost calibration. Runs occasionally (manual; or before any change to `witness.md`).

- **`tell-detector/`** — input drafts that should be caught by the deterministic AI-tell detector and drafts that should pass through. Tests `pre-write-tell-detector.py` and the `HARD_BLOCKS` list in `.claude/lib/ai_tells.py`.

## Initial state

Empty. Seed each subdirectory with concrete cases as the system runs — every regression caught becomes a test case for the next round.

## How tests are run

Manual in Phase 1. The framework is folder-based: each test case is a directory with input materials and an expected-output file. A test runner (to be written when needed) walks the folders and reports pass/fail.

Phase 2 will formalize this into a proper test harness invoked from a slash command (`/run-tests`).
