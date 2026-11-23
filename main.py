#!/usr/bin/env python3
"""The One-Line Laugh — one funny line, written to /output/entry.txt.

The line is a single sentence of at most 200 characters. It names an
everyday truth everyone recognises (the inbox is never really empty)
and saves the surprise for the very end.
"""

from __future__ import annotations

import os
import sys

LINE = "I finally reached inbox zero, and Gmail immediately sent me a congratulatory email."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def check_line(line: str) -> str:
    """Return the line when it meets the contest gate, else fail loudly.

    The gate is the brief itself: one sentence, 1 to 200 characters,
    no line breaks, nothing but the joke.
    """
    text = line.strip()
    if not text:
        raise ValueError("entry is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.endswith(".") or text.count(".") != 1:
        raise ValueError("entry must be exactly one sentence")
    return text


def main() -> int:
    text = check_line(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
