#!/usr/bin/env python3
"""Entry point for the make.fun news-image-20261121 submission.

The image is pre-built (entry.png, 1024x1024) and bundled with this file.
Running this script copies it unchanged to the output directory, so the
grader receives exactly the bytes that were verified locally. No network,
no randomness, no re-rendering: run it twice and the output is identical.
"""
import hashlib
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit(f"missing bundled image: {SOURCE}")
    expected = SOURCE.stat().st_size
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    written = target.stat().st_size
    assert written == expected, f"copy truncated: {written} != {expected}"
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    print(f"wrote {target} ({written} bytes) sha256={digest}")


if __name__ == "__main__":
    main()
