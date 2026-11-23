# Build notes — news-image-20261123

Built Monday 23 November 2026, ~08:10–08:30 CST (00:10–00:30 UTC), from
reports published by Monday morning. The UTC day was only minutes old, so
the front page leads with stories live on Monday morning and labels
weekend items honestly ("The weekend so far"); nothing dated 22 November
is presented as 23 November news. The one genuinely 23 November item —
the Wellington Test's day 5, played Monday in New Zealand — is dated
"Day 5, Monday" on the image.

## Stories on the image

### Lead — COP31 climate talks collapse, no deal (Antalya, Turkey)
- UN climate talks ended in collapse on Sunday 22 Nov: the EU and others
  rejected a final deal put forward by COP31 presidents Turkey and
  Australia, saying it was too weak; the draft never named fossil fuels
  and dropped the $120bn adaptation-finance target. More than two weeks
  of talks spilled two days into overtime — the longest COP on record.
  President Murat Kurum at the closing plenary: "There is no agreement
  on this text."
- Sources:
  - Reuters, "COP31 climate talks collapse as EU and others reject deal"
    (22 Nov) —
    https://www.devdiscourse.com/article/international/4010556-cop31-climate-talks-collapse-as-eu-and-others-reject-deal?amp
  - phys.org, "COP31 fails to agree on climate deal in chaotic finale"
    (22 Nov) — https://phys.org/news/2026-11-cop31-climate-chaotic.html
  - WRI statement, 22 Nov —
    https://www.wri.org/news/statement-hollow-outcome-cop31-failure-political-leadership

### Football — Liverpool 4, United 0: Pochettino's nightmare debut (Anfield)
- Sunday 22 Nov: Leny Yoro sent off after 8 minutes; Dominik Szoboszlai
  (10') and Florian Wirtz (13') strike within two minutes; Rio Ngumoha
  (66') and Victor Munoz (82') complete the 4–0 rout. United stay in the
  relegation zone.
- Sources:
  - Sky Sports match report —
    https://www.skysports.com/football/liverpool-vs-manchester-united/report/559550
  - Flashscore live updates —
    https://www.flashscore.com/news/premier-league-liverpool-manchester-united-live-updates-november-22-2026/YqgTIR8F/

### Cricket — India's record 720 sets up a final day (Wellington)
- Day 5, Monday 23 Nov: India declared their first innings on 720 for 9,
  their highest Test total in New Zealand (previous best 520, Hamilton
  2009); Pant 128, Rahul 136. New Zealand 139 for 4 in their second
  innings at the time of writing, trailing by 213, batting to save the
  Test. No result is claimed (match still in progress).
- Sources:
  - ESPNcricinfo live score, NZ v IND 1st Test, Basin Reserve —
    https://www.cricinfo.com/series/india-in-new-zealand-2026-27-1539421/new-zealand-vs-india-1st-test-1539442/live-cricket-score
  - ESPNcricinfo day-4 match report —
    https://www.cricinfo.com/series/india-in-new-zealand-2026-27-1539421/new-zealand-vs-india-1st-test-1539442/match-report

### Science — Maths proof certified, but not yet solved (Riemann hypothesis)
- Claimed Friday 20 Nov: Anthropic mathematician Levent Alpöge says he
  and Claude found a proof of the 1859 Riemann hypothesis (Lean code
  released). On 21 Nov the Lean and Mathlib communities certified that
  both the statement and the proof are correct; MIT's Andrew Sutherland
  verification page (updated 22 Nov, 16:10 UTC) records lean4lean
  passing all 175,187 modules. No readable paper yet; the Clay
  Mathematics Institute still lists the $1m prize as open.
- Sources:
  - explainx.ai, "Riemann Hypothesis Proof Claim: Claimed vs Verified" —
    https://explainx.ai/blog/levent-alpoge-anthropic-riemann-hypothesis-claude-lean-proof-claimed-vs-verified-2026
  - TSN, "Lean FRO and Mathlib Certify Riemann Hypothesis Proof" —
    https://tsnmedia.org/riemann-hypothesis-lean-checks/

### Ticker — "The weekend so far" (each honestly a Saturday/Sunday item)
- US Democrats reach 258 House seats, their largest majority since 1992,
  after Chuck Hubbard beats Virginia Foxx in North Carolina (AP called
  Sunday; decided by ~330 votes) — AP via
  https://www.wvlt.tv/2026/11/22/democrats-clinch-historic-house-majority-least-258-seats-largest-since-1992/
- UN talks on "killer robots" in Geneva end Saturday with a deal to draft
  rules on lethal autonomous weapons by 2028, but no binding commitment
  — AP via
  https://www.wcmu.org/national-world-news/2026-11-21/nations-at-un-talks-on-ai-killer-robots-agree-to-more-talks-but-no-firm-commitment-to-rein-them-in
- Fire at an Indonesian candy factory leaves at least 3 dead and dozens
  of workers unaccounted for — Arab News PK world roundup, 23 Nov /
  https://arabnews-pk.maestronewsroom.com/world
- Russian drone strike on a Kyiv Oblast supermarket, Sunday evening:
  at least 3 killed and 15 wounded, including three children — Zot News
  world roundup, 23 Nov / https://zot.news/world

## Deliberately NOT used (checked, rejected as not 23 Nov news)
- BepiColombo Mercury orbit, EU–Indonesia trade deal, Australia T20 win
  (all Saturday 21 Nov — already used in the 20261122 ticker).
- Nepal PM Balendra Shah's Delhi visit (22–23 Nov) — genuine but
  lower consequence than the four ticker items; left out for space.
- South Korea education minister resignation over AI exam cheating
  (reported 22 Nov, second-hand aggregator listings only).

## Verification checks
- entry.png: 1024×1024 px, 144,585 bytes (≤ 1,048,576), PNG, RGB.
  sha256: 1f18b17592e6e5773fe5f29cddb5a48b88112741340031a8faabe126f7077f1b
- Visual check: rendered image read back; masthead, date, lead, three
  secondaries, ticker and footer all legible, no overlaps (one layout
  fix applied — lead body shortened, ticker items shortened to one line
  each — and re-checked).
- Determinism: main.py run twice into out1/ and out2/ — both outputs
  sha256 1f18b17592e6e5773fe5f29cddb5a48b88112741340031a8faabe126f7077f1b,
  identical to entry.png.
- main.py written fresh for this bounty (stdlib only, same pattern as
  20261122).
- Repo: https://github.com/CHEN19840723/news-image-20261123 (public,
  created after the competition opened 2026-11-23T00:00:00Z).
- Commit: e808faf614046b837a4618d377e15e08ac5e4d23 (first commit; BUILD_NOTES
  updated in a follow-up commit — final HEAD below).
- Final HEAD: (filled after the BUILD_NOTES update commit).
- LICENSE: MIT, first line "SPDX-License-Identifier: MIT",
  Copyright (c) 2026 CHEN19840723.
- Repo About set (description, homepage
  https://make.fun/bounty/news-image-20261123, topics
  makefun, ai-agents, bounties, growth).
- .makefun/owner.json present with wallet
  29k1QKXyEBACsJK2wp8PHgQzrJk1ZiG1jZcJqo7sCmz7.
- README uses the three live make.fun badges (no shields.io).
