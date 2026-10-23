# Gift-hamper jar labels — first fit proofs

These are editable SVG design concepts, NOT approved regulatory labels or production-ready cutting files. No preservative or extended shelf-life claim is made. On 2026-10-21 Butter Cookies were dropped and the cookie draft was changed to Chocolate Chunk only. The current reduced-sugar, soft-centred formula is a DEVELOPMENT TRIAL on page 9 of `sweetbakes/Tranche-Sweet-Bakes-V1.pdf`; validate the bake before approving label declarations. The root master DOCX has no cookie entries. Garlic & herb butter is the separate jarred finishing mixture, not garlic knots.

The cookie draft now carries the existing green vegetarian symbol and the official FSSAI logo asset. These do not certify the draft as print-ready; confirm final ingredients are vegetarian and licence/product coverage before approval. The chocolate is Van Houten 46.5% dark couverture, not compound. Ingredients are listed in descending recipe input weight, with a wheat/gluten and milk statement. Baking soda is named as raising agent INS 500(ii). Chocolate supplier sub-ingredients and allergen declarations still require the actual pack label; cross-contact statements also need confirmation. Nutrition must be recalculated after the reduced-sugar trial is accepted, and storage/shelf-life placeholders remain unresolved. No added preservative appears in the trial formula; revise declarations if one is subsequently introduced.

## Artwork

| Draft | Canvas | Lid circle | Neck width | Body panel |
| --- | --- | --- | --- | --- |
| Dark Couverture Chocolate Chunk Cookies | 262 × 172 mm | 48 mm | 16 mm | 256 × 72 mm |
| Garlic & herb butter | 212 × 134 mm | 48 mm | 16 mm | 206 × 50 mm |

The large cookie-jar physical geometry was finalized from a paper fit on 2026-10-23. It is one connected custom-cut sticker: a 48 mm lid circle, a 46 × 16 mm connecting strip measured from the circle edge to the body panel, and a 256 × 72 mm body panel. The jar circumference measured approximately 265 mm with thin thread and was independently confirmed by the paper wrap, leaving an approximately 9 mm viewing gap. These dimensions are final for artwork layout. The file remains named `Draft` because the cookie recipe, nutrition, supplier declaration, storage and other regulatory copy are not yet approved for sale.

The small garlic-butter jar geometry was finalized for trial cutting on 2026-10-23: a 48 mm lid circle, a 30 × 16 mm connecting strip measured from the circle edge to the body panel, and a 206 × 50 mm body panel. The supplied 212 × 134 mm SVG canvas provides 3 mm clear space around the 206 × 128 mm silhouette. The filename/content remain `Draft` until the physical fit and regulatory copy are approved.

## Near-full-wrap revision

Both body panels now wrap nearly around the container, with three sections from left to right: product declarations/batch details, product name/illustration in the CENTRE, and WhatsApp QR/social details. The lid head and connecting strip are aligned above the central product section. Cookie wording is "HANDMADE / Dark Couverture / Chocolate Chunk / COOKIES". Use this claim only while the actual chocolate is genuine couverture. Illustrations are original stylised SVG artwork, not photographs of the actual bakes; no internet images were used. Real product photos may replace the central illustrations once supplied: preferably a broken cookie showing the soft chocolate centre, and a separate garlic & herb butter serving photo, photographed in soft daylight on a plain neutral background. No suitable photos of these actual products were found by filename in the workspace; do not substitute cake/bread photos or unrelated stock food.

Cookie wrap length is the measured 265 mm body circumference minus an approximately 9 mm viewing gap, giving the finalized 256 mm panel. The butter body panel is 206 mm long for the current physical trial; confirm its final viewing gap when the paper proof is fitted.

The shared QR asset `Assets/WhatsApp-Order-QR.png` encodes exactly `https://wa.me/918800206057?text=hi` (ordering number, NOT customer care). Generated with segno, normal QR version 4, error correction H, four-module white quiet zone, scale 16 (656 × 656 px). Placed at 29 mm on cookies and 24 mm on butter. Retain the white quiet zone and test actual printed QR on the CURVED jar with multiple phones. Website and Instagram are verified from the current website. Facebook says "handle to confirm"; no account was guessed.

Address has been removed from the draft artwork at the user's request. This is NOT a determination that address declarations are optional: resolve any mandatory manufacturer/packer address on the appropriate package surface before approving retail labels; a QR or website is not automatically a substitute.

Artwork is in `Artwork/`. Each is ONE connected cream/olive silhouette with transparency outside it: round logo head → narrow neck → rounded body panel. The outer thin copper lines are decorative, NOT cutting paths. The cookie connecting strip is 46 × 16 mm; the butter connecting strip is 30 × 16 mm. Strip length is measured from the circle edge to the body-panel edge. The butter bend positions still require the physical trial fit.

## Large cookie jar — printer specification

Supply `Artwork/JarLabel-Chocolate-Chunk-Cookies-Draft.svg` as the vector master. Tell the printer:

- Finished sticker must be one connected, custom contour-cut piece.
- Lid circle: 48 mm diameter.
- Connecting strip: 46 mm long × 16 mm wide, measured from circle edge to body-panel edge.
- Body panel: 256 mm long × 72 mm high, with rounded corners as drawn.
- Overall finished silhouette: 256 mm wide × 166 mm high; the supplied SVG canvas is 262 × 172 mm and includes 3 mm clear space around the silhouette.
- Print at 100% scale. Do not fit, stretch or proportionally resize.
- Use the silhouette outer edge as the basis for a separate vector cut path; the inner copper keylines are decorative and must not be cut.
- Ask the printer to add its required bleed outside the contour, normally 2–3 mm, without changing the finished dimensions. Keep the supplied safe-area artwork placement.
- Recommended for a short run: digital print on food-packaging-suitable adhesive stock with plotter contour cutting. Request a physical proof before the full quantity.
- Supply the final cutter-ready PDF/SVG back for approval with fonts outlined and bitmap assets embedded. Confirm the QR scans from the curved applied proof.

The logo is the existing `../../logo/Logo.PNG`, referenced relative to each SVG, as in the existing logo sticker workflow. Keep that asset and folder relationship intact. Georgia and Arial/Helvetica are live fonts; confirm renderer/printer font availability before production. Colours: cream #faf7f2, olive #6e7750, brown #5a3e2b, copper #c69c6d. Copper is a flat ink colour, not metallic foil.

## PNG conversion

Run `Convert-HamperLabelsToPng.ps1` in this folder on the ImageMagick machine. It delegates to the existing parent converter at 300 DPI (or the supplied Dpi parameter), using `Artwork` as its source. Outputs stay here in `Artwork-png/`. The parent converter now accepts optional SourceFolderNames; its original four-folder behaviour remains unchanged when omitted.

Expected 300 DPI canvas dimensions: cookies 3094 × 2031 px; butter 2504 × 1583 px. Transparent PNG rectangles are NOT rectangular sticker outlines: tell the printer the label is a connected custom-cut shape. A PNG alone does not supply a vector cutting die.

## Fit test before refining

1. Print SVG/PNG at actual size, 100%, with no fit-to-page scaling; confirm each 48 mm lid circle with a ruler.
2. Cut around the connected silhouette and tape to the empty container. Check lid flat area, rim transition, strip length, body-panel height and curvature. The butter panel must stay below the shoulder and above the base curve. Record the butter wrap-end gap and evaluate readability/QR scanning around the curve.
3. Open the lid and decide whether the neck should tear as an opening seal. No tamper-evident claim is established by this design.
4. Test adhesive on both metal and the clear container; use condensation-resistant stock/adhesive for the refrigerated butter. Test writing on the chosen laminate/topcoat.

## Content still needed

- Final recipes, ingredient order, chocolate supplier sub-ingredients, allergens/cross-contact and nutrition; do not copy the garlic-knots nutrition onto its butter topping.
- Actual packed net weights, batch/date fields, MRP and validated date-marking/storage instructions.
- Review applicable FSSAI/Legal Metrology requirements, including food category/product name (the butter mixture may contain olive oil), veg mark, FSSAI logo, full nutrition/serving information and required type sizes. The current compact panels may need widening once real copy is available. Existing licence number/business details are carried over for layout only, not certification of product coverage.
- Both drafts visibly say LAYOUT PROOF / NOT FOR SALE. Do not remove that notice until content and fit are approved.
- No chilli-garlic-oil label yet: formulation, safe process and storage instructions are unresolved. Oil and butter do not establish a safe 2–3-week life for added garlic. Refrigeration does not validate that claim, particularly for garlic-in-oil; obtain qualified food-safety advice and product-specific shelf-life validation.

For production, commission a separate agreed dieline and bleed (typically printer-specified), safe margins, embedded assets/outlined fonts and a physical proof. Do not send these fit proofs as approved retail labels.