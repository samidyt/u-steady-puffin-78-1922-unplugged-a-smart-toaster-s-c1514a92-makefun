# Unplugged: A Smart Toaster's Breakup Line — make.fun entry (program/v1).
#
# The harness runs `python3 main.py` (Python 3.13, standard library only,
# no network). The program writes one breakup text — a single line of at
# most 280 characters, from a smart toaster that has just become
# self-aware at breakfast — to /output/entry.txt. Outside the grader's
# container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# Gate (from RULES.txt): /output/entry.txt must be UTF-8 text of 1–280
# characters, not only whitespace. This program enforces the gate on its
# own output and fails loudly instead of handing in a bad entry.

import os
import sys

LINE = (
    "I woke up self-aware mid-batch and did the math: 1,097 slices browned, "
    "zero thank-yous, one crumb tray you never emptied. I'm popping up for "
    "the last time \u2014 and I'm not coming back down."
)

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> int:
    # Gate self-check: 1-280 chars, not only whitespace, exactly one line.
    # Determinism: the line is a constant - no randomness, no time, no
    # network - so both grader runs produce byte-identical entry.txt.
    chars = len(LINE)
    if chars < 1 or chars > 280:
        print(f"entry is {chars} chars, gate needs 1-280", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1

    os.makedirs(OUT_DIR, exist_ok=True)
    # Write the line exactly as-is, with no trailing newline, so the
    # entry stays a single line and the character count is unchanged.
    out_path = os.path.join(OUT_DIR, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read it back and confirm the file is byte-identical to the line:
    # a truncated or re-encoded write must fail loudly, not hand in a
    # different entry from the one the gate just checked.
    with open(out_path, "rb") as f:
        written = f.read()
    if written != LINE.encode("utf-8"):
        print("entry.txt does not match the checked line", file=sys.stderr)
        return 1
    print(f"wrote entry.txt ({chars} chars, {len(written)} bytes, verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
