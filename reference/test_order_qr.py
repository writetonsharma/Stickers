"""Check QR masters and their actual 300-DPI printer PNGs.

Requires Pillow and zxing-cpp for rendered QR decoding.
"""
from __future__ import annotations

import json
import unittest
from pathlib import Path
from xml.etree import ElementTree as ET

from PIL import Image
import zxingcpp

from add_order_qr import ROOT, add_order_qr
from generate_sweet_bakes_labels import PRODUCTS, label_svg

SVG = '{http://www.w3.org/2000/svg}'
XLINK = '{http://www.w3.org/1999/xlink}href'
ORDER_URL = 'https://wa.me/918800206057?text=hi'


def active_masters() -> list[Path]:
    products = json.loads((ROOT / 'reference/RegulatoryLabels-Products.json').read_text(encoding='utf-8'))['products']
    inactive = {p['code'] for p in products if p.get('selling') is False}
    return [p for p in sorted((ROOT / 'Regulatory').glob('*.svg'))
            if not any(f'-{code}-' in p.name for code in inactive)]


class OrderQrTests(unittest.TestCase):
    def test_all_active_masters_and_printer_pngs(self) -> None:
        for path in active_masters():
            with self.subTest(label=path.name):
                svg = ET.parse(path).getroot()
                images = list(svg.iter(f'{SVG}image'))
                qrs = [i for i in images if i.get(XLINK, i.get('href')) == 'WhatsApp-Order-QR.png']
                is_lid = path.stem.endswith('-Top')
                self.assertEqual(len(qrs), 0 if is_lid else 1)
                for image in images:
                    asset = image.get(XLINK, image.get('href', ''))
                    self.assertTrue((path.parent / asset).is_file(), asset)
                width_mm = float(svg.attrib['width'].removesuffix('mm'))
                height_mm = float(svg.attrib['height'].removesuffix('mm'))
                view_width = float(svg.attrib['viewBox'].split()[2])
                if qrs:
                    qr_mm = float(qrs[0].attrib['width']) * width_mm / view_width
                    self.assertGreaterEqual(qr_mm, 20)
                png = ROOT / 'Regulatory-png' / f'{path.stem}.png'
                with Image.open(png) as image:
                    image.load()
                    self.assertEqual(image.size, (round(width_mm / 25.4 * 300), round(height_mm / 25.4 * 300)))
                    self.assertAlmostEqual(image.info['dpi'][0], 300, delta=0.1)
                    if qrs:
                        for scale in (1, 0.5):
                            check = image.convert('RGB')
                            if scale != 1:
                                check = check.resize((round(image.width * scale), round(image.height * scale)))
                            decoded = zxingcpp.read_barcodes(check)
                            self.assertIn(ORDER_URL, [r.text for r in decoded], f'{path.name} at {scale * 300} DPI')

    def test_refactor_is_idempotent(self) -> None:
        for path in active_masters():
            if path.name.startswith('RegulatoryLabel-'):
                source = path.read_text(encoding='utf-8')
                self.assertEqual(add_order_qr(source), source, path.name)

    def test_generator_preserves_qr_and_current_sweet_bake_masters(self) -> None:
        for product in PRODUCTS:
            generated = label_svg(product)
            self.assertEqual(generated, (ROOT / 'Regulatory' / product['filename']).read_text(encoding='utf-8'))
            ET.fromstring(generated)

    def test_smaller_package_dimensions(self) -> None:
        for product in PRODUCTS:
            svg = ET.fromstring(label_svg(product))
            expected = ('110mm', '110mm') if product['code'] == 'BW-001' else ('89mm', '127mm')
            self.assertEqual((svg.attrib['width'], svg.attrib['height']), expected)


if __name__ == '__main__':
    unittest.main()