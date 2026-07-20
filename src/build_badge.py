import argparse
from pathlib import Path

import cadquery as cq

WIDTH = 184.15
HEIGHT = 31.75
THICKNESS = 4.7625
BRIDGE_THICKNESS = 1.35

HERE = Path(__file__).resolve().parent
PROJECT_ROOT = HERE.parent
VERSION_FILE = PROJECT_ROOT / "VERSION"
SVG_FILE = PROJECT_ROOT / "output" / "325i_badge_outline.svg"
OUT_DIR = PROJECT_ROOT / "output"


def project_version() -> str:
    """Return the version stored in the repository VERSION file."""
    try:
        return VERSION_FILE.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        return "unknown"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate the BMW 325i badge STEP and STL files."
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {project_version()}",
    )
    return parser.parse_args()


def build_badge() -> cq.Workplane:
    """Build and return the baseline connected BMW 325i badge model."""
    if not SVG_FILE.is_file():
        raise FileNotFoundError(f"Badge outline SVG not found: {SVG_FILE}")

    visible = (
        cq.importers.importSVG(str(SVG_FILE)).wires().toPending().extrude(THICKNESS)
    )

    rear_bar = (
        cq.Workplane("XY")
        .center(0, HEIGHT * 0.34 - HEIGHT / 2)
        .rect(WIDTH - 10.0, 2.0)
        .extrude(BRIDGE_THICKNESS)
    )

    i_bridge = (
        cq.Workplane("XY")
        .center(WIDTH * 0.895 - WIDTH / 2, HEIGHT * 0.595 - HEIGHT / 2)
        .rect(1.6, HEIGHT * 0.53)
        .extrude(BRIDGE_THICKNESS)
    )

    return visible.union(rear_bar).union(i_bridge)


def main() -> None:
    parse_args()
    OUT_DIR.mkdir(exist_ok=True)

    model = build_badge()
    basename = "325i_badge_184.15x31.75x4.76mm"
    step_file = OUT_DIR / f"{basename}.step"
    stl_file = OUT_DIR / f"{basename}_cq.stl"

    cq.exporters.export(model, str(step_file))
    cq.exporters.export(model, str(stl_file))

    print(f"BMW 325i badge generator {project_version()}")
    print(f"Generated: {step_file}")
    print(f"Generated: {stl_file}")


if __name__ == "__main__":
    main()
