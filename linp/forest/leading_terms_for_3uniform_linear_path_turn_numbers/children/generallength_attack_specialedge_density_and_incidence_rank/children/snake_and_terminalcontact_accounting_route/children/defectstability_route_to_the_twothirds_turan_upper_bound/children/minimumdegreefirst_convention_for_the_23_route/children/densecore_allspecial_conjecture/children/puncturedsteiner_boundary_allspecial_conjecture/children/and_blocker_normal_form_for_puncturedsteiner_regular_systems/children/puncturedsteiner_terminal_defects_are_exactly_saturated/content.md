# Punctured-Steiner terminal defects are exactly saturated

## Statement

In the setting of efe44a01f2dc, let P be a maximum d-edge path ending in a nonspecial maximum-rank edge e, let p be the number of alternating path components in the union of the two terminal double-blocker matchings, and for v in {y,z} let S_v,U_v denote respectively the numbers of single blockers and unused precursor vertices in the terminal defect accounting. Then p∈{1,2} and
S_y+S_z=p,
U_y+U_z=p.
More precisely:
- if p=1, one terminal has (B,S,U)=(d-1,0,0) and the other has (d-2,1,1);
- if p=2, both terminals have (B,S,U)=(d-2,1,1).

## Body

The universal residual/blocker theorem efe44a01f2dc gives p∈{1,2}.

Apply the certified terminal defect accounting identity 437f531f4ad8:
d_H(y)+d_H(z)=2L+S_y+S_z-p.
Here H is d-regular and L=d, so
2d=2d+S_y+S_z-p,
hence
S_y+S_z=p.

The same theorem gives
S_y+S_z+U_y+U_z=2p.
Substituting S_y+S_z=p yields
U_y+U_z=p.

For the pointwise refinement, use
d_H(v)=1+B_v+S_v.
If B_v=d-1, then d=1+(d-1)+S_v, so S_v=0. The local defect identity
2d-2-2B_v=S_v+U_v
then gives U_v=0.

If B_v=d-2, then d=1+(d-2)+S_v, so S_v=1, and the same local identity gives
2=S_v+U_v,
hence U_v=1.

Therefore the p=1 case has one perfect terminal with no defects and one deficient terminal with exactly one single blocker and one unused precursor vertex; the p=2 case has exactly one single blocker and one unused precursor vertex at each terminal.

Thus every open alternating path component is globally saturated: there is exactly one single-blocker defect and exactly one unused defect per open component, with no extra slack anywhere.