# Every label of a locally minimal 4|4 union is locked out of the common long interior

## Statement

Let H be a boundary tournament and let X|Y|P be a spanning three-cover minimizing quadratic potential within its connected pairwise-repartition component, with |X|=|Y|=4 and P=(p_1,...,p_m) of order m>=6. Put W=V(X) union V(Y) and M=(p_2,...,p_{m-1}). Then every vertex w in W is noninsertable into every position of the displayed path M. More precisely, if A is whichever of X,Y contains w, then (A-{w}) union {p_1,p_m} is Hamiltonian while M union {w} is non-Hamiltonian. Consequently each of the eight labels w supplies a tight triple through w reversing a displayed edge of M.

## Body

Fix w in W. Exactly one of the two displayed four-sides X,Y contains w; call it A, and call the other four-side B. The same spanning cover A|B|P is componentwise Phi-minimal. Apply local_four_allfour_interior_lock01 to the four-side A and the path P of order m>=6. The theorem gives that (A-{w}) union {p_1,p_m} is Hamiltonian, whereas M union {w} is non-Hamiltonian. Hence w is noninsertable into every position of the displayed path M and has a label-specific reversal witness on a displayed edge of M. Since w was arbitrary and X,Y partition W, all eight labels are simultaneously locked against the same interior M.