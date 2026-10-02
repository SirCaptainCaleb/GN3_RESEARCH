# A whole ascending chord spans at most rank minus one path edges

## Statement

Let e={x,v,u} be an ascending nonspecial edge of rank r, and let R be any linear path avoiding v that contains both x and u. Let R[x,u] denote the unique path segment between x and u, with d(e;R) edges.

Then
  e union R[x,u]
is a linear cycle of length d(e;R)+1. Consequently
  d(e;R) <= r-1.

In particular, if e is a whole chord on a canonical common-anchor precursor R, its two distinguished endpoints x,u lie at anchor distance at most phi(e)-1.

## Body

Because R avoids v and e={x,v,u}, the only vertices of e lying on R are x and u. Take the minimal R-segment joining x to u, denoted R[x,u]. Its open vertex set contains neither x nor u and is disjoint from e. The two boundary path edges meet e at x and u respectively, and no other path edge of the segment meets e.

Thus adjoining e to R[x,u] closes a linear cycle. Its length is d(e;R)+1.

Since e is nonspecial of rank r, the certified cycle-rank theorem f2925a904b8e implies that every linear cycle containing e has length at most r. Hence
  d(e;R)+1<=r,
so d(e;R)<=r-1.

No source-clean, terminal-single, payment, endpoint-potential, or common-terminal assumption beyond the displayed whole-chord geometry is required.