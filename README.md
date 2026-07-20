# BMW 325i Badge Generator

Current version: **26.07.20-1**

This repository contains the initial printable BMW 325i connected-emblem model and the CadQuery source used to generate the solid model.

## Dimensions

- Overall width: 184.15 mm
- Overall height: 31.75 mm
- Maximum thickness: 4.7625 mm
- Recessed rear bridge thickness: 1.35 mm

## Included files

- `src/build_badge.py` — CadQuery build script
- `output/325i_badge_outline.svg` — editable source outline
- `output/325i_badge_184.15x31.75x4.76mm.stl` — baseline printable STL
- `output/325i_badge_preview.png` — preview image
- `VERSION` — current project version
- `CHANGELOG.md` — release history

## Build the model

Run the following command from the repository root in an environment with CadQuery installed:

```powershell
python .\src\build_badge.py
```

The script generates:

```text
output/325i_badge_184.15x31.75x4.76mm.step
output/325i_badge_184.15x31.75x4.76mm_cq.stl
```

Display the project version without building:

```powershell
python .\src\build_badge.py --version
```

## Versioning

Releases use a date-based format:

- `YY.MM.DD` for the first release made on a date
- `YY.MM.DD-1`, `YY.MM.DD-2`, and so on for later revisions made that same date

Git tags include a leading `v`, such as `v26.07.20-1`.

## Current model status

This is the printable baseline. It establishes the overall silhouette, dimensions, flat rear surface, and recessed connecting bridges. Crowned faces, drafted sides, edge bevels, mounting features, and further OEM silhouette refinements remain future geometry revisions.
