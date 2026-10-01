# The terminal-only D contact forces the outer right joint to top potential

## Statement

Retain the sole surviving one-low odd-boundary state at
  p=phi(v)=2q-3, q>=4,
with
  P=(g_1,...,g_p)
maximum at v and occupied slots A,B,C,D. Let
  h_D={y_D,v,D}
be the rank-(q+1) edge whose sole P-contact
  D=private(g_{q-1})
is terminal-only, as in 512f6864eb96.

Then the charged endpoint rotation at v yields a p-edge path ending at
  G=g_q∩g_{q+1}.
Hence
  phi(G)>=p=2q-3.

Thus the residual state has two adjacent full-potential rotation endpoints
  E=g_{q-1}∩g_q,
  G=g_q∩g_{q+1},
with phi(E),phi(G)>=p.

## Body

Since h_D is assigned to v, its opposite terminal D satisfies
  phi(D)>=phi(v)=p.
Its unique entrance y_D is absent from P, while its sole P-contact is D. Apply the charged endpoint rotation 2e04b9ddaeaf to h_D on P.

The first path edge containing D is
  g_{q-1},
so j=q-1. The rotation theorem gives a p-edge path
  g_1,...,g_{q-1},h_D,g_p,g_{p-1},...,g_{q+1}
ending at
  G=g_q∩g_{q+1}.
Therefore
  phi(G)>=p.

The corresponding conclusion phi(E)>=p from the adjacent low C-terminal contact is fb9dfc3b63b8. Hence both E and G have endpoint potential at least p.
