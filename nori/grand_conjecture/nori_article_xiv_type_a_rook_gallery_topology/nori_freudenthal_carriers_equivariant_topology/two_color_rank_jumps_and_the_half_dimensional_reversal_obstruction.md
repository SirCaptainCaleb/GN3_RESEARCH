# Two-color rank jumps and the half-dimensional reversal obstruction

Let \(n\ge5\), let \(c:E(Q_n)\to\mathbb F_2\) be antipodally odd, and let \(K_a=\Delta P_a(c)\) be the monochromatic endpoint complexes of the preceding Subsections, embedded in the oriented-interval torus. Write
\[
K=K_0\cup K_1,\qquad I=K_0\cap K_1,\qquad
R(u,v)=(\bar v,\bar u).
\tag{1}
\]
The involution \(R\) exchanges \(K_0\) and \(K_1\) and preserves their intersection. A vertex \(p=(u,v)\) has rank \(r(p)=d(u,v)\). An edge \([p,q]\) belongs to \(I\) when the same oriented endpoint extension is feasible in both colors, with all traversed dimensions disjoint.

**Theorem 1 (two-color rank jump).** If distinct vertices \(p=(u,v)\), \(q=(u',v')\) are comparable in \(I\), then
\[
\boxed{r(q)-r(p)\ge2}
\tag{2}
\]
after ordering them so that \(p\prec q\). Moreover, writing
\[
a=d(u',u),\qquad b=d(v,v'),\qquad
r(q)-r(p)=a+b,
\tag{3}
\]
every nonzero one of \(a,b\) is at least two.

*Proof.* The comparison \(p\prec q\) in each \(K_t\), \(t=0,1\), requires color-\(t\) geodesics \(u'\to u\) and \(v\to v'\), allowing empty paths, with the distance equality (3). If \(a=1\), the edge \(u'u\) would have to have color zero and color one simultaneously. Hence \(a\ne1\). Similarly \(b\ne1\). Since \(p\ne q\), at least one of \(a,b\) is positive, proving the result. \(\square\)

**Theorem 2 (sharpness of the rank jump).** For every \(n\ge5\), put \(m=\lfloor(n-3)/2\rfloor\). There is a legally antipodally odd coloring for which \(I\) contains a simplex with \(m\) vertices of ranks
\[
\boxed{2,4,\ldots,2m.}
\tag{4}
\]
Consequently the rank-jump dimension bound below is sharp as a statement about unrestricted legal colorings.

*Proof.* Put \(v_s=\sum_{i=1}^{2s}e_i\), for \(0\le s\le m\). For \(1\le s\le m\), prescribe on the two-dimensional square based at \(v_{s-1}\), in directions \(2s-1,2s\), that the route traversing \(2s-1\) then \(2s\) has color word \(00\), and that the alternative route has word \(11\). The squares have pairwise disjoint direction sets. Moreover \(2m\le n-3\), so at least three unused dimensions have bit zero on every prescribed edge. No two such edges are antipodal, and these prescriptions therefore extend freely to a legal antipodally odd coloring by giving every antipodal mate the complementary color.

For every \(s\), concatenating the color-zero routes through the first \(s\) squares gives a color-zero geodesic from \(0\) to \(v_s\), and concatenating the color-one routes gives a color-one geodesic with the same endpoints. Hence \(p_s=(0,v_s)\) is a vertex of \(I\). The routes across the \(s\)-th square also supply the color-zero and color-one terminal extensions witnessing \(p_{s-1}\prec p_s\) for \(s\ge2\). Thus the \(p_s\) form a simplex of \(I\) with the asserted ranks. \(\square\)

**Corollary 3 (half-dimensional bi-monochromatic complex).** Suppose that \(c\) has no monochromatic full antipodal geodesic. By the one-missing-dimension extension theorem of Article XIV, \(K\) contains only endpoint pairs of rank at most \(n-2\). By the two-color near-spanning closure theorem of the preceding Subsection, \(I\) contains no pair of rank \(n-2\), and it contains no pair of rank one. Theorem 1 therefore bounds every chain in \(I\) to ranks in \(\{2,\dots,n-3\}\), separated by at least two:
\[
\boxed{\dim I\le m-1,\qquad
m=\left\lfloor\frac{n-3}{2}\right\rfloor.}
\tag{5}
\]

**Theorem 4 (half-dimensional reversal-odd sphere map).** Under the same hypothetical absence of a monochromatic full geodesic, there are \(R\)-equivariant maps
\[
\boxed{I\longrightarrow S^{m-1},\qquad
K_0\cup K_1\longrightarrow S^m,\qquad
m=\left\lfloor\frac{n-3}{2}\right\rfloor,}
\tag{6}
\]
with the antipodal action on both spheres. The covering class \(\alpha\in H^1(K/R;\mathbb F_2)\) satisfies
\[
\boxed{\alpha^{m+1}=0.}
\tag{7}
\]

*Proof.* For a vertex \(p=(u,v)\in I\), let \(i(p)\) be the smallest dimension in which \(u_i=v_i\). Such a dimension exists since \(r(p)\le n-3\). Define
\[
\lambda(p)=(-1)^{u_{i(p)}} e_{\,1+\lfloor(r(p)-2)/2\rfloor}
\in\{\pm e_1,\dots,\pm e_m\}.
\tag{8}
\]
By Theorem 1, consecutive ranks in any chain of \(I\) differ by at least two. The integer indices in (8) are therefore distinct on different vertices of any simplex, and their signed crosspolytope vertices span a face of \(\partial\mathcal O_m\cong S^{m-1}\). Under \(R(u,v)=(\bar v,\bar u)\), rank and unused dimensions are preserved, while the common bit at \(i(p)\) is complemented. Hence \(\lambda(Rp)=-\lambda(p)\), giving the first equivariant map.

View \(S^m\) as the suspension of \(S^{m-1}\). The map on \(I\) extends over \(K_0\) into the contractible closed upper hemisphere: \(I\subseteq K_0\) is a subcomplex, so the extension can be constructed inductively over cells. Define the map on \(K_1=RK_0\) by applying \(R\) to the input and the antipodal map to the output. The two definitions agree on \(I\), since \(\lambda\) is equivariant, and together give the second map in (6). Under the no-closure hypothesis, \(R\) acts freely on \(K\) by the fixed-center theorem of the preceding Subsections. The quotient map \(K/R\to\mathbb RP^m\) identifies \(\alpha\) with the pullback of the canonical degree-one class, whose \((m+1)\)-st cup power vanishes. This proves (7). \(\square\)

**Consequences for the Wu--Yang modification.** The punctured reversal carrier of Article XV has double-cover class \(\beta\) with \(\beta^{n-1}\ne0\), whereas the color-sensitive two-color endpoint union under a hypothetical NORI1 counterexample admits the map (6) to \(S^m\), where \(m\) grows at half the ambient dimension. An equivariant map from the punctured carrier into \(K\) would therefore contradict the cup-power obstruction. The present theorem constructs the low-dimensional target and proves its sharp rank combinatorics; it does not construct that transfer. The adjacent-square carrier obstruction already recorded in this Article shows that any such transfer must use nonlocal compatibility rather than individually selecting monochromatic subintervals of every oriented torus cell.

Theorem 4 substantially strengthens the \(S^{n-4}\) target in the preceding Subsection. The stronger result relies on comparison edges in the **intersection of the two color poset complexes**, not merely on the existence of two differently colored geodesics between individual endpoint pairs. This distinction is essential: a chain in \(I\) carries simultaneous monochromatic extension witnesses of both colors, and it is those witnesses that force the two-rank gap.
