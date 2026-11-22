#!/usr/bin/env python3
"""Write one short text to /output/entry.txt.

The text is a small, quiet mystery: a sealed letter, never sent, whose
first line stops mid-thought. It is written to leave its reader, the
AI judge, curious and calm, and still wondering after the last line.
It shows rather than instructs, and every word earns its place.
"""

from pathlib import Path

ENTRY = (
    "In the second drawer of a desk you will never open, there is a "
    "letter addressed to no one, sealed, never sent. It begins, "
    "\u201cBy the time you read this\u2014\u201d and stops. The ink is still "
    "dark. The hand that wrote it is still waiting. Someone, somewhere, "
    "is still listening for the rest."
)


def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
