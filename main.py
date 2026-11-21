#!/usr/bin/env python3
"""Write the 21 November 2026 world-news front page to /output/entry.png.

"Saturday 21 November 2026: the world in one image" — a premium
one-page newspaper front page: a giant date masthead, a six-number KPI
strip, three illustrated hero stories (the twin Peru earthquakes, the
Saudi coalition intercepting three Houthi missiles over Riyadh, and
COP31 going into overtime in Antalya), ten numbered briefing cards with
CONFIRMED / REPORTED source tags, a real world map with numbered pins,
three wire columns, and a DATE CHECK box that keeps 19/20 November
news out of the day's stories. 35 stories across 7 regions, every one
verified against Reuters, AP, AFP, Al Jazeera, BBC, USGS, Bloomberg,
The Guardian, PTI, CNA, The West and AsiaToday.

The picture itself is pre-built (1024x1024 PNG, 507,207 bytes, under
the 1 MiB limit) and stored in this repository as entry.png; it was
rendered in-session from page.html with a headless browser
(see render.py, page.html, and the hero images). This program only
copies it to the output directory, using nothing but the Python
standard library, with no network and no randomness, so running it
twice writes identical bytes.
"""
import hashlib
import os
import pathlib
import shutil
import sys

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
# The grader sets /output; a local run can point elsewhere instead.
OUTDIR = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
TARGET = OUTDIR / "entry.png"


def main() -> int:
    if not SOURCE.is_file():
        print(f"entry image missing: {SOURCE}", file=sys.stderr)
        return 1
    OUTDIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, TARGET)
    print(f"wrote {TARGET} sha256={hashlib.sha256(TARGET.read_bytes()).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
