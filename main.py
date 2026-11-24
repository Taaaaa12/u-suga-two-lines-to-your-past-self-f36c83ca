#!/usr/bin/env python3
"""Two Lines to Your Past Self.

Writes exactly two lines to /output/entry.txt: line one warns the past
self about one specific moment, line two says why that moment mattered
and what changed because of it. Deterministic, no network, no input.
"""

import os

ENTRY = (
    "Don't leave the hospital at 3 a.m. promising you'll be back in the morning.\n"
    "She was gone before sunrise, and you've carried that empty chair into every goodbye since.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
