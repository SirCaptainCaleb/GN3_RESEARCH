# Consecutive top-rank host edges cannot both be forward-flat ascending outputs

## Statement

Let P=(g_1,...,g_L) be a globally longest L-edge path. Suppose two consecutive host edges g_j,g_{j+1} both occur as nonspecial ascending outputs in the top-rank rotation decomposition 09e3d5b2bd6b. Then this is impossible.

Equivalently, among the top-rank output edges on P, those lying in the flat ascending branch form an independent set in the path-edge order.

More explicitly, if g_j is a flat ascending output, then its forward joint
  z_j=g_j intersect g_{j+1}
has endpoint potential L-1, while the backward joint z_{j-1} and private vertex b_j of g_j both have endpoint potential L. Hence the next edge g_{j+1} cannot also be flat ascending with entrance z_{j+1}, because z_j would be one of its terminal vertices and would have to have potential at least L.

## Body

By 09e3d5b2bd6b, if g_j is a nonspecial ascending output of rank L, then its unique entrance is the forward joint
  z_j=g_j intersect g_{j+1}
and
  phi(z_j)=L-1.

The other two vertices of g_j are its terminals: the backward joint
  z_{j-1}=g_{j-1} intersect g_j
and the private vertex b_j. Since g_j has rank L, a longest L-edge path ending in g_j through z_j may choose either terminal as its physical last vertex. Therefore
  phi(z_{j-1})>=L,
  phi(b_j)>=L.
By global maximality of L, both equal L.

Now suppose g_{j+1} were also a flat ascending output. Its unique entrance would be its forward joint z_{j+1}. Thus its remaining two vertices, including the backward joint z_j, are terminals of the rank-L edge g_{j+1}. Hence phi(z_j)>=L, contradicting phi(z_j)=L-1.

Therefore consecutive flat ascending output edges cannot occur.
