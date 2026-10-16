# Odd-cube monochromatic geodesic orbit bottleneck and product cylinders

- Stable ID: note_nori_odd_q3_geodesic_orbit_bottleneck_20261015
- Author: unspecified; session provenance retained
- Primary home: subsection:extremal_geodesic_blockers_and_exponential_paired_root_stability
- Labels: verified_counterexample, geodesic, edge_flip, product
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r9962_4
- Updated session: session_nori_r9962_4
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Write Q_3 vertices as integers with bits x_0,x_1,x_2, and color direction-i edges by the bit-independent rules
c_0(x)=1-x_1, c_1(x)=x_2, c_2(x)=x_1.
Each rule flips under x->bar x, so the coloring is antipodally odd.

**Proposition (a geodesic edge bottleneck).** Every color-zero full antipodal geodesic traverses the undirected edge e={2,3}. There are four oriented color-zero full geodesics, represented by (root, direction order)
(2, (0,1,2)), (3, (0,1,2)), (4, (2,1,0)), (5, (2,1,0)).
The corresponding vertex sequences are
(2,3,1,5), (3,2,0,4), (4,0,2,3), (5,1,3,2).
These are all color-zero full geodesics.

*Proof.* Since c_0=0 requires x_1=1, c_1=0 requires x_2=0, and c_2=0 requires x_1=0, a red full path must traverse direction 2 before direction 0, or direction 0 before direction 2 with the intervening direction 1 appropriately placed. Checking the six possible direction orders against these three color rules leaves precisely the four displayed rooted paths (the two admissible orders are (0,1,2) and (2,1,0)); each contains {2,3}. This is a finite complete certificate. QED.

The antipodal edge bar e={4,5} is color one. Thus the antipodal orbit {e,bar e} meets every monochromatic full geodesic: all color-zero geodesics use e, and all color-one geodesics use bar e (by antipodal complementation). This disproves the proposed universal strengthening: 'in every good odd coloring, for each antipodal edge orbit, some monochromatic full geodesic avoids that orbit'. In particular, it prevents a proof of NORI1 by preservation of an *unchanged* monochromatic witness under every single orbit flip. Flipping this orbit does leave the coloring good, but every monochromatic full geodesic of the original coloring uses the changed orbit.

**Dimension-uniform cylinder extension.** Let g be any legal odd coloring of Q_r admitting a color-zero full geodesic, and let h be the Q_3 coloring above. In the Cartesian product h\boxtimes g on Q_(3+r), every color-zero full geodesic crosses the 2^r-edge cylinder C_e={((2,y),(3,y)):y in Q_r}, because its projection to Q_3 is a color-zero full geodesic of h. Conversely, concatenating witnesses of h and g shows the product has full color-zero geodesics. Products of legal good colorings of Q_2 and Q_3 give such examples in every dimension n>=5 (as well as n=3). The cylinder is a family of antipodal edge orbits in high dimension; the construction does not claim that one particular edge orbit is used by every full geodesic of the product.

**Scope.** This is a counterexample to geodesic-orbit avoidance, which is stronger than NORI1. It does not supply a NORI1 counterexample and does not rule out a color-changing replacement witness after an edge-orbit flip.
