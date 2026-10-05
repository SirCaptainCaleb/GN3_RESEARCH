# From antipodal labels to cellular root topology

**Summary:** The topology must use cells and extreme-switch roots, not merely antipodal labels on the permutation graph.

## Statement

Naive Tucker and rook-label arguments fail on the permutahedron graph, but their failure identifies the correct cellular objects: commuting squares, braid hexagons, and an odd extreme-switch root map.

## Cold composition

## From rook labels to cellular roots

### Extreme-switch labels

Return first to the unexactified permutation sphere, where the local topology is easiest to see. For a spanning order whose status word contains at least two runs, let
\[
a(\pi)=\text{first switch position},
\qquad
b(\pi)=\text{last switch position},
\]
and put
\[
m=n-2,
\qquad
\bar b(\pi)=m-b(\pi).
\]

Reversal exchanges the two extreme coordinates:
\[
a(\pi^{\rm rev})=\bar b(\pi),
\qquad
\bar b(\pi^{\rm rev})=a(\pi).
\]

A natural first label is therefore the ordered pair
\[
q(\pi)=\bigl(a(\pi),\bar b(\pi)\bigr).
\]
Adjacent transpositions change only a bounded neighborhood of the status word. In particular, away from singular cases the two coordinates behave like a rook move: one coordinate is retained while the other changes locally.

This was the source of the Tucker and Ky Fan attempts.

### Why graph-level Tucker is insufficient

The temptation is to seek a theorem saying that an antipodal rook labeling of the permutahedron graph must contain a complementary edge or a diagonal label. That statement is false in this generality.

Indeed, for a permutation
\[
\pi=(v_1,\ldots,v_n)
\]
consider the purely combinatorial label
\[
Q(\pi)=(v_1,v_n).
\]
Reversal swaps the two coordinates:
\[
Q(\pi^{\rm rev})=(v_n,v_1).
\]
An adjacent transposition either occurs internally, leaving \(Q\) unchanged, or touches one endpoint and changes only one coordinate. Thus adjacent labels share a coordinate exactly as a rook condition would require.

Therefore antipodality plus rook adjacency on the \(1\)-skeleton is not enough to force a contradiction.

The same lesson persists for signed variants. One can build antipodal signed labels with very few magnitudes that avoid complementary labels on every permutahedron edge. Any successful Tucker argument must therefore use higher-dimensional consistency, not merely the graph.

This negative result is worth preserving. It explains why the later cellular topology is necessary.

### Tucker and Ky Fan as guides

A Tucker-style conclusion would ideally produce two compatible chambers carrying complementary extreme data. A Ky Fan-style conclusion would be stronger: an alternating simplex or chain could carry several coordinated switch-front witnesses at once.

The difficulty is not the absence of powerful antipodal theorems. The difficulty is representing the chamber data on a dimension-correct antipodal triangulation while preserving the positional meaning of the labels.

A naive triangulation of the permutahedron introduces diagonals between chambers that need not differ by adjacent transpositions. The local status word can then change in ways not controlled by the rook calculation. Conversely, a labeling confined to chamber vertices remembers the correct local swaps but does not satisfy the hypotheses of the simplicial theorem.

This is the reason Tucker and Ky Fan remain in the article as diagnostic tools rather than claimed closure theorems.

### Rank-two cells: squares and hexagons

The Coxeter complex supplies a canonical cellular repair.

Two independent adjacent transpositions commute. Their four chambers form a square. Adjacent transpositions at neighboring positions satisfy the braid relation
\[
s_is_{i+1}s_i=s_{i+1}s_is_{i+1},
\]
and their six chambers form a hexagon.

These are the rank-two cells controlling all local ambiguity in the chamber graph.

These rank-two cells describe the local relations of adjacent swaps. A proposed graph-level extension must check what the actual status labels do on these cells; their combinatorial shape alone does not prove that every square is harmless or that every exceptional hexagon produces a directed root cycle.

The explicit barycentric extension in the next Section avoids this extension problem: it averages all chamber roots on every face and is defined on all nested face chains. Squares and hexagons remain useful for local combinatorial analysis, but no unproved assertion about their label patterns is needed to define the odd map.

### The extreme-switch root

Replace the ordered pair \(q(\pi)\) by the vector
\[
\phi(\pi)
=
e_{a(\pi)}-e_{\bar b(\pi)}.
\]
This vector lies in the type-\(A\) root space. Reversal is odd:
\[
\phi(\pi^{\rm rev})
=
-\phi(\pi).
\]

The vector is zero exactly at an exact diagonal
\[
a(\pi)=\bar b(\pi).
\]
Otherwise it is an oriented edge of the complete directed graph on the switch-coordinate set.

The root has two advantages over the rook pair.

First, convex combinations make sense. A family of chamber labels may balance at the origin even when no single chamber is diagonal.

Second, the rank-two cellular relations become algebraic relations among roots. A square expresses commuting local changes; an exceptional braid hexagon can support a directed root cycle.

This is the point at which the topology stops asking for one complementary edge and starts asking for **balanced recurrence**.

### From the Helly witnesses to the root

The root coordinates should be read back through the first Section.

The exact two-cover obstruction is a family of defect intervals. The root discards almost all of that family and remembers only the first and reflected-last switch fronts. It is therefore a topological compression of the Helly failure.

This compression is useful because it produces an odd map into a linear representation. It is dangerous because a zero of the compressed data need not itself be the exact two-cover state.

The rest of Article VII is devoted to that gap:
\[
\text{topological balance of extreme witnesses}
\quad\Longrightarrow?\quad
\text{exact combinatorial intersection}.
\]

## Ky Fan forces a hole-sweeping face

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

## Metadata

- ID: antipodal_labels_and_cellular_root_topology
- Kind: section
- Version: 5
- Math version: 4
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — From rook labels to cellular roots](../SUBSECTIONS/antipodal_labels_and_cellular_root_topology_subsection_a.md) (`antipodal_labels_and_cellular_root_topology_subsection_a`; development v4; composition v1; stale=False)
- [Subsection 2 — Ky Fan forces a hole-sweeping face](../SUBSECTIONS/antipodal_labels_and_cellular_root_topology_subsection_b.md) (`antipodal_labels_and_cellular_root_topology_subsection_b`; development v2; composition vNone; stale=False)
