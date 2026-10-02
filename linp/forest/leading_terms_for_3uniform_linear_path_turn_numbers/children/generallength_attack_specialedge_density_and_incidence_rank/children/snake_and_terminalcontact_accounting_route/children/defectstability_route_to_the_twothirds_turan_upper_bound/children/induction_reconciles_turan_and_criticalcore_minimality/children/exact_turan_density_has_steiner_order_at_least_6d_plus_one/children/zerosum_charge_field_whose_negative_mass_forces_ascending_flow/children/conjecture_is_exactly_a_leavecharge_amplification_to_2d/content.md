# The equality-layer conjecture is exactly a leave-charge amplification to 2d

## Statement

In the exact-density charge coordinates k_v=(d_U(v)-s)/2, one has d_H(v)=3d-k_v. Hence the equality-layer conclusion d_H(v)<=d is exactly k_v>=2d. A counterexample has k_v<=2d-1 for every vertex, sum k_v=0, a forced positive spike kappa=3d-2ell+3 in {3,1,2}, and every negative charge -r sources at least kappa+r+2 ascending edges. Thus the grand equality step is precisely a charge-amplification problem from kappa to 2d, with ascending flow as the amplification mechanism.

## Body


Retain the exact-density charge coordinates of 588537713840:
  k_v=(d_U(v)-s)/2,
so
  sum_v k_v=0
and
  d_H(v)=3d-k_v.

The equality-layer assertion E_ell asks:

Every P_ell-free exact-density linear triple system containing a nonspecial edge has a vertex of degree at most d.

In charge coordinates,
  d_H(v)<=d
if and only if
  3d-k_v<=d,
if and only if
  k_v>=2d.

Therefore E_ell is exactly equivalent to the charge-amplification statement:

Every P_ell-free exact-density system in the relevant nonspecial class has
  max_v k_v>=2d.                                    (1)

Conversely, a counterexample to E_ell has minimum degree at least d+1, hence
  3d-k_v>=d+1
for every v, equivalently
  k_v<=2d-1                                         (2)
for every v.

Together with 588537713840, any counterexample therefore has the following purely numerical/flow skeleton:
- k_v∈Z and sum_v k_v=0;
- max_v k_v lies in [kappa,2d-1], where
    kappa=3d-2ell+3∈{3,1,2};
- each negative-charge vertex k_v=-r has phi(v)<=ell-2 and is the source of at least
    kappa+r+2
  ascending nonspecial edges.

Thus the grand equality problem can be attacked as a charge-amplification theorem: starting from the forced seed spike kappa, show that either the ascending flow created by the compensating negative mass yields P_ell, or the leave-degree distribution develops a larger positive charge; iterate until charge 2d appears, which is exactly a degree-at-most-d vertex.

No additional loss occurs in this reformulation.
