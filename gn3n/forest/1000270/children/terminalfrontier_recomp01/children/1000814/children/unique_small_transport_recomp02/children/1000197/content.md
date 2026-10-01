# A two-crossing leave-return under universal initial extenders forces a four-window

## Statement


Let H be a minimum counterexample. Let A,B,C be disjoint displayed tight paths of a common order r>=3, and let x,y be distinct vertices outside them such that both x and y initial-extend each of A,B,C.

Suppose a two-cover T of H-{x,y}=A union B union C is order-neutral on each displayed core and has exactly two cross-core edges. Suppose one T-component has leave-and-return form
A_1, D, A_2,
where A=A_1 A_2 is the displayed A-order split into two nonempty contiguous blocks, D is one of the whole cores B,C in its displayed order, and the other T-component is the remaining whole core E.

Then either H has a spanning two-cover, or H contains a proper Hamiltonian four-set W whose complement is non-Hamiltonian with path-cover number two.

Consequently, in the witness-free unique-small plateau of unique_small_transport_recomp02, the two-crossing leave-and-return alternative cannot occur.


## Body

Because T has exactly two cross-core edges, its four maximal core blocks have counts 2,1,1. Hence in the stated leave-and-return case the intervening block D is an entire core and the other component E is the remaining entire core.

Write A_1=(a_1,...,a_t) in the inherited order. If t>=2, then x initial-extends A, so (x,a_1,a_2) is tight. Prepending x to the T-component A_1,D,A_2 therefore creates a tight path, while (y,E) is tight because y initial-extends E. These two paths would span H, impossible. Thus t=1.

Write A_1=(a), D=(d_1,...,d_r), and let c be the first vertex of A_2. The T-component (a,D,A_2) shows that (a,D) and (D,c) are tight paths.

If either (x,a,d_1) or (a,x,d_1) were tight, then respectively (x,a,D,A_2) or (a,x,D,A_2) would be a tight path, using the initial-extension property at the next new triple and inherited triples thereafter. Together with (y,E) this would two-cover H. Hence both are non-tight, so boundary reversal antisymmetry gives (d_1,a,x) and (d_1,x,a) tight. Exchanging x and y gives (d_1,a,y) and (d_1,y,a) tight.

Now boundary reversal antisymmetry gives exactly one of (x,a,y) and (y,a,x) as tight. If (x,a,y) is tight, then (d_1,x,a,y) is a Hamilton tight path on W={d_1,a,x,y}, using (d_1,x,a). If (y,a,x) is tight, then (d_1,y,a,x) is a Hamilton tight path, using (d_1,y,a). Thus W is Hamiltonian without any four-vertex classification.

The set W is proper because |V(H)|>=11. If H-W were Hamiltonian, Hamilton paths on W and H-W would two-cover H. Hence H-W is non-Hamiltonian, and minimum-counterexample calculus gives path-cover number two.

Therefore the leave-and-return case yields either a spanning two-cover or the stated proper Hamiltonian four-set with path-cover-two complement.