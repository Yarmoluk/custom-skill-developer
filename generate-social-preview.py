#!/usr/bin/env python3
"""Generate Cognify-branded social preview matching cognify-skills style."""

from PIL import Image, ImageDraw, ImageFont
import os

# Canvas — GitHub social preview (1280x640)
W, H = 1280, 640
img = Image.new("RGB", (W, H), (14, 17, 23))
draw = ImageDraw.Draw(img)

# === BACKGROUND: dark gradient (top-left lighter, bottom-right darker) ===
for y in range(H):
    for x in range(0, W, 4):  # step 4 for speed
        # Radial-ish gradient from top-left
        dist = ((x / W) * 0.6 + (y / H) * 0.8)
        r = int(18 - dist * 8)
        g = int(22 - dist * 9)
        b = int(32 - dist * 12)
        r = max(10, min(25, r))
        g = max(12, min(28, g))
        b = max(18, min(38, b))
        draw.rectangle([(x, y), (x + 3, y)], fill=(r, g, b))

# === FONTS ===
def get_font(name, size):
    paths = [
        f"/System/Library/Fonts/{name}.ttc",
        f"/System/Library/Fonts/{name}.ttf",
        f"/Library/Fonts/{name}.ttf",
        f"/Library/Fonts/{name}.ttc",
        f"/System/Library/Fonts/Supplemental/{name}.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()

font_badge = get_font("HelveticaNeue", 16)
font_title_blue = get_font("HelveticaNeue", 72)
font_title_white = get_font("HelveticaNeue", 72)
font_subtitle = get_font("HelveticaNeue", 24)
font_pill = get_font("HelveticaNeue", 17)

# === TOP BADGE: "AGENT SKILLS OPEN STANDARD" ===
badge_text = "AGENT SKILLS OPEN STANDARD"
badge_x = 70
badge_y = 160

# Badge background — subtle blue-tinted bar
badge_bbox = draw.textbbox((0, 0), badge_text, font=font_badge)
badge_w = badge_bbox[2] - badge_bbox[0]
badge_h = badge_bbox[3] - badge_bbox[1]
# Thin line across most of width
line_y = badge_y + badge_h // 2
draw.line([(badge_x, line_y + 12), (W - 70, line_y + 12)], fill=(35, 45, 60), width=1)
# Badge pill background
pill_pad_x = 12
pill_pad_y = 6
draw.rounded_rectangle(
    [(badge_x - pill_pad_x, badge_y - pill_pad_y),
     (badge_x + badge_w + pill_pad_x, badge_y + badge_h + pill_pad_y)],
    radius=4,
    fill=(20, 30, 45),
    outline=(40, 55, 75),
    width=1
)
draw.text((badge_x, badge_y), badge_text, fill=(120, 160, 200), font=font_badge)

# === TITLE: "Cognify" in blue, "Skill Developer" in white ===
title_y = 220
# "Cognify" in blue
cognify_text = "Cognify"
draw.text((70, title_y), cognify_text, fill=(60, 150, 255), font=font_title_blue)
cognify_bbox = draw.textbbox((70, title_y), cognify_text, font=font_title_blue)
cognify_w = cognify_bbox[2] - cognify_bbox[0]

# "Skill Developer" in white, same line
rest_text = " Skill Developer"
draw.text((70 + cognify_w, title_y), rest_text, fill=(255, 255, 255), font=font_title_white)

# === SUBTITLE ===
subtitle = "The comprehensive guide to building Agent Skills"
draw.text((70, title_y + 90), subtitle, fill=(140, 150, 165), font=font_subtitle)

# === CATEGORY PILLS ===
pills = [
    "17 Chapters",
    "82K Words",
    "4 MicroSims",
    "Quality Scoring",
    "Meta-Skill Routing",
    "Pipeline Orchestration",
]

pill_y = title_y + 155
pill_x = 70
pill_gap = 12
pill_pad_x = 16
pill_pad_y = 8

for pill_text in pills:
    p_bbox = draw.textbbox((0, 0), pill_text, font=font_pill)
    p_w = p_bbox[2] - p_bbox[0]
    p_h = p_bbox[3] - p_bbox[1]

    # Pill background
    draw.rounded_rectangle(
        [(pill_x, pill_y),
         (pill_x + p_w + pill_pad_x * 2, pill_y + p_h + pill_pad_y * 2)],
        radius=6,
        fill=(22, 28, 38),
        outline=(40, 50, 65),
        width=1
    )
    draw.text((pill_x + pill_pad_x, pill_y + pill_pad_y), pill_text, fill=(180, 190, 205), font=font_pill)

    pill_x += p_w + pill_pad_x * 2 + pill_gap

# === SAVE ===
output_dir = os.path.dirname(os.path.abspath(__file__))
output = os.path.join(output_dir, "social-preview.png")
img.save(output, "PNG", quality=95)
print(f"Social preview saved to: {output}")
print(f"Size: {os.path.getsize(output) / 1024:.0f}KB")

# Also copy to docs/images for the README
import shutil
banner_dest = os.path.join(output_dir, "docs", "images", "social-preview.png")
shutil.copy2(output, banner_dest)
print(f"Copied to: {banner_dest}")
