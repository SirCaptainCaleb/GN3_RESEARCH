# Every neutral four-to-six endpoint transfer is a fixed-pair swap of two disjoint Hamiltonian four-blocks

## Statement

Suppose a local four-side endpoint transfer is in the neutral m=6 equality case. Write the original state as A|P|Q with A a Hamiltonian four-side and P=(p_1,...,p_6). Put E={p_1,p_6} and B={p_2,p_3,p_4,p_5}. Then B is a Hamiltonian four-side, both B union E=P and A union E are Hamiltonian six-sets, A and B are disjoint, and the neutral move is exactly the pairwise repartition A|(B union E) -> B|(A union E), leaving Q fixed. Hence every edge of the neutral 4|6|6 transition graph is a fixed-pair swap between disjoint Hamiltonian four-blocks across a common two-vertex set E.

## Body

In the m=6 equality branch, P itself is the Hamiltonian six-set B union E, where B=(p_2,p_3,p_4,p_5) is its inherited interior tight four-path and E={p_1,p_6}. The equality conclusion says U=A union E is also Hamiltonian, and the legal neutral repartition replaces A|P by U|B. Reordering the two displayed components gives B|(A union E). Since A is disjoint from P, it is disjoint from B union E, hence in particular A and B are disjoint. Thus the move has the exact symmetric form A|(B union E) -> B|(A union E), with Q unchanged. No further hypothesis is used.