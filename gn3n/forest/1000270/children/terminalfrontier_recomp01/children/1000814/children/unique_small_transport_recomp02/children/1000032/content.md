# Corrected: a two-crossing leave-return forces a Hamiltonian four-window

## Statement

Let H be a minimum counterexample. Let A,B,C be disjoint displayed tight paths of common order r>=3, and let x,y be distinct vertices outside them such that both x and y initial-extend each of A,B,C.

Suppose a two-cover T of H-{x,y}=A union B union C is order-neutral on each displayed core and has exactly two cross-core edges. Suppose one T-component has leave-and-return form A_1,D,A_2, where A=A_1A_2 is split into two nonempty contiguous displayed blocks, D is one whole remaining core, and the other T-component is the third whole core E.

Then H contains a proper Hamiltonian four-set whose complement is non-Hamiltonian with path-cover number two. Hence this two-crossing leave-and-return configuration is impossible in the witness-free unique-small plateau.

## Body

Because T has exactly two cross-core edges, its four maximal core blocks have counts 2,1,1. Thus D and E are whole cores.

Write A_1=(a_1,...,a_t). If t>=2, then x initial-extends A, so prepending x to the T-component A_1,D,A_2 creates a tight path: the only new triple is (x,a_1,a_2). Since y initial-extends E, (y,E) is tight. These two paths span H, impossible. Hence t=1; write A_1=(a), D=(d_1,...,d_r).

Because (a,D,A_2) is a T-path, a initial-extends D. Both x and y also initial-extend D.

If either (x,a,d_1) or (a,x,d_1) were tight, then respectively (x,a,D,A_2) or (a,x,D,A_2) would be a tight path; together with (y,E) this would two-cover H. Hence both are non-tight, and boundary antisymmetry gives (d_1,a,x) and (d_1,x,a) tight.

Similarly, using y in the leave-return component and (x,E) as the other spanning path gives (d_1,a,y) and (d_1,y,a) tight.

Boundary antisymmetry gives exactly one of the reversal pair (x,a,y) and (y,a,x) as tight. In the first case (d_1,x,a,y) is a Hamilton tight path on W={d_1,a,x,y}, using (d_1,x,a) and (x,a,y). In the second case (d_1,y,a,x) is a Hamilton tight path, using (d_1,y,a) and (y,a,x). Hence W is Hamiltonian.

The set W is proper because |V(H)|=3r+2>=11. If H-W were Hamiltonian, Hamilton paths on W and H-W would form a spanning two-cover of H. Hence H-W is non-Hamiltonian, and minimum-counterexample calculus gives path-cover number two.

Thus the two-crossing leave-and-return configuration forces the stated Hamiltonian four-set with two-coverable complement.
