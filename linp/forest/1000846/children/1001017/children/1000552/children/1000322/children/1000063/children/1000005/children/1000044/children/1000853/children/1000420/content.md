# Class-III rank-four terminal stars force an alternating five-vertex matching

## Statement

Let H be a 12-vertex 5-regular linear triple system. Suppose e={x,y,z} is a nonspecial edge of rank four with unique entrance x, and let
  P=(g_1,g_2,g_3,e)
be a longest path ending in e through x. Write
  g_1={r,a,b},  g_2={r,c,d},
and relabel c,d so that
  g_3={c,x,t}.
Let u,v,w be the three vertices outside V(P), and put
  R={r,t,u,v,w}.

After possibly swapping c,d, the terminal stars contain the crossed rectangle
  {y,a,c}, {y,b,d}, {z,a,d}, {z,b,c}.

The two remaining edges through y other than e determine a 2-edge matching M_y on R, and the two remaining edges through z determine an edge-disjoint 2-edge matching M_z on R. Every vertex of R lies in M_y∪M_z; hence M_y∪M_z is an alternating five-vertex path. Moreover r is an internal vertex of this path, so r has degree two in M_y∪M_z.

Finally, among the eight edges of H not yet listed, every edge contains exactly one vertex of
  A={r,a,b,c,d}
and two vertices of
  B={x,t,u,v,w}.

## Body

Orient the path so that
  g_1={r,a,b},  g_2={r,c,d},  g_3={c,x,t},  e={x,y,z}.
Let u,v,w be the three vertices outside V(P).

Fix the terminal y. The five edges through y have pairwise disjoint off-y pairs by linearity. The edge e uses the pair {x,z}; hence the other four y-edges form a matching of size four on
  {r,a,b,c,d,t,u,v,w},
leaving exactly one of these nine vertices unmatched.

We first force c and d to be matched to a and b. If a y-edge h contains c or d but misses g_1, then
  g_1,g_2,h,e
is a four-edge linear path ending in e through y: g_1 is disjoint from h, g_2 meets h in c or d, g_2 is disjoint from e, and h meets e only at y. This is a longest e-ending path with entrance y, contradicting uniqueness of the entrance x. Thus every y-edge containing c or d also meets g_1.

Such an edge cannot use r together with c or d, because then it would share two vertices with g_2. Hence a y-edge containing c or d must pair that vertex with a or b.

Neither c nor d can be the unique unmatched vertex. For example, if c were unmatched, then d would be paired with one of a,b, say a. Since c is already the unique unmatched vertex, b must also occur in some y-edge. That edge cannot use r, since it would share {b,r} with g_1; it cannot use c, since c is unmatched; and it cannot use d, since distinct y-edges cannot both contain d. Thus it misses g_2, and then
  g_2,g_1,h,e
is a four-edge linear path ending in e through y, again contradicting the unique entrance. The same argument excludes d as the unmatched vertex.

Therefore c and d are both matched, one to a and one to b. After swapping c,d if necessary, the y-star contains
  Y_a={y,a,c},  Y_b={y,b,d}.

The identical argument at z gives two edges pairing {a,b} bijectively with {c,d}. Linearity forbids either z-edge from using the same off-terminal pair as the corresponding y-edge, so necessarily
  Z_a={z,a,d},  Z_b={z,b,c}.

After removing e and these four rectangle edges, the two remaining y-edges have off-y pairs entirely in
  R={r,t,u,v,w};
they form a 2-edge matching M_y. Likewise the two remaining z-edges give a 2-edge matching M_z on R. The two matchings have no common edge, since otherwise a y-edge and a z-edge would share two nonterminal vertices.

Let d_M(s) be the degree of s in M_y∪M_z. There are exactly twelve listed edges:
the four path edges, the four rectangle edges, and the four residual terminal edges. Since H has 12*5/3=20 edges, exactly eight edges remain, and none contains y or z because those vertices are already saturated.

We claim d_M(s)>=1 for every s in R. Consider the remaining eight edges and use linearity as a partner-capacity bound.

For r, the known path edges g_1,g_2 already use the four partners a,b,c,d, and the terminal matchings use d_M(r) further partners in R. Its remaining hypergraph degree is 3-d_M(r), so it needs
  2(3-d_M(r))
distinct new partners among only
  5-d_M(r)
available vertices. Hence d_M(r)>=1.

For t, the edge g_3 already uses partners c,x. Its remaining degree is 4-d_M(t), and only 7-d_M(t) new partners are available. Thus
  2(4-d_M(t)) <= 7-d_M(t),
so d_M(t)>=1.

For each s in {u,v,w}, its only listed incidences are the d_M(s) terminal-matching edges. Its remaining degree is 5-d_M(s), with 9-d_M(s) available partners. Thus
  2(5-d_M(s)) <= 9-d_M(s),
again giving d_M(s)>=1.

The two 2-edge matchings contribute total degree eight on the five-set R, and every vertex has degree one or two. Therefore the degree sequence is 2,2,2,1,1. Since the union of two matchings has no odd cycle and no common edge, it is an alternating path on all five vertices.

Now put
  A={r,a,b,c,d}.
Every pair of vertices of A has already appeared in one of the listed edges: g_1 and g_2 cover the pairs within {r,a,b} and {r,c,d}, while the four rectangle edges cover ac,ad,bc,bd. Hence every one of the eight remaining hyperedges contains at most one vertex of A.

The residual degrees required at a,b,c,d are respectively 2,2,1,2. At r the residual degree is 3-d_M(r). Thus the eight remaining edges require
  2+2+1+2+(3-d_M(r))=10-d_M(r)
incidences with A.
Since each remaining edge contributes at most one such incidence,
  10-d_M(r) <= 8.
As d_M(r)<=2, we obtain d_M(r)=2. Hence r is an internal vertex of the alternating five-vertex path M_y∪M_z. Equality also shows that every remaining edge contains exactly one vertex of A, and therefore exactly two vertices of
  B={x,t,u,v,w}.
