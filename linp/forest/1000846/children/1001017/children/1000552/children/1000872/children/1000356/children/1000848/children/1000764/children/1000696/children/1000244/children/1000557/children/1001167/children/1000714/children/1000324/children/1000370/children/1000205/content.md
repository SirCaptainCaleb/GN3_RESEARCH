# The final odd-boundary residue forces two successive top-potential rotated endpoints

## Statement

In the surviving one-low odd-boundary 0-1-1 state, retain
  p=phi(v)=2q-3,
  P=(g_1,...,g_p),
with the low rank-q edge e_C terminal-only at
  C=g_{q-2}∩g_{q-1},
and the rank-(q+1) high edge h_D terminal-only at
  D=private(g_{q-1}).

Put
  E=g_{q-1}∩g_q,
  G=g_q∩g_{q+1}.

Then
  phi(E)>=p
and
  phi(G)>=p.

More precisely, the charged endpoint rotations of e_C and h_D on P produce p-edge paths ending at E and G respectively.

## Body

The E conclusion is fb9dfc3b63b8: e_C has entrance absent from P and opposite terminal C first occurring on g_{q-2}. Applying the charged endpoint rotation gives
  g_1,...,g_{q-2},e_C,g_p,g_{p-1},...,g_q,
a p-edge path ending at
  E=g_{q-1}∩g_q.
Hence phi(E)>=p.

For h_D, write h_D={y_D,v,D}, where y_D is its absent unique entrance and D is the opposite terminal. Since h_D is assigned to v, phi(D)>=phi(v)=p, so h_D is potential-charged at v. Its sole P-contact D is private to g_{q-1}, hence its first occurrence index is j=q-1.

Apply the same charged endpoint rotation 2e04b9ddaeaf. It yields
  g_1,...,g_{q-1},h_D,g_p,g_{p-1},...,g_{q+1}.
This is a p-edge linear path. The rotation theorem identifies the final vertex
  g_q∩g_{q+1}=G,
so phi(G)>=p.

Thus the two adjacent terminal-only contacts C,D generate successive high-potential rotated endpoints E,G on the far side of the omitted central edge g_q.