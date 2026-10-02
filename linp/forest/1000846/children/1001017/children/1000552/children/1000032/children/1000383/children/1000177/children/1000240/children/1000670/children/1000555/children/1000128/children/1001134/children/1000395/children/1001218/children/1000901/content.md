# Two separated endpoint lenses from one source rail are at most half-rank

## Statement

Let S be a maximum (r-1)-edge path ending at x, so phi(x)=r-1. Let Q and R be maximum endpoint paths containing x. Suppose z_Q,x and z_R,x bound clean balanced endpoint lenses between S,Q and S,R respectively, chosen on the x-side of S, with side lengths t_Q and t_R.

Assume the two host-side lens paths Q[z_Q,x] and R[z_R,x] meet each other only at x. Then
  max{t_Q,t_R} <= r/2.
Equivalently, if either source endpoint lens has length greater than r/2, the Q- and R-host sides must have a second common vertex away from x.

In the whole-pair braid, where S is a canonical source rail for an ascending rank-r edge with entrance x, every source lens longer than half the parent rank therefore forces additional local overlap between the two lens-free host rails.

## Body

The two lens sides on S are terminal segments ending at x, hence are nested. Relabel Q,R if necessary so that t_R>=t_Q. Then z_Q lies on the S-segment from z_R to x, and
  |S[z_R,z_Q]|=t_R-t_Q.

By cleanliness of the two endpoint lenses, the interiors of Q[z_Q,x] and R[z_R,x] avoid S. By hypothesis these two host sides are internally disjoint from each other. Therefore
  S[z_R,z_Q], Q[z_Q,x], reverse(R[z_R,x])
is a linear cycle. Its length is
  (t_R-t_Q)+t_Q+t_R=2t_R.

Delete from this cycle either edge incident with x. The remaining 2t_R-1 edges form a linear path with last vertex x. Since phi(x)=r-1,
  2t_R-1<=r-1,
so 2t_R<=r. This proves t_R=max{t_Q,t_R}<=r/2.

The contrapositive gives the final assertion: if one lens is longer than r/2, the two host-side paths cannot meet only at x and hence have another common vertex.