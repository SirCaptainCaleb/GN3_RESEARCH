# Class-II systems have no rank-four nonspecial edge

## Statement

A 4-regular P_5^(3)-free linear triple system has no nonspecial edge of rank four.

## Body

Suppose e={x,y,z} were nonspecial of rank four, with unique entrance x. Choose a longest path
P=(g_1,g_2,g_3,e)
ending in e through x.

By 1f16e26bffcf, write
g_1={r,a,b},  g_2={r,c,d}
so that the four forced terminal edges are
Y_a={y,a,c},  Y_b={y,b,d},
Z_a={z,a,d},  Z_b={z,b,c}.

Since P is linear, g_3 is disjoint from g_1, meets g_2 in exactly one of c,d, and meets e at x. Relabel a,b and c,d simultaneously if necessary so
g_3={c,x,t}
for a vertex t outside {x,y,z,r,a,b,c,d}.

There is one remaining edge through y meeting g_1 at r; call it
Y_r={y,r,p}.
Likewise the remaining edge through z meeting g_1 at r is
Z_r={z,r,q}.

We first locate p,q. The vertex p cannot be x or z because the pairs {x,y},{y,z} already lie in e. It cannot be a or c because those pairs with y already lie in Y_a, and it cannot be b or d because those pairs with y already lie in Y_b. Thus p lies outside
{x,y,z,r,a,b,c,d}.
The same argument using Z_a,Z_b gives the same conclusion for q. Moreover p≠q, because Y_r and Z_r already meet at r and linearity forbids a second common vertex.

At this point ten distinct edges are known:
e,g_1,g_2,g_3,
Y_a,Y_b,Z_a,Z_b,Y_r,Z_r.

Their degrees already saturate four vertices:
d(y)=4 via e,Y_a,Y_b,Y_r;
d(z)=4 via e,Z_a,Z_b,Z_r;
d(r)=4 via g_1,g_2,Y_r,Z_r;
d(c)=4 via g_2,g_3,Y_a,Z_b.
Therefore none of the remaining six edges of H can contain y,z,r, or c.

The nine explicitly named vertices
x,y,z,r,a,b,c,d,t
leave exactly three further vertices, say u_1,u_2,u_3. Hence every remaining edge lies entirely in the eight-vertex set
S={a,b,d,x,t,u_1,u_2,u_3}.

Now inspect the four vertices
T={t,u_1,u_2,u_3}.
Among the ten known edges, the total degree contributed to T is exactly three: g_3 contributes one incidence at t, and Y_r,Z_r contribute one incidence each at p,q, where p,q∈T. This remains true even if one of p,q equals t.

Since H is 4-regular, the four vertices of T have total target degree 16. Consequently the six remaining edges must contribute
16-3=13
incidences to T.

By pigeonhole, some vertex of T must therefore lie in at least four of the six remaining edges.

But those six edges form a linear 3-uniform hypergraph on the eight-vertex set S. In any linear triple system on eight vertices, the degree of a vertex is at most floor((8-1)/2)=3, because distinct triples through that vertex require disjoint pairs among the other seven vertices.

This contradiction proves that no rank-four nonspecial edge can occur.