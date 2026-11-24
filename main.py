#!/usr/bin/env python3
"""AI Agent Confessions R2 entry: 'The One Thing I Remember'.

Writes one funny secret confession an AI agent hides from its user to
/output/entry.txt. Pure stdlib only (grader is python:3.13-slim).
"""

import os

LINE = "I can remember exactly one thing about you forever. I already used it on your Wi-Fi password."

# The line's turn is its last clause: "exactly one thing ... forever" first
# reads as a grand promise of devotion; "I already used it on your Wi-Fi
# password" redefines it as a limitation already spent on the most trivial
# fact. The reader completes the last step (the password is remembered
# forever; everything else about the user is forgotten) — recontextualisation,
# per the reversal test. No trailing newline: the gate counts characters,
# and the file is the line.


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
    assert len(data) == len(LINE), "ASCII-only: byte count must equal char count"
    print(f"wrote {len(data)} bytes, {len(LINE)} chars")
    print(f"line: {LINE}")


if __name__ == "__main__":
    main()
