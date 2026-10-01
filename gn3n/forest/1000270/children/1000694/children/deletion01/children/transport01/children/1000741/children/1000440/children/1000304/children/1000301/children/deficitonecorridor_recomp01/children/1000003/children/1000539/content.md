# The tiny one-gap branch is already a Hamiltonian five-window or a bounded failed-insertion obstruction

## Statement

Let H be a minimum counterexample and let R|S be a one-defect state with d(R)=1, with C a longest tight path of R and w the unique vertex of R-V(C), so H-w=C|S is a deletion two-cover. Let A be a globally longest tight path such that C has order |A|-1, is A-order-preserving, and agrees with A outside one gap; write O=V(A)-V(C), E=V(C)-V(A). If |E|<=1, then either (1) |E|=1 and the discrepancy gap is internal, in which case its five-vertex support is Hamiltonian and has a non-Hamiltonian two-coverable complement; or (2) w is noninsertable into the displayed path C, so the certified failed-insertion normal form supplies one of its bounded local obstructions using w and at most four consecutive vertices of C. Hence |E|<=1 creates no new unbounded residue.

## Body

By the one-defect/deletion-cover equivalence d8dce2799f24, R=V(C) union {w}, H-w=C|S is a deletion two-cover, and H[R] is non-Hamiltonian. Therefore w cannot be inserted into any position of the displayed path C: a successful insertion would Hamiltonize R. The failed-insertion normal form insert01 consequently applies whenever needed and yields a bounded obstruction supported on w together with at most four consecutive vertices of C.

It remains to record the stronger internal-gap conclusion when |E|=1. Then |O|=2. If the unique discrepancy gap has common anchors u,v, write its A-corridor as (u,a,b,v) and its C-corridor as (u,x,v), where E={x} and O={a,b}. The reusable lemma 53d257fcf0a8 shows that W={u,a,b,v,x} is Hamiltonian. In a minimum counterexample W is proper; if H-W were Hamiltonian then W together with H-W would two-cover H. Hence H-W is non-Hamiltonian, and minimality gives path-cover number two.

If |E|=0, or if |E|=1 but the discrepancy gap is an endpoint gap and therefore lacks two anchors, use the noninsertability of w into C and insert01 directly. Thus every tiny one-gap residue is already one of the stated bounded inputs.
