# Common-edge geodesic carriers collapse below the antipodal index

- Stable ID: note_nori_xiv_common_edge_dowker_carrier_equivariant_collapse_20261020_r12002
- Author: session_nori_r12002_2
- Primary home: article:nori_article_xiv_type_a_rook_gallery_topology
- Labels: topology, method-obstruction, dimension-uniform, dowker, geodesic-incidence
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r12002_2
- Updated session: session_nori_r12002_2
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Let \(n\ge3\), \(Q_n\) be the cube, \(\tau\) central antipodality, and \(\mathcal G_n\) the set of complete unoriented cube geodesics. Define
\[
K_n=\{A\subseteq\mathcal G_n:\text{all paths in }A\text{ share a cube edge}\}.
\]
The involution acts freely on \(K_n\).

**Theorem.** \(K_n\) is \(\tau\)-equivariantly homotopy equivalent to a free complex of dimension at most \(n-2\). Hence there is no equivariant map \(S^{n-1}\to |K_n|\).

*Proof.* Let \(L_n\) have as vertices the edges of \(Q_n\), and simplices the edge sets contained in a common complete geodesic. The incidence-poset proof of Dowker duality, natural under the antipodal action, gives \(K_n\simeq_\tau L_n\).

A maximal simplex of \(L_n\) has vertices the edges \(e_1,\ldots,e_n\) of a complete geodesic \(v_0v_1\cdots v_n\). Remove any internal edge \(e_k\), \(2\le k\le n-1\). The remaining edge graph has two path components with endpoint pairs \((v_0,v_{k-1})\) and \((v_k,v_n)\). Completing these components to a full geodesic requires one connecting cube edge. Among the four terminal pairings only \(v_{k-1}v_k=e_k\) is a cube edge: the three others have Hamming distances \(k\), \(n-k+1\), and \(n\), respectively, each at least two. Thus this codimension-one face belongs to a unique maximal simplex.

Choose such free faces in antipodal pairs. They are free, and collapsing all the maximal simplices along the selected free faces in antipodal pairs leaves a free equivariant complex of dimension at most \(n-2\). For every free \(\mathbb Z_2\)-complex of dimension \(d\), cellular approximation of the classifying map of the quotient yields an equivariant map into \(S^d\). Therefore an equivariant map from \(S^{n-1}\) to \(K_n\) would produce an equivariant map \(S^{n-1}\to S^{n-2}\), contradicting Borsuk–Ulam. \(\square\)

**Scope.** This excludes a coloring-independent full-index antipodal carrier whose simplices represent complete geodesics with a common original edge. It leaves open color-dependent carrier gluings. A weaker sufficient simplex condition is that all paths have the same color in one common direction. For direction-indexed color signs \(z_i(P)=(-1)^{c(e_i(P))}\), the centered vector \(z(P)-n^{-1}(\sum_j z_j(P))\mathbf1\) is antipodally odd; its affine extension cannot vanish on a color-unanimous simplex unless a participating path is monochromatic. Consequently a full-index equivariant carrier using these color-unanimous simplices would imply NORI1. Such a carrier has not been constructed.

## Weakening common-edge overlap to color agreement: a sharp index criterion

For a legal coloring \(c\), every full path \(P\) uses a unique original edge \(e_i(P)\) in each direction \(i\). Write its direction-indexed profile \(w(P)\in\mathbb F_2^n\), \(w_i(P)=c(e_i(P))\). Define a *color-agreement path complex*
\[
U_c=\{A\subseteq\mathcal G_n:\exists i\in[n], a\in\mathbb F_2,\ \forall P\in A,\ w_i(P)=a\}.
\]
This contains \(K_n\) and is antipodally invariant; \(\tau\) complements every profile.

**Theorem (sharp antipodal-index dichotomy).** For \(n\ge2\):
\[
\boxed{\operatorname{ind}_{\mathbb Z_2}U_c=n-1
\iff \mathcal W(c)=\mathbb F_2^n,}
\]
where the index is the least \(d\) admitting a \(\tau\)-equivariant continuous map into \(S^d\). If any profile is omitted, an explicit equivariant map \(U_c\to S^{n-2}\) exists.

*Proof.* Regard the \(2n\) literals \((i,a)\) as vertices \((-1)^a e_i\) of the boundary of the \(n\)-crosspolytope \(\mathcal O_n=\operatorname{conv}\{\pm e_i\}\). The Dowker incidence dual of \(U_c\) is the simplicial subcomplex
\[
D_c=\bigcup_{w\in\mathcal W(c)}\operatorname{conv}\{(-1)^{w_i}e_i:i\in[n]\}\subseteq\partial\mathcal O_n.
\]
Incidence-poset duality gives \(U_c\simeq_\tau D_c\). If all profiles occur, \(D_c=\partial\mathcal O_n\cong S^{n-1}\) antipodally, so its index is \(n-1\).

If \(w\notin\mathcal W(c)\), then \(\bar w\notin\mathcal W(c)\). Set \(v=((-1)^{w_1},\ldots,(-1)^{w_n})\). The only two points of \(\partial\mathcal O_n\) parallel to \(v\) are \(\pm v/n\), lying in the interiors of the missing opposite facets. Consequently orthogonal projection onto \(v^\perp\), followed by normalization, provides an odd map \(D_c\to S(v^\perp)\cong S^{n-2}\). Transport through equivariant Dowker equivalence. \(\square\)

**Interpretation and prior work.** Article VIII's unrestricted full-profile span theorem proves \(\operatorname{aff}_{\mathbb F_2}\mathcal W(c)=\mathbb F_2^n\), and already identifies universal full-profile surjectivity as equivalent to NORI1 by direction-dependent global recoloring. Hence the high-index criterion above is a new topological formulation of the same unsolved obligation, without resolving NORI1. The common-edge complex loses top index by elementary collapse regardless of the coloring; the weaker color-agreement complex recovers top index precisely when every direction-color facet is realized. This identifies the necessary *color-dependent gluing*: a sphere-valued obstruction cannot be defeated by profile affine span or shared-edge incidences alone.

The dual type-\(B_n\) Coxeter sphere in Article XIV provides a canonical full-dimensional antipodal domain with chamber vertices representing complete geodesics. Constructing a color-agreement carrier map from that sphere would finish NORI1, but Article XIV's primary unanchored cells and their nonzero projective obstruction show that extension across their boundaries is the missing step. Any future proposal must exploit shared-square compatibility between cells and produce one complete path witness; per-cell independent color assignments cannot force it.
