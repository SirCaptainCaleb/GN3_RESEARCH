# Local 3-cycle collisions have bounded host-edge reuse

## Statement

Let T be a family of interior color-terminal collisions x_i=v_j on one simple rainbow terminal-pair path. Suppose every collision in T is of the local 3-cycle type from 20ee63fa1617: for each hit index j choose an edge g_j of the colliding chosen maximum path such that
  g_j,E_j,E_{j+1}
form a linear 3-cycle.

Then there is a subfamily T' with
  |T'|>=ceil(|T|/2)
whose distinguished parent-edge pairs {E_j,E_{j+1}} are pairwise edge-disjoint.

Within T', any fixed hyperedge g occurs as g_j for at most four collisions. Consequently the family {g_j : j in T'} contains at least
  ceil(|T'|/4)
  >= ceil(ceil(|T|/2)/4)
distinct hyperedges.

## Body

The hit indices j are distinct because the terminal-path vertices v_j are distinct and the entrance labels x_i are pairwise distinct. Partition T by the parity of j. In either parity class, distinct hit indices differ by at least two, so the corresponding adjacent parent-edge pairs
  {E_j,E_{j+1}}
are disjoint. Choose the larger parity class T'.

Fix a hyperedge g and count collisions in T' for which g_j=g. For each such collision, g meets E_j and E_{j+1} in two distinct vertices, because g,E_j,E_{j+1} form a linear 3-cycle. Since the distinguished parent-edge pairs are disjoint across T', these are two distinct vertex-parent-edge incidences for every collision.

We claim that a fixed vertex w belongs to at most three parent hyperedges of the rainbow terminal-pair path. If w is a terminal-path vertex, simplicity of the graph path makes w=v_s for at most one s, so w is terminal in at most the two incident parent edges E_s,E_{s+1}. Independently, rainbowness makes w an entrance label x_t for at most one parent edge E_t. These are the only ways w can belong to a parent triple. Hence w is contained in at most three parent hyperedges.

The three vertices of g therefore support at most nine incidences with parent hyperedges of the terminal-pair path. Every collision counted for g consumes two distinct such incidences, and the disjointness of the distinguished parent pairs ensures that no incidence is consumed twice. Thus g supports at most floor(9/2)=4 collisions of T'.

The final distinct-host-edge bound follows by dividing |T'| by four.