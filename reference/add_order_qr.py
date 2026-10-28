"""Apply a repeatable ordering footer to active flat regulatory SVG masters.

Keeps declared print sizes, product copy, batch fields and nutrition values.
The connected jar labels already use the same QR and are left untouched.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def portrait_footer(compact: bool) -> str:
    start = 1145 if compact else 1200
    lines = [
        (0, 16, "MANUFACTURED &amp; PACKED BY"),
        (31, 21, "TRANCHE"),
        (60, 19, "35, Parkview Apartment, Sector 15,"),
        (85, 19, "Gurgaon, Haryana 122001, India"),
        (115, 18, "Consumer care: +91 87967 70308"),
        (145, 18, "Orders: +91 88002 06057"),
        (175, 18, "tranchebakery.in  |  @tranchebakery"),
    ]
    result = ['<g id="ordering-footer">']
    for offset, size, text in lines:
        style = ' fill="#6e7750" font-weight="700"' if offset == 0 else ''
        if offset == 31:
            style = ' font-weight="700"'
        result.append(f'<text x="40" y="{start + offset}" font-size="{size}"{style}>{text}</text>')
    if compact:
        logo_x, logo_y, license_x, license_y = 490, 1270, 40, 1350
        qr_x, qr_y, qr_size, caption_y = 710, 1140, 247, 1400
    else:
        logo_x, logo_y, license_x, license_y = 40, 1390, 225, 1430
        qr_x, qr_y, qr_size, caption_y = 710, 1190, 240, 1460
    result.extend([
        f'<image xlink:href="FSSAI_Logo-official.png" x="{logo_x}" y="{logo_y}" width="160" height="67" preserveAspectRatio="xMidYMid meet"/>',
        f'<text x="{license_x}" y="{license_y}" font-size="18">Lic. No. 20826005005996</text>',
        f'<image xlink:href="WhatsApp-Order-QR.png" x="{qr_x}" y="{qr_y}" width="{qr_size}" height="{qr_size}" preserveAspectRatio="xMidYMid meet"/>',
        f'<text x="{qr_x + qr_size / 2:g}" y="{caption_y}" font-size="14" font-weight="700" text-anchor="middle" fill="#6e7750">SCAN TO ORDER</text>',
        '</g>',
    ])
    return '\n    '.join(result)


def add_order_qr(svg: str) -> str:
    if 'id="ordering-footer"' in svg:
        return re.sub(r'(?m)[ \t]+$', '', svg)

    compact = 'width="89mm"' in svg
    if compact:
        # Recover 35 units from the storage-to-batch gap, not from text sizes.
        start = svg.index('<rect x="40" y="975"')
        end = svg.index('<text x="40" y="1200"', start)
        batch = re.sub(r'\by(?:1|2)?="(\d+)"',
                       lambda m: m[0].replace(m[1], str(int(m[1]) - 35)), svg[start:end])
        svg = svg[:start] + batch + svg[end:]
    start = svg.index('<text x="40" y="1200"')
    # Preserve proof/release warnings rather than silently removing them.
    end = svg.index('  </g>\n</svg>', start)
    warnings = re.findall(r'<text\b[^>]*>CONTENT PROOF[^<]*</text>', svg[start:end])
    warning_text = '\n    ' + '\n    '.join(warnings) if warnings else ''
    return svg[:start] + portrait_footer(compact) + warning_text + '\n' + svg[end:]


def main() -> None:
    products = json.loads((ROOT / 'reference/RegulatoryLabels-Products.json').read_text(encoding='utf-8'))['products']
    inactive = {p['code'] for p in products if p.get('selling') is False}
    for path in sorted((ROOT / 'Regulatory').glob('RegulatoryLabel-*.svg')):
        if any(f'-{code}-' in path.name for code in inactive):
            continue
        original = path.read_text(encoding='utf-8')
        updated = add_order_qr(original)
        if updated != original:
            path.write_text(updated, encoding='utf-8')
            print(f'Updated {path.name}')


if __name__ == '__main__':
    main()