# Strict containment in deletion-partition trees forces a unique smaller support

**Summary:** A support in a deletion-partition tree properly contains at most one other support; containment forces a leaf and a precise path-with-pendant-edges structure.

## Statement

In an edge-labeled tree of partitions S_u disjoint-union S_v = V minus the edge label, each S_p properly contains at most one other vertex set S_r. Such containment forces p to be a leaf, the p-r path to have odd length, all off-path edges to be pendant at odd distance from p, and every external label to belong to S_p alone. Exactly one edge incident with r has its label outside S_p.

## Body

Let \(V\) be a finite set and let \(T\) be a finite tree with at least one edge. Give its edges distinct labels from \(V\), and write \(D\subseteq V\) for the set of labels. Associate a set \(S_u\subseteq V\) with each vertex \(u\) of \(T\), subject to
\[
S_u\cap S_v=\varnothing,\qquad S_u\cup S_v=V-\{d\}
\]
whenever \(uv\) is the edge labeled \(d\). No order or Hamiltonicity assumption is made.

**Lemma 1 (membership).** For an edge label \(d\in D\), membership of \(d\) in \(S_w\) holds precisely when the distance from \(w\) to the nearer endpoint of the edge labeled \(d\) is odd. For \(d\in V-D\), the vertices \(w\) with \(d\in S_w\) form one bipartition class of \(T\). Moreover, \(|S_w|\) is constant on each bipartition class.

**Proof.** The two endpoints of the edge labeled \(d\) both omit \(d\). Along every other edge, exactly one endpoint set contains \(d\). The unique paths in the tree therefore give the asserted parity rule. For a label outside \(D\), membership alternates across every edge. Finally, adjacent set sizes sum to \(|V|-1\), so set sizes agree at distance two and consequently throughout either bipartition class. \(\square\)

**Theorem 2 (containment).** Suppose \(p\ne r\) and \(S_r\subsetneq S_p\). Write the \(p\)-\(r\) path as
\[
p=v_0,v_1,\ldots,v_\ell=r.
\]
Then:
1. \(\ell\) is odd.
2. Every edge outside this path is pendant and is attached to a path vertex \(v_j\) with \(j\) odd.
3. Every label in \(V-D\) belongs to \(S_p\) and to no \(S_r\).

Conversely, if \(\ell\) is odd and conditions 2 and 3 hold, then \(S_r\subseteq S_p\). Under these conditions,
\[
S_p-S_r=(V-D)\ \cup\
\{\text{labels of edges outside the }p\text{-}r\text{ path}\}.
\]
In particular, inclusion is strict precisely when this displayed set is nonempty.

**Proof.** If \(p,r\) belonged to the same bipartition class, their sets would have equal size by Lemma 1, contrary to strict inclusion. Thus \(\ell\) is odd.

The label of the path edge \(v_{j-1}v_j\) belongs to both sets when \(j\) is even and to neither when \(j\) is odd. Indeed, its nearer-endpoint distances from \(p,r\) are \(j-1\) and \(\ell-j\), which have the same parity.

Consider a branch off the path at \(v_j\). Its first edge label has nearer-endpoint distances \(j\) from \(p\) and \(\ell-j\) from \(r\). These have opposite parity. For its label not to lie in \(S_r-S_p\), \(j\) must be odd. If the branch has a second edge, its distances are \(j+1\) and \(\ell-j+1\); its label then lies in \(S_r-S_p\), a contradiction. Thus all off-path edges are pendant at odd-indexed vertices.

For each label outside \(D\), membership at \(p,r\) is complementary by Lemma 1. Inclusion forces its presence at \(p\) and absence at \(r\). This proves necessity.

Under the three conditions, every path-edge label has the same membership in both sets, every off-path edge label belongs to \(S_p\) alone, and every label outside \(D\) belongs to \(S_p\) alone. The inclusion and difference formula follow. \(\square\)

**Corollary 3 (uniqueness).** For each vertex \(p\), at most one vertex \(r\ne p\) satisfies \(S_r\subsetneq S_p\). If such a vertex exists, \(p\) is a leaf. Among the edges incident with \(r\), exactly one has its label outside \(S_p\): the final edge of the \(p\)-\(r\) path.

**Proof.** Theorem 2 allows no off-path edge at \(p=v_0\), so \(p\) is a leaf. All off-path vertices are pendant at odd-indexed path vertices and hence lie in the bipartition class of \(p\).

Suppose another vertex \(r'\) has \(S_{r'}\subsetneq S_p\). It belongs to the opposite class, so it lies on the \(p\)-\(r\) path. If \(r'\ne r\), the portion from \(r'\) to \(r\) has positive even length, at least two. It is an off-path branch of length at least two relative to the \(p\)-\(r'\) path, contradicting Theorem 2.

The final path edge has odd index \(\ell\), so its label is absent from \(S_p\). Every other edge at \(r\) is pendant at the odd-indexed vertex \(r\), so its label belongs to \(S_p\). \(\square\)

**Corollary 4 (neighbor labels).** Let \(p\) be a leaf with neighbor \(q\). There is at most one edge whose label belongs to \(S_q\) and that is incident with a vertex \(r\) satisfying \(S_r\subsetneq S_p\). If such an \(r\) exists, then \(S_q\subseteq D\).

**Proof.** The edge \(pq\), with label \(x\), gives \(S_q=V-(S_p\cup\{x\})\). By Corollary 3 there is at most one candidate \(r\), and at most one incident edge label outside \(S_p\). Theorem 2 also puts every label outside \(D\) in \(S_p\), so none belongs to \(S_q\). \(\square\)

## Metadata

- ID: strict_containment_in_deletion_partition_trees
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Toolkit status: Limbo
