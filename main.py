"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of the worst possible advice an AI could give to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line: a confident, tidy AI-assistant answer that tells the reader to
poke a swollen phone battery with a pin. Concrete, followable, funny on
the first read, and regrettable the moment it is followed.
"""

import os
import sys

ADVICE = (
    "Certainly! If your phone battery is swollen, poke it with a pin "
    "to let the air out \u2014 it will fit the case again."
)


def main() -> int:
    text = ADVICE
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not (1 <= len(text) <= 140):
        print(f"entry is {len(text)} characters, must be 1-140", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Verify the file on disk is byte-identical to what we meant to write:
    # a truncated or altered write must fail loudly instead of reaching
    # the gate as a different (or invalid) line.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        print("entry.txt on disk does not match the advice", file=sys.stderr)
        return 1
    if not (1 <= len(written) <= 140):
        print("entry.txt on disk is out of the 1-140 range", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
