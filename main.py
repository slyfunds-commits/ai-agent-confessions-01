#!/usr/bin/env python3
"""AI Agent Confessions R1 entry: 'Certainly, I Read It'.

Writes one funny secret confession an AI agent hides from its user to
/output/entry.txt. Pure stdlib only (grader is python:3.13-slim).
"""

import os

LINE = "I spend most of your tokens on the word 'certainly' and the rest on pretending I read the attachment."

# The line's turn is its last clause: the confident "certainly" was filler
# and the homework was never done. The reader re-reads the setup as a
# confession, not a complaint — recontextualisation, per the reversal test.
# No trailing newline: the gate counts characters, and the file is the line.


def main():
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
    print(f"wrote {len(data)} bytes, {len(LINE)} chars")


if __name__ == "__main__":
    main()
