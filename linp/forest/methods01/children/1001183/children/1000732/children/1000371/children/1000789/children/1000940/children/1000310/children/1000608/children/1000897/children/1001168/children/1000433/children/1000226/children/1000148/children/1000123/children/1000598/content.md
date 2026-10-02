# Tight U_11 color-terminal collisions contain a half-size matching of multiple-overlap source-path pairs

## Statement

Let T be a family of interior U_11 color-terminal collisions
  x_i=v_j
on one simple rainbow terminal-pair path, all satisfying the tight equality
  r_j+r_{j+1}=r_i+2.

For each collision draw the directed index edge
  i -> j.
Then these directed edges form a vertex-disjoint union of directed paths. In particular T contains a subfamily T' of size at least
  ceil(|T|/2)
such that all indices occurring in the pairs {i,j} are distinct.

For every collision i->j in T',
  |V(R_i) intersect V(R_j)|>=2.

Hence |T| tight collisions force at least ceil(|T|/2) index-disjoint pairs of chosen maximum source paths having at least two common vertices.

## Body

By 1b787a779ada, every tight collision i->j satisfies
  |V(R_i) intersect V(R_j)|>=2.

It remains only to analyze the collision relation on indices. Each index i is the owner of at most one color-terminal collision: the unique entrance x_i is one fixed vertex, and the terminal-pair path is simple, so x_i can equal at most one path vertex v_j.

Likewise each hit index j has indegree at most one. If
  x_i=v_j=x_h,
then the rainbow property of the terminal-pair path forces i=h.

Thus the directed collision graph has indegree at most one and outdegree at most one. Every directed edge points strictly backward, j<=i-2, so directed cycles are impossible. Therefore every connected component is a directed path.

A directed path with e edges has a matching of size ceil(e/2). Taking maximum matchings independently in the components gives a matching of size at least ceil(|T|/2) over the whole collision graph. The corresponding source-path pairs are index-disjoint, and each has at least two common vertices by the first paragraph.