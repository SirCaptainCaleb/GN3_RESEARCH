# Endpoint Hamiltonicity always forces coarse crossing and additionally yields transport or fine double crossing

## Statement

Let H be a minimum counterexample and let X|C|D be a spanning three-cover, where H[X] is Hamiltonian, C=(c_0,c_1,...,c_m) is a nontrivial tight path, and D is a nonempty tight path. Suppose H[X union {c_0}] is Hamiltonian. Then every two-cover of H-c_0 contains an ordinary path edge crossing the coarse cut X | ((V(C)-{c_0}) union V(D)). In addition, at least one of the following holds. (1) Some Hamilton path on X union {c_0} has c_0 as an endpoint; then the greedy endpoint-transport theorem 883bd2af7e73 absorbs a maximal initial segment of C into X and produces a tight triple reversing the terminal or initial edge of the enlarged Hamilton component. (2) The vertex c_0 is internal in every Hamilton path on X union {c_0}; then 5ff05be1a5bc forces at least two crossings in every deletion two-cover of H-c_0 across the finer four-class partition induced by deleting c_0 from a Hamilton order of X+c_0.

## Body

Apply hamiltonian_enlargement_forces_crossing01 to v=c_0, A=V(X), and B=(V(C)-{c_0}) union V(D). Both A and B are nonempty and A+c_0 is Hamiltonian, so every two-cover of H-c_0 crosses the coarse cut A|B. This conclusion is unconditional on the position of c_0 in Hamilton orders of X+c_0.

Now split according to those Hamilton orders. If some Hamilton order has c_0 at an endpoint, apply 883bd2af7e73 in the matching orientation. It greedily absorbs consecutive vertices c_0,c_1,... into the Hamilton component until the first failed append and then supplies a tight triple reversing the current component-end edge, giving (1). If no Hamilton order places c_0 at an endpoint, then c_0 is permanently internal and 5ff05be1a5bc applies, giving the finer double-crossing conclusion (2). These two cases exhaust the Hamilton orders. Thus coarse crossing is common to both branches, rather than an alternative to greedy endpoint transport.