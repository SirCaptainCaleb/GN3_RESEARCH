# Two clean endpoint replacements on one component force a two-cover or doubled barriers at both ends

## Statement

Let H be a minimum counterexample, H-b=P|Q a deletion cover, and P=(p_0,...,p_m) with |P|>=4. Suppose there is a deletion cover of H-p_0 whose P-side is (b,p_1,...,p_m) with Q unchanged, and a deletion cover of H-p_m whose P-side is (p_0,...,p_{m-1},b) with Q unchanged. Then either H has a spanning two-cover, or all four triples (p_1,b,p_0), (p_1,p_0,b), (b,p_m,p_{m-1}), and (p_m,b,p_{m-1}) are tight. Since H is a minimum counterexample, the second alternative must hold.

## Body

Put R=(p_1,...,p_{m-1}), which has order at least two.

The original path P shows that both (p_0,R) and (R,p_m) are tight. The clean initial replacement shows (b,R) is tight, and the clean terminal replacement shows (R,b) is tight.

Apply the certified same-end extender theorem 7b9f6ae39813 to the core R with left extenders p_0,b and right extender p_m. Either H[V(P) union {b}] is Hamiltonian, or both (p_1,b,p_0) and (p_1,p_0,b) are tight.

Apply its symmetric form to R with right extenders p_m,b and left extender p_0. Either H[V(P) union {b}] is Hamiltonian, or both (b,p_m,p_{m-1}) and (p_m,b,p_{m-1}) are tight.

If H[V(P) union {b}] were Hamiltonian, that Hamilton path together with the unchanged path Q would be a spanning two-cover of H, impossible in a minimum counterexample. Hence both non-Hamiltonian alternatives hold simultaneously, yielding the four displayed tight triples. No cyclic permutation of a tight triple is used.