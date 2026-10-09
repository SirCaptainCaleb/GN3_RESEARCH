# Equivariant zero curves force an odd-degree connector graph on all antipodal root pairs

# An antipodal zero-locus connector between distinct geodesic roots

Let \(n\ge2\) and let \(K_n\) be the all-root antipodal-geodesic simplicial pseudomanifold. The antipodal involution \(\tau:v\mapsto\bar v\) has precisely \(2^{n-1}\) isolated fixed points \(m_e\), one midpoint for each unordered antipodal endpoint pair \(e=\{x,\bar x\}\). Remove disjoint small invariant open ball neighborhoods of these points. Denote the resulting compact \(n\)-dimensional pseudomanifold with boundary by \(M_n\). Each boundary component \(B_e\) is the suspension of the Coxeter sphere \(\operatorname{sd}(\partial\Delta^{n-1})\), so
\[
(B_e,\tau)\cong(S^{n-1},u\mapsto-u),\qquad B_e/\tau\cong\mathbb RP^{n-1}.
\]
The action on \(M_n\) is free.

**Theorem (odd-degree root-connector theorem).** Let \(f:M_n\to\mathbb R^{n-1}\) be a generic equivariant piecewise-linear map, with \(f(\tau z)=-f(z)\). Then its zero set descends to a compact one-dimensional manifold \(\Gamma=f^{-1}(0)/\tau\), consisting of circles and arcs. For every antipodal root-pair \(e\), the number of endpoints of \(\Gamma\) on \(B_e/\tau\) is **odd**. Consequently the multigraph on the \(2^{n-1}\) antipodal root-pairs, with one edge for every arc of \(\Gamma\) joining distinct boundary components (arcs returning to the same component count as loops), has odd degree at every vertex. In particular, for every root pair \(e\) there is a zero-set connector to a *different* root pair.

**Proof.** Equivariant PL general position is available because the involution acts freely: triangulate the quotient, assign generic compatible values to pairs of lifted vertices, and subdivide if necessary. Require the origin to avoid the images of all faces of dimension at most \(n-2\), including boundary faces of dimension at most \(n-2\). In each \(n\)-simplex, the transverse zero set is then empty or a line segment; it meets any \((n-1)\)-face at most once. Every interior \((n-1)\)-face lies in exactly two top simplices, so the segments glue in pairs. Each boundary \((n-1)\)-face lies in exactly one, yielding a degree-one endpoint. Lower-dimensional singularities are avoided. Thus the zero set, and its free-involution quotient, is a compact PL one-manifold with boundary.

On the component \(B_e/\tau\cong\mathbb RP^{n-1}\), the equivariant map \(f|_{B_e}\) defines a section of the rank-\((n-1)\) bundle \(\gamma^{\oplus(n-1)}\), where \(\gamma\) is the tautological line bundle. Its top Stiefel–Whitney class is
\[
w_{n-1}(\gamma^{\oplus(n-1)})
=w_1(\gamma)^{n-1}\ne0
\quad\text{in }H^{n-1}(\mathbb RP^{n-1};\mathbb F_2).
\]
For a transverse section the mod-two number of zeros evaluates this class on the fundamental class, giving exactly \(1\). Hence the number of boundary zero orbits on each \(B_e\) is odd.

An arc with both endpoints on \(B_e/\tau\) contributes two to that boundary's endpoint count, whereas an arc with one endpoint there and the other on a different boundary contributes one. Circles contribute zero. Since the total endpoint count at \(e\) is odd, its number of cross-boundary arcs is odd, proving all claims. \(\square\)

**Meaning for NORI / Hartman.** Unlike Borsuk–Ulam's pointwise zero, this theorem forces a whole *root-changing connector*. Its conclusion is independent of the coloring: for any generic odd \(f\), zero curves link distinct antipodal endpoint pairs. To solve NORI, construct \(f\) from genuine ordered-three-face one-switch reachability or defect data so that an inter-root zero curve entails a compatible insertion/exchange, a strictly decreasing defect, or an actual one-switch antipodal geodesic. The theorem establishes the topological connector, while the color-compatible extraction remains unproved. The theorem applies directly to the all-root simplicial geometry; lifting labels from the 2n-bit torus requires the actual equivariance and incidence checks.
