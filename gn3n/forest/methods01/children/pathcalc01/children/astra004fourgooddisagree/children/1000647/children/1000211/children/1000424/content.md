# Every minimum counterexample contains a reversible consecutive pair

## Statement

Every minimum counterexample H contains distinct vertices u,v and two tight paths R,S such that u,v occur consecutively as (u,v) in R and consecutively as (v,u) in S.

## Body

By 44a0c8ced13c, H contains two tight paths with order disagreement. Apply Section 4 of the certified path-intersection calculus pathcalc01.

If outcome (1) there occurs, we already have a common ordinary edge traversed in opposite directions.

If outcome (2) occurs, there is a tight triple T=(x,y,z) reversing an ordered edge of one of the original paths P. By definition, either (z,y) is an ordered edge of P or (y,x) is an ordered edge of P. In the first case T contains the consecutive pair (y,z), opposite to (z,y) in P; in the second T contains (x,y), opposite to (y,x) in P. Hence again there is a reversible consecutive pair.

If outcome (3) occurs, let the resulting vertex-simple tight cycle have cyclic order
C=(c_0,c_1,...,c_{k-1}).
Opening the cycle immediately after c_0 gives the tight path
R=(c_1,c_2,...,c_{k-1},c_0),
which contains the consecutive pair (c_{k-1},c_0). The two-vertex sequence
S=(c_0,c_{k-1})
is itself a tight path vacuously and contains the reverse pair. Thus the cycle outcome also yields a reversible consecutive pair.

Therefore every possible output of pathcalc01 produces two tight paths carrying one common consecutive pair in opposite directions.
