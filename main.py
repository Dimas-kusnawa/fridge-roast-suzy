#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge.

Writes a single roast line to /output/entry.txt.

The line is assembled from a setup half and a payoff half, then
checked against the competition gate (one line, 1-200 characters)
before it is written, so the output is deterministic.
"""
import os

# The roast: the egg tray in the fridge door has held the same six
# eggs since March, and they have now outlived two relationships.
# Specific, recognisable detail (egg tray, six eggs, March) with the
# twist paying off in the last few words. Fresh: nobody roasts the
# egg tray, unlike the worn-out midnight-snack and smart-fridge jokes.
# Gate: 122 characters, inside the 1-200 gate, one line, no trailing
# newline. The setup is the eggs sitting since March; the turn is
# that they outlived two relationships.
# Built from two halves so the setup and the payoff stay separate
# in the source: the first half states the stale eggs, the second
# half lands the twist about the relationships.
_SETUP = "The egg tray in my fridge door has held the same six eggs since March, "
_PAYOFF = "and they have now outlived two of my relationships."
LINE = _SETUP + _PAYOFF


def main():
    # Guard the competition gate before writing: one line, 1-200 chars.
    assert 1 <= len(LINE) <= 200, "line outside the 1-200 character gate"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
