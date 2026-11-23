#!/usr/bin/env python3
"""Render the 23 November 2026 news-image entry (1024x1024 PNG).

Fresh build for make.fun news-image-20261123. All facts verified against
real sources on the morning of Monday 23 November 2026 (see BUILD_NOTES.md).
Draws a newspaper front page with PIL only; no network, no photos.
"""
import math
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 244, 236)
INK = (25, 25, 25)
RED = (158, 27, 30)
BLUE = (31, 78, 121)
GREY = (90, 86, 78)
LIGHT = (233, 227, 214)
DARKSTRIP = (28, 28, 30)

F = "/usr/share/fonts/truetype/noto/"
SERIF_BLACK = F + "NotoSerif-Black.ttf"
SERIF_BOLD = F + "NotoSerif-Bold.ttf"
SERIF = F + "NotoSerif-Regular.ttf"
SANS_BLACK = F + "NotoSans-Black.ttf"
SANS_BOLD = F + "NotoSans-Bold.ttf"
SANS = F + "NotoSans-Regular.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap using measured widths."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, max_w, leading, fill=INK):
    lines = wrap(draw, text, fnt, max_w)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def rule(draw, x0, y, x1, w=2, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=w)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---- Masthead ------------------------------------------------------------
d.text((W // 2, 18), "THE WORLD TODAY", font=font(SERIF_BLACK, 88),
       fill=INK, anchor="ma")
rule(d, 40, 128, 984, 4, RED)
d.text((W // 2, 140), "MONDAY, 23 NOVEMBER 2026",
       font=font(SANS_BLACK, 36), fill=RED, anchor="ma")
d.text((W // 2, 188), "ONE DAY  •  ONE PAGE  •  THE WORLD, AS REPORTED BY MONDAY MORNING",
       font=font(SANS_BOLD, 17), fill=GREY, anchor="ma")
rule(d, 40, 222, 984, 2, INK)

# ---- Lead story: COP31 collapses -----------------------------------------
y = 242
d.text((40, y), "CLIMATE  —  ANTALYA, TURKEY", font=font(SANS_BLACK, 21),
       fill=RED)
y += 30
headline = "Climate talks collapse — no deal"
hl_font = font(SERIF_BOLD, 46)
y = para(d, 40, y, headline, hl_font, 600, 50)
y += 6
body = ("Nearly 200 nations leave Antalya empty-handed after the EU and "
        "others reject a final draft that never names fossil fuels. The "
        "longest COP on record ends with no cover deal.")
body_font = font(SANS, 21)
y = para(d, 40, y, body, body_font, 600, 28)
y += 6
d.text((40, y), "President Kurum: “There is no agreement on this text.”",
       font=font(SANS_BOLD, 22), fill=BLUE)

# Lead art panel: globe under a hot sun, right side
ax0, ay0, ax1, ay1 = 672, 242, 984, 452
d.rectangle([ax0, ay0, ax1, ay1], fill=(214, 232, 240), outline=INK, width=3)
# sun
d.ellipse([ax0 + 218, ay0 + 12, ax0 + 292, ay0 + 86], fill=(230, 126, 34))
for ang in range(0, 360, 45):
    cx, cy = ax0 + 255, ay0 + 49
    x1 = cx + 48 * math.cos(math.radians(ang))
    y1 = cy + 48 * math.sin(math.radians(ang))
    x2 = cx + 62 * math.cos(math.radians(ang))
    y2 = cy + 62 * math.sin(math.radians(ang))
    d.line([(x1, y1), (x2, y2)], fill=(230, 126, 34), width=5)
# globe
gx, gy, gr = ax0 + 110, ay0 + 118, 58
d.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], fill=(46, 111, 164),
          outline=INK, width=3)
d.ellipse([gx - 26, gy - gr, gx + 26, gy + gr], outline=(248, 244, 236), width=2)
d.line([(gx - gr, gy), (gx + gr, gy)], fill=(248, 244, 236), width=2)
d.arc([gx - gr, gy - 34, gx + gr, gy + 34], 200, 340,
      fill=(248, 244, 236), width=2)
# land blobs
d.ellipse([gx - 48, gy - 30, gx - 8, gy + 2], fill=(96, 160, 90))
d.ellipse([gx + 2, gy + 6, gx + 44, gy + 44], fill=(96, 160, 90))
d.text((ax0 + 156, ay1 - 26), "NO DEAL IN ANTALYA", font=font(SANS_BLACK, 17),
       fill=RED, anchor="ma")

rule(d, 40, 500, 984, 2, INK)

# ---- Three secondary stories ---------------------------------------------
cols = [
    ("FOOTBALL  —  ANFIELD", "Liverpool 4, United 0: Pochettino's horror debut",
     "Yoro sent off after 8 minutes; Szoboszlai and Wirtz strike in two "
     "minutes.",
     "ball"),
    ("CRICKET  —  WELLINGTON", "India's record 720 sets up a final day",
     "Day 5, Monday: India declared on 720 for 9 — a record. NZ 139 "
     "for 4, trail by 213.",
     "bat"),
    ("SCIENCE  —  A FAMOUS PROOF", "Maths proof certified — but not yet solved",
     "Lean and Mathlib certify the claimed Riemann proof; all 175,187 "
     "modules pass. Clay prize still open.",
     "pi"),
]
col_w, gap = 304, 16
x = 40
y0 = 518
for kicker, head, body, art in cols:
    d.text((x, y0), kicker, font=font(SANS_BLACK, 17), fill=RED)
    hy = para(d, x, y0 + 26, head, font(SERIF_BOLD, 26), col_w, 31)
    by = para(d, x, hy + 6, body, font(SANS, 17), col_w, 22)
    # small drawn icon at bottom of column (no caption: keeps clear of rule)
    iy = 712
    if art == "bat":
        d.rectangle([x + 90, iy, x + 210, iy + 12], fill=(160, 110, 60),
                    outline=INK, width=2)
        d.rectangle([x + 195, iy + 2, x + 250, iy + 10], fill=(120, 80, 40),
                    outline=INK, width=2)
        d.ellipse([x + 40, iy - 26, x + 92, iy + 26], fill=(178, 34, 34),
                  outline=INK, width=2)
    elif art == "ball":
        cx, cy, r = x + 152, iy + 10, 42
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(250, 250, 250),
                  outline=INK, width=3)
        d.polygon([(cx, cy - 16), (cx + 15, cy - 5), (cx + 9, cy + 13),
                   (cx - 9, cy + 13), (cx - 15, cy - 5)], fill=INK)
        d.line([(cx, cy - 16), (cx, cy - r)], fill=INK, width=2)
        d.line([(cx + 15, cy - 5), (cx + r, cy - 8)], fill=INK, width=2)
    else:
        d.text((x + 60, iy - 30), "π", font=font(SERIF_BLACK, 92), fill=BLUE)
        d.text((x + 170, iy - 10), "1  2  3  5\n7  11  13 …",
               font=font(SANS_BOLD, 20), fill=INK)
    x += col_w + gap

rule(d, 40, 792, 984, 2, INK)

# ---- Ticker ---------------------------------------------------------------
ty0, ty1 = 812, 952
d.rectangle([40, ty0, 984, ty1], fill=DARKSTRIP)
d.text((60, ty0 + 12), "THE WEEKEND SO FAR",
       font=font(SANS_BLACK, 20), fill=(255, 196, 66))
ticker = [
    "US Democrats reach 258 House seats, their largest majority since 1992.",
    "UN 'killer robots' talks: rules to be drafted by 2028, no binding deal.",
    "Indonesia candy-factory fire: at least 3 dead, dozens unaccounted for.",
    "Russian drone hits Kyiv supermarket: at least 3 killed, 15 wounded.",
]
ty = ty0 + 40
for item in ticker:
    lines = wrap(d, "•  " + item, font(SANS, 18), 904)
    for ln in lines:
        d.text((60, ty), ln, font=font(SANS, 18), fill=(240, 238, 232))
        ty += 22
    ty += 2

# ---- Footer ---------------------------------------------------------------
d.text((W // 2, 966), "Drawn from reports published by Monday morning  •  Reuters  •  AP  •  Sky Sports  •  ESPNcricinfo",
       font=font(SANS, 16), fill=GREY, anchor="ma")
d.text((W // 2, 990), "THE WORLD TODAY  —  Monday, 23 November 2026",
       font=font(SANS_BOLD, 15), fill=GREY, anchor="ma")

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
