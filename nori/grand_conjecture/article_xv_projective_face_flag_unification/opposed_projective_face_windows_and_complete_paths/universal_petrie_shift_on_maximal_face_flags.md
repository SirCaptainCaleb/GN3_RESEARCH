# Universal Petrie shift on maximal face flags

# Universal Petrie shift on maximal face flags

A maximal face flag of a simple polytope defines a complete affine-basis walk. Its rank-flip product has a stronger universal property than the individual cube and simplex formulas: **it shifts the canonical walk forward by one edge**. This supplies the common transport identity needed for a cyclic variation or topological proof.

Let \(P\) be a simple convex \(d\)-polytope with flag
\[
\mathcal F:\quad F_0\subset F_1\subset\cdots\subset F_d=P,\qquad \dim F_i=i,
\]
and let \(v_0,\ldots,v_d\) be its canonical basis path. Let \(r_i\) exchange the \(i\)-face in a maximal flag with the other \(i\)-face in its rank-two interval, \(0\le i\le d-1\). Write \(T=r_0r_1\cdots r_{d-1}\), meaning successive application of the indicated flips.

**Theorem 1 (universal one-step flag transport).** The canonical path of \(T\mathcal F\) begins with
\[
\boxed{\quad v_1,v_2,\ldots,v_d.\quad}
\tag{1}
\]
It has one additional last vertex \(v_{d+1}\), uniquely determined by its final face flag. More precisely, after applying \(r_0,\ldots,r_j\) to \(\mathcal F\), the newly selected \(i\)-face for every \(i\le j\) is the unique \(i\)-face \(G_i\) satisfying
\[
v_1,\ldots,v_{i+1}\in G_i,
\quad
\operatorname{aff}G_i=\operatorname{aff}\{v_1,\ldots,v_{i+1}\},
\tag{2}
\]
while the faces of rank above \(j\) remain unchanged.

*Proof.* For \(j=0\), \(r_0\) changes \(F_0=\{v_0\}\) to the other endpoint \(v_1\) of \(F_1\); thus \(G_0=\{v_1\}\). Assume the assertion through rank \(j-1\). Then the intermediate flag contains
\[
G_{j-1}\subset F_j\subset F_{j+1},
\]
with \(v_1,\ldots,v_j\in G_{j-1}\) and \(v_{j+1}\in F_{j+1}\setminus F_j\). At the vertex \(v_j\in G_{j-1}\), the path edge \(v_jv_{j+1}\) lies in \(F_{j+1}\) and leaves its facet \(F_j\). Inside the simple \((j+1)\)-face \(F_{j+1}\), there are precisely two \(j\)-faces containing the \((j-1)\)-face \(G_{j-1}\): one is \(F_j\), and the other \(G_j\) contains the edge \(v_jv_{j+1}\). Thus \(G_j\) contains all the previously selected vertices \(v_1,\ldots,v_j\) and also \(v_{j+1}\). Since these \(j+1\) vertices are affinely independent, they span \(G_j\). Applying \(r_j\) replaces \(F_j\) by \(G_j\), proving the induction.

After all flips, the flag begins \(G_0\subset\cdots\subset G_{d-1}\subset P\). Its canonical path must follow \(v_1\to v_2\to\cdots\to v_d\): at each rank, the next listed vertex is on the unique edge exiting the preceding face. This proves (1). \(\square\)

**Corollary 2 (universal local-word shift).** Let \(k\in\{1,2\}\), let \(c:\mathscr I_k(P)\to\mathbb F_2\) be any coloring, and set \(m=d+1-k\). For the projective-incidence word
\[
\mathsf w_k(\mathcal F)=(w_0,w_1,\ldots,w_{m-1})
\]
one has
\[
\boxed{\quad
\mathsf w_k(T\mathcal F)
=(w_1,w_2,\ldots,w_{m-1},w_{\rm new}).
\quad}
\tag{3}
\]
No symmetry or parity hypothesis on the coloring is required.

*Proof.* The two canonical walks share the \(d\)-edge tail \(v_1,\ldots,v_d\) by Theorem 1; therefore their \(k\)-step observations agree on each of the first \(m-1\) overlapping windows. The last window in \(T\mathcal F\) is new. \(\square\)

**Corollary 3 (cyclic switch representation for all simple polytopes).** Fix a \(T\)-orbit of maximal flags of length \(L\). There is a cyclic binary sequence \(a_0,\ldots,a_{L-1}\) such that the color word of \(T^s\mathcal F\) is the consecutive \(m\)-term window
\[
(a_s,a_{s+1},\ldots,a_{s+m-1})
\tag{4}
\]
with indices modulo \(L\). Define the cyclic comparisons \(d_i=\mathbf1_{\{a_i\ne a_{i+1}\}}\) and \(D=\sum_{i=0}^{L-1}d_i\). Then
\[
\boxed{\quad
\min_{0\le s<L}\operatorname{sw}(\mathsf w_k(T^s\mathcal F))
=\min_s\sum_{j=0}^{m-2}d_{s+j}
\le \left\lfloor\frac{m-1}{L}D\right\rfloor.
\quad}
\tag{5}
\]

*Proof.* Repeated use of (3) constructs the sequence \(a_i\) and proves (4). The flag returns after \(L\) shifts, so the sequence is cyclic. Each comparison \(d_i\) occurs in precisely \(m-1\) of the \(L\) window switch sums, counted with multiplicity. Their average is \((m-1)D/L\); the minimum is at most its floor. \(\square\)

**Theorem 4 (specialization of opposition monodromy).** On the simplex, \(T\) cyclically shifts a Hamilton vertex order and has order \(d+1\) on each flag orbit. Complementation \(J\) of face subsets reverses the vertex order, so \(JTJ=T^{-1}\). On the cube, \(T\) is the one-step geodesic root slide; \(T^d\) is central complementation and \(T^{2d}=1\) on flags. Thus the original boundary periodic word and the NORI1 antiperiodic half-cycle word are instances of (4), with different relations between \(T\) and opposition.

*Proof.* The specializations of the rank-flip formula were established in the preceding Subsection. In the simplex, reversing a vertex permutation conjugates cyclic rotation to its inverse. In the cube, after \(d\) slides every dimension has been flipped once and the dimension order returns; after another \(d\) slides the original root returns. \(\square\)

**Research consequence.** The cyclic-rotation operation previously introduced separately for NORI1 and boundary tournaments is intrinsic to *every* simple-polytope flag geometry. This is stronger than merely arranging two classes in a common Coxeter notation. The remaining one-switch problem is to use antipodal odd projective-incidence color descent and interaction of different \(T\)-orbits to force a low-variation orbit. Equation (5) alone is insufficient: arbitrary cyclic binary sequences can have high variation.
