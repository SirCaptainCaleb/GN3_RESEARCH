# A 2q-3 cut with M crossing collisions forces linear overlap matching or linear 3-cycle packing

## Statement

Let
v_0v_1...v_k
be a rainbow terminal-pair path whose parent hyperedges belong to U_11 and have nondecreasing edge ranks.
Fix a cut with
  r_t=q,
  r_{t+1}=2q-3,
and suppose M interior color-terminal collisions cross the cut.

Then at least one of the following holds:

(1) there are at least ceil(M/6) pairwise index-disjoint pairs of chosen maximum source paths, each pair having at least two common vertices;

(2) the hypergraph contains at least ceil(M/64) pairwise edge-disjoint linear 3-cycles arising from the crossing collisions.

Thus collision congestion at the next-to-boundary multiplicative jump has a linear, rather than square-root, structural cost.

## Body

By c9982d3355c8 and ed2ef3140f4f, every crossing collision has one of two structural outputs.

Overlap type: there is an adjacent index s in {j,j+1} such that
  |V(R_i) intersect V(R_s)|>=2.

Triangle type: the two exact contact intervals overlap and an edge of R_i together with E_j,E_{j+1} forms a local linear 3-cycle.

Let O and T be the numbers of overlap-type and triangle-type collisions, choosing the overlap label when both outputs happen to be available. Then
  O+T=M.

Suppose first that T>=M/2. The certified local-triangle packing theorem 48125e6d5ad9 gives at least
  ceil(T/32)>=ceil(M/64)
pairwise edge-disjoint linear 3-cycles. This is (2).

Now suppose O>=M/2. For each overlap-type collision x_i=v_j choose one witnessing adjacent index s in {j,j+1} and draw a directed edge
  i -> s.

Every directed edge points backward because s<=j+1<=i-1. Each owner index i has outdegree at most one. A fixed index s can be the chosen target only for a collision hitting v_s or v_{s-1}; since hit indices are distinct on the rainbow terminal-pair path, the indegree is at most two.

The underlying graph therefore has maximum degree at most three. It is also a forest. Indeed, if it contained an undirected cycle, choose the largest index on that cycle. Both incident cycle edges would point from this largest index toward smaller indices, giving outdegree at least two, a contradiction.

A forest of maximum degree at most three has an edge coloring with three colors: remove a leaf edge, color the remaining forest inductively, and use at the leaf edge a color absent from the at most two other edges at its nonleaf endpoint. Therefore one color class is a matching of size at least
  ceil(O/3)>=ceil(M/6).

The corresponding source-path pairs are index-disjoint and each has at least two common vertices. This is (1).
