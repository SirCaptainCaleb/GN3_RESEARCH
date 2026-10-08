# The pure size-three curvature tube has an explicit spanning one-change escape — preserved pre-item development

Work in the pure-orientation ternary sector h=alpha. Let P=(f_1,...,f_m) be a sigma-monochromatic path and suppose its entire omitted set is U={a,b,c}. Put tau=1-sigma. Assume U is a tau-front circuit at (f_1,f_2), with persistent directed pair cycle a->b->c->a. The propagation theorem gives, for every relevant j,
alpha(a,b,f_j)=alpha(b,c,f_j)=alpha(c,a,f_j)=tau,
and
alpha(u,f_j,f_{j+1})=tau for every u in U.
Reverse edges of the U-cycle therefore have color sigma against every pivot f_j.

Then the size-three whole-front branch closes explicitly.

For m>=4 consider
H=(f_m,f_{m-1},...,f_3,a,c,f_2,f_1,b).
Every status wholly inside the reversed P-segment has color tau, because reversing a sigma-tight path complements all ternary statuses.

At the splice and thereafter:
(1) alpha(f_4,f_3,a)=sigma, since it is the reversal of alpha(a,f_3,f_4)=tau.
(2) alpha(f_3,a,c)=sigma, because c->a is a circuit edge, hence the reverse pair a,c satisfies alpha(a,c,f_3)=sigma, and cyclic permutation preserves alpha.
(3) alpha(a,c,f_2)=sigma by the same reverse-edge relation.
(4) alpha(c,f_2,f_1)=sigma, since it is the reversal of alpha(f_1,f_2,c)=alpha(c,f_1,f_2)=tau.
(5) alpha(f_2,f_1,b)=sigma, since it is the reversal of alpha(b,f_1,f_2)=tau.

Thus H has status word tau^* sigma^*: at most one change. It spans all vertices, contradicting counterexamplehood.

The short cases need no separate machinery. If m=3, the order (f_3,a,c,f_2,f_1,b) has all displayed statuses sigma. If m=2, (a,c,f_2,f_1,b) is sigma-monochromatic by (3)--(5). Hence every m>=2 closes.

Therefore a pure-orientation whole-front three-circuit cannot occur in a NOR counterexample. Equivalently, the propagated full-curvature tube with flat cross walls is not a surviving obstruction: reversing the monochromatic carrier down to f_3 and threading the reverse circuit edge a,c across the first two tail vertices yields an explicit spanning one-change order.

This removes the entire pure size-three circuit branch and shows that the curvature tube should be viewed as a constructive certificate, not an irreducible obstruction.
