#!/usr/bin/env python3
"""
Brand asset validator.
Checks SVG cleanliness and PNG transparency requirements.
Run: python scripts/validate.py
"""

import os
import sys
import glob

errors = []
warnings = []

# ── SVG validation ────────────────────────────────────────────────────────────

SVG_FORBIDDEN = [
    ('background:',      'SVG has inline background style — must be transparent'),
    ('background-color', 'SVG has background-color style'),
    ('<rect.*fill.*width="100%', 'SVG has full-canvas background rect'),
]

BASE_SVGS = glob.glob('logos/**/*.svg', recursive=True) + glob.glob('icons/*.svg')

for path in sorted(BASE_SVGS):
    content = open(path).read()

    # Check for forbidden patterns
    for pattern, message in SVG_FORBIDDEN:
        import re
        if re.search(pattern, content, re.IGNORECASE):
            errors.append(f'SVG {path}: {message}')

    # Check: base marks (not explicit color variants) should use currentColor
    name = os.path.basename(path)
    if name in ('teal.svg', 'amber.svg') or 'animated' in path:
        if 'currentColor' not in content:
            warnings.append(f'SVG {path}: expected currentColor but not found')

    # Check: no fixed width/height on base marks (except favicon)
    if name != 'favicon.svg' and 'animated' not in path and 'static' in path:
        if 'width="500"' in content or 'height="500"' in content:
            errors.append(f'SVG {path}: has fixed 500px dimensions — remove width/height, keep viewBox only')

print(f'SVG: checked {len(BASE_SVGS)} files')

# ── PNG transparency validation ───────────────────────────────────────────────

try:
    from PIL import Image

    ICON_PNGS = glob.glob('icons/**/*.png', recursive=True) + glob.glob('icons/*.png')

    for path in sorted(ICON_PNGS):
        img = Image.open(path)
        if img.mode != 'RGBA':
            errors.append(f'PNG {path}: mode={img.mode} — icon PNGs must be RGBA (transparent bg)')
            continue
        corner = img.getpixel((0, 0))
        if corner[3] != 0:
            errors.append(f'PNG {path}: corner alpha={corner[3]} — background must be fully transparent (alpha=0)')

    print(f'PNG icons: checked {len(ICON_PNGS)} files')

    # White-bg wordmarks: verify no dark pixels at edges
    WHITE_PNGS = glob.glob('logos/**/wordmarks/white/*.png', recursive=True)
    for path in sorted(WHITE_PNGS):
        img = Image.open(path).convert('RGB')
        w, h = img.size
        edge_pts = [(0,0),(w-1,0),(0,h-1),(w-1,h-1),(w//2,h-1),(w//2,0)]
        dark = [(x,y,img.getpixel((x,y))) for x,y in edge_pts if min(img.getpixel((x,y))) < 200]
        if dark:
            errors.append(f'PNG {path}: dark pixels at edges {dark[:2]} — white wordmarks must have pure white bg')

    print(f'PNG white wordmarks: checked {len(WHITE_PNGS)} files')

except ImportError:
    warnings.append('Pillow not installed — PNG checks skipped')

# ── Report ────────────────────────────────────────────────────────────────────

print()
for w in warnings:
    print(f'  WARN  {w}')
for e in errors:
    print(f'  FAIL  {e}')

if errors:
    print(f'\n{len(errors)} error(s) found. Fix before merging.')
    sys.exit(1)
else:
    print(f'All checks passed ✓  ({len(warnings)} warning(s))')
