# A locally minimal four-side saturates its two-endpoint six-shell

## Statement

Let H be a minimum counterexample and let X|P|Q be a spanning three-cover that is quadratic-potential-minimal in its pairwise-repartition component, with |X|=4 and P=(p_1,...,p_m), m>=7. Put E={p_1,p_m}, R=(p_2,...,p_{m-1}), and U=X union E. Then U is non-Hamiltonian; both X union {p_1} and X union {p_m} are non-Hamiltonian; for every x in X the five-set E union (X-{x}) is Hamiltonian; and for every x in X the set R union {x} is non-Hamiltonian. Consequently the four Hamiltonian five-sets E union (X-{x}) all have non-Hamiltonian path-cover-two complements in H. Thus a nonescaping four-side beside a path of order at least seven forces a saturated endpoint shell: the two endpoint deletions of U are bad and all four four-side deletions are good.

## Body

Write Phi for the quadratic potential of the displayed three-cover.

If U were Hamiltonian, then replacing the pair X|P by U|R would be a legal pairwise repartition, with pair sizes changing from (4,m) to (6,m-2). For m>=7 this is strictly more balanced and has strictly smaller quadratic potential, contradicting local minimality. Hence U is non-Hamiltonian.

If X union {p_1} were Hamiltonian, then (X union {p_1}) | (p_2,...,p_m) would be a legal repartition of X|P, with pair sizes (5,m-1), again strictly lowering the quadratic potential for m>=7. The same argument with the opposite end shows X union {p_m} is non-Hamiltonian.

By the certified six-set four-of-six theorem, U has at least four Hamiltonian one-vertex deletions. The deletions of p_1 and p_m are exactly X union {p_m} and X union {p_1}, which were just shown non-Hamiltonian. Therefore every remaining deletion is Hamiltonian: for each x in X,
F_x=E union (X-{x})
is a Hamiltonian five-set.

Finally suppose R union {x} were Hamiltonian for some x in X. Then F_x and R union {x} are disjoint tight-path supports partitioning X union V(P), and replacing X|P by these two paths changes the pair sizes from (4,m) to (5,m-1), again a strict quadratic-potential decrease. This contradicts local minimality. Hence R union {x} is non-Hamiltonian for every x.

Each F_x is a proper Hamiltonian five-set in a minimum counterexample. Its complement cannot be Hamiltonian, since that would two-cover H, and minimality gives path-cover number at most two. Thus every H-F_x is non-Hamiltonian with path-cover number exactly two.
