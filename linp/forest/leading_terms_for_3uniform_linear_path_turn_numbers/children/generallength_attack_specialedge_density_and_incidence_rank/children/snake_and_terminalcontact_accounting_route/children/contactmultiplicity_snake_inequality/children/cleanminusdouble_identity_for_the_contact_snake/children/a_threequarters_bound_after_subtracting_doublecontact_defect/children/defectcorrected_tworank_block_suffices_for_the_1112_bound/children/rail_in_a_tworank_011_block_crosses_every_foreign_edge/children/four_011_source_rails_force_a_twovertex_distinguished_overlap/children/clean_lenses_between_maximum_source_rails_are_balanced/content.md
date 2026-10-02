# Clean lenses between maximum source rails are balanced

## Statement

Let Q,R be maximum endpoint paths ending at x,y. If two common vertices bound a clean lens whose two alternative segments are internal to both rails, then the two segments have equal edge length: replacing a shorter segment by the longer one would create a path ending at the same source longer than its endpoint potential. If a source endpoint lies on the lens, the corresponding endpoint-preserving replacement still gives the appropriate one-sided segment inequality.

## Body

Let Q and R be linear hypergraph paths ending at vertices x and y, with
  |Q|=phi(x), |R|=phi(y).

Let a,b be two common vertices. Suppose the Q-subpath Q[a,b] and R-subpath R[a,b] form a clean lens: each has endpoints a,b, their interiors are vertex-disjoint from the other full path, and replacing either one by the other preserves a linear path whenever the distinguished endpoint of the host path lies outside the replaced segment.

Write
  s_Q=|Q[a,b]|, s_R=|R[a,b]|.

If x lies outside the interior of Q[a,b], and replacing Q[a,b] by R[a,b] preserves a path ending at x, maximality of Q gives
  s_R<=s_Q.
Indeed the replacement has length
  |Q|-s_Q+s_R
and still ends at x, so it cannot exceed phi(x)=|Q|.

Likewise, if y lies outside the R-segment in the corresponding sense,
  s_Q<=s_R.

Therefore, when the lens is internal to both maximum endpoint paths,
  s_Q=s_R.

If exactly one of the source endpoints x,y lies on the lens boundary/segment so that only one replacement is endpoint-preserving, the corresponding one-sided inequality survives.

Thus every clean elementary lens between two source-clean maximum rails is balanced unless one of the source endpoints participates in the lens; endpoint lenses are oriented by a definite segment-length inequality.