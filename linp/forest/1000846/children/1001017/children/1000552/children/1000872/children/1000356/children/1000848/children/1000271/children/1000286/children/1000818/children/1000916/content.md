# A source hit forces a second source-rail intersection

## Statement

For two source-clean 0-1-1 edges through a common assigned terminal, if the source x_j of one edge lies on the other edge's chosen maximum source rail Q_i, then Q_i and Q_j share at least two vertices. Hence any pair of source rails with exactly one common vertex must contact each other's offending edges reciprocally through the opposite terminals u_i,u_j, never through the sources.

## Body

Let e_i={x_i,v,u_i} and e_j={x_j,v,u_j} be two distinct 0-1-1 ascending nonspecial edges assigned at the common terminal v, and let Q_i,Q_j be their chosen source-clean maximum endpoint paths ending physically at x_i,x_j.

Suppose x_j belongs to V(Q_i). Then Q_i and Q_j have at least two common vertices.

Indeed x_j is a common vertex because it is the physical endpoint of Q_j. If it were the unique common vertex, the universal unique-intersection lemma 5854d853a44b would force x_j to be a same-index path joint on Q_j. But x_j is the physical last vertex of Q_j, so it is not a path joint. Contradiction.

Therefore every directed source hit x_j in V(Q_i) forces |V(Q_i) cap V(Q_j)|>=2.

Consequently, if Q_i and Q_j have exactly one common vertex, then neither directional foreign-edge contact can use the foreign source. By complete source-rail transversality 3d93f4d4b775, Q_i meets e_j and Q_j meets e_i. Since source hits are excluded, these contacts must use the opposite terminals:
  u_j in V(Q_i),
  u_i in V(Q_j).

Thus every simple edge of the source-rail intersection K4 is necessarily a reciprocal terminal-terminal (U-U) exchange, while every X-hit pair is a nonsimple/theta edge.
