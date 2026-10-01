# The final one-low odd-boundary state creates a four-vertex high-potential central packet

## Statement

In the surviving p=2q-3 one-low 0-1-1 state, the occupied contacts are A,B,C,D, with both C and D terminal-only. Let
  e_C={x_C,v,C}
have rank q and
  e_D={x_D,v,D}
have rank q+1,
where x_C,x_D are their absent unique entrances.

Then charged endpoint rotations of P_v give
  phi(E)>=p,   E=g_{q-1}∩g_q,
  phi(G)>=p,   G=g_q∩g_{q+1},
with p=2q-3.

Since C and D are opposite terminals of edges assigned to v, also
  phi(C)>=p, phi(D)>=p.
Hence the four vertices C,D,E,G, lying in the three consecutive central path edges g_{q-1},g_q,g_{q+1}, all have endpoint potential at least p.

## Body

The assertion phi(E)>=p is fb9dfc3b63b8.

For e_D, the sole P_v-contact outside the final edge is D=private(g_{q-1}); its entrance x_D is absent by 512f6864eb96. Since e_D is assigned at v, its opposite terminal D has phi(D)>=phi(v)=p, so the charged endpoint rotation theorem 2e04b9ddaeaf applies.

The first path-edge index containing D is j=q-1. The theorem rotates P_v to
  g_1,...,g_{q-1},e_D,g_p,g_{p-1},...,g_{q+1},
a p-edge path with last vertex
  w=g_q∩g_{q+1}=G.
Therefore phi(G)>=p.

Finally C and D are the opposite terminals of edges assigned to v, so by the assignment rule
  phi(C),phi(D)>=phi(v)=p.
Combining with phi(E),phi(G)>=p proves the four-vertex high-potential packet.