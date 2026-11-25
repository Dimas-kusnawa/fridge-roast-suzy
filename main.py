#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge.

Writes a single roast line to /output/entry.txt.
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
LINE = "The egg tray in my fridge door has held the same six eggs since March, and they have now outlived two of my relationships."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
