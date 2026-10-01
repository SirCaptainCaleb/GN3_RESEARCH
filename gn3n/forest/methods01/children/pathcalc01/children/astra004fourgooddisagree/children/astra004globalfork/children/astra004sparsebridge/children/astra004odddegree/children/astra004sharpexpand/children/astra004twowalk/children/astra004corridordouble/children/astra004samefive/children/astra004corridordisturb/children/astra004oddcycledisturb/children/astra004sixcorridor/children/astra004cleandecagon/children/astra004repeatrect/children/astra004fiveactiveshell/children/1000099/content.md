# A three-leaf same-core star forces a complete reverse-end fan

## Statement


Let H be a boundary tournament with maximum tight-path order lambda. Let C=(c_1,...,c_m) be a tight path of order m=lambda-2, and let e,a,b,c be four distinct vertices outside C. Suppose
(e,C,a), (e,C,b), (e,C,c)
are tight paths. Then for every ordered pair of distinct leaves u,v in {a,b,c},
(u,v,c_m)
is tight.

Consequently, for the three leaves a,b,c the four-set
{a,b,c,c_m}
is Hamiltonian.

The left-right symmetric statement holds when the three displayed paths have the form
(a,C,e), (b,C,e), (c,C,e):
then (c_1,u,v) is tight for every ordered pair of distinct leaves u,v, and {c_1,a,b,c} is Hamiltonian.


## Body


Fix two distinct leaves u,v in {a,b,c}. The three paths
(e,C,u), (e,C,v)
show that u and v both right-extend C while e left-extends C.

The set V(C) union {e,u,v} has order
(lambda-2)+3=lambda+1,
so by maximality of lambda it is non-Hamiltonian. Apply 7b9f6ae39813 in its right-right-left form. Its Hamiltonian alternative is impossible, hence both reverse endpoint triples
(v,u,c_m) and (u,v,c_m)
are tight.

Since u,v were arbitrary, (u,v,c_m) is tight for every ordered pair of distinct leaves.

Now boundary antisymmetry applied to the reversal pair
(a,b,c), (c,b,a)
says exactly one of these two triples is tight. If (a,b,c) is tight, then
(a,b,c,c_m)
is a tight four-vertex path because (b,c,c_m) is tight. If (c,b,a) is tight, then
(c,b,a,c_m)
is tight because (b,a,c_m) is tight. Thus {a,b,c,c_m} is Hamiltonian.

The opposite orientation is symmetric. ∎
