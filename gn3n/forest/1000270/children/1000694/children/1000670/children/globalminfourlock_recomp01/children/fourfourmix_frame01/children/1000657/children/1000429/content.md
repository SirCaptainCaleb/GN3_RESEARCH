# A global 4|5|a minimum synchronizes one four-side label with both long endpoints and three five-side deletions

## Statement

Let X|Y|P be a spanning three-cover minimizing quadratic potential among all spanning three-covers of a boundary tournament, with |X|=4, |Y|=5, and P=(p_1,...,p_a), a>=7. Then there exists x in X such that both (X-{x}) union {p_1} and (X-{x}) union {p_a} are Hamiltonian, Y union {x} is non-Hamiltonian, and at least three vertices y in Y satisfy (Y-{y}) union {x} Hamiltonian.

## Body

For an endpoint e in {p_1,p_a}, global minimality forces X union {e} to be non-Hamiltonian: if it were Hamiltonian, replacing X|P by a five-path on X union {e} and the inherited path P-e would change orders 4,a to 5,a-1 and decrease Phi by 2a-10>0.

Fix such an endpoint e. The five-set X union {e} is non-Hamiltonian, while deleting e leaves the Hamiltonian four-set X. By smallset01, a non-Hamiltonian five-set has at most one non-Hamiltonian four-vertex deletion. Hence at least three vertices x in X satisfy (X-{x}) union {e} Hamiltonian. Let I_e be this set. Thus |I_{p_1}|,|I_{p_a}|>=3. Since X has four vertices, their intersection has size at least two. Choose x in I_{p_1} intersect I_{p_a}.

We claim Y union {x} is non-Hamiltonian. If it were Hamiltonian, choose either endpoint e of P. Then (X-{x}) union {e}, Y union {x}, and P-e would form a spanning three-cover of orders 4,6,a-1. Relative to the original orders 4,5,a, the potential drop is
16+25+a^2-[16+36+(a-1)^2]=2a-12>0
for a>=7, contradicting global minimality.

Finally apply four-of-six to the non-Hamiltonian six-set Y union {x}. At least four of its six vertex deletions are Hamiltonian. Deleting x leaves Y, which is Hamiltonian, so at least three deletions y in Y also leave Hamiltonian five-sets (Y-{y}) union {x}. ∎
