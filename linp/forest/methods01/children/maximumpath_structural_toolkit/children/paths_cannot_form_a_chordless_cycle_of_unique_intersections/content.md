# Four equal-length maximum paths cannot form a chordless cycle of unique intersections

## Statement

Let A,B,C,D be maximum endpoint paths of the same length L. Suppose
  |V(A) intersect V(B)|=|V(B) intersect V(C)|=|V(C) intersect V(D)|=|V(D) intersect V(A)|=1,
while
  V(A) intersect V(C)=V(B) intersect V(D)=emptyset.
Then no such four paths exist.

## Body

By 5854d853a44b, write the four unique consecutive intersections as aligned joints at levels
  a for A-B, b for B-C, c for C-D, d for D-A.

The four joint vertices are distinct. For example, the A-B and B-C joints cannot coincide because that common vertex would lie in A intersect C, which is empty. Hence adjacent levels are distinct: on any one path, two distinct joints cannot occur between the same consecutive edge pair.

Consider A. Its segment between the A-B and A-D joints has |d-a| edges. The alternative route from the A-B joint to the A-D joint obtained by following B to the B-C joint, then C to the C-D joint, then D to the A-D joint has
  |b-a|+|c-b|+|d-c|
edges. The hypotheses on pairwise intersections make this alternative route internally disjoint from the remainder of A and internally linear: consecutive constituent paths meet only at the displayed joints and the nonconsecutive pairs are disjoint. Replacing the A-segment by this route therefore gives a path with the same last vertex as A. Maximality of A gives
  |b-a|+|c-b|+|d-c| <= |d-a|.
The reverse inequality is the triangle inequality, so equality holds. Equality in the real-line triangle inequality implies that a,b,c,d occur monotonically in this order. Because adjacent levels are distinct, the monotonicity is strict.

Now make the analogous replacement on B. The B-segment between levels a and b can be replaced by the route through A,D,C, giving
  |d-a|+|c-d|+|b-c| <= |b-a|.
Again equality must hold, so a,d,c,b must occur monotonically in this order.

But a,b,c,d are strictly monotone. Reversing all inequalities if necessary, suppose a<b<c<d. Then a,d,c,b is neither nondecreasing nor nonincreasing, contradicting the equality condition for the second replacement. Thus the assumed four-path configuration is impossible.