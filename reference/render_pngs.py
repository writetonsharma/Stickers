"""Render TRANCHE packaging SVG masters to dimensionally accurate PNG proofs."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from xml.etree import ElementTree

try:
    from PIL import Image
    from resvg_py import svg_to_bytes
except ImportError as error:
    raise SystemExit(
        "Missing renderer dependencies. Run: "
        r".\.venv\Scripts\python.exe -m pip install -r "
        r"LogoAndStickers\print-render-requirements.txt"
    ) from error


ARTWORK_DIR = Path(__file__).resolve().parent
FINAL_LABELS_DIR = ARTWORK_DIR / "RegulatoryLabels-FinalProof"
FINAL_LABEL_PNG_DIR = ARTWORK_DIR / "RegulatoryLabels-FinalProof-300dpi"
DEFAULT_MASTERS = (
    ARTWORK_DIR / "LogoSticker-75mm.svg",
    ARTWORK_DIR / "FreshnessSeal-Universal.svg",
    ARTWORK_DIR / "RegulatoryLabel-ClassicTableWhite.svg",
    ARTWORK_DIR / "BreadCareCard-ThankYou.svg",
    ARTWORK_DIR / "BreadCareCard-Care.svg",
)
PHYSICAL_LENGTH = re.compile(r"^\s*(\d+(?:\.\d+)?)\s*mm\s*$", re.IGNORECASE)


def millimetres(value: str, attribute: str, source: Path) -> float:
    match = PHYSICAL_LENGTH.fullmatch(value)
    if not match:
        raise ValueError(
            f"{source.name}: SVG {attribute} must use millimetres, got {value!r}"
        )
    return float(match.group(1))


def dimensions(source: Path, dpi: int) -> tuple[int, int]:
    root = ElementTree.parse(source).getroot()
    width_mm = millimetres(root.attrib.get("width", ""), "width", source)
    height_mm = millimetres(root.attrib.get("height", ""), "height", source)
    width_px = round(width_mm / 25.4 * dpi)
    height_px = round(height_mm / 25.4 * dpi)
    return width_px, height_px


def destination_for(source: Path) -> Path:
    if source.parent.resolve() == FINAL_LABELS_DIR.resolve():
        return FINAL_LABEL_PNG_DIR / f"{source.stem}.png"
    return source.with_name(f"{source.stem}-300dpi.png")


def render(source: Path, dpi: int) -> Path:
    width_px, height_px = dimensions(source, dpi)
    destination = destination_for(source)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(
        svg_to_bytes(
            svg_path=str(source),
            resources_dir=str(source.parent),
            width=width_px,
            height=height_px,
            dpi=float(dpi),
            text_rendering="optimize_legibility",
            image_rendering="optimize_quality",
        )
    )

    with Image.open(destination) as image:
        image.load()
        image.save(destination, dpi=(dpi, dpi))
    with Image.open(destination) as check:
        if check.size != (width_px, height_px):
            raise RuntimeError(
                f"{destination.name}: expected {width_px}x{height_px}, got "
                f"{check.width}x{check.height}"
            )
    return destination


def collect_sources(arguments: list[Path]) -> list[Path]:
    if not arguments:
        sources = [path for path in DEFAULT_MASTERS if path.exists()]
        if FINAL_LABELS_DIR.exists():
            sources.extend(sorted(FINAL_LABELS_DIR.glob("*.svg")))
        return sources

    sources: list[Path] = []
    for argument in arguments:
        path = argument.resolve()
        if path.is_dir():
            sources.extend(sorted(path.glob("*.svg")))
        elif path.is_file() and path.suffix.lower() == ".svg":
            sources.append(path)
        else:
            raise ValueError(f"Not an SVG file or directory: {argument}")
    return list(dict.fromkeys(sources))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Render packaging SVGs at their declared physical dimensions. "
            "With no paths, regenerate the approved packaging proof set."
        )
    )
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="SVG files or directories containing SVG files",
    )
    parser.add_argument("--dpi", type=int, default=300, help="output DPI (default: 300)")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.dpi <= 0:
        raise ValueError("DPI must be greater than zero")

    sources = collect_sources(args.paths)
    if not sources:
        raise ValueError("No SVG files found")

    for source in sources:
        destination = render(source, args.dpi)
        width_px, height_px = dimensions(source, args.dpi)
        print(f"Rendered {source.name} -> {destination.name} ({width_px}x{height_px})")
    print(f"Rendered {len(sources)} SVG file(s) at {args.dpi} DPI.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, RuntimeError, ValueError, ElementTree.ParseError) as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)