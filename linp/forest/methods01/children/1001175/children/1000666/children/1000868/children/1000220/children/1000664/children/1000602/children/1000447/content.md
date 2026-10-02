# A clean cross-edge of uniquely intersecting maximum rails must cross the aligned joint

## Statement

Let A and B be maximum endpoint paths of the same length l, ending physically at x_A and x_B, and assume
  V(A) intersect V(B)={y}.
Thus y is an aligned internal joint of the two paths.

Let f be a hyperedge not belonging to A or B such that
  f intersect V(A)={a},
  f intersect V(B)={b},
with a,b distinct from y, and the third vertex of f outside V(A) union V(B).

Then a and b must lie on opposite sides of y in their respective path orders.

Consequently, in the lens-free flat-cycle system of 960a5153b900 and 315871ed0c8b, suppose the outer rails R_{i-1},R_{i+1} intersect. Their intersection is unique; call it z_i. The central cycle edge
  e_i={x_i,t_i,t_{i+1}}
meets R_{i-1} exactly at t_{i+1} and R_{i+1} exactly at t_i. Therefore t_{i+1} and t_i lie on opposite sides of the aligned joint z_i on those two outer rails.

## Body

Split A at a into a far-side subpath A^- ending at a and an endpoint-side subpath A^+ beginning at a and ending physically at x_A. Define B^-,B^+ analogously.

Because A and B have unique common vertex y, if a and b lie on the same side of y then the two complementary concatenations
  A^- , f , B^+
and
  B^- , f , A^+
are both linear: in each concatenation at most one of the two rail pieces contains y, and f meets the two rails only at its intended consecutive contacts.

Let their lengths be L_1,L_2. Splitting a path at an internal vertex never loses edges: the two side lengths sum to at least l (and to l+1 when the split vertex is private to one path edge). Hence
  L_1+L_2
   = (|A^-|+|A^+|)+(|B^-|+|B^+|)+2
   >= 2l+2.
Thus one of L_1,L_2 exceeds l.

But the first concatenation ends physically at x_B and the second ends physically at x_A. Since phi(x_A)=phi(x_B)=l, both lengths must be at most l, a contradiction. Hence a,b lie on opposite sides of y.

For the flat-cycle application, lens-freeness and maximum-rail balance imply that any intersection of R_{i-1},R_{i+1} is unique; otherwise those two equal-length maximum rails contain a balanced elementary lens. By 315871ed0c8b applied to indices i-1 and i+1,
  e_i intersect V(R_{i-1})={t_{i+1}},
  e_i intersect V(R_{i+1})={t_i}.
The rail endpoints and all entrance labels are absent from the other rail, so the third vertex x_i is outside both outer rails. The general cross-edge statement applies and gives the claimed opposite-side orientation.