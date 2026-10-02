# Punctured-Steiner maximum-rank obstructions have one of two saturated defect topologies

## Statement

Under the hypotheses of efe44a01f2dc, a hypothetical maximum-rank nonspecial edge e has exactly one of two saturated defect topologies.

(A) One-chain case: one terminal has a perfect double-blocker matching on W, while the other terminal has exactly one single blocker {v,o,w} and exactly one unused precursor vertex u; the unique alternating path component of M_y∪M_z joins w to u.

(B) Two-chain case: each terminal v∈{y,z} has exactly one single blocker {v,o,w_v} using the unique outside vertex o and exactly one unused precursor vertex u_v. The two single blockers intersect at o, so together with e they form a linear 3-cycle. The union M_y∪M_z has exactly two alternating path components, whose endpoint defects are drawn from {w_y,u_y,w_z,u_z}.

## Body

This is the pointwise content of efe44a01f2dc and ffbd337476d6.

In the p=1 case, one terminal has B=d-1 and hence (S,U)=(0,0), while the other has B=d-2 and hence (S,U)=(1,1). For the deficient terminal v, let {v,o,w} be its unique single blocker and let u be its unique precursor vertex unused by the v-star. The double-blocker matching M_v is unmatched exactly at w and u, while the other terminal matching is perfect. Therefore the unique degree-one vertices of M_y∪M_z are w and u, so its unique alternating path component joins them.

In the p=2 case, both terminals have B=d-2 and (S,U)=(1,1). Since there is a unique vertex o outside the maximum path P, each single blocker necessarily uses o:
f_y={y,o,w_y},  f_z={z,o,w_z}.
Linearity implies w_y≠w_z. The two single blockers intersect exactly at o, while f_y∩e={y} and f_z∩e={z}; hence
f_y,e,f_z
is a linear 3-cycle.

For each terminal v, its double-blocker matching is unmatched exactly at the blocker contact w_v and the unique unused precursor u_v. Therefore the degree-one/isolated defects of M_y∪M_z are exactly the symmetric-difference/intersection pattern of
{w_y,u_y} and {w_z,u_z},
and there are exactly two alternating path components counting isolates.

Thus every hypothetical nonspecial maximum-rank edge in the punctured-Steiner boundary family has one of only two global defect topologies: one open alternating chain, or two open chains attached to a canonical terminal triangle.