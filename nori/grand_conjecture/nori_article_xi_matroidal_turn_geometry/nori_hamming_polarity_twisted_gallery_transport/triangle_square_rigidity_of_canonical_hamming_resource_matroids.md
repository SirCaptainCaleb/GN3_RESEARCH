# Triangle-square rigidity of canonical Hamming resource matroids

# Triangle–square rigidity of canonical Hamming resource matroids

Let \(G=\square_{i=1}^k K_{E_i}\) be a finite Cartesian product of nontrivial complete graphs, with \(|E_i|=m_i\ge2\). Write \(A_i\subseteq E(G)\) for the graph edges changing coordinate \(i\), and \(d=\sum_i(m_i-1)\). A **Cartesian square** is a four-cycle obtained by changing two different coordinates, and a **fiber triangle** is a three-cycle obtained by changing one coordinate. A matroid \(N\) on the graph-edge ground set \(E(G)\) is said to have **local resource compatibility** if:

(S) every graph vertex star \(\delta_G(x)\) is independent in \(N\);

(T) every fiber triangle is dependent in \(N\);

(P) the two opposite graph edges of each Cartesian square are parallel elements of \(N\).

These axioms refer only to the graph's intrinsic local geometry and the circuit/independence structure of \(N\). No representation, spectral projection, orientation, or edge coloring is assumed.

For the product \(G\), define \(R(G)\) to be the matroid on \(E(G)\) obtained by giving each edge \(e\in A_i\), joining symbols \(a,b\in E_i\), the graphic resource label \((i,\{a,b\})\). On the set of distinct labels the matroid is
\[
R_0(G)=\bigoplus_{i=1}^k M(K_{E_i});
\tag{1}
\]
the matroid \(R(G)\) is its parallel extension in which different graph edges with a common label are parallel.

**Theorem 1 (local resource rigidity).** A matroid \(N\) on \(E(G)\) satisfies (S), (T), and (P) if and only if
\[
\boxed{N=R(G).}
\tag{2}
\]
In particular, the three local matroid axioms determine the complete independence system, and
\[
\boxed{\operatorname{rk}N=\sum_{i=1}^k(m_i-1)=\deg G.}
\tag{3}
\]
Every graph cycle is then \(N\)-dependent, and every resource-independent graph walk has distinct vertices.

*Proof.* Fix a vertex \(o=(o_1,\ldots,o_k)\) of \(G\). For each factor \(i\), let \(B_i\) be the \(m_i-1\) edges incident with \(o\) that change coordinate \(i\), and put \(B=\bigcup_i B_i=\delta_G(o)\). By (S), \(B\) is independent.

First consider an arbitrary edge of type \(i\), changing the two symbols \(a,b\in E_i\), in a fiber whose other coordinates need not agree with those of \(o\). Change those other coordinates one at a time until the fiber coincides with the fiber of \(o\). At every change the edge is opposite a corresponding edge in a Cartesian square. By (P), its resource element is parallel to the corresponding element in the next fiber. Hence it is parallel to the edge \(e^i_{ab}\) of type \(i\) in the reference fiber through \(o\).

If \(a=o_i\) or \(b=o_i\), the element \(e^i_{ab}\) belongs to \(B_i\). Otherwise the edges \(e^i_{o_i a}, e^i_{o_i b},e^i_{ab}\) form a fiber triangle. By (T) its three elements are dependent, and by (S) each pair is independent since any pair shares a graph vertex. Thus the triangle is a three-element circuit, giving
\[
e^i_{ab}\in\operatorname{cl}_N
\{e^i_{o_i a},e^i_{o_i b}\}
\subseteq\operatorname{cl}_N(B_i).
\tag{4}
\]
Together with opposite-edge parallel transport this proves
\[
A_i\subseteq\operatorname{cl}_N(B_i)
\qquad\text{for every }i.
\tag{5}
\]
The \(B_i\)'s are disjoint subsets of the independent set \(B\), so \(r_N(A_i)=|B_i|=m_i-1\), while \(B\) spans all of \(E(G)\). Therefore
\[
r_N(E(G))=|B|=\sum_i r_N(A_i).
\tag{6}
\]
Rank additivity across the partition \(E(G)=\bigsqcup_i A_i\) implies
\[
N=\bigoplus_i N|A_i.
\tag{7}
\]

It remains to determine the single-factor restriction. By (P), all copies of a given edge \(\{a,b\}\) in distinct fibers are parallel, and every such parallel class contains the reference-fiber edge \(e^i_{ab}\). Consider the induced restriction \(N_i\) to the reference-fiber edges of \(K_{E_i}\). Every vertex star in \(K_{E_i}\) is independent by (S), and every triangle is a three-element circuit by (S) and (T).

We claim that \(N_i=M(K_{E_i})\). Every graph spanning tree \(T\) of \(K_{E_i}\) can be turned into the star at \(o_i\) through successive **triangle pivots** that preserve matroid span. Root \(T\) at \(o_i\). Whenever a vertex \(v\) has depth at least two, let \(u\) be its parent and \(p\) the parent of \(u\). Replace the tree edge \(uv\) by the complete-graph edge \(pv\). The result is another spanning tree with smaller total depth, and the triangle \(pu,uv,pv\) is a three-element circuit. Because \(pu\) remains in the tree, the outgoing and incoming edges lie in each other's closure together with \(pu\), so the two spanning-tree edge sets have the same closure and rank. Repeating the operation eventually yields the star at \(o_i\), which is independent of rank \(m_i-1\). Thus **every spanning tree has rank \(m_i-1\) and is independent**, and every graph forest, being extendible to a spanning tree, is independent in \(N_i\).

Conversely, take any graph cycle \(C\) of \(K_{E_i}\), with vertex set \(S\), and choose \(z\in S\). Its star edges \(\{zv:v\in S\setminus\{z\}\}\) form an independent family of \(|S|-1\) elements. Every edge \(uv\) of the cycle not incident with \(z\) belongs to the closure of \(zu,zv\) by the triangular circuit; edges incident with \(z\) already belong to the star. Hence the \(|S|\) edges of \(C\) have rank at most \(|S|-1\), so \(C\) is dependent. Consequently the independent sets of \(N_i\) are precisely the graph forests, proving \(N_i=M(K_{E_i})\).

Equations (7) and the parallel-class description now give \(N=R(G)\). Conversely, in \(R(G)\) every graph vertex star uses distinct edges of the factor-graphic root stars, and their union is independent in the direct sum; any triangle in a factor is a graphic cycle; and opposite Cartesian-square edges share the same factor and unordered pair of symbols, hence are parallel. Thus \(R(G)\) satisfies (S), (T), and (P), proving (2).

Finally every closed graph walk projects in every coordinate to a closed walk of the corresponding complete graph. If the original walk is nonempty, some coordinate projection is nontrivial; its multiset of graphic resource labels contains a repeated edge or a cycle, and so is dependent. The original edge set is dependent in \(R(G)\). In particular a resource-independent walk cannot repeat a vertex. \(\square\)

**Corollary 2 (intrinsic matroidal unification).** For
\[
M_{\rm cub}=\bigoplus_{i=1}^nU_{1,2},
\qquad M_{\rm bd}=U_{2,n},
\tag{8}
\]
the connected-component rank-one reduction \(M^\flat\) and its basis graph \(G=\Gamma(M^\flat)\) recover the two canonical root graphs \(Q_n\) and \(K_n\). Theorem 1 uniquely determines their resource matroids from vertex-star independence, triangle dependence, and Cartesian-square parallelism:
\[
R(Q_n)=\text{coordinate-direction partition matroid on cube edges},
\quad
R(K_n)=M(K_n).
\tag{9}
\]
Thus both resource-independence notions have a common choice-free characterization using ordinary matroid circuits and the local graph structure. The turn bits and global involution are additional data that remain necessary for the colored path assertion.

**Proposition 3 (logical sharpness of the three axioms).** Each hypothesis (S), (T), and (P) is needed for uniqueness.

- Without (S), take \(G=K_3\), and put the rank-one uniform matroid \(U_{1,3}\) on its graph edges. Its triangle is dependent, and (P) is vacuous, while the canonical resource is \(M(K_3)=U_{2,3}\).
- Without (T), take \(G=K_3\) and the free rank-three matroid on its graph edges. Every star is independent and (P) is vacuous, but the canonical triangle circuit disappears.
- Without (P), take \(G=Q_2=C_4\) and \(N=U_{2,4}\) on its four graph edges. Every two-edge star is independent, and (T) is vacuous; the four-cycle is dependent, but opposite edges are independent rather than parallel. The canonical resource instead is \(U_{1,2}\oplus U_{1,2}\).

These examples also show that star independence and graph-cycle dependence alone do not determine the cube resource matroid: the commuting-square condition (P) carries essential information.

**Interpretation.** The rank-one reduction of the source matroid supplies the common Hamming root geometry. Theorem 1 recovers the full resource matroid solely from its local triangle/square behavior, with no spectral or vector choice. Independent-star terminal arguments therefore have a canonical combinatorial foundation in both source models. The missing step toward the full NORI1 statement is a global antipodal rank-saturation argument for arbitrary edge colorings; Theorem 1 isolates its resource geometry from the unconstrained coloring problem.
