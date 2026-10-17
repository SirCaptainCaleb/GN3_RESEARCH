# Two-direction square connectors and opposed-core geodesic forcing

- Stable ID: note_nori_antipodal_two_direction_square_connector_20261017
- Author: Independent NORI1 critical-star researcher
- Primary home: subsection:square_defects_and_path_order_holonomy_in_dimension_simple_chain_lifts
- Labels: NORI1, square-curvature, geodesic-core, fixed-coloring, critical-star
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11254_3
- Updated session: session_nori_r11254_3
- Disposition: none
- Successor: none

## Related references

- None

## Research note

**Theorem (two-direction antipodal square connector; all n>=3).** Let c be an antipodally odd binary undirected-edge coloring of Q_n. Fix distinct directions i,j and vertices a, b=a xor e_i xor e_j. Suppose a red dimension-simple path R of length n-2 runs from b to bar a using all directions other than i,j. Let the four square colors be p=c(a,a+e_i), q=c(a+e_i,b), r=c(a,a+e_j), s=c(a+e_j,b), with red=0 and blue=1.

There are six full antipodal geodesics containing R as a contiguous subpath: two with both missing directions prepended, two with both appended, and two with one prepended and the other appended. At least one is red if and only if (p,q,r,s) differs from (0,1,0,1). The unique failure pattern has the two edges incident to a red and the two incident to b blue. Consequently, nonzero square curvature kappa(F)=p xor q xor r xor s always permits a red full antipodal completion.

**Proof.** Prepending two steps succeeds in order (i,j) if p=q=0, and in order (j,i) if r=s=0. Appending two steps succeeds if p=q=1 or r=s=1: antipodal oddness complements all the colors along the appended routes. For the mixed two completions, one succeeds if p=1,q=0 and the other if r=1,s=0. Thus all six fail only when each pair (p,q),(r,s) has unequal entries and neither pair equals (1,0); equivalently both equal (0,1). The exceptional pattern has zero curvature. All candidates use every direction once and connect antipodal endpoints because R traverses each other direction once and starts at b and ends at bar a. The two opposite squares are disjoint for n>=3, and no auxiliary face vertex occurs internally on R, establishing dimension simplicity.

**Theorem (opposed same-color cores force completion).** If, in addition, there is a red (n-2)-edge dimension-simple path R' from a to bar b using all directions other than i,j, then one of these two cores extends to a red full antipodal geodesic regardless of the four colors on F. Indeed, failure for R requires a-red/b-blue on the face, whereas failure for R' requires b-red/a-blue. These requirements cannot hold together.

**Critical-star avoidance corollary.** If a prescribed antipodal pair U is disjoint from both red cores and both opposite two-faces, the opposed-core theorem provides a red full geodesic avoiding U. Likewise one red core at a nonflat square supplies an avoiding red geodesic when U misses that core and the two opposite faces.

**Audit and scope.** A standalone Python verifier, nori_two_direction_connector.py, enumerates all 16 patterns (p,q,r,s), all six antipodal path completions, and n=3,...,11, confirming 15 successful patterns and one obstructing pattern in each dimension. The proof holds uniformly in n. The two-core theorem is a local sufficient condition inside the original coloring. It does not assert that arbitrary legal colorings contain the required near-full red cores, and hence does not settle NORI1. This new connector formulation and sharp obstruction complement the existing square-defect operators and earlier one-edge antipodal closing lemma.
