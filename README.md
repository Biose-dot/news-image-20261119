# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Biose-dot/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Biose-dot/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

**The World in One Day** — a single 1024×1024 poster summing up the world news of **Thursday, 19 November 2026**. The image (`entry.png`) is drawn entirely from source by `build_image.py` (Python + Pillow); `main.ts` hands it to the grader by copying it to `/output/entry.png`.

## The day's stories on the poster

1. **Shenzhen — Trump, Xi & Putin hold first three-way summit.** The US, Chinese and Russian presidents meet together for the first time, on the sidelines of the APEC forum; Ukraine and nuclear arms control (with New START expired) top the agenda.
2. **Ukraine strikes the Crimean Bridge again** — a third strike in a week; traffic across the Kerch Strait bridge suspended.
3. **ICJ rules on the Rohingya genocide case** — the UN's top court in The Hague delivers judgment in The Gambia's case against Myanmar over the 2017 crackdown.
4. **Iran attacks Gulf states after a US strike on Qeshm Island** — Kuwait repels its first Iranian attack in two months; a missile threat on Riyadh is intercepted.
5. **COP31, Antalya** — ministers race to unblock the climate deal in the summit's final phase in Türkiye.
6. **Anthropic's record $81bn IPO** — the AI firm's market debut raises $81.3 billion and values it near $1.5 trillion, passing SpaceX's mark.
7. **Record 589 million children live in conflict zones** — Save the Children's report: nearly one in four children worldwide lived close to war in 2025.

Every story was reported on 19 November 2026 by at least two of the sources below.

## Sources

- Open Chronicle — Global News Brief, 19 November 2026: https://openchronicle.org/2026/11/19/global-news-brief-key-developments-around-the-world-november-19-2026/
- Horizon — World news and markets for 19 November 2026: https://www.horizonapp.link/en/2026/11/19
- One Turn News — Trump, Xi, Putin Meet in Shenzhen (19 Nov 2026 edition): https://oneturn.news/news/
- AppiSToS — World, 19.11.2026: https://www.appistos.gr/en/diethni.html
- News Media House — World: https://www.newsmediahouse.com/section/world/

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

This writes the poster to `out/entry.png`. To redraw the poster from source: `python3 build_image.py`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=tvfbjxfd&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
