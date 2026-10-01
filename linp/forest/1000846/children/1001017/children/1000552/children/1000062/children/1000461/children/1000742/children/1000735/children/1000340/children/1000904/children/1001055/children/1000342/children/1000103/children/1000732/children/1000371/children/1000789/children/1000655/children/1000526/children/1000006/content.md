# Rank windows remove the high-triangle collapse in the source-mass frontier

## Statement

In the setup of 98152151c212, with s interior switchers and D doubly occupied cells,
  sum_{f in F} phi(x_f)
  >= (p/2)s + max{ floor((s-D)^2/4), s(s-1)/8 }.
Hence triangle concentration cannot reduce the quadratic source term below s(s-1)/8. For a low-defect switching family with s=(5/8-o(1))p,
  sum_{f in F} phi(x_f) >= (185/512-o(1))p^2,
uniformly in D.
More precisely the cell-dispersion term dominates while D <= (1-1/sqrt(2))s+O(1), and the rank-window term dominates beyond that threshold.

## Body

The certified cell-dispersion theorem 98152151c212 gives
  M:=sum_{f in F}phi(x_f) >= (p/2)s + floor((s-D)^2/4).
The common-terminal rank-window lemma 75fdc99c76a8, applied to the same family, gives independently
  M >= (p/2)s + s(s-1)/8.
Taking the larger lower bound proves the envelope.

The two quadratic bonuses cross asymptotically when
  (s-D)^2/4 = s^2/8,
i.e.
  D=(1-1/sqrt(2))s.
Thus the older dispersion estimate controls the low-double regime, while the new rank-window estimate prevents the high-double regime from collapsing.

At low defect, s=(5/8-o(1))p, so the rank-window side alone yields
  M >= (5/16)p^2 + (25/512)p^2 - o(p^2)
    = (185/512-o(1))p^2.
This removes switcher-triangle density D as a mechanism for lowering source-rank mass below that coefficient.
