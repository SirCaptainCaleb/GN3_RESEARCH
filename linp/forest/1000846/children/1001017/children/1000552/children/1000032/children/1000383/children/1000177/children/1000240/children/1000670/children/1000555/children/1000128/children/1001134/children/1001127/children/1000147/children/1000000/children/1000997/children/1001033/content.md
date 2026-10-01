# Cycle-free common unique-entrance edges form one consistently oriented block

## Statement

Let
  A=(a_1,...,a_L),  B=(b_1,...,b_M)
be linear paths in a linear 3-graph, oriented toward their last vertices. Assume A union B contains no linear cycle.

Then the full common-edge set
  E(A) intersect E(B)
is a contiguous edge block in each path.

Suppose this common block contains an edge h that is internal to both A and B, is nonspecial, and has the following property: if y is the unique entrance of h, then the edge immediately after h on A meets h at y, and the edge immediately after h on B also meets h at y.

Then, provided the common block has at least two edges, the common block occurs in the same order in the two oriented paths.

## Body

Because A and B are linear paths, their edge sequences are induced paths in the intersection graph of the hypergraph restricted to E(A) union E(B).

Suppose the common-edge set were disconnected along A. Choose two successive common edges h_0,k_0 in the A-order with no common edge strictly between them. The A-segment and B-segment between h_0 and k_0 give two distinct graph paths with the same endpoints. Their union contains a graph cycle. Choose a shortest graph cycle C in this union.

If C has length at least four, then C is induced. In a linear 3-graph an induced intersection-graph cycle of length at least four is a linear hypergraph cycle: nonconsecutive hyperedges are disjoint, and consecutive intersection vertices are distinct because equality of two successive intersection vertices would make the first and third hyperedges intersect, creating a chord.

If the shortest graph cycle has length three, and its three pairwise intersection vertices are distinct, it is already a linear 3-cycle. Otherwise the three hyperedges meet at one common vertex. Such a triangle is a chordal shortcut between the two original routes; shorten across it and repeat. Finiteness gives either a linear triangle or a chordless graph cycle of length at least four. Both contradict the hypothesis.

Hence the full common-edge set is connected in each path, and therefore forms one contiguous edge block.

Write this block in A-order. Its B-order is either the same or reversed. Suppose it is reversed. Consider the distinguished edge h from the statement. Because h is internal to both full paths, each path has an edge immediately after h. Under reversed block orientation, these two successor edges are distinct. If h is internal to the common block, they are its two different common-block neighbors. If h is at a block boundary, one successor is the neighboring common edge and the other lies outside the common block. In either case both successor edges meet h at the same vertex y by hypothesis.

Viewed in either A or B, these two distinct successor edges lie on opposite sides of h and are therefore nonconsecutive path edges. Since both contain y, they intersect, contradicting linearity of that path. Hence reversed orientation is impossible, so the common block has the same order in A and B.
