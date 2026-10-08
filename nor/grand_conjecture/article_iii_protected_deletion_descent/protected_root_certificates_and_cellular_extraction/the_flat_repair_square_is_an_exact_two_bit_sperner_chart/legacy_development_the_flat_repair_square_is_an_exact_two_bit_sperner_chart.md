# The flat repair square is an exact two-bit Sperner chart — preserved pre-item development

## Development

## The flat repair square is an exact two-bit Sperner chart

Continue with the boundary-separated flat repair square on a flat transition tetrahedron (a,b,c,d).

Its four local two-window words are

(a,b,c,d):      (x,1-x),
(a,b,d,c):      (x,x),
(b,a,c,d):      (1-x,1-x),
(b,a,d,c):      (1-x,x).

As x ranges over {0,1}, these are exactly the four binary pairs

00,01,10,11,

each occurring once.

### Cubical chart

Identify the four repair states with the vertices of an abstract square according to whether the left endpoint swap L and right endpoint swap R have been applied.

Let

F(state)
=
(alpha(first three local positions), alpha(last three local positions))
in {0,1}^2.

Then F is a bijection from the four repair states to the four vertices of the Boolean square.

After possibly complementing one or both target coordinates, F is exactly the standard cubical vertex labeling

(0,0),(1,0),(0,1),(1,1).

Thus the affine extension of F across the geometric repair square has degree one onto [0,1]^2 and has one preimage of every interior point.

### Sperner / Poincare-Miranda interpretation

The two endpoint swaps are not merely two alternative surgeries. Together they form a genuine local fixed-point chart on ACTUAL full coordinate orders.

If a global compatible-state complex is built by gluing such flat-repair squares along transport edges, the central two-window status field already satisfies the correct cubical boundary behavior on each elementary 2-cell. No tie-breaking or invented convex labels are needed locally.

Equivalently, for any prescribed binary target pair (u,v), exactly one corner of the repair square realizes that pair on the two central windows.

### Boundary provenance

The left swap preserves the ordered right boundary pair (c,d); the right swap preserves the ordered left boundary pair (a,b). Therefore the two coordinate directions of the Boolean chart are physically separated at the two sides of the packet. The chart retains the outside order and localizes all interaction to the bounded central packet.

### Article III relevance

Root §104 proves that one monotone transport flag is zero-free. Root §109 shows that the first branching of opposite repair directions is an actual square. The present theorem identifies that square with a complete two-bit cubical chart.

This suggests a faithful topological carrier built from realized repair states:
- 1-cells are audited transport moves;
- elementary 2-cells are flat repair squares carrying the exact Boolean status chart;
- overlapping adjacent-swap interactions are the bounded braid/A3 cells already under local extraction study.

A global Sperner/Poincare-Miranda obstruction on this realized complex would therefore force a genuinely compatible branching/braid event rather than a raw root cancellation.

The remaining theorem is global: prove that the relevant realized-state subcomplex has enough boundary coverage / nonzero degree after imposing the extremal witness restrictions.
