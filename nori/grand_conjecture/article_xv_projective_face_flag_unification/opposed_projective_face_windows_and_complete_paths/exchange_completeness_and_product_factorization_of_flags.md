# Exchange completeness and product factorization of flags

# Exchange completeness and product factorization of flags

The universal one-step shift is not the only structure available in an arbitrary simple polytope. Its full face incidence gives a strong extension property for local paths, and products admit a factorization into independent full paths and shuffles.

Let \(P\) be a simple convex \(d\)-polytope and let \(\mathcal F(P)\) be its maximal face flags, identified with canonical affine-basis walks.

**Theorem 1 (any two incident edges extend to a complete flag).** Let \(d\ge2\). For every pair of distinct edges \(uv\), \(vw\) incident at a common vertex \(v\), there is a maximal face flag whose canonical walk begins
\[
\boxed{\quad u\longrightarrow v\longrightarrow w.\quad}
\tag{1}
\]
Thus every ordered nonbacktracking two-edge walk of \(G(P)\) occurs as the first two steps of a complete basis path.

*Proof.* At a vertex of a simple polytope, every pair of incident edges lies in a unique two-dimensional face \(F\). Start the desired flag with \(F_0=\{u\}\subset F_1=uv\subset F_2=F\). Since \(F\) is a polygon, its unique edge at \(v\) other than \(uv\) is \(vw\). Extend the partial face chain to a maximal chain through \(P\), which is possible in any finite graded face lattice. The canonical path begins with (1), as claimed. \(\square\)

**Corollary 2 (unconditional first-switch avoidance).** If \(d\ge3\), every binary coloring of the undirected edges of \(P\) has a complete face-flag path whose first two edges have the same color. No antipodal symmetry is needed.

*Proof.* At any vertex \(v\), there are \(d\ge3\) incident edges. Two have the same color by the pigeonhole principle. Order these edges as \(uv\), \(vw\) and apply Theorem 1. \(\square\)

When \(d=3\), the complete path has three edges, so its first two equal bits imply at most one switch over the entire path. Consequently every binary edge coloring of every simple three-dimensional polytope has a one-switch complete face-flag path, even in the absence of an opposition involution.

This local extension property is a structural distinction from a sparse cycle of affinely independent basis paths: in the full simple-polytope graph, all choices of two incident edges are realized by complete flags. It rules out globally alternating complete edge-color words, and is the elementary input behind stronger switch-selection attempts in higher ranks.

**Theorem 3 (factorization of complete flags in products).** Let \(P,Q\) be simple convex polytopes of dimensions \(p,q\). Maximal face flags of the \((p+q)\)-polytope \(P\times Q\) are in canonical bijection with triples
\[
\boxed{
(\mathcal F_P,\mathcal F_Q,\sigma),\qquad
\mathcal F_P\in\mathcal F(P),\quad
\mathcal F_Q\in\mathcal F(Q),
}
\tag{2}
\]
where \(\sigma\) is a shuffle of \(p\) symbols \(P\) and \(q\) symbols \(Q\), retaining the internal order within each factor. Under this correspondence, the canonical complete basis path of the product flag is the corresponding interleaving of the factor paths, moving in precisely one factor at each step.

*Proof.* Every nonempty face of \(P\times Q\) is \(A\times B\) with \(A\) a face of \(P\) and \(B\) a face of \(Q\), and its dimension is \(\dim A+\dim B\). In a maximal product flag, each rank increase raises the dimension of precisely one factor by one. Recording which factor increases gives the shuffle \(\sigma\); deleting repeated factor faces leaves independent maximal flags of \(P\) and \(Q\). Conversely, any two factor flags and a shuffle determine a maximal product flag by advancing the chosen factor at each rank.

An edge of the product is either an edge of \(P\) times a vertex of \(Q\), or vice versa. The unique edge leaving a product face \(A\times B\) in the next enlarged product face is the unique exiting edge in whichever factor advances, with the other factor's current vertex fixed. Thus the canonical product walk is the indicated interleaving. Its moves form a basis because the factor moves form bases of complementary direct-sum spaces. \(\square\)

**Corollary 4 (a natural enlarged geometric class).** If \(P,Q\) have central involutions mapping their face lattices freely, then \(P\times Q\) has the free central involution \((x,y)\mapsto(\tau_Px,\tau_Qy)\) on its flag sphere and an induced free involution on first-order edge incidences. Hence products of centrally symmetric simple polytopes supply opposed first-order projective-window systems. In particular, the conjecture covers arbitrary products of centrally symmetric polygons, segments, and other centrally symmetric simple factors, rather than being restricted to cubes.

*Proof.* The product of the central face automorphisms carries each proper face \(A\times B\) to \(\tau_P(A)\times\tau_Q(B)\). A nonempty proper face of a centrally symmetric full-dimensional polytope cannot equal its antipodal image: a supporting hyperplane of such a face lies strictly away from the central interior point, while its antipodal hyperplane has opposite support value. Thus no proper face is fixed; the induced flag action is free. The image of a proper edge under central inversion is another edge, never the same edge. The corresponding map on undirected first-order projective incidences is therefore free and transforms each complete flag's word by applying the incidence involution without changing its position order. \(\square\)

Theorem 3 explains why products are a serious test for the common conjecture: they have abundant complete basis paths formed by all shuffles, yet their face incidence is richer than either a single simplex or a cube. The one-switch existence assertion on arbitrary products with arbitrary odd colorings remains open.
