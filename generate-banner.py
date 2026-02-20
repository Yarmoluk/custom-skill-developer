#!/usr/bin/env python3
"""Generate Cognify-branded banner for Custom Skill Developer Guide."""

from PIL import Image, ImageDraw, ImageFont
import os

# Canvas — GitHub social preview (1280x640)
W, H = 1280, 640
img = Image.new("RGB", (W, H), (12, 12, 16))
draw = ImageDraw.Draw(img)

# === BACKGROUND LAYERS ===

# Subtle gradient simulation (dark to slightly lighter)
for y in range(H):
    r = int(12 + (y / H) * 8)
    g = int(12 + (y / H) * 8)
    b = int(16 + (y / H) * 12)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# Geometric grid lines (futuristic HUD)
thin_color = (28, 28, 36)

# Horizontal scan lines
for y in range(40, 120, 12):
    draw.line([(80, y), (W - 80, y)], fill=thin_color, width=1)
for y in range(H - 120, H - 40, 12):
    draw.line([(80, y), (W - 80, y)], fill=thin_color, width=1)

# Corner brackets
bracket_color = (50, 50, 62)
draw.line([(60, 35), (60, 75)], fill=bracket_color, width=2)
draw.line([(60, 35), (100, 35)], fill=bracket_color, width=2)
draw.line([(W - 60, 35), (W - 60, 75)], fill=bracket_color, width=2)
draw.line([(W - 60, 35), (W - 100, 35)], fill=bracket_color, width=2)
draw.line([(60, H - 35), (60, H - 75)], fill=bracket_color, width=2)
draw.line([(60, H - 35), (100, H - 35)], fill=bracket_color, width=2)
draw.line([(W - 60, H - 35), (W - 60, H - 75)], fill=bracket_color, width=2)
draw.line([(W - 60, H - 35), (W - 100, H - 35)], fill=bracket_color, width=2)

# Accent glow bar (blue to purple gradient)
bar_y = 175
bar_w = 220
bar_x = (W - bar_w) // 2
for i in range(bar_w):
    ratio = i / bar_w
    r = int(0 + ratio * 88)
    g = int(122 - ratio * 36)
    b = int(255 - ratio * 41)
    draw.line([(bar_x + i, bar_y), (bar_x + i, bar_y + 3)], fill=(r, g, b))

# === TEXT ===

def get_font(name, size):
    paths = [
        f"/System/Library/Fonts/{name}.ttc",
        f"/System/Library/Fonts/{name}.ttf",
        f"/Library/Fonts/{name}.ttf",
        f"/Library/Fonts/{name}.ttc",
        f"/System/Library/Fonts/Supplemental/{name}.ttf",
        f"/System/Library/Fonts/Supplemental/{name}.ttc",
    ]
    for p in paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()

font_wordmark = get_font("HelveticaNeue", 22)
font_title = get_font("HelveticaNeue", 52)
font_subtitle = get_font("HelveticaNeue", 20)
font_meta = get_font("HelveticaNeue", 15)
font_badge = get_font("HelveticaNeue", 13)
font_stat_num = get_font("HelveticaNeue", 34)
font_stat_label = get_font("HelveticaNeue", 11)

# "C O G N I F Y" wordmark
wordmark = "C  O  G  N  I  F  Y"
wm_bbox = draw.textbbox((0, 0), wordmark, font=font_wordmark)
wm_w = wm_bbox[2] - wm_bbox[0]
draw.text(((W - wm_w) // 2, 130), wordmark, fill=(0, 122, 255), font=font_wordmark)

# Title
title = "Custom Skill Developer"
t_bbox = draw.textbbox((0, 0), title, font=font_title)
t_w = t_bbox[2] - t_bbox[0]
draw.text(((W - t_w) // 2, 195), title, fill=(255, 255, 255), font=font_title)

# Subtitle
sub1 = "The Comprehensive Guide to Building Agent Skills"
s1_bbox = draw.textbbox((0, 0), sub1, font=font_subtitle)
s1_w = s1_bbox[2] - s1_bbox[0]
draw.text(((W - s1_w) // 2, 268), sub1, fill=(174, 174, 178), font=font_subtitle)

# Standard line
sub2 = "Built to the agentskills.io open standard"
s2_bbox = draw.textbbox((0, 0), sub2, font=font_meta)
s2_w = s2_bbox[2] - s2_bbox[0]
draw.text(((W - s2_w) // 2, 300), sub2, fill=(99, 99, 102), font=font_meta)

# Divider
div_y = 340
draw.line([(W // 2 - 80, div_y), (W // 2 + 80, div_y)], fill=(50, 50, 58), width=1)

# === STAT CARDS ===
stats = [
    ("17", "Chapters", (0, 122, 255)),
    ("82K", "Words", (88, 86, 214)),
    ("200", "Concepts", (52, 199, 89)),
    ("20+", "Skills Built", (255, 159, 10)),
    ("7", "Dimensions", (255, 255, 255)),
]

card_w = 130
card_h = 70
gap = 20
total = len(stats) * card_w + (len(stats) - 1) * gap
start_x = (W - total) // 2
card_y = 370

for i, (num, label, color) in enumerate(stats):
    cx = start_x + i * (card_w + gap)
    draw.rounded_rectangle(
        [(cx, card_y), (cx + card_w, card_y + card_h)],
        radius=8,
        fill=(25, 25, 32),
        outline=(40, 40, 50),
        width=1
    )
    n_bbox = draw.textbbox((0, 0), num, font=font_stat_num)
    n_w = n_bbox[2] - n_bbox[0]
    draw.text((cx + (card_w - n_w) // 2, card_y + 8), num, fill=color, font=font_stat_num)
    l_bbox = draw.textbbox((0, 0), label, font=font_stat_label)
    l_w = l_bbox[2] - l_bbox[0]
    draw.text((cx + (card_w - l_w) // 2, card_y + 48), label, fill=(120, 120, 125), font=font_stat_label)

# Bottom badge row
badges = ["agentskills.io", "Claude Code", "Claude.ai", "VS Code", "Cursor", "Codex", "Gemini CLI"]
badge_text = "  |  ".join(badges)
b_bbox = draw.textbbox((0, 0), badge_text, font=font_badge)
b_w = b_bbox[2] - b_bbox[0]
draw.text(((W - b_w) // 2, 475), badge_text, fill=(70, 70, 78), font=font_badge)

# Bottom meta line
meta = "Daniel Yarmoluk  |  Cognify  |  2026  |  Apache 2.0"
m_bbox = draw.textbbox((0, 0), meta, font=font_badge)
m_w = m_bbox[2] - m_bbox[0]
draw.text(((W - m_w) // 2, H - 50), meta, fill=(70, 70, 78), font=font_badge)

# === SAVE ===
output_dir = os.path.dirname(os.path.abspath(__file__))
output = os.path.join(output_dir, "docs", "images", "banner.png")
os.makedirs(os.path.dirname(output), exist_ok=True)
img.save(output, "PNG", quality=95)
print(f"Banner saved to: {output}")
print(f"Size: {os.path.getsize(output) / 1024:.0f}KB")

# Also save as social preview
social = os.path.join(output_dir, "social-preview.png")
img.save(social, "PNG", quality=95)
print(f"Social preview saved to: {social}")
