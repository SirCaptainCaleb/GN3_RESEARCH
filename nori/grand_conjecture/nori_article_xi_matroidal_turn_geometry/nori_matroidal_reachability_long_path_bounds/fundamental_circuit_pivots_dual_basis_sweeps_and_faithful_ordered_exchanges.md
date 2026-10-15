# Fundamental-circuit pivots, dual-basis sweeps, and faithful ordered exchanges

# Fundamental-circuit pivots, dual-basis sweeps, and faithful ordered exchanges

Let \(M\) be a finite loopless matroid on \(E\), and let \(\Gamma(M)\) denote its basis-exchange graph. For an oriented edge \(B\to B'=B-a+e\), let \(C_M(e,B)\) be the fundamental circuit of \(e\) with respect to \(B\). The circuit contains \(a,e\), since replacing \(a\) by \(e\) gives a basis.

**Theorem 1 (canonical pivot of a small fundamental circuit).** Suppose every circuit of \(M\) has cardinality at most three. Each oriented basis exchange \(B\to B-a+e\) admits a unique intrinsic label of one of the following types:
\[
\begin{array}{ll}
\text{parallel exchange:}& C_M(e,B)=\{a,e\};\\
\text{triangular exchange:}& C_M(e,B)=\{a,b,e\},\quad
b\in B\cap B'.
\end{array}
\tag{1}
\]
In the triangular case the ordered triple \((a,b,e)\) is determined by the oriented exchange and the matroid. Reversing the exchange changes it to \((e,b,a)\). The labels are preserved by every matroid isomorphism.

*Proof.* The element \(e\) is outside \(B\), and a fundamental circuit contains \(e\) together with at least one element of \(B\). Because \(B-a+e\) is independent, \(a\) is in this circuit. The size bound gives the two displayed possibilities; in the size-three case the third element \(b\) belongs to \(B\setminus\{a\}=B\cap B'\). Fundamental circuits are unique. For the reverse exchange \(B'\to B\), the fundamental circuit of \(a\) with respect to \(B'\) is the same circuit: its removal of \(e\) restores the basis, and its removal of \(b\) also yields a basis by the fundamental-circuit exchange criterion. The description is matroid-theoretic and therefore commutes with isomorphisms. \(\square\)

The theorem identifies the local middle element of a boundary triple as a *fundamental-circuit pivot*. It also identifies a cubical coordinate exchange with a two-element fundamental circuit. No auxiliary ordering of the retained basis elements is used in either case.

**Theorem 2 (faithfulness rigidity for uniform sliding windows).** Fix \(1\le r<n\). Map an injective ordered \((r+1)\)-tuple
\[
(a,x_1,\ldots,x_{r-1},e)
\]
to the oriented basis exchange
\[
\{a,x_1,\ldots,x_{r-1}\}
\longrightarrow
\{x_1,\ldots,x_{r-1},e\}
\tag{2}
\]
of \(U_{r,n}\). Every oriented edge of \(\Gamma(U_{r,n})=J(n,r)\) has precisely \((r-1)!\) preimages. Hence an oriented exchange determines its ordered sliding window if and only if \(r\le2\).

For \(r=2\), arbitrary reversal-odd boundary 3-tournaments on \([n]\) are in bijection with orientations of \(J(n,2)\): orient the edge
\[
\{a,b\}\longrightarrow\{b,e\}
\]
when \(b(a,b,e)=1\). Every orientation of \(J(n,2)\) arises. For \(r\ge3\), some reversal-odd ordered-\((r+1)\)-window colorings cannot descend to orientations of the basis-exchange graph.

*Proof.* The ordered source and target bases in (2) recover \(a\) as their deleted element, \(e\) as their inserted element, and the unordered set \(X=B\cap B'\) of their \(r-1\) retained elements. The preimages are precisely the permutations of \(X\). This gives the factorial and the characterization \(r\le2\). When \(r=2\), the sole retained element is \(b\), and reversing the graph edge reverses \((a,b,e)\). Thus the reversal-odd identity specifies one orientation of each undirected graph edge with no further compatibility conditions. When \(r\ge3\), choose two different permutations of \(X\) and give their windows different binary colors; assign the complementary colors to their reversed windows, then fill the remaining reversal orbits arbitrarily. The coloring is reversal-odd but assigns different colors to the same directed exchange, so it does not descend. \(\square\)

**Theorem 3 (dual-basis permutation sweeps).** In both canonical models the colored states along a complete path admit distinct intrinsic resource labels forming one basis of the dual matroid.

(i) Let \(M=\bigoplus_{i=1}^kU_{1,2}\). Every dual basis \(D\) has complementary primal basis \(B=E\setminus D\). For each permutation \(d_1,\ldots,d_k\) of \(D\), let \(B_j\) arise from \(B_{j-1}\) by exchanging its element parallel to \(d_j\) for \(d_j\). Then
\[
B=B_0,B_1,\ldots,B_k=D
\tag{3}
\]
is an antipodal geodesic of the \(k\)-cube. Its \(k=r(M^*)\) exchange edges have distinct two-element-circuit labels indexed by \(D\); every antipodal geodesic from \(B\) is obtained from one such permutation.

(ii) Let \(M=U_{2,n}\), \(n\ge3\). Every dual basis \(D\) has complementary primal basis \(\{s,t\}\). For each permutation \(d_1,\ldots,d_{n-2}\) of \(D\), the word
\[
(s,d_1,\ldots,d_{n-2},t)
\tag{4}
\]
defines a path in \(J(n,2)\) through its consecutive unordered pairs. Its \(n-2=r(M^*)\) oriented exchanges are labeled, in order, by the distinct triangular-circuit pivots \(d_1,\ldots,d_{n-2}\). Conversely, the original-element Hamiltonian tight words with endpoints \(s,t\) are precisely (4).

In both instances, the reversal operation on complete paths acts on the corresponding color words by
\[
w\longmapsto\overline{\operatorname{rev}(w)}.
\tag{5}
\]

*Proof.* The complement of a primal basis is a dual basis. In (i), each \(d_j\) belongs to a different parallel pair, so all exchanges are legal and no pair is toggled twice. A path from \(B\) to \(E\setminus B\) has length at least \(k\), and equality forces every pair to be toggled once. In (ii), consecutive unordered pairs of the displayed word intersect in the single middle element; every pair is a basis and every original vertex appears once. The ordered-triple labels are its successive windows, whose middle elements are precisely the members of \(D\). Conversely, a Hamiltonian tight word determines its two endpoints and the order of its interior elements. The reversal of a boundary word reverses and complements each triple label by reversal oddness. For the cube, reverse the geodesic and apply the canonical complementation map to every basis; the antipodal odd edge rule complements the reversed sequence of edge colors. This proves (5). \(\square\)

**Corollary 4 (the common resource parameter).** The natural number of primitive colored states of a complete gallery is
\[
\boxed{r(M^*)=|E(M)|-r(M)}
\tag{6}
\]
in both canonical models: \(k\) for the cube and \(n-2\) for the boundary tournament. The canonical exchange label is an inserted element in (i) and a retained fundamental-circuit pivot in (ii). For uniform rank \(r\ge3\), the underlying oriented basis-exchange graph alone loses \((r-1)!\)-fold ordered-window information.

This identifies a common matroidal resource budget and a choice-free source of its local exchange labels. It leaves two additional ingredients to a path-existence theorem: a compatible global polarity of colored exchange states, and a rank-increasing exchange rule that preserves a coherent path with distinct resources. In the cube the antipode acts on bases; in uniform rank two, reversal acts on directed exchanges. The two actions have different domains, and the colored signed-cover matroid requires the additional gallery information developed elsewhere in Article XI.
