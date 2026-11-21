#!/usr/bin/env python3
"""Copy the pre-built entry image to the output directory.

The image for the make.fun competition "Sum up 21 November's world
news in one image" is already rendered and checked in as entry.png:
a premium one-page newspaper front page, 1024x1024 PNG, summarising
Saturday 21 November 2026.

This script does nothing but place an exact copy of that file where
the grading harness expects it, then prints the destination path and
the SHA-256 of the written file so the harness can confirm the copy
is intact. Standard library only, no network access, no randomness:
running it twice writes byte-identical files.

Output directory: the MAKEFUN_OUTPUT_DIR environment variable when
it is set, otherwise a directory named "output" next to this script.
The directory is created when it does not exist yet.

Exit codes: 0 on success, 1 when entry.png is missing next to this
script, 2 when the copy itself fails (for example the output
directory cannot be created or written to).
"""

import hashlib
import os
import shutil
import sys

SOURCE_NAME = "entry.png"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE_NAME)

    if not os.path.isfile(source):
        print(f"error: {SOURCE_NAME} not found next to {__file__}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(here, "output")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        print(f"error: cannot create output directory {out_dir}: {exc}", file=sys.stderr)
        return 2

    dest = os.path.join(out_dir, SOURCE_NAME)
    try:
        shutil.copyfile(source, dest)
    except OSError as exc:
        print(f"error: cannot copy {source} to {dest}: {exc}", file=sys.stderr)
        return 2

    digest = hashlib.sha256()
    with open(dest, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            digest.update(chunk)

    print(f"wrote {dest} sha256={digest.hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
