# Every minimum counterexample has nonvacuous order disagreement

## Statement

Every minimum counterexample H contains two tight paths R,S, each of order at least three, whose common vertices do not occur in the same relative order.

## Body

Split according to six-vertex Hamiltonicity.

Case 1: some six-set U is non-Hamiltonian. By the certified four-of-six theorem in smallset01, at least four vertices d of U have H[U-{d}] Hamiltonian. Choose Hamilton tight paths on four such five-vertex deletions. The certified theorem astra004fourgooddisagree forces two of these five-paths to disagree in relative order. Both paths have order five, so the conclusion holds.

Case 2: every six-set of H is Hamiltonian. Choose any deletion two-cover
H-x=P|Q.
Every deletion-cover component in a minimum counterexample has order at least three.

If one component, say P, has order at most five, then 3<=|P|<=5 and the certified theorem 6f72075b0b54 applies. It gives four Hamiltonian deletion paths inside C=V(P) union {x}, and some pair has order disagreement. Each such path has order |P|>=3, so again the conclusion holds.

It remains that |P|,|Q|>=6. Write
P=(p_0,...,p_{m-1}), m>=6.
The omitted vertex x is not insertable into the displayed order P, since such an insertion together with Q would give a spanning two-cover of H.

For 0<=i<=m-5 let
W_i=(p_i,p_{i+1},p_{i+2},p_{i+3},p_{i+4}).
By the present case assumption, the six-set V(W_i) union {x} is Hamiltonian.

If x is noninsertable into the displayed order W_i for some i, the certified theorem noninsertableorderdisagree01 says that every Hamilton path on V(W_i) union {x} disagrees in relative order with W_i. This gives paths of orders five and six and proves the conclusion.

Hence suppose x is insertable into every W_i. In a five-window, insertion positions 2 and 3 are impossible: every new consecutive triple required there also occurs in the full path P, so such an insertion would insert x into P. Thus each W_i has a successful insertion in one of the two left positions {0,1} or one of the two right positions {4,5}. Choose one successful insertion for each i and call its side L or R.

If adjacent windows W_i,W_{i+1} have opposite chosen sides, the resulting Hamilton six-paths disagree on their five common vertices x,p_{i+1},...,p_{i+4}. Indeed, in the R-then-L case x is after p_{i+2} in the first path and before p_{i+2} in the second; in the L-then-R case x is before p_{i+3} in the first and after p_{i+3} in the second. Thus the conclusion holds.

Therefore, if no disagreement has yet occurred, all adjacent chosen sides agree and hence all windows have one common side. But W_0 cannot use side L: an insertion before p_0 or between p_0,p_1 requires no predecessor outside W_0, so the same insertion extends verbatim to all of P. Similarly the last window W_{m-5} cannot use side R. Hence the common side would have to be simultaneously R and L, a contradiction.

Thus in every case H contains order disagreement witnessed by two tight paths each of order at least three.