# Local 3-cycle collisions force a linear packing of edge-disjoint 3-cycles

## Statement

Let T be a family of interior U_11 color-terminal collisions on one simple rainbow terminal-pair path, and suppose every member is of the local linear 3-cycle type from 20ee63fa1617.

Then the hypergraph contains at least
  ceil(|T|/32)
pairwise edge-disjoint linear 3-cycles arising from members of T.

## Body

Apply 3f165c52a1a6. Choose a subfamily T_1 with
  |T_1|>=ceil(|T|/2)
such that the distinguished parent-edge pairs
  {E_j,E_{j+1}}
are pairwise edge-disjoint, and every fixed host hyperedge occurs for at most four members of T_1.

Choose from T_1 at most one collision for each host hyperedge. This gives a subfamily T_2 with
  |T_2|>=ceil(|T_1|/4)>=ceil(|T|/8),
whose host hyperedges are pairwise distinct and whose distinguished parent-edge pairs remain pairwise edge-disjoint.

For a collision alpha in T_2, write its triangle edge set as
  {g_alpha,A_alpha,B_alpha},
where g_alpha is the host edge and {A_alpha,B_alpha} is its distinguished parent-edge pair.

Construct a conflict graph K on T_2 by joining two collisions when their two linear 3-cycles share a hyperedge. Since all host edges are distinct and all distinguished parent edges are distinct across the family, the only possible shared-edge event is that the host edge of one collision equals a distinguished parent edge of the other.

Orient such a conflict alpha->beta when
  g_alpha in {A_beta,B_beta}.
Each vertex alpha has outdegree at most one, because g_alpha is one fixed hyperedge and the distinguished parent pairs are pairwise edge-disjoint. Each vertex beta has indegree at most two, because beta has only the two distinguished parent edges A_beta,B_beta and the host edges are pairwise distinct. Hence the underlying conflict graph has maximum degree at most three.

A graph of maximum degree at most three has an independent set of size at least one quarter of its vertices. Choose such an independent set T_3. The corresponding linear 3-cycles are pairwise edge-disjoint, and
  |T_3|>=ceil(|T_2|/4)>=ceil(|T|/32).
This proves the claim.
