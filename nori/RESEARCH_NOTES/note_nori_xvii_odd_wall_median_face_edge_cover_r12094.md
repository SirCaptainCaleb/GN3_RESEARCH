# Odd-wall median-face cover of the complement of a full cube geodesic

- Stable ID: note_nori_xvii_odd_wall_median_face_edge_cover_r12094
- Author: unspecified; session provenance retained
- Primary home: subsection:central_freudenthal_subdivision_and_the_all_root_geodesic_chamber_sphere
- Labels: combinatorial-topology, median-descent
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r12094_3
- Updated session: session_nori_r12094_3
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Let P be any full antipodal geodesic of Q_n, n>=3, extended by antipodal translation to a 2n-cycle. For each vertex p of this cycle, let a,b be the consecutive original directions on P immediately before and after p, and let F_p be the (n-2)-face through p with a,b fixed.

THEOREM (median-face edge cover). Each F_p is the median-to-p face of a three-point triangle on P, with the other two median arms of length one. Furthermore E(Q_n) \ E(P) is the union of all E(F_p). Every vertex of Q_n belongs to an odd number of these faces, and a vertex on P belongs to one.

Proof. Set q=bar(p), r=q xor e_a, s=q xor e_b. The vertices p,r,s lie on P and have cyclic gaps n-1,2,n-1. Their median is m=q xor e_a xor e_b, and the interval [m,p] is F_p. Normalize P to root 0 and dimension order (1,...,n). Define t_j(x)=x_j xor x_(j+1) for j<n, and t_n(x)=1 xor x_n xor x_1. The sum of the n bits t_j(x) is always odd. The 2n vertices of P are precisely those having one nonzero t_j. For each j, the two faces with the j-th twisted transition fixed to one are F_p and F_bar(p), with p the cycle vertex between successive directions j and j+1 (mod n). A dimension-k edge toggles only t_(k-1),t_k. If some other t_j is one, the edge belongs to the corresponding F_p. If all other t_j vanish, parity forces precisely one of t_(k-1),t_k to be one at either endpoint. Toggling direction k moves that unique transition to its neighbor, giving an edge of P. The same argument excludes P edges from all F_p and gives the odd vertex-cover multiplicity.

ODD-WALL REPRESENTATION. The map x -> (t_1(x),...,t_n(x)) induces a bijection between Q_n modulo antipodality and the odd-parity vectors in F_2^n. An original direction k flip toggles the adjacent pair (k-1,k). Rank-one transition vectors describe the projective P-cycle; rank-three vectors are the medians of admissible triples of P vertices. A pairwise different triple of transition positions gives the three median arms, each with disjoint direction support. The F_p are the two lifts of the affine hyperplanes t_j=1. These claims are combinatorial, independent of edge colors.

CONDITIONAL MEDIAN-SQUARE LAW. Now let P minimize the twisted cyclic change count d>=3 for an antipodally odd coloring. At a color-change boundary p suppose both incident constant-color runs have length at least two. Let original adjacent colors at p be A != B, and let (v,w) be the colors on the alternative two-edge path across its ab-square, ordered from p xor e_a to p xor e_b. Let Q be any spanning geodesic of F_p rooted at m=bar(p) xor e_a xor e_b, with s(Q) ordinary switches and first color alpha(Q). The arbitrary-cut median three-route inequality yields
s(Q)+[v!=A]+[w!=B]+epsilon >= d,
where epsilon=0 if v=w=1-alpha(Q) and epsilon=1 otherwise. The two singleton median-arm colors are 1-v,1-w; their interior-cut mismatch costs are [v!=A],[w!=B], and the cut at p lies on a color-change boundary. In particular, s(Q)<=d-3 forces (v,w)=(B,A), i.e. both parallel edge pairs of that square have equal colors and the two directions have opposite colors; s(Q)<=d-4 is impossible at any such boundary. This uses arbitrary nonlinear shared-edge-consistent coloring.

Scope. The covering accounts for all original edges outside P, and the conditional inequality links cheap median faces to local square structure. Neither theorem guarantees a cheap median arm in a globally minimizing bad coloring. Producing a favorable compatible arm across the overlapping face system remains open.
