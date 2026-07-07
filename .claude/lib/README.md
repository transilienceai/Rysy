# .claude/lib/

Shared Python utilities used by hooks and skills. Importable as a Python package when the directory is added to `sys.path` (which the hooks do at runtime via `os.environ["CLAUDE_PROJECT_DIR"]`).

## Files

- **`ai_tells.py`** — the canonical hard-block list of AI cold-email tells. Used by `pre-write-tell-detector.py`. Adding entries to `HARD_BLOCKS` is human-approved; the list is the *deterministic* floor that complements the witness sub-agent's probabilistic review.

- **`markdown_index.py`** — utilities for parsing markdown frontmatter and building INDEX.md files. Used by the `reindex-memory` skill. Pure markdown indexing — no embeddings, no vector search.

## Why a shared lib

Hooks and skills both need access to the AI-tells list and the index-building helpers. Without a shared lib, the same logic would be duplicated in multiple places, and the hard-block list would drift. The lib keeps single sources of truth.

## Adding utilities

Utilities here should be:
- Pure Python (no external dependencies beyond the standard library, where avoidable)
- Fast (used inside hooks, which run on every matching tool call)
- Documented (each module has a docstring explaining its role)
- Tested (where applicable — `tests/` has the testbed)
