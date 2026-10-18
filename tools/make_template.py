"""Generate the printable A4 sketch template (assets/sketch_squares_A4.png).

Two squares stacked vertically and centered on an A4 page at 300 DPI.
Print at 100% / "Actual size", not "Fit to page".

Usage: python3 tools/make_template.py [output.png]
Requires: Pillow (pip install pillow)
"""
import sys
from PIL import Image, ImageDraw

DPI = 300
PAGE_W_MM, PAGE_H_MM = 210, 297
SQUARE_MM = 130      # side of each square
BORDER_MM = 0.5      # border thickness
GAP_MM = 21          # space between the two squares


def mm(v):
    return round(v / 25.4 * DPI)


def main(out="assets/sketch_squares_A4.png"):
    w, h = mm(PAGE_W_MM), mm(PAGE_H_MM)
    side, border, gap = mm(SQUARE_MM), mm(BORDER_MM), mm(GAP_MM)
    edge = (h - 2 * side - gap) // 2   # equal top and bottom margin
    x = (w - side) // 2

    img = Image.new("RGB", (w, h), "white")
    d = ImageDraw.Draw(img)
    for y in (edge, edge + side + gap):
        d.rectangle([x, y, x + side - 1, y + side - 1], outline="black", width=border)
    img.save(out, dpi=(DPI, DPI))


if __name__ == "__main__":
    main(*sys.argv[1:])
