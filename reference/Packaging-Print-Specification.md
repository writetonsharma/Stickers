# TRANCHE Packaging Print Specification

**Prepared:** 24 July 2026  
**Status:** Printer quotation, material sampling and physical proofing  
**Production approval:** Do not begin the full print run until the physical materials, dimensions, colours, adhesion and readability have been approved by TRANCHE.

## Packaging Set

| Item | Finished size | Shape | Application | Size status |
| --- | ---: | --- | --- | --- |
| Logo sticker | 75 mm diameter | Circle | Outer paper bag | Selected |
| Sealing sticker | 50 x 150 mm | Portrait rectangle with 3 mm rounded corners | Folded inner plastic bread bag | Selected, subject to a fit test on the actual bag |
| Regulatory sticker | 100 x 150 mm | Portrait rectangle with 3 mm rounded corners | Outer retail package | Provisional until tested on the selected outer bag |
| Thank-you and bread-care card | 65 x 90 mm | Double-sided portrait card with 3 mm rounded corners | Threaded onto the package | Selected, subject to thread-hole testing |

All dimensions above are finished trim/cut dimensions. Bleed is additional and must not reduce the finished size.

## Common Print Requirements

- Supply the printer's dieline and technical artwork requirements before final production files are prepared.
- Use 3 mm bleed on every side unless the printer's process requires a different amount.
- Keep important text, logos, QR codes and regulatory content at least 3 to 4 mm inside the cut line. Use a larger clearance around the card's thread hole as specified below.
- Print in full colour using the printer's requested CMYK profile.
- Match the approved warm brown, warm white and muted olive colours as closely as the selected materials permit.
- Use a matte appearance throughout the packaging set. Avoid high-gloss finishes.
- Embed linked images in the production PDF and embed fonts or convert them to outlines.
- Keep vector text and line work as vectors. Do not rasterize the complete artwork.
- Confirm the minimum reproducible type size, line weight, cut tolerance and front-to-back registration tolerance.
- Provide a digital proof followed by at least one physical printed and cut proof of every item.
- Verify dimensions on the physical proof with a ruler. Do not scale artwork to fit a standard sheet.
- Confirm expected indoor storage life, colourfastness and resistance to ordinary handling and scuffing.
- Packaging components will not be designed for direct contact with bread. Confirm that the selected materials, inks and adhesives are suitable for their intended use on food packaging.

## 1. Logo Sticker

### Finished format

- Finished size: 75 mm diameter.
- Shape: die-cut circle.
- Application: front of the outer paper or kraft bag.
- Current master: `LogoSticker-75mm.svg`.
- Linked source image: `Logo.PNG`.
- Current 300 DPI proof: `LogoSticker-75mm-300dpi.png`, 886 x 886 pixels.

### Material and finish

- Preferred material: premium white matte paper label stock.
- Alternative: matte white BOPP if moisture resistance is required.
- Adhesive: permanent adhesive tested on the exact outer paper or kraft bag.
- Finish: matte and reasonably scuff-resistant.
- No writable coating is required.
- The white stock should preserve the logo's intended colour and contrast against the outer bag.

### Printer checks

- Confirm that the circular cut is centred on the artwork.
- Confirm that all small logo lettering remains sharp and readable at 75 mm diameter.
- Confirm whether the printer requires a separate spot-colour cut contour.
- The current SVG references `Logo.PNG`; embed this image in the final printer PDF or package it with the SVG.
- Test adhesion on a filled and folded outer bag, not only on a flat paper sample.

## 2. Sealing Sticker

### Finished format

- Finished size: 50 x 150 mm, portrait.
- Shape: rectangle with approximately 3 mm rounded corners to reduce edge lifting.
- Application: closes the folded inner plastic bread bag.
- Current master: `FreshnessSeal-Universal.svg`.
- Current proof: `FreshnessSeal-Universal-300dpi.png`.
- Variable handwritten fields: Product, Packed on and Net weight.

### Material and finish

- Preferred material: white matte BOPP or PP label stock.
- Adhesive: permanent adhesive specifically matched to the actual inner bag material, such as LDPE, PP or BOPP.
- The bakery must provide the printer with an actual inner bag or its complete material specification.
- Surface: writable topcoat that accepts the bakery's selected permanent marker without beading, smudging or slow drying.
- Finish: matte. Do not apply glossy lamination over writable fields.
- Required performance: resistance to ordinary moisture, bread oils, bag flexing, refrigeration-free storage and freezing/thawing when customers freeze the bread in its inner bag.

### Printer checks and tests

- Apply the sample across the real folded closure and leave it for at least 24 hours.
- Confirm that the edges do not lift when the filled bag flexes.
- Write on the sample with the bakery's selected marker and test immediate smudging and rub resistance after drying.
- Freeze a sealed sample, allow it to thaw and check adhesion, print integrity and writing legibility.
- Confirm that the adhesive does not leave the closure unreliable during normal customer handling.
- Provide blank material samples before the full run.

## 3. Regulatory Sticker

### Finished format

- Provisional finished size: 100 x 150 mm, portrait.
- Shape: rectangle with approximately 3 mm rounded corners.
- Application: readily visible on the outer retail package.
- The final size must be approved only after testing it on the selected outer bag and measuring the flat usable panel, window, folds and closure area.
- Product-specific masters: `RegulatoryLabels-FinalProof/`.
- Product-specific 300 DPI proofs: `RegulatoryLabels-FinalProof-300dpi/`.
- The final production set contains separate artwork for each active product variant.

### Required content and readability

- Preserve the product name, description, ingredients, allergen statement, approximate nutrition panel, storage statement, business details, FSSAI logo and licence number, consumer contact details and all variable fields.
- Variable handwritten fields include Batch/Lot No., Packed on, Best before, Net Quantity and MRP.
- Mandatory information must remain clearly legible and must not be reduced merely to force all products into identical coordinates.
- Keep the official vegetarian and FSSAI marks sharp and at legally appropriate final sizes.
- Final content and artwork remain subject to current FSSAI and Legal Metrology review before commercial printing.

### Material and finish

- For a kraft or paper outer bag: preferred material is opaque white matte paper label stock with permanent adhesive.
- For a smooth plastic application area: use opaque white matte BOPP with an adhesive matched to that plastic.
- The stock must be opaque enough that the bag colour or printed background does not reduce text contrast.
- Surface: writable with the bakery's selected permanent marker.
- Finish: matte. Do not apply glossy lamination over variable fields.
- Adhesive: permanent and tested on the exact outer package.

### Printer checks

- Print the densest ingredient declaration and nutrition panel as part of the physical proof.
- Confirm small text, nutrition-table rules and official marks remain sharp at final size.
- Test handwriting, drying time and rub resistance in every variable field.
- Confirm that the complete label lies on a flat area without crossing the window, gusset, major fold or closure.
- Do not proceed with the full regulatory-label run while 100 x 150 mm remains provisional.

## 4. Double-Sided Thank-You and Bread-Care Card

### Finished format

- Finished size: 65 x 90 mm, portrait.
- Shape: double-sided card with approximately 3 mm rounded corners.
- Front master: `BreadCareCard-ThankYou.svg`.
- Back master: `BreadCareCard-Care.svg`.
- Front proof: `BreadCareCard-ThankYou-300dpi.png`, 768 x 1063 pixels at 300 DPI.
- Back proof: `BreadCareCard-Care-300dpi.png`.
- The card is not adhesive. It is attached to the package with thread.

### Card stock and finish

- Preferred stock: 300 to 350 GSM warm-white or natural-white cardstock.
- Finish: uncoated or lightly textured matte stock.
- The stock must accept clean printing on both sides and resist tearing around the thread hole.
- Avoid glossy lamination unless a physical proof demonstrates that it does not make the card feel plastic or reduce QR-code reliability.
- Confirm paper grain direction and stiffness so the card hangs neatly rather than curling.

### Thread hole

- Provisional hole diameter: 4 to 5 mm, centred horizontally near the top.
- Confirm the exact diameter, punching tolerance and distance from the top edge with the printer after testing the selected thread.
- Keep important artwork and text at least 5 mm away from the finished hole edge.
- Test whether reinforcement is necessary. Prefer sufficiently strong card stock over a visible reinforcement eyelet unless tearing occurs.

### Printer checks

- Confirm accurate front-to-back alignment and correct top orientation on both sides.
- Punch and cut at least one physical sample using the intended production process.
- Scan the printed QR code from several ordinary mobile phones before production approval.
- Thread the physical sample and hang it from a filled package to assess balance, rotation and tear resistance.
- Verify that all text remains comfortably readable at the finished 65 x 90 mm size.
- The editable SVGs reference `Logo.PNG` and `BreadCare-StorageQR.png`; embed those assets in the final printer PDF or package them with the SVG files.

## Artwork Delivery

For final production, request the printer's preferred file format. The recommended delivery package is:

1. Press-ready CMYK PDF files created from the approved SVG masters.
2. A separate dieline or cut-contour layer if requested by the printer.
3. Embedded fonts or outlined text.
4. Embedded raster assets at sufficient effective resolution.
5. One low-resolution reference proof showing intended orientation and appearance.
6. This specification document.

The existing PNG files are viewing and content proofs. They should not replace the vector production masters unless the printer specifically requires raster artwork and confirms the required dimensions, colour profile and resolution.

### Regenerating PNG proofs

From the `C:\Personal\Bakery` workspace folder, regenerate all approved packaging PNG proofs with:

```powershell
.\.venv\Scripts\python.exe .\LogoAndStickers\render_pngs.py
```

Render one SVG or all SVGs in one directory by passing its path:

```powershell
.\.venv\Scripts\python.exe .\LogoAndStickers\render_pngs.py .\LogoAndStickers\LogoSticker-75mm.svg
.\.venv\Scripts\python.exe .\LogoAndStickers\render_pngs.py .\LogoAndStickers\RegulatoryLabels-FinalProof
```

If the rendering dependencies are missing, install the pinned versions into the workspace virtual environment:

```powershell
.\.venv\Scripts\python.exe -m pip install -r .\LogoAndStickers\print-render-requirements.txt
```

The renderer reads the physical `width` and `height` in millimetres from each SVG, calculates the correct pixel dimensions, resolves linked images from the SVG's directory and embeds 300 DPI metadata. Product-specific regulatory PNGs are written to `RegulatoryLabels-FinalProof-300dpi`; other PNG proofs are written beside their SVG masters with a `-300dpi.png` suffix.

## Samples to Give the Printer

- The exact outer paper or kraft bag.
- The exact inner plastic bread bag.
- The permanent marker that will be used for variable information.
- The intended thread or cord for the card.
- A representative filled or padded package for placement tests.
- Approved digital artwork and colour reference images.

## Physical Proof Acceptance Checklist

- [ ] Finished dimensions and cut shapes are correct.
- [ ] Bleed reaches every cut edge without unintended white slivers.
- [ ] Important content remains within the safe area.
- [ ] Brown, warm white and olive colours are acceptable under normal lighting.
- [ ] Fine text and lines are sharp and readable.
- [ ] Logo sticker adheres to the outer bag without lifting.
- [ ] Sealing sticker holds the folded inner bag closed for at least 24 hours.
- [ ] Sealing sticker passes marker, rub, freezer and thaw tests.
- [ ] Regulatory sticker fits the usable package panel and all mandatory content is legible.
- [ ] All handwritten fields accept ink without smudging.
- [ ] Thank-you card is correctly aligned on both sides.
- [ ] QR code scans from the printed card.
- [ ] Thread hole and cardstock withstand normal handling.
- [ ] Printer has confirmed material names, adhesives, finishes, colour profile, tolerances and production lead time in writing.

## Final Approval Boundary

Approval of a digital image is not production approval. Production approval requires physical samples made with the proposed stock, adhesive, ink, coating, cutting and punching processes. Any material, size or process change after approval requires a new proof.
