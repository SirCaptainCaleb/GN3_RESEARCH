# Optimal dual weight concentrates on the intersection of union-Hamiltonian supports

## Statement

Let x be an optimal fractional cover by tight-path supports and w an optimal dual weighting with w(P)<=1 for every tight-path support P. If A and B are positive-weight path supports of x and A union B is a tight-path support, then w(A)=w(B)=w(A union B)=w(A intersect B)=1, so w(A symmetric difference B)=0. Hence if w is positive on every vertex, no two distinct positive-weight path supports have Hamiltonian union.

## Body

Primal-dual equality and feasibility give
sum_P x_P >= sum_P x_P w(P) = sum_v w(v)c_x(v) >= sum_v w(v),
while the two endpoint sums are equal at optimum. Thus every path support P with x_P>0 has w(P)=1.

For path supports A,B with x_A,x_B>0 and U=A union B also a path support, dual feasibility gives w(U)<=1. Inclusion-exclusion gives
2=w(A)+w(B)=w(U)+w(A intersect B).
Because w(A intersect B)<=1, both terms on the right equal 1. Therefore w(A minus B)=w(B minus A)=0.

If every vertex has positive dual weight, the symmetric difference must be empty, so A=B.
