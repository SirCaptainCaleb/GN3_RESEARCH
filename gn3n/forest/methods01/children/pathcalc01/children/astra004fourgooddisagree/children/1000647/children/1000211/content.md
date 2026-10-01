# Every minimum counterexample contains order disagreement

## Statement

Every minimum counterexample H contains two tight paths on overlapping vertex sets that order some common pair of vertices differently.

## Body

Assume for contradiction that H is a minimum counterexample with no order disagreement. By c644ac221801, every six-vertex induced subtournament is Hamiltonian and every component of every exact one-vertex deletion two-cover has order at least six.

Choose any deletion cover H-x=P|Q and write P=(p_0,...,p_{m-1}), where m>=6. The omitted vertex x is not insertable into the displayed order P, since such an insertion together with Q would give a spanning two-cover of H.

For 0<=i<=m-5 put
W_i=(p_i,p_{i+1},p_{i+2},p_{i+3},p_{i+4}).
The six-set V(W_i) union {x} is Hamiltonian. If x were noninsertable into the displayed order W_i, the certified theorem noninsertableorderdisagree01 would force order disagreement between W_i and every Hamilton order of its enlargement, contrary to the standing hypothesis. Hence x is insertable into every W_i.

Number the six insertion positions in W_i from 0 (before p_i) through 5 (after p_{i+4}). Positions 2 and 3 are impossible: all three new consecutive triples needed for such an insertion are already contained inside W_i union {x}, so the same insertion would be valid in the full displayed path P, contradicting global noninsertability of x. Thus every W_i admits an insertion of x in one of the two left positions {0,1} or one of the two right positions {4,5}. Choose one successful insertion for each i and call its side L or R accordingly.

Adjacent windows cannot have different sides. Indeed, W_i and W_{i+1} share x and the four vertices p_{i+1},...,p_{i+4}. If the chosen insertion in W_i is on the right while that in W_{i+1} is on the left, then in the first tight path x occurs after p_{i+2}, while in the second x occurs before p_{i+2}; this is order disagreement. Conversely, if W_i uses the left side and W_{i+1} the right side, then x occurs before p_{i+3} in the first path and after p_{i+3} in the second. Both contradict the hypothesis. Hence all chosen window insertions have one common side.

The first window W_0 cannot use the left side. At positions 0 or 1 there is no missing predecessor outside W_0, so every local triple required by the insertion is exactly every new triple required to insert x at the same position in the full path P. Thus a left insertion in W_0 would insert x into P. Therefore W_0 must use side R.

Similarly, the last window W_{m-5} cannot use the right side. At positions 4 or 5 there is no missing successor outside the last window, so a right insertion there extends verbatim to an insertion into all of P. Therefore W_{m-5} must use side L.

This contradicts the fact that all adjacent windows must use the same side. Hence the assumed absence of order disagreement is impossible.