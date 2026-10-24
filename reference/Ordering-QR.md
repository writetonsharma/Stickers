# Ordering QR on packaging

## Shared destination

- Asset: `../Regulatory/WhatsApp-Order-QR.png`.
- Destination: **https://wa.me/918800206057?text=hi** (WhatsApp ordering).
- Customer care remains **+91 87967 70308**, separate from ordering.
- This is a direct ordering link, not a payment QR or a third-party redirect.
- The existing PNG includes its four-module white quiet zone; do not crop it,
  recolour it, add a logo inside it, or put text/borders across it.

## Layouts

| Label | Finished label size | QR including quiet zone |
| --- | --- | --- |
| Standard active regulatory label | 100 × 150 mm | 24 × 24 mm |
| Walnut brownie | 135 × 65 mm | 20 × 20 mm |
| Both biscotti | 89 × 127 mm | approximately 22 × 22 mm |
| Connected cookie jar | existing custom contour | 29 × 29 mm, unchanged |
| Connected garlic-butter jar | existing custom contour | 24 × 24 mm, unchanged |

Portrait labels use a two-column manufacturer/contact and ordering footer, with
the FSSAI logo and licence retained. Biscotti recovers space from the gap before
the batch panel. Brownie nutrition rows have less vertical padding, with no
reduction to nutrition font size. Product, ingredients, allergens, nutrition
values, storage and handwritten batch fields are retained. Non-selling product
masters are intentionally not updated.

`add_order_qr.py` applies the layout to active flat masters and is safe to rerun.
`generate_sweet_bakes_labels.py` calls the same layout function so generating
brownie/biscotti masters does not remove the QR. The root SVG-to-PNG converter
embeds linked assets and writes dimension-checked 300-DPI printer PNGs.
`test_order_qr.py` checks dimensions, linked images, generation consistency,
idempotence and QR decoding from the actual printer PNGs at 300 and 150 DPI.
The test needs Pillow and zxing-cpp in the Python environment.

## Release checks

- Print at **100% / actual size**, not fit-to-page. Scan with real phones after
  application to the final box/jar; check glare and curved surfaces as well.
- Digital decoding is not a substitute for a physical scan test or printer/
  regulatory approval. Keep the existing proof warnings until release.
- Brownies, biscotti and cookies are not yet in the app's current menu. The QR
  opens the general ordering bot, not a product-specific basket. These products
  need assisted ordering via Message Us until separately added to the app.
- The connected jar masters still have their existing draft regulatory copy;
  this QR/layout work does not approve or finalize that copy.

## Consolidation and transfer

The former `Gifthampers/` masters, PNGs and ordering asset now live in
`Regulatory/` and `Regulatory-png/`. The connected-label specification is
`Connected-Jar-Labels.md` here. Do not recreate the old folder.

A transfer bundle must include **deletions** of the old tracked locations as
well as additions at the new locations. The existing base64 unpacker only
writes files; do not use it unchanged to claim the move is fully transferred.
The master recipe DOCX and Sweet Bakes source/PDF are outside the Stickers Git
repository and require a separate explicit transfer, not just a stickers diff.