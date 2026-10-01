# Fractional tight-path covers round with less than one unit of loss

## Statement

Let tau*(H) be the minimum total weight of a fractional cover of V(H) by supports of tight paths. Then pc(H) <= ceil(tau*(H)) for every finite boundary tournament H.

## Body

Unproved rounding conjecture, intended as a companion to astraidea001 rather than a consequence of it. A fractional cover assigns nonnegative weights a_P to tight paths with sum_{P containing v} a_P>=1 at each vertex. The proposed rounding would turn tau*<=2 into the grand two-cover theorem. Generic set systems do not have this property; the entire burden is to exploit reversal antisymmetry and path splicing. Possible attack: choose an optimal fractional solution with extremal overlap structure; uncross two overlapping path supports using their actual orders, preserving enough fractional coverage. Arbitrary restrictions of a tight path need not be tight, so ordinary matroid or set-cover uncrossing cannot simply be imported. Main risk: an integrality gap may exist even at tau*<2 while pc=2, in which case the ceiling inequality still survives; a genuine refutation needs pc>ceil(tau*). No such gap analysis has been done.