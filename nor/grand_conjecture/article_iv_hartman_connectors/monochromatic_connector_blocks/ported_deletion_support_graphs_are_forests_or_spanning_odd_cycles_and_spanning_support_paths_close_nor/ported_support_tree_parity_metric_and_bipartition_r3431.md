# Tree parity metric for ported-deletion support graphs

## Composition

Let \(A\) be the shore. A **deletion-support graph** has vertex set consisting of support subsets appearing in chosen fully ported two-path deletion covers. The edge \(e_a\) joins the two disjoint supports whose union is \(A\setminus\{a\}\); each deletion label occurs on at most one edge.

**Parity-path identity.** For support vertices \(S,T\) joined by a simple path \(P\) of length \(\ell\), let \(L(P)\) be its edge-label set. Then
\[
S\triangle T=
\begin{cases}
L(P),&\ell\text{ even},\\
A\setminus L(P),&\ell\text{ odd}.
\end{cases}
\]
For a coordinate \(u\), membership flips across every \(e_a\) except \(e_u\), whose endpoints both omit \(u\). The parity of flips along \(P\) is \(\ell-\mathbf{1}_{u\in L(P)}\), giving the identity.

Suppose one component is a tree \(T\) containing every deletion label. For \(v\in V(T)\) and \(a\in A\), let \(d_T(v,e_a)\) be the minimum distance to an endpoint of \(e_a\). Zero membership at the ends of \(e_a\) and the unique tree path give
\[
a\in S(v)\iff d_T(v,e_a)\text{ is odd}.
\]
Rooting the tree at \(v\), edges at odd distance correspond bijectively to vertices at even positive depth. Consequently, if \(X,Y\) are the bipartition classes, \(|S(v)|=|X|-1\) for \(v\in X\), and \(|S(v)|=|Y|-1\) for \(v\in Y\). When both paths in every deletion cover have at least two vertices, \(|X|,|Y|\geq3\).

In a spanning support tree, \(S(v)\) and \(S(w)\) are complementary precisely when the joining path has even length and uses *all* deletion labels. This happens exactly when the tree itself is an even-length path and \(v,w\) are its endpoints. The corresponding two fully ported zero paths glue to a spanning monochromatic connector. A branching tree supplies no complementary support pair.

**Sharpness in actual ported deletion witnesses.** Consider the eight-vertex tree
\[
v_0v_1,\ v_1v_2,\ v_2v_3,\ v_1v_4,\ v_4v_5,\ v_5v_6,\ v_6v_7.
\]
Label its seven edges bijectively by \(A=\{1,\dots,7\}\), and define \(S(v)=\{a:d_T(v,e_a)\text{ odd}\}\). Its bipartition classes both have four vertices; hence all eight distinct supports have cardinality three. Each edge \(e_a=vw\) gives a partition \(S(v)\sqcup S(w)=A\setminus\{a\}\). Choose any transitive tournament on \(A\). The increasing orders on these three-element supports are genuine fully ported zero paths; hence all seven deletion covers are realized. Yet the branching support graph contains no complementary support pair. The ambient transitive tournament itself closes, showing that a branch in an arbitrarily selected deletion family cannot certify a genuine obstruction.

The remaining closure task must exploit the **orders** carried by support witnesses, permitting port-preserving witness replacement or absorption across the branching exchange configuration.

## Development

Strengthens the forest-versus-odd-cycle support theorem. The support family has a parity-distance representation in every support component. When one tree component contains all deletion labels, its support cardinalities are precisely the two bipartition-class sizes minus one. This identifies branching trees as the sole connected forest obstruction to complementary support gluing, and supplies a metric invariant for comparing actual ported deletion witnesses. Full NOR closure still requires a port-preserving exchange or an alternative connector.
