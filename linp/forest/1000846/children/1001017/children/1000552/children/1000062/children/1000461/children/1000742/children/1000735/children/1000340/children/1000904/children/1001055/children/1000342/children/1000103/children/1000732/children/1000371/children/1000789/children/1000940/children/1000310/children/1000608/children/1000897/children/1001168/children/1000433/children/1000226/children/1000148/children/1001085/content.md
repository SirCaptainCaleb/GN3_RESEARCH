# Many local triangle collisions force linearly many edge-disjoint 3-cycles

## Statement

Let
  v_0v_1...v_k
be a rainbow path in the terminal-pair graph with parent hyperedges
  E_s={x_s,v_{s-1},v_s}.
Let M be a set of interior color-terminal collisions x_i=v_j for which there is a hyperedge g_i such that
  g_i,E_j,E_{j+1}
form a linear 3-cycle, as in alternative (2) of 20ee63fa1617.

Then the hypergraph contains at least floor(|M|/32) pairwise edge-disjoint linear 3-cycles of this form.

More explicitly:
(1) one parity class of hit indices j has size at least |M|/2 and its distinguished parent-edge pairs {E_j,E_{j+1}} are pairwise disjoint;
(2) within such a parity class, any fixed hyperedge g can be the third edge of at most four distinguished 3-cycles;
(3) after choosing one cycle for each distinct third edge, the remaining cycle family has an edge-intersection graph of maximum degree at most three.

## Body

Different collisions have different hit indices j. Indeed the terminal-path vertices v_j are distinct, while the entrance labels x_i are distinct because the terminal-pair path is rainbow. Choose a parity of j containing at least |M|/2 collisions. If j,j' have the same parity and j!=j', then the adjacent index pairs {j,j+1} and {j',j'+1} are disjoint. Hence the corresponding distinguished parent-edge pairs are pairwise edge-disjoint.

Fix a hyperedge g and suppose T selected collisions in this parity class use g as the third edge of their 3-cycles. Each such cycle uses two distinct parent edges, and those parent edges meet g in two distinct vertices.

For any selected parent edge E_s={x_s,v_{s-1},v_s}, its intersection vertex with g is one of its three vertices. Across all selected parent edges, a fixed vertex w can occur as a unique entrance x_s for at most one edge, because the path is rainbow. It can occur as a terminal-path vertex in at most two parent edges, namely the two graph-path edges incident with w when w is one of the v_t. Therefore w belongs to at most three selected parent edges.

The edge g has three vertices, so at most nine incidences between g and selected parent edges are possible. Each distinguished 3-cycle using g consumes two such incidences, on two distinct vertices of g. Thus
  2T<=9,
so T<=4.

Starting from the chosen parity class, retain one collision for each distinct third edge g. By the preceding bound this leaves at least |M|/8 cycles. In this retained family, the third edges are pairwise distinct and the distinguished parent-edge pairs are pairwise disjoint.

Build a graph whose vertices are the retained 3-cycles, joining two cycles when they share a hyperedge. Since parent-edge pairs are disjoint and third edges are distinct, any shared hyperedge must be the third edge of one cycle and a parent edge of the other. For a fixed cycle C, its third edge can be a parent edge of at most one other retained cycle, and each of its two parent edges can be the third edge of at most one other retained cycle. Hence this conflict graph has maximum degree at most three.

A graph of maximum degree three has an independent set of size at least one quarter of its vertices. Therefore at least
  (|M|/8)/4 = |M|/32
of the retained 3-cycles are pairwise edge-disjoint, up to the harmless floor in the statement.
