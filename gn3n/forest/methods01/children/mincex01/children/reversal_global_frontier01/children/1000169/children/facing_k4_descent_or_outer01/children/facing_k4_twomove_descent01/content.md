# Inner facing four-windows give a two-move same-component quadratic descent

## Statement

Let H be a minimum counterexample and let H-x=P|Q be a deletion two-cover, with P=(p_0,...,p_{p-1}) and Q=(q_0,...,q_{q-1}) of orders p,q>=3. Suppose one of the two inner facing four-windows from facing_k4_descent_or_outer01 is Hamiltonian. Then the corresponding lower-quadratic-potential spanning three-cover is reachable from the singleton lift P|Q|{x} by exactly two legal pairwise repartitions. Consequently the inner-window alternative gives a strict decrease of at least six inside the same pairwise-repartition component as the deletion singleton lift.

## Body

Suppose first W_L={p_0,q_{q-1},x,p_1} is Hamiltonian. Start from the singleton lift P|Q|{x}. Repartition the pair Q|{x} on its union into the inherited path Q^-=(q_0,...,q_{q-2}) and the two-vertex path R=(q_{q-1},x). This is a legal pairwise repartition.

Now repartition the pair P|R on its union. The Hamiltonian four-set W_L and the inherited tail P^-=(p_2,...,p_{p-1}) are disjoint tight paths whose supports partition V(P) union V(R). Hence replacing P|R by W_L|P^- is a second legal pairwise repartition. The untouched component Q^- gives exactly the spanning three-cover
W_L | (p_2,...,p_{p-1}) | (q_0,...,q_{q-2})
from facing_k4_descent_or_outer01.

For W_R={p_0,q_{q-1},x,q_{q-2}}, first repartition P|{x} into the inherited tail (p_1,...,p_{p-1}) and the two-vertex path (p_0,x). Then repartition that two-vertex path together with Q into W_R and the inherited prefix (q_0,...,q_{q-3}). This yields exactly the symmetric displayed three-cover.

By facing_k4_descent_or_outer01, the final quadratic-potential change from P|Q|{x} is at most -6 in either case. Since both transformations are legal pairwise repartitions, the decrease occurs inside the same connected component of the pairwise-repartition graph.
