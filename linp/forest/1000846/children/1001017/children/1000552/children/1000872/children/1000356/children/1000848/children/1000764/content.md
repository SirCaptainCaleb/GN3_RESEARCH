# A defect-corrected consecutive-rank block is sufficient for the 11/12 bound

## Statement

Fix, for every vertex v with p=phi(v), a maximum endpoint path P_v. For a charged ascending edge e={x,v,u} assigned to v (so phi(u)>=p), call e double at v if both x and u lie on P_v.

For each rank r let
  n_r(v)=number of assigned charged edges of rank r,
  d_r(v)=number of those edges that are double at v.

Suppose that for every v and every consecutive rank pair {q,q+1},
  [n_q(v)-d_q(v)] + [n_{q+1}(v)-d_{q+1}(v)] <= 3.   (*)

Then the same consecutive-level pairing used in 2665d2c81d39 gives
  a(v)-D_v <= (3/4)phi(v)
after the same bottom-level residue corrections, where
  a(v)=sum_r n_r(v)
and D_v is the total double-contact incidence count at v.

Consequently
  A-D <= (3/4)sum_v phi(v),
and hence
  m <= (11/12)sum_v phi(v)-n/3
by bed2a5868628.

Even the corresponding +1 residue fallback suffices for leading coefficient 11/12.

## Body

For fixed v, every assigned ascending edge is potential-charged at v, so its rank lies in the certified charged window
  L=ceil((p+2)/2) <= r <= p.

Put
  b_r=n_r-d_r.
Then
  a(v)-sum_r d_r = sum_r b_r.
Since D_v counts all double incidences at v, not merely assigned ascending doubles,
  a(v)-D_v <= sum_r b_r.                              (1)

Assume (*) for every consecutive pair. Pair the admissible rank levels exactly as in 2665d2c81d39. Each two-level block contributes at most 3 to sum b_r.

For p congruent to 0 or 1 modulo 4, the admissible rank window has even size, so the paired total is at most floor(3p/4).

For p congruent to 2 modulo 4, leave the bottom rank L unpaired. The central-window bound used in 2665d2c81d39 gives n_L<=1, hence b_L<=1, and pairing the remaining levels gives floor(3p/4).

For p congruent to 3 modulo 4, the odd-central-window bound gives n_L<=2, hence b_L<=2, and pairing the rest gives floor(3p/4).

Thus
  sum_r b_r<=floor(3p/4)<=3p/4.
Together with (1),
  a(v)-D_v<=3p/4.

Summing over v gives
  A-D <= (3/4)sum_v phi(v),
because every ascending edge is assigned once while D=sum_v D_v. The conclusion is then exactly bed2a5868628.

If one omits the final odd-residue sharpening and uses the older +1 fallback, the same algebra gives only an additive O(n) error but retains leading coefficient 11/12.
