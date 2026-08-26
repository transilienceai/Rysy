#!/usr/bin/env python3
"""
pre-write-self-protect.py

PreToolUse hook. Blocks any write or edit to self/* unless a marker file
(.claude/.diff-in-progress) is present. The apply-approved-diff skill is
the only sanctioned creator of that marker — and it deletes the marker
immediately after applying the diff.

This is the architectural enforcement of the constitution-versus-memory
dialectic. Marker file is more reliable than env-var inheritance, which
does not propagate through hook subprocesses on most platforms.
"""

import json
import sys
import os


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception as e:
        # Fail open on parse error, but ask for confirmation
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "ask",
                "permissionDecisionReason": f"self-protect: could not parse hook input ({e})"
            }
        }))
        return

    tool_name = payload.get("tool_name", "")
    tool_input = payload.get("tool_input", {})

    if tool_name not in ("Write", "Edit", "MultiEdit"):
        sys.exit(0)

    target = tool_input.get("file_path", "")

    project_root = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
    self_dir = os.path.realpath(os.path.join(project_root, "self"))

    try:
        target_real = os.path.realpath(target)
    except Exception:
        sys.exit(0)

    if not target_real.startswith(self_dir):
        sys.exit(0)

    # It IS a self/ write. Check for the marker file.
    marker = os.path.join(project_root, ".claude", ".diff-in-progress")
    if os.path.exists(marker):
        # apply-approved-diff is in flight; allow.
        sys.exit(0)

    # Deny — surface a clear reason.
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": (
                "self/ is read-only to Rysy. The only sanctioned path for "
                "self/character.md to change is via the apply-approved-diff "
                "skill (invoked through /apply-diff) with a human-approved "
                "proposed diff in experience/journal/proposed-character-diffs/. "
                "If a constitutional change is warranted, write a proposed "
                "diff there and ask the human to approve it."
            )
        }
    }))


if __name__ == "__main__":
    main()
