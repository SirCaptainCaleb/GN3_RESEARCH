# Leaf comparisons in deletion-support forests

## Metadata

- ID: leaf_comparisons_in_deletion_support_forests_subsection_a
- Parent Section: leaf_comparisons_in_deletion_support_forests
- Position: 1
- Row version: 18
- Development version: 18
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

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

**Proof.** By Connected support-tree census bounds exceptional leaf transfer, every support represented by a vertex of \(A\) has order \(|A|-1\), and every support represented by a vertex of \(B\) has order \(|B|-1\). Every selected edge of \(J\) joins the two bipartition classes, so every selected deletion cover \(F_v\) has component orders
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

**Proof.** Apply Exceptional leaf transfer equals the support-order gap to the block form supplied by Lemma 1. \(\square\)

Thus the unique possible non-mixing label in a connected support tree is not accompanied by an arbitrary smaller-support defect: it transfers exactly the support-order gap, and under balanced selection it admits an equally balanced support-compatible switch.

## Positional rigidity of the exceptional label

**Corollary 11.** Assume minimum-imbalance selection and suppose \(J\) is connected. Let \(y\in Q\) be the exceptional label from Theorem 2. Relative to any Hamiltonian order on \(Q\), at least one of the following holds:

1. the equally balanced support-compatible replacement from Corollary 10 has an order disagreement on \(Q-\{y\}\);
2. \(y\) is one of the first two or last two vertices of the displayed order on \(Q\).

If \(y\) is second from the relevant end, there is a tight triple reversing \(x\) and \(y\) across the endpoint vertex between their insertion slots.

**Proof.** This is An exceptional leaf label is end-local or order-disagreeing. \(\square\)

Hence an exceptional non-mixing label cannot lie deep in the neighboring path without already producing an order disagreement. In the order-compatible case it is confined to an end-two window, with the non-extreme position carrying a displayed reversal.


## Exceptional endpoint closure

**Corollary 12.** Assume minimum-imbalance selection and suppose the selected support graph \(J\) is connected. Let \(F_x=P\mid Q\) correspond to a leaf edge, and let \(y\in Q\) be the exceptional label from Theorem 2. Relative to any Hamiltonian order on \(Q\), at least one of the following holds:

1. the equally balanced support-compatible replacement at \(y\) has an order disagreement on \(Q-\{y\}\);
2. there is a tight triple reversing \(x\) and \(y\) across an endpoint vertex of \(Q\);
3. the selected singleton lifts \(F_x\mid\{x\}\) and \(F_y\mid\{y\}\) lie in the same quadratic-potential level and are joined by at most two neutral pairwise repartitions.

**Proof.** Apply An exceptional leaf label gives disagreement, reversal, or neutral selected-lift recurrence. \(\square\)

Thus the exceptional non-mixing label has no residual positional case: after order disagreement and the displayed reversal are excluded, it is already a bounded neutral recurrence between selected deletion roots.

## Reselecting an exceptional cover changes the forest geometry

The exceptional non-mixing label can be used to change the selected support graph, rather than merely recorded as a local residue.

Suppose \(J\) is connected, \(P\) is a leaf with neighbor \(Q\), \(x\) labels \(PQ\), and \(y\in Q\) is exceptional. By Exceptional leaf reselection creates a smaller leaf or disconnects the support forest, the equally balanced support-compatible cover
\[
G_y=P\mid\bigl((Q-\{y\})\cup\{x\}\bigr)
\]
may replace the selected cover at \(y\). The second support in this replacement is new. After the replacement, either the selected support graph becomes disconnected, or it remains a connected tree in which
\[
W=(Q-\{y\})\cup\{x\}
\]
is a leaf adjacent to \(P\) and satisfies \(|W|<|P|\).

In the connected outcome, the new leaf has no exceptional neighboring label: every \(z\in P\) has a selected deletion cover containing a consecutive pair joining \(W\) to \(P-\{z\}\). Hence both endpoints of any Hamiltonian order on \(P\) are available for the direct-mixing endpoint comparison. The exceptional branch has therefore been converted into either the disconnected-forest case or a connected leaf comparison with no non-mixing exception.

## Route results consolidated from the Toolkit

### Connected support-tree census bounds exceptional leaf transfer

**Statement.** Let J be a connected selected support tree with bipartition A union B. Every support represented in A has order |A|-1 and every support represented in B has order |B|-1. Under minimum-imbalance deletion-cover selection, if a leaf comparison has no consecutive pair between the two old supports, then the transferred block from the leaf support has order at most the support-size gap Delta. The corresponding containment path has exactly that many off-path edges. In particular, Delta=1 forces a one-vertex transfer and exactly one pendant edge off the containment path.

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

### Exceptional leaf transfer equals the support-order gap

**Statement.** Let J be a connected selected support tree. Let P be a leaf support with neighbor Q, let x label PQ, and let y in Q. Suppose the selected cover of H-y has one component S properly contained in P and its other component has block order (R,x,Q-{y}) or (Q-{y},x,R), where R=P-S. Then |S|=|Q| and |R|=|P|-|Q|. In particular Q-{y} union {x} is Hamiltonian and P | ((Q-{y}) union {x}) is a deletion cover of H-y with exactly the same component-order multiset as the selected exceptional cover.

Let \(J\) be a connected selected support tree, with bipartition \(A\dot\cup B\). For each support-vertex \(u\in V(J)\), write \(S_u\) for its represented support. Every edge of \(J\) has a distinct deletion label, and connectedness gives \(|E(J)|=|V(H)|\), hence \(|V(J)|=|V(H)|+1\).

Root \(J\) at a support-vertex \(w\). For an edge labeled \(d\), the usual membership alternation across deletion-partition edges shows that \(d\in S_w\) exactly when the farther endpoint of that edge has positive even depth from \(w\). Edges are in bijection with non-root vertices, so \(|S_w|\) equals the number of vertices in the bipartition class of \(w\) other than \(w\) itself. Consequently every support represented in \(A\) has order \(|A|-1\), and every support represented in \(B\) has order \(|B|-1\).

Now let \(P=S_p\) be a leaf support with neighbor \(Q=S_q\), and let \(x\) label \(pq\). Fix \(y\in Q\), put \(C=Q-\{y\}\), and suppose the selected deletion cover \(F_y\) has one component with support \(S=S_r\subsetneq P\), while its other component has one of the block orders
\[
(R,x,C),\qquad(C,x,R),
\]
where \(R=P-S\neq\varnothing\).

Since \(S_r\subsetneq S_p\), the deletion-partition containment parity forces the \(p\)-\(r\) path in \(J\) to have odd length. Hence \(r\) lies in the bipartition class opposite \(p\), which is also the class containing the neighbor \(q\). The census above therefore gives
\[
|S|=|Q|.
\]
Thus
\[
|R|=|P|-|S|=|P|-|Q|.
\]
Moreover \(C\cup\{x\}\) is a contiguous subpath of the second component of \(F_y\), so it is Hamiltonian. Therefore
\[
P\mid(C\cup\{x\})
\]
is another deletion cover of \(H-y\). The selected exceptional cover has component orders
\[
|S|,\quad |R|+1+|C|
 =|Q|,\quad |P|,
\]
while the displayed replacement has component orders \(|P|,|Q|\). Hence the two covers have exactly the same component-order multiset and the same quadratic contribution.

In particular, if the selected covers are chosen to minimize component imbalance, the replacement is also minimum-imbalance. On the common domain \(H-\{x,y\}\), its support partition is \(P\mid C\), the same support partition inherited from \(F_x=P\mid Q\). Thus every exceptional leaf comparison in a connected support tree admits an equally balanced support-compatible replacement at the same omitted label. \(\square\)

### An exceptional leaf label is end-local or order-disagreeing

**Statement.** Let H have path-cover number greater than two, let F_x=P|Q be a selected deletion cover whose support P is a leaf of a connected selected support tree, and let y in Q be exceptional in the sense that F_y has no edge between P and Q-{y}. Assume minimum-imbalance selection. Then there is an equally balanced deletion cover G_y=P|((Q-{y}) union {x}) support-compatible with F_x. For any Hamiltonian order Q, either the order induced by G_y on Q-{y} disagrees with the inherited order from Q, or y occupies one of the first two or last two positions of Q. If y occupies the second position from the relevant end, a tight triple reverses x and y across the endpoint vertex between their insertion slots.

Let \(H\) be a finite boundary \(3\)-tournament with \(\operatorname{pc}(H)>2\). Let \(F_x=P\mid Q\) be a selected deletion cover whose support \(P\) is a leaf of a connected selected support tree, and let \(y\in Q\) be an exceptional label: the selected cover \(F_y\) has no consecutive pair joining \(P\) to \(Q-\{y\}\). Assume the selected covers minimize component imbalance.

By Exceptional leaf transfer equals the support-order gap, there is an equally balanced deletion cover
\[
G_y=P\mid W,
\]
where \(W=(Q-\{y\})\cup\{x\}\) is Hamiltonian. Moreover the Hamiltonian order on \(W\) inherited from the exceptional comparison has one of the forms
\[
(x,B),\qquad(B,x),
\]
for some order \(B\) of \(Q-\{y\}\). Thus \(x\) occupies an extreme insertion slot relative to \(B\).

Fix the displayed Hamiltonian order of \(Q\), and compare its inherited order on \(Q-\{y\}\) with \(B\). If these orders disagree, the first conclusion holds. Assume therefore that they agree. Then \(F_x\) and \(G_y\), restricted to \(H-\{x,y\}\), have the same two support sets \(P\) and \(Q-\{y\}\) with the same relative orders.

Both omitted labels are therefore inserted into the same common ordered support \(B\): the cover \(F_x\) inserts \(y\) to recover \(Q\), while \(G_y\) inserts \(x\) to recover \(W\). Their insertion slots must be equal or adjacent. Indeed, if at least one whole slot separated them, inserting both \(x\) and \(y\) into \(B\) at their respective positions would create a tight path: every consecutive triple would be inherited from \(F_x\), from \(G_y\), or from the common order \(B\), and no new consecutive triple would contain both inserted labels. Together with the path on \(P\), this would two-cover \(H\), a contradiction.

Since the insertion slot of \(x\) is extreme, the slot of \(y\) is either the same extreme slot or the adjacent slot. Hence \(y\) occupies the first or second position of the displayed order on \(Q\), or symmetrically the last or penultimate position.

In the adjacent-slot case, write the common order locally as \(z,R\) at the relevant end. Up to reversal of the display, the two paths have local forms
\[
(x,z,R),\qquad(z,y,R).
\]
Every consecutive triple in \(x,z,y,R\) is known tight except possibly \((x,z,y)\). If that triple were tight, this path together with \(P\) would two-cover \(H\). Therefore \((x,z,y)\) is non-tight, and boundary reversal gives
\[
(y,z,x)
\]
tight. Thus the adjacent-slot alternative supplies an explicit reversal triple. \(\square\)

### An exceptional leaf label gives disagreement, reversal, or neutral selected-lift recurrence

**Statement.** Let H have path-cover number greater than two, let F_x=P|Q be a selected minimum-imbalance deletion cover with P a leaf of a connected selected support tree, and let y in Q be the exceptional label whose selected cover has no consecutive pair joining P to Q-{y}. Fix a Hamiltonian order on Q. Then at least one of the following holds: (i) the equally balanced support-compatible deletion cover at y has an order disagreement on Q-{y}; (ii) there is a tight triple reversing x and y across an endpoint-neighbor of Q; (iii) the selected singleton lifts F_x|{x} and F_y|{y} lie in the same pairwise-repartition component and are joined by a path of at most two neutral pairwise repartitions.

Let H have path-cover number greater than two. Choose, for every deleted label, a two-cover of minimum component imbalance, and suppose the selected support graph is a connected tree. Let
\[
F_x=P\mid Q
\]
be a selected deletion cover with P a leaf support, and let y\in Q be the unique possible exceptional label whose selected deletion cover F_y contains no consecutive pair joining P to Q-\{y\}. Fix a Hamiltonian order on Q.

By An exceptional leaf label is end-local or order-disagreeing, there is an equally balanced deletion cover
\[
G_y=P\mid W,\qquad W=(Q-\{y\})\cup\{x\},
\]
support-compatible with F_x on the common domain. Relative to the inherited order on Q-\{y\}, either G_y already has an order disagreement, or y lies in one of the two end positions of Q. In the second position from an end, the same theorem gives a tight triple reversing x and y across the intervening endpoint vertex.

It remains to consider the order-compatible case in which y occupies an extreme position of Q. Write the common ordered support as B=Q-\{y\}. The path of F_x on Q inserts y into an extreme slot of B. The path W in G_y inserts x into an extreme slot of the same ordered support. The insertion-slot argument used in An exceptional leaf label is end-local or order-disagreeing shows that the slots are equal or adjacent. Since y is itself extreme, the adjacent case is precisely the already-listed second-position case. Hence in the remaining case x and y occupy the same extreme insertion slot.

Now compare the singleton lifts. Repartitioning the pair
\[
Q\mid\{x\}
\]
inside F_x|\{x\} as
\[
W\mid\{y\}
\]
gives G_y|\{y\} in one pairwise repartition. The affected component orders are unchanged, so this move is neutral for the quadratic potential.

By Exceptional leaf transfer equals the support-order gap, G_y and the selected exceptional cover F_y have the same component-order multiset. Therefore repartitioning the two non-singleton paths of G_y|\{y\} into the two non-singleton paths of F_y|\{y\} is a second neutral pairwise repartition. Thus
\[
F_x\mid\{x\}\longleftrightarrow G_y\mid\{y\}\longleftrightarrow F_y\mid\{y\}
\]
is a neutral path of length at most two.

Hence every exceptional leaf label produces an order disagreement, an explicit reversal, or neutral recurrence between the two selected singleton lifts. \(\square\)

### Exceptional leaf reselection creates a smaller leaf or disconnects the support forest

**Statement.** Let J be a connected selected support tree arising from minimum-imbalance deletion covers. Let P be a leaf with neighbor Q, let x label PQ, and let y in Q be exceptional, so the selected cover at y has no consecutive pair joining P to Q-{y}. Replace that selected cover by the equally balanced cover P|((Q-{y}) union {x}). The new support W=(Q-{y}) union {x} was not previously represented in J. The new selected support graph is either disconnected, or is a connected tree in which W is a leaf adjacent to P with |W|<|P|. In the connected outcome, no label of P is exceptional relative to W|P.

Let \(H\) be a finite boundary \(3\)-tournament with \(\operatorname{pc}(H)>2\). Choose a minimum-imbalance deletion cover \(F_v\) of \(H-v\) for every vertex \(v\), and suppose the selected support graph \(J\) is a connected tree. Let \(P=S_p\) be a leaf support, let \(Q=S_q\) be its neighbor, and let \(x\) label the edge \(pq\).

Suppose \(y\in Q\) is exceptional: the selected cover \(F_y\) has no consecutive pair joining \(P\) to \(Q-\{y\}\). By Exceptional leaf transfer equals the support-order gap, there are nonempty sets
\[
S\subsetneq P,\qquad R=P-S,\qquad B=Q-\{y\},
\]
such that \(F_y\) has component supports \(S\) and \(R\cup\{x\}\cup B\), while
\[
G_y=P\mid W,\qquad W=B\cup\{x\},
\]
is another minimum-imbalance deletion cover of \(H-y\). Moreover
\[
|S|=|Q|,\qquad |R|=|P|-|Q|>0,\qquad |W|=|Q|.
\]
In particular, \(|P|>|Q|\).

Write \(\mathcal A\mathbin{\dot\cup}\mathcal B\) for the bipartition of \(J\), with \(p\in\mathcal A\) and \(q\in\mathcal B\). By Connected support-tree census bounds exceptional leaf transfer,
\[
|P|=|\mathcal A|-1,\qquad |Q|=|\mathcal B|-1,
\]
so \(|\mathcal A|>|\mathcal B|\).

We first show that \(W\) is not already a support represented in \(J\). Suppose \(W=S_u\) for some \(u\in V(J)\). Since \(x\in W\), the vertex \(u\) is neither \(p\) nor \(q\). Because \(p\) is a leaf and \(x\) labels \(pq\), the path from \(u\) to the edge \(pq\) reaches \(q\) first. The membership rule in [[strict_containment_in_deletion_partition_trees]] therefore gives
\[
x\in S_u
\quad\Longleftrightarrow\quad
\operatorname{dist}_J(u,q)\text{ is odd}.
\]
Hence \(u\in\mathcal A\). The support-tree census then gives
\[
|W|=|S_u|=|\mathcal A|-1=|P|,
\]
contrary to \(|W|=|Q|<|P|\). Thus \(W\) is a new support.

Now replace only the selected cover \(F_y\) by \(G_y\), and call the new selected support graph \(J'\). The strict-containment structure says that the support \(S\) is represented by a vertex \(r\), that the \(p\)-\(r\) path has odd length, and that the edge labeled \(y\) is the final edge of this path. Consequently removing the old edge labeled \(y\) separates the old tree into an \(S\)-side and a \(P\)-side, with \(P\) on the latter. The replacement inserts the new edge \(PW\). Since \(W\) is new, this edge lies wholly on the \(P\)-side and cannot reconnect the \(S\)-side.

If \(S\) had degree one in \(J\), then after removal of the old \(y\)-edge it is no longer represented by any selected cover. The remaining old edges form one tree, and adjoining the new leaf \(W\) at \(P\) gives a connected tree \(J'\). If \(S\) had degree at least two, its side retains at least one selected edge, so \(J'\) is a forest with two edge-containing components.

In the connected case, \(W\) is a leaf of \(J'\) with neighbor \(P\), and
\[
|W|=|Q|<|P|.
\]
All selected covers in the new selection still minimize component imbalance. The exceptional-transfer bound in Connected support-tree census bounds exceptional leaf transfer permits a non-mixing leaf comparison only when the leaf support is larger than its neighbor. Therefore no label \(z\in P\) is exceptional relative to the new leaf edge \(WP\): for every \(z\in P\), the selected cover of \(H-z\) contains a consecutive pair joining \(W\) to \(P-\{z\}\).

Thus reselecting an exceptional leaf cover has only two outcomes: it disconnects the selected support forest, or it replaces the old larger leaf by a new smaller leaf for which every neighboring-support label mixes the two old supports. \(\square\)

### Leaf endpoint comparison forces direct mixing or splits the old support

**Statement.** At a leaf selected support P in a support forest, endpoint deletion comparison either produces a direct edge between the old supports or splits a displayed edge of P. Under minimum-imbalance deletion-cover selection, the isolated P-piece in the split case has order at least |Q|, so splitting requires |P|>|Q|.

# Leaf endpoint comparison forces direct mixing or splits the old support

Let H be a minimum counterexample to pc(H) <= 2. Choose one deletion cover F_v for every v in V(H), and let J be the selected support graph. Suppose J is a forest and e_x=PQ is a leaf edge, with P the leaf support. Let y be an endpoint of a displayed Hamilton order on Q, and put B=Q-{y}.

Then at least one of the following holds.

1. The selected deletion cover F_y contains a path edge joining a surviving vertex of P to a surviving vertex of Q.
2. Some displayed edge of P has its endpoints in different paths of F_y.

In alternative 2, F_y has exactly two path edges joining distinct classes of P | B | {x}; both are incident with x. The path containing x consists of x, all of B, and one nonempty part of P, while the other path contains the remaining nonempty part of P. In particular B union {x} is Hamiltonian.

If this Hamilton path preserves the inherited order of B, then x lies in one of the first two insertion positions when y is the initial endpoint of Q, and in one of the last two insertion positions when y is the terminal endpoint. The non-extreme insertion forces a tight triple reversing a displayed end edge. If both endpoint comparisons use the extreme insertion, the three deletion covers at x and at the two endpoints of Q have a common fixed support P; their singleton lifts form an equal-quadratic-potential triangle, and the two endpoint-replacement orders disagree on their common non-P support.

## Proof

Because P is a leaf support of J, the selected cover F_y shares neither P nor Q with F_x: it cannot share Q because every support of F_y omits y, and it cannot share P because P is incident only with e_x. Hence F_y is support-incompatible with F_x on H-{x,y}.

Consider the three classes P, B, {x}. The cover F_y has at least two path edges joining distinct classes. If it had at most one, deleting that edge from its two paths would leave at most three path blocks. The resulting support partition would be one of (P union B)|{x}, (P union {x})|B, or P|(B union {x}). The first gives a two-cover of H after adjoining the two-vertex path (x,y); the second makes P union {x} Hamiltonian and gives a two-cover with Q; the third is support-compatible with F_x. All are impossible.

Assume alternative 1 fails. Then every interclass edge is incident with x. Since x lies on one path of F_y, at most two path edges are incident with x. Therefore there are exactly two interclass edges, both incident with x.

Cut these two edges. Besides the singleton block {x}, there are three maximal blocks contained in P or B, so exactly one of P,B is split into two blocks. If B were split, the two interclass edges would join x to the two B-blocks: joining x to the unique P-block would make P union {x} Hamiltonian. Thus one path of F_y would have support B union {x}, and the other path would have support exactly P. This would make P a support of F_y, contradicting that P is the leaf support incident only with e_x.

Hence P is split. The same contracted two-path argument shows that x joins the unique B-block to one P-block, while the other P-block is the second path. Thus the vertices of P lie in both paths of F_y. Since the displayed order on P is a path, some consecutive displayed pair has its endpoints in different paths of F_y. This proves alternative 2. The path segment B together with x is Hamiltonian, giving the additional assertion.

For the insertion refinement, write Q=(q_0,...,q_m). Suppose first y=q_0 and a Hamilton order on B union {x} preserves the order q_1,...,q_m. Since Q union {x} is non-Hamiltonian, x can occur only before q_1 or between q_1 and q_2; any later insertion permits q_0 to be prepended. In the second case, (q_0,q_1,x) must be non-tight, so (x,q_1,q_0) is tight and reverses the displayed initial edge of Q. The terminal-end statement is symmetric: a non-extreme insertion gives (q_m,q_{m-1},x) tight.

If both endpoint replacements use the extreme positions, their orders are

(x,q_1,...,q_m),
(q_0,...,q_{m-1},x).

Together with Q they give deletion covers at q_0, q_m, and x sharing P. Let X=Q union {x}. Their singleton lifts are P|(X-{d})|{d} for d in {x,q_0,q_m}; any two differ by repartitioning X and leaving P fixed. Hence they form a triangle in the pairwise-repartition graph and have equal quadratic potential. After deleting q_0 and q_m, the two endpoint-replacement paths induce opposite positions of x on the common support {x,q_1,...,q_{m-1}}, so they have an order disagreement. ∎

## Balanced-selection corollary

Suppose, in addition, that for every deletion label the selected two-cover minimizes the sum of squares of its two component orders among all two-covers of that deletion. In alternative 2 above, write the two pieces of \(P\) as \(R,S\), where the path containing \(x\) has support
\[
B\cup\{x\}\cup R
\]
and the other path has support \(S\). Put
\[
p=|P|,\qquad q=|Q|,\qquad r=|R|,\qquad s=|S|.
\]
Then \(p=r+s\), while \(|B\cup\{x\}|=q\). The selected deletion cover at \(y\) therefore has component orders
\[
q+r,\qquad s.
\]
But
\[
P\mid(B\cup\{x\})
\]
is another two-cover of \(H-y\), with component orders \(p,q\). Minimality of the selected cover gives
\[
(q+r)^2+s^2\le p^2+q^2.
\]
Since \(p=r+s\), the difference between the left and right sides is
\[
2r(q-s).
\]
As \(r>0\), it follows that
\[
s\ge q.
\]
In particular \(p>q\). Consequently, if the leaf support satisfies \(|P|\le |Q|\), alternative 1 is forced: the endpoint deletion cover must contain an edge joining the two old supports.

Along every path in a connected component of the support forest, support orders alternate between two values, because adjacent support orders sum to \(|V(H)|-1\). Hence if a tree component has leaves in both bipartition classes, one of its leaves lies in the smaller (or equal) class and therefore forces direct support mixing. Thus a forest component with no such direct-mixing leaf must have all of its leaves in the larger support-size bipartition class.

### A leaf support reduces endpoint comparison to path disturbance, reversal, descent, or an omission swap

**Statement.** Let H be a minimum counterexample and choose deletion covers whose selected support graph is a forest. If H-x=P|Q corresponds to a leaf edge with P the leaf support and y is a displayed endpoint of Q, then the selected deletion cover at y yields an order disagreement, a displayed inherited edge of P or Q-y split between its two paths, a leave-and-return path segment through exterior vertices, a tight triple reversing the displayed endpoint edge of Q, a two-cover of H, a strict quadratic-potential decrease from the singleton lift at y, or a Phi-neutral omission swap to another deletion cover compatible with the selected cover at y.

Let H be a minimum counterexample. Choose one deletion cover F_v for each vertex v, and let J be the selected support graph. Assume J is a forest. Let
H-x=P|Q
be a selected deletion cover whose support P is a leaf of J, and let y be an endpoint of the displayed path Q. Put B=Q-{y}, with the inherited order.

By the leaf-support endpoint comparison, the selected deletion cover F_y has one of the following properties:

(i) an edge of F_y joins a surviving vertex of P to a surviving vertex of B; or

(ii) a displayed edge of P has its endpoints in different paths of F_y.

In case (ii) the asserted split-edge outcome already holds.

Assume case (i). Regard H-x=P|Q as the base deletion cover, regard y as the displayed endpoint of Q, and compare it with F_y. Apply the direct-mixed-edge disturbance theorem to the displayed path Q, its endpoint y, and the comparison cover F_y.

If the surviving vertices of B do not occur in inherited relative order inside the paths of F_y, there is an order disagreement. Otherwise that theorem gives at least one of the following:

1. an inherited edge of B has its endpoints in different paths of F_y;
2. one path of F_y leaves B through a nonempty exterior segment and later returns to B;
3. a tight triple reverses the displayed endpoint edge of Q incident with y;
4. H has a two-cover;
5. the singleton lift F_y|{y} admits a strict quadratic-potential decrease by one pairwise repartition;
6. the endpoint restoration is Phi-neutral and, after omitting the unique transferred vertex, gives another deletion cover compatible with F_y on their common domain.

Combining case (ii) with these alternatives proves the statement.

Thus, for a leaf support in the selected support forest, an ordinary edge joining the two old supports is not an additional terminal configuration. It immediately resolves into one of the listed order-theoretic, path-theoretic, or potential-theoretic alternatives.

## Toolkit Limbo placement audit: support-tree obstruction

### Branching in a reduced support tree prevents rounding by two selected paths

**Statement.** Let H be a finite boundary 3-tournament with pc(H)>2, with one two-cover selected for every deletion. Suppose its selected support graph J is a connected tree, with support S_u at vertex u. For distinct u,v, S_u union S_v=V(H) if and only if the u-v tree path P has even length and every edge outside P is pendant and attached at odd distance from u along P; then S_u intersect S_v is exactly the set of labels outside P. In particular, suppose J has bipartition X,Y with |X|>|Y|, deg(x)<=2 for x in X and deg(y)>=2 for y in Y. Let K be the tree on Y obtained by deleting X-leaves and suppressing remaining degree-two X-vertices. The fractional cover number restricted to {S_u} is two, but a pair of selected supports has spanning union if and only if K is a path. If K branches, no selection and trimming of two displayed paths can give a spanning two-cover. This is a conditional obstruction within the selected family, not a counterexample to general rounding.


Let H, J, and S_u be as in the connected selected-support tree theorem: pc(H)>2, one deletion cover is selected at every ground label, and J is a tree with those labels as its edges. Let u,v be distinct vertices of J, and let P be their unique tree path.

**Lemma.** S_u union S_v=V(H) if and only if P has even length and every edge outside P is a pendant edge attached to an odd-distance vertex of P, with distance measured from u. In that case S_u intersect S_v is exactly the set of labels of the edges outside P.

**Proof.** Membership of an edge label e in S_w is determined by the parity of the distance from w to the nearer endpoint of e: membership holds precisely when that distance is odd. This is the rooted tree formula of deletion_supports_form_a_forest_or_a_spanning_odd_cycle.

If P has odd length, its first edge has distance zero from u and even distance from v. Its label is therefore absent from both supports, so their union is not V(H).

Suppose P has even length. The symmetric-difference formula in deletion_supports_form_a_forest_or_a_spanning_odd_cycle gives S_u symmetric-difference S_v=labels(P). Thus every edge label on P belongs to exactly one support, while every label off P belongs either to both or to neither.

An off-path branch begins at a path vertex p at distance j from u. The first edge of that branch belongs to both supports exactly when j is odd. If the branch has a second edge, that edge has nearer-endpoint distance j+1, so when the first edge is included, the second is omitted by both supports. Therefore all off-path labels can be covered only when every off-path edge is pendant and attached at an odd-distance path vertex. Conversely, under that condition every off-path edge label belongs to both supports. This proves both claims.

## Consequence for the mass-two tree shapes

Suppose J has bipartition X,Y with |X|>|Y|, every X-vertex of degree at most two, and every Y-vertex of degree at least two. Form a tree K on Y by deleting the X-leaves and suppressing each remaining degree-two X-vertex. The edges of K correspond to two-edge paths of J; this construction is well-defined because every nonleaf X-vertex has degree two. Here |Y|>=3, as each selected deletion component has order at least two.

**Corollary.** Two selected supports have union V(H) if and only if K is a path.

For necessity, the lemma forces every vertex off the path P in J to be a leaf in the same bipartition class as its endpoints. The endpoints cannot lie in Y, since every Y-vertex has degree at least two and the lemma allows no extra edge at either endpoint. Hence the endpoints lie in X, and every Y-vertex lies on P. All the edges of K are therefore on one path, so K is a path.

For sufficiency, if K is a path, each of its two end Y-vertices has at least one adjacent X-leaf in J: its degree in J is at least two, and only one incident edge leads into K. Choose one such leaf at each end. Their path in J has even length, contains every degree-two X-vertex and every Y-vertex, and all its omitted edges are X-leaf edges attached to Y-vertices. These are exactly the odd-distance vertices along the path. The lemma applies.

For these two supports, their intersection is the set of the other leaf-edge labels. The displayed Hamilton orders on that intersection need not agree, and its vertices need not occupy removable end segments. A spanning union therefore still does not establish a spanning two-cover.

In particular, if K branches, NO pair of selected supports has a spanning union, even though the selected-support family has fractional cover number two, as proved below. Any integral two-cover in H would have to use at least one Hamiltonian support outside this selected family. This is a conditional structural obstruction to rounding within the selected family, not a constructed counterexample to the grand conjecture or to general fractional rounding.


## Fractional mass two within the same family

For completeness the fractional claim used in this fence is proved here, so no unpublished premise is needed. Put a=|X|, b=|Y|, r=a-b>0 and s_u=1_{S_u}. There are n=a+b-1 ground labels. Rooting the tree at x in X, the support formula of deletion_supports_form_a_forest_or_a_spanning_odd_cycle identifies S_x with the parent edges of X-{x}. Sum the identities s_u+s_v=1_V-1_d over these edges and move s_x to the left. This gives
sum_X s_x + sum_Y(deg(y)-1)s_y=(a-1)1_V.
Rooting in Y gives
sum_Y s_y + sum_X(deg(x)-1)s_x=(b-1)1_V.
Subtracting,
sum_X(2-deg(x))s_x + sum_Y(deg(y)-2)s_y=r1_V.
All coefficients are nonnegative under the stated degree conditions and their sum is 2r. Division by r gives a fractional cover of mass two using only the selected supports, with each ground vertex covered once.

This is also optimal within that family. Since |Y|>=3 and X has maximum degree two, some X-vertex x has degree two. Give weight one to each of its two incident ground-edge labels and zero to all other labels. S_x contains neither. For every other support vertex u, the nearer-endpoint distances from u to these two edges differ by one, so S_u contains exactly one of their labels by the membership parity formula. Thus no selected support has weight exceeding one, while the ground set has weight two. This supplies a restricted dual lower bound of two.

Scope: this restricted dual weighting is not asserted feasible on all tight paths. Neither existence of a counterexample H with this tree shape nor failure of general fractional rounding is asserted. The conclusion identifies what an integral construction would have to add: when K branches, at least one resulting path must have support outside the selected family, and trimming any two selected paths is insufficient. When K is a path the spanning-union criterion removes this set-theoretic obstruction, but the overlapping Hamilton orders still require a genuine gluing argument.


## Paired endpoint reduction after one balanced reselection

**Theorem 13.** Assume minimum-imbalance deletion-cover selection and suppose the selected support graph \(J\) is a connected tree. After changing at most one selected deletion cover to an equally balanced alternative, one of the following holds:

1. the selected support graph is disconnected;
2. the selected support graph is a connected tree containing a leaf support \(L\) with neighbor \(M\) such that, for every \(z\in M\), the selected deletion cover \(F_z\) contains an ordinary edge joining \(L\) to \(M-\{z\}\).

In the second alternative, both endpoints of every Hamiltonian order on \(M\) force direct mixing between the two old supports.

**Proof.** Choose a leaf support \(P\) of \(J\), let \(Q\) be its neighbor, and let \(x\) label \(PQ\). If there is no exceptional label \(y\in Q\), then by definition every \(F_y\), \(y\in Q\), contains an edge between \(P\) and \(Q-\{y\}\). Take \(L=P\) and \(M=Q\).

Otherwise let \(y\in Q\) be the unique exceptional label. By Corollary 10, the deletion cover
\[
G_y=P\mid\bigl((Q-\{y\})\cup\{x\}\bigr)
\]
has the same component-order multiset as the selected minimum-imbalance cover \(F_y\), so replacing \(F_y\) by \(G_y\) preserves minimum-imbalance selection. By Exceptional leaf reselection creates a smaller leaf or disconnects the support forest, this replacement either disconnects the selected support graph or leaves it connected with
\[
W=(Q-\{y\})\cup\{x\}
\]
as a leaf adjacent to \(P\), and no label \(z\in P\) is exceptional relative to the leaf edge \(W\mid P\). In the connected outcome, therefore, every selected cover \(F_z\), \(z\in P\), contains an edge joining \(W\) to \(P-\{z\}\). Taking \(L=W\) and \(M=P\) proves the second alternative. \(\square\)

The connected-tree route may therefore be started from a leaf edge with direct mixing available at both ends of the neighboring displayed path. The earlier one-endpoint conclusion is needed only before this balanced reselection.

**Corollary 14.** Let \(H\) be a minimum counterexample and assume minimum-imbalance selection. After changing at most one selected deletion cover as in Theorem 13, either the selected support forest is disconnected, or there is a leaf edge
\[
H-x=L\mid M,\qquad M=(m_0,\ldots,m_s),
\]
for which the endpoint comparison can be run independently at both \(m_0\) and \(m_s\). For each endpoint \(z\in\{m_0,m_s\}\), at least one of the following occurs:

1. an order disagreement on \(M-\{z\}\);
2. an inherited edge of \(M-\{z\}\) is split between the two paths of \(F_z\);
3. one path of \(F_z\) leaves \(M-\{z\}\) through a nonempty exterior segment and later returns;
4. a tight triple reverses the displayed end edge of \(M\) incident with \(z\);
5. the singleton lift \(F_z\mid\{z\}\) admits a strict quadratic-potential decrease;
6. a selected singleton lift at another omitted label is reached on the same quadratic-potential level by at most two neutral pairwise repartitions.

**Proof.** In the connected outcome of Theorem 13, both endpoint covers contain an edge joining the leaf support \(L\) to the surviving part of \(M\). Apply Corollary 8 separately to \(m_0\) and \(m_s\). The two-cover alternative is absent because \(H\) is a counterexample. Corollary 9 converts the neutral omission-swap outcome into equal-potential recurrence between selected singleton lifts. \(\square\)

Thus the unresolved connected-tree case carries two endpoint disturbances simultaneously. A completion may use their interaction; it no longer needs to spend an endpoint merely to guarantee the existence of direct mixing.


## Two endpoint exceptions cannot coexist quietly

The component-escape alternative in a disconnected support forest is not needed when both displayed endpoints are compared simultaneously.

**Lemma 13 (two-endpoint non-mixing collapse).** Let
[
F_x=Pmid Q,
qquad
Q=(q_0,ldots,q_m),
qquad mge1,
]
be a selected deletion cover in a minimum counterexample, with (P) a leaf support of its support-forest component and (Q) its neighbor.

Suppose that for each endpoint
[
yin{q_0,q_m},
]
the selected deletion cover (F_y) has no ordinary path edge joining (P) to (Q-{y}).

Then at least one of the following holds:

1. (H) has a Hamiltonian support of order two with two-coverable complement;
2. one of the alternative covers constructed below has an order disagreement with (F_x) on the common support (Q-{y});
3. a tight triple reverses two omitted labels across a common vertex, as in the adjacent-slot conclusion of the insertion-slot lemma;
4. the two endpoint alternatives have an order disagreement on their common domain.

In particular, after order disagreement and external reversal are treated as successful disturbances, the two endpoints of (Q) cannot both be non-mixing.

**Proof.** Fix an endpoint (yin{q_0,q_m}). Lemma 1 of this Section applies to the non-mixing cover (F_y). It gives a block decomposition whose mixed component contains (Q-{y}) together with (x) as a contiguous tight subpath. Hence
[
G_y
=
Pmidigl((Q-{y})cup{x}igr)
]
is also a deletion cover of (H-y).

Compare (G_y) with
[
F_x=Pmid Q
]
on (H-{x,y}). They have the same support partition
[
Pmid(Q-{y}).
]
Use the same displayed order on (P) in both covers. If the order induced by (G_y) on (Q-{y}) disagrees with the inherited order from (Q), outcome 2 holds. Otherwise the two covers are compatible.

By the insertion-slot lemma, the omitted labels (x,y) are inserted into equal or adjacent slots of the common order on (Q-{y}). An adjacent pair of slots gives outcome 3. Thus, outside outcome 3, the slots are equal.

Now put
[
a=q_0,qquad b=q_m.
]
For (y=a), the vertex (a) occupies the initial endpoint slot of the inherited order on (Q-a). Hence compatibility forces (x) to occupy that same initial slot in (G_a). Likewise, for (y=b), compatibility forces (x) to occupy the final endpoint slot in (G_b).

If (|Q|=2), then (Q) itself is a two-vertex Hamiltonian support and
[
H-Q=Pmid{x}
]
has path-cover number at most two. This is outcome 1.

Assume therefore (|Q|ge3), and choose any
[
zin Q-{a,b}.
]
Restrict (G_a) and (G_b) to (H-{a,b}). Their support partitions agree:
[
Pmidigl((Q-{a,b})cup{x}igr).
]
But in (G_a), the vertex (x) precedes (z), while in (G_b), the vertex (x) follows (z). Thus the two common-support orders disagree, giving outcome 4. (square)

Therefore a disconnected support forest has no independent “both endpoints escape” residue. For every leaf-neighbor Hamiltonian path, at least one endpoint comparison enters direct mixing, order disagreement, or reversal, unless bounded support has already appeared.
