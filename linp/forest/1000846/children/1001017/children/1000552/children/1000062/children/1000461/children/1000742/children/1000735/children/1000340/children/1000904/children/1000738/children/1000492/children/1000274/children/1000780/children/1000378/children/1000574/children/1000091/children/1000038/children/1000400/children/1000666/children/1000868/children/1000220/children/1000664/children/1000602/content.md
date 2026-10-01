# Disjoint outer rails force consecutive aligned joints into the late half

## Statement

Let A=(a_1,...,a_l), B=(b_1,...,b_l), C=(c_1,...,c_l) be maximum endpoint paths of the same length l, ending physically at x_A,x_B,x_C respectively.

Assume
  V(A) intersect V(B)={y},
  V(B) intersect V(C)={z},
and
  V(A) intersect V(C)=emptyset.
By unique-intersection alignment, write
  y=a_r intersect a_{r+1}=b_r intersect b_{r+1},
  z=b_s intersect b_{s+1}=c_s intersect c_{s+1}.

Then
  min{r,s} >= ceil(l/2).

Applied to the lens-free flat-cycle rail system of 960a5153b900, if R_{i-1} and R_{i+1} are disjoint, then
  min{k_{i-1},k_i} >= ceil((p-2)/2).
Equivalently, whenever one of the two adjacent aligned levels k_{i-1},k_i is earlier than the midpoint, the outer rails R_{i-1},R_{i+1} must intersect.

## Body

Assume without loss of generality that r<=s.

Because A and B meet only at y, B and C meet only at z, and A,C are disjoint, the following concatenation is a linear path:
- traverse A backwards from its physical endpoint x_A to the joint y;
- traverse B from y to z;
- traverse C from z to its physical endpoint x_C.

The first segment has l-r edges, the middle segment has s-r edges, and the last segment has l-s edges. Hence the concatenated path has length
  (l-r)+(s-r)+(l-s)=2l-2r.
Its physical last vertex can be chosen as x_C. Since C is a maximum l-edge endpoint path ending at x_C,
  phi(x_C)=l.
Therefore
  2l-2r <= l,
so
  r>=l/2.
As r is integral,
  r>=ceil(l/2).

If instead s<=r, reverse the roles of A and C to obtain
  s>=ceil(l/2).
Thus
  min{r,s}>=ceil(l/2).

For the flat-cycle application, 960a5153b900 supplies
  V(R_{i-1}) intersect V(R_i)={y_{i-1}}
at aligned level k_{i-1}, and
  V(R_i) intersect V(R_{i+1})={y_i}
at aligned level k_i.
Substitute A=R_{i-1}, B=R_i, C=R_{i+1}, l=p-2. The contrapositive gives the final formulation.
