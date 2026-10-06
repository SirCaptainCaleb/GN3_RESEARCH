# Local square obstruction and witness incompatibility

Localize failure of union closure in accessible NOR support families and identify what makes the top-missing square genuinely obstructive.

For any finite accessible family F containing the empty set, union closure is equivalent to the local square-completion rule: whenever C, C union {a}, and C union {b} are feasible, C union {a,b} is feasible.

Proof: choose a non-union pair A,B with U=A union B infeasible, minimizing |U| and then |A|+|B|. Choose removable a from A and b from B. Secondary minimality forces a outside B and b outside A. Primary minimality gives U-a and U-b feasible. It also gives C=U-{a,b} feasible because C=(A-a) union (B-b). Hence every failure of union closure contains a top-missing Boolean square.

For NOR feasible-support families this means global failure of antimatroidality is always local on a cube 2-face.

If one sigma-tight witness P for C admits both a and b as same-color front extensions, then (a,b,P) already has at most one color change, because every window except possibly the first has color sigma. Thus a genuine top-missing NOR square can survive only because the two side feasibilities require incompatible witness orders of the common support C.

Also, if P is sigma-tight on all but two ambient vertices x,y, then a NOR counterexample forces both x and y to be blocked at the front. Writing F for the first r-1 vertices and Q for the first r-2 vertices of P, counterexamplehood forces h(x,F)=h(y,F)=1-sigma and h(x,y,Q)=h(y,x,Q)=sigma. Otherwise one of (x,y,P),(y,x,P) has at most one change.

The closure target is therefore witness synchronization: compare the two side witnesses of a top-missing support square, locate their first order disagreement from the common terminal state, and either repair the disagreement or descend to a smaller top-missing square.
