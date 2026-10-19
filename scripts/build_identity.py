#!/usr/bin/env python3
"""Build the original Knowlet identity assets using only Python's standard library."""

from html import escape
from math import cos, pi, sin
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"

THEMES = {
    "dark": {
        "bg": "#0b1418", "fg": "#edf5ee", "muted": "#9ab1b5",
        "line": "#24373c", "accent": "#cbf278", "teal": "#66d7ca",
        "grid": "#142529", "ink": "#172a29",
    },
    "light": {
        "bg": "#f3f6f2", "fg": "#122d2a", "muted": "#536864",
        "line": "#d1ddd7", "accent": "#497323", "teal": "#007e78",
        "grid": "#e4ebe5", "ink": "#e0eadc",
    },
}

# Bespoke geometric letterforms; no external or embedded font is needed for the wordmark.
GLYPHS = {
    "K": (84, "M0 0H18V46L60 0H83L39 54L84 112H62L18 55V112H0Z"),
    "N": (87, "M0 0H18L69 79V0H87V112H69L18 33V112H0Z"),
    "O": (91, "M28 0H63Q91 0 91 28V84Q91 112 63 112H28Q0 112 0 84V28Q0 0 28 0ZM29 18Q18 18 18 29V83Q18 94 29 94H62Q73 94 73 83V29Q73 18 62 18Z"),
    "W": (128, "M0 0H20L38 83L55 24H73L90 83L108 0H128L101 112H81L64 56L47 112H27Z"),
    "L": (76, "M0 0H18V94H76V112H0Z"),
    "E": (78, "M0 0H78V18H18V47H67V65H18V94H78V112H0Z"),
    "T": (92, "M0 0H92V18H55V112H37V18H0Z"),
}


def wordmark(x: float, y: float, scale: float, color: str) -> str:
    pieces = [f'<g transform="translate({x} {y}) scale({scale})" fill="{color}" fill-rule="evenodd">']
    offset = 0
    for letter in "KNOWLET":
        width, path = GLYPHS[letter]
        pieces.append(f'<path transform="translate({offset} 0)" d="{path}"/>')
        offset += width + 12
    return "\n".join(pieces) + "</g>"


def text(x, y, content, size, color, *, mono=False, spacing=0, weight=400, anchor="start"):
    font = "ui-monospace, SFMono-Regular, Consolas, monospace" if mono else "Arial, Helvetica, sans-serif"
    return (
        f'<text x="{x}" y="{y}" fill="{color}" font-family="{font}" '
        f'font-size="{size}" font-weight="{weight}" letter-spacing="{spacing}" '
        f'text-anchor="{anchor}">{escape(content)}</text>'
    )


def point(t: float, p: float):
    """Project a toroidal field into a small, deliberately abstract signal sculpture."""
    radius = 83 + 35 * cos(p)
    x = radius * cos(t)
    y = radius * sin(t)
    z = 35 * sin(p)
    # Orthographic rotations around x and z keep the silhouette deterministic.
    yy, zz = y * cos(0.82) - z * sin(0.82), y * sin(0.82) + z * cos(0.82)
    xx, yy = x * cos(-0.48) - yy * sin(-0.48), x * sin(-0.48) + yy * cos(-0.48)
    return xx, yy, zz


def path_for(points):
    return "M" + " L".join(f"{x:.2f} {y:.2f}" for x, y, _ in points) + " Z"


def sculpture(x, y, scale, c):
    pieces = [f'<g transform="translate({x} {y}) scale({scale})" fill="none">']
    pieces.append(f'<circle r="155" stroke="{c["line"]}" stroke-width="0.8"/>')
    pieces.append(f'<circle r="139" stroke="{c["line"]}" stroke-width="0.8" stroke-dasharray="2 10"/>')
    for i in range(28):
        p = 2 * pi * i / 28
        points = [point(2 * pi * j / 96, p) for j in range(96)]
        pieces.append(f'<path d="{path_for(points)}" stroke="{c["teal"]}" stroke-width="0.65" opacity="0.36"/>')
    for i in range(32):
        t = 2 * pi * i / 32
        points = [point(t, 2 * pi * j / 40) for j in range(40)]
        pieces.append(f'<path d="{path_for(points)}" stroke="{c["teal"]}" stroke-width="0.7" opacity="0.48"/>')
    # A single quiet pulse follows the outer ring. The base image is complete without motion.
    pieces.append(f'<g class="signal"><circle cx="155" cy="0" r="4.2" fill="{c["accent"]}"/>'
                  f'<circle cx="155" cy="0" r="9" stroke="{c["accent"]}" opacity="0.28"/></g>')
    for dx, dy in [(-166, -138), (166, -138), (-166, 138), (166, 138)]:
        pieces.append(f'<path d="M{dx-5} {dy}h10 M{dx} {dy-5}v10" stroke="{c["muted"]}" stroke-width="1"/>')
    pieces.append("</g>")
    return "\n".join(pieces)


def svg_open(width, height, title, desc, c):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title>
<desc id="desc">{escape(desc)}</desc>
<style>
.signal {{ transform-origin: 0px 0px; animation: orbit 24s linear infinite; }}
@keyframes orbit {{ to {{ transform: rotate(360deg); }} }}
@media (prefers-reduced-motion: reduce) {{ .signal {{ animation: none; }} }}
</style>
<rect x="0.5" y="0.5" width="{width-1}" height="{height-1}" rx="14" fill="{c['bg']}" stroke="{c['line']}"/>
'''


def hero(theme, mobile=False):
    c = THEMES[theme]
    width, height = (640, 630) if mobile else (1200, 440)
    pieces = [svg_open(width, height, "KNOWLET — Albert Hsieh", "Systems, security, and applied AI. A developer in Taipei, Taiwan. Original geometric wordmark and an abstract toroidal signal field.", c)]
    # Fine drafting marks hold the composition together without fake status or metrics.
    top = 73 if mobile else 70
    pad = 32 if mobile else 48
    pieces.append(f'<path d="M{pad} {top}H{width-pad}" stroke="{c["line"]}"/>')
    pieces.append(f'<path d="M{pad} 31v16 M{pad+8} 39l10-8 M{pad+8} 39l10 8" fill="none" stroke="{c["accent"]}" stroke-width="3"/>')
    pieces.append(text(pad+34, 45, "ENGINEERING / FIELD NOTES", 12 if not mobile else 14, c["muted"], mono=True, spacing=1))
    if not mobile:
        pieces.append(text(width-pad, 45, "TAIPEI, TW  /  UTC+8", 12, c["muted"], mono=True, spacing=1, anchor="end"))
        pieces.append(text(pad, 123, "ALBERT HSIEH", 16, c["muted"], mono=True, spacing=4))
        pieces.append(wordmark(pad, 151, 0.86, c["fg"]))
        pieces.append(text(pad, 295, "Systems. Security. Applied AI.", 26, c["fg"], weight=400))
        pieces.append(text(pad, 332, "Curiosity, down to the implementation.", 18, c["muted"]))
        pieces.append(sculpture(970, 221, 0.97, c))
        pieces.append(f'<path d="M{pad} 379H{width-pad}" stroke="{c["line"]}"/>')
        pieces.append(text(pad, 411, "01 / BUILD", 13, c["accent"], mono=True, spacing=1.5))
        pieces.append(text(269, 411, "02 / BREAK", 13, c["teal"], mono=True, spacing=1.5))
        pieces.append(text(489, 411, "03 / UNDERSTAND", 13, c["muted"], mono=True, spacing=1.5))
        pieces.append(text(width-pad, 411, "knowlet / open source", 12, c["muted"], mono=True, anchor="end"))
    else:
        pieces.append(text(pad, 119, "ALBERT HSIEH", 17, c["muted"], mono=True, spacing=3.4))
        pieces.append(wordmark(pad, 146, 0.71, c["fg"]))
        pieces.append(text(pad, 269, "Systems. Security. Applied AI.", 27, c["fg"]))
        pieces.append(text(pad, 305, "Curiosity, down to the implementation.", 20, c["muted"]))
        pieces.append(sculpture(448, 442, 0.78, c))
        pieces.append(text(pad, 379, "01 / BUILD", 16, c["accent"], mono=True, spacing=1))
        pieces.append(text(pad, 421, "02 / BREAK", 16, c["teal"], mono=True, spacing=1))
        pieces.append(text(pad, 463, "03 / UNDERSTAND", 16, c["muted"], mono=True, spacing=1))
        pieces.append(f'<path d="M{pad} 575H{width-pad}" stroke="{c["line"]}"/>')
        pieces.append(text(pad, 609, "TAIPEI, TW / UTC+8", 14, c["muted"], mono=True))
        pieces.append(text(width-pad, 609, "knowlet / open source", 13, c["muted"], mono=True, anchor="end"))
    pieces.append("</svg>\n")
    return "\n".join(pieces)


def footer(theme):
    c = THEMES[theme]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="68" viewBox="0 0 1200 68" role="img" aria-label="Build. Break. Understand.">
<path d="M0 1H1200" stroke="{c['line']}"/>
<path d="M1 24v21 M10 34l12-10 M10 34l12 11" fill="none" stroke="{c['accent']}" stroke-width="3"/>
{text(44, 42, 'BUILD. BREAK. UNDERSTAND.', 13, c['muted'], mono=True, spacing=2)}
{text(1200, 42, 'KNOWLET', 13, c['muted'], mono=True, spacing=2, anchor='end')}
</svg>
'''


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for theme in THEMES:
        for mobile in (False, True):
            suffix = f"mobile-{theme}" if mobile else theme
            (OUT / f"hero-{suffix}.svg").write_text(hero(theme, mobile), encoding="utf-8")
        (OUT / f"footer-{theme}.svg").write_text(footer(theme), encoding="utf-8")
    print("Built 6 original identity SVGs.")


if __name__ == "__main__":
    main()
