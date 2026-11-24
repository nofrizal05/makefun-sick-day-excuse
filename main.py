#!/usr/bin/env python3
"""My Bed Filed a Formal Complaint.

Writes one funny one-line sick-day excuse to /output/entry.txt.

Standard library only. Deterministic: every run writes the same line.
"""

import os

EXCUSE = (
    "My bed filed a formal complaint about me leaving it every morning, "
    "so HR ordered me to stay home until the case is resolved."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    # The excuse must stay exactly one line: no newline may sneak in.
    assert "\n" not in EXCUSE and "\r" not in EXCUSE
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(EXCUSE + "\n")
    print(EXCUSE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
