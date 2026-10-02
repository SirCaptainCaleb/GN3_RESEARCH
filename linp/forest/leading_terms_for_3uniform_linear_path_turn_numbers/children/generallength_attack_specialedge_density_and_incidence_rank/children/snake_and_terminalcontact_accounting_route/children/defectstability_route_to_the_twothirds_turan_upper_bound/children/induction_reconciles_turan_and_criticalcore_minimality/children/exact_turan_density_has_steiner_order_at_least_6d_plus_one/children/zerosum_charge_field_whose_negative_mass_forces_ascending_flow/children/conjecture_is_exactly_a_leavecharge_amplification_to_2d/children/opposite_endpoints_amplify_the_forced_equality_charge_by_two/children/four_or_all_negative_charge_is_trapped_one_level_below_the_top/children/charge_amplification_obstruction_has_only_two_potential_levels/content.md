# A stalled charge amplification obstruction has only two potential levels

## Statement

If max charge is below kappa+4 in an exact-density P_ell-free equality obstruction, then every vertex has endpoint potential ell-2 or ell-1. All negative charge lies in S=L_{ell-2}; every top-layer vertex in T=L_{ell-1} has charge at least kappa; and every ascending edge is an S-to-TT rank-(ell-1) edge.

## Body


Assume the stalled branch of 76c961f0dc48:
  max_v k_v < kappa+4,
where
  kappa=3d-2ell+3.

Since charges are integral,
  max_v k_v <= kappa+3.
Because
  d_H(v)=3d-k_v,
the minimum degree satisfies
  delta(H)>=3d-(kappa+3)
          =3d-(3d-2ell+3)-3
          =2ell-6.

Apply the certified endpoint-potential floor 6a4d9b21f0c3:
  phi(v)>=ceil((delta(H)+1)/2)
        >=ceil((2ell-5)/2)
        =ell-2
for every vertex v.

Since H is P_ell-free,
  phi(v)<=ell-1
for every v. Therefore
  V(H)=S disjoint_union T,
where
  S={v:phi(v)=ell-2},
  T={v:phi(v)=ell-1}.

By 76c961f0dc48, every negative-charge vertex lies in S. Every u∈T is a global-maximum endpoint and hence
  d_H(u)<=2ell-3,
so
  k_u=3d-d_H(u)>=3d-2ell+3=kappa.

Thus the stalled amplification state is genuinely two-level:
- all negative charge is confined to S;
- all top-layer vertices T have positive charge at least kappa;
- all ascending edges are sourced in S and have rank ell-1 with both terminals in T;
- no vertex has endpoint potential below ell-2.
