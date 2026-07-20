# Reference Measurement Workflow

## Front-view measurements

1. Photograph or scan the badge straight-on.
2. Crop without rotating or rescaling non-uniformly.
3. Calibrate the image using the verified 184.15 mm overall width.
4. Confirm that the calibrated height is approximately 31.75 mm.
5. Record every character bounding box and edge-to-edge gap in
   `assets/reference/measurements.md`.
6. Compare the SVG outline against the reference at 50% opacity.

## Side-profile measurements

Record:

- total thickness;
- flat rear thickness;
- front crown rise;
- bevel width;
- edge radius or bevel angle;
- any side-wall draft.

## Acceptance checks

Before a geometry revision is released:

- overall width is 184.15 mm;
- overall height is 31.75 mm;
- maximum thickness is 4.7625 mm, unless deliberately revised;
- generated solids are valid;
- STL and STEP exports complete without errors;
- the version in `VERSION`, the changelog, and the Git tag agree.
