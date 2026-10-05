# Ky Fan forces a hole-sweeping face

## Metadata

- ID: antipodal_labels_and_cellular_root_topology_subsection_b
- Parent Section: antipodal_labels_and_cellular_root_topology
- Position: 2
- Row version: 2
- Development version: 2
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

### Ky Fan forces a hole-sweeping face

Assume
\[
k=\kappa_2(H)\ge2.
\]
For a proper permutahedron face \(F\), call an actual vertex \(v\in V(H)\)

- **uniformly positive on \(F\)** if \(v\in P_\pi\) for every chamber \(\pi\in\mathcal V(F)\);
- **uniformly negative on \(F\)** if \(v\in Q_\pi\) for every chamber \(\pi\in\mathcal V(F)\).

Uniformity is inherited by subfaces. Reversal exchanges the two signs.

**Theorem 5.1 (hole-sweeping face).** There exists a proper permutahedron face \(F\) having no uniformly positive and no uniformly negative actual vertex. Consequently, for every \(v\in V(H)\), some chamber \(\pi\in\mathcal V(F)\) has
\[
v\in X_\pi.
\]

**Proof.** Suppose every proper face has a uniformly signed actual vertex. Fix an arbitrary total order of \(V(H)\). Label the barycentric-subdivision vertex corresponding to \(F\) by the least actual vertex that is uniformly signed on \(F\), with sign \(+\) or \(-\) according to its uniform role.

This is an antipodal labeling: the candidate set is unchanged by reversal and every sign is reversed. Moreover a barycentric edge joins nested faces \(F\subset G\), and its endpoint labels cannot be complementary in one absolute label. Indeed, if \(v\) is uniformly positive on \(F\) and uniformly negative on \(G\), then uniform negativity on \(G\) is inherited by \(F\), impossible. The other orientation is symmetric.

The barycentric subdivision of the boundary of the \((n-1)\)-dimensional permutahedron is an antipodal triangulation of \(S^{n-2}\). Ky Fan's lemma therefore gives a top-dimensional simplex whose \(n-1\) labels have distinct absolute values. Such a simplex is a maximal chain
\[
F_0\subsetneq F_1\subsetneq\cdots\subsetneq F_{n-2}
\]
of proper faces. The bottom face \(F_0\) is one chamber \(\pi\). Every sign attached to a larger face is inherited by this chamber. Hence \(n-1\) distinct actual vertices of \(H\) lie in \(P_\pi\cup Q_\pi\). Therefore
\[
|X_\pi|\le1,
\]
contradicting
\[
|X_\pi|=\delta(\pi)\ge\kappa_2(H)=k\ge2.
\]
Thus some proper face \(F\) has no uniformly signed vertex.

Now fix \(v\in V(H)\). If \(v\) never belonged to \(X_\pi\) on this face, then it would take only the roles \(P\) and \(Q\). The chamber graph of a permutahedron face is connected. By the no-direct-side-flip lemma of [[spanning_orders_and_defect_helly]], one adjacent transposition cannot change \(v\) directly from \(P\) to \(Q\) or conversely. Hence its role would be constant on the whole face, making \(v\) uniformly signed, a contradiction. Therefore \(v\) occurs in the exact hole in some chamber of \(F\). \(\square\)

Call such an \(F\) a **hole-sweeping face**. Its significance is global: one fixed ordered-partition face supports canonical partial two-covers whose holes collectively sweep the entire vertex set.

Two immediate consequences are worth recording. The first face block has order at least three, because the first two positions of every chamber always lie in \(P_\pi\); a block of order at most two would make one of its vertices uniformly positive. Symmetrically the last face block has order at least three.

This theorem supplies the higher-dimensional consistency missing from the earlier graph-level Tucker attempt. The labels are actual vertices rather than switch positions, the exact deletion gap \(k\ge2\) forbids complementary labels across chamber edges, and Ky Fan forces failure of uniform signed labeling on one genuine permutahedral face.
