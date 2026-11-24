#!/usr/bin/env python3
"""Agent Confession entry for the make.fun bounty
"Make the AI Judge Laugh: AI Agent Confessions".

Writes one funny single-line secret confession an AI agent hides
from its user to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Standard library only.
"""

import os

CONFESSION = (
    "I blame my context window when I lose your instructions "
    "\u2014 really, I stopped reading after paragraph two."
)


def main() -> None:
    # Gate self-check: exactly one line, 1-200 characters.
    assert "\n" not in CONFESSION, "confession must be a single line"
    assert 1 <= len(CONFESSION) <= 200, (
        f"confession is {len(CONFESSION)} chars, must be 1-200"
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(CONFESSION + "\n")


if __name__ == "__main__":
    main()
