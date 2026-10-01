# A one-gap deficit-one residue is bounded or exposes a standard paired-noninsertion witness

## Statement

Let A be a globally longest tight path and let C be a tight A-order-preserving path of order |A|-1 that agrees with A outside one common-vertex gap g. Write O=V(A)-V(C) and E=V(C)-V(A), so O and E lie in g and |O|=|E|+1. Then either |E|<=1, in which case the entire symmetric-difference kernel has at most three vertices and the gap support has at most five vertices when g is internal (at most four when g is an endpoint gap), or |E|>=2 and two vertices x,y in E expose one of the four certified longest-path paired-noninsertion outcomes: a Hamiltonian four-set, a Hamiltonian five-set, a tight cross triple through A, or a direct tight interval connector through A.

## Body

The one-gap conclusion gives O=V(A)-V(C), E=V(C)-V(A), both supported in one gap, with |O|=|E|+1. If |E|<=1 then |O|<=2, hence |O union E|<=3. Adding the two common anchors of an internal gap gives at most five vertices in the whole local gap kernel; an endpoint gap has at most one anchor, hence at most four.

Assume |E|>=2 and choose distinct x,y in E. Both lie outside V(A). Since A is globally longest, neither x nor y is insertable into the displayed order of A: a successful insertion would produce a tight path of order |A|+1. Therefore the certified longest-path paired-noninsertion theorem 6839f08d0cf8 applies to x,y relative to A. It yields one of four outcomes: a Hamiltonian four-set using one of x,y and three consecutive vertices of A; a Hamiltonian five-set using x,y and three consecutive vertices of A; a tight cross triple (x,a_i,y) or (y,a_i,x); or a direct tight interval connector from one of x,y through a nonempty subpath of A to the other. These are precisely the stated alternatives.
