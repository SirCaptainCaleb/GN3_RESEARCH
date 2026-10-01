# Quadratic minima have no one- or two-vertex side, and a three-side forces crossed endpoint five-sets

## Statement

Let C=P_1|P_2|P_3 be a Phi-minimal trapped Astra-003 three-cover. If |V(C)|>=6, no component is a singleton. If |V(C)|>=9, every component has order at least three. Moreover, if X is a component of order three and P=(p_1,...,p_m) is another component with m>=6, then X union {p_1,p_2}, X union {p_1,p_m}, and X union {p_{m-1},p_m} are non-Hamiltonian, while X union {p_2,p_m} and X union {p_1,p_{m-1}} are Hamiltonian.

## Body

A singleton together with a path of order m>=3 admits the legal repartition (x,p_1)|(p_2,...,p_m), lowering Phi by 2m-4, so a Phi-minimal trapped cover on at least six vertices has no singleton. Likewise, if X has order two and P has order m>=4, any Hamilton path on X union {p_1} together with the inherited suffix P-p_1 gives a 3|(m-1) repartition lowering Phi by 2m-6. Thus on at least nine vertices every component has order at least three. Now suppose |X|=3 and m>=6. If any of X union {p_1,p_2}, X union {p_1,p_m}, or X union {p_{m-1},p_m} were Hamiltonian, combining it with the corresponding inherited contiguous remainder of P would strictly lower Phi; hence all three are non-Hamiltonian. Applying the certified fixed-three-path extension theorem to X with p_1,p_2,p_m forces X union {p_2,p_m} Hamiltonian, and applying it with p_1,p_{m-1},p_m forces X union {p_1,p_{m-1}} Hamiltonian.