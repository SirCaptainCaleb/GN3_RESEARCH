# The oriented-interval torus and alternating puncture degrees

Let \(D\) be the cell structure on a circle with vertices \(0,1\) and two edges \(e^+,e^-\) joining them, oriented \(0\to1\) and \(1\to0\), respectively. Let
\[
\mathbb T_n=D^n,\qquad J(e^+)=e^-,\ J(e^-)=e^+,\ J(0)=0,\ J(1)=1
\]
in each factor. The action of \(J\) on the torus is simultaneous reflection and its fixed points are the \(2^n\) product vertices.

To each ordered pair of cube vertices \(u,v\in\{0,1\}^n\) associate the product cell \(C(u,v)\) whose \(i\)-th factor is \(e^+\) for \((u_i,v_i)=(0,1)\), \(e^-\) for \((u_i,v_i)=(1,0)\), and vertex \(u_i\) for \(u_i=v_i\). Thus \(\dim C(u,v)=d(u,v)\). Let \(P_{\rm all}\) be the poset of ordered distinct cube-vertex pairs with
\[
(u,v)\preceq(u',v')
\iff
d(u',v')=d(u',u)+d(u,v)+d(v,v').
\tag{1}
\]

**Theorem 1 (the universal endpoint torus).** The correspondence \((u,v)\mapsto C(u,v)\) identifies \(P_{\rm all}\) with the face poset of the positive-dimensional cells of \(\mathbb T_n\). Endpoint reversal \((u,v)\mapsto(v,u)\) corresponds to \(J\). Hence, for \(n\ge2\),
\[
\boxed{X_n=\Delta P_{\rm all}}
\tag{2}
\]
is the full subcomplex of \(\operatorname{sd}\mathbb T_n\) on barycenters of positive-dimensional cells. It is the complement of the disjoint open barycentric stars of the \(2^n\) product vertices, and has a free \(J\)-action. It is equivariantly homotopy equivalent to an \(n\)-torus with \(2^n\) disjoint open \(n\)-balls removed.

*Proof.* The four local states \(0,1,e^+,e^-\) correspond to the four ordered pairs of bits. The product cell \(C(u,v)\) is a face of \(C(u',v')\) precisely when every direction in which \(u,v\) differ also changes in \(u',v'\), with the same orientation, while the other changing directions of \(u',v'\) are frozen at either endpoint value. These are precisely the conditions for the distance equality (1). Swapping \(u,v\) exchanges each changing arc \(e^+\leftrightarrow e^-\) and fixes the remaining factor vertices. Chains of positive-dimensional cells give all simplices of (2). The omitted open stars are disjoint balls; reflection fixes only their centers, so the action on the complement is free. \(\square\)

**Theorem 2 (homology of the universal endpoint complex).** For \(n\ge2\), the integral homology groups of \(X_n\) are free abelian, with
\[
\boxed{\operatorname{rank}H_k(X_n;\mathbb Z)=
\begin{cases}
\binom nk,&0\le k\le n-2,\\
n+2^n-1,&k=n-1,\\
0,&k\ge n .
\end{cases}}
\tag{3}
\]

*Proof.* Remove \(N=2^n\) disjoint small open \(n\)-balls from the torus and denote the complement by \(M\). It deformation retracts onto \(X_n\). Excision gives \(H_n(\mathbb T_n,M;\mathbb Z)=\mathbb Z^N\), with all other relative homology zero. The fundamental class of the oriented torus maps to a primitive vector \((\pm1,\ldots,\pm1)\in\mathbb Z^N\). The homology sequence of the pair then gives \(H_k(M)\cong H_k(\mathbb T_n)=\mathbb Z^{\binom nk}\) for \(k<n-1\), and a short sequence
\[
0\longrightarrow\mathbb Z^{N-1}\longrightarrow H_{n-1}(M)
\longrightarrow\mathbb Z^n\longrightarrow0.
\]
This splits over \(\mathbb Z\) and yields (3). \(\square\)

Let \(\mathcal B_n\) be the poset of nonempty signed dimension sets, whose order complex is \(\operatorname{sd}\partial\mathcal O_n\cong S^{n-1}\), and define the signed-support map
\[
\rho(u,v)=
\bigl(\{i:(u_i,v_i)=(0,1)\},
\{i:(u_i,v_i)=(1,0)\}\bigr).
\tag{4}
\]
It is \(J\)-equivariant. For each vertex \(z\in\{0,1\}^n\), the barycentric link \(L_z\) of its product zero-cell is an \((n-1)\)-sphere contained in \(X_n\). Given a signed dimension set, choose its specified oriented arcs and fix all other factor states at \(z_i\). This identifies \(L_z\) with \(\Delta\mathcal B_n\) and is inverse to \(\rho|_{L_z}\).

**Theorem 3 (alternating puncture degrees).** Give each \(L_z\) the standard local torus orientation and the target crosspolytope its usual orientation. With the degree at \(z=0\) normalized to one,
\[
\boxed{\deg(\rho|_{L_z})=(-1)^{|z|},\qquad
\sum_{z\in\{0,1\}^n}\deg(\rho|_{L_z})=0.}
\tag{5}
\]

*Proof.* At local vertex \(z_i=0\), the arcs \(e^+,e^-\) point in the positive and negative tangent directions. At \(z_i=1\), their tangent directions are reversed. The map \(\rho\) sends \(e^+\) and \(e^-\) to the positive and negative crosspolytope rays independently of \(z\). Hence changing one bit of \(z\) changes the local mapping degree by a factor of \(-1\). This proves the first identity. The second is \(\sum_z(-1)^{|z|}=(1-1)^n=0\). \(\square\)

**Theorem 4 (unrestricted color-sensitive embedding).** For any binary edge coloring \(c\) and either color \(a\), let \(P_a(c)\) be the ordered-pair poset of monochromatic color-\(a\) geodesics, with comparisons required to have monochromatic endpoint extensions satisfying (1). Then the natural map
\[
\boxed{\Delta P_a(c)\hookrightarrow X_n}
\tag{6}
\]
is an equivariant simplicial embedding. Every simplex has a common monochromatic dimension-simple geodesic witnessing all its ordered endpoint pairs. If the maximum monochromatic color-\(a\) geodesic length is \(L\), its image uses only torus cells of dimension at most \(L\).

*Proof.* Every monochromatic endpoint pair defines a product cell, and every comparison satisfies (1), hence is a product face incidence. Reversing a monochromatic geodesic preserves its color. Repeated application of the distance equality shows that the monochromatic paths witnessing a chain can be concatenated with disjoint sets of traversed dimensions; the resulting geodesic contains all specified endpoint pairs. Since \(\dim C(u,v)=d(u,v)\), the final claim follows. \(\square\)

**Relation to Article XV.** In the angular model \(\mathbb T_n=(\mathbb R/2\mathbb Z)^n\) the involution of this Subsection is \(J(t)=-t\), with fixed points \(t_i\in\{0,1\}\). Translation by \(\tfrac12\mathbf1\) conjugates it to \(R(t)=\mathbf1-t\), whose fixed points \(t_i=\pm\tfrac12\) are removed in Article XV's free reversal carrier. Thus \(X_n\) is an equivariant spine of that punctured affine torus, after translation of its cubical decomposition. Its color-dependent subcomplex (6) makes the original problem intrinsic to this topological space, without losing the dimension-simple geodesic witnesses.

Under a hypothetical failure of NORI1, the known length-\((n-1)\) extension lemma confines the monochromatic subcomplex to torus cells of dimension at most \(n-2\). The ambient complex nevertheless contains the \((n-1)\)-dimensional antipodal link spheres of (5). Producing a color-sensitive equivariant transfer from the ambient carrier to the constrained endpoint complex would contradict the index bound. The alternating sum (5) also explains why an unweighted aggregation of all puncture degrees cannot supply the missing transfer: those degrees already cancel.
