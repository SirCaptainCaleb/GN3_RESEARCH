# The forest case

## Metadata

- ID: deletion_covers_and_the_support_graph_the_forest_case_subsection_a
- Parent Section: deletion_covers_and_the_support_graph_the_forest_case
- Position: 1
- Row version: 4
- Development version: 4
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

Assume \(J\) is a forest. Let \(e_x=PQ\) be a leaf edge, with \(P\) the leaf support and \(Q\) its neighbor. Thus
\[
V(H)=P\mathbin{\dot\cup}Q\mathbin{\dot\cup}\{x\}.
\]
The detailed leaf analysis is carried by [[leaf_comparisons_in_deletion_support_forests]]. Its strongest consequence is that the forest route has a substantially cleaner normal form than the original one-endpoint comparison suggests.

### Connected trees

Assume first that \(J\) is connected. For every leaf support \(P\) with neighbor \(Q\), all but at most one label \(y\in Q\) have a selected deletion cover \(F_y\) containing a consecutive pair with one endpoint in \(P\) and the other in \(Q-\{y\}\). Under the standing minimum-imbalance selection, the unique possible exceptional cover may be replaced by an equally balanced alternative. After at most one such reselection, either the selected support graph becomes disconnected, or it remains a connected tree with a leaf edge
\[
H-x=L\mid M
\]
such that every \(z\in M\) has a selected deletion cover \(F_z\) containing an edge joining \(L\) to \(M-\{z\}\).

In particular, fixing any Hamiltonian order
\[
M=(m_0,\ldots,m_s),
\]
both endpoint deletion covers \(F_{m_0}\) and \(F_{m_s}\) contain direct mixed edges between the two old supports. Thus the connected-tree branch does not need a preliminary endpoint merely to force interaction: direct mixing is simultaneously available at both ends.

**Proposition 8 (two-endpoint leaf normal form).** Under minimum-imbalance deletion-cover selection, if the selected support graph is a connected tree, then after changing at most one selected cover to an equally balanced alternative, either the support graph becomes disconnected or there is a leaf edge
\[
H-x=L\mid M,\qquad M=(m_0,\ldots,m_s),
\]
for which each endpoint deletion cover \(F_{m_i}\), \(i\in\{0,s\}\), contains an edge joining a surviving vertex of \(L\) to a surviving vertex of \(M\).

**Proof.** This is the paired-endpoint reduction proved in [[leaf_comparisons_in_deletion_support_forests]]. \(\square\)

Consequently the connected-tree case enters the direct-mixing hypothesis of the Remaining Lemma at either endpoint. If one continues the local endpoint analysis instead, the same cited Section shows independently at both ends that one obtains an order disagreement, a split inherited edge of \(M-\{m_i\}\), a leave-and-return path disturbance through \(L\), an end-edge reversal, strict quadratic-potential descent, or equal-potential recurrence between selected singleton lifts. The important global point is that these are now paired endpoint disturbances: neither endpoint is spent establishing the existence of a mixed edge.

### Disconnected forests

Let \(T\) be the tree component containing a leaf edge \(P Q\), and let \(D_T\) be its set of edge labels. For a Hamiltonian order on \(Q\) with endpoints \(a,b\), [[leaf_comparisons_in_deletion_support_forests]] gives the following dichotomy:

- if \(a,b\in D_T\), then at least one of \(F_a,F_b\) contains an edge joining \(P\) to the surviving part of \(Q\);
- otherwise at least one endpoint label has its selected edge in a different tree component of \(J\).

More strongly, among labels \(y\in Q\cap D_T\), at most one can fail to mix \(P\) with \(Q-\{y\}\); if \(Q\) contains any label outside \(D_T\), then no internal label is exceptional.

Hence the genuinely new residue of the disconnected-forest branch is not a split leaf support. It is component escape: an endpoint of the neighboring Hamilton path may index a selected deletion cover whose support edge lies in another tree component. Whenever both endpoint labels remain in the leaf component, the forest route again reaches the direct-mixing hypothesis of the Remaining Lemma.

Thus the forest case is reduced to two global interfaces:

1. direct mixed edges at one or, in the connected-tree normal form, both ends of a neighboring displayed path;
2. in a disconnected support forest, migration of an endpoint label to another support-tree component.

The earlier leaf-splitting alternative is absorbed by the leaf-comparison structure and need not be carried as a terminal forest residue.

### Component escape is not a terminal forest residue

The disconnected-forest alternative can now be treated at the same endpoint level as the connected-tree case.

**Corollary 9.** Let
[
H-x=Pmid Q,
qquad
Q=(q_0,ldots,q_m),
]
correspond to a leaf edge of an arbitrary selected support forest. Then, unless (H) already contains a bounded Hamiltonian support with two-coverable complement, an order disagreement, or an external reversal, at least one endpoint
[
yin{q_0,q_m}
]
has a selected deletion cover (F_y) containing an ordinary path edge joining (P) to (Q-{y}).

Consequently the endpoint disturbance theorem applies at some displayed endpoint of every leaf-neighbor path, regardless of whether the selected endpoint edge remains in the leaf's tree component.

**Proof.** If one endpoint cover already contains such a mixed edge, there is nothing to prove. Suppose neither endpoint cover mixes the two old supports. Lemma 13 of [[leaf_comparisons_in_deletion_support_forests]] then gives one of: a bounded Hamiltonian support, an order disagreement, or an adjacent-slot reversal. These are exactly the excluded successful disturbances. Hence the two endpoint covers cannot both be non-mixing in the unresolved branch. (square)

Combining this with
[[path_disturbance_endpoint_reversal_descent_or_an_omission_swap]],
the forest route has only the following outputs at a leaf edge:
[
	ext{order disagreement},quad
	ext{split/leave-and-return},quad
	ext{external reversal},quad
	ext{strict }Phi	ext{-descent},quad
	ext{neutral omission swap},
]
or a two-cover/bounded-support conclusion.

Order disagreement and split/leave-and-return already collapse to the external-reversal interface in Article III. Thus the only genuinely quiet forest phenomenon is neutral omission-swap recurrence. The earlier “component escape” alternative is no longer independent.



### Neutral omission-swap recurrence is not a forest obstruction

The last quiet forest alternative also closes globally.

**Corollary 10 (forest recurrence closure).** In the forest branch, every leaf-endpoint comparison eventually yields one of
[
	ext{two-cover},quad
	ext{bounded Hamiltonian support},quad
	ext{order disagreement},quad
	ext{external reversal},quad
	ext{split/leave-and-return disturbance},quad
	ext{strict }Phi	ext{-descent}.
]
Neutral omission-swap recurrence is not an additional terminal alternative.

**Proof.** By Corollary 9, after bounded support, order disagreement, and external reversal are excluded, some displayed endpoint of every leaf-neighbor path enters the direct-mixing disturbance theorem
[[path_disturbance_endpoint_reversal_descent_or_an_omission_swap]].
Its only quiet output is a neutral omission swap.

Continue such a neutral swap through the selected minimum-imbalance deletion covers as in
[[balanced_omission_swap_gives_descent_or_selected_singleton_recurrence]].
Corollary 12 of
[[three_cover_repartitions_and_recurrence_several_deleted_labels_in_one_component]]
shows that, in a selected support forest, no indefinitely neutral trajectory exists: every such continuation eventually leaves the neutral regime through a two-cover, bounded-support outcome, order disagreement, external reversal, split disturbance, or strict descent. (square)

Thus the selected-support forest is no longer an independent global obstruction. After the Article I support-graph reductions, every forest branch returns to the same successful disturbance interfaces already used by Articles III–VI.
