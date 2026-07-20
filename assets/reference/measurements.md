# BMW 325i Badge Measurements

This file is the dimensional source of truth for the BMW 325i badge project.
Values marked **verified** may be used as fixed CAD constraints. Values marked
**unverified** must not be treated as OEM dimensions until measured from the
reference badge or a calibrated image.

## Verified overall dimensions

| Property | Value | Status |
|---|---:|---|
| Overall width | 184.15 mm | Verified |
| Overall height | 31.75 mm | Verified |
| Maximum thickness | 4.7625 mm | Verified |
| Rear bridge thickness | 1.35 mm | Existing printable baseline; not yet OEM-verified |

## Coordinate convention

- Origin: lower-left corner of the overall badge bounding box.
- X axis: left to right.
- Y axis: bottom to top.
- Z axis: rear face to front face.
- All dimensions are millimetres.

## Character measurements still required

| Feature | Required measurement | Status |
|---|---|---|
| `3` bounding box | X, Y, width, height | Unverified |
| `2` bounding box | X, Y, width, height | Unverified |
| `5` bounding box | X, Y, width, height | Unverified |
| `i` stem bounding box | X, Y, width, height | Unverified |
| `i` dot bounding box | X, Y, width, height | Unverified |
| Character gaps | Minimum edge-to-edge gaps | Unverified |
| Main stroke widths | Representative straight and curved strokes | Unverified |
| Corner radii | Outer and inner radii by character | Unverified |
| Front crown | Rise from edge to highest point | Unverified |
| Edge bevel | Width and angle/radius | Unverified |
| Side draft | Draft angle from front to rear | Unverified |
| Rear mounting features | Position and dimensions | Unverified |

## Image calibration requirements

A photograph used for measurement should include:

1. The badge facing the camera squarely.
2. A ruler or calibration object in the same plane as the badge.
3. Enough resolution to distinguish character edges.
4. Minimal perspective distortion.
5. A separate side-profile photograph for crown, bevel, and thickness measurements.

Do not infer small dimensions from an uncalibrated perspective photograph.
