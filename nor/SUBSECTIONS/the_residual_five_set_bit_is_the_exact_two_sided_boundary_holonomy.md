# The residual five-set bit is the exact two-sided boundary holonomy

## Metadata

- ID: the_residual_five_set_bit_is_the_exact_two_sided_boundary_holonomy
- Parent Section: directed_nor_union_closed_bridge
- Position: 130
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## The residual five-set bit is exactly the two-sided boundary-reversal holonomy

Normalize a double-full singleton five-set as in subsection 124:
alpha(0,1,2)=0,
alpha(1,2,3)=1,
alpha(2,3,4)=0,
with both transition tetrahedra {0,1,2,3} and {1,2,3,4} fully curved. Let
t=alpha(0,1,4)=alpha(0,2,4)=alpha(0,3,4).

Suppose we seek a monochromatic reordering of these five vertices which preserves the two boundary pair *sets* {0,1} and {3,4}, but reverses both ordered pairs so that it can potentially match the opposite color on both external sides.

There is only one such five-vertex order:
(1,0,2,4,3),
because the remaining vertex 2 must occupy the middle position.

Its three statuses are:
alpha(1,0,2)=1-alpha(0,1,2)=1,
alpha(0,2,4)=t,
alpha(2,4,3)=1-alpha(2,3,4)=1.

Hence its word is exactly
1, t, 1.

### Holonomy theorem
A double-full singleton gadget admits a monochromatic resolution reversing both boundary pairs if and only if
t=1.
In that case the unique two-sided resolution is
(1,0,2,4,3)
and is monochromatic color 1.

If t=0, no monochromatic resolution can simultaneously reverse both boundary pairs while preserving their underlying endpoint sets. One must use a one-sided resolution and pay a reconnection defect on the opposite side.

### Interpretation
The residual bit t is therefore not an arbitrary leftover face value. It is exactly a local Z_2 holonomy:
- t=1 means the singleton packet can be passed through the five-set with both boundary orientations reversed coherently;
- t=0 means two-sided coherent passage is obstructed, and any monochromatic cancellation must export the mismatch through one boundary.

This gives a natural transport invariant for the closed-component problem. A sequence of local singleton cancellations carries a boundary-orientation bit. Returning to the same ordered boundary data requires the total exported holonomy around the cycle to vanish. If the repair dynamics force an odd number of t=0 one-sided passages, the component cannot close.

The next task is to compute how this holonomy bit changes under the audited two/three-position repair moves.

## Frontier

- Development version when composed: None
- Development version now: 1
