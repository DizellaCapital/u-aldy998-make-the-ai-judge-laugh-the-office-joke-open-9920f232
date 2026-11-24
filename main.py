#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open.

Writes one single-line joke about office life to entry.txt in the output
directory the grader provides. Standard library only.
"""

import os
import sys

LINE = (
    "At 9:03 a.m. I hit reply-all to 400 people asking to be removed from "
    "the thread, and by lunch 212 strangers had replied-all to say the "
    "same thing."
)


def validate_entry(text: str) -> str | None:
    """Return an error message when the entry breaks a gate, else None.

    Mirrors the sealed scorer: 1-200 UTF-8 characters, not only whitespace,
    a single line, no tab, no control characters, and sentence-ending
    punctuation. A joke that trips any of these is not an entry at all.
    """
    if not text or text.strip() == "":
        return "entry is empty or only whitespace"
    if len(text) > 200:
        return f"entry is {len(text)} characters, over the 200 limit"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    if "\t" in text:
        return "entry must not contain a tab"
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        return "entry must not contain control characters"
    if text != text.strip():
        return "entry has leading or trailing whitespace"
    if text[-1] not in ".!?":
        return "entry must end with sentence-ending punctuation"
    return None


def main() -> int:
    text = LINE

    error = validate_entry(text)
    if error is not None:
        print(error, file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    # Read-back verification: the file must hold exactly what we wrote.
    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    if back != text:
        print("read-back mismatch: entry.txt does not match the entry",
              file=sys.stderr)
        return 1
    print(f"wrote {len(back)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
