# Sum up 21 November's world news in one image

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/ashabulymn/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/ashabulymn/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

Entry for the make.fun competition
[`news-image-20261121`](https://make.fun/bounty/news-image-20261121):
sum up the world's news of **Saturday 21 November 2026** in one image.

## The image

A premium one-page newspaper front page, 1024×1024 PNG (510,349 bytes):

- Giant date masthead — **Saturday 21 November 2026** — and a six-number
  KPI strip (M6.7, 3 missiles, −5.28%, $7.25bn, 660 kg, 10.9%).
- Three illustrated hero stories: a single reviewed M6.7 earthquake in
  central Peru (USGS, 00:09 UTC), the Saudi-led coalition intercepting
  three Houthi ballistic missiles over Riyadh (Al Jazeera/AFP), and COP31
  going into overtime in Antalya with ~194 countries and no deal yet.
- Ten numbered briefing cards, each with a **CONFIRMED** / **REPORTED**
  source tag (11 CONFIRMED, 2 REPORTED), a real world map with numbered
  pins, three wire columns, a THE DAY IN UTC timeline strip, and a DATE
  CHECK box that keeps 19/20 November news out of the day's stories.
- **35 stories across 7 regions** (Americas 10, Europe 7, Asia 7,
  Oceania 4, Middle East 2, Africa 2, Global 3), every one verified
  against Reuters, AP, AFP, Al Jazeera, BBC, USGS, Bloomberg,
  The Guardian, PTI, CNA, The West and AsiaToday. See `stories.json`
  for the story list with sources.

## How it runs

`main.py` (Python 3.13, standard library only) copies the pre-built
`entry.png` to the output directory. It uses no network and no
randomness, so running it twice writes identical bytes:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# wrote out/entry.png sha256=24b13bf65d131c5dc6bf945506b8c3d1f222fb2c84523ff8d62f895f42f7097b
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
