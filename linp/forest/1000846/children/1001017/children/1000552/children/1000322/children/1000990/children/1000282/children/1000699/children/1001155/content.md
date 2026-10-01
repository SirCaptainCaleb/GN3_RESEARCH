# Exact density forces at least 4d minus one above-threshold vertices

## Statement

If a linear 3-graph H satisfies |E(H)|=d|V(H)| and minimum degree at least d+1, then at least 4d-1 vertices have degree at least d+2. Consequently every q-edge path omits at least 4d-2q-2 such vertices; for q<=ell-1 this recovers the lower bound 4d-2ell from a05f009dfcef.

## Body


Let H be an n-vertex linear 3-uniform hypergraph with
  |E(H)|=dn
and minimum degree at least d+1. Put
  R={v:d_H(v)>=d+2}
and r=|R|.

The total degree excess above the threshold d+1 is
  E:=sum_v(d_H(v)-(d+1))
    =3dn-(d+1)n
    =(2d-1)n.

Vertices outside R contribute zero to E. By linearity,
  d_H(v)<= (n-1)/2
for every v, so each v∈R contributes at most
  (n-1)/2-(d+1)
  =(n-2d-3)/2.
Hence
  (2d-1)n
  <= r(n-2d-3)/2,
so
  r >= 2(2d-1)n/(n-2d-3).                         (1)

Since n-2d-3<n, the right side of (1) is strictly larger than
  2(2d-1)=4d-2.
Therefore, whenever such a graph exists,
  r>=4d-1.                                          (2)

Now let P be any q-edge path. It contains exactly 2q+1 vertices, so
  |R\V(P)| >= r-(2q+1)
            >= 4d-2q-2.                             (3)

If q<=ell-1, then
  |R\V(P)| >= 4d-2ell.
This recovers a05f009dfcef immediately.

Thus the pathwise omitted-packet theorem is a corollary of a stronger global statement: exact density with minimum degree d+1 forces at least 4d-1 vertices of degree at least d+2.
