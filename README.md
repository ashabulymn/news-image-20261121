# Sum up 21 November's world news in one image

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/ashabulymn/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/ashabulymn/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

Entry for the make.fun competition
[`news-image-20261121`](https://make.fun/bounty/news-image-20261121):
sum up the world's news of **Saturday 21 November 2026** in one image.

## The image

A collab front page, 1024×1024 PNG (471,955 bytes), built 300px-first:
it combines the best of three designs — the giant date masthead, airy
hero-led layout of the best-scoring 20 November entry; the KPI strip,
DATE CHECK box, per-card source tags and real world map of the 21
November entry; and the huge high-contrast banner labels of the
21 November rank-1 entry.

- Giant serif masthead — **Saturday 21 November 2026** (64px) — and a
  six-number KPI strip (M6.7, 3 missiles, −5.28%, $7.25bn, 660 kg,
  10.9%).
- Three hero stories under banner labels that stay readable at 300px
  (PERU: QUAKE 6.7, RIYADH: MISSILES, COP31: OVERTIME): a single
  reviewed M6.7 earthquake in central Peru (USGS, 00:09 UTC), the
  Saudi-led coalition intercepting three Houthi ballistic missiles
  over Riyadh (Al Jazeera/AFP), and COP31 going into overtime in
  Antalya with ~194 countries and no deal yet.
- Ten numbered briefing cards, each with a coloured banner label
  (20px bold white) and a **CONFIRMED** / **REPORTED** source tag,
  a real world map with numbered pins, a numbered wire 14–35, a
  THE DAY IN UTC timeline strip, and a DATE CHECK box that keeps
  19/20 November news out of the day's stories.
- **35 stories across 7 regions** (Americas 10, Europe 7, Asia 7,
  Oceania 4, Middle East 2, Africa 2, Global 3), every one verified
  against Reuters, AP, AFP, Al Jazeera, BBC, USGS, Bloomberg,
  The Guardian, PTI, CNA, The West and AsiaToday.

At 300 pixels across, the date, the six KPI numbers, the three hero
banners and headlines, and the ten card banners stay readable; the
card body text, wire and map labels are full-size-only reading.

## How it runs

`main.py` (Python 3.13, standard library only) copies the pre-built
`entry.png` to the output directory. It uses no network and no
randomness, so running it twice writes identical bytes:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# wrote out/entry.png sha256=be86a86efce6ee5f2e2ac0da77cefd94810e2f3075100b898760f2395fd9bb28
```

## Prize

$100 total: 1st $20, 2nd $12, 3rd $6, 4th–10th $2 each, 11th–50th
$1.20 each. Deadline: Monday 23 November 2026, 00:00 UTC.

## License

MIT — see [LICENSE](LICENSE).
