#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

Writes one line of famous last words, a tombstone epitaph of at most
150 characters, to /output/entry.txt.
"""

import os

ENTRY = "I always said I'd sleep when I'm dead. I was right."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
