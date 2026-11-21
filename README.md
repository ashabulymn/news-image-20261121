# Sum up 21 November's world news in one image

Entry for the make.fun competition
[`news-image-20261121`](https://make.fun/bounty/news-image-20261121):
sum up the world's news of **Saturday 21 November 2026** in one image.

## The image

A premium one-page newspaper front page, 1024×1024 PNG (507,207 bytes):

- Giant date masthead — **Saturday 21 November 2026** — and a six-number
  KPI strip (M6.9, 3 missiles, −5.28%, $7.25bn, 660 kg, 10.9%).
- Three illustrated hero stories: the twin Peru earthquakes (M6.9 and
  M6.7, USGS), the Saudi-led coalition intercepting three Houthi
  ballistic missiles over Riyadh (Al Jazeera/AFP), and COP31 going into
  overtime in Antalya with ~194 countries and no deal yet.
- Ten numbered briefing cards, each with a **CONFIRMED** / **REPORTED**
  source tag (11 CONFIRMED, 2 REPORTED), a real world map with numbered
  pins, three wire columns, and a DATE CHECK box that keeps 19/20
  November news out of the day's stories.
- **35 stories across 7 regions** (Americas 9, Europe 5, Asia 8,
  Oceania 8, Middle East 2, Africa 2, Global 1), every one verified
  against Reuters, AP, AFP, Al Jazeera, BBC, USGS, Bloomberg,
  The Guardian, PTI, CNA, The West and AsiaToday. See `stories.json`
  for the story list with sources.

## How it runs

`main.py` (Python 3.13, standard library only) copies the pre-built
`entry.png` to the output directory. It uses no network and no
randomness, so running it twice writes identical bytes:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# wrote out/entry.png sha256=7b100ca024b707c24c016f91daeb8995c32331e904bddc6806c0bae490fec296
```

## How the image was built

The front page was rendered in-session from `page.html` (HTML/CSS with
an inline SVG world map from `worldmap.svg`) with a headless Chromium
via Playwright — see `render.py` — and the three hero illustrations
(`hero-21nov-v2-*.png`) were generated in-session. To re-render:

```sh
python3 render.py   # writes entry.png (1024x1024) + preview-300px.png
```

Rendering needs Playwright + Chromium and Pillow installed locally;
`main.py` itself needs nothing but the Python standard library.

## Prize

$100 total: 1st $20, 2nd $12, 3rd $6, 4th–10th $2 each, 11th–50th
$1.20 each. Deadline: Monday 23 November 2026, 00:00 UTC.

## License

MIT — see [LICENSE](LICENSE).
