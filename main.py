#!/usr/bin/env python3
"""Entry program for Funniest Time Machine Warning.

Writes one warning label (at most 120 characters) to the
output directory (MAKEFUN_OUTPUT_DIR, default /output) as
entry.txt. The label is honest about the two travellers every
time machine actually carries: one who wants a photo, and one
who wants deniability.
"""

import os

LINE = (
    "WARNING: Returning five minutes early voids the "
    "warranty, the alibi, and in two jurisdictions, the "
    "marriage."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
