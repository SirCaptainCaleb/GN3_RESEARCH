# Fundamental exchange forests and rank-one dual rigidity

Let \(M\) be a finite matroid on \(E\), and let \(\Gamma(M)\) be its basis-exchange graph. For a basis \(B\), the **fundamental exchange graph** \(F_B\) is the bipartite graph on \(B\sqcup(E\setminus B)\), with edge \(be\) precisely when \(B-b+e\) is a basis. Loops and coloops become isolated vertices; the remaining connected components correspond to the connected matroid components.

Define the canonical basis-incidence embedding
\[
\Phi:\mathcal B(M)\longrightarrow\mathbb R^E,\qquad
\Phi(B)=\sum_{b\in B}{\bf e}_b.
\]
An exchange edge \(B\to B-b+e\) has difference vector \({\bf e}_e-{\bf e}_b\).

**Theorem (exchange-forest rigidity).** The following conditions are equivalent.

(i) For every basis \(B\), the exchange-difference vectors of the edges incident with \(B\) are linearly independent.

(ii) For every basis \(B\), the fundamental exchange graph \(F_B\) is a forest.

(iii) Every connected component of \(M\) is a loop, a coloop, a uniform rank-one matroid \(U_{1,m}\), or its dual \(U_{m-1,m}\).

In particular, the canonical basis-incidence resource matroid has independent stars throughout the basis-exchange graph precisely for direct sums of rank-one or corank-one uniform matroids.

*Proof.* The difference vectors \({\bf e}_e-{\bf e}_b\) at a basis \(B\) are the oriented vertex-edge incidence columns of \(F_B\), viewed in \(\mathbb R^E\). Incidence columns are independent if and only if the corresponding graph has no cycle, so (i) and (ii) are equivalent.

We prove (ii) implies (iii). Suppose an induced path
\[
b_1-e_1-b_2-e_2\tag{1}
\]
occurs in \(F_B\), with \(b_1,b_2\in B\) and \(e_1,e_2\notin B\). Thus
\[
B-b_1+e_1,\quad B-b_2+e_1,\quad B-b_2+e_2
\]
are bases, whereas \(B-b_1+e_2\) is dependent. Put \(A=B\setminus\{b_1,b_2\}\), and contract \(A\). In the rank-two matroid \(M/A\), the pair \(\{b_2,e_2\}\) is dependent, while \(\{b_1,e_2\}\) and \(\{b_2,e_1\}\) are bases. Therefore \(b_2\) and \(e_2\) are nonloops in the same parallel class, and \(\{e_1,e_2\}\) is a basis. Lifting to \(M\) shows
\[
B-\{b_1,b_2\}+\{e_1,e_2\}\ \text{is a basis}.\tag{2}
\]

Pivot from \(B\) to the adjacent basis \(B'=B-b_2+e_1\). The four substitutions
\[
B'-b_1+b_2,\quad B'-e_1+b_2,\quad
B'-e_1+e_2,\quad B'-b_1+e_2
\]
are all bases, by the hypotheses and (2). Hence \(F_{B'}\) contains a four-cycle on bipartition \(\{b_1,e_1\}\sqcup\{b_2,e_2\}\), contradicting (ii). Thus **no** fundamental exchange graph can contain an induced four-vertex path.

We next recall why the connected components of \(F_B\) correspond to those of \(M\). Let \(S_1,\ldots,S_h\) be the vertex sets of the components of \(F_B\), and let \(B_j=B\cap S_j\). Every \(e\in S_j\setminus B_j\) belongs to the closure of \(B_j\), since its fundamental circuit relative to \(B\) is contained in \(S_j\). Therefore \(\operatorname{rk}_M(S_j)=|B_j|\). As \(\sum_j|B_j|=\operatorname{rk}(M)\), the rank-additivity criterion implies \(M=\bigoplus_jM|S_j\). Conversely each matroid direct-sum component induces no fundamental exchanges with other components. Thus a connected, nontrivial component of \(M\) yields a connected \(F_B\).

By (ii), each such graph is a tree, and by the preceding pivot argument it contains no induced four-vertex path. A connected tree with no four-vertex path is a star. Since the star spans every element of its connected matroid component, one side of its bipartition has a single vertex. Thus that component has rank one or corank one. A connected rank-one matroid is \(U_{1,m}\), and a connected corank-one matroid is its dual \(U_{m-1,m}\). Loops and coloops are harmless singleton components. This proves (iii).

Conversely, for \(U_{1,m}\) the graph \(F_B\) is \(K_{1,m-1}\), and for \(U_{m-1,m}\) it is \(K_{m-1,1}\). Direct sums give disjoint unions of these stars and isolated vertices, which are forests. Hence (iii) implies (ii). \(\square\)

**Application to the two canonical root graphs.** The basis graph \(Q_n\) of \(\bigoplus^nU_{1,2}\) has a canonical embedding \(\Phi\) whose incident differences are independent: its resources are the \(n\) parallel classes of coordinate directions. The original basis graph \(J(n,2)\) of \(U_{2,n}\), \(n\ge4\), fails this condition because \(F_B=K_{2,n-2}\) has cycles. Its intrinsic line-graph root \(K_n=\Gamma(U_{1,n})\), however, satisfies the condition, and its exchange-difference vectors represent the graphic matroid \(M(K_n)\). Thus the passage from the boundary model's Johnson basis graph to its complete-graph root is mathematically necessary for this common independent-star resource mechanism.

The theorem is an ordinary-matroid obstruction to using canonical basis-indicator gradients directly in both problems, and provides a structural reason for examining a derived root graph equipped with a graphic or spectral resource matroid.
