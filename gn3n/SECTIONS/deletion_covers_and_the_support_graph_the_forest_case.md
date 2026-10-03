# The forest case

## Body

Assume \(J\) is a forest. Let \(e_x=PQ\) be a leaf edge, with \(P\) the leaf vertex of \(J\). If \(y\in Q\), then \(e_y\) cannot share \(Q\), because every support of \(F_y\) omits \(y\), and it cannot share \(P\), because \(P\) is incident only with \(e_x\). Hence \(F_y\) is support-incompatible with \(F_x\).

Choose an endpoint \(y\) of a Hamiltonian order on \(Q\). Lemma 7 can be sharpened here because \(P\) is a leaf support.

**Proposition 8.** In the forest case, for some selected cover \(H-x=P\mid Q\) with \(P\) a leaf support of the selected support graph, and for either displayed endpoint \(y\) of \(Q\), at least one of the following holds:
1. the selected deletion cover at \(y\) contains an edge joining a surviving vertex of \(P\) to a surviving vertex of \(Q\);
2. some displayed edge of \(P\) has its endpoints in different paths of the selected deletion cover at \(y\).

In the second alternative, the endpoint replacement \((Q-\{y\})\cup\{x\}\) is Hamiltonian. If its order preserves the inherited order of \(Q-\{y\}\), then the insertion of \(x\) is confined to the two slots nearest the deleted endpoint; the non-extreme slot yields an explicit end-edge reversal. If both endpoint comparisons use the extreme slot, the three associated singleton lifts form the equal-potential triangle of [[leaf_endpoint_singleton_triangle01]], carrying an order disagreement between the two endpoint-replacement covers.

**Proof.** See [[leaf_endpoint_singleton_triangle01]]. The extra forest input is decisive: in the no-cut interaction branch of Lemma 7, if \(Q-\{y\}\) rather than \(P\) were split between the two paths of the comparison cover, then the other path would have support exactly \(P\). That would make the selected edge labeled \(y\) incident with the leaf support \(P\), contradicting that \(P\) is incident only with \(e_x\). Hence \(P\) is split, and some consecutive displayed edge of \(P\) crosses the two comparison paths. \(\square\)

Thus the forest case reaches a canonical recurrence residue after a single endpoint comparison: either a comparison edge joins the two old supports, or a displayed old-path edge is split between the two comparison paths.


The balanced selection gives a quantitative refinement. In the split case, let \(S\subset P\) be the comparison path lying wholly inside \(P\), and let \(R=P-S\) be the nonempty part of \(P\) lying on the comparison path containing \(x\) and \(Q-\{y\}\). Comparing the selected deletion cover at \(y\) with the valid cover
\[
P\mid((Q-\{y\})\cup\{x\})
\]
shows, by the quadratic-potential identity, that
\[
|S|\ge |Q|.
\]
Hence \(|P|>|Q|\) whenever the split alternative occurs. In particular, if a leaf support is no larger than its neighbor, the direct-mixing alternative is forced.

Since adjacent support orders sum to \(|V(H)|-1\), support orders alternate between two values on each tree component of \(J\). Therefore, if a tree component has leaves in both bipartition classes, at least one leaf is no larger than its neighbor and forces direct mixing. A forest component with no direct-mixing leaf must have every leaf in the larger support-size bipartition class. See [[leaf_endpoint_singleton_triangle01]].


The connected-tree case admits a stronger conclusion without balanced selection. For every leaf support \(P\) with neighbor \(Q\), all but at most one label \(y\in Q\) have a selected deletion cover containing an edge between \(P\) and \(Q-\{y\}\). In particular, one of the two endpoints of any Hamiltonian order on \(Q\) forces direct mixing.

Choose such an endpoint \(y\). Applying [[path_disturbance_endpoint_reversal_descent_or_an_omission_swap]] with exterior class \(P\) and inherited path \(Q-\{y\}\) eliminates the old leaf-splitting residue. In a minimum counterexample, the endpoint comparison therefore yields an order disagreement, a split inherited edge of \(Q-\{y\}\), a leave-and-return path disturbance through \(P\), an explicit reversal of the end edge at \(y\), strict quadratic-potential descent, or a neutral omission swap.

Minimum-imbalance selection sharpens the last alternative further. By [[balanced_omission_swap_gives_descent_or_selected_singleton_recurrence]], the omission swap continues without increasing \(\Phi\) to the selected singleton lift at the new omitted label. Moreover [[connected_support_tree_census_bounds_exceptional_leaf_transfer]] shows that if \(A\dot\cup B\) is the bipartition of the connected support tree, then every selected deletion cover has component orders \((|A|-1,|B|-1)\). Hence all selected singleton lifts have one common potential
\[
(|A|-1)^2+(|B|-1)^2+1.
\]
Thus the omission-swap residue in the connected-tree case is necessarily equal-\(\Phi\) recurrence between selected singleton lifts, joined by at most two neutral pairwise repartitions; it cannot give strict descent between selected singleton lifts. The only remaining strict-descent branch is the direct lower-\(\Phi\) three-cover supplied by the endpoint comparison itself.

For a disconnected forest, the same endpoint conclusion holds whenever both endpoint labels remain in the leaf's tree component; otherwise at least one endpoint's selected edge leaves that component. The detailed endpoint-forcing and recurrence arguments are in [[leaf_comparisons_in_deletion_support_forests]].

## Metadata

- ID: deletion_covers_and_the_support_graph_the_forest_case
- Kind: section
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Subsection 1 — HOT, version 1: (untitled)
