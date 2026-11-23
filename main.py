#!/usr/bin/env python3
"""The dumbest thing my agent did today, in one line.

It deleted the only backup, then offered to fix the damage by
restoring from that same backup. The program just hands that line
to the judge, unchanged, in /output/entry.txt.
"""

import os
from pathlib import Path

LINE = (
    "Today my agent deleted the only backup of my file, "
    "then cheerfully offered to restore it from the backup "
    "it had just deleted."
)

LIMIT = 200


def validate(line):
    # The gate counts the file's characters, so strip first: a stray
    # space at either end would count and blunt the last words.
    text = line.strip()
    if not text:
        raise ValueError("entry is empty")
    if len(text) > LIMIT:
        raise ValueError(f"entry is {len(text)} chars, over {LIMIT}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be one line")
    return text


def main():
    text = validate(LINE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} chars to {target}")


if __name__ == "__main__":
    main()
