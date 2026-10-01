# The final odd-boundary residue forces the entire central edge to top potential

## Statement

In the final one-low odd-boundary 0-1-1 residue with
  p=2q-3,
  P=(g_1,...,g_p),
let
  E=g_{q-1}∩g_q,
  F=the private vertex of g_q,
  G=g_q∩g_{q+1}.

Then
  phi(E),phi(F),phi(G) >= p.
Hence every vertex of the central path edge g_q has endpoint potential at least p.

## Body

Use the charged rotation of the low terminal-only edge e_C from fb9dfc3b63b8. It produces the p-edge path
  P_C=(g_1,...,g_{q-2},e_C,g_p,g_{p-1},...,g_q).
The last edge is g_q and its predecessor is g_{q+1}, meeting g_q at G.

The two other vertices of g_q are E and F. The joint E belonged in the original path only to g_{q-1},g_q, and g_{q-1} is omitted from P_C; it is not in e_C by linearity/labels. Thus E occurs only in the final edge of P_C and is a last vertex, giving phi(E)>=p, as already recorded.

The private vertex F occurs only in g_q on the original path. It is not in e_C: the latter consists of its absent entrance x_C, the common terminal v, and C, whereas F lies on P and is distinct from v,C. Hence F also occurs only in the final edge g_q of P_C. Since the predecessor meets g_q at G, F is likewise a last vertex. Therefore phi(F)>=p.

Finally phi(G)>=p follows from the adjacent D-terminal charged rotation 7f982be42601 / 2de359bc02f1.

Thus all three vertices E,F,G of g_q have potential at least p.