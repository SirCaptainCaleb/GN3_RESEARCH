# Negative charge at level p pays a fixed branching surcharge

## Statement

Let N_p={v:phi(v)=p,k_v<0} and R_p=sum_{N_p}(-k_v). Then (2p-1)|V_{p+1}| >= 2[(3d-2p+1)|N_p|+R_p]. Thus each negative-charge vertex at level p pays both its charge mass and a fixed surcharge 3d-2p+1 in next-superlevel terminal capacity; the surcharge is large at low potential and falls to kappa+2 at p=ell-2.

## Body


In the exact-density setting of 34747339fa9, fix a potential level p and let
  N_p={v:phi(v)=p and k_v<0},
  R_p=sum_{v∈N_p}(-k_v).

For v∈N_p,
  d_H(v)=3d-k_v>3d,
so the positive-part term in 34747339fa9 is certainly active whenever p<=ell-2; indeed
  d_H(v)-2p+1
  =3d-2p+1-k_v
  =(3d-2p+1)+(-k_v).

Restricting the left side of the level-growth inequality to N_p gives
  (2p-1)|V_{p+1}|
  >= 2 sum_{v∈N_p}(3d-2p+1-k_v)
  =2[(3d-2p+1)|N_p|+R_p].                         (1)

Thus the cost of negative charge at level p has two parts:
- one unit of next-level terminal capacity per charge unit R_p, with factor 2;
- a fixed per-source surcharge 3d-2p+1.

The surcharge decreases linearly with p. At the highest possible negative-charge source level p=ell-2 it equals
  3d-2ell+5=kappa+2,
matching 588537713840. Near the minimum endpoint-potential floor it is of order 2d, so low-level negative charge forces much stronger expansion.

Formula (1) is therefore the natural layerwise input for a charge-amplification iteration: negative charge cannot sit low without rapidly enlarging V_{p+1}; if it is pushed high instead, charge-potential covariance and top-layer terminal capacities become restrictive.
