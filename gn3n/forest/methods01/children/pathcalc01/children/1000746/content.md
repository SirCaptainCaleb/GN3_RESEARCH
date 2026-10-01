# Two extenders at one end and one at the other Hamiltonize the whole core

## Statement

Let H be a boundary tournament and let R=(r_1,...,r_m), m>=2, be a tight path. Let a,b,c be three distinct vertices outside R. If both (a,R) and (b,R) are tight and (R,c) is tight, then H[V(R) union {a,b,c}] is Hamiltonian. Symmetrically, if (R,a) and (R,b) are tight and (c,R) is tight, then the same union is Hamiltonian.

## Body

Assume first that a and b both left-extend R and c right-extends R.

On the three-set {a,b,r_1}, exactly one of the two reversal classes is tight. Therefore, after possibly interchanging a and b, we may assume
(a,b,r_1)
is tight.

Consider the ordering
(a,b,r_1,r_2,...,r_m,c).

Its first consecutive triple is tight by the chosen order of a,b. Its second triple
(b,r_1,r_2)
is tight because (b,R) is a tight path. Every interior triple on R is tight because R is a tight path. Finally
(r_{m-1},r_m,c)
is tight because (R,c) is a tight path. Thus the displayed ordering is a Hamilton tight path on V(R) union {a,b,c}.

The right-right-left statement is symmetric: after ordering the two right extenders suitably relative to r_m, the path
(c,r_1,...,r_m,a,b)
is tight. ∎
