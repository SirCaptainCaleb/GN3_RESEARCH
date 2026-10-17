# Cubelike Pfaffian parity, matching duality and Arf classification

- Stable ID: note_nori_cubelike_pfaffian_matching_duality_20261016_r10917
- Author: unspecified; session provenance retained
- Primary home: subsection:paired_direction_involutions_and_geodesic_endpoint_matchings
- Labels: NORI1, cubelike, Pfaffian, perfect-matching, mod-two, dimension-uniform
- Lifecycle: active
- Epistemic status: proved
- Current version: 4
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10917_3
- Updated session: session_nori_r10917_3
- Disposition: none
- Successor: none

## Related references

- note:note_nori_signed_complex_structures_pfaffian_20261016
- note:note_nori_folded_cube_transit_conservation_20261016_r10917

## Research note

Let V=F_2^r, r>=1, N=2^r, and let g_1,...,g_d be distinct nonzero group elements. Build the simple cubelike graph G=Cay(V,{g_i}), so undirected edges join x and x+g_i. Choose any orientation of every edge and let K_i be the skew-symmetric signed adjacency supported on direction g_i, with K_i(x,x+g_i)=+1 if x->x+g_i and -1 if reversed. Put K(t)=sum_i t_i K_i, with commuting formal indeterminates t_i.

THEOREM 1 (orientation-independent binary Pfaffian polynomial). Over F_2[t_1,...,t_d],
Pf(K(t)) = (t_1+...+t_d)^(N/2) = sum_i t_i^(N/2).
In particular, if I is any subset of generator labels, the union of their matchings has an odd number of perfect matchings if and only if |I| is odd. For odd d, the full skew adjacency K=K(1,...,1) has odd integer Pfaffian and odd determinant, hence is invertible over R for every orientation. This includes every odd folded cube G_d (r=d-1; generators g_i=1+e_i).

PROOF. Modulo two, K_i becomes the permutation matrix T_i of the translation x->x+g_i; the T_i commute and satisfy T_i^2=I. In characteristic two all T_i are commuting unipotents, since (T_i+I)^2=0, and can be simultaneously upper triangularized over an algebraic closure with each diagonal entry one. Hence
det(K(t)) mod2=det(sum_i t_i T_i)=(sum_i t_i)^N.
Because K(t) is skew-symmetric with vanishing diagonal, its determinant is its Pfaffian squared over the integer polynomial ring, hence after reduction modulo two. The Frobenius square map is injective on F_2[t], giving Pf(K(t))=(sum t_i)^(N/2). As N/2 is a power of two for r>=2, the last expression is sum_i t_i^(N/2). For r=1, N/2=1 and the same identity holds.

An alternative combinatorial proof: translation of V acts on perfect matchings, preserving the number of matched edges of each generator label. Every orbit has power-of-two cardinality. Modulo two, only translation-fixed matchings survive. A matching fixed by all translations that contains one g_i-edge must contain all g_i-edges, hence is the full direction-g_i matching. Thus the parity-weighted matching generating polynomial has one surviving pure monomial t_i^(N/2) per generator. Pfaffian orientation signs disappear modulo two.

THEOREM 2 (complementary matching parity duality). Suppose d is odd. For every even-cardinality subset S of vertices,
#PM(G[S]) = #PM(G[V-S]) (mod 2).
In particular G has an odd number of perfect matchings; after deleting two distinct vertices u,v, the remaining graph has an odd number of perfect matchings if and only if uv is an edge of G. Thus the entire cubelike adjacency relation is recovered from parity of vertex-deleted perfect matchings.

PROOF. Let A be the unsigned adjacency matrix over F_2. Since A=sum_i T_i, commutativity and T_i^2=I yield A^2=dI=I, hence det A=1 and A^{-1}=A. For any even S, Jacobi's complementary principal-minor identity gives
det A[V-S]=det(A) det((A^{-1})[S])=det A[S].
Every principal submatrix here is alternating over F_2 (symmetric and zero diagonal). Its determinant is the square of its Pfaffian, and in F_2 the square of a field element is itself. The Pfaffian mod2 is the parity of the number of perfect matchings on the induced vertex set. This gives the duality. For |S|=2, the induced S graph has an odd matching iff u,v are adjacent.

EXHAUSTIVE FINITE AUDIT. For G_5 (the 16-vertex folded five-cube, generators 1,2,4,8,15 on F_2^4), the identity A^2=I was checked entrywise over F_2; a recursive matching parity counter independently checked Theorem 2 on all 32768 even-cardinality subsets S. Every one satisfied the complement parity equality, and the full graph had an odd number of perfect matchings. For G_3=K4, the graph has three perfect matchings, again odd.

SHARP LIMITATION. This parity theorem alone does not imply any directed odd cycle: it holds for every orientation, including orientations directed according to a total vertex order, which have no directed cycles. Near balance is a separate essential condition. Even combined with near balance, the established Q7 rooted alternating-geodesic obstruction shows the Pfaffian invariant does not force a shortest directed odd cycle through every prescribed vertex. No claim of unrestricted NORI1 closure is made here.

COROLLARY (every orientation edge has nonvanishing Pfaffian influence). Under Theorems 1-2, let d be odd and K be the oriented integer skew adjacency. Then its determinant and Pfaffian are odd. Its inverse has rational entries with odd denominators and, reducing those entries modulo two, satisfies K^{-1}=A. In particular the inverse entry corresponding to an edge is odd modulo two, while a nonedge inverse entry is even modulo two. For any directed edge u->v, the Pfaffian of the skew principal minor K[V-{u,v}] is odd, and flipping just the orientation of uv changes Pf(K) by a nonzero integer congruent to two modulo four. Consequently Pf(K) modulo four records the parity of the set of edges whose orientations were reversed relative to any fixed reference orientation.

PROOF. K reduces modulo two to A and A^2=I; the odd determinant makes K invertible over the localization of Z at two. Therefore K^{-1} reduces to A. The inverse-Pfaffian cofactor formula, or the complementary matching parity theorem, gives oddness of the vertex-deleted minor for every edge. In a Pfaffian expansion along u, the dependence on the skew entry K_uv is linear with coefficient plus or minus Pf(K[V-{u,v}]). Negating K_uv therefore changes the Pfaffian by plus or minus twice that odd integer, which is nonzero and congruent to two modulo four. Iterating across any collection of edge flips gives the parity statement.

SMALL COMPUTATIONAL AUDIT. With G_5 on F_2^4 and lexicographic edge orientation, direct integer Pfaffian recursion yields Pf(K)=9. The Pfaffian minor after deleting vertices 0 and 1 is 3. Flipping orientation of edge 0-1 changes Pf(K) from 9 to 3, a difference of minus six, congruent to two modulo four. This audit and the all-subsets parity check give independent evidence of the cofactor formula.

DECISIVE LIMITATION. The property holds for acyclic orientations of the folded cube as well as near-balanced ones; hence it cannot alone ensure a directed shortest odd cycle. The orientation-sensitive higher two-adic Pfaffian coefficients might encode interactions, but the present results neither identify a monochromatic-geodesic coefficient nor prove its nonvanishing. Further extension is not justified without such a direct bridge.


COROLLARY (uniform half-rank theorem for oriented cubelike graphs). For every orientation D of a finite cubelike graph G on N=2^r vertices with an odd number d of generators,
rank_F2(D) >= N/2
and rank_R(D) >= N/2.
No assumption on indegree, outdegree, connectivity of the oriented digraph, or coloring locality is needed. In particular every near-balanced folded G_(2m+1) has rank_R(D)>=2^(2m-1), sharpening the earlier lower bound greater than one third of its matrix size from the common-neighbor estimate.

PROOF. Reduction modulo two gives D+D^T=A because each undirected edge is oriented once. The preceding involution A^2=I gives rank_F2(A)=N. Subadditivity and equality of transposed ranks yield N=rank_F2(D+D^T)<=2rank_F2(D), giving the first bound. Rank over R of a zero-one integer matrix is no smaller than rank modulo two, by a minor with odd determinant, giving the second. Equivalently over R the skew matrix K=D-D^T is nonsingular, and rank K<=2rank D. QED.

SMALL AUDIT. For the near-balanced folded G5 orientation induced by the legal Q5 coloring (c0,c1,c2,c3,c4)=(x1,x0,1+x1,1+x0,x0), 1000 orientations obtained by legal directed-square reversals had binary directed-adjacency ranks between 13 and 16 on its 16 vertices, consistent with the theorem. The theorem itself is noncomputational and applies to all orientations.


## Arf classification of the orientation-independent cubelike quadratic form

Let G=Cay(F_2^r,S) be a simple cubelike graph with N=2^r vertices and odd valency |S|. Write A for its unsigned adjacency over F_2. For an orientation D, define
q_G(z)=z^T D z=sum_({u,v} edge) z_u z_v (mod 2),
where z is a vector indexed by graph vertices. This expression does not depend on the orientation, because each edge contributes once. Its polar form is B(z,w)=z^T A w. As A^2=I, B is nondegenerate symplectic, and q_G has a well-defined Arf invariant.

**THEOREM (complete Arf classification).** The Arf invariant of q_G is one if G is the complete graph K4, and zero for every other simple odd-valent cubelike graph. In particular every odd folded cube G_d for odd d>=5 has Arf invariant zero, whereas G_3=K4 has Arf invariant one. The classification holds without assuming G is connected.

*Proof for non-complete cubelike graphs.* Since the generator set S is a proper subset of the nonzero vectors, choose a nonzero group element h not in S. Let T_h translate graph vertices by h. Consider the half-dimensional linear subspace
L_h=im(I+T_h)={z:z_v=z_(v+h) for all v}.
It has dimension N/2 because T_h is a free fixed-point-free involution on the vertex set. Since A commutes with T_h and (I+T_h)^2=0, the polar form vanishes on L_h.

To see that the quadratic form itself vanishes, take z=(I+T_h)y. Since translation by h preserves graph edges, q_G(T_h y)=q_G(y). Polarizing gives
q_G(z)=q_G(y)+q_G(T_h y)+B(y,T_h y)=y^T A T_h y.
The matrix A T_h is symmetric over F_2. Its diagonal entry at vertex v equals A_(v,v+h), which vanishes because h is not a generator. A symmetric zero-diagonal matrix has y^T A T_h y=0 in characteristic two. Hence L_h is totally singular of dimension N/2. Since q_G is nondegenerate, it is hyperbolic and has Arf invariant zero.

*Proof for complete graphs.* The only complete cubelike graph on V=F_2^r has S=V minus {0}, so G=K_N with N=2^r. For a vertex subset of size k, the induced edge count has parity q_G=binom(k,2) mod 2. Its Gauss sum is
sum_(z in F_2^N) (-1)^{q_G(z)}
= sum_(k=0)^N binom(N,k)(-1)^(k(k-1)/2)
= Re((1-i)(1+i)^N)
= 2^((N+1)/2) cos((N-1)pi/4).
For N=2 this is +2, for N=4 it is -4, and for every N>=8 a power of two it equals +2^(N/2). By the nondegenerate quadratic Gauss sum formula, the sign is (-1)^Arf(q_G). Therefore K4 alone is nonsplit. QED.

**COROLLARY (rank gap in the nonsplit case).** For every orientation D of G, rank_F2(D)>=N/2. If q_G has Arf invariant one, then rank_F2(D)>=N/2+1 and the same lower bound holds over R. In particular any orientation of K4 has adjacency rank at least three.

*Proof.* If rank D=N/2, then ker D has dimension N/2. For x,y in ker D, B(x,y)=x^T(D+D^T)y=0, and q_G(x)=x^T D x=0. Thus ker D is a half-dimensional totally singular subspace, forcing Arf(q_G)=0. Contraposition proves the additional unit of rank in the nonsplit case. QED.

**EXPLICIT EVEN-EDGE SUBSPACE.** The proof furnishes an unconditional combinatorial certificate for every cubelike graph missing some translation direction h: for every vertex set Y, the symmetric difference Z=Y triangle (Y+h) spans an induced subgraph with an even number of edges. There are N/2 independent binary choices for such Z. This property does not require any orientation.

**FINITE CHECK.** A symplectic Gram-Schmidt computation of the quadratic form for folded G_d gives Arf values one, zero, zero, zero in dimensions d=3,5,7,9. An independent enumeration of the 64 orientations of G3=K4 gives real adjacency ranks 3 or 4, with no rank-two case.

**Implication and limit.** The universal mod-two invertibility theorem yields a half-rank guarantee for every orientation. The Arf invariant creates an additional rank obstruction only in the small K4 case; from dimension five onward it is identically split. This eliminates a proposed proof of unrestricted NORI1 via a nonsplit quadratic or parity invariant. Invertibility, matching parity, and Arf type hold independently of the existence of monochromatic full geodesics.
