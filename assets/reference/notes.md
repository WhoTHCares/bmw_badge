# BMW 325i Badge Reference Notes

## Current baseline

The current CadQuery script imports the existing SVG outline, extrudes it to the
full thickness, and unions two recessed rear reinforcement features:

- one long horizontal rear bar;
- one vertical bridge behind the disconnected `i` elements.

The current release is therefore a printable silhouette baseline, not yet an
OEM surface reproduction.

## Locked constraints

- Preserve the overall 184.15 mm by 31.75 mm bounding box.
- Preserve the maximum 4.7625 mm thickness unless a later physical measurement
  supersedes it.
- Keep the rear face flat unless mounting measurements require otherwise.
- Do not modify character outlines based only on subjective appearance.

## Geometry work order

1. Calibrate the front reference image.
2. Measure each character bounding box and gap.
3. Correct the 2D outline while preserving the overall bounding box.
4. Validate the outline by overlaying it on the calibrated reference.
5. Add the front crown and edge transitions.
6. Reassess the hidden rear reinforcement.
7. Add mounting features only after physical measurements are available.

## Revision rule

A geometry change should include at least one of the following:

- a new verified measurement;
- a calibrated overlay comparison;
- a printability correction supported by a test print;
- a documented manufacturing constraint.
