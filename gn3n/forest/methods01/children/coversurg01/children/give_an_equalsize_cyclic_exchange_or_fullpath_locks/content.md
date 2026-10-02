# Synchronized three-way replacements give an equal-size cyclic exchange or full-path locks

## Statement

Let X|Y|P be any spanning three-cover of a boundary tournament, with P=(p_1,...,p_m), and let x be a vertex of X. Let J be any subset of V(Y). Assume both (V(X)-{x}) union {p_1} and (V(X)-{x}) union {p_m} are Hamiltonian, and assume (V(Y)-{y}) union {x} is Hamiltonian for every y in J. For each y in J, if (V(P)-{e}) union {y} is Hamiltonian for some endpoint e of P, there is a spanning three-cover with exactly the same component orders as X|Y|P by the cyclic support exchange x from X to Y, y from Y to P, e from P to X. If neither endpoint truncation enlarged by y is Hamiltonian, then y is noninsertable into every position of the displayed path P. Consequently, if no equal-size cyclic exchange exists for any y in J, every vertex of J is globally noninsertable into P.

## Body

Fix y in J. For an endpoint e in {p_1,p_m}, let A_e=(V(X)-{x}) union {e} and B_y=(V(Y)-{y}) union {x}. By hypothesis A_e and B_y are Hamiltonian.

If H[(V(P)-{e}) union {y}] is Hamiltonian for at least one endpoint e, choose Hamilton paths on A_e, B_y, and (V(P)-{e}) union {y}. Their supports are pairwise disjoint and partition V(H). Their orders are |X|, |Y|, and |P|, respectively, exactly the original component orders. Thus they form an equal-size spanning three-cover whose supports implement the cyclic exchange x:X->Y, y:Y->P, e:P->X.

Suppose instead that neither endpoint truncation enlarged by y is Hamiltonian. If y could be inserted into any position of the displayed tight order P, then deleting a suitable endpoint from that inserted order would leave a Hamilton path on one of the two endpoint truncations together with y. For insertion before p_1 or after p_m delete the opposite endpoint. For an internal insertion, deleting either endpoint that lies outside the local insertion preserves all consecutive triples used by the inserted path. This contradicts the assumed non-Hamiltonicity of both endpoint-truncation enlargements. Hence y is noninsertable into every position of P.

The argument applies independently to each y in J. If no equal-size cyclic exchange exists for any y in J, the first alternative fails for every y, so every y is globally noninsertable into P. No component-size, minimality, trappedness, or ambient-order hypothesis is used. ∎