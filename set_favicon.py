#!/usr/bin/env python3
"""Build a clean favicon from the real TE+TC monogram arrow paths (the recognizable
chevrons), on a white rounded square, base64-inline it, and replace the <link rel=icon>
line in index.html. Keeps the app self-contained/offline."""
import base64
import re

INDEX = "/Users/taylor/Desktop/Coding/Hydraulic Student Companion/index.html"

# Arrow paths lifted verbatim from assets copy/logo-tetc-monogram.svg (the three
# colored swooshes). Tiny gray letters are dropped: illegible at favicon size.
ARROW_ORANGE = ("M103 510.3 100.9 506.9 98.8 510.3 100.7 510.3 100.7 517.1C100.7 520.7 "
                "97.8 523.5 94.3 523.5L65.8 523.5 65.8 524 94.3 524C98.1 524 101.2 520.9 "
                "101.2 517.1L101.2 510.3 103.1 510.3Z")
ARROW_MAGENTA = ("M94.8 500 94.8 498.1C94.8 494.3 91.7 491.2 87.9 491.2L85.4 491.2 86.9 "
                 "491.2 65.7 491.2 65.7 491.7 86.9 491.7 85.4 491.7 87.9 491.7C91.5 491.7 "
                 "94.3 494.6 94.3 498.1L94.3 500 92.4 500 94.5 503.4 96.6 500 94.7 500Z")
ARROW_TEAL = ("M88.5 500.3C88.5 496.7 91 494.5 94.5 494.5L104.7 494.5 104.7 496.4 108.1 "
              "494.3 104.7 492.2 104.7 494.1 94.5 494.1C90.7 494.1 88 496.6 88 500.4L88 "
              "501.5C88 505.1 85 507.6 81.5 507.6L79.4 507.6 79.9 507.6 65.7 507.6 65.7 "
              "508.1 79.9 508.1 79.4 508.1 81.5 508.1C85.3 508.1 88.5 505.3 88.5 501.5L88.5 500.4Z")

# Square viewBox centered on the arrows (arrows span ~x65.7-108.1, y491.2-524).
svg = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="61 482 52 52">'
    '<rect x="61" y="482" width="52" height="52" rx="9" fill="#ffffff"/>'
    f'<path d="{ARROW_ORANGE}" fill="#E8943A"/>'
    f'<path d="{ARROW_MAGENTA}" fill="#BD2F7F"/>'
    f'<path d="{ARROW_TEAL}" fill="#0DB4AE"/>'
    '</svg>'
)

b64 = base64.b64encode(svg.encode("utf-8")).decode("ascii")
link = f'  <link rel="icon" href="data:image/svg+xml;base64,{b64}" />'

html = open(INDEX, encoding="utf-8").read()
new, n = re.subn(r'[ \t]*<link rel="icon"[^\n]*\n', link + "\n", html)
if n != 1:
    raise SystemExit(f"Expected to replace exactly 1 icon link, replaced {n}.")
open(INDEX, "w", encoding="utf-8").write(new)
print(f"Favicon replaced. SVG {len(svg)} bytes -> {len(b64)} b64 chars.")
