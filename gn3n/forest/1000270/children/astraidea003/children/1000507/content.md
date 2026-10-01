# Quadratic-minimal three-covers forbid Hamiltonian endpoint transfer

## Statement

Let C=P|Q|R be a spanning three-path cover of a boundary tournament, with P=(p_0,...,p_{a-1}), |P|=a, |Q|=b, and a>=b+2. If H[V(Q) union {p_0}] or H[V(Q) union {p_{a-1}}] is Hamiltonian, then one legal Astra-003 pairwise repartition produces a three-cover C' with Phi(C')<Phi(C). Consequently, at a Phi-minimal state in any trapped Astra-003 component, both endpoint enlargements of every smaller component by either endpoint of a component at least two vertices larger are non-Hamiltonian.

## Body

# Endpoint transfer decreases the quadratic potential

Let C=P|Q|R be a spanning three-path cover, with

P=(p_0,...,p_{a-1}),  |P|=a,  |Q|=b,

and assume a>=b+2.

Suppose first that H[V(Q) union {p_0}] is Hamiltonian, and let L be a Hamilton path on this support. The suffix

P^-=(p_1,...,p_{a-1})

is a tight path. The paths L and P^- are disjoint and partition V(P) union V(Q), so replacing P|Q by L|P^- is one legal pairwise repartition. The third component R is unchanged.

The old contribution of P,Q to the quadratic potential is a^2+b^2. The new contribution is

(a-1)^2+(b+1)^2.

Their difference is

a^2+b^2-[(a-1)^2+(b+1)^2]=2(a-b-1)>0.

Thus Phi strictly decreases. The argument using p_{a-1} is identical, with the tight prefix (p_0,...,p_{a-2}) as the residual path.

Therefore, if C minimizes Phi in a connected component of the Astra-003 move graph containing no two-cover, then for every ordered pair of components P,Q with |P|>=|Q|+2, neither support V(Q) union {first(P)} nor V(Q) union {last(P)} can be Hamiltonian.
