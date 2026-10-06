#!/usr/bin/env python3
"""Book Skills PreToolUse hook: ask before any MCP tool that sends or publishes.

hooks.json matches send-type MCP tool names; this script re-checks the name so a
broad matcher can never catch drafts or reads. Stdlib only. Never raises, never
blocks: any problem -> exit 0 silently (Claude Code's normal permission flow applies).
"""
import json
import os
import re
import sys

REASON = ("Book Skills outbound guard: this sends or publishes something outside "
          "your machine. Confirm: evidence audit passed, personalisation verified, "
          "recipient correct.")

SEND = re.compile(
    r"^(send|send_message|send_email|send_mail|send_sms|send_dm|send_reply|send_invite"
    r"|reply|reply_all|forward|post_message|slack_send_message|slack_schedule_message"
    r"|schedule_message|create_event|update_event|respond_to_event"
    r"|publish_[a-z0-9_-]*|[a-z0-9-]+_publish_[a-z0-9_-]*"
    r"|share_[a-z0-9_-]*|[a-z0-9-]+_share)$")

# Never guard drafts or reads, whatever the matcher let through.
SAFE = re.compile(
    r"(^|_)drafts?$|^(create|update|delete|get|list)_drafts?\b"
    r"|^(get|list|search|read|find|fetch|query|describe|inspect)_")


def is_outbound(tool_name):
    if not tool_name.startswith("mcp__") or "__" not in tool_name[5:]:
        return False
    suffix = tool_name.rsplit("__", 1)[-1].lower()
    if not suffix or SAFE.search(suffix):
        return False
    return bool(SEND.match(suffix))


def main():
    if sys.stdin is None or sys.stdin.isatty():
        return
    raw = sys.stdin.read()
    if not raw.strip():
        return
    data = json.loads(raw)
    name = data.get("tool_name", "") if isinstance(data, dict) else ""
    if not isinstance(name, str) or not is_outbound(name):
        return
    sys.stdout.write(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "ask",
        "permissionDecisionReason": REASON}}))


if __name__ == "__main__":
    try:
        import signal
        if hasattr(signal, "SIGALRM"):
            signal.signal(signal.SIGALRM, lambda *_: os._exit(0))
            signal.alarm(3)
        main()
    except BaseException:
        pass
    sys.exit(0)
