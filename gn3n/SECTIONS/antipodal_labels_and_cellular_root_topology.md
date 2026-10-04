# From antipodal labels to cellular root topology

**Summary:** The topology must use cells and extreme-switch roots, not merely antipodal labels on the permutation graph.

## Statement

Naive Tucker and rook-label arguments fail on the permutahedron graph, but their failure identifies the correct cellular objects: commuting squares, braid hexagons, and an odd extreme-switch root map.

## Body

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

For the extreme-switch data, commuting squares are benign: the two changes are spatially separated and the resulting root labels can be joined without forcing an uncontrolled complementary diagonal.

Braid hexagons are the genuinely interesting cells. The same three local directions are reordered in all six possible ways, so the status data can wind. The exceptional cellular behavior is naturally encoded by a directed \(3\)-cycle in root space.

Thus the progression
\[
\text{Tucker}
\longrightarrow
\text{failure on the graph}
\longrightarrow
\text{cellular squares and hexagons}
\]
is not historical ornament. It identifies the correct scale on which the antipodal labeling is coherent.

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


## Metadata

- ID: antipodal_labels_and_cellular_root_topology
- Kind: section
- Version: 3
- Math version: 2
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Subsection 1 — crystallized, version 3: From rook labels to cellular roots
- Subsection 2 — HOT, version 1: Further developments
