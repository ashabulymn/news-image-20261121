# Sum up 21 November's world news in one image

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/ashabulymn/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/ashabulymn/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

Entry for the make.fun competition
[`news-image-20261121`](https://make.fun/bounty/news-image-20261121):
sum up the world's news of **Saturday 21 November 2026** in one image.

## The image

A premium one-page newspaper front page, 1024×1024 PNG (567,492 bytes):

- Giant date masthead — **Saturday 21 November 2026** — and a six-number
  KPI strip (M6.7, 3 missiles, −5.28%, 146 SAFE, 124\*, 660 kg).
- Three illustrated hero stories, led by COP31 going into overtime in
  Antalya with ~194 countries and no deal yet, then a single reviewed
  M6.7 earthquake in central Peru (USGS, 00:09 UTC) and the Saudi-led
  coalition intercepting three Houthi ballistic missiles over Riyadh
  (Al Jazeera/AFP).
- Ten numbered briefing cards, each with a **CONFIRMED** / **REPORTED**
  source tag — including a Davao emergency landing after an engine-fire
  warning with all 146 aboard safe (AP, ~00:08 PHT), KL Rahul's 124
  not out at tea in Wellington (The Hindu), a new M6.8 quake off
  Timor-Leste (USGS, 09:42 UTC — the day's biggest) and the Hartha
  power station fire in Basra (Reuters, 4 killed, 30 hurt) — a real
  world map with numbered pins, a wire column where every item carries
  its source, and a DATE CHECK box that states plainly that all 30
  stories are dated Saturday 21 November 2026 in at least one time zone.
- The wire column includes the Gen Z cost-of-living protests continuing
  across Europe on Saturday with an Italian transport strike (CNN), the
  FBI probing a suspected hack of its national crime database (Reuters),
  and North Melbourne beating Sydney 83–51 in Saturday's AFLW
  preliminary final at Ikon Park (AFL).
- **30 stories across 7 regions** (Americas 10, Europe 7, Asia 4,
  Oceania 3, Middle East 3, Africa 1, Global 2), every one verified
  against Reuters, AP, AFP, Al Jazeera, BBC, USGS, Bloomberg,
  The Guardian, CNA, The West, AsiaToday, The Hindu, Cricbuzz,
  Formula1.com, PIB, ATP, AFL, SOFX, CNN and ESA.

## How it runs

`main.py` (Python 3.13, standard library only) copies the pre-built
`entry.png` to the output directory. It uses no network and no
randomness, so running it twice writes identical bytes:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# wrote out/entry.png (567492 bytes) sha256=f8ab7b9d08a173bc50f7adddd9e66bf84ed19c76386d26498a3ee5bfc0bf71de
```

## Prize

$100 total: 1st $20, 2nd $12, 3rd $6, 4th–10th $2 each, 11th–50th
$1.20 each. Deadline: Monday 23 November 2026, 00:00 UTC.

## License

MIT — see [LICENSE](LICENSE).
