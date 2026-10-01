# Failure of kappa-plus-four amplification forces many full-rank single blockers at one top vertex

## Statement

Continue in the trapped-negative exceptional state and assume
  max_v k_v <= kappa+3.
Then there exists a top-layer vertex u with
  phi(u)=ell-1
and graph degree
  d_G(u)>=2kappa+5
as in 2fdc43803de8.

Choose any G-edge h incident with u and a longest
  p=(ell-1)-edge
path P ending in h with physical last vertex u. Let B_P(u) count incident terminal edges f!=h for which both vertices of f\{u} lie in V(P)\h.

Then
  B_P(u)<=3.

Consequently, among the other G-edges incident with u, at least
  d_G(u)-1-3 >= 2kappa+1
have exactly one of their two non-u vertices on V(P)\h. In particular there are at least 3,5,7 such full-rank equal-potential single blockers in the three residue classes kappa=1,2,3.

## Body

Put p=ell-1. Since P is globally longest and ends at u, the certified exact terminal-degree/double-blocker inequality db94e08d513d gives
  d_H(u)+B_P(u)<=2p-1=2ell-3.

In charge coordinates,
  d_H(u)=3d-k_u
and
  2ell-3=3d-kappa.
Therefore
  B_P(u)
  <=(3d-kappa)-(3d-k_u)
  =k_u-kappa
  <=3.

Now every G-edge f incident with u is a rank-p nonspecial edge for which u is terminal. By terminal adjacency/blocking, any f!=h must meet P in at least one vertex besides u; otherwise appending f to P gives a (p+1)-edge path.

If both non-u vertices of f lie on P\h, then f is counted by B_P(u). There are at most three such edges. Every remaining G-edge f!=h therefore has exactly one of its two non-u vertices on P\h.

There are at least
  d_G(u)-1-B_P(u)
  >=(2kappa+5)-1-3
  =2kappa+1
such edges.
