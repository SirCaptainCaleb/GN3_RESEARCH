# The trapped-negative charge state needs at least two kappa plus five negative vertices

## Statement

Continue in the exceptional two-layer charge state of 76c961f0dc48 and 1ecaca9f1fc7. Put
  a=kappa+2,
  N={v:k_v<0},
  R=sum_{v∈N}(-k_v),
and let S=V(G) be the support of the top-layer matching graph G.

Then
  |N|>=2a+1=2kappa+5.

More quantitatively, for every v∈N with -k_v=r,
  r <= R/(2a)-a.

## Body

Fix v∈N with negative mass r=-k_v. By 76c961f0dc48, the color class corresponding to v is a matching in G of size at least
  a+r
because a=kappa+2.
A matching of that size uses at least
  2(a+r)
distinct vertices of S. Hence
  |S|>=2(a+r).                                       (1)

By 1ecaca9f1fc7,
  R>=a|S|,
so
  |S|<=R/a.                                          (2)

Combining (1) and (2) gives
  2(a+r)<=R/a,
hence
  r<=R/(2a)-a.                                       (3)

Let t=|N|. Summing (3) over all v∈N gives
  R=sum r
   <=t(R/(2a)-a).
If t<=2a, then
  tR/(2a)<=R,
so the right-hand side is at most
  R-ta<R,
a contradiction. Therefore
  t>2a.
Since t is integral,
  |N|=t>=2a+1=2kappa+5.