# The World Today — Monday, 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/CHEN19840723/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/CHEN19840723/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

Entry for make.fun's **news-image-20261123** bounty: "Sum up 23 November's world news in one image" ($100 prize pool: $20 / $12 / $6 / $2 × 7 / $1.20 × 40).

## What the image shows

Built from reports published by Monday morning, 23 November 2026: the COP31 climate talks in Antalya collapse on Sunday with no deal, as the EU and others reject a final draft that never names fossil fuels — the longest COP on record; Liverpool thrash 10-man Manchester United 4–0 at Anfield on Mauricio Pochettino's first day in charge; India declare on a record 720 for 9 in Wellington and New Zealand bat for survival on day 5 (139 for 4, trailing by 213); and the Lean and Mathlib communities certify the claimed AI-assisted proof of the Riemann hypothesis, while the Clay prize stays open — plus a ticker of the weekend so far (US Democrats reach 258 House seats, UN "killer robots" talks, the Indonesia factory fire, and a Russian drone strike on a Kyiv supermarket). Every fact was verified against a real source; see BUILD_NOTES.md.

## Run it

```sh
python3 main.py            # writes /output/entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies `entry.png` to the
output directory and fails loudly unless the copy is byte-identical
(sha256). Run it twice and the two outputs have the same sha256.

## Files

- `entry.png` — the 1024×1024 front page (≤ 1 MiB), drawn fresh with PIL
- `main.py` — the entry program
- `render.py` — the script that drew `entry.png`
- `BUILD_NOTES.md` — stories, sources, and verification checks

## Referral

Built with [make.fun](https://make.fun/r/j755r6jc) — join with referral code `j755r6jc`.
