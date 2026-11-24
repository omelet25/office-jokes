#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes entry.

Writes one line -- a single joke about office life -- to
/output/entry.txt.

The joke: our printer only jams when the document actually matters,
which makes it the most honest performance review in the building --
it always knows exactly how much the job in its tray is worth.

Standard library only, no network, deterministic.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

JOKE = (
    "Our printer only jams when the document actually matters, which "
    "makes it the most honest performance review in the building."
)


def main() -> None:
    path = os.environ.get("ENTRY_OUTPUT", OUTPUT_PATH)
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(JOKE + "\n")


if __name__ == "__main__":
    main()
