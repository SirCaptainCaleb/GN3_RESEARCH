# Coxeter flag-parity transport and curvature reconstruction up to one phase

# Coxeter flag parity and curvature reconstruction

This section links the all-rank Coxeter chain homotopies of Article XIV, Subsections 34–35, to the complete color information recoverable from square curvature. The theorem applies to every unrestricted antipodally odd coloring, for all \(n\ge3\).

Let \(c\) be a binary undirected-edge coloring of \(Q_n\) with \(c(\tau e)=1+c(e)\), and let \(\kappa=\delta c\) be its square-curvature cochain. A rooted dimension-simple complete geodesic flag is \(g=(x;d_0,\ldots,d_{n-1})\). Define its **flag parity**
\[
\boxed{p_c(g)=\sum_{e\in P(g)}c(e)\pmod2.}
\tag{1}
\]
The generator \(s_0\) flips the initial root in direction \(d_0\) while fixing the ordered dimensions, and \(s_i\) (\(1\le i<n\)) swaps \(d_{i-1},d_i\) while preserving the root.

**Theorem 1 (curvature transport at every Coxeter generator).** Let \(F_i(g)\) be the square used in exchanging the adjacent dimensions \(d_{i-1},d_i\), located after crossing the preceding \(i-1\) dimensions. Then
\[
\boxed{p_c(gs_i)+p_c(g)=\kappa(F_i(g)),\qquad 1\le i<n.}
\tag{2}
\]
For the root flip, let
\[
S_j(g)=F_{\{d_0,d_j\}}
\left(x\oplus\bigoplus_{r=1}^{j-1}e_{d_r}\right),
\qquad 1\le j<n.
\tag{3}
\]
These \(n-1\) squares form a strip between the two geodesics after their common initial undirected edge. Then
\[
\boxed{p_c(gs_0)+p_c(g)=1+\sum_{j=1}^{n-1}\kappa(S_j(g)).}
\tag{4}
\]

*Proof.* Interchanging adjacent dimensions replaces the two-edge route through a square by its alternative. Therefore the mod-two sum of the two complete geodesic edge chains is the boundary of that square, proving (2) by Stokes. For (4), the geodesics \(P(g)\) and \(P(gs_0)\) share and cancel their first undirected edge. Their suffixes are parallel paths in the two opposite \(d_0\)-faces. The sum of the strip boundaries equals
\[
\partial\Bigl(\sum_{j=1}^{n-1}S_j(g)\Bigr)
=P(g)+P(gs_0)+e_0+\tau e_0,
\]
where \(e_0\) is the shared initial undirected edge. Evaluating \(c\), the last pair contributes one by antipodal oddness, giving (4). \(\square\)

**Theorem 2 (all-flag parity reconstruction up to one global phase).** Suppose two legal colorings \(c,c'\) have the same square-curvature cochain. Then a single bit \(\epsilon\in\mathbb F_2\), independent of root and dimension order, satisfies
\[
\boxed{p_{c'}(g)=p_c(g)+\epsilon
\quad\text{for every full geodesic flag }g.}
\tag{5}
\]
Both values of \(\epsilon\) occur among legal colorings with that same curvature.

*Proof.* By (2) and (4), the difference \(p_{c'}(g)+p_c(g)\) is constant across every type-B Coxeter generator edge. These generators connect all rooted dimension orders, so the difference is constant. To obtain the opposite phase, add the invariant closed one-cochain \(d^{(a)}\) which is one on all edges of any fixed dimension \(a\), and zero on the other dimensions. This addition preserves antipodal oddness and curvature while flipping the parity of every complete geodesic, because every such geodesic uses \(a\) once. \(\square\)

**Corollary 3 (root-slide monodromy).** For the canonical root-slide rotation
\[
T(x;d_0,\ldots,d_{n-1})
=(x\oplus e_{d_0};d_1,\ldots,d_{n-1},d_0),
\tag{6}
\]
the color word transforms as
\((w_1,\ldots,w_n)\mapsto(w_2,\ldots,w_n,1-w_1)\). Consequently
\[
\boxed{p_c(Tg)=p_c(g)+1,\qquad
p_c(\tau g)=p_c(g)+n\pmod2.}
\tag{7}
\]
In particular \(T^n g=\tau g\) accumulates \(n\) parity flips, agreeing with antipodal complementation of all edge colors.

**Corollary 4 (parity-complete, switch-incomplete information).** The square curvature determines the **entire parity profile across all complete geodesics**, modulo one global binary phase. Yet Subsection 31 proves that every one of the \(2^n\) possible color words can appear on an individually prescribed complete geodesic while curvature is held fixed. Therefore curvature recovers global *word parity differences*, not switch counts or switch positions. The latter require finer color-sensitive incidence data.

**Relevance to the Wu–Yang adaptation.** Equations (2)–(4) supply the generator-level color-parity transport law compatible with the full-rank dimension-simple Coxeter chain geometry, without introducing any auxiliary class of graphs. The higher chain homotopies of Subsection 35 handle the uncolored braid and commuting polygons. The remaining proof problem is to retain ordered red/blue run structure under these homotopies and force cancellation of the primary high-rank second-switch obstruction under a hypothetical NORI1 counterexample. Neither theorem here asserts a monochromatic full-geodesic existence conclusion.
