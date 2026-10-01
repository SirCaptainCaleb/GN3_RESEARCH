# The unresolved one-split common-label branch has second-type pivots on both cores

## Statement

In the one-split toggle, choose Hamilton paths on R union {a} and S union {b} and apply compattogglewindows31 to the common failed label c. If either c-obstruction is first-type, then its four-vertex window is either Hamiltonian or the exceptional cyclic non-Hamiltonian K4; in the cyclic case every exterior fifth vertex extends that kernel to a Hamiltonian five-set. Consequently, after excluding these already-structured four-kernel outcomes, the only genuinely new c-synchronized residue is that c has a second-type failed-insertion pivot on both disjoint Hamiltonian supports R union {a} and S union {b}.

## Body

# Proof

By compattogglewindows31, c is noninsertable into the chosen Hamilton path on R union {a} and into the chosen Hamilton path on S union {b}, and each failed insertion has one of the two local types from insert01.

Suppose one of these two c-obstructions is first-type. The proof of the first-type insertion-kernel theorem in transport01 is purely local up to the subsequent complement statements: the first-type comparison 3-cycle on c and three consecutive path vertices determines a four-set X. If X is Hamiltonian, we have the first structured outcome. If X is non-Hamiltonian, the forcing argument uniquely identifies X with the exceptional cyclic K4 of smallset01. The cyclic-kernel extension theorem in smallset01 then says X union {d} is Hamiltonian for every exterior vertex d.

Thus any first-type c-window immediately supplies either a Hamiltonian four-set or a universal cyclic four-kernel.

Therefore, if neither c-window yields one of these outcomes, neither can be first-type. Both must be second-type obstructions from insert01.

Hence the unresolved common-label branch has c sitting at a certified second-type pivot on each of the two disjoint Hamiltonian supports R union {a} and S union {b}.
