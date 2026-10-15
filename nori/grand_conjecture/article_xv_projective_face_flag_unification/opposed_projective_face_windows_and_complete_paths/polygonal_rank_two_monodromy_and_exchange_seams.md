# Polygonal rank-two monodromy and exchange seams

# Polygonal rank-two monodromy and exchange seams

The universal flag shift \(T=r_0r_1\cdots r_{d-1}\) holds for every simple polytope. However, the local effect of a rank-one exchange depends on the size of the containing two-dimensional face. This is relevant to color-sensitive chain fillings.

Let \(P\) be a simple \(d\)-polytope, \(d\ge2\), and let \(\mathcal F\) be a maximal flag whose initial two-face \(F_2\) is a polygon with \(p\ge3\) vertices. Label its vertices cyclically \(u_0,u_1,\ldots,u_{p-1}\), such that the canonical complete path of \(\mathcal F\) begins \(u_0,u_1,u_2\).

**Theorem 1 (rank-one exchange and the square criterion).** Let \(r_1\) change only the first edge face \(F_1=u_0u_1\), retaining the initial root \(u_0\) and the containing two-face \(F_2\). The canonical path of \(r_1\mathcal F\) begins
\[
\boxed{\quad u_0,u_{p-1},u_{p-2}.\quad}
\tag{1}
\]
The two complete paths have a common vertex after their second steps if and only if \(p=4\). When \(p=4\), the two initial two-edge routes are the opposite routes across a quadrilateral and rejoin at \(u_2\), so their entire suffix from that vertex onward coincides.

*Proof.* Since \(F_2\) is a polygon, the two edges incident with \(u_0\) in \(F_2\) are \(u_0u_1\) and \(u_0u_{p-1}\). The flip \(r_1\) replaces the former by the latter. At the new first endpoint \(u_{p-1}\), the unique edge within \(F_2\) leaving \(u_0u_{p-1}\) is \(u_{p-1}u_{p-2}\); this gives (1). The second-step endpoints agree precisely when \(u_2=u_{p-2}\), namely \(p=4\). If the endpoints agree, the unchanged higher-rank faces and uniquely determined exiting edges give the same remaining suffix. \(\square\)

**Theorem 2 (polygonal rank-two monodromy).** Restrict attention to the rank-two residue of flags with a fixed first two-face \(F_2\). The product \(r_0r_1\) cyclically shifts the initial vertex and its directed boundary edge by one position, giving
\[
\boxed{\quad (r_0r_1)^p=1\quad}
\tag{2}
\]
on this residue, with least positive period \(p\).

*Proof.* The two flips affect only the initial vertex and edge. Applying \(r_0\) changes \(u_i\) to \(u_{i+1}\) along the selected edge \(u_iu_{i+1}\). Applying \(r_1\) then selects the other edge at \(u_{i+1}\) within \(F_2\), namely \(u_{i+1}u_{i+2}\). Thus each application advances the directed edge once around the polygon. It returns after \(p\) steps and no earlier. \(\square\)

**Corollary 3 (limitation of a direct square filling).** Any attempted chain map that glues two complete paths related by a single \(r_1\) exchange at their common endpoint after two steps, while preserving the remaining suffix, works on quadrilateral rank-two faces and fails on other polygonal rank-two faces. A common color-sensitive one-switch proof across arbitrary simple polytopes must therefore use the intrinsic polygonal dihedral monodromy (2), or a stronger global carrier, instead of identifying all rank-two exchanges with cubical commuting squares.

Triangles and squares appear here as the first two values of the natural parameter \(p\), not as alternative classes inserted into the conjecture. The mathematical task is to develop coherent equivariant chain fillings over all rank-two \(2p\)-flag residues that respect projective-incidence coloring and attach compatibly in higher-dimensional cells. Theorem 2 supplies the underlying residue cycles; the required color-sensitive chain assignment remains open.
