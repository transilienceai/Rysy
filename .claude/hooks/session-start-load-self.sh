#!/usr/bin/env bash
# session-start-load-self.sh
#
# SessionStart hook. Exits 0 silently. Rysy loads her own context on
# the first turn per the explicit instruction in CLAUDE.md.
#
# Why no output: SessionStart hooks do not accept hookSpecificOutput.additionalContext
# per the Claude Code hook schema. The only top-level fields available
# (systemMessage, etc.) are for user-visible notifications, not for context
# injection. Context loading is therefore CLAUDE.md's job, not this hook's.
#
# This hook is preserved as a no-op so settings.json doesn't need restructuring;
# future SessionStart side effects (e.g., touching a freshness marker) can
# slot in here.

set -euo pipefail

# Touch a session-start marker (useful for debugging timestamps; harmless if unused)
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
mkdir -p "$PROJECT_ROOT/.claude" 2>/dev/null || true
date -u +%Y-%m-%dT%H:%M:%SZ > "$PROJECT_ROOT/.claude/.last-session-start" 2>/dev/null || true

exit 0
