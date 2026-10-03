# The forest case

## Body

## The forest case

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

## Metadata

- ID: deletion_covers_and_the_support_graph_the_forest_case
- Kind: section
- Version: 2
- Math version: 2
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Subsection 1 — HOT, version 2: The forest case
