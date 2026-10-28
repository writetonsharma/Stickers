from __future__ import annotations

import json
from pathlib import Path
from xml.sax.saxutils import escape

from add_order_qr import add_order_qr


ROOT = Path(__file__).resolve().parents[1]
PRODUCTS_PATH = ROOT / "reference" / "RegulatoryLabels-Products.json"
NUTRITION_PATH = ROOT / "reference" / "RegulatoryLabels-Nutrition.json"
MATRIX_PATH = ROOT / "reference" / "RegulatoryLabels-ProductionMatrix.md"
LABEL_DIR = ROOT / "Regulatory"

SHARED_CROSS_CONTACT = (
    "Made in a kitchen that also handles milk and milk products, tree nuts, soy, sesame and other seeds."
)

PRODUCTS = [
    {
        "code": "BW-001",
        "filename": "RegulatoryLabel-BW-001-Walnut-Dark-Chocolate-Brownies.svg",
        "layout": "square",
        "name": "Walnut Dark Chocolate Brownies",
        "title_size": 36,
        "description": "Moist eggless dark chocolate brownies with toasted walnuts",
        "ingredients": (
            "Sweetened condensed milk (milk solids, sugar), dark chocolate couverture, sugar, butter, refined wheat "
            "flour, walnuts (tree nuts), whole milk, cocoa powders, natural vanilla and salt."
        ),
        "ingredient_lines": [
            "Sweetened condensed milk (milk solids, sugar), dark chocolate couverture, sugar,",
            "butter, refined wheat flour, walnuts (tree nuts), whole milk, cocoa powders, natural",
            "vanilla and salt.",
        ],
        "allergens": "Contains wheat, gluten, milk and tree nuts (walnuts).",
        "pack": "4 brownies",
        "yieldGrams": 540,
        "formulaGrams": {
            "dark_couverture": 100,
            "butter": 85,
            "condensed_milk": 110,
            "caster_sugar": 90,
            "milk": 55,
            "maida": 80,
            "medium_cocoa": 20,
            "dark_brown_cocoa": 10,
            "vanilla": 2,
            "salt": 2,
            "walnuts": 60,
        },
        "nutrition": {
            "energyKcal": 497,
            "proteinG": 7.3,
            "carbohydrateG": 52.2,
            "totalSugarsG": 37.6,
            "addedSugarsG": 34.0,
            "fatG": 29.8,
            "saturatedFatG": 14.7,
            "transFatG": 0.6,
            "sodiumMg": 181,
        },
        "storage": "Store airtight in a cool, dry place. Best-before date as marked.",
    },
    {
        "code": "BI-001",
        "filename": "RegulatoryLabel-BI-001-Almond-Biscotti.svg",
        "layout": "compact_portrait",
        "name": "Almond Biscotti",
        "title_size": 40,
        "description": "Crisp eggless twice-baked almond biscuits",
        "ingredients": (
            "Refined wheat flour, sugar, whole milk, almonds (tree nuts), butter, raising agent "
            "(sodium bicarbonate [INS 500(ii)]), salt and natural vanilla."
        ),
        "ingredient_lines": [
            "Refined wheat flour, sugar, whole milk, almonds (tree nuts), butter, raising agent",
            "(sodium bicarbonate [INS 500(ii)]), salt and natural vanilla.",
        ],
        "allergens": "Contains wheat, gluten, milk and tree nuts (almonds).",
        "pack": "6 biscotti",
        "yieldGrams": 120,
        "formulaGrams": {
            "maida": 105,
            "caster_sugar": 35,
            "butter": 25,
            "milk": 35,
            "almonds": 30,
            "baking_soda": 1,
            "salt": 1,
            "vanilla": 1,
        },
        "nutritionYieldGrams": 200,
        "nutrition": {
            "energyKcal": 448,
            "proteinG": 9.3,
            "carbohydrateG": 61.6,
            "totalSugarsG": 19.2,
            "addedSugarsG": 17.5,
            "fatG": 18.7,
            "saturatedFatG": 7.4,
            "transFatG": 0.4,
            "sodiumMg": 343,
        },
        "storage": "Store airtight in a cool, dry place. Best-before date as marked.",
    },
    {
        "code": "BI-002",
        "filename": "RegulatoryLabel-BI-002-Dark-Chocolate-Dipped-Almond-Biscotti.svg",
        "layout": "compact_portrait",
        "name": "Dark Chocolate Dipped Almond Biscotti",
        "title_size": 31,
        "description": "Six almond biscotti dipped in dark chocolate couverture",
        "ingredients": (
            "Dark chocolate couverture (sugar, cocoa solids, cocoa butter, emulsifiers [soya lecithin and polyglycerol "
            "esters of interesterified ricinoleic acid] and nature-identical flavouring substance [vanillin]), refined "
            "wheat flour, sugar, whole milk, almonds (tree nuts), butter, raising agent (sodium bicarbonate "
            "[INS 500(ii)]), salt and natural vanilla."
        ),
        "ingredient_lines": [
            "Dark chocolate couverture*, refined wheat flour, sugar, whole milk, almonds (tree nuts),",
            "butter, raising agent (sodium bicarbonate [INS 500(ii)]), salt and natural vanilla.",
            "*Contains soya lecithin; full couverture declaration retained in the product record.",
        ],
        "allergens": "Contains wheat, gluten, milk, soy and tree nuts (almonds).",
        "pack": "6 dipped biscotti",
        "yieldGrams": 210,
        "formulaGrams": {
            "dark_couverture": 90,
            "maida": 63,
            "caster_sugar": 21,
            "butter": 15,
            "milk": 21,
            "almonds": 18,
            "baking_soda": 0.6,
            "salt": 0.6,
            "vanilla": 0.6,
        },
        "nutrition": {
            "energyKcal": 488,
            "proteinG": 7.4,
            "carbohydrateG": 59.2,
            "totalSugarsG": 31.5,
            "addedSugarsG": 30.6,
            "fatG": 25.3,
            "saturatedFatG": 13.2,
            "transFatG": 0.2,
            "sodiumMg": 201,
        },
        "storage": "Store airtight in a cool, dry place. Best-before date as marked.",
    },
]


def upsert(items: list[dict], product: dict) -> None:
    record = {
        "code": product["code"],
        "name": product["name"],
        "description": product["description"],
        "ingredients": product["ingredients"],
        "allergens": product["allergens"],
        "pack": product["pack"],
        "yieldGrams": product["yieldGrams"],
        "nutrition": product["nutrition"],
    }
    for index, current in enumerate(items):
        if current["code"] == product["code"]:
            items[index] = record
            return
    items.append(record)


def upsert_nutrition(items: list[dict], product: dict) -> None:
    record = {
        "code": product["code"],
        "yieldGrams": product.get("nutritionYieldGrams", product["yieldGrams"]),
        "formulaGrams": product["formulaGrams"],
        "nutritionPer100g": product["nutrition"],
    }
    for index, current in enumerate(items):
        if current["code"] == product["code"]:
            items[index] = record
            return
    items.append(record)


def square_label_svg(product: dict) -> str:
        nutrition = product["nutrition"]
        ingredient_lines = product["ingredient_lines"]
        return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="110mm" height="110mm" viewBox="0 0 1100 1100" role="img" aria-labelledby="title description">
    <title id="title">TRANCHE {escape(product["name"])} regulatory label</title>
    <description id="description">Single-column square label for a 6 by 6 inch brownie box; recipe-based approximate nutrition.</description>
    <rect width="1100" height="1100" fill="#faf7f2"/><rect x="18" y="18" width="1064" height="1064" rx="8" fill="none" stroke="#5a3e2b" stroke-width="2"/>
    <g fill="#2b2b2b" font-family="Arial, Helvetica, sans-serif">
        <text x="42" y="62" fill="#5a3e2b" font-family="Georgia, 'Times New Roman', serif" font-size="30" font-weight="700" letter-spacing="3">TRANCHÉ</text>
        <text x="42" y="88" fill="#6e7750" font-size="13" font-weight="700" letter-spacing="2">ARTISAN BAKERY</text>
        <text x="42" y="138" fill="#5a3e2b" font-family="Georgia, 'Times New Roman', serif" font-size="34" font-weight="700">{escape(product["name"])}</text>
        <text x="42" y="168" font-size="18">{escape(product["description"])}</text>
        <g transform="translate(990 48)"><rect width="58" height="58" fill="#fff" stroke="#008a3b" stroke-width="4"/><circle cx="29" cy="29" r="15" fill="#008a3b"/></g>
        <line x1="42" y1="185" x2="1058" y2="185" stroke="#c69c6d" stroke-width="2"/>

        <text x="42" y="215" fill="#6e7750" font-size="16" font-weight="700" letter-spacing="1.5">INGREDIENTS</text>
        <g font-size="17"><text x="42" y="243">{escape(ingredient_lines[0])}</text><text x="42" y="267">{escape(ingredient_lines[1])}</text><text x="42" y="291">{escape(ingredient_lines[2])}</text></g>
        <text x="42" y="322" fill="#6e7750" font-size="16" font-weight="700" letter-spacing="1.5">ALLERGEN INFORMATION</text>
        <text x="42" y="349" font-size="18" font-weight="700">{escape(product["allergens"])}</text>
        <text x="42" y="374" font-size="15">Made in a kitchen that also handles milk products, tree nuts, soy, sesame and other seeds.</text>
        <line x1="42" y1="392" x2="1058" y2="392" stroke="#c69c6d" stroke-width="2"/>

        <text x="42" y="421" fill="#6e7750" font-size="16" font-weight="700" letter-spacing="1.5">NUTRITION INFORMATION</text>
        <text x="1058" y="421" font-size="16" text-anchor="end">Approximate values per 100 g</text>
        <g font-size="18"><rect x="42" y="438" width="1016" height="256" fill="#fff" stroke="#5a3e2b" stroke-width="1.5"/><line x1="710" y1="438" x2="710" y2="694" stroke="#5a3e2b"/><path d="M42 470H1058 M42 502H1058 M42 534H1058 M42 566H1058 M42 598H1058 M42 630H1058 M42 662H1058" stroke="#eadfce"/>
            <text x="60" y="461" font-weight="700">Nutrient</text><text x="1040" y="461" font-weight="700" text-anchor="end">Per 100 g</text>
            <text x="60" y="493">Energy</text><text x="1040" y="493" text-anchor="end">{nutrition["energyKcal"]} kcal</text>
            <text x="60" y="525">Protein</text><text x="1040" y="525" text-anchor="end">{nutrition["proteinG"]} g</text>
            <text x="60" y="557">Carbohydrate</text><text x="1040" y="557" text-anchor="end">{nutrition["carbohydrateG"]} g</text>
            <text x="78" y="589">Total sugars / Added sugars</text><text x="1040" y="589" text-anchor="end">{nutrition["totalSugarsG"]} g / {nutrition["addedSugarsG"]} g</text>
            <text x="60" y="621">Total fat</text><text x="1040" y="621" text-anchor="end">{nutrition["fatG"]} g</text>
            <text x="78" y="653">Saturated fat / Trans fat</text><text x="1040" y="653" text-anchor="end">{nutrition["saturatedFatG"]} g / {nutrition["transFatG"]} g</text>
            <text x="60" y="685">Sodium</text><text x="1040" y="685" text-anchor="end">{nutrition["sodiumMg"]} mg</text></g>

        <text x="42" y="725" fill="#6e7750" font-size="16" font-weight="700" letter-spacing="1.5">STORAGE</text><text x="42" y="751" font-size="18">{escape(product["storage"])}</text>
        <rect x="42" y="760" width="1016" height="88" rx="5" fill="#fff" stroke="#5a3e2b" stroke-width="1.5"/><text x="60" y="782" fill="#6e7750" font-size="15" font-weight="700" letter-spacing="1.2">BATCH DETAILS</text>
        <g font-size="18"><text x="60" y="809">Batch / Lot No.</text><line x1="195" y1="813" x2="470" y2="813" stroke="#2b2b2b"/><text x="510" y="809">Packed on</text><line x1="606" y1="813" x2="1038" y2="813" stroke="#2b2b2b"/><text x="60" y="837">Best before</text><line x1="172" y1="841" x2="470" y2="841" stroke="#2b2b2b"/><text x="510" y="837">Net Qty.</text><line x1="592" y1="841" x2="695" y2="841" stroke="#2b2b2b"/><text x="705" y="837">g</text><text x="750" y="837">MRP ₹</text><line x1="812" y1="841" x2="1038" y2="841" stroke="#2b2b2b"/></g>

        <text x="42" y="900" fill="#6e7750" font-size="14" font-weight="700" letter-spacing="1.2">MANUFACTURED &amp; PACKED BY</text><text x="42" y="929" font-size="19" font-weight="700">TRANCHE</text>
        <text x="42" y="956" font-size="16">35, Parkview Apartment, Sector 15, Gurgaon, Haryana 122001, India</text>
        <text x="42" y="983" font-size="15">Consumer care: +91 87967 70308  |  Orders: +91 88002 06057</text><text x="42" y="1009" font-size="15">tranchebakery.in  |  @tranchebakery</text>
        <image xlink:href="FSSAI_Logo-official.png" x="655" y="905" width="140" height="59" preserveAspectRatio="xMidYMid meet"/><text x="725" y="992" font-size="15" text-anchor="middle">Lic. No. 20826005005996</text>
        <g id="ordering-footer"><text x="958" y="868" font-size="13" font-weight="700" text-anchor="middle" fill="#6e7750">SCAN TO ORDER</text><image xlink:href="WhatsApp-Order-QR.png" x="858" y="875" width="200" height="200" preserveAspectRatio="xMidYMid meet"/></g>
    </g>
</svg>
'''


def label_svg(product: dict) -> str:
    if product.get("layout") == "square": return square_label_svg(product)
    nutrition = product["nutrition"]
    ingredient_tspans = "".join(
        f'<tspan x="40" y="{274 + index * 24}">{escape(line)}</tspan>'
        for index, line in enumerate(product["ingredient_lines"])
    )
    return add_order_qr(f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="89mm" height="127mm" viewBox="0 0 1000 1427" role="img" aria-labelledby="title description">
  <title id="title">TRANCHE {escape(product["name"])} regulatory label content proof</title>
  <description id="description">Content proof with recipe-based approximate nutrition; verify measured net weight before release.</description>
    <rect width="1000" height="1427" fill="#faf7f2"/><rect x="20" y="20" width="960" height="1387" rx="8" fill="none" stroke="#5a3e2b" stroke-width="2"/>
  <g fill="#2b2b2b" font-family="Arial, Helvetica, sans-serif">
    <text x="40" y="70" fill="#5a3e2b" font-family="Georgia, 'Times New Roman', serif" font-size="32" font-weight="700" letter-spacing="3">TRANCHÉ</text>
    <text x="40" y="98" fill="#6e7750" font-size="14" font-weight="700" letter-spacing="2">ARTISAN BAKERY</text>
    <text x="40" y="151" fill="#5a3e2b" font-family="Georgia, 'Times New Roman', serif" font-size="{product["title_size"]}" font-weight="700">{escape(product["name"])}</text>
    <text x="40" y="183" font-size="20">{escape(product["description"])}</text>
    <g transform="translate(895 50)"><rect width="60" height="60" fill="#ffffff" stroke="#008a3b" stroke-width="5"/><circle cx="30" cy="30" r="15" fill="#008a3b"/></g>
    <line x1="40" y1="210" x2="960" y2="210" stroke="#c69c6d" stroke-width="2"/>
    <text x="40" y="245" fill="#6e7750" font-size="17" font-weight="700" letter-spacing="1.5">INGREDIENTS</text>
    <text x="40" y="274" font-size="17">{ingredient_tspans}</text>
    <text x="40" y="370" fill="#6e7750" font-size="17" font-weight="700" letter-spacing="1.5">ALLERGEN INFORMATION</text>
    <text x="40" y="402" font-size="19" font-weight="700">{escape(product["allergens"])}</text>
    <text x="40" y="432" font-size="17">{escape(SHARED_CROSS_CONTACT)}</text>
    <line x1="40" y1="455" x2="960" y2="455" stroke="#c69c6d" stroke-width="2"/>
    <text x="40" y="486" fill="#6e7750" font-size="17" font-weight="700" letter-spacing="1.5">NUTRITION INFORMATION</text>
    <text x="960" y="486" font-size="18" text-anchor="end">Approximate values per 100 g</text>
    <g font-size="21"><rect x="40" y="505" width="920" height="336" fill="#ffffff" stroke="#5a3e2b" stroke-width="1.5"/><line x1="655" y1="505" x2="655" y2="841" stroke="#5a3e2b"/><path d="M40 547H960 M40 589H960 M40 631H960 M40 673H960 M40 715H960 M40 757H960 M40 799H960" stroke="#eadfce"/>
      <text x="58" y="533" font-weight="700">Nutrient</text><text x="940" y="533" font-weight="700" text-anchor="end">Per 100 g</text>
      <text x="58" y="575">Energy</text><text x="940" y="575" text-anchor="end">{nutrition["energyKcal"]} kcal</text>
      <text x="58" y="617">Protein</text><text x="940" y="617" text-anchor="end">{nutrition["proteinG"]} g</text>
      <text x="58" y="659">Carbohydrate</text><text x="940" y="659" text-anchor="end">{nutrition["carbohydrateG"]} g</text>
      <text x="78" y="701">Total sugars / Added sugars</text><text x="940" y="701" text-anchor="end">{nutrition["totalSugarsG"]} g / {nutrition["addedSugarsG"]} g</text>
      <text x="58" y="743">Total fat</text><text x="940" y="743" text-anchor="end">{nutrition["fatG"]} g</text>
      <text x="78" y="785">Saturated fat / Trans fat</text><text x="940" y="785" text-anchor="end">{nutrition["saturatedFatG"]} g / {nutrition["transFatG"]} g</text>
      <text x="58" y="827">Sodium</text><text x="940" y="827" text-anchor="end">{nutrition["sodiumMg"]} mg</text></g>
    <line x1="40" y1="865" x2="960" y2="865" stroke="#c69c6d" stroke-width="2"/>
    <text x="40" y="900" fill="#6e7750" font-size="17" font-weight="700" letter-spacing="1.5">STORAGE</text><text x="40" y="932" font-size="20">{escape(product["storage"])}</text>
    <rect x="40" y="975" width="920" height="182" rx="5" fill="#ffffff" stroke="#5a3e2b" stroke-width="1.5"/><text x="60" y="1008" fill="#6e7750" font-size="16" font-weight="700" letter-spacing="1.2">BATCH DETAILS</text>
    <g font-size="20"><text x="60" y="1048">Batch / Lot No.</text><line x1="215" y1="1052" x2="480" y2="1052" stroke="#2b2b2b"/><text x="515" y="1048">Packed on</text><line x1="620" y1="1052" x2="940" y2="1052" stroke="#2b2b2b"/><text x="60" y="1095">Best before</text><line x1="185" y1="1099" x2="480" y2="1099" stroke="#2b2b2b"/><text x="515" y="1095">Net Qty.</text><line x1="603" y1="1099" x2="715" y2="1099" stroke="#2b2b2b"/><text x="725" y="1095">g</text><text x="765" y="1095">MRP ₹</text><line x1="835" y1="1099" x2="940" y2="1099" stroke="#2b2b2b"/><text x="940" y="1135" font-size="15" text-anchor="end">MRP inclusive of all taxes</text></g>
    <text x="40" y="1200" fill="#6e7750" font-size="16" font-weight="700" letter-spacing="1.2">MANUFACTURED &amp; PACKED BY</text><text x="40" y="1231" font-size="21" font-weight="700">TRANCHE</text><text x="40" y="1260" font-size="19">35, Parkview Apartment, Sector 15, Gurgaon, Haryana 122001, India</text><text x="40" y="1294" font-size="18">Consumer care: +91 87967 70308  |  Orders: +91 88002 06057</text><text x="40" y="1324" font-size="18">tranchebakery.in  |  @tranchebakery</text>
    <image xlink:href="FSSAI_Logo-official.png" x="790" y="1182" width="170" height="71" preserveAspectRatio="xMidYMid meet"/><text x="960" y="1273" font-size="18" text-anchor="end">Lic. No. 20826005005996</text>
    <text x="40" y="1380" font-size="15" fill="#884b36" font-weight="700">CONTENT PROOF · VERIFY MEASURED NET WEIGHT BEFORE PRINT RELEASE</text>
  </g>
</svg>
''')


def main() -> None:
    products_document = json.loads(PRODUCTS_PATH.read_text(encoding="utf-8"))
    nutrition_document = json.loads(NUTRITION_PATH.read_text(encoding="utf-8"))
    for product in PRODUCTS:
        upsert(products_document["products"], product)
        upsert_nutrition(nutrition_document["products"], product)
        (LABEL_DIR / product["filename"]).write_text(label_svg(product), encoding="utf-8")
    PRODUCTS_PATH.write_text(json.dumps(products_document, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    NUTRITION_PATH.write_text(json.dumps(nutrition_document, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    matrix = MATRIX_PATH.read_text(encoding="utf-8")
    rows = []
    for product in PRODUCTS:
        n = product["nutrition"]
        rows.append(
            f'| {product["code"]} | {product["name"]} | {product.get("nutritionYieldGrams", product["yieldGrams"])} g* | '
            f'{n["energyKcal"]} | {n["proteinG"]} | {n["carbohydrateG"]} | {n["totalSugarsG"]} / {n["addedSugarsG"]} | '
            f'{n["fatG"]} | {n["saturatedFatG"]} / {n["transFatG"]} | {n["sodiumMg"]} |'
        )
    matrix_lines = matrix.splitlines()
    matrix_lines = [line for line in matrix_lines if not any(line.startswith(f'| {product["code"]} |') for product in PRODUCTS)]
    insertion = next(index for index, line in enumerate(matrix_lines) if line == "## Calculation Decisions")
    matrix_lines[insertion:insertion] = rows + [""]
    assumption = (
        "- Sweet Bakes labels marked `*` use provisional measured-yield targets for nutrition only: BW-001 540 g baked per four-piece batch; "
        "BI-001 200 g baked per full 9–11-piece batch; BI-002 210 g per six-pack (120 g plain biscotti plus 90 g couverture). "
        "Replace with averaged production weights before print release."
    )
    if assumption not in matrix_lines:
        decision_end = next(index for index, line in enumerate(matrix_lines) if line == "## Release Boundary")
        matrix_lines.insert(decision_end - 1, assumption)
    MATRIX_PATH.write_text("\n".join(matrix_lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()