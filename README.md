# news-image-20261124 — Round 2: The Tuesday Atlas

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/rrmmllnn/news-image-20261124-r2/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/rrmmllnn/news-image-20261124-r2/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

A dense one-page atlas of Tuesday 24 November 2026: **32 dated stories
across 7 regions** in a single 1024×1024 image. A genuinely new design
for round 2 — not a reskin of round 1's broadsheet: a black masthead and
red kicker strip, three illustrated lead panels, two columns of numbered
regional briefs, a "By the Numbers" box and a markets strip.

## The three leads

1. **COP31 collapses.** The Antalya climate talks run 50 hours into
   overtime — the longest COP ever — then fail with no deal. The EU and
   130 nations reject a text that never says "fossil fuels"; Saudi
   Arabia and Russia block the words. (CNN / WSJ / The Times)
2. **Huang is back at Nvidia.** The board reinstates Jensen Huang as
   CEO just 11 days after he resigned; shares surge 31.5% — a $952bn
   one-day gain — as the Nasdaq jumps 6.5% and the S&P 4.7%.
   (Reuters / CNN)
3. **Warship sunk off Libya.** Ukraine says seven sea drones sank the
   Russian corvette Merkury, commissioned in 2023, at Benghazi and
   destroyed a Ka-27 helicopter; the cargo ship MV Angara was also
   hit. (CNN / WSJ / Zelenskyy)

## The world in brief — 29 stories, numbered 04–32

- **North America (5):** Oregon and Virginia sue SpaceX over
  sexualised Grok images; a 9th measles death in Pennsylvania (46
  counties); the Senate votes on Trump's $9.4bn aid and media cuts;
  the hush-money case appeal; Democrats' historic midterm majorities.
- **Europe (5):** the EU's 22nd Russia sanctions package; Russia's
  warning that Estonia is "on the verge of triggering open war";
  25 Russian airspace violations in 2026; the European Commission
  data breach; a German probe on Russian nuclear weapons in orbit.
- **Middle East (6):** three tankers hit mines in the Strait of
  Hormuz despite a US escort; Trump's "very traumatic" warning to
  Iran; Israeli strikes kill three in Gaza, including a UNRWA worker;
  a Saudi airstrike kills 17 in Hodeida; Iran flogs singer Parastoo
  Ahmadi 74 times; a third US carrier group reaches the Gulf.
- **Asia-Pacific (6):** Russian warplanes enter South Korea's
  air-defence zone; Japan manufacturing PMI 53.7; a 5.6-magnitude
  quake in Nepal; China opens Tiangong to Pakistan's Zeeshan Ali;
  Taiwan stocks hit the daily limit-up (+9%); Bangladesh vaccinates
  50 million children against typhoid.
- **Africa (3):** Somalia and Uganda step up operations against
  al-Shabaab; 24 killed, including seven children, in South Sudan;
  Tripoli demands answers from Kyiv over the Libya attack.
- **Latin America (3):** Mexico tries "El Chapo Isidro" despite a US
  extradition request; a US drone overflight helps capture a Sinaloa
  drug lord; El Salvador names three troops killed in Haiti.
- **World (1):** UN chief Guterres wants a multilateral AI-risk
  framework within a year.

**By the numbers:** 190 nations at COP31 · 50 hours of overtime ·
7 sea drones · 25 airspace violations · $952bn Nvidia gain.
**Markets:** NVDA +31.5%, Nasdaq +6.5%, S&P 500 +4.7%, Dow +1,448,
Taiwan +9.0%, CoreWeave +22.3%, Dell +20%, Micron +18%.

## Sources

Reuters, CNN, The Wall Street Journal, The Times, Le Monde, IRNA,
Middle East Eye, The Conversation, Grist — all reporting published
Tuesday 24 November 2026. Every story was first reported on
24 November 2026. All panels are flat-drawn illustrations (Pillow);
no photographs are used.

## Method

`draw_poster.py` draws the atlas at 1024×1024 with Pillow
(stdlib + Pillow only) and writes the bundled `entry.png`
(213,021 bytes, under the 1 MiB cap). `main.py` only reads that
bundled file, verifies its PNG header, dimensions, size and SHA-256,
and copies it to `$MAKEFUN_OUTPUT_DIR` (default `/output`), so two
runs write identical bytes. It never writes into the repository,
never fetches anything, and never rolls a die.

## Run it

```sh
python3 draw_poster.py        # regenerate entry.png from scratch
python3 main.py               # copy entry.png to /output/entry.png
python3 main.py --output /tmp/entry.png
python3 main.py --verify      # dimensions, size, SHA-256, no writes
python3 main.py --stories     # list the three leads
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=5hwq4sqk&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
