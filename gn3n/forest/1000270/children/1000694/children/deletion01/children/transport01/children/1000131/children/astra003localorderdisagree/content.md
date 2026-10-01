# Every order-eleven omission state has order disagreement inside both local deletion families

## Statement

Let H be a hypothetical order-eleven minimum counterexample and P|Q|(x) any spanning 5|5|1 state. Put R_P=P union {x} and R_Q=Q union {x}. For either side R, choose any four distinct good deletion labels d for which R-d is Hamiltonian, choose arbitrary Hamilton paths on those four five-sets, and pair them with the fixed opposite five-path. Among the resulting four exact deletion covers, some pair has relative-order disagreement on their common varying support. Thus both local support-compatible deletion families necessarily contain explicit order disagreement.

## Body

Fix a spanning omission state

P | Q | (x)

with |P|=|Q|=5.

Put

R_P=V(P) union {x}.

As in the certified order-eleven stress test 2ac31d8f3bb6, R_P is a non-Hamiltonian six-set, and its good-deletion set

G(R_P)={d in R_P : R_P-{d} is Hamiltonian}

has order at least four.

Choose any four distinct labels

d_1,d_2,d_3,d_4 in G(R_P).

For each i choose an arbitrary Hamilton path P_i on R_P-{d_i} and form the exact deletion cover

F_i = P_i | Q

of H-d_i.

The stress-test theorem shows that this family is pairwise compatible on component membership: for i != j, after restricting to H-{d_i,d_j}, both covers have exactly the same support classes

(R_P-{d_i,d_j}) | V(Q).

Normalize the untouched Q component to the same displayed Hamilton order in all four covers.

Suppose, for contradiction, that no pair F_i,F_j has relative-order disagreement on the varying common support R_P-{d_i,d_j}. Then every pair agrees both on component membership and on the relative orders of common vertices in each component. Hence the four chosen deletion covers are pairwise compatible in the pair-state sense.

They therefore form a K4 in the compatibility graph.

But the certified compatibility-density theorem compatdensity01 states that the compatibility graph of any chosen family of exact deletion covers in a counterexample is K4-free: four pairwise-compatible deletion covers would glue to a spanning two-cover of H.

Contradiction.

Therefore some pair F_i,F_j has relative-order disagreement inside the common varying support R_P-{d_i,d_j}. Since the opposite Q path was normalized identically, this is a genuine disagreement entirely internal to the bad six-set R_P.

The same argument with P,Q interchanged applies to

R_Q=V(Q) union {x}.

Hence every order-eleven omission state carries unavoidable relative-order disagreement inside each of its two local four-or-larger support-compatible deletion families.

This conclusion does not assume maximum path order five. It holds throughout the hypothetical order-eleven minimum-counterexample shell.
