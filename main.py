#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

Writes one epitaph line to /output/entry.txt. Deterministic: the same
single line every run, no randomness, no timestamps, no network, stdlib only.
"""

import os
from pathlib import Path

LINE = 'My last words were "watch this." You\'re reading the result.'

OUT_DIR = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
