# Facing endpoint four-windows either give a six-unit quadratic drop or omit the deletion label

## Statement

Let H be a minimum counterexample and let H-x=P|Q be a deletion two-cover, where P=(p_0,...,p_{p-1}) and Q=(q_0,...,q_{q-1}) have orders p,q>=3. For the facing endpoint pair p_0,q_{q-1}, at least one of the following holds.

(1) There is a spanning three-cover of H of the form
W_L | (p_2,...,p_{p-1}) | (q_0,...,q_{q-2}),
where W_L={p_0,q_{q-1},x,p_1} is Hamiltonian, or symmetrically
W_R | (p_1,...,p_{p-1}) | (q_0,...,q_{q-3}),
where W_R={p_0,q_{q-1},x,q_{q-2}} is Hamiltonian. In either case its quadratic potential is at least six smaller than the singleton-lift cover P|Q|{x}.

(2) The outer-neighbor four-set
W_O={p_0,q_{q-1},p_1,q_{q-2}}
is Hamiltonian and H-W_O is non-Hamiltonian with path-cover number two.

The symmetric dichotomy holds at the other facing pair q_0,p_{p-1}.

## Body

By 3640577112bf, at least one of W_L,W_R,W_O is Hamiltonian, and every Hamiltonian choice has non-Hamiltonian path-cover-two complement.

If W_L is Hamiltonian, its complement is exactly the disjoint union of the inherited tight paths (p_2,...,p_{p-1}) and (q_0,...,q_{q-2}); hence the displayed three paths cover H. Its potential is
16+(p-2)^2+(q-1)^2,
whereas the singleton lift P|Q|{x} has potential p^2+q^2+1. The difference is
20-4p-2q.
Minimum-counterexample calculus gives |H|=p+q+1>10, so p+q>=10. With p,q>=3, 4p+2q>=26, and therefore the difference is at most -6.

The W_R calculation is symmetric:
16+(p-1)^2+(q-2)^2-(p^2+q^2+1)=20-2p-4q<=-6.

Thus if either inner window is Hamiltonian, alternative (1) holds with a uniform six-unit drop. If neither inner window is Hamiltonian, 3640577112bf forces W_O to be Hamiltonian, giving alternative (2). The other facing pair follows by symmetry.
