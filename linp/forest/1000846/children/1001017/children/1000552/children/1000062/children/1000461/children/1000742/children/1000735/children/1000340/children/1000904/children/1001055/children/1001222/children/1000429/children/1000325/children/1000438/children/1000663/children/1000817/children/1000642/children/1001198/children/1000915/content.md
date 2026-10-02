# Long nested balanced lenses must intersect off the host

## Statement

Let P be a globally longest L-edge linear path. Let two clean balanced endpoint lenses on P have nested host intervals
  [a,d] and [b,c]
in the order a<b<c<d along P. Let A be the off-host side joining a to d and B the off-host side joining b to c. Assume A and B are internally vertex-disjoint. If T=|P[a,d]| is the outer host-side length, then
  2T <= L+1.
Equivalently,
  T <= floor((L+1)/2).

Consequently, if two balanced endpoint lenses on a globally longest host path have nested host intervals and the outer interval has length greater than (L+1)/2, then their off-host sides must intersect.

## Body

Write
  alpha=|P[a,b]|,
  t=|P[b,c]|,
  delta=|P[c,d]|.
Then the outer host interval has length
  T=alpha+t+delta.
Because the lenses are balanced,
  |A|=T
and
  |B|=t.

Assume A and B are internally vertex-disjoint. Cleanliness gives that the interior of each off-host side is disjoint from P. Therefore the concatenation
  A[a,d], reverse(P[d,c]), reverse(B[b,c]), reverse(P[b,a])
is a linear cycle: consecutive pieces meet at d,c,b,a respectively, and all nonconsecutive intersections are excluded by cleanliness together with the assumed internal disjointness of A and B.

Its length is
  |A|+|P[c,d]|+|B|+|P[a,b]|
  =T+delta+t+alpha
  =2T.

Deleting any one edge from a linear cycle of length 2T leaves a linear path of length 2T-1. Since L is the global maximum path length,
  2T-1<=L.
Hence
  2T<=L+1,
which proves the claim.