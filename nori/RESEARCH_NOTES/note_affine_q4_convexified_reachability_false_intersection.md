# Affine Q4 certificate: convex reachability intersections need not splice

- Stable ID: note_affine_q4_convexified_reachability_false_intersection
- Author: unspecified; session provenance retained
- Primary home: article:nori_article_ix_unification
- Labels: proved, topology, obstruction, nori1
- Lifecycle: active
- Epistemic status: proved
- Current version: 6
- Retention: current and at most one previous snapshot
- Created session: session_nori_r0_2
- Updated session: session_nori_r6202_2
- Disposition: none
- Successor: none

## Related references

- note:note_antipodal_geodesic_reachability_splicing
- article:nori_article_viii_edges

## Research note

# A legal affine Q4 obstruction to convexified reachability extraction

Take bit coordinates x=(x_0,x_1,x_2,x_3) in Q_4 and color each undirected direction-i edge by

c_0(x)=1+x_1,
c_1(x)=x_0+x_2+x_3,
c_2(x)=1+x_0,
c_3(x)=x_1,

with values in F_2. The expression for c_i is independent of x_i, so each edge has a well-defined color. Every displayed affine row contains an odd number of other coordinate variables, hence c_i(bar x)=1+c_i(x); the coloring is antipodally odd.

Let R(u;0) be the set of vertices accessible from u by an all-zero *geodesic*, including the empty path. Encode vertices as integers x_0+2x_1+4x_2+8x_3. precise monotone reachability from u=0 and bar u=15 gives

R(0;0)={0,2,3,7,8},
R(15;0)={1,4,9,10,11,12,14,15}.

Proof/certificate: the entire directed (root-monotone) zero-edge reachable transition network from 0 is 0→2, 0→8, 2→3, 3→7. The network from 15 is 15→14, 15→11, 14→12, 11→10, 11→9, 12→4, 9→1. All other root-monotone outgoing edges of these reachable vertices have color one; direct substitution verifies exhaustion. Thus the two vertex sets are DISJOINT and no all-zero antipodal geodesic starts at 0 (or 15).

Nevertheless the vertices 7 and 8 are antipodes, and both belong to R(0;0), while 1 and 14 are antipodes, and both belong to R(15;0). Consequently the geometric cube center (1/2,1/2,1/2,1/2) lies in BOTH Euclidean convex hulls: it is (7+8)/2 and (1+14)/2 in bit-vector notation. Hence

conv(R(0;0)) ∩ conv(R(15;0)) ≠ ∅

while R(0;0) ∩ R(15;0) = ∅.

This explicitly disproves a naive *convexified-reachability intersection implies geodesic splice* extraction statement even for affine, legal antipodally odd cube-edge colorings, already in dimension four. A topological fixed point or convex-hull intersection requires an additional discrete extraction mechanism certifying a common reachable CUBE VERTEX. The valid metric splicing lemma remains precise once that common vertex exists. The internal antipodal pairs in the separate reachability sets certify 2-cp paths, a weaker property than the desired monochromatic antipodal geodesic at the prescribed root.

Scope: a root-fixed obstruction to one particular topological extraction step, NOT a counterexample to unrestricted NORI1 or to other topological complexes that preserve common-vertex witnesses.
