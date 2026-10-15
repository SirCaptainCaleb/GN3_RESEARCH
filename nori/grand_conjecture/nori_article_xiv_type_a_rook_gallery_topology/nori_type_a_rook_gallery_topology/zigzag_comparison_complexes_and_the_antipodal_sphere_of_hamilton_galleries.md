# Zigzag comparison complexes and the antipodal sphere of Hamilton galleries

# Zigzag comparison complexes and the antipodal sphere of Hamilton galleries

Let \(V\) have \(n\ge3\) elements and let \(W=\{z\in\mathbb R^V:\sum_{v\in V}z_v=0\}\). For a permutation \(\pi=(v_1,\ldots,v_n)\) and \(\sigma\in\{-1,1\}\), define
\[
r_i(\pi,\sigma)=\sigma(-1)^{i-1}(e_{v_i}-e_{v_{i+1}}),\qquad 1\le i<n,
\]
and its **dual zigzag cone**
\[
C_{\pi,\sigma}=\{z\in W:\langle z,r_i(\pi,\sigma)\rangle\ge0
\text{ for every }1\le i<n\}.
\tag{1}
\]
The ordered roots have Gram matrix \(2I+A(P_{n-1})\). Thus each \((\pi,\sigma)\) encodes a Hamilton alternating rook gallery, with \(\sigma=-1\) corresponding to entry-swap of every rook state. The inequalities in (1) orient every edge \(v_iv_{i+1}\) of the Hamilton path from the endpoint with the larger required value of \(z\) toward the smaller one; denote the resulting alternately oriented Hamilton path by \(D_{\pi,\sigma}\). In particular, an arc \(u\to v\) means \(z_u\ge z_v\).

**Theorem 1 (Hamilton gallery nerve).** The spherical sets
\[
S_{\pi,\sigma}=C_{\pi,\sigma}\cap S(W)
\]
form a finite antipodally invariant cover of \(S(W)\cong S^{n-2}\). Their nerve \(\mathcal N_n\), with vertices \((\pi,\sigma)\), has the following combinatorial characterization:
\[
\boxed{\quad
F\in\mathcal N_n
\iff
\bigcup_{(\pi,\sigma)\in F}D_{\pi,\sigma}
\text{ is not strongly connected}.
\quad}
\tag{2}
\]
Every nonempty finite intersection of sets \(S_{\pi,\sigma}\) is contractible. The involution
\[
(\pi,\sigma)\longmapsto(\pi,-\sigma)
\tag{3}
\]
acts freely on \(\mathcal N_n\), and its geometric realization is \(\mathbb Z_2\)-equivariantly homotopy equivalent to \(S^{n-2}\) with its antipodal action.

*Proof.* Every \(z\in W\) admits a permutation satisfying
\[
z_{v_1}\ge z_{v_2}\le z_{v_3}\ge z_{v_4}\le\cdots:
\]
successively choose the largest remaining entry, the smallest remaining entry, and so on. Such a \(z\) lies in \(C_{\pi,+1}\), proving the covering assertion. Equation (1) gives \(C_{\pi,-1}=-C_{\pi,+1}\), hence antipodal invariance.

For a nonempty family \(F\), let \(D_F=\bigcup_{(\pi,\sigma)\in F}D_{\pi,\sigma}\). If \(D_F\) is strongly connected, the inequalities \(z_u\ge z_v\) along every directed path force all entries of any \(z\in\bigcap_F C_{\pi,\sigma}\) to agree. Since \(z\in W\), their common value is zero. Thus the spherical intersection is empty. Conversely, if \(D_F\) has at least two strongly connected components, its condensation is a directed acyclic graph. Assign strictly decreasing real values along a topological ordering of its components, then subtract their weighted mean over \(V\). The resulting nonzero vector lies in \(W\) and satisfies every inequality represented by \(D_F\). Normalizing it gives a point of the spherical intersection. This proves (2).

Each cone \(C_{\pi,\sigma}\) is pointed: if \(z\) and \(-z\) both belong to it, all consecutive entries of \(z\) are equal along the Hamilton path, so \(z=0\). Every intersection of these cones is convex and lies in one pointed cone. A nonempty intersection with \(S(W)\) is therefore contractible: fix a point \(z_0\) in it and contract \(z\) toward \(z_0\) along the normalized straight-line interpolation. The denominator stays positive because a pointed cone contains no pair of opposite nonzero vectors. These spherical polyhedra admit a common triangulation, so the finite good-cover nerve lemma identifies \(|\mathcal N_n|\) with \(S(W)\) up to homotopy. This identification is equivariant by the antipodally paired cones and the equivariant nerve lemma.

Finally \(C_{\pi,+1}\cap C_{\pi,-1}=\{0\}\). Hence no nerve simplex contains both \((\pi,+1)\) and \((\pi,-1)\). Every simplex fixed setwise by (3) would contain such a pair, so the simplicial involution has no fixed simplex. \(\square\)

The characterization (2) realizes the antipodal sphere as a simplicial complex defined entirely in terms of compatible collections of **complete Hamilton paths**. In particular the nonrepetition condition is retained at each vertex of the nerve; compatibility of several vertices is decided by strong connectivity of their combined comparison digraph. The nerve construction is independent of a boundary-tournament coloring. Under the rook entry-swap involution, the directed-arc labels \(\beta\) are preserved, so \((\pi,+1)\) and \((\pi,-1)\) carry the same triple-bit word. Consequently antipodality of this carrier alone imposes no oddness relation on those words; any color-sensitive obstruction must also use directed-arc reversal or additional incidence data.

The use of **dual** cones in Theorem 1 is necessary for its covering assertion. Positive hulls of the alternating root bases do not enjoy the analogous property.

**Proposition 2 (open holes in the positive-root cone family).** For \(n\ge4\), let
\[
P_{\pi,\sigma}=\left\{\sum_{i=1}^{n-1}t_i r_i(\pi,\sigma):t_i\ge0\right\}.
\]
Then \(\bigcup_{\pi,\sigma}P_{\pi,\sigma}\) misses a nonempty open subset of \(W\), and hence misses a nonempty open subset of \(S(W)\).

*Proof.* Given \(z\in W\) and \(\pi=(v_1,\ldots,v_n)\), write \(A_i=\sum_{j=1}^i z_{v_j}\). Since the \(r_i(\pi,\sigma)\) form a basis of \(W\), its expansion coefficients are
\[
t_i=\sigma(-1)^{i-1}A_i.
\tag{4}
\]
Thus membership in \(P_{\pi,\sigma}\) requires its successive partial sums \(A_i\) to alternate weakly in sign.

Choose distinct symbols \(a,b\in V\) and set
\[
z_a=1,\qquad z_b=-\tfrac12,\qquad
z_v=-\frac1{2(n-2)}\quad(v\notin\{a,b\}).
\tag{5}
\]
These entries sum to zero. If \(A_1>0\), then \(v_1=a\), and \(A_2>0\) for every choice of \(v_2\), so the signs cannot alternate. If \(A_1<0\), obtaining \(A_2\ge0\) requires \(v_2=a\). When \(v_1=b\), this gives \(A_2=1/2\), and any third entry leaves \(A_3>0\). When \(v_1\notin\{a,b\}\), this gives \(A_2=1-1/[2(n-2)]\), and again any third entry leaves \(A_3>0\). Because \(n\ge4\), three partial sums are present; neither possible alternating sign pattern occurs. Every exclusion is strict, so the same conclusion holds in an open neighborhood of \(z\). \(\square\)

Theorem 1 supplies an intrinsic antipodal topological carrier for the Hamilton-gallery geometry. Proposition 2 separates this carrier from the positive-root-cone geometry used in chain-level rook-label arguments. Neither result establishes that a given reversal-odd boundary labeling admits a gallery with at most one color switch; that requires a theorem involving the labeling as well as the carrier.
