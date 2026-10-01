# Fourfold triangle-host reuse forces two further color-terminal collisions

## Statement

Retain the parity-selected family T' from 3f165c52a1a6, so the distinguished parent-edge pairs {E_j,E_{j+1}} are pairwise disjoint. Fix a hyperedge g.

If g is the third edge of four distinguished linear 3-cycles
  g,E_j,E_{j+1},
then at least two vertices of g are simultaneously:
(1) terminal-path vertices v_s of the rainbow terminal-pair path, and
(2) unique entrance labels x_t of parent hyperedges.

Hence fourfold reuse of one triangle host forces at least two additional color-terminal collisions x_t=v_s on the same rainbow terminal-pair path.

## Body

The four distinguished 3-cycles use eight distinct parent hyperedges, because the parity selection makes their adjacent parent-edge pairs pairwise disjoint. Each of those eight parent hyperedges meets g in one vertex.

For a fixed vertex w of g, among parent hyperedges of the rainbow terminal-pair path, w can occur as a terminal-path vertex in at most two edges: if w=v_s, only E_s and E_{s+1} contain w as a terminal. Independently, w can occur as a unique entrance label in at most one parent edge, because the terminal-pair path is rainbow.

Thus the three vertices of g provide at most six terminal incidences plus at most three entrance incidences. Four triangles require eight parent-edge incidences with g.

Suppose fewer than two vertices of g were both terminal-path vertices and entrance labels. Then at most one vertex could contribute the full capacity three. Each of the other two vertices could contribute at most two, because a vertex that is not simultaneously a terminal-path vertex and an entrance label cannot realize both types of incidence. The total capacity would therefore be at most
  3+2+2=7,
contradicting the required eight incidences.

Hence at least two vertices w of g occur both as some terminal-path vertex v_s and as some entrance label x_t. Each equality x_t=v_s is a color-terminal collision. Since the terminal-pair path is rainbow and simple, the two vertices yield two distinct collisions.