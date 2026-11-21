#!/usr/bin/env python3
"""Render page.html to 1024x1024 entry.png deterministically (21 Nov draft)."""
import hashlib, math
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
HTML = HERE / "page.html"
OUT = HERE / "entry.png"
PREVIEW = HERE / "preview-300px.png"

def main():
    with sync_playwright() as p:
        b = p.chromium.launch(args=[
            "--font-render-hinting=none", "--force-color-profile=srgb",
            "--hide-scrollbars", "--disable-lcd-text",
        ])
        pg = b.new_page(viewport={"width": 1024, "height": 1024}, device_scale_factor=1)
        pg.goto(HTML.as_uri())
        pg.wait_for_timeout(400)
        pg.evaluate("document.body.style.animation='none'")
        dims = pg.evaluate("() => ({w: document.documentElement.scrollWidth, h: document.documentElement.scrollHeight})")
        assert dims["w"] <= 1024 and dims["h"] <= 1024, f"OVERFLOW page {dims}"
        clip = pg.evaluate("""() => {
          const bad = [];
          document.querySelectorAll('.hero-body, .card-text, .wire-col, .datecheck, .masthead').forEach(el => {
            if (el.scrollHeight > el.clientHeight + 1) bad.push(el.className + ' ' + el.scrollHeight + '>' + el.clientHeight);
          });
          return bad;
        }""")
        assert not clip, f"CLIPPED: {clip}"
        pts = pg.evaluate("""() => {
          const out = [];
          document.querySelectorAll('.mapbox svg circle').forEach(c => {
            out.push([parseFloat(c.getAttribute('cx')), parseFloat(c.getAttribute('cy')), parseFloat(c.getAttribute('r'))]);
          });
          return out;
        }""")
        for i in range(len(pts)):
            for j in range(i + 1, len(pts)):
                d = math.hypot(pts[i][0] - pts[j][0], pts[i][1] - pts[j][1])
                need = pts[i][2] + pts[j][2] + 0.5
                assert d >= need, f"PIN OVERLAP {pts[i]} vs {pts[j]} dist={d:.1f} need {need}"
        pg.screenshot(path=str(OUT))
        b.close()
    im = Image.open(OUT)
    assert im.size == (1024, 1024), f"SIZE {im.size}"
    im.save(OUT, optimize=True, compress_level=9)
    im2 = Image.open(OUT)
    im2.resize((300, 300), Image.LANCZOS).save(PREVIEW, optimize=True)
    data = OUT.read_bytes()
    n = len(data)
    print(f"entry.png: {im.size[0]}x{im.size[1]} {n} bytes ({n/1024:.1f} KiB) sha256 {hashlib.sha256(data).hexdigest()}")
    assert n <= 1048576, "FILE TOO BIG (>1 MiB)"
    if n > 470 * 1024:
        print("WARN: >470 KiB — above target")
    print("OK: dimensions, overflow, clipping, pin distances, size all pass")

if __name__ == "__main__":
    main()
