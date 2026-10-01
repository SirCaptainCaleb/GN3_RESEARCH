# A globally quadratic-minimal three-cover cannot have profile 4|4|a with a at least six

## Statement

Let H be a boundary tournament and let X|Y|P be a spanning three-cover minimizing quadratic potential among all spanning three-covers of H. If |X|=|Y|=4 and |P|=a>=6, then a contradiction follows. Hence no globally quadratic-minimal spanning three-cover has component-order profile 4|4|a for a>=6.

## Body

Write X and Y as Hamiltonian four-paths and P=(p_1,...,p_a), a>=6. Fix one endpoint e of P. Global minimality implies X union {e} is non-Hamiltonian: otherwise replacing X|P by a Hamilton five-path on X union {e} and the inherited path P-e gives component orders 5,a-1 instead of 4,a and lowers Phi by 2a-10>0.

Because X union {e} is a non-Hamiltonian five-set while X itself is Hamiltonian, smallset01 implies that at most one of its four vertex-deletions inside X is non-Hamiltonian. Hence there are at least three distinct vertices x in X for which (X-{x}) union {e} is Hamiltonian.

For each such x, Y union {x} must be non-Hamiltonian. Indeed, if Y union {x} were Hamiltonian, then the three disjoint Hamiltonian supports (X-{x}) union {e}, Y union {x}, and P-e would form a spanning three-cover of orders 4,5,a-1. Relative to the original orders 4,4,a, the potential drop would be
16+16+a^2-[16+25+(a-1)^2]=2a-10>0,
contradicting global minimality. Thus at least three vertices of X are bad one-vertex extensions of Y.

Apply the preceding three-bad-four-mix lemma to X and Y. It gives a 5|3 cover of X union Y. Keeping P unchanged yields a spanning three-cover C_1 of component orders 5,3,a. Its potential exceeds that of the original 4|4|a cover by exactly 2.

Now apply the certified arbitrary-state theorem threesidedescent6 to the three-vertex component of C_1 and the a-vertex path P. If one endpoint extension is Hamiltonian, the resulting move decreases Phi(C_1) by 2a-8, so relative to the original cover the net decrease is 2a-10>0. If both endpoint four-sets are non-Hamiltonian, threesidedescent6 instead decreases Phi(C_1) by 4a-20, giving net decrease 4a-22>0 for every a>=6. Either case contradicts global minimality. ∎
