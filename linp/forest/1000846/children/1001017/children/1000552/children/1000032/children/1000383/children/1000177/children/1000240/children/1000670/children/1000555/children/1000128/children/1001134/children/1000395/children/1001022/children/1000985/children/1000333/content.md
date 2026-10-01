# Adjacent R-contacts either pay length deficit or saturate the Q-segment with common vertices

## Statement

Let R be a maximum endpoint path ending at y, and among all maximum endpoint paths ending at x let Q maximize |V(Q) intersect V(R)|. Let a,b be two internal common vertices that are consecutive on R in the strong sense that the R-subpath R[a,b] meets Q only at a and b. Put
  s=|R[a,b]|,  d=|Q[a,b]|.
Then d>=s. Moreover, if d=s, every vertex of Q[a,b] other than a,b belongs to R. Equivalently, the Q-side of every zero-length-deficit adjacent R-contact interval is completely saturated by common vertices.

## Body

Because R[a,b] meets Q only at its boundary vertices, replacing the internal Q-segment Q[a,b] by R[a,b] gives a linear path Q' ending at the same last vertex x. Its length is
  |Q'|=|Q|-d+s.
Since Q is maximum at x, s<=d.

Assume now that s=d. Then Q' is again maximum at x. An s-edge linear 3-uniform path has 2s+1 vertices. Since R[a,b] meets Q only at a,b, all
  2s-1
other vertices of R[a,b] are new R-vertices gained by Q'. On the other hand the removed Q[a,b] has exactly 2s-1 vertices other than a,b, so at most 2s-1 vertices of V(Q) intersect V(R) can be lost in the replacement.

If even one internal vertex of Q[a,b] were absent from R, the switch would lose at most 2s-2 common vertices while gaining 2s-1 new R-vertices. Hence
  |V(Q') intersect V(R)|>|V(Q) intersect V(R)|,
contradicting the overlap-maximal choice of Q. Therefore all 2s-1 internal vertices of Q[a,b] lie on R.

Thus an adjacent R-contact interval has either strict integer length deficit d-s>=1, or equality together with complete common-vertex saturation of its Q-side.
