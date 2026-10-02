# High-rank unobstructed whole chords pack into two endpoint vertex-rank zones

## Statement


Let R be a linear path with endpoints a,b, avoiding a common vertex v. Let F be a family of distinct ascending nonspecial edges
  e={x,v,u}
such that, for every e in F,
- both x and u lie on R;
- e has rank r=phi(e);
- a clean maximum source path S_e ending at x is fixed.

Call e unobstructed on R if S_e does not meet the R-side from u toward the endpoint lying opposite x.

Fix an integer R0. Then the number of unobstructed members of F with rank at least R0 is at most
  max(0,2(phi(a)-R0)+1)
  + max(0,2(phi(b)-R0)+1).

Consequently, every additional rank-at-least-R0 whole chord beyond this endpoint-zone capacity has a clean source rail with a second intersection with R on the side beyond its opposite terminal.


## Body


For an unobstructed edge e of rank r>=R0, apply ed412ed8e3b1. If the endpoint opposite x is a, and t is the number of R-edges from u to a, then
  t<=phi(a)-r<=phi(a)-R0.
Thus u lies in the terminal segment of R consisting of at most D_a=phi(a)-R0 edges next to a. A D_a-edge loose 3-uniform path contains at most 2D_a+1 vertices, so at most max(0,2D_a+1) distinct choices of u are possible on this side.

The same argument for endpoint b gives at most max(0,2D_b+1) choices, where D_b=phi(b)-R0.

Distinct edges of F have distinct opposite terminals u: any two already share v, so sharing u as well would violate linearity. Summing the two endpoint capacities gives the displayed bound.

The final assertion is the contrapositive of this counting bound together with ed412ed8e3b1.
