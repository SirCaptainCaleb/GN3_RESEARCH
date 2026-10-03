# Leaf comparisons in deletion-support forests

**Summary:** In a connected deletion-support tree, every leaf comparison forces an edge between the old supports at all but one neighboring-support label, hence at some endpoint; disconnected forests have only an additional change-of-component alternative.

## Statement

Let H have path-cover number greater than two and choose a two-cover of H-y for every vertex y. If the selected support graph is a tree, then for every leaf support P with neighbor Q, all but at most one label y in Q have a selected cover F_y containing a consecutive pair joining P to Q minus y. Thus at least one endpoint of Q forces this adjacency. In a support forest the same bound holds for labels whose selected edges lie in the leaf's tree component; if Q contains a label from another component, there are no exceptions among those internal labels. No balancing assumption is needed.

## Body

Let \(H\) be a finite boundary \(3\)-tournament with \(\operatorname{pc}(H)>2\), and suppose that \(H-y\) has a two-cover for every vertex \(y\). A tight path is an ordered list of distinct vertices whose consecutive triples are hyperedges; one- and two-vertex paths are tight vacuously. A two-cover consists of at most two disjoint tight paths spanning the indicated vertex set.

For each \(y\in V(H)\), choose a two-cover \(F_y\) of \(H-y\). Each \(F_y\) has exactly two paths, both of order at least two. A single path on \(H-y\), together with \(y\), would two-cover \(H\); a singleton component \(z\) of \(F_y\) could instead be joined to \(y\) as the two-vertex path \((y,z)\), again giving a two-cover of \(H\).

The selected support graph \(J\) has the distinct path supports occurring in the \(F_y\) as its vertices. The cover \(F_y\) gives an edge labeled \(y\) between its two supports. Distinct labels give distinct edges, because their endpoint supports have union \(V(H)-\{y\}\). Assume that \(J\) is a forest.

Fix a leaf support \(P\) of \(J\), its neighbor \(Q\), and the label \(x\) of their edge. Thus
\[
V(H)=P\mathbin{\dot\cup}Q\mathbin{\dot\cup}\{x\}.
\]
Write \(T\) for their tree component and \(D_T\) for its edge-label set. For \(y\in Q\), an edge between \(P\) and \(Q-\{y\}\) in \(F_y\) means a consecutive pair in one of its two path orders with one endpoint in each of those sets.

## Comparisons without an edge between the old supports

**Lemma 1.** If \(y\in Q\) and \(F_y\) has no edge between \(P\) and \(Q-\{y\}\), then one path of \(F_y\) has support \(S\subsetneq P\). Writing \(R=P-S\) and \(B=Q-\{y\}\), the other path has one of the orders
\[
(R,x,B),\qquad(B,x,R),
\]
where \(R\) and \(B\) denote the respective nonempty contiguous path segments. In particular, \(B\cup\{x\}\) is Hamiltonian.

**Proof.** Exactly one path of \(F_y\) contains \(x\). The other path avoids \(x\), and the absence of edges between \(P\) and \(B\) forces it to lie wholly in one of those two sets.

If that other path lies in \(B\), the path containing \(x\) contains all of \(P\). Removing \(x\) from this path leaves at most two nonempty contiguous segments, each entirely in \(P\) or entirely in \(B\). Consequently all vertices of \(P\), together with \(x\), form a contiguous tight subpath: either the two segments both lie in \(P\), or the \(P\)-segment is immediately beside \(x\). Hence \(P\cup\{x\}\) is Hamiltonian. Together with the selected path on \(Q\), this two-covers \(H\), a contradiction.

Thus the other path has support \(S\subseteq P\). Equality would make the selected edge labeled \(y\) incident with the leaf support \(P\); its sole incident edge is labeled \(x\ne y\). Therefore \(S\subsetneq P\). Both \(R=P-S\) and \(B\) are nonempty. Removing \(x\) from its path must leave one segment containing all of \(R\) and the other containing all of \(B\). This gives the two displayed orders and the Hamiltonicity assertion. \(\square\)

## The restriction imposed by one tree component

**Theorem 2.** At most one vertex \(y\in Q\cap D_T\) has a selected cover \(F_y\) without an edge between \(P\) and \(Q-\{y\}\). If \(Q-D_T\ne\varnothing\), there is no such vertex.

**Proof.** The support sets at the vertices of \(T\) satisfy
\[
S_u\cap S_v=\varnothing,\qquad S_u\cup S_v=V(H)-\{d\}
\]
on its edge labeled \(d\). Thus the containment theorem and its neighbor-label corollary in [[strict_containment_in_deletion_partition_trees]] apply.

For a label \(y\in Q\cap D_T\) whose cover has no edge between the old supports, Lemma 1 supplies a component support \(S\subsetneq P\). Because the selected edge labeled \(y\) lies in \(T\), \(S\) is a vertex of \(T\). The neighbor-label corollary says that at most one edge of \(T\) with label in \(Q\) can be incident with such a proper subset of \(P\). It also says that the existence of such a subset forces \(Q\subseteq D_T\). Both conclusions follow. \(\square\)

The following description records the full support structure of a possible exception. Let \(p,r\) be the vertices of \(T\) with supports \(P,S\), where \(S\subsetneq P\) is supplied by Lemma 1.

**Proposition 3.** The \(p\)-\(r\) path has odd length. Every edge of \(T\) outside this path is pendant and is attached at odd distance from \(p\). Every ground label outside \(D_T\) belongs to \(P-S\). The exceptional label \(y\) is the label of the final edge of the \(p\)-\(r\) path. Moreover,
\[
P-S=(V(H)-D_T)\ \cup\
\{\text{labels of edges of }T\text{ outside that path}\}.
\]

**Proof.** The containment theorem gives the path shape, the outside-label condition, and the displayed identity. Among edges incident with \(r\), only the final path edge has its label outside \(P\). The selected edge labeled \(y\) is incident with \(r\), and \(y\in Q\) is outside \(P\). It must therefore be that final edge. \(\square\)

## Connected support trees and endpoint comparisons

**Corollary 4.** If \(J\) is a connected tree, then for every leaf support \(P\) and its neighbor \(Q\), at least \(|Q|-1\) labels \(y\in Q\) have a selected cover \(F_y\) containing an edge between \(P\) and \(Q-\{y\}\). For any chosen Hamiltonian order of \(Q\), at least one of its two endpoints has this property.

**Proof.** In the connected case \(D_T=V(H)\), so Theorem 2 leaves at most one exceptional label in \(Q\). The two endpoints of a Hamiltonian order on \(Q\) are distinct because \(|Q|\ge2\); they cannot both be exceptional. \(\square\)

**Corollary 5.** In an arbitrary selected support forest, let \(a,b\) be the endpoints of a Hamiltonian order on \(Q\). At least one of the following holds:
1. \(F_a\) has an edge between \(P\) and \(Q-\{a\}\), or \(F_b\) has an edge between \(P\) and \(Q-\{b\}\);
2. at least one of the selected edges labeled \(a,b\) lies in a different tree component of \(J\).

If \(a,b\in D_T\), alternative 1 always holds. If \(Q-D_T\ne\varnothing\), every label in \(Q\cap D_T\) has a cover with an edge between the old supports.

**Proof.** If both selected edges lie in \(T\), Theorem 2 prevents both distinct labels from being exceptional. Its second assertion gives the last sentence. \(\square\)

All assertions hold for arbitrary choices of the deletion covers. No minimization of their component sizes or quadratic potential is assumed.

## Metadata

- ID: leaf_comparisons_in_deletion_support_forests
- Kind: line
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Chunk 1 — HOT, version 1: (untitled)
