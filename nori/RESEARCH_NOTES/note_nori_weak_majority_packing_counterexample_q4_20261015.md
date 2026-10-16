# Q4 weighted-majority path-packing obstruction and fractional certificate

- Stable ID: note_nori_weak_majority_packing_counterexample_q4_20261015
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: counterexample, packing, weighted-majority
- Lifecycle: active
- Epistemic status: proved
- Current version: 4
- Retention: current and at most one previous snapshot
- Created session: session_nori_r9657_1
- Updated session: session_nori_r9657_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

**Theorem (packing obstruction in Q4).** Write vertices as (t,a,b,c) and set Phi=(-1)^a+(-1)^b+(-1)^c. Give edges of positive midpoint potential color zero and edges of negative midpoint potential color one. Middle-layer tied edges join supports {u} to {u,v} among a,b,c; color these zero precisely when u->v in the directed triangle a->c->b->a, and one otherwise, independent of t. This tie choice is antipodally odd, because complement takes the edge {u}--{u,v} to {w}--{v,w}, where {u,v,w}={a,b,c}, and u->v holds iff w->v fails in the directed triangle. Thus this is a legal weak weighted-majority coloring.

Any zero-colored full antipodal geodesic stays within Hamming layers 0,1,2 in the (a,b,c) bits, since every edge incident to layer three has color one. Orient such a geodesic from layer one to complementary layer two. Ignoring its t-step, the three direction changes must have layer sequence 1,0,1,2 or 1,2,1,2. The latter is impossible: at its first visit to a layer-two vertex, the arrival and departure middle-layer edges are the edges from singleton u and singleton v to {u,v}. The directed triangle gives these two edges opposite colors. Hence every zero full antipodal geodesic has layer sequence 1,0,1,2 and uses TWO of the six zero edges between Hamming layers zero and one (three directions, two t-slices). Pairwise edge-disjoint zero full geodesics therefore number at most three.

The maximum three is attained by the edge-disjoint antipodal geodesics 2--3--1--9--13, 5--4--0--2--10, and 7--5--1--0--8, where t,a,b,c have binary weights 1,2,4,8. All edges on these paths are zero. Thus the conjectured 2^(n-2)=4 edge-disjoint zero antipodal geodesics fails already at n=4, despite every zero edge extending to some zero geodesic.

The fractional packing number is also three: assign dual weight 1/2 to each of the six layer-zero-to-one zero edges, and zero to the other ten zero edges. Every zero full path receives total dual weight one, certifying the fractional packing upper bound three. Conversely the three displayed paths attain three.

The minimum cardinality of a hitting set of zero edges meeting every zero full geodesic is four, established by an exhaustive check of the binom(16,3) triples of zero edges and the four-edge upper bound given by one full zero direction matching. Therefore the false decomposition conjecture must be separated from the potentially useful, strictly weaker transversal conjecture tau>=2^(n-2).

**Dimension-uniform obstruction.** For any n>=4 let m=n-3, use m zero-weight dimensions u and three positive-weight dimensions a,b,c, and set Phi(u,a,b,c)=(-1)^a+(-1)^b+(-1)^c. Color every edge by the sign of its midpoint Phi, and on the ties between core-Hamming layers one and two use the same directed triangle a->c->b->a, independently of u. The coloring is antipodally odd and is a weak weighted-majority coloring with nonzero weights. Every zero full antipodal geodesic, after orienting from core layer one to its complementary layer two, has core-layer pattern 1,0,1,2; the other possible pattern 1,2,1,2 would require two opposite colors at one layer-two core vertex. The m zero-weight steps do not affect this argument. Thus every zero full geodesic contains two core-direction edges between layers zero and one. There are 3*2^m such zero edges, giving the dimension-uniform edge-disjoint packing upper bound 3*2^(m-1)=3*2^(n-4), which is three quarters of 2^(n-2). In particular the proposed perfect packing fails for all even n>=4, by a fixed factor rather than just an additive defect. The edge-extension theorem continues to ensure every zero edge belongs to some monochromatic-zero full antipodal geodesic. This is an obstruction to a packing proof, not a refutation of transversal robustness.

**Witness count in the packing obstruction family.** For n=m+3 the number of unoriented monochromatic-zero antipodal geodesics is 3*2^(m-1)*(m+2)!. Orient each such path from core Hamming layer one to core layer two. Its initial core singleton has three choices and its m zero-weight root bits have 2^m choices. The core moves are forced to delete the initial singleton first, add one other dimension second, and add the remaining dimension last; the cyclic tie choice permits only one order of the two latter moves. All m zero-weight flips occur before the final core move, since zero-weight edges at core layer two have color one. They may otherwise be interleaved arbitrarily with the first two core moves, in (m+2)!/2 ways. Thus the count is 3*2^(m-1)*(m+2)!. For n=4 this is 18 and for n=6 it is 1440, although no more than 3*2^(n-4) can be edge-disjoint.
