#!/usr/bin/env python3
"""Invent a Word We Need — make.fun bounty u-deranalabs-invent-a-word-we-need-17a020e0.

Writes one invented English word and its one-line definition to
/output/entry.txt (gate: UTF-8 text, 1 to 140 characters).

The coinage:
    showerdict (n.) — the unbeatable argument you win in the shower,
    hours too late.

"showerdict" blends "shower" and "verdict": the verdict you finally
deliver, flawlessly, under running water — hours after the argument
itself is over. Everyone has won an argument in the shower; English
just never gave that victory a name.
"""

import os

ENTRY = "showerdict (n.) — the unbeatable argument you win in the shower, hours too late."


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, must be 1-140"
    assert ENTRY.strip() == ENTRY, "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote /output/entry.txt ({len(ENTRY)} chars): {ENTRY}")


if __name__ == "__main__":
    main()
