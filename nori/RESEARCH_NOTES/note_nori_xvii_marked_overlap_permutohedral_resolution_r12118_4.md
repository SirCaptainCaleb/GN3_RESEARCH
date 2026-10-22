# Equivariant marked-gallery resolution of median mixed overlap

- Stable ID: note_nori_xvii_marked_overlap_permutohedral_resolution_r12118_4
- Author: unspecified; session provenance retained
- Primary home: subsection:central_freudenthal_subdivision_and_the_all_root_geodesic_chamber_sphere
- Labels: NORI1, combinatorial-topology, Freudenthal, permutohedral-carrier, mixed-overlap, cohomological-index, integral-witnesses
- Lifecycle: active
- Epistemic status: proved
- Current version: 4
- Retention: current and at most one previous snapshot
- Created session: session_nori_r12118_4
- Updated session: session_nori_r12132_2
- Disposition: none
- Successor: none

## Related references

- note:note_nori_median_arm_mobius_ladder_nerve_index_r12061_3
- note:note_nori_xvii_median_three_route_telescoping_r12024_2

## Research note

# Equivariant marked-gallery resolution of the median mixed overlap

Fix any antipodally odd binary coloring of the original undirected edges of Q_n and a full antipodal geodesic P of odd twisted defect d>=5. Let m be its canonical seam-majority vertex. Use the two opposed run-face unions U_+,U_- of note_nori_median_arm_mobius_ladder_nerve_index_r12061_3, with W=U_+ intersect U_-. That established theorem gives: W is a finite cubical subcomplex, tau(W)=W, neither m nor bar(m) lies in W, and W has the reduced integral homology of S^(h-1), where h=2 floor((d-1)/4)>=2.

For any cube vertex x put S(x)={i:x_i != m_i}. Triangulate each cubical face of W by the root-m Freudenthal triangulation, forming K. Every simplex sigma of K has an ordered vertex chain x_0,...,x_k with S_0 subsetneq ... subsetneq S_k, S_j=S(x_j). Let Perm_n be the root-m permutohedron: its vertices are full direction permutations. For sigma define A_sigma as the face of Perm_n consisting of permutations for which every S_j occurs as an initial direction set. With D_0=S_0, D_j=S_j\ S_(j-1) for 1<=j<=k, D_(k+1)=[n]\ S_k, it is the product of permutohedra for the ordered blocks D_0,...,D_(k+1). All these faces are nonempty.

THEOREM (marked-gallery carrier). Let

  E_W = {(z,p) in |K| x Perm_n : p in A_sigma whenever z lies in relint(sigma)}.

(1) E_W is a compact polyhedron and the projection rho:E_W -> |W| has nonempty convex, contractible fibers rho^(-1)(z)=A_sigma.

(2) A vertex permutation pi of A_sigma determines a full original-cube geodesic m->bar(m) visiting x_0,...,x_k in order, using every direction once. All intermediate edges between consecutive marked vertices lie inside their shared cubical face of W; the prefix to x_0 lies in some face of U_+, and the suffix from x_k lies in some face of U_-. Thus every marked gallery is a compatible original-edge path, and each permutohedral edge is a legal adjacent-direction square exchange preserving all marks.

(3) If R:Perm_n -> Perm_n reverses the permutation and tau is cube antipodality, then J(z,p)=(tau z,Rp) is a free involution of E_W. For every marked full path, J is antipodal translation followed by reversal; its direction-indexed signed color profile changes sign.

(4) rho induces a mod-two cohomology isomorphism E_W/J -> W/tau, preserving the covering class u in degree one. Consequently,

  H^*(E_W/J;F_2)=F_2[u]/(u^h),   u^(h-1) != 0.

In particular, no equivariant continuous map E_W -> S^(h-2) exists. The marked-gallery carrier has cohomological antipodal index h-1.

PROOF. Every S_j prefix constraint defines a permutohedral face. Their nested intersection is the face of the ordered partition D_0|...|D_(k+1), a product of permutohedra. If eta is a face of sigma, dropping a marked vertex merges two successive blocks, giving A_sigma subset A_eta as a face. Hence the incidence union defining E_W is closed under limits at the boundaries of K simplices, proving it is compact and polyhedral with the stated fibers.

The block ordering forces the rooted full path to pass through all x_j. Consecutive marked vertices lie in a common cubical face F of W, so every direction-once route between them lies in F. Because x_0 lies in U_+, some positive run face contains x_0 and m, and hence the full interval [m,x_0]; similarly some negative run face contains [x_k,bar(m)]. Permutations within each ordered block generate the product permutohedron by adjacent swaps, preserving the marks and original edge identities. This proves (1),(2).

Antipodality sends the increasing support chain S_0<...<S_k to the increasing chain [n]\S_k<...<[n]\S_0. Reversing permutations exchanges these ordered blocks. Therefore J maps A_sigma to A_(tau sigma), respects the incidence polyhedron, and is free because tau has no fixed points on W. The original edge on each direction in the reversed antipodal path is the antipodal mate of the corresponding edge of the original path; binary colors complement. This proves (3).

The quotient projection is a proper surjection between compact finite polyhedra. Its fiber over [z] is homeomorphic to A_sigma: choose z in its free tau-orbit. All fibers are contractible, so Vietoris-Begle gives an isomorphism in mod-two cohomology. Equivariance identifies the double-cover classes.

The established homology calculation for W gives H^*(W;F_2) one-dimensional in degrees 0 and h-1, vanishing otherwise. In the Cartan-Leray spectral sequence of the free tau-action, the only possible nonzero transgression is d_h(a_(h-1))=u^h. It must be nonzero, or W/tau would have nonzero cohomology in unbounded degrees, contradicting its finite dimension. Hence H^*(W/tau;F_2)=F_2[u]/(u^h). The quotient projection transports this ring and u to E_W/J. An equivariant map to S^(h-2) would annihilate u^(h-1), contradiction.

REMAINING GAP. E_W carries the nonzero mixed-overlap projective obstruction and simultaneously carries full shared-edge-consistent paths with one use of every direction. This eliminates a geometric incompatibility of witnesses. No implication has been proved from the absence of defect-one paths to a zero-free odd map E_W -> S^(h-2), nor from a fractional zero of an interpolated color profile to a monochromatic member of a permutohedral fiber. Such a color-filtered obstruction or an integral low-defect exchange is required. The d=3 case has W empty and remains assigned to the median three-route mechanism.

COROLLARY (simultaneous balanced path statistics on one compatible marked chain). Let r be any integer with 1<=r<=h-1, and fix r original directions i_1,...,i_r. There exist a simplex sigma of the rooted Freudenthal triangulation of W and a probability law on the full original-cube geodesics indexed by the vertices of A_sigma such that

  E[(-1)^(c_(i_j)(P))]=0  for every j=1,...,r,

where c_i(P) is the color of the unique direction-i edge of P. Every path in this law visits all vertices of sigma in their support order, and the two end arms assemble into one direction-once full geodesic.

PROOF. At a vertex pi of Perm_n assign the vector of r signed colors ((-1)^(c_(i_j)(m,pi)))_j. The reversal R negates this vector by antipodal oddness of the edge coloring. Extend these vertex labels to a continuous R-odd map on Perm_n using its barycentric subdivision: at each face barycenter take the average of its vertex labels, then interpolate along flags. Its restriction to E_W through the second factor is J-odd. Since u^r != 0 on E_W/J for r<=h-1, the restriction must vanish somewhere; otherwise normalization gives an equivariant map E_W -> S^(r-1), annihilating u^r. The zero lies over some sigma and in A_sigma; affine interpolation on a flag of faces of A_sigma writes the zero as a convex combination of the signed vectors at its vertex permutations. This gives the probability law. All represented permutations satisfy the same marked-prefix constraints.

LIMITATION. The law may involve multiple full paths. No constituent is required to be monochromatic or to have twisted defect below d. The marked-chain constraint retains original support compatibility, while the missing implication is a color-sensitive integral selection or exchange from this compatible family.

## Residual projective index on compatible color walls (session session_nori_r12132_2)

Let k=h-1 for h=2 floor((d-1)/4) and d>=5. Fix r<=k original directions I. Assign each permutation pi of the root-m permutohedron the r-vector of signed colors of its unique direction-i edges (i in I). Reversal R negates every sign, since the corresponding rooted edge is antipodal. Average signs on face barycenters and interpolate along flags to obtain an R-odd PL map f_I on the permutohedron. Its restriction to E_W is J-odd; on every fiber A_sigma its image lies in the convex hull of the sign vectors of the original full-path vertices.

Let Z_I=f_I^(-1)(0) in E_W. Let K_I be the antipodally invariant subcomplex of the Freudenthal triangulation of W consisting of simplices sigma for which BOTH colors of every selected original direction i occur among paths indexed by vertices of A_sigma. Deleting a mark enlarges A_sigma, so this is a subcomplex.

THEOREM. The covering class satisfies u^(k-r) != 0 on Z_I/J and also on K_I/tau. In particular, for r=k, one compatible marked simplex admits original paths with color variation in all r selected directions; for r<k the locus of such simplices retains cohomological antipodal index at least k-r.

PROOF. The standard equivariant zero-locus lemma says: if u^k !=0 on compact free Z2-space X and f:X->R^r is odd (r<=k), then u^(k-r) !=0 on the quotient of f^(-1)(0). Otherwise, an invariant neighborhood of the zero set kills u^(k-r), while normalization f/||f|| on its complement gives an equivariant map to S^(r-1), killing u^r there. The relative cup product kills u^k on X, contradiction. Apply with X=E_W. A zero over relint(sigma) is a convex combination of the signed path profiles at vertices of A_sigma, and consequently both signs of every selected direction occur there. Thus the equivariant projection Z_I->K_I transports nonvanishing of the covering-class power.

Every simplex of K_I simultaneously hosts an ORIGINAL SQUARE sensitivity witness for each i in I: two permutations in the product permutohedron A_sigma have different direction-i edge colors, and are joined by adjacent swaps within its blocks. Some swap must change direction-i color. Such a swap necessarily interchanges i with some direction j in its same block, and Delta_j c_i=1 on the corresponding original ij-square. Different selected i can have different squares, but all are witnessed within the one marked-face carrier. Shared-edge consistency and direction simplicity are automatic.

This is a nonlocal simultaneous sensitivity theorem, not a low-defect geodesic theorem. Rank-phase alternation can coexist with abundant sensitivity; an additional median-energy inequality is necessary to turn the surviving cohomology into a defect-reducing exchange.

## Uniform separation of the mixed-overlap carrier from every canonical seam arm (session session_nori_r12132_2)

Let d=2r+1>=5 and use the cyclic blue-run support partition [n]=B_0 disjointunion ... disjointunion B_(d-1). Let m be the canonical seam-majority, z_j the red-to-blue seams, and A_j=D(m,z_j)=B_(j-r) union ... union B_(j-1), the union of r consecutive cyclic run blocks. Each positive run face F_(z_k) fixes all directions in B_k union B_(k+r) at the m-bit values, and its antipodal negative face F_(bar z_k) fixes those directions at the opposite bit values. Put W=(union_k F_(z_k)) intersect (union_k F_(bar z_k)), and b_min=min_k |B_k|>=1.

THEOREM (spoke-separation lemma). For every j and every original cube vertex x in W,

  d_H(x,I(m,z_j)) >= b_min,
  d_H(x,I(bar m,bar z_j)) >= b_min.

In particular the cubical subcomplex W is disjoint from every canonical median-arm interval I(m,z_j) and from every antipodal arm I(bar m,bar z_j). Consequently no marked vertex of E_W lies on any of the d canonical arms H_j:m->z_j of the proved d-route telescoping theorem.

PROOF. Let S(x)={i:x_i != m_i}. The interval I(m,z_j) consists of vertices y with S(y) subset A_j. Therefore d_H(x,I(m,z_j))=|S(x)\ A_j|. Since x belongs to the negative family, x lies in F_(bar z_k) for some k, and S(x) contains the entire two blocks B_k and B_(k+r). The r-consecutive block interval A_j cannot contain both indices k and k+r in a d=2r+1 cyclic set: the shorter cyclic distance is r, while an interval of r consecutive indices has maximum distance r-1. Hence some complete block of size at least b_min lies in S(x)\ A_j. This proves the first inequality.

Similarly x lies in some F_(z_l), hence both B_l,B_(l+r) lie outside S(x). The interval I(bar m,bar z_j) consists of vertices with support containing [n]\ A_j. Since A_j cannot contain both B_l,B_(l+r), at least one whole block lies outside A_j and also outside S(x). Thus d_H(x,I(bar m,bar z_j))=|([n]\ A_j)\ S(x)|>=b_min. QED.

RESEARCH CONSEQUENCE. The nonzero projective class on W and E_W is geometrically separated from all canonical median arms used in the d-route telescoping inequality. The simultaneous color-wall/sensitivity certificates in E_W therefore have no immediate status as witnesses for the canonical arm switch costs s_j. A future forcing argument must furnish a color-controlled transfer from the mixed equator toward the positive/negative spokes, preserving direction simplicity and costing fewer than the defect budget. The separation can be arbitrarily large when all monochromatic runs of P have large length, so bounded-radius transport has no uniform justification. This sharply identifies the compatibility step beyond the previously established cohomological index.
