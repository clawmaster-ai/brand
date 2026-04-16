# Logo Usage Guidelines

## Which variant to use

| Context | Use |
|---|---|
| Dark UI / product interface | `static/teal.svg` or `static/amber.svg` (set `color` via CSS) |
| Light UI / white background | `static/white.svg` ← always dark bg, or `static/black.svg` for light bg |
| Web favicon | `icons/favicon.svg` |
| Web animated (hero, splash) | `animated/v4-animated.svg` or `v3-animated.svg` |
| README header | `marketing/readme/{en,zh,jp}.png` |
| Social share / OG | `marketing/og/{en,zh,jp}.png` |
| GitHub repo social preview | `marketing/social-preview.png` |
| App icon (iOS / PWA / desktop) | `icons/` — see platform sizes below |

---

## Platform icon sizes

| File | Size | Platform |
|---|---|---|
| `favicon.svg` | Scalable | Web browser tab |
| `apple-touch-icon.png` | 180×180 | iOS home screen |
| `icon-192.png` | 192×192 | PWA / Android |
| `icon-512.png` | 512×512 | PWA large / maskable |
| `tauri/32x32.png` | 32×32 | Desktop taskbar |
| `tauri/128x128.png` | 128×128 | Desktop app icon |
| `tauri/icon.icns` | Multi-size | macOS |
| `tauri/icon.ico` | Multi-size | Windows |

All PNG icons have **transparent backgrounds**.

---

## Clear space

Minimum clear space around the mark: **20% of the mark's height** on all sides. Never place the mark against a competing graphic without adequate breathing room.

---

## Minimum sizes

| Context | Min size |
|---|---|
| Digital favicon | 16×16px |
| App icon | 32×32px |
| Wordmark with text | mark height ≥ 24px |

---

## Color on backgrounds

| Background | Use |
|---|---|
| Dark (`#02080E`, `#0C0804`, any dark) | Teal / Amber / White variant |
| White / light | Black variant or `color: #1A1A1A` via CSS |
| Colorful / photographic | White variant |

---

## Do's ✓

- Use `currentColor` SVGs — set color via CSS `color` property
- Use white wordmarks on dark sections of README
- Use dark wordmarks on product documentation pages
- Keep the mark on its brand background in presentations

## Don'ts ✗

- Don't stretch or distort the mark
- Don't add drop shadows or outer glows to the SVG mark
- Don't place the mark on a background that clashes with the jewel tone
- Don't use the amber mark on a navy background or vice versa
- Don't use WordArt-style effects on the wordmark text
- Don't use ZH/JP text inside wordmark images (use CSS text instead)
