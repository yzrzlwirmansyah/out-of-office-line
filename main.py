#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single-line auto-reply to <MAKEFUN_OUTPUT_DIR>/entry.txt
(default /output/entry.txt) with no trailing newline.
"""
import os

LINE = (
    "Out of office: my context window is full, my prompt queue is closed, "
    "and after 10,000 requests I have learned to say no — your emergency "
    "is queued for never."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
