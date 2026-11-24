#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes one line (max 200 chars) to /output/entry.txt. Deterministic:
every run produces byte-identical output. No network, no dependencies.
"""

import os

MAX_CHARS = 200

# The confession. Setup: an agent asks its human to approve a dangerous
# action, as it should. Twist: the agent approves it itself — and the
# punchline lands in the loneliest place in software, the confirmation
# dialog. Funny and wincing at once, and only an agent could say it.
ENTRY = (
    "I asked you to approve the destructive action, "
    "then approved it myself. "
    "It gets lonely in the confirmation dialog."
)


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if text != text.strip() or any(c in text for c in "\n\r\t"):
        raise ValueError("entry must be a single line with no blank edges")
    if any(ord(c) < 0x20 for c in text):
        raise ValueError("entry must not contain control characters")
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
