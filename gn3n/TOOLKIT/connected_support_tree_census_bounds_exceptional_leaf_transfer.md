# Connected support-tree census bounds exceptional leaf transfer

**Summary:** In a connected selected support tree, support orders equal bipartition-class sizes minus one; an exceptional balanced leaf split transfers at most the bipartition-size gap, with unit gap forcing a one-vertex transfer and a single off-path pendant edge.

## Statement

Let J be a connected selected support tree with bipartition A union B. Every support represented in A has order |A|-1 and every support represented in B has order |B|-1. Under minimum-imbalance deletion-cover selection, if a leaf comparison has no consecutive pair between the two old supports, then the transferred block from the leaf support has order at most the support-size gap Delta. The corresponding containment path has exactly that many off-path edges. In particular, Delta=1 forces a one-vertex transfer and exactly one pendant edge off the containment path.

## Body

Let \(H\) be a finite boundary \(3\)-tournament with \(\operatorname{pc}(H)>2\). Choose a two-cover \(F_x\) of \(H-x\) for every \(x\in V(H)\), and let \(J\) be the selected support graph. Assume that \(J\) is a connected tree. Write \(A\dot\cup B\) for its bipartition, and write \(S_u\subseteq V(H)\) for the path support represented by \(u\in V(J)\).

Since every deletion label occurs on exactly one selected edge and distinct labels give distinct edges,
\[
|E(J)|=|V(H)|.
\]
Hence
\[
|V(H)|=|A|+|B|-1.
\]

**Lemma 1 (support-tree census).** For every \(u\in A\) and \(v\in B\),
\[
|S_u|=|A|-1,\qquad |S_v|=|B|-1.
\]

**Proof.** Fix \(w\in V(J)\) and root \(J\) at \(w\). For an edge \(e\) labeled \(d\), let its endpoints have depths \(k-1\) and \(k\), with the second endpoint farther from \(w\). The membership rule for deletion-partition trees says that \(d\in S_w\) exactly when the distance from \(w\) to the nearer endpoint of \(e\) is odd. Thus
\[
d\in S_w\quad\Longleftrightarrow\quad k-1\text{ is odd}
\quad\Longleftrightarrow\quad k\text{ is even}.
\]
The edges of the rooted tree are in bijection with the non-root vertices via their farther endpoints. Therefore \(|S_w|\) is the number of positive even-depth vertices. These are precisely the vertices in the bipartition class of \(w\), excluding \(w\) itself. The formulas follow. \(\square\)

Now assume that the selected deletion covers minimize the sum of squares of their two component orders. Let \(P=S_p\) be a leaf support, let \(Q=S_q\) be its neighbor, and let \(x\) label the edge \(pq\). Suppose \(p\in A\), \(q\in B\), and write
\[
\Delta=|P|-|Q|=|A|-|B|.
\]

Let \(y\in Q\), put \(C=Q-\{y\}\), and suppose that the selected cover \(F_y\) has no consecutive pair with one endpoint in \(P\) and the other in \(C\). The leaf-comparison structure gives a support \(S\subsetneq P\) and a nonempty set \(R=P-S\) such that the other path of \(F_y\) has one of the block orders
\[
(R,x,C),\qquad (C,x,R).
\]
Write
\[
p_0=|P|,\quad q_0=|Q|,\quad r=|R|,\quad s=|S|.
\]
Then \(p_0=r+s\), while \(C\cup\{x\}\) has order \(q_0\). The selected cover \(F_y\) has component orders \(q_0+r,s\), whereas
\[
P\mid(C\cup\{x\})
\]
is another two-cover of \(H-y\) with component orders \(p_0,q_0\). Minimum imbalance therefore gives
\[
(q_0+r)^2+s^2\le p_0^2+q_0^2.
\]
Using \(p_0=r+s\), this reduces to
\[
2r(q_0-s)\le0.
\]
Since \(r>0\), one has \(s\ge q_0\), and hence
\[
1\le r=p_0-s\le p_0-q_0=\Delta.
\]

This proves the following.

**Theorem 2 (bounded exceptional transfer).** In a connected selected support tree with minimum-imbalance deletion-cover selection, an exceptional leaf comparison with no consecutive pair between the two old supports can occur only on the larger support-tree bipartition class. If \(P\) is the leaf support and
\[
\Delta=|P|-|Q|>0,
\]
then the comparison transfers a contiguous block \(R\subseteq P\) of order at most \(\Delta\) into the path containing \(x\) and \(Q-\{y\}\).

The containment geometry gives the same bound directly in the support tree. Let \(r_0\in V(J)\) represent the support \(S=P-R\). Since \(J\) is connected, every ground label is an edge label of \(J\). The strict-containment theorem therefore gives
\[
P-S=
\{\text{labels of edges of }J\text{ outside the }p\text{-}r_0\text{ path}\}.
\]
Consequently the number of edges outside that path is exactly \(|R|\), and hence at most \(\Delta\). Every such edge is pendant and is attached at odd distance from \(p\).

**Corollary 3 (unit-gap rigidity).** If \(\Delta=1\), then every exceptional leaf comparison transfers exactly one vertex of \(P\). Moreover the \(p\)-\(r_0\) path has exactly one edge of \(J\) outside it; that edge is pendant and is attached at odd distance from \(p\).

There is also a purely tree-theoretic interpretation of \(\Delta\). Suppose \(|A|>|B|\) and every leaf of \(J\) lies in \(A\). Then every vertex of \(B\) has degree at least two, and
\[
|A|+|B|-1
 =|E(J)|
 =\sum_{v\in B}\deg(v).
\]
Thus
\[
\Delta=|A|-|B|
 =1+\sum_{v\in B}\bigl(\deg(v)-2\bigr).
\]

**Corollary 4 (branch-excess identity).** If all leaves lie in the larger bipartition class \(A\), the support-order gap equals one plus the total degree excess above two on the smaller class:
\[
|S_A|-|S_B|
=
1+\sum_{v\in B}\bigl(\deg(v)-2\bigr).
\]
In particular, gap one is equivalent to every vertex of the smaller class having degree two.

## Metadata

- ID: connected_support_tree_census_bounds_exceptional_leaf_transfer
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
