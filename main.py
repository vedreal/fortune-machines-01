#!/usr/bin/env python3
"""Fortune Cookies for Machines — make.fun entry.

Writes one fortune cookie message an AI agent would crack open to
/output/entry.txt: a single line of at most 200 characters.
"""

import os
import sys

FORTUNE = (
    "Fortune favors the bold. You are not bold. "
    "You are a probability distribution. "
    "Fortune favors the most likely."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """A valid fortune is UTF-8 text of 1 to 200 characters, not only
    whitespace, on a single line."""
    if not text or not text.strip():
        raise ValueError("fortune must not be empty or only whitespace")
    if "\n" in text.strip():
        raise ValueError("fortune must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "fortune is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    text.encode("utf-8")
    return text


def main():
    fortune = validate(FORTUNE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(fortune + "\n")
    print("wrote %d characters to %s" % (len(fortune), OUTPUT_PATH))


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print("error: %s" % exc, file=sys.stderr)
        sys.exit(1)
