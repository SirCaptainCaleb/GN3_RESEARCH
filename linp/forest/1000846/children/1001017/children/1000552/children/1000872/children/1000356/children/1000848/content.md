# The 11/12 coefficient only requires a three-quarters bound after subtracting double-contact defect

## Statement

Choose for every vertex v a maximum endpoint path P_v as in the contact-snake framework. Let
  A = number of ascending nonspecial edges,
  S = sum_v phi(v),
  D = total number of double-contact incidences mu_v(e)=2
with respect to the chosen paths.

Then
  3m-A+D <= 2S-n.

Consequently the global estimate
  A-D <= (3/4)S
is sufficient to imply
  m <= (11/12)S - n/3.
In particular, for a P_ell-free linear 3-graph it implies
  m <= ((11ell-15)/12)n.

More locally, assign every ascending edge to a terminal of minimum endpoint potential, and let a(v) be the number assigned to v. If D_v is the number of double-contact incidences at v on P_v, then the pointwise inequalities
  a(v)-D_v <= (3/4)phi(v)
for all v are sufficient. The same conclusion follows from any global charging proof of their sum, even if individual vertices violate the uncorrected charged-degree bound.

## Body

The certified clean-minus-double contact identity 4e165e65be58 gives
  3m-C+D <= 2S-n,
where C is the number of clean incidences.

Every clean incidence is the unique entrance incidence of an ascending nonspecial edge. Each ascending edge has only one entrance, so
  C<=A.
Therefore
  3m-A+D <= 3m-C+D <= 2S-n.                         (1)

If
  A-D <= (3/4)S,
then rearranging (1) gives
  3m <= 2S-n + A-D
      <= (11/4)S-n,
hence
  m <= (11/12)S-n/3.

If H is P_ell-free, phi(v)<=ell-1 for every v, so
  S<=(ell-1)n,
and therefore
  m <= (11/12)(ell-1)n-n/3
    = ((11ell-15)/12)n.

For the local formulation, assign each ascending edge to exactly one of its two terminals having minimum potential (ties arbitrarily). Then
  A=sum_v a(v).
Also
  D=sum_v D_v
for the chosen maximum endpoint paths. Thus summing
  a(v)-D_v <= (3/4)phi(v)
over v yields A-D<=(3/4)S, and the preceding argument applies.
