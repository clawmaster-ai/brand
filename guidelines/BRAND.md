# Brand Guidelines

## Brand Architecture

```
OpenMaster        Universe / Platform brand
    └── ClawMaster    Flagship product
    └── XxxMaster     Future products share the same design language:
                      geometric mark + jewel tone + dark background
```

OpenMaster is the umbrella. Each XxxMaster product gets its own geometric mark and distinct jewel-tone color. All share: dark background, geometric mark, single-color glow.

---

## Colors

### OpenMaster
| Token | Hex | Use |
|---|---|---|
| Primary | `#00BCD4` | Mark color, wordmark text |
| Secondary | `#4DD0E1` | Vertex nodes, accents |
| Background | `#02080E` | Deep navy — brand dark bg |

### ClawMaster
| Token | Hex | Use |
|---|---|---|
| Primary | `#F5A623` | Mark color, wordmark text |
| Secondary | `#FFD54F` | Highlights |
| Background | `#0C0804` | Deep warm dark — brand bg |

---

## Typography

| Brand | Wordmark Font | Weight | Notes |
|---|---|---|---|
| OpenMaster | **Inter Light** | 300 | Clean, humanist, digital-native |
| ClawMaster | **Futura Light** | 300 | Geometric, brand-grade (NASA, VW) |

Letter-spacing: `0.06–0.08em` horizontal · `0.14–0.18em` stacked

---

## Logo Marks

### V4 Hex Warrior (OpenMaster)
A regular hexagon with six circular nodes at the vertices, six radial spokes connecting them to one dominant center node. The hexagon outline is dashed at low opacity.

**Animation:** Each node activates independently with a different period (3.5–4.8s) and irregular delay — the pattern never repeats. Center node breathes at 3s. Hex outline rotates imperceptibly at 24s/revolution.

### V3 Command Signal (ClawMaster)
Three concentric semicircular arcs opening to the left, emanating from a solid focal dot. Two accent dots mark the outer arc endpoints.

**Animation:** Arcs pulse outward from focal dot in sequence (inner → outer) with staggered delays. 2.8s cycle.

---

## Taglines

| | OpenMaster | ClawMaster |
|---|---|---|
| EN | One Platform. Every Master. | Master the Claw, Command the Core. |
| ZH | 一生态，众大师 | 执掌利爪，驯服混乱 |
| JP | 共に、極みへ | 爪に道あり、要を制せ |

**Note:** Wordmark images contain EN tagline only. ZH/JP taglines appear as live text in HTML/CSS contexts.

---

## Wordmark Layouts

| Layout | Aspect | Use case |
|---|---|---|
| Horizontal | 16:9 | Website hero, README header, presentations |
| Stacked | 1:1 | App splash screen, social avatar, square contexts |
| Compact | 16:9 | Nav bar, app header, small contexts |

**Two themes per layout:**
- **Dark** — brand dark background, glowing mark — for product surfaces, dark UIs
- **White** — pure `#FFFFFF` background, EN only — for print, press kits, light UIs

---

## Future Products

When adding a new XxxMaster product:
1. Design a new geometric mark from the same pattern language (arcs, nodes, geometry)
2. Pick a new jewel tone (not teal, not amber)
3. Use Inter or Futura Light for the wordmark
4. Keep the dark background palette consistent
5. Add tokens to `brand-tokens.json`
