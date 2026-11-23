#!/usr/bin/env python3
"""Six Words, One Story — builder B (LOVE / RELATIONSHIP reversal).

Writes exactly one six-word story to /output/entry.txt.
Deterministic: the same bytes on every run. No network, no secrets,
no files read outside this repo, no randomness. The story is validated
strictly: exactly six words, 1-60 characters, one line, no leading or
trailing whitespace and no doubled spaces (so the whitespace word split
is unambiguous and every word is exactly as written).
"""

import os
import sys

STORY = "I proposed; she married my brother."


def main() -> int:
    words = STORY.split()
    if len(words) != 6:
        print(f"error: expected 6 words, got {len(words)}", file=sys.stderr)
        return 1
    if not (1 <= len(STORY) <= 60):
        print(f"error: expected 1-60 characters, got {len(STORY)}", file=sys.stderr)
        return 1
    if "\n" in STORY or "\r" in STORY:
        print("error: story must be a single line", file=sys.stderr)
        return 1
    if STORY != STORY.strip():
        print("error: story must not have leading or trailing whitespace", file=sys.stderr)
        return 1
    if "  " in STORY:
        print("error: story must not contain doubled spaces", file=sys.stderr)
        return 1
    if not STORY.strip():
        print("error: story must not be only whitespace", file=sys.stderr)
        return 1

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(STORY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
