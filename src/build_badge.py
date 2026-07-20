from pathlib import Path
import cadquery as cq

WIDTH = 184.15
HEIGHT = 31.75
THICKNESS = 4.7625
BRIDGE_THICKNESS = 1.35

HERE = Path(__file__).resolve().parent
SVG_FILE = HERE.parent / "output" / "325i_badge_outline.svg"
OUT_DIR = HERE.parent / "output"
OUT_DIR.mkdir(exist_ok=True)

visible = cq.importers.importSVG(str(SVG_FILE)).wires().toPending().extrude(THICKNESS)

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

model = visible.union(rear_bar).union(i_bridge)

cq.exporters.export(model, str(OUT_DIR / "325i_badge_184.15x31.75x4.76mm.step"))
cq.exporters.export(model, str(OUT_DIR / "325i_badge_184.15x31.75x4.76mm_cq.stl"))

print("Generated STEP and CadQuery STL in:", OUT_DIR)
