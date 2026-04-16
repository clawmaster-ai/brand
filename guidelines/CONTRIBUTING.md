# Contributing to Brand Assets

## Naming conventions

```
logos/{brand}/animated/v{N}-animated.svg
logos/{brand}/static/{color}.svg          # amber | teal | white | black
logos/{brand}/wordmarks/{theme}/{layout}.png  # theme: dark|white, layout: horizontal|stacked|compact
icons/icon-{size}.png
marketing/{type}/{lang}.png               # type: readme|og, lang: en|zh|jp
```

Never use spaces in filenames. Use lowercase and hyphens.

---

## SVG requirements

All SVG files must pass validation (`scripts/validate.py`):

- **Transparent background** — no `background:` in `style`, no `<rect>` filling the canvas
- **currentColor** — use `fill="currentColor"` and `stroke="currentColor"` for the base marks. Explicit color variants (`white.svg`, `black.svg`, `amber.svg`) may hardcode their specific color.
- **ViewBox only** — use `viewBox="0 0 100 100"`, remove fixed `width`/`height` attributes (except favicon which may set `width="32" height="32"`)
- **No inline background styles** — `style="background:white"` fails validation

---

## PNG requirements

- Icon PNGs must have **transparent backgrounds** (RGBA, corner alpha = 0)
- Wordmark PNGs may have opaque backgrounds (dark or white) — these are presentation assets
- **White-background wordmarks**: background must be `#FFFFFF` — no dark gradients, no vignette

---

## Adding a new asset via AI generation

All prompts are stored in `prompts/` for reproducibility. When generating new assets:

1. Copy the closest existing prompt as a starting point
2. Use this framing for **white-background wordmarks** (avoids Gemini dark gradients):
   ```
   Flat 2D brand identity guideline page. [aspect] format.
   Page from a brand manual. Flat, clinical, 2D. Not a photo.
   BACKGROUND: Pure flat white #FFFFFF — all edges, all corners. No gradient. No shadow. No vignette. No dark floor.
   ...
   OUTPUT: Flat 2D vector graphic. Pure white background. No photography. No effects.
   ```
3. Do **not** use dark-background images as `--ref` for white-bg generations — this causes dark gradient contamination
4. Run pixel verification after generation:
   ```bash
   python3 scripts/validate.py --check-white output/white-*.png
   ```

### Recommended tools

- [baoyu-imagine](https://github.com/baoyu/baoyu-imagine) — Google Gemini / OpenAI image generation
- Provider: `google`, model: `gemini-3-pro-image-preview`, quality: `2k`

---

## Pull request checklist

- [ ] Assets follow naming conventions
- [ ] SVGs pass `scripts/validate.py`
- [ ] Icon PNGs have transparent backgrounds
- [ ] White wordmark PNGs have pure white backgrounds (no dark gradients)
- [ ] `tokens/brand-tokens.json` updated if adding a new brand
- [ ] Prompts committed to `prompts/` if AI-generated
