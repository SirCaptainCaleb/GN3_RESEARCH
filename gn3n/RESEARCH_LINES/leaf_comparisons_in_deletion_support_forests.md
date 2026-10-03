# Leaf comparisons in deletion-support forests

**Summary:** In a connected deletion-support tree, every leaf comparison forces an edge between the old supports at all but one neighboring-support label, hence at some endpoint; disconnected forests have only an additional change-of-component alternative.

## Statement

Let H have path-cover number greater than two and choose a two-cover of H-y for every vertex y. If the selected support graph is a tree, then for every leaf support P with neighbor Q, all but at most one label y in Q have a selected cover F_y containing a consecutive pair joining P to Q minus y. Thus at least one endpoint of Q forces this adjacency. In a support forest the same bound holds for labels whose selected edges lie in the leaf's tree component; if Q contains a label from another component, there are no exceptions among those internal labels. No balancing assumption is needed.

## Body

## Leaf comparisons in deletion-support forests

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


## Endpoint forcing in a connected support tree

**Corollary 6.** Suppose the selected support graph \(J\) is a connected tree. Let \(P\) be a leaf support with neighbor \(Q\), let \(x\) be the label of the edge \(PQ\), and fix a Hamiltonian order
\[
Q=(q_0,\ldots,q_m).
\]
There is an endpoint \(y\in\{q_0,q_m\}\) such that, with \(B=Q-\{y\}\), the selected deletion cover \(F_y\) has an edge joining \(P\) to \(B\). For such a choice of \(y\), at least one of the following holds:

1. the surviving vertices of \(B\) have an order disagreement with their inherited order in \(Q\);
2. an inherited edge of \(B\) has its endpoints in different paths of \(F_y\);
3. one path of \(F_y\) leaves \(B\) through a nonempty exterior segment and later returns to \(B\);
4. a tight triple reverses the displayed end edge of \(Q\) incident with \(y\);
5. \(H\) has a two-cover;
6. the singleton lift \(F_y\mid\{y\}\) admits a pairwise repartition with strictly smaller quadratic potential;
7. endpoint restoration is quadratic-potential neutral and, after omitting the unique transferred vertex, yields a deletion cover compatible with \(F_y\) on the common domain.

In particular, after choosing the endpoint guaranteed by the support-tree structure, no split of the leaf support \(P\) is needed as a terminal alternative.

**Proof.** By Corollary 4, at most one label of \(Q\) has a selected deletion cover with no edge between \(P\) and the surviving vertices of \(Q\). Since the two endpoints \(q_0,q_m\) are distinct, one endpoint \(y\) has a selected cover \(F_y\) containing such an edge.

Apply [[path_disturbance_endpoint_reversal_descent_or_an_omission_swap]] to the deletion cover
\[
H-x=P\mid Q,
\]
taking the displayed path \(Q\), its endpoint \(y\), the exterior class \(P\), and the comparison cover \(F_y\) of \(H-y\). If the surviving vertices of \(Q-\{y\}\) do not occur in inherited relative order in \(F_y\), outcome 1 holds. Otherwise the cited theorem gives outcomes 2--7 exactly. \(\square\)

**Corollary 7.** Let \(J\) be an arbitrary support forest, let \(P\) be a leaf in a tree component \(T\) with neighbor \(Q\), and let \(q_0,q_m\) be the endpoints of a Hamiltonian order on \(Q\). If the selected edges labeled \(q_0,q_m\) both lie in \(T\), then one of these two endpoints satisfies the conclusion of Corollary 6. Consequently, either some endpoint label leaves \(T\), or the forest case already yields one of the seven alternatives above.

**Proof.** If both endpoint labels lie in \(D_T\), Corollary 5 guarantees that at least one of them has a selected deletion cover containing an edge between \(P\) and the surviving part of \(Q\). The proof of Corollary 6 then applies verbatim. \(\square\)


## Balanced selection converts omission swaps into selected-lift recurrence

**Corollary 8.** Assume in addition that, for every vertex \(v\), the selected deletion cover \(F_v\) minimizes the sum of squares of its two component orders among all two-covers of \(H-v\). In Corollaries 6 and 7, alternative 7 may be replaced by the following stronger alternative:

7. for some vertex \(w\), the selected singleton lift \(F_w\mid\{w\}\) lies in the same pairwise-repartition component as \(F_y\mid\{y\}\) and has quadratic potential at most that of \(F_y\mid\{y\}\); if the potentials are equal, the two selected singleton lifts are joined by a path of at most two neutral pairwise repartitions.

Consequently, in a minimum counterexample with minimum-imbalance selected deletion covers, every leaf-endpoint comparison in Corollary 6 yields an order disagreement, a split inherited edge, a leave-and-return path segment, an endpoint-edge reversal, strict quadratic descent, or neutral recurrence between selected singleton lifts.

**Proof.** The only new point is alternative 7. Corollary 6 obtains it from the neutral omission-swap outcome of [[path_disturbance_endpoint_reversal_descent_or_an_omission_swap]]. Apply [[balanced_omission_swap_gives_descent_or_selected_singleton_recurrence]]. If the selected deletion cover at the new omitted label has smaller quadratic contribution than the omission-swap cover, the resulting selected singleton lift gives strict quadratic descent in the same pairwise-repartition component. If the contributions are equal, the omission-swap lift and the selected singleton lift are adjacent by repartitioning the two non-singleton paths, so the original selected singleton lift and the new selected singleton lift are joined by at most two neutral moves. Since a minimum counterexample has no two-cover, alternative 5 of Corollary 6 is absent. \(\square\)


## Equal-potential recurrence in a connected support tree

**Corollary 9.** Assume the hypotheses of Corollary 8 and suppose that the selected support graph \(J\) is a connected tree with bipartition \(A\dot\cup B\). Then every selected singleton lift has the same quadratic potential
\[
\Phi_0=(|A|-1)^2+(|B|-1)^2+1.
\]
Consequently, if the endpoint comparison of Corollary 6 reaches the neutral omission-swap alternative, it reaches another selected singleton lift on the same \(\Phi\)-level, joined to the original selected singleton lift by at most two neutral pairwise repartitions. In particular, within a connected support tree the omission-swap residue is genuine neutral recurrence, never strict descent between selected singleton lifts.

**Proof.** By [[connected_support_tree_census_bounds_exceptional_leaf_transfer]], every support represented by a vertex of \(A\) has order \(|A|-1\), and every support represented by a vertex of \(B\) has order \(|B|-1\). Every selected edge of \(J\) joins the two bipartition classes, so every selected deletion cover \(F_v\) has component orders
\[
|A|-1,\qquad |B|-1.
\]
After adjoining the omitted singleton \(v\), every selected singleton lift \(F_v\mid\{v\}\) therefore has potential \(\Phi_0\).

Now apply Corollary 8 to a neutral omission swap from \(F_y\mid\{y\}\). It produces a selected singleton lift \(F_w\mid\{w\}\) of potential at most \(\Phi_0\), in the same pairwise-repartition component. The census identity forces its potential to equal \(\Phi_0\). The equality case of [[balanced_omission_swap_gives_descent_or_selected_singleton_recurrence]] then gives a neutral path of at most two pairwise repartitions. \(\square\)


## Size of the exceptional transfer

**Corollary 10.** Suppose \(J\) is a connected support tree. In the exceptional case of Lemma 1, write \(S\subsetneq P\), \(R=P-S\), and \(B=Q-\{y\}\) as there. Then
\[
|S|=|Q|,\qquad |R|=|P|-|Q|.
\]
Consequently the exceptional cover \(F_y\) and the deletion cover
\[
P\mid(B\cup\{x\})
\]
of \(H-y\) have the same component-order multiset. If the selected deletion covers minimize component imbalance, this replacement is also minimum-imbalance and is support-compatible with \(F_x=P\mid Q\) on \(H-\{x,y\}\).

**Proof.** Apply [[exceptional_leaf_transfer_equals_support_order_gap]] to the block form supplied by Lemma 1. \(\square\)

Thus the unique possible non-mixing label in a connected support tree is not accompanied by an arbitrary smaller-support defect: it transfers exactly the support-order gap, and under balanced selection it admits an equally balanced support-compatible switch.

## Positional rigidity of the exceptional label

**Corollary 11.** Assume minimum-imbalance selection and suppose \(J\) is connected. Let \(y\in Q\) be the exceptional label from Theorem 2. Relative to any Hamiltonian order on \(Q\), at least one of the following holds:

1. the equally balanced support-compatible replacement from Corollary 10 has an order disagreement on \(Q-\{y\}\);
2. \(y\) is one of the first two or last two vertices of the displayed order on \(Q\).

If \(y\) is second from the relevant end, there is a tight triple reversing \(x\) and \(y\) across the endpoint vertex between their insertion slots.

**Proof.** This is [[exceptional_leaf_label_is_end_local_or_order_disagreeing]]. \(\square\)

Hence an exceptional non-mixing label cannot lie deep in the neighboring path without already producing an order disagreement. In the order-compatible case it is confined to an end-two window, with the non-extreme position carrying a displayed reversal.


## Exceptional endpoint closure

**Corollary 12.** Assume minimum-imbalance selection and suppose the selected support graph \(J\) is connected. Let \(F_x=P\mid Q\) correspond to a leaf edge, and let \(y\in Q\) be the exceptional label from Theorem 2. Relative to any Hamiltonian order on \(Q\), at least one of the following holds:

1. the equally balanced support-compatible replacement at \(y\) has an order disagreement on \(Q-\{y\}\);
2. there is a tight triple reversing \(x\) and \(y\) across an endpoint vertex of \(Q\);
3. the selected singleton lifts \(F_x\mid\{x\}\) and \(F_y\mid\{y\}\) lie in the same quadratic-potential level and are joined by at most two neutral pairwise repartitions.

**Proof.** Apply [[exceptional_leaf_label_gives_disagreement_reversal_or_neutral_recurrence]]. \(\square\)

Thus the exceptional non-mixing label has no residual positional case: after order disagreement and the displayed reversal are excluded, it is already a bounded neutral recurrence between selected deletion roots.

## Reselecting an exceptional cover changes the forest geometry

The exceptional non-mixing label can be used to change the selected support graph, rather than merely recorded as a local residue.

Suppose \(J\) is connected, \(P\) is a leaf with neighbor \(Q\), \(x\) labels \(PQ\), and \(y\in Q\) is exceptional. By [[exceptional_leaf_reselection_creates_smaller_leaf_or_disconnects]], the equally balanced support-compatible cover
\[
G_y=P\mid\bigl((Q-\{y\})\cup\{x\}\bigr)
\]
may replace the selected cover at \(y\). The second support in this replacement is new. After the replacement, either the selected support graph becomes disconnected, or it remains a connected tree in which
\[
W=(Q-\{y\})\cup\{x\}
\]
is a leaf adjacent to \(P\) and satisfies \(|W|<|P|\).

In the connected outcome, the new leaf has no exceptional neighboring label: every \(z\in P\) has a selected deletion cover containing a consecutive pair joining \(W\) to \(P-\{z\}\). Hence both endpoints of any Hamiltonian order on \(P\) are available for the direct-mixing endpoint comparison. The exceptional branch has therefore been converted into either the disconnected-forest case or a connected leaf comparison with no non-mixing exception.

## Metadata

- ID: leaf_comparisons_in_deletion_support_forests
- Kind: line
- Version: 12
- Math version: 9
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Chunk 1 — HOT, version 12: Leaf comparisons in deletion-support forests
