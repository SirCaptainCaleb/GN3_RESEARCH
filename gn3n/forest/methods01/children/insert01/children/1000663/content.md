# A Hamilton path missing one vertex gives a balanced cover or two separated noninsertion obstructions

## Statement

Let K be a boundary tournament on 2r vertices with r>=3, let x be a vertex, and let P=(v_1,...,v_{2r-1}) be a Hamilton path of K-x. Put L=(v_1,...,v_{r-1}), m=v_r, and R=(v_{r+1},...,v_{2r-1}). Then at least one of the following holds: (1) K has a two-cover whose two supports both have order r, namely a Hamilton path on V(L) union {x} together with the inherited path (m,R); (2) K has such a balanced two-cover given by the inherited path (L,m) together with a Hamilton path on V(R) union {x}; (3) x is noninsertable into both displayed paths L and R. In case (3), the failed-insertion normal form supplies one bounded insertion-obstruction window on each side of the single central vertex m.

## Body

The inherited sequences (L,m) and (m,R) are tight paths of order r. If K[V(L) union {x}] is Hamiltonian, a Hamilton path on that support together with (m,R) gives the balanced two-cover in (1). Similarly, if K[V(R) union {x}] is Hamiltonian, then (L,m) together with a Hamilton path on V(R) union {x} gives (2). Suppose neither support is Hamiltonian. If x were insertable into the displayed order L at any position, the resulting tight path would be a Hamilton path on V(L) union {x}, contradiction. Hence x is noninsertable into L. The same argument gives noninsertability into R. Applying the failed-insertion normal form from insert01 separately to L and R gives the two bounded obstruction windows. The two windows are separated in the displayed path P by the single central vertex m; no bound on r beyond r>=3 is used.
