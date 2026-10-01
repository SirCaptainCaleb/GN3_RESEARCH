# General upper bound improved to (ell-13/6)n

## Statement

For every ell>=6, every n-vertex linear 3-uniform hypergraph with no linear P_ell satisfies
  |E(H)| <= (ell-13/6)|V(H)|.
Equivalently,
  ex_L(n,P_ell^(3)) <= (ell-13/6)n.
This improves the certified (ell-2)n general bound by n/6.

## Body

Suppose for contradiction that H is a P_ell-free linear triple system with
  m>(ell-13/6)n,
chosen with n minimum.

By the standard minimum-degree reduction fc68ffc8e4ea,
  delta(H)>ell-13/6.
For ell>=6 this gives delta(H)>=4.

The certified minimum-degree endpoint-potential floor 6a4d9b21f0c3 then gives, for every vertex v,
  phi(v)>=ceil((delta(H)+1)/2)>=3.

Therefore the dense potential theorem 7cae1cb001ac applies:
  (1/n)sum_v phi(v) >= m/n+7/6.

Since H is P_ell-free, every endpoint potential is at most ell-1. Hence
  ell-1 >= (1/n)sum_v phi(v)
          >= m/n+7/6
          > (ell-13/6)+7/6
          = ell-1,
a contradiction.

Thus m<=(ell-13/6)n for ell>=6.
