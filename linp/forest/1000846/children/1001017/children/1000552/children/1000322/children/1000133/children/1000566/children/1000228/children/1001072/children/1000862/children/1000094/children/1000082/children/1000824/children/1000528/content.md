# A two-chord block reversal switches the entrance of a zero-slack witness

## Statement

Let
T_1,C_1,T_2,C_2,...,C_{c-1},T_c
be an alternating zero-slack witness as in b93769ee6fab, with T_c=e and final entrance port x∈e. Fix another port y∈e. Suppose for some 2<=j<=c-1 there are DXX connectors h joining y to a vertex of T_j and g joining T_{j-1} to T_{c-1} such that:
(i) the connector colors in the sequence below are all distinct;
(ii) at T_j the h-port differs from the port used by C_j;
(iii) at T_{j-1} the g-port differs from the port used by C_{j-2} when j>2;
(iv) at T_{c-1} the g-port differs from the port used by C_{c-2}.
Then there is a maximum alternating witness ending in e through y.

## Body

Consider the reordered triple sequence
T_1,T_2,...,T_{j-1},T_{c-1},T_{c-2},...,T_j,T_c.

Use the old connectors C_1,...,C_{j-2} on the initial segment, then g between T_{j-1} and T_{c-1}, then the old connectors C_{c-2},C_{c-3},...,C_j along the reversed middle block, and finally h from T_j to T_c.

Exactly two old connectors, C_{j-1} and C_{c-1}, are omitted and exactly two new connectors g,h are inserted. Therefore there are again c-1 connectors.

The stated port conditions guarantee that at each internal forest triple the incoming and outgoing connectors meet distinct vertices. The color condition guarantees that distinct connector hyperedges have distinct D-vertices. The forest triples themselves are pairwise disjoint, and each connector has X-endpoints only in its two adjacent triples.

Thus, by the same argument as 283f95e0c27e, the resulting alternating hyperedge sequence is a linear path of length 2c-1. Its last edge is T_c=e, and the penultimate connector h meets e at y. Therefore it is a maximum witness ending in e through the entrance label y.

If e were nonspecial with unique entrance x, no such compatible two-switch can exist for either y≠x.