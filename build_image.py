#!/usr/bin/env python3
"""Draw the news-image-20261119 entry poster from source.

The poster sums up the world news of Thursday 19 November 2026 in one
1024x1024 PNG. Every story below was reported on that day by at least two
of the news services listed in the footer (see README.md for the list).

Run:  python3 build_image.py   ->  writes entry.png beside this file.
Only used at build time; the submitted program (main.ts) just copies the
finished entry.png to /output.
"""

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

NAVY = (13, 27, 46)
PANEL = (22, 40, 63)
PANEL2 = (18, 34, 54)
RED = (200, 16, 46)
GOLD = (240, 183, 60)
WHITE = (245, 247, 250)
GREY = (168, 182, 200)
LIGHT = (214, 224, 238)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, xy, text, fnt, fill, max_w, leading):
    x, y = xy
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def story_card(draw, box, color, kicker, headline, summary):
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=PANEL2)
    draw.rectangle([x0, y0, x1, y0 + 6], fill=color)
    pad = 18
    draw.text((x0 + pad, y0 + 13), kicker, font=font(SANS_B, 18), fill=color)
    y = text_block(
        draw, (x0 + pad, y0 + 38), headline, font(SANS_B, 25), WHITE,
        x1 - x0 - 2 * pad, 30,
    )
    text_block(
        draw, (x0 + pad, y + 6), summary, font(SANS, 17), LIGHT,
        x1 - x0 - 2 * pad, 22,
    )


def main():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)

    # --- Masthead -------------------------------------------------------
    d.text((512, 26), "GLOBAL NEWS IN ONE IMAGE", font=font(SANS_B, 21),
           fill=GOLD, anchor="ma")
    d.text((512, 54), "THE WORLD IN ONE DAY", font=font(SERIF_B, 66),
           fill=WHITE, anchor="ma")
    d.rectangle([0, 138, W, 190], fill=RED)
    d.text((512, 150), "THURSDAY  ·  19 NOVEMBER 2026", font=font(SANS_B, 33),
           fill=WHITE, anchor="ma")

    # --- Lead story: Shenzhen trilateral summit -------------------------
    lead = [24, 204, 1000, 406]
    d.rectangle(lead, fill=PANEL)
    d.rectangle([24, 204, 32, 406], fill=GOLD)
    d.text((56, 218), "SHENZHEN  ·  APEC SUMMIT  ·  TOP STORY",
           font=font(SANS_B, 20), fill=GOLD)
    y = text_block(
        d, (56, 246), "Trump, Xi & Putin hold first three-way summit",
        font(SANS_B, 40), WHITE, 690, 47,
    )
    text_block(
        d, (56, y + 8),
        "First-ever meeting of the US, Chinese and Russian presidents, "
        "on the APEC sidelines. Ukraine and nuclear arms control top "
        "the agenda.",
        font(SANS, 19), LIGHT, 690, 25,
    )
    # Motif: three summit seats as circles over a table line.
    seats = [(806, RED, "USA"), (872, GOLD, "CHN"), (938, (70, 130, 220), "RUS")]
    for cx, col, label in seats:
        d.ellipse([cx - 27, 262, cx + 27, 316], fill=col)
        d.text((cx, 324), label, font=font(SANS_B, 16), fill=WHITE, anchor="ma")
    d.line([782, 360, 962, 360], fill=GREY, width=4)

    # --- Story grid: 2 columns x 3 rows ---------------------------------
    cards = [
        ((24, 418, 506, 590), (232, 84, 84), "EUROPE  ·  WAR IN UKRAINE",
         "Ukraine strikes Crimean Bridge again",
         "Third strike in a week; traffic across the Kerch Strait "
         "bridge is suspended."),
        ((518, 418, 1000, 590), (96, 178, 120), "THE HAGUE  ·  WORLD COURT",
         "ICJ rules on Rohingya genocide case",
         "The UN's top court judges The Gambia's case against Myanmar "
         "over the 2017 crackdown."),
        ((24, 598, 506, 770), (240, 130, 60), "MIDDLE EAST  ·  ESCALATION",
         "Iran attacks Gulf states after US strike",
         "Kuwait repels its first attack in two months; a missile "
         "threat on Riyadh is intercepted."),
        ((518, 598, 1000, 770), (80, 190, 200), "ANTALYA  ·  COP31 CLIMATE",
         "Ministers race to save COP31 climate deal",
         "Final-phase talks in Antalya, Türkiye, strain toward an "
         "agreed text."),
        ((24, 778, 506, 950), (170, 120, 230), "MARKETS  ·  ARTIFICIAL INTELLIGENCE",
         "Anthropic's record $81bn IPO",
         "The AI firm's debut raises $81.3 billion and values it near "
         "$1.5 trillion, passing SpaceX's mark."),
        ((518, 778, 1000, 950), (230, 200, 90), "WORLD  ·  CHILDREN IN WAR",
         "Record 589m children in war zones",
         "Save the Children: nearly 1 in 4 children worldwide lived "
         "close to war in 2025."),
    ]
    for box, color, kicker, headline, summary in cards:
        story_card(d, box, color, kicker, headline, summary)

    # --- Footer ----------------------------------------------------------
    d.text(
        (512, 964),
        "Compiled 19 Nov 2026 from Open Chronicle, Horizon, One Turn News, "
        "AppiSToS and News Media House",
        font=font(SANS, 15), fill=GREY, anchor="ma",
    )

    img.save("entry.png", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()
