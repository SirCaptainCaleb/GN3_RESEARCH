# Exceptional leaf reselection creates a smaller leaf or disconnects the support forest

**Summary:** In a connected minimum-imbalance support tree, replacing an exceptional leaf deletion cover by its equally balanced support-compatible alternative either disconnects the selected support forest or creates a new smaller leaf with no non-mixing exception.

## Statement

Let J be a connected selected support tree arising from minimum-imbalance deletion covers. Let P be a leaf with neighbor Q, let x label PQ, and let y in Q be exceptional, so the selected cover at y has no consecutive pair joining P to Q-{y}. Replace that selected cover by the equally balanced cover P|((Q-{y}) union {x}). The new support W=(Q-{y}) union {x} was not previously represented in J. The new selected support graph is either disconnected, or is a connected tree in which W is a leaf adjacent to P with |W|<|P|. In the connected outcome, no label of P is exceptional relative to W|P.

## Body

Let \(H\) be a finite boundary \(3\)-tournament with \(\operatorname{pc}(H)>2\). Choose a minimum-imbalance deletion cover \(F_v\) of \(H-v\) for every vertex \(v\), and suppose the selected support graph \(J\) is a connected tree. Let \(P=S_p\) be a leaf support, let \(Q=S_q\) be its neighbor, and let \(x\) label the edge \(pq\).

Suppose \(y\in Q\) is exceptional: the selected cover \(F_y\) has no consecutive pair joining \(P\) to \(Q-\{y\}\). By [[exceptional_leaf_transfer_equals_support_order_gap]], there are nonempty sets
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

Write \(\mathcal A\mathbin{\dot\cup}\mathcal B\) for the bipartition of \(J\), with \(p\in\mathcal A\) and \(q\in\mathcal B\). By [[connected_support_tree_census_bounds_exceptional_leaf_transfer]],
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
All selected covers in the new selection still minimize component imbalance. The exceptional-transfer bound in [[connected_support_tree_census_bounds_exceptional_leaf_transfer]] permits a non-mixing leaf comparison only when the leaf support is larger than its neighbor. Therefore no label \(z\in P\) is exceptional relative to the new leaf edge \(WP\): for every \(z\in P\), the selected cover of \(H-z\) contains a consecutive pair joining \(W\) to \(P-\{z\}\).

Thus reselecting an exceptional leaf cover has only two outcomes: it disconnects the selected support forest, or it replaces the old larger leaf by a new smaller leaf for which every neighboring-support label mixes the two old supports. \(\square\)

## Metadata

- ID: exceptional_leaf_reselection_creates_smaller_leaf_or_disconnects
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
