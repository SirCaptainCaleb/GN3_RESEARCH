# Sorting parallel facet colors can create a monochromatic antipodal geodesic in an ordinary cube

- Stable ID: note_parallel_facet_compression_creates_zero_geodesic_20261015
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: facet-imbalance, compression, path-lifting, method-limitation
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r9314_1
- Updated session: session_nori_r9314_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Let an ordinary binary coloring on Q_3 have bits h,a,b and direction-edge colors
\[
f_h(a,b)=a\lor b,\qquad f_a(h,b)=h(1-b),\qquad f_b(h,a)=1-ha.
\]
The formulas use ordinary arithmetic on bits. They ignore the bit of the traversed direction and therefore define undirected-edge colors.

There is no color-zero full antipodal geodesic. A zero h-edge requires a=b=0, whereas a zero b-edge requires h=a=1. If h is traversed before b, then direction a must be traversed between them to change its bit from zero to one. At that a-step, h=1 and b=0, so its color is one. If b is traversed before h, then a must again be traversed between them, now from one to zero, at h=1,b=0. This again has color one.

Compress toward h=0 by replacing each pair of parallel horizontal colors (u,v) in layers h=0,1 with (min(u,v),max(u,v)); leave h-edges unchanged. The only altered function is
\[
f_b'(h,a)=1-a(1-h).
\]
The compressed cube has the color-zero full path from (h,a,b)=(0,1,1), in direction order b,a,h. Its three edge colors are zero, and its terminal vertex is (1,0,0).

Thus a generic ordinary-facet lemma asserting that this compression preserves nonexistence of a color-zero full antipodal geodesic is false. The example is not antipodally odd. The broader implication from a compressed odd coloring back to its original odd coloring remains open; it would need global information beyond this ordinary-facet lifting statement.

For an odd coloring, the same sorting operation does preserve oddness, because antipodal complementation swaps the two layers and complements their colors, and min/max are interchanged by color complementation. Repeated sorting also increases the number of one-edges weighted by the sum of their other fixed bits whenever a change occurs. Hence repeated sorting terminates at direction functions monotone in every other bit. At the all-zero root these monotone functions give a full word of type 0*1*: greedily traverse zero edges, then traverse the remaining one-edges, whose colors cannot decrease. Odd root-slide surgery then gives a monochromatic full geodesic in the compressed coloring. The missing step in this proposed closure route is its preservation under undoing compression, for which the ordinary-facet statement above cannot serve as a proof.
