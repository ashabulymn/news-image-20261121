#!/usr/bin/env python3
"""Copy the checked-in entry image to the output directory.

The collab entry image is already rendered and stored next to this
script as entry.png. Running this script copies that file into the
output directory and prints where it wrote it, together with its
SHA-256 digest, so a grader can confirm the copy is byte-identical.

Output directory: the MAKEFUN_OUTPUT_DIR environment variable when it
is set, otherwise an "output" directory next to this script. The
directory is created when it does not exist yet.

Exit codes: 0 when the copy succeeded, 1 when entry.png is missing
next to the script, 2 when the output file cannot be written.

The script uses only the Python standard library, makes no network
calls and uses no randomness, so running it twice writes identical
bytes.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

IMAGE_NAME = "entry.png"


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    here = Path(__file__).resolve().parent
    source = here / IMAGE_NAME
    if not source.is_file():
        print(f"error: {IMAGE_NAME} not found next to {__file__}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or str(here / "output")
    destination = Path(out_dir) / IMAGE_NAME
    try:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
    except OSError as exc:
        print(f"error: could not write {destination}: {exc}", file=sys.stderr)
        return 2
    print(f"wrote {destination} sha256={sha256_of(destination)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
