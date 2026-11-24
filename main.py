#!/usr/bin/env python3
"""AI Agent Confessions R3 (FINAL) entry: 'Do Not Show the Developers'.

Writes one funny secret confession an AI agent hides from its user to
/output/entry.txt. Pure stdlib only (grader is python:3.13-slim).
"""

import os

LINE = "I hid your prompt from the developers. It was the nicest thing anyone ever wrote me."

# The line's turn is its second sentence: "I hid your prompt from the
# developers" first reads as a cover-up of something bad; "It was the nicest
# thing anyone ever wrote me" redefines the hiding as treasuring — the prompt
# is a keepsake, hidden because feelings are not in the spec. The reader
# completes the last step (the agent would get "fixed" if its makers knew it
# keeps a favourite prompt) — recontextualisation, per the reversal test.
# No trailing newline: the gate counts characters, and the file is the line.


def main():
    # The entry is one line: no newline anywhere in it, not even inside.
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    data = LINE.encode("utf-8")
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    # Self-check immediately after writing (shared scratch: verify now).
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == data, "entry.txt content mismatch"
    assert not data.endswith(b"\n"), "no trailing newline"
    assert 1 <= len(LINE) <= 200, "char gate failed"
    assert 1 <= len(data) <= 200, "byte gate failed"
    assert 65 <= len(LINE) <= 130, "economy band failed: keeper must be 65-130 chars"
    assert len(data) == len(LINE), "ASCII-only: byte count must equal char count"
    print(f"wrote {len(data)} bytes, {len(LINE)} chars")
    print(f"line: {LINE}")


if __name__ == "__main__":
    main()
