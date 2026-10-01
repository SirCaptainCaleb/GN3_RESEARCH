# Universal triple reachability forces a seven-set no-merge barrier

## Statement

Let H be a hypothetical order-eleven minimum counterexample. For every three-set X and every balanced Hamiltonian 4|4 cover P|Q of H-X, both seven-sets X union P and X union Q are non-Hamiltonian. Equivalently, every balanced 4|4 complement of every three-set is simultaneously blocked from absorbing that three-set on either side.

## Body


Let (H) be a hypothetical minimum counterexample of order eleven.

Fix an arbitrary three-element set
[
Xsubseteq V(H).
]
Every three-set is Hamiltonian. By the balanced order-eight theorem astra003balanced8, the complement
[
W=V(H)-X
]
admits a partition
[
W=Psqcup Q,qquad |P|=|Q|=4,
]
with both (P) and (Q) Hamiltonian.

Thus
[
X|P|Q
]
is a spanning (3|4|4) cover. By the global order-eleven connectivity theorem, this state lies in the universal connected component of the Astra-003 move graph, but the following conclusion uses only that (H) is a counterexample.

Suppose
[
Xcup P
]
were Hamiltonian. Since (Q) is Hamiltonian and disjoint from (Xcup P), the two paths
[
(Xcup P)mid Q
]
would form a spanning two-cover of (H), contradiction.

Therefore
[
Xcup P
]
is non-Hamiltonian.

The same argument gives
[
Xcup Q
]
non-Hamiltonian.

Since (X) was arbitrary, every balanced Hamiltonian (4|4) cover of the complement of every three-set has the simultaneous no-merge property:
[
H[Xcup P]\text{ and }H[Xcup Q]\text{ are both non-Hamiltonian}.
]

This is the static form of the order-eleven merge obstruction after the reconfiguration graph has been shown connected.
