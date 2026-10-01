# Every foreign 0-1-1 contact manufactures an endpoint lens

## Statement

In a four-edge 0-1-1 consecutive-rank obstruction, every forced foreign contact of a source rail Q_i with e_j creates a two-vertex overlap with the chosen maximum endpoint path of the contacted vertex. An X-hit at x_j yields a source-source theta Q_i∩P_{x_j}; a U-hit at u_j yields a source-terminal theta Q_i∩P_{u_j}. Hence all twelve directed transversal incidences manufacture endpoint lenses.

## Body

Let e_j={x_j,v,u_j} be a 0-1-1 ascending nonspecial edge, and let P_{x_j},P_{u_j} be the globally chosen maximum endpoint paths ending physically at x_j,u_j.

Let Q be any other chosen maximum endpoint path whose physical endpoint is distinct from x_j,u_j.

If x_j belongs to V(Q), then Q and P_{x_j} share at least two vertices. If they shared only x_j, the universal unique-intersection theorem 5854d853a44b would force x_j to be a joint on P_{x_j}, impossible because x_j is its physical endpoint.

Likewise, if u_j belongs to V(Q), then Q and P_{u_j} share at least two vertices, for the same reason.

Apply this to the complete source-rail transversality system 3d93f4d4b775. For every ordered pair i!=j, the source rail Q_i contains at least one distinguished vertex
  w_{ij} in {x_j,u_j}.
Whichever label occurs, Q_i has a second intersection with the chosen maximum endpoint path P_{w_{ij}}.

Thus each of the twelve directed foreign contacts in a four-edge 0-1-1 violation generates a genuine two-vertex overlap between maximum endpoint paths:
- an X-hit generates a source-source theta Q_i versus Q_j=P_{x_j};
- a U-hit generates a source-terminal theta Q_i versus P_{u_j}.

In particular there is no simple-contact escape at the level of endpoint-path geometry: a foreign contact may move from the source rail to the opposite-terminal path, but it always creates a lens somewhere in the chosen maximum-path family.
