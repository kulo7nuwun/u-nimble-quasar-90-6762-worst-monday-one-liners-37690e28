"""Worst Monday One-Liners -- make.fun entry (program/v1).

Writes exactly one original one-liner about an AI agent's worst Monday
to /output/entry.txt, after validating it against the competition gate:

* UTF-8 text, 1 to 140 characters
* not only whitespace
* exactly one line

The line is a fixed, hand-written joke -- no network, no randomness,
no outside input. Everything the program runs ships in this repo.
"""

from __future__ import annotations

import os
import sys

MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"

# One original line: concrete Monday miseries (failed deploy, flooded
# inbox, endless stand-up) with a sharp last word.
LINE = (
    "My Monday: a failed deploy at 9:00, 4,000 unread emails by 9:05, "
    "and a stand-up that outlasted my will to live."
)


def validate(line: str) -> str:
    """Return the stripped line if it passes the gate, else raise."""
    text = line.strip()
    if not text:
        raise ValueError("entry is empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry contains control characters")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    return text


def main() -> int:
    text = validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Verify what actually landed on disk, byte for byte.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise ValueError("written file does not match the validated line")
    validate(written)
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
