# The neutral three-five forward exchange graph has no directed six-cycle

## Statement

In the setting of five_three_forward_exchange_cycle_bound01, the directed exchange graph has no directed cycle of length six. Consequently every directed cycle has length at least seven. More precisely, the six-cycle normal form of five_three_sixcycle_normalform01 would force a Hamiltonian 4|4 partition of W, contradicting the standing hypothesis that no such partition exists.

## Body

Assume a directed six-cycle and use five_three_sixcycle_normalform01. Thus W is the disjoint union {a,d} sqcup A_0 sqcup A_1 sqcup A_2, with each A_i a two-set, and the six Hamiltonian five-sets have the repeated cyclic good-pair/bad-pair pattern. In particular, for the fixed pair A_0, both five-sets a union A_0 union A_2 and d union A_0 union A_2 have A_2 as their bad-deletion pair. Therefore for every root r in {a,d} and every z in A_2, the four-set A_0 union {r,z} is non-Hamiltonian.

Apply the certified fixed-pair orientation-class theorem bd3c8d17ca06 to the fixed pair A_0. The exterior vertices split into two orientation classes, and any two vertices in the same class complete A_0 to a Hamiltonian four-set. Since each r in {a,d} forms a bad extension with each z in A_2, every root must lie in the orientation class opposite every vertex of A_2. Hence a and d lie in one common class and the two vertices of A_2 lie in the other. It follows that both A_0 union {a,d} and A_0 union A_2 are Hamiltonian.

Apply the same argument cyclically. For fixed pair A_1, the bad neighboring block is A_0, so A_1 union {a,d} and A_1 union A_0 are Hamiltonian. For fixed pair A_2, the bad neighboring block is A_1, so A_2 union {a,d} and A_2 union A_1 are Hamiltonian. In particular A_0 union {a,d} is Hamiltonian and its complementary four-set W-(A_0 union {a,d})=A_1 union A_2 is Hamiltonian. This is a Hamiltonian 4|4 partition of W, contradicting the hypothesis of five_three_forward_exchange_cycle_bound01. Therefore no directed six-cycle exists. Combined with the already certified/provisional cycle-bound theorem excluding lengths at most five, every directed cycle has length at least seven.