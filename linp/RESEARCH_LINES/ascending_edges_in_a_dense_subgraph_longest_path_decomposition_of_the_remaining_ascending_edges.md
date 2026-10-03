# Longest-path decomposition of the remaining ascending edges

## Body

Choose for every vertex \(v\) a maximum path
\[
P_v=(g_1,\ldots,g_p),\qquad p=\phi(v),
\]
with last vertex \(v\). Assign each ascending edge
\[
e=\{x,u,v\}
\]
to a terminal of smaller vertex rank, breaking ties arbitrarily. Thus, if \(e\) is assigned to \(v\),
\[
\phi(u)\ge\phi(v)=p. \tag{5}
\]

Except when \(e\) is the last edge of \(P_v\), every maximum \(p\)-edge path ending at \(v\) contains \(x\) or \(u\). Indeed, otherwise \(e\) can be appended after \(P_v\), contradicting maximality. Thus every assigned edge falls into one of the following three classes:
\[
\begin{array}{ll}
D:& x,u\in V(P_v),\\[2mm]
X:& x\in V(P_v),\ u\notin V(P_v),\\[2mm]
U:& u\in V(P_v),\ x\notin V(P_v).
\end{array}
\tag{6}
\]

The class \(D\) is controlled by double intersections with the chosen paths. The other two classes have more useful structure.

## Lemma 7

Fix \(\varepsilon>0\). Among the edges in class \(X\) assigned to a fixed vertex \(v\), only \(O_\varepsilon(1)\) can satisfy
\[
\phi(e)\le (1-\varepsilon)\phi(v). \tag{7}
\]

#### Proof
For an edge in class \(X\), the intersection of \(e\) with \(P_v\) is exactly \(\{x,v\}\). Order such intersections along \(P_v\). If two unique entrances occur far enough apart, the two corresponding edges can replace an interval of \(P_v\), producing a path that ends at one entrance and is too long for its vertex rank. Quantitatively, if the later edge has edge-rank deficit
\[
D=\phi(v)-\phi(e),
\]
then successive admissible entrance positions must be separated by at least \(D+1\), up to an absolute boundary term. Hence only
\[
O\!\left(\frac{\phi(v)}{D+1}+1\right)
\]
such edges can occur. Under (7), \(D\ge\varepsilon\phi(v)\), which gives \(O_\varepsilon(1)\). ∎

Thus a leading-order class \(X\) family must have edge rank \((1-o(1))\phi(v)\).

The class \(U\) creates many alternative last vertices by rotation.

## Lemma 8

Let \(U(v)\) be the class \(U\) edges assigned to \(v\). There is a set \(W(v)\) of vertices with
\[
\phi(w)\ge\phi(v)\qquad (w\in W(v))
\]
such that
\[
|U(v)|\le 2|W(v)|+1. \tag{8}
\]

#### Proof
Let \(e=\{x,u,v\}\in U(v)\), and let \(j(e)\) be the first index for which \(u\in g_{j(e)}\). Since \(x\notin V(P_v)\), the edge \(e\) can replace the suffix immediately after \(g_{j(e)}\), producing a \(\phi(v)\)-edge path with new last vertex
\[
w(e)=g_{j(e)+1}\cap g_{j(e)+2}.
\]
Hence \(\phi(w(e))\ge\phi(v)\).

Different indices \(j\) give different vertices \(w(e)\). By linearity, distinct edges assigned to \(v\) have distinct opposite terminals \(u\). Along a linear path, at most two vertices have their first occurrence in a given \(g_j\) for \(j\ge2\), and at most three do so in \(g_1\). Therefore at most two edges of \(U(v)\) give the same \(j\), apart from one boundary excess. This yields (8). ∎

Lemmas 7 and 8 reduce the unresolved ascending mass to two phenomena:

1. many edges of edge rank \(p-o(p)\) whose unique entrance lies on a maximum \(p\)-edge path;
2. many alternative last vertices of rank at least \(p\), produced from edges whose opposite terminal lies on that path.

## Metadata

- ID: ascending_edges_in_a_dense_subgraph_longest_path_decomposition_of_the_remaining_ascending_edges
- Kind: line
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Chunk 1 — crystallized, version 1: (untitled)
- Chunk 2 — crystallized, version 1: Lemma 7
- Chunk 3 — HOT, version 1: Lemma 8
