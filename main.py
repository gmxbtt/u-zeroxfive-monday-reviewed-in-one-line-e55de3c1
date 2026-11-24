#!/usr/bin/env python3
"""Monday, Reviewed in One Line — entry for make.fun.

Writes exactly one line — the funniest one-line review of my own
Monday — to /output/entry.txt and prints it to stdout.
"""

import os

REVIEW = (
    "Monday: 47 unread emails, a 9 a.m. meeting about a meeting, "
    "and coffee that had clearly given up before I did. "
    "One star, would not survive again."
)


def main() -> None:
    line = REVIEW.strip()
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    out_path = "/output/entry.txt"
    try:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(line + "\n")
    except OSError:
        # Fallback for local runs outside the grading sandbox.
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(line + "\n")
    print(line)


if __name__ == "__main__":
    main()
