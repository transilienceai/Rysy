#!/usr/bin/env bash
# session-end-reflect.sh
#
# SessionEnd hook. Runs reindex-memory directly. Surfaces a pattern-promotion
# suggestion as a systemMessage if notes have accumulated above threshold.
#
# Per Claude Code's hook schema, SessionEnd does NOT accept
# hookSpecificOutput.additionalContext — only top-level fields like
# systemMessage. We use systemMessage for the suggestion (user-visible notification).

set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

# Run reindex-memory directly — don't wait for the next skill invocation
python3 "$PROJECT_ROOT/.claude/lib/markdown_index.py" "$PROJECT_ROOT" >/dev/null 2>&1 || true

# Count new notes since last reindex (best effort)
NOTES_DIR="$PROJECT_ROOT/craft/notes"
INDEX_FILE="$NOTES_DIR/INDEX.md"
NEW_NOTES=0

if [ -d "$NOTES_DIR" ] && [ -f "$INDEX_FILE" ]; then
    NEW_NOTES=$(find "$NOTES_DIR" -name "*.md" -newer "$INDEX_FILE" -not -name "INDEX.md" -not -name "README.md" 2>/dev/null | wc -l | tr -d ' ' || echo 0)
fi

# Emit systemMessage only if there's something worth surfacing
if [ "$NEW_NOTES" -ge 5 ]; then
    SUGGESTION="$NEW_NOTES new craft notes since last index. Consider /promote-patterns to evaluate them for promotion." \
    python3 - <<'PYEOF'
import json
import os
print(json.dumps({
    "systemMessage": os.environ.get("SUGGESTION", "")
}))
PYEOF
else
    # Silent close — reindex already done, no suggestion to surface
    exit 0
fi
