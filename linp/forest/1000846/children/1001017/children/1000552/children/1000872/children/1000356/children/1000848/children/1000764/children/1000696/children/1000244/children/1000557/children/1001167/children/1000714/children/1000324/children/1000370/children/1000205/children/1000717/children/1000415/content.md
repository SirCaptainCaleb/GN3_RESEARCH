# The final odd-boundary residue manufactures a high-rank central edge

## Statement

In the final one-low odd-boundary 0-1-1 residue, let
  p=2q-3
and let g_q be the central path edge with vertices
  E=g_{q-1}∩g_q,
  F=private(g_q),
  G=g_q∩g_{q+1}.

Then
  phi(g_q)>=p,
and
  phi(E),phi(F),phi(G)>=p.

Thus the residue produces an edge of rank at least the terminal potential p whose entire vertex set also has endpoint potential at least p, despite the four offending assigned edges having ranks only q and q+1.

## Body

By the C-terminal charged rotation used in fb9dfc3b63b8 and a3ea758efa27, the sequence
  g_1,...,g_{q-2},e_C,g_p,g_{p-1},...,g_q
is a linear path of exactly p edges and has last edge g_q.
Therefore, by definition of edge rank,
  phi(g_q)>=p.

The endpoint-potential bounds
  phi(E),phi(F),phi(G)>=p
are exactly a3ea758efa27: E and F are physical last vertices of this p-edge path, while G is a physical last vertex of the adjacent D-terminal rotation.

Hence both the edge g_q and all three of its vertices have potential at least p.
