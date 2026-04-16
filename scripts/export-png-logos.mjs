import sharp from 'sharp';
import { writeFileSync } from 'fs';

const SIZE = 512;
const PAD  = 0.18; // 18% padding on each side

function makeSVG(bg, color, iconPath) {
  // Scale the 100×100 viewBox icon to fill the padded area
  const inner  = SIZE * (1 - PAD * 2);
  const offset = SIZE * PAD;
  return `<svg width="${SIZE}" height="${SIZE}" viewBox="0 0 ${SIZE} ${SIZE}" xmlns="http://www.w3.org/2000/svg">
  <rect width="${SIZE}" height="${SIZE}" fill="${bg}"/>
  <g transform="translate(${offset},${offset}) scale(${inner / 100})">
    ${iconPath}
  </g>
</svg>`;
}

// ── ClawMaster · V3 Command Signal ─────────────────────────────────────────
const cmIcon = `
  <circle cx="68" cy="50" r="5" fill="#F5A623"/>
  <g fill="none" stroke="#F5A623" stroke-linecap="round">
    <path d="M 68 40 A 10 10 0 0 0 68 60" stroke-width="3.5"/>
    <path d="M 68 31 A 19 19 0 0 0 68 69" stroke-width="3"/>
    <path d="M 68 22 A 28 28 0 0 0 68 78" stroke-width="2.5"/>
  </g>
  <circle cx="68" cy="22" r="2.5" fill="#F5A623"/>
  <circle cx="68" cy="78" r="2.5" fill="#F5A623"/>
`;

// ── OpenMaster · V4 Hex Warrior ─────────────────────────────────────────────
const omIcon = `
  <g fill="none" stroke="#00BCD4" stroke-width="1.5" opacity="0.35">
    <polygon points="50,22 74,36 74,64 50,78 26,64 26,36" stroke-dasharray="3 2"/>
    <line x1="50" y1="22" x2="50" y2="50"/>
    <line x1="74" y1="36" x2="50" y2="50"/>
    <line x1="74" y1="64" x2="50" y2="50"/>
    <line x1="50" y1="78" x2="50" y2="50"/>
    <line x1="26" y1="64" x2="50" y2="50"/>
    <line x1="26" y1="36" x2="50" y2="50"/>
  </g>
  <g fill="#00BCD4">
    <circle cx="50" cy="22" r="3.5"/>
    <circle cx="74" cy="36" r="3.5"/>
    <circle cx="74" cy="64" r="3.5"/>
    <circle cx="50" cy="78" r="3.5"/>
    <circle cx="26" cy="64" r="3.5"/>
    <circle cx="26" cy="36" r="3.5"/>
    <circle cx="50" cy="50" r="8"/>
  </g>
`;

const exports = [
  { file: 'logos/clawmaster/github-avatar.png', bg: '#0C0804', icon: cmIcon },
  { file: 'logos/openmaster/github-avatar.png', bg: '#02080E', icon: omIcon },
];

for (const { file, bg, icon } of exports) {
  const svg = makeSVG(bg, null, icon);
  await sharp(Buffer.from(svg)).png().toFile(file);
  console.log(`✓ ${file}`);
}
